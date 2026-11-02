"""Test double for LLMProvider: scripted replies or errors, records every call. Never touches the network."""

import re
from collections import deque
from collections.abc import AsyncGenerator, Callable, Iterable, Mapping, Sequence
from typing import NamedTuple

import anyio

from .context import CHARS_PER_TOKEN
from .provider import ChatMessage, LLMError, LLMResult, ReasoningEffort


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
