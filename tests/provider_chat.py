"""A chat model served by old-style `FakeProvider`s, for tests while U3b1 moves the interview calls (gone with them).

Tests written against `FakeProvider` (scripts, `FakeStream`s, `.calls`, `.budgets`, `.cancelled`, `on_call`) keep
them: the chat model hands each call (`invoke` or `astream`) to the provider its router picks and turns the provider's
reply, chunks or error into the chat model's. The call's timeout (the helper's per-attempt or whole-stream limit) is
recorded as the provider's budget.
"""

from collections.abc import AsyncIterator, Callable
from contextlib import aclosing
from typing import Any

import anyio
from langchain_core.messages import AIMessage, AIMessageChunk, BaseMessage
from langchain_core.outputs import ChatGeneration, ChatGenerationChunk, ChatResult
from pydantic import PrivateAttr

from app.core.ai.chat_fake import FakeChatModel, fake_reply
from app.core.ai.provider import ChatMessage, LLMResult
from tests.provider_fakes import FakeProvider

_ROLES = {"system": "system", "human": "user", "ai": "assistant"}
# The old layer's finish reasons in Gemini's words, so the chat helper maps them back.
_VENDOR_FINISH = {"stop": "STOP", "length": "MAX_TOKENS"}


async def closed_soon(is_closed: Callable[[], bool], ticks: int = 100) -> bool:
    """Whether a vendor stream closed within `ticks` event-loop turns after the caller closed `stream_chat`.

    LangChain's `astream` doesn't close the model's own stream when its caller stops early; asyncio's async-generator
    finalizer does, a few turns later (about 15 with the Gemini integration, U3b1 learnings). So a test of a client
    leaving waits for that, bounded, instead of reading the flag at once."""
    for _ in range(ticks):
        if is_closed():
            return True
        await anyio.lowlevel.checkpoint()
    return is_closed()


def _message(result: LLMResult, text: str) -> AIMessage:
    message = fake_reply(
        text,
        input_tokens=result.prompt_tokens,
        output_tokens=result.completion_tokens,
        reasoning_tokens=result.reasoning_tokens,
        cached_tokens=result.cached_tokens,
        finish_reason=_VENDOR_FINISH.get(result.finish_reason or "stop", "STOP"),
    )
    message.response_metadata["model_name"] = result.model
    return message


class ProviderChatModel(FakeChatModel):
    """`route` is one provider, or a function from the call's system prompt to the provider that serves it."""

    _route: Any = PrivateAttr(default=None)

    def __init__(self, route: FakeProvider | Callable[[str], FakeProvider], **kwargs: Any):
        super().__init__(**kwargs)
        self._route = route if callable(route) else (lambda _system: route)

    def _provider_call(self, messages: list[BaseMessage]) -> tuple[FakeProvider, list[ChatMessage], dict[str, Any]]:
        provider = self._route(messages[0].text if messages else "")
        ours = [ChatMessage(role=_ROLES[m.type], content=m.text) for m in messages]  # pyright: ignore[reportArgumentType]
        limits = {"max_tokens": self.max_output_tokens or 0, "temperature": self.temperature, "budget_seconds": self.timeout}
        return provider, ours, limits

    def _generate(
        self, messages: list[BaseMessage], stop: list[str] | None = None, run_manager: Any = None, **kwargs: Any
    ) -> ChatResult:
        provider, ours, limits = self._provider_call(messages)
        result = provider.complete(ours, **limits)
        return ChatResult(generations=[ChatGeneration(message=_message(result, result.text))])

    async def _astream(
        self, messages: list[BaseMessage], stop: list[str] | None = None, run_manager: Any = None, **kwargs: Any
    ) -> AsyncIterator[ChatGenerationChunk]:
        provider, ours, limits = self._provider_call(messages)
        # Closing this stream closes the provider's, so its `cancelled` flag shows a client that left.
        async with aclosing(provider.stream(ours, **limits)) as items:
            async for item in items:
                if isinstance(item, LLMResult):
                    # Usage and the finish reason on a last, empty chunk, as Gemini's stream ends.
                    final = _message(item, "")
                    chunk = AIMessageChunk(
                        content="", usage_metadata=final.usage_metadata, response_metadata=final.response_metadata
                    )
                else:
                    chunk = AIMessageChunk(content=item)
                yield ChatGenerationChunk(message=chunk)
