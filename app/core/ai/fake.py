"""Test double for LLMProvider: scripted replies or errors, records every call. Never touches the network."""

from collections import deque
from collections.abc import Callable, Iterable, Sequence

from .context import CHARS_PER_TOKEN
from .provider import ChatMessage, LLMError, LLMResult, ReasoningEffort


class FakeProvider:
    DEFAULT_REPLY = "Thanks, that's a clear answer."

    def __init__(
        self,
        replies: Iterable[str | LLMResult | LLMError] = (),
        *,
        on_call: Callable[[], None] | None = None,
        # Used once the scripted replies run out; a callable gives each call its own text (e.g. unique questions).
        default: str | Callable[[], str] = DEFAULT_REPLY,
    ):
        self._replies = deque(replies)
        self._on_call = on_call
        self._default = default
        self.calls: list[list[ChatMessage]] = []
        self.budgets: list[float | None] = []
        self.reasoning_efforts: list[ReasoningEffort | None] = []

    def complete(
        self,
        messages: Sequence[ChatMessage],
        *,
        max_tokens: int,
        temperature: float | None = None,
        budget_seconds: float | None = None,
        reasoning_effort: ReasoningEffort | None = None,
    ) -> LLMResult:
        self.calls.append(list(messages))
        self.budgets.append(budget_seconds)
        self.reasoning_efforts.append(reasoning_effort)
        if self._on_call:
            self._on_call()
        if self._replies:
            reply = self._replies.popleft()
        else:
            reply = self._default() if callable(self._default) else self._default
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
