"""`stream_chat`, the async stream helper of the LangChain call layer (U3b1 step 12, FR7, AC7, AC10).

It keeps the U2 rules for a stream: transport retries only before the first chunk (`RetryPolicy.acall`), vendor
errors mapped to our LLMError types, `after_output` set on a failure after text, one Langfuse generation per call.
And the two stream rules the spike forced (learnings.md, step 1): the vendor gets the time left in the turn as its
timeout (one deadline for the whole stream), while `LLM_TIMEOUT_SECONDS` only limits the wait for the first chunk.
"""

import anyio
import pytest
from google.api_core import exceptions as gx
from langchain_core.prompts import ChatPromptTemplate

from app.core.ai.chat_fake import FakeChatModel, fake_chunks
from app.core.ai.chat_stream import stream_chat
from app.core.ai.chat_tracing import TracerHandle
from app.core.ai.provider import (
    LLMBadResponseError,
    LLMError,
    LLMResult,
    LLMServerError,
    LLMTimeoutError,
)
from app.core.ai.tracing import Tracer
from app.core.config import settings
from tests.core.ai.test_chat_contract import _gemini
from tests.core.ai.test_langchain_behaviour import _response
from tests.core.ai.test_retry import Clock
from tests.core.ai.test_tracing import FakeClient
from tests.provider_chat import closed_soon

pytestmark = pytest.mark.anyio

PROMPT = ChatPromptTemplate.from_messages([("system", "Ask one question."), ("human", "{text}")])
LABELS = {"task": "interviewer_stream", "prompt_version": "v5", "budget_left_ms": 30000}


@pytest.fixture
def anyio_backend():
    return "asyncio"


async def run(model, *, budget=30.0, first_chunk_seconds=None, close_after=None):
    """Every text chunk, then the LLMResult or the LLMError the stream ended with."""
    clock = Clock()
    items: list[str | LLMResult | LLMError] = []
    stream = stream_chat(
        model,
        PROMPT,
        {"text": "hi"},
        max_tokens=300,
        budget_seconds=budget,
        labels=LABELS,
        first_chunk_seconds=first_chunk_seconds,
        clock=clock,
        async_sleep=clock.async_sleep,
    )
    try:
        async for item in stream:
            items.append(item)
            if close_after is not None and len(items) == close_after:
                break
    except LLMError as exc:
        items.append(exc)
    finally:
        await stream.aclose()
    return items


async def test_text_chunks_then_the_result_with_the_merged_usage():  # FR7
    model = FakeChatModel([fake_chunks("CATEGORY: technical\n", "How would ", "you shard it?", input_tokens=40, output_tokens=12)])

    *chunks, result = await run(model)

    assert chunks == ["CATEGORY: technical\n", "How would ", "you shard it?"]
    assert isinstance(result, LLMResult)
    assert result.text == "CATEGORY: technical\nHow would you shard it?"
    assert (result.prompt_tokens, result.completion_tokens, result.finish_reason, result.attempts) == (40, 12, "stop", 1)


async def test_a_failure_before_the_first_chunk_is_retried():  # EC4
    model = FakeChatModel([gx.ServiceUnavailable("down"), fake_chunks("Hello?")])

    *chunks, result = await run(model)

    assert chunks == ["Hello?"] and isinstance(result, LLMResult) and result.attempts == 2
    assert len(model.calls) == 2


async def test_a_failure_before_any_text_that_persists_is_ours_and_not_after_output():  # EC4
    model = FakeChatModel([gx.ServiceUnavailable("down")] * (1 + settings.llm_max_retries))

    [error] = await run(model)

    assert isinstance(error, LLMServerError) and not error.after_output
    assert error.attempts == 1 + settings.llm_max_retries and len(model.calls) == 1 + settings.llm_max_retries


async def test_a_failure_after_text_is_never_retried_and_flagged():  # EC5: the caller may have shown the text
    model = FakeChatModel([fake_chunks("Tell me ", gx.DeadlineExceeded("slow")), fake_chunks("unused")])

    chunks_and_error = await run(model)

    assert chunks_and_error[:-1] == ["Tell me "]
    error = chunks_and_error[-1]
    assert isinstance(error, LLMTimeoutError) and error.after_output and len(model.calls) == 1


async def test_the_first_chunk_must_come_within_its_limit():  # EC7: LLM_TIMEOUT_SECONDS bounds the first chunk only
    model = FakeChatModel([fake_chunks("late")] * 3, chunk_delay=0.2)

    *_, error = await run(model, first_chunk_seconds=0.02)

    assert isinstance(error, LLMTimeoutError) and not error.after_output


async def test_a_stream_may_run_past_the_first_chunk_limit():  # EC7: no whole-stream cap below the turn deadline
    model = FakeChatModel([fake_chunks("a ", "b ", "c ", "d ", "e ", "f?")], chunk_delay=0.05)

    *chunks, result = await run(model, first_chunk_seconds=0.2)

    # 6 chunks x 50 ms = 300 ms, past the 200 ms first-chunk limit: only the first one had to beat it.
    assert chunks == ["a ", "b ", "c ", "d ", "e ", "f?"] and isinstance(result, LLMResult)


async def test_the_vendor_timeout_is_the_time_left_in_the_turn():  # spike: the SDK timeout bounds the whole stream
    model = FakeChatModel([fake_chunks("Hi?")])

    await run(model, budget=22.0)

    [(_, kwargs)] = model.calls
    assert kwargs["timeout"] == 22.0 and kwargs["max_output_tokens"] == 300


async def test_no_call_without_time_left():  # EC10
    model = FakeChatModel([fake_chunks("Hi?")])

    [error] = await run(model, budget=0)

    assert isinstance(error, LLMTimeoutError) and model.calls == []


async def test_an_empty_stream_is_a_bad_response():  # EC2
    model = FakeChatModel([fake_chunks("  ", finish_reason="MAX_TOKENS")])

    *_, error = await run(model)

    assert isinstance(error, LLMBadResponseError) and error.finish_reason == "length"


async def test_a_stream_without_usage_still_succeeds():  # EC12
    model = FakeChatModel([fake_chunks("Hi?", input_tokens=None, output_tokens=None)])

    *_, result = await run(model)

    assert isinstance(result, LLMResult) and (result.prompt_tokens, result.completion_tokens) == (None, None)


def traced(model) -> FakeClient:
    client = FakeClient()
    model.callbacks = [TracerHandle(Tracer(client))]
    return client


async def test_one_generation_per_call_with_its_labels_and_usage():  # FR10, AC10
    model = FakeChatModel([gx.ServiceUnavailable("down"), fake_chunks("Hi?", input_tokens=40, output_tokens=12)])
    client = traced(model)

    await run(model)

    [generation] = client.generations
    assert generation.kwargs["name"] == "interviewer_stream" and generation.kwargs["metadata"] == LABELS
    final = generation.final
    assert final["output"] == "Hi?" and final["metadata"]["attempts"] == 2
    assert final["usage_details"]["input"] == 40


async def test_a_failure_after_text_records_the_partial_text():  # FR10
    model = FakeChatModel([fake_chunks("Tell me ", gx.ServiceUnavailable("down"))])
    client = traced(model)

    await run(model)

    [generation] = client.generations
    assert generation.final["level"] == "ERROR" and generation.final["output"] == "Tell me "


async def test_closing_the_stream_early_cancels_the_generation():  # EC8: the client left
    model = FakeChatModel([fake_chunks("Tell me ", "about ", "it?")])
    client = traced(model)

    items = await run(model, close_after=1)

    [generation] = client.generations
    assert items == ["Tell me "]
    assert generation.final["status_message"] == "cancelled" and generation.final["output"] == "Tell me "


class _ClosingStreamClient:
    """The Gemini SDK's async client, streaming slowly and recording when its stream is closed."""

    def __init__(self):
        self.closed = False

    async def stream_generate_content(self, **_):
        async def chunks():
            try:
                for text in ["Tell me ", "about ", "it?"]:
                    await anyio.sleep(0.01)
                    yield _response(text, prompt=5, candidates=1)
            finally:
                self.closed = True

        return chunks()


async def test_closing_early_closes_the_gemini_stream_too():  # EC8: no more tokens are generated
    model, _ = _gemini([])
    vendor = _ClosingStreamClient()
    object.__setattr__(model, "async_client_running", vendor)

    items = await run(model, close_after=1)

    # LangChain's astream doesn't close the vendor's stream itself; asyncio's async-generator finalizer does, a few
    # loop turns later (measured: about 15), which `closed_soon` allows for.
    assert items == ["Tell me "] and await closed_soon(lambda: vendor.closed)
