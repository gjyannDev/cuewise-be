"""Test doubles for the Transcriber, SpeechSynthesizer and Embedder: scripted replies or errors, record every call. No
network. (The scripted LLM double is `tests/provider_fakes.py`.)"""

import hashlib
import random
import time
from collections import deque
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import NamedTuple

from .embedder import EmbeddingKind, EmbeddingResult
from .provider import LLMError, LLMTimeoutError
from .synthesizer import SynthesisResult
from .transcriber import TranscriptionResult


class FakeTranscriber:
    """Scripted transcripts (text, a full result, or an error), one per call; records each call's audio, type and
    keyterms."""

    DEFAULT_TEXT = "I would cache the results and invalidate them on write."

    def __init__(self, replies: Iterable[str | TranscriptionResult | LLMError] = (), *, duration: float | None = 12.5):
        self._replies = deque(replies)
        self._duration = duration
        self.calls: list[tuple[bytes, str, tuple[str, ...]]] = []

    async def transcribe(
        self, audio: bytes, *, content_type: str, keyterms: Sequence[str] = ()
    ) -> TranscriptionResult:
        self.calls.append((audio, content_type, tuple(keyterms)))
        reply = self._replies.popleft() if self._replies else self.DEFAULT_TEXT
        if isinstance(reply, LLMError):
            raise reply
        if isinstance(reply, TranscriptionResult):
            return reply
        return TranscriptionResult(
            text=reply, duration_seconds=self._duration, model="fake-stt", latency_ms=0, attempts=1
        )

    async def aclose(self) -> None:
        pass


class FakeSynthesizer:
    """Scripted clips (bytes, a full result, or an error), one per call; records each call's text. Without a script,
    every call returns a few bytes of `audio/mpeg`."""

    DEFAULT_AUDIO = b"ID3fake-mp3"

    def __init__(self, replies: Iterable[bytes | SynthesisResult | LLMError] = (), *, content_type: str = "audio/mpeg"):
        self._replies = deque(replies)
        self._content_type = content_type
        self.calls: list[str] = []

    async def synthesize(self, text: str) -> SynthesisResult:
        self.calls.append(text)
        reply = self._replies.popleft() if self._replies else self.DEFAULT_AUDIO
        if isinstance(reply, LLMError):
            raise reply
        if isinstance(reply, SynthesisResult):
            return reply
        return SynthesisResult(
            audio=reply,
            content_type=self._content_type,
            model="fake-tts",
            characters=len(text),
            latency_ms=0,
            attempts=1,
        )

    async def aclose(self) -> None:
        pass


class EmbedCall(NamedTuple):
    texts: tuple[str, ...]
    kind: EmbeddingKind
    budget_seconds: float | None


class FakeEmbedder:
    """Deterministic vectors (seeded by each text), or scripted ones per text so a test can fix which note is nearest.
    Scripted errors are raised one per call before any vector; `delay` waits like a slow vendor, but never past the
    call's budget (then it times out, as the real client would)."""

    def __init__(
        self,
        vectors: Mapping[str, Sequence[float]] | None = None,
        *,
        dimensions: int = 768,
        model: str = "fake-embedding",
        errors: Iterable[LLMError] = (),
        delay: float = 0.0,
        sleep: Callable[[float], None] = time.sleep,
    ):
        self._vectors = dict(vectors or {})
        self._dimensions = dimensions
        self._model = model
        self._errors = deque(errors)
        self._delay = delay
        self._sleep = sleep
        self.calls: list[EmbedCall] = []

    @property
    def model(self) -> str:
        return self._model

    @property
    def dimensions(self) -> int:
        return self._dimensions

    def embed(
        self, texts: Sequence[str], *, kind: EmbeddingKind, budget_seconds: float | None = None
    ) -> EmbeddingResult:
        self.calls.append(EmbedCall(tuple(texts), kind, budget_seconds))
        if self._delay:
            if budget_seconds is not None and self._delay > budget_seconds:
                self._sleep(budget_seconds)
                raise LLMTimeoutError("Embedding request timed out")
            self._sleep(self._delay)
        if self._errors:
            raise self._errors.popleft()
        return EmbeddingResult(
            vectors=[list(self._vectors[t]) if t in self._vectors else self._seeded(t) for t in texts],
            model=self._model,
            input_tokens=None,
            latency_ms=0,
            attempts=1,
        )

    def close(self) -> None:
        pass

    def _seeded(self, text: str) -> list[float]:
        rng = random.Random(hashlib.sha256(text.encode()).digest())
        return [rng.uniform(-1, 1) for _ in range(self._dimensions)]
