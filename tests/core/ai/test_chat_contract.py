"""The contract every chat model the factory can build must meet behind the call helper (spec FR7, AC5): a text
reply, a structured reply, usage reported, and vendor errors arriving as our LLMError types. Runs against the Gemini
model `build_chat_model` builds (with its SDK client scripted, no network) and against the fake used by unit tests,
so the fake can't drift from the real thing."""

import asyncio
from collections.abc import Callable
from typing import Any

import pytest
from google.api_core import exceptions as gx
from langchain_core.messages import AIMessageChunk
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from app.core.ai.chat import ChatModel, complete_chat, complete_structured
from app.core.ai.chat_errors import to_llm_error
from app.core.ai.chat_fake import FakeChatModel, fake_chunks, fake_reply
from app.core.ai.factory import build_chat_model
from app.core.ai.provider import (
    LLMRateLimitError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)
from app.core.config import Settings
from tests.core.ai.test_langchain_behaviour import _response, _ScriptedClient
from tests.core.ai.test_retry import Clock

PROMPT = ChatPromptTemplate.from_messages([("system", "Answer as JSON when asked."), ("human", "{text}")])
LABELS = {"task": "contract", "prompt_version": "v1"}

# A scripted outcome: (reply text, prompt tokens, completion tokens) or an exception the vendor SDK would raise.
Outcome = tuple[str, int, int] | Exception
Build = Callable[[list[Outcome]], tuple[ChatModel, Callable[[], list[dict[str, Any]]]]]


def _gemini(outcomes: list[Outcome]):
    # Constructor values win over the environment in pydantic-settings, so the test's own LLM config is used as is.
    settings = Settings(
        _env_file=None,  # pyright: ignore[reportCallIssue]
        llm_providers=["google"],
        llm_google_api_key="k",  # pyright: ignore[reportArgumentType]
        llm_google_model="gemini-contract",
        llm_google_base_url="https://x.test/",
    )
    model = build_chat_model(settings)
    assert model is not None
    client = _ScriptedClient(*[o if isinstance(o, Exception) else _response(o[0], prompt=o[1], candidates=o[2]) for o in outcomes])
    object.__setattr__(model, "client", client)
    return model, lambda: client.calls


def _fake(outcomes: list[Outcome]):
    model = FakeChatModel(
        [o if isinstance(o, Exception) else fake_reply(o[0], input_tokens=o[1], output_tokens=o[2]) for o in outcomes]
    )
    return model, lambda: [kwargs for _, kwargs in model.calls]


BUILDS = [pytest.param(_gemini, id="gemini"), pytest.param(_fake, id="fake")]


class Profile(BaseModel):
    name: str
    skills: list[str]


def run(model, **overrides):
    clock = Clock()
    fields = {"max_tokens": 300, "budget_seconds": 30, "labels": LABELS, "timeout_seconds": 15, "max_retries": 1}
    return complete_chat(model, PROMPT, {"text": "hi"}, clock=clock, sleep=clock.sleep, **(fields | overrides))


@pytest.mark.parametrize("build", BUILDS)
def test_a_text_reply_comes_back_as_an_llm_result_with_usage(build: Build):
    model, _ = build([("Hello.", 12, 3)])
    result = run(model)
    assert (result.text, result.prompt_tokens, result.completion_tokens) == ("Hello.", 12, 3)
    assert result.finish_reason == "stop" and result.attempts == 1


@pytest.mark.parametrize("build", BUILDS)
def test_a_structured_reply_is_parsed(build: Build):
    model, _ = build([('{"name": "Ada", "skills": ["python"]}', 20, 8)])
    clock = Clock()
    outcome = complete_structured(
        model, PROMPT, {"text": "hi"}, Profile,
        max_tokens=300, budget_seconds=30, labels=LABELS, timeout_seconds=15, max_retries=1,
        clock=clock, sleep=clock.sleep,
    )  # fmt: skip
    assert outcome.value == Profile(name="Ada", skills=["python"])
    assert outcome.result.prompt_tokens == 20


@pytest.mark.parametrize("build", BUILDS)
@pytest.mark.parametrize(
    ("vendor_error", "ours"),
    [
        (gx.ResourceExhausted("quota"), LLMRateLimitError),
        (gx.ServiceUnavailable("down"), LLMServerError),
        (gx.DeadlineExceeded("slow"), LLMTimeoutError),
        (gx.PermissionDenied("no"), LLMRequestError),
        (gx.InvalidArgument("bad"), LLMRequestError),  # wrapped by the Gemini integration, read through its cause
    ],
)
def test_vendor_errors_arrive_as_our_errors(build: Build, vendor_error: Exception, ours: type):
    model, _ = build([vendor_error])
    with pytest.raises(ours):
        run(model, max_retries=0)


@pytest.mark.parametrize("build", BUILDS)
def test_the_per_call_limits_reach_the_model(build: Build):
    model, calls = build([("ok", 1, 1)])
    run(model, budget_seconds=4)
    [call] = calls()
    if "request" in call:  # Gemini: what the SDK request carries
        assert call["timeout"] == 4 and call["request"].generation_config.max_output_tokens == 300
    else:
        assert call["timeout"] == 4 and call["max_output_tokens"] == 300


def test_a_per_call_temperature_reaches_the_gemini_request():
    model, calls = _gemini([("ok", 1, 1)])
    run(model, temperature=0.2)
    assert calls()[0]["request"].generation_config.temperature == pytest.approx(0.2)


@pytest.mark.parametrize("build", BUILDS)
def test_the_per_call_limits_reach_a_structured_call_too(build: Build):
    # Regression: `.bind()`-ed limits were dropped by `with_structured_output` (test_langchain_behaviour.py).
    model, calls = build([('{"name": "Ada", "skills": []}', 1, 1)])
    clock = Clock()
    complete_structured(
        model, PROMPT, {"text": "hi"}, Profile,
        max_tokens=300, budget_seconds=4, labels=LABELS, timeout_seconds=15, max_retries=1, temperature=0.2,
        clock=clock, sleep=clock.sleep,
    )  # fmt: skip
    [call] = calls()
    if "request" in call:
        config = call["request"].generation_config
        assert call["timeout"] == 4 and config.max_output_tokens == 300 and config.temperature == pytest.approx(0.2)
    else:
        assert (call["timeout"], call["max_output_tokens"], call["temperature"]) == (4, 300, 0.2)


# --- Streaming (U3b1 FR2): `astream`, which the stream helper builds on --------------------------------------------

# One streamed call: its chunks in order, as (text, prompt tokens so far, completion tokens so far) - Gemini reports
# usage cumulatively and the SDK turns it into per-chunk differences - with an exception where the stream breaks.
# A bare exception fails the call before the first chunk.
StreamOutcome = list[tuple[str, int, int] | Exception] | Exception


class _ScriptedStreamClient:
    """Stands in for the SDK's async client: `stream_generate_content` is awaited, then iterated."""

    def __init__(self, outcome: StreamOutcome):
        self.outcome = outcome
        self.calls: list[dict[str, Any]] = []

    async def stream_generate_content(self, **kwargs: Any):
        self.calls.append(kwargs)
        if isinstance(self.outcome, Exception):
            raise self.outcome
        outcome = self.outcome

        async def chunks():
            for position, item in enumerate(outcome, 1):
                if isinstance(item, Exception):
                    raise item
                response = _response(item[0], prompt=item[1], candidates=item[2])
                if position < len(outcome):  # like Gemini: only the last chunk says why the reply ended
                    response.candidates[0].finish_reason = 0
                yield response

        return chunks()


def _gemini_stream(outcome: StreamOutcome):
    model, _ = _gemini([])
    client = _ScriptedStreamClient(outcome)
    object.__setattr__(model, "async_client_running", client)
    return model, lambda: client.calls


def _fake_stream(outcome: StreamOutcome):
    if isinstance(outcome, Exception):
        model = FakeChatModel([outcome])
    else:
        totals = [item for item in outcome if not isinstance(item, Exception)][-1]
        parts = [item if isinstance(item, Exception) else item[0] for item in outcome]
        model = FakeChatModel([fake_chunks(*parts, input_tokens=totals[1], output_tokens=totals[2])])
    return model, lambda: [kwargs for _, kwargs in model.calls]


STREAM_BUILDS = [pytest.param(_gemini_stream, id="gemini"), pytest.param(_fake_stream, id="fake")]


def _collect(model) -> tuple[list[AIMessageChunk], BaseException | None]:
    chunks: list[AIMessageChunk] = []

    async def run():
        async for chunk in model.astream(PROMPT.invoke({"text": "hi"})):
            chunks.append(chunk)

    try:
        asyncio.run(run())
    except Exception as exc:  # noqa: BLE001 - the test asserts which error, after which chunks
        return chunks, exc
    return chunks, None


@pytest.mark.parametrize("build", STREAM_BUILDS)
def test_a_stream_yields_its_text_in_order_with_the_total_usage(build):
    model, _ = build([("Hel", 7, 1), ("lo.", 7, 3)])
    chunks, error = _collect(model)
    assert error is None
    merged = sum(chunks[1:], chunks[0])
    assert [c.text for c in chunks if c.text] == ["Hel", "lo."]
    assert (merged.usage_metadata["input_tokens"], merged.usage_metadata["output_tokens"]) == (7, 3)
    assert merged.response_metadata.get("finish_reason") == "STOP"


@pytest.mark.parametrize("build", STREAM_BUILDS)
def test_a_stream_can_fail_before_its_first_chunk(build):
    model, _ = build(gx.ServiceUnavailable("down"))
    chunks, error = _collect(model)
    assert chunks == [] and isinstance(to_llm_error(error), LLMServerError)


@pytest.mark.parametrize("build", STREAM_BUILDS)
def test_a_stream_can_fail_after_some_text(build):
    model, _ = build([("Hel", 7, 1), gx.DeadlineExceeded("slow")])
    chunks, error = _collect(model)
    assert [c.text for c in chunks if c.text] == ["Hel"]
    assert isinstance(to_llm_error(error), LLMTimeoutError)


@pytest.mark.parametrize("build", STREAM_BUILDS)
def test_the_per_call_timeout_reaches_a_stream(build):
    model, calls = build([("ok", 1, 1)])
    _collect(model.model_copy(update={"timeout": 4}))
    [call] = calls()
    assert call["timeout"] == 4


def test_a_fake_stream_without_usage_reports_none():
    model = FakeChatModel([fake_chunks("a", "b", input_tokens=None, output_tokens=None)])
    chunks, _ = _collect(model)
    assert all(c.usage_metadata is None for c in chunks)


def test_a_fake_plain_reply_streams_as_one_chunk_and_a_stream_script_works_blocking():
    model = FakeChatModel(["Whole reply.", fake_chunks("Hel", "lo.")])
    chunks, _ = _collect(model)
    assert [c.text for c in chunks if c.text] == ["Whole reply."] and chunks[0].usage_metadata is not None
    assert model.invoke("hi").text == "Hello."
