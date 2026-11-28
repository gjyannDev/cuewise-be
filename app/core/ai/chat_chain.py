"""The provider chain (U3c): the chat models of `LLM_PROVIDERS`, in order, which the call helpers (`chat.py`,
`chat_stream.py`) try one after the other.

Why an explicit loop in our helpers and not LangChain's `model.with_fallbacks([...])`: the helpers already own what a
fallback must keep per attempt (the time left in the turn as the timeout, the token cap, the error mapping, one
Langfuse generation, the `RetryPolicy` backoff). `.with_fallbacks()` would run each branch with none of that.

Only transport errors (timeout, 429, 5xx: `LLMError.retryable`) move a call to the next provider. A rejected request
(bad key) raises at once, so a misconfigured primary is not hidden; a bad reply is a content problem and stays in the
caller's own attempt loop (which runs through the same chain).
"""

from dataclasses import dataclass

from langchain_core.language_models import BaseChatModel

from app.core.logging import Logger

from .provider import LLMError


@dataclass(frozen=True)
class ChatChain:
    """Ordered `(provider name, chat model)` pairs; the first is the primary."""

    members: tuple[tuple[str, BaseChatModel], ...]

    def __post_init__(self) -> None:
        if not self.members:
            raise ValueError("a ChatChain needs at least one chat model")


def as_chain(model: BaseChatModel | ChatChain) -> ChatChain:
    """A bare chat model (tests, a single provider) is a chain of one."""
    return model if isinstance(model, ChatChain) else ChatChain((("default", model),))


def log_switch(logger: Logger, previous: str, name: str, error: LLMError) -> None:
    """One event per hand-over: provider names and the error class only, never text."""
    logger.warning("llm_provider_switch", from_provider=previous, to_provider=name, reason=type(error).__name__)
