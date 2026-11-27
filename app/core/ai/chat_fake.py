"""A LangChain chat model for tests (spec FR6): scripted replies or errors, every call recorded. No network.

It stands in for `ChatGoogleGenerativeAI` behind the call helper in `chat.py`, so it behaves like it where the helper
relies on it: replies are `AIMessage`s with `usage_metadata` and a `finish_reason`, per-call kwargs (`timeout`,
`generation_config`) arrive through `bind`, and `with_structured_output(..., include_raw=True)` parses JSON text with
the same shape of result (`raw`, `parsed`, `parsing_error`) as Gemini's `json_schema` method.
"""

from collections import deque
from collections.abc import AsyncIterator, Iterable
from operator import itemgetter
from typing import Any

import anyio
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, AIMessageChunk, BaseMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.outputs import ChatGeneration, ChatGenerationChunk, ChatResult
from langchain_core.runnables import Runnable, RunnablePassthrough
from pydantic import BaseModel, PrivateAttr

# A streamed reply (`fake_chunks`): its chunks in order, with an exception where the stream breaks.
FakeStreamReply = list[AIMessageChunk | BaseException]
FakeChatReply = str | AIMessage | BaseException | FakeStreamReply


def fake_reply(
    text: str,
    *,
    input_tokens: int | None = 10,
    output_tokens: int | None = 5,
    reasoning_tokens: int | None = None,
    cached_tokens: int | None = None,
    finish_reason: str = "STOP",
) -> AIMessage:
    """An AIMessage shaped like Gemini's: usage in `usage_metadata` (None = the vendor reported none)."""
    message = AIMessage(text, response_metadata={"finish_reason": finish_reason, "model_name": "fake-chat"})
    if input_tokens is not None and output_tokens is not None:
        usage: dict[str, Any] = {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
        }
        if reasoning_tokens is not None:
            usage["output_token_details"] = {"reasoning": reasoning_tokens}
        if cached_tokens is not None:
            usage["input_token_details"] = {"cache_read": cached_tokens}
        message.usage_metadata = usage  # type: ignore[assignment]
    return message


def fake_chunks(
    *parts: str | BaseException,
    input_tokens: int | None = 10,
    output_tokens: int | None = 5,
    finish_reason: str = "STOP",
) -> FakeStreamReply:
    """A streamed reply: one chunk per text part, an exception raised where it stands (a stream that breaks after
    some text). Like Gemini's last chunk, the last one carries the finish reason and the usage (None = none reported);
    a stream that ends in an exception has neither."""
    chunks: FakeStreamReply = [part if isinstance(part, BaseException) else AIMessageChunk(content=part) for part in parts]
    last = chunks[-1] if chunks else None
    if isinstance(last, AIMessageChunk):
        # Merging chunks joins string metadata, so the model name sits on one chunk only, as on Gemini's last one.
        last.response_metadata.update(finish_reason=finish_reason, model_name="fake-chat")
        last.usage_metadata = fake_reply("", input_tokens=input_tokens, output_tokens=output_tokens).usage_metadata
    return chunks


class FakeChatModel(BaseChatModel):
    """Pops one scripted reply per call: text (wrapped by `fake_reply`), a ready AIMessage, a streamed reply
    (`fake_chunks`), or an exception to raise (a vendor-style one, to test the error mapping). Every kind works for
    `invoke` and `astream`: plain text streams as one chunk, a streamed reply is merged for `invoke`. After the script
    runs out, `default` is returned."""

    default: str = "Fake reply."
    # Like a vendor model's fields: the helper sets them per call on a copy, so the recorded values show what was used.
    temperature: float | None = None
    timeout: float | None = None
    max_output_tokens: int | None = None
    # Seconds `astream` waits before each chunk, like a slow vendor (timing tests: first-chunk limit, long streams).
    chunk_delay: float = 0.0
    _replies: deque[FakeChatReply] = PrivateAttr(default_factory=deque)
    # Every call: the messages it got, its per-call kwargs, and the per-call limits (timeout, max_output_tokens, ...).
    _calls: list[tuple[list[BaseMessage], dict[str, Any]]] = PrivateAttr(default_factory=list)

    def __init__(self, replies: Iterable[FakeChatReply] = (), **kwargs: Any):
        super().__init__(**kwargs)
        self._replies = deque(replies)

    @property
    def calls(self) -> list[tuple[list[BaseMessage], dict[str, Any]]]:
        return self._calls

    @property
    def _llm_type(self) -> str:
        return "fake-chat"

    def _next(self, messages: list[BaseMessage], kwargs: dict[str, Any]) -> str | AIMessage | FakeStreamReply:
        limits = {"temperature": self.temperature, "timeout": self.timeout, "max_output_tokens": self.max_output_tokens}
        self._calls.append((list(messages), dict(kwargs) | limits))
        reply = self._replies.popleft() if self._replies else self.default
        if isinstance(reply, BaseException):
            raise reply
        return reply

    def _generate(
        self, messages: list[BaseMessage], stop: list[str] | None = None, run_manager: Any = None, **kwargs: Any
    ) -> ChatResult:
        reply = self._next(messages, kwargs)
        if isinstance(reply, list):
            merged = AIMessageChunk(content="")
            for chunk in reply:
                if isinstance(chunk, BaseException):
                    raise chunk
                merged = merged + chunk
            reply = AIMessage(merged.text, response_metadata=merged.response_metadata, usage_metadata=merged.usage_metadata)
        message = reply if isinstance(reply, AIMessage) else fake_reply(reply)
        return ChatResult(generations=[ChatGeneration(message=message)])

    async def _astream(
        self, messages: list[BaseMessage], stop: list[str] | None = None, run_manager: Any = None, **kwargs: Any
    ) -> AsyncIterator[ChatGenerationChunk]:
        reply = self._next(messages, kwargs)
        if not isinstance(reply, list):
            message = reply if isinstance(reply, AIMessage) else fake_reply(reply)
            reply = [AIMessageChunk(
                content=message.text, response_metadata=message.response_metadata, usage_metadata=message.usage_metadata
            )]  # fmt: skip
        for chunk in reply:
            if self.chunk_delay:
                await anyio.sleep(self.chunk_delay)
            if isinstance(chunk, BaseException):
                raise chunk
            generation = ChatGenerationChunk(message=chunk.model_copy(deep=True))
            if run_manager is not None:
                await run_manager.on_llm_new_token(chunk.text, chunk=generation)
            yield generation

    def with_structured_output(  # type: ignore[override]
        self, schema: type[BaseModel], *, method: str = "json_schema", include_raw: bool = False, **_: Any
    ) -> Runnable:
        parser = PydanticOutputParser(pydantic_object=schema)
        if not include_raw:
            return self | parser
        parsed = RunnablePassthrough.assign(parsed=itemgetter("raw") | parser, parsing_error=lambda _: None)
        fallback = RunnablePassthrough.assign(parsed=lambda _: None)
        return {"raw": self} | parsed.with_fallbacks([fallback], exception_key="parsing_error")
