from __future__ import annotations

import json
import math
from collections.abc import Generator
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import ClassVar, Literal, Self, TypedDict

import torch
from accelerate import init_on_device, load_checkpoint_in_model
from einops import rearrange
from torch import nn
from transformers import Lfm2Config, Lfm2Model
from transformers.models.lfm2.modeling_lfm2 import Lfm2HybridConvCache

from liquid_audio.model.conformer.encoder import ConformerEncoder, ConformerEncoderConfig
from liquid_audio.model.mlp import MLP
from liquid_audio.model.transformer import MHA, RawLMBackbone, SharedEmbedding, StandardBlock
from liquid_audio.processor import PreprocessorConfig
from liquid_audio.utils import LFMModality, get_model_dir, mel2emb_len, module_exists


class LFM2_HFConfig(TypedDict):
    pretrained_model_name_or_path: str
    revision: str


@dataclass(kw_only=True)
class LFM2AudioConfig:
    architectures: list[str]  # for huggingface compatibility

    codebooks: int
    tie_audio_embeddings: bool

    semantic_codebook_factor: float
    codebook_weight: Literal["log", "linear"]

    interleaved_n_text: int
    interleaved_n_audio: int

    preprocessor: PreprocessorConfig
    encoder: ConformerEncoderConfig
    lfm: Lfm2Config
    depthformer: DepthformerConfig


@dataclass(kw_only=True)
class DepthformerConfig:
    layers: int
    dim: int
    tie: bool


class LFM2AudioModel(nn.Module):
    audio_vocab_size: ClassVar[int] = 2048 + 1  # Includes +1 for EOAudio

    def __init__(
        self,
        conf: LFM2AudioConfig,
    ):
        super().__init__()

        self.conf = conf
        self.codebooks = conf.codebooks

        ## LFM2 ##
        self.lfm = Lfm2Model(conf.lfm)

        ## Audio encoder ##
        self.conformer = ConformerEncoder(**asdict(conf.encoder))
        self.audio_adapter = MLP(self.conformer._feat_out, self.lfm.config.hidden_size, [self.lfm.config.hidden_size])

        ## Depthformer ##
        self.depthformer_layers = conf.depthformer.layers
        self.depthformer_dim = conf.depthformer.dim
        self.depthformer_tie = conf.depthformer.tie
        self.audio_embedding = SharedEmbedding(
            dim=self.lfm.config.hidden_size,
            vocab_size=self.audio_vocab_size * self.conf.codebooks,
            embed_init_scale=1.0,
            norm_eps=0.00001,
            tie_embedding=conf.tie_audio_embeddings,
        )

        self.codebook_offsets: torch.Tensor
        self.register_buffer("codebook_offsets", torch.arange(self.conf.codebooks) * self.audio_vocab_size)

        self.audio_loss_weights: torch.Tensor
        if conf.codebook_weight == "log":
            weights = (torch.linspace(1, 0, self.codebooks) * math.log(conf.semantic_codebook_factor)).exp()
        else:
            weights = torch.ones((self.codebooks,))
            weights[0] *= conf.semantic_codebook_factor
        self.register_buffer(
            "audio_loss_weights",
            weights,
        )

        scale = 1 / math.sqrt(2 * self.depthformer_layers)

        layers = [
            StandardBlock(MHA(self.depthformer_dim, out_init_scale=scale), out_init_scale=scale)
            for _ in range(self.depthformer_layers)
        ]
        self.depthformer = RawLMBackbone(layers, has_embedding=False)

        self.depth_linear = nn.Linear(self.lfm.config.hidden_size, self.depthformer_dim * self.codebooks)
        self.depth_embeddings = nn.ModuleList(
            [
                SharedEmbedding(
                    dim=self.depthformer_dim,
                    vocab_size=self.audio_vocab_size,
                    tie_embedding=self.depthformer_tie,
                )
                for _ in range(self.codebooks)
            ]
        )

    @classmethod
    def from_pretrained(
        cls,
        repo_id: str | Path,
        *,
        revision: str | None = None,
        dtype: torch.dtype = torch.bfloat16,
        device: torch.device | str = "cuda",
    ) -> Self:
        cache_path = get_model_dir(repo_id, revision=revision)

        with (cache_path / "config.json").open() as f:
            config = json.load(f)

        conf = LFM2AudioConfig(
            lfm=Lfm2Config(**config.pop("lfm")),
            encoder=ConformerEncoderConfig(**config.pop("encoder")),
            depthformer=DepthformerConfig(**config.pop("depthformer")),
            **config,
        )

        if isinstance(device, str):
            device = torch.device(device)

        with init_on_device(device, include_buffers=True):
            model = cls(conf).to(device=device, dtype=dtype)

        if module_exists("flash_attn"):
            model.lfm.set_attn_implementation("flash_attention_2")
        else:
            model.lfm.set_attn_implementation("sdpa")

        load_checkpoint_in_model(model, cache_path)

        return model

    @torch.no_grad()
    def generate_sequential(
        self,
        *,
        text: torch.Tensor,
        audio_in: torch.Tensor,
        audio_in_lens: torch.Tensor,
        audio_out: torch.Tensor,
        modality_flag: torch.Tensor,
        max_new_tokens: int = 20,
        text_temperature: float | None = None,
        text_top_k: int | None = None,
        audio_temperature: float | None = None,
        audio_top_k: int | None = None,
    ) -> Generator[torch.Tensor, None, None]:
        in_emb = self._prefill(
            text=text,
            audio_in=audio_in,
            audio_in_lens=audio_in_lens,
            audio_out=audio_out,
            modality_flag=modality_flag,
        )

        current_modality: LFMModality = LFMModality.TEXT
        cache: Lfm2HybridConvCache | None = None

        for _ in range(max_new_tokens):
            # breakpoint()
            lfm_out = self.lfm(
                inputs_embeds=in_emb,
                past_key_values=cache,
                use_cache=True,
            )
            output_embeddings = lfm_out.last_hidden_state
            cache = lfm_out.past_key_values

            if current_modality == LFMModality.TEXT:
                text_logits = nn.functional.linear(output_embeddings[0, -1], self.lfm.embed_tokens.weight)
                next_token = self._sample_text_token(text_logits, temperature=text_temperature, top_k=text_top_k)
                yield next_token

                if next_token == 128:  # <|audio_start|>
                    current_modality = LFMModality.AUDIO_OUT
                if next_token == 7:  # <|im_end|>
                    break

                in_emb = self.lfm.embed_tokens(next_token)[None, :]

            elif current_modality == LFMModality.AUDIO_OUT:
                next_token = self._sample_audio_frame(
                    output_embeddings[0, -1],
                    temperature=audio_temperature,
                    top_k=audio_top_k,
                )

                if next_token[0] == 2048:
                    next_token[:] = 2048
                    current_modality = LFMModality.TEXT

                yield next_token
                in_emb = self.audio_embedding(next_token + self.codebook_offsets).sum(0)[None, None, :]

    @torch.no_grad()
    def generate_interleaved(
        self,
        *,
        text: torch.Tensor,
        audio_in: torch.Tensor,
        audio_in_lens: torch.Tensor,
        audio_out: torch.Tensor,
        modality_flag: torch.Tensor,
        max_new_tokens: int = 20,
        text_temperature: float | None = None,
        text_top_k: int | None = None,
        audio_temperature: float | None = None,
        audio_top_k: int | None = None,
    ) -> Generator[torch.Tensor, None, None]:
        in_emb = self._prefill(
            text=text,
            audio_in=audio_in,
            audio_in_lens=audio_in_lens,
            audio_out=audio_out,
            modality_flag=modality_flag,
        )

        current_modality: LFMModality = LFMModality.TEXT
        modality_left: int = self.conf.interleaved_n_text
        cache: Lfm2HybridConvCache | None = None

        text_done: bool = False

        for _ in range(max_new_tokens):
            modality_left -= 1
            lfm_out = self.lfm(
                inputs_embeds=in_emb,
                past_key_values=cache,
                use_cache=True,
            )
            output_embeddings = lfm_out.last_hidden_state
            cache = lfm_out.past_key_values

            if current_modality == LFMModality.TEXT:
                text_logits = nn.functional.linear(output_embeddings[0, -1], self.lfm.embed_tokens.weight)
                next_token = self._sample_text_token(text_logits, temperature=text_temperature, top_k=text_top_k)

                if next_token == 7:  # <|im_end|>
                    break

                yield next_token

                if next_token == 130:  # <|text_end|>
                    text_done = True
                if not modality_left or text_done:
                    current_modality = LFMModality.AUDIO_OUT
                    modality_left = self.conf.interleaved_n_audio

                in_emb = self.lfm.embed_tokens(next_token)[None, :]

            elif current_modality == LFMModality.AUDIO_OUT:
                next_token = self._sample_audio_frame(
                    output_embeddings[0, -1],
                    temperature=audio_temperature,
                    top_k=audio_top_k,
                )

                if not modality_left and not text_done:
                    current_modality = LFMModality.TEXT
                    modality_left = self.conf.interleaved_n_text

                if next_token[0] == 2048:
                    next_token[:] = 2048
                    current_modality = LFMModality.TEXT

                yield next_token
                in_emb = self.audio_embedding(next_token + self.codebook_offsets).sum(0)[None, None, :]

    def _prefill(
        self,
        *,
        text: torch.Tensor,
        audio_in: torch.Tensor,
        audio_in_lens: torch.Tensor,
        audio_out: torch.Tensor,
        modality_flag: torch.Tensor,
    ) -> torch.Tensor:
        ## Sanity check
        assert len(text.shape) == 2
        assert len(audio_in.shape) == 2
        assert len(audio_in_lens.shape) == 1
        assert len(audio_out.shape) == 2
        assert len(modality_flag.shape) == 2

        assert text.shape[0] == 1

        assert audio_in.shape[0] == 128
        assert audio_out.shape[0] >= self.codebooks
        assert modality_flag.shape[0] == 1

        assert (modality_flag == LFMModality.TEXT).sum() == text.shape[1]
        assert (modality_flag == LFMModality.AUDIO_OUT).sum() == audio_out.shape[1]
        assert (modality_flag == LFMModality.AUDIO_IN).sum() == mel2emb_len(audio_in_lens).sum()
        assert audio_in.shape[1] == audio_in_lens.sum()

        # Text embeddings
        text_emb = self.lfm.embed_tokens(text[0])
        text_mask = modality_flag == LFMModality.TEXT

        # Audio-in embeddings
        ## Batch and pad
        audio_in_list = audio_in.mT.split(audio_in_lens.tolist())
        if audio_in_list:
            padded_audio_in = nn.utils.rnn.pad_sequence(audio_in_list, batch_first=True)
        else:
            padded_audio_in = text_emb.new_empty((0, 8 + 1, 128))

        ## Encode
        audio_enc, audio_in_len = self.conformer(padded_audio_in.mT, audio_in_lens)

        ## Unbatch, unpad
        len_mask = torch.arange(audio_enc.shape[-1], device=audio_enc.device).unsqueeze(0) < audio_in_len.unsqueeze(1)
        audio_enc_concatenated = audio_enc.mT[len_mask]

        ## Adapt
        audio_in_emb = self.audio_adapter(audio_enc_concatenated)
        audio_in_mask = modality_flag == LFMModality.AUDIO_IN
        assert audio_in_emb.shape[0] == audio_in_mask.sum()

        # Audio-out embeddings
        offset_audio_tokens = audio_out[: self.codebooks] + self.codebook_offsets.unsqueeze(1)
        audio_out_emb = self.audio_embedding(offset_audio_tokens).sum(0)
        audio_out_mask = modality_flag == LFMModality.AUDIO_OUT
        assert audio_out_emb.shape[0] == audio_out_mask.sum()

        # Assemble LFM input
        B, L, D = *modality_flag.shape, self.lfm.config.hidden_size

        in_emb = text_emb.new_empty((B, L, D))

        in_emb[text_mask] = text_emb
        in_emb[audio_in_mask] = audio_in_emb
        in_emb[audio_out_mask] = audio_out_emb

        return in_emb

    def _sample_text_token(
        self, logits: torch.Tensor, *, temperature: float | None = None, top_k: int | None = None
    ) -> torch.Tensor:
        greedy = temperature is None or temperature <= 0 or top_k == 1
        if greedy:
            next_token = logits.argmax(keepdim=True)
        else:
            assert isinstance(temperature, float) and temperature > 0
            logits /= temperature
            if top_k is not None:
                min_score = torch.topk(logits, top_k).values[-1]
                to_remove = logits < min_score
                logits = torch.masked_fill(logits, to_remove, -float("inf"))
            probs = logits.softmax(0)
            next_token = torch.multinomial(probs, 1)

        return next_token

    def _sample_audio_frame(
        self,
        embedding: torch.Tensor,  # lfm_dim sized vecto
        *,
        temperature: float | None = None,
        top_k: int | None = None,
    ) -> torch.Tensor:
        greedy = temperature is None or temperature <= 0 or top_k == 1
        depthformer_in = rearrange(self.depth_linear(embedding), "(C D) -> C D", C=self.codebooks, D=self.depthformer_dim)
        depthformer_token = torch.zeros_like(depthformer_in[0])
        cache = None

        out_tokens: list[torch.Tensor] = []
        for i in range(self.codebooks):
            cur_depthformer_input = depthformer_in[i] + depthformer_token
            depthformer_out, cache = self.depthformer.forward_cached(cur_depthformer_input[None, None, :], cache)
            depthformer_logits = self.depth_embeddings[i].get_logits(depthformer_out.squeeze())  # type: ignore[operator]

            if greedy:
                next_token = depthformer_logits.argmax(keepdim=True)
            else:
                assert isinstance(temperature, float) and temperature > 0
                depthformer_logits /= temperature
                if top_k is not None:
                    min_score = torch.topk(depthformer_logits, top_k).values[-1]
                    to_remove = depthformer_logits < min_score
                    depthformer_logits = torch.masked_fill(depthformer_logits, to_remove, -float("inf"))
                probs = depthformer_logits.softmax(0)
                next_token = torch.multinomial(probs, 1)

            out_tokens.append(next_token)
            depthformer_token = self.depth_embeddings[i](next_token).squeeze()

        return torch.cat(out_tokens)
