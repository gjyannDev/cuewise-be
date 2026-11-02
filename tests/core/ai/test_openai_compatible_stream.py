"""OpenAICompatibleProvider.stream: chat completions with `stream: true`, read as SSE chunks (sse-streaming Step 10).

The provider retries only before the first chunk: once text was yielded, a failure is raised flagged `after_output`,
and the caller decides (the interviewer takes the draft back and retries or asks from the bank). AC11.
"""

import json

import httpx
import pytest

from app.core.ai.openai_compatible import OpenAICompatibleProvider
from app.core.ai.provider import (
    ChatMessage,
    LLMBadResponseError,
    LLMRateLimitError,
    LLMRequestError,
    LLMResult,
    LLMServerError,
    LLMTimeoutError,
)

pytestmark = pytest.mark.anyio

MESSAGES = [
    ChatMessage(role="system", content="You are an interviewer."),
    ChatMessage(role="user", content="We argued about REST vs GraphQL."),
]


@pytest.fixture
def anyio_backend():
    return "asyncio"


def chunk(text=None, *, finish=None, model="vendor/model-x") -> dict:
    delta = {} if text is None else {"content": text}
    return {"id": "gen-1", "model": model, "choices": [{"index": 0, "delta": delta, "finish_reason": finish}]}


USAGE = {
    "choices": [],
    "usage": {
        "prompt_tokens": 212,
        "completion_tokens": 18,
        "prompt_tokens_details": {"cached_tokens": 100},
        "completion_tokens_details": {"reasoning_tokens": 4},
    },
}


def sse_body(*events: dict, done: bool = True) -> bytes:
    """A text/event-stream body as OpenAI-compatible endpoints send it (Google's adds no extra fields we rely on)."""
    lines = [f"data: {json.dumps(event)}\n\n" for event in events]
    if done:
        lines.append("data: [DONE]\n\n")
    return "".join(lines).encode()


class Interrupted(httpx.AsyncByteStream):
    """A body that sends some bytes, then fails (a dropped connection), optionally moving the clock per piece."""

    def __init__(self, pieces: list[bytes], error: Exception | None, clock=None, step: float = 0.0):
        self.pieces, self.error, self.clock, self.step = pieces, error, clock, step

    async def __aiter__(self):
        for piece in self.pieces:
            if self.clock is not None:
                self.clock.now += self.step
            yield piece
        if self.error is not None:
            raise self.error


class Clock:
    def __init__(self):
        self.now = 0.0
        self.sleeps: list[float] = []

    def __call__(self) -> float:
        return self.now

    async def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


@pytest.fixture
def clock():
    return Clock()


@pytest.fixture
def make_provider(clock):
    def _make(*script, max_retries=2, budget=30.0, timeout=15.0):
        requests: list[httpx.Request] = []
        steps = list(script)

        async def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            step = steps.pop(0)
            if isinstance(step, Exception):
                raise step
            return step

        provider = OpenAICompatibleProvider(
            api_key="test-key-123",
            model="vendor/model-x",
            base_url="https://llm.test/api/v1",
            timeout_seconds=timeout,
            max_retries=max_retries,
            total_budget_seconds=budget,
            async_transport=httpx.MockTransport(handler),
            async_sleep=clock.sleep,
            clock=clock,
        )
        return provider, requests

    return _make


def ok(*events, done=True) -> httpx.Response:
    return httpx.Response(200, content=sse_body(*events, done=done), headers={"content-type": "text/event-stream"})


async def drain(provider, **kwargs) -> tuple[list[str], LLMResult]:
    chunks, final = [], None
    async for item in provider.stream(MESSAGES, max_tokens=150, **kwargs):
        if isinstance(item, LLMResult):
            final = item
        else:
            chunks.append(item)
    assert final is not None
    return chunks, final


async def test_chunks_arrive_in_order_and_the_result_joins_them_with_usage(make_provider):  # AC11
    provider, requests = make_provider(
        ok(chunk("How would "), chunk("you shard it?"), chunk(finish="stop"), USAGE)
    )

    chunks, result = await drain(provider)

    assert chunks == ["How would ", "you shard it?"]
    assert result.text == "How would you shard it?"
    assert (result.model, result.finish_reason, result.attempts) == ("vendor/model-x", "stop", 1)
    assert (result.prompt_tokens, result.completion_tokens) == (212, 18)
    assert (result.cached_tokens, result.reasoning_tokens) == (100, 4)
    body = json.loads(requests[0].content)
    assert body["stream"] is True
    assert body["stream_options"] == {"include_usage": True}
    assert body["max_tokens"] == 150
    await provider.aclose()


async def test_a_stream_without_a_usage_chunk_reports_none_never_a_guess(make_provider):  # AC11, EC17
    provider, _ = make_provider(ok(chunk("Why?"), chunk(finish="stop")))

    _, result = await drain(provider)

    assert (result.prompt_tokens, result.completion_tokens, result.cached_tokens) == (None, None, None)


@pytest.mark.parametrize(
    "first",
    [httpx.Response(429), httpx.Response(503), httpx.ConnectError("refused"), ok({"error": {"code": 503}})],
    ids=["429", "503", "connect", "error-chunk"],
)
async def test_a_failure_before_the_first_chunk_is_retried(make_provider, clock, first):  # AC11
    provider, requests = make_provider(first, ok(chunk("Why this design?"), chunk(finish="stop")))

    chunks, result = await drain(provider)

    assert chunks == ["Why this design?"]
    assert result.attempts == 2
    assert len(requests) == 2
    assert len(clock.sleeps) == 1


async def test_a_failure_after_the_first_chunk_is_not_retried_and_is_flagged(make_provider):  # AC11
    body = Interrupted([sse_body(chunk("How would "), done=False)], httpx.ReadError("connection reset"))
    provider, requests = make_provider(httpx.Response(200, stream=body))

    seen = []
    with pytest.raises(LLMServerError) as exc:
        async for item in provider.stream(MESSAGES, max_tokens=150):
            seen.append(item)

    assert seen == ["How would "]
    assert exc.value.after_output is True
    assert exc.value.attempts == 1
    assert len(requests) == 1


async def test_an_error_chunk_mid_stream_raises_after_output(make_provider):  # AC11
    provider, requests = make_provider(ok(chunk("Tell me "), {"error": {"code": 429, "message": "quota"}}))

    with pytest.raises(LLMRateLimitError) as exc:
        [item async for item in provider.stream(MESSAGES, max_tokens=150)]

    assert exc.value.after_output is True
    assert len(requests) == 1


async def test_a_read_timeout_is_a_timeout_error(make_provider):  # AC11
    provider, _ = make_provider(httpx.ReadTimeout("slow"), max_retries=0)

    with pytest.raises(LLMTimeoutError) as exc:
        [item async for item in provider.stream(MESSAGES, max_tokens=150)]

    assert exc.value.after_output is False


async def test_the_total_budget_also_bounds_a_slow_stream(make_provider, clock):  # AC11: a trickle can't run forever
    pieces = [sse_body(chunk(f"word{i} "), done=False) for i in range(5)]
    provider, _ = make_provider(httpx.Response(200, stream=Interrupted(pieces, None, clock, step=0.6)), budget=1.0)

    seen = []
    with pytest.raises(LLMTimeoutError) as exc:
        async for item in provider.stream(MESSAGES, max_tokens=150):
            seen.append(item)

    assert exc.value.after_output is True
    assert 1 <= len(seen) < 5


async def test_blank_output_is_a_bad_response(make_provider):  # AC11
    provider, _ = make_provider(ok(chunk("  "), chunk(finish="length")), max_retries=0)

    with pytest.raises(LLMBadResponseError) as exc:
        [item async for item in provider.stream(MESSAGES, max_tokens=150)]

    assert exc.value.finish_reason == "length"


async def test_a_rejected_request_is_not_retried(make_provider):  # AC11
    provider, requests = make_provider(httpx.Response(400, json={"error": "bad model"}))

    with pytest.raises(LLMRequestError):
        [item async for item in provider.stream(MESSAGES, max_tokens=150)]

    assert len(requests) == 1


async def test_malformed_chunk_json_is_a_bad_response(make_provider):  # AC11
    provider, _ = make_provider(
        httpx.Response(200, content=b"data: {not json\n\n", headers={"content-type": "text/event-stream"}),
        max_retries=0,
    )

    with pytest.raises(LLMBadResponseError):
        [item async for item in provider.stream(MESSAGES, max_tokens=150)]
