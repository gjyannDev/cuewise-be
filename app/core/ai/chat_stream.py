"""The streamed call of the LangChain call layer (U3b1): `astream()` under the same rules as `complete_chat`.

`stream_chat` yields the reply's text chunks as they arrive, then the `LLMResult` (merged usage, finish reason,
attempts, latency), so a caller that shows text while it streams changes as little as possible. Its rules:
- **Retries only before the first chunk** (`RetryPolicy.acall`, the U2 rules: timeouts, 429 and 5xx, full jitter,
  never sooner than Retry-After, nothing started past the budget). After a chunk, the caller may have shown it, so a
  failure is raised with `after_output` set and never retried here.
- **Two time limits, because the vendor SDK has only one.** The Gemini SDK passes the model's `timeout` to the whole
  stream as one deadline (spike, docs/features/u3b1-interview-calls/learnings.md), so a `timeout` of
  `LLM_TIMEOUT_SECONDS` would cut a long question. The vendor gets the time left in the turn instead, and
  `LLM_TIMEOUT_SECONDS` bounds only the wait for the first chunk, enforced here.
- Vendor errors leave as our LLMError types (`to_llm_error`); one Langfuse generation per call (`ChatTrace`), with
  the text sent so far when it fails or is closed early.
"""

import time
from collections.abc import AsyncGenerator, Awaitable, Callable, Mapping
from typing import Any, cast

import anyio
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessageChunk
from langchain_core.runnables import Runnable

from app.core.config import settings

from .chat import ChatModel, _finish_reason, _result, _tracer_of, logger
from .chat_chain import as_chain, log_switch
from .chat_errors import to_llm_error
from .chat_tracing import ChatTrace
from .provider import LLMBadResponseError, LLMError, LLMResult, LLMTimeoutError
from .retry import RetryPolicy
from .tracing import TraceLabels


async def stream_chat(
    model: ChatModel,
    prompt: Runnable[Any, Any],
    inputs: Mapping[str, Any],
    *,
    max_tokens: int,
    budget_seconds: float,
    labels: TraceLabels,
    first_chunk_seconds: float | None = None,
    clock: Callable[[], float] = time.perf_counter,
    async_sleep: Callable[[float], Awaitable[None]] = anyio.sleep,
) -> AsyncGenerator[str | LLMResult]:
    """`prompt | model` streamed: text chunks, then the LLMResult. Raises an LLMError (with `after_output` once text
    was yielded). `first_chunk_seconds` defaults to LLM_TIMEOUT_SECONDS."""
    first_limit = settings.llm_timeout_seconds if first_chunk_seconds is None else first_chunk_seconds
    task = labels.get("task")
    task = task if isinstance(task, str) else None
    policy = RetryPolicy(
        max_retries=settings.llm_max_retries, task="chat", logger=logger, clock=clock, async_sleep=async_sleep
    )
    tracer = _tracer_of(model)
    chain = as_chain(model)
    trace = ChatTrace(tracer, labels, {"max_tokens": max_tokens}) if tracer is not None else None
    config = {"callbacks": [trace]} if trace is not None else None
    start = clock()

    async def open_member(member: BaseChatModel, remaining: float) -> tuple[AsyncGenerator[AIMessageChunk], AIMessageChunk]:
        limited = member.model_copy(update={"timeout": remaining, "max_output_tokens": max_tokens})
        # An async generator at runtime (LangChain types it as an iterator): closed below when it fails.
        chunks = cast(
            "AsyncGenerator[AIMessageChunk]",
            (prompt | limited).astream(dict(inputs), config=config),  # type: ignore[arg-type]
        )
        try:
            with anyio.fail_after(min(first_limit, remaining)):
                return chunks, await anext(chunks)
        except StopAsyncIteration:
            raise LLMBadResponseError("LLM returned an empty message") from None
        except Exception as exc:  # every vendor/framework error (and the first-chunk timeout) leaves as an LLMError
            await chunks.aclose()
            raise to_llm_error(exc) from exc

    async def open_stream(
        remaining: float,
    ) -> tuple[str, BaseChatModel, AsyncGenerator[AIMessageChunk], AIMessageChunk]:
        # The retried step: open a stream and wait for its first chunk. A transport error before any chunk hands the
        # call to the next provider (within the time left); the first chunk commits the stream to its provider.
        started = clock()
        error: LLMError = LLMTimeoutError("LLM call has no time left")
        previous: str | None = None
        for name, member in chain.members:
            left = remaining - (clock() - started)
            if left <= 0:
                break
            if previous is not None:
                log_switch(logger, previous, name, error)
            try:
                chunks, chunk = await open_member(member, left)
            except LLMError as exc:
                if not exc.retryable:
                    raise
                error, previous = exc, name
                continue
            return name, member, chunks, chunk
        raise error  # every provider failed before its first chunk: RetryPolicy backs off and runs the chain again

    try:
        opened = await policy.acall(open_stream, budget=budget_seconds, task=task)
    except LLMError as exc:
        if trace is not None:
            trace.fail(exc)
        raise
    provider, answered, chunks, chunk = opened.value
    merged, parts, read_all = chunk, [], False
    try:
        while True:
            if chunk.text:
                parts.append(chunk.text)
                yield chunk.text
            try:
                chunk = await anext(chunks)
            except StopAsyncIteration:
                break
            merged = merged + chunk
        read_all = True
    except Exception as exc:  # after the first chunk: never retried, the caller may have shown the text
        error = to_llm_error(exc)
        error.attempts, error.latency_ms = opened.attempts, round((clock() - start) * 1000)
        error.after_output = bool(parts)
        policy.log_giveup(error, task=task)
        if trace is not None:
            trace.fail(error, "".join(parts))
        raise error from exc
    finally:
        await chunks.aclose()
        if trace is not None and not read_all:
            trace.cancel("".join(parts))  # a no-op after `fail`; otherwise the caller closed us early
    if not merged.text.strip():
        error = LLMBadResponseError(
            "LLM returned an empty message", finish_reason=_finish_reason(merged.response_metadata.get("finish_reason"))
        )
        error.attempts, error.latency_ms = opened.attempts, round((clock() - start) * 1000)
        if trace is not None:
            trace.fail(error)
        raise error
    result = _result(
        merged, answered, provider=provider, attempts=opened.attempts, latency_ms=round((clock() - start) * 1000)
    )
    if trace is not None:
        trace.succeed(result)
    yield result
