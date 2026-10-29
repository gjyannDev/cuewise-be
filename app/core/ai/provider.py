"""The LLM contract every feature codes against: message/result types, typed errors, the provider protocol.

Nothing here knows about HTTP or a vendor, so a controller can handle "the LLM failed" without importing httpx.
"""

from collections.abc import Sequence
from typing import ClassVar, Literal, Protocol

from pydantic import BaseModel, ConfigDict


class ChatMessage(BaseModel):
    """One turn of the conversation sent to the model. The model keeps no memory: every call sends them all."""

    model_config = ConfigDict(frozen=True)

    role: Literal["system", "user", "assistant"]
    content: str


class LLMResult(BaseModel):
    text: str
    model: str
    # None when the provider doesn't report usage; never guessed.
    prompt_tokens: int | None
    completion_tokens: int | None
    latency_ms: int
    # "stop" = finished on its own, "length" = cut off by max_tokens.
    finish_reason: str | None
    attempts: int


class LLMError(Exception):
    """Base for every provider failure. `retryable` marks faults that may pass on their own (timeouts, 429, 5xx)."""

    retryable: ClassVar[bool] = False

    def __init__(self, message: str, *, status_code: int | None = None, finish_reason: str | None = None):
        super().__init__(message)
        self.status_code = status_code
        # "length" here means the token cap ran out before any reply text (e.g. a reasoning model still thinking).
        self.finish_reason = finish_reason
        # Filled in by the provider once it stops trying, so callers can log them.
        self.attempts = 1
        self.latency_ms = 0


class LLMTimeoutError(LLMError):
    retryable = True


class LLMRateLimitError(LLMError):
    retryable = True


class LLMServerError(LLMError):
    """5xx or a dropped connection: the provider's side failed."""

    retryable = True


class LLMRequestError(LLMError):
    """Other 4xx (bad key, bad request): retrying sends the same broken request again."""


class LLMBadResponseError(LLMError):
    """A 200 whose body is unusable (not JSON, no choices, blank text). Not transient, so not retried."""


class LLMProvider(Protocol):
    def complete(
        self,
        messages: Sequence[ChatMessage],
        *,
        max_tokens: int,
        temperature: float | None = None,
        # Lowers the total time budget for this call (a caller's own deadline); it never raises it.
        budget_seconds: float | None = None,
    ) -> LLMResult: ...

    def close(self) -> None: ...
