"""Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or errors, record every call. No network."""

import hashlib
import random
import re
import time
from collections import deque
from collections.abc import AsyncGenerator, Callable, Iterable, Mapping, Sequence
from typing import NamedTuple

import anyio

from .context import CHARS_PER_TOKEN
from .embedder import EmbeddingKind, EmbeddingResult
from .provider import ChatMessage, LLMError, LLMResult, LLMTimeoutError, ReasoningEffort
from .transcriber import TranscriptionResult


class FakeStream(NamedTuple):
    """A scripted streamed reply: these chunks (each after `delay` seconds), then `error` if given, else the result."""

    chunks: Sequence[str]
    error: LLMError | None = None
    delay: float = 0.0


Reply = str | LLMResult | LLMError | FakeStream


class FakeProvider:
    DEFAULT_REPLY = "Thanks, that's a clear answer."

    def __init__(
        self,
        replies: Iterable[Reply] = (),
        *,
        on_call: Callable[[], None] | None = None,
        # Used once the scripted replies run out; a callable gives each call its own text (e.g. unique questions).
        default: str | Callable[[], str] = DEFAULT_REPLY,
        # Rewrites a text reply before it is streamed (a test can script one reply for both a JSON and a streamed
        # prompt format).
        stream_format: Callable[[str], str] | None = None,
    ):
        self._replies = deque(replies)
        self._on_call = on_call
        self._default = default
        self._stream_format = stream_format
        self.calls: list[list[ChatMessage]] = []
        self.budgets: list[float | None] = []
        self.reasoning_efforts: list[ReasoningEffort | None] = []
        # Set when a stream was closed (or cancelled) before it finished: the call a client walked away from.
        self.cancelled = False

    def complete(
        self,
        messages: Sequence[ChatMessage],
        *,
        max_tokens: int,
        temperature: float | None = None,
        budget_seconds: float | None = None,
        reasoning_effort: ReasoningEffort | None = None,
        # Labels for tracing only (task, prompt_version, ...); providers ignore them, TracingProvider records them.
        trace_labels: Mapping[str, str | int | None] | None = None,
    ) -> LLMResult:
        reply = self._next(messages, budget_seconds, reasoning_effort)
        if isinstance(reply, FakeStream):
            if reply.error is not None:
                raise reply.error
            reply = "".join(reply.chunks)
        if isinstance(reply, LLMError):
            raise reply
        return reply if isinstance(reply, LLMResult) else self._result(reply, messages)

    async def stream(
        self,
        messages: Sequence[ChatMessage],
        *,
        max_tokens: int,
        temperature: float | None = None,
        budget_seconds: float | None = None,
        reasoning_effort: ReasoningEffort | None = None,
        # Labels for tracing only (task, prompt_version, ...); providers ignore them, TracingProvider records them.
        trace_labels: Mapping[str, str | int | None] | None = None,
    ) -> AsyncGenerator[str | LLMResult]:
        """A text reply is streamed word by word; a FakeStream as scripted. An LLMError fails before any chunk."""
        reply = self._next(messages, budget_seconds, reasoning_effort)
        if isinstance(reply, LLMError):
            raise reply
        if isinstance(reply, FakeStream):
            script = reply
        else:
            text = reply.text if isinstance(reply, LLMResult) else reply
            if self._stream_format is not None:
                text = self._stream_format(text)
                reply = text
            script = FakeStream(re.findall(r"\S+\s*|\s+", text))
        finished = False
        try:
            for chunk in script.chunks:
                if script.delay:
                    await anyio.sleep(script.delay)
                yield chunk
            if script.error is not None:
                script.error.after_output = bool(script.chunks)
                finished = True
                raise script.error
            finished = True
            yield reply if isinstance(reply, LLMResult) else self._result("".join(script.chunks), messages)
        finally:
            if not finished:
                self.cancelled = True

    def close(self) -> None:
        pass

    async def aclose(self) -> None:
        pass

    def _next(
        self, messages: Sequence[ChatMessage], budget_seconds: float | None, reasoning_effort: ReasoningEffort | None
    ) -> Reply:
        self.calls.append(list(messages))
        self.budgets.append(budget_seconds)
        self.reasoning_efforts.append(reasoning_effort)
        if self._on_call:
            self._on_call()
        if self._replies:
            return self._replies.popleft()
        return self._default() if callable(self._default) else self._default

    @staticmethod
    def _result(text: str, messages: Sequence[ChatMessage]) -> LLMResult:
        return LLMResult(
            text=text,
            model="fake-model",
            prompt_tokens=sum(len(m.content) for m in messages) // CHARS_PER_TOKEN,
            completion_tokens=len(text) // CHARS_PER_TOKEN,
            latency_ms=0,
            finish_reason="stop",
            attempts=1,
        )


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
