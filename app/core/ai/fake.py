"""Test double for LLMProvider: scripted replies or errors, records every call. Never touches the network."""

from collections import deque
from collections.abc import Callable, Iterable, Sequence

from .provider import ChatMessage, LLMError, LLMResult

# Rough rule of thumb (~4 characters per token for English); real counts come from the provider's `usage`.
CHARS_PER_TOKEN = 4


class FakeProvider:
    DEFAULT_REPLY = "Thanks, that's a clear answer."

    def __init__(
        self,
        replies: Iterable[str | LLMResult | LLMError] = (),
        *,
        on_call: Callable[[], None] | None = None,
    ):
        self._replies = deque(replies)
        self._on_call = on_call
        self.calls: list[list[ChatMessage]] = []

    def complete(
        self, messages: Sequence[ChatMessage], *, max_tokens: int, temperature: float | None = None
    ) -> LLMResult:
        self.calls.append(list(messages))
        if self._on_call:
            self._on_call()
        reply = self._replies.popleft() if self._replies else self.DEFAULT_REPLY
        if isinstance(reply, LLMError):
            raise reply
        if isinstance(reply, LLMResult):
            return reply
        return LLMResult(
            text=reply,
            model="fake-model",
            prompt_tokens=sum(len(m.content) for m in messages) // CHARS_PER_TOKEN,
            completion_tokens=len(reply) // CHARS_PER_TOKEN,
            latency_ms=0,
            finish_reason="stop",
            attempts=1,
        )

    def close(self) -> None:
        pass
