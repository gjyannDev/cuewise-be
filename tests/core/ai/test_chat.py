"""The LangChain call helper (`complete_chat`, `complete_structured`): budget, retries, errors, usage and tracing on
one model call (spec FR3, FR4, FR5; AC2-AC4; EC5-EC7, EC16). Driven by the fake chat model with an injected clock
and sleep, so retries never wait for real."""

from typing import Any

import pytest
from google.api_core import exceptions as gx
from google.protobuf import duration_pb2
from google.rpc import error_details_pb2
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from app.core.ai.chat import Structured, complete_chat, complete_structured
from app.core.ai.chat_fake import FakeChatModel, fake_reply
from app.core.ai.chat_tracing import TracerHandle
from app.core.ai.provider import (
    LLMBadResponseError,
    LLMError,
    LLMRateLimitError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)
from app.core.ai.tracing import Tracer
from tests.core.ai.test_retry import Clock
from tests.core.ai.test_tracing import FakeClient

PROMPT = ChatPromptTemplate.from_messages([("system", "Be brief."), ("human", "{text}")])
INPUTS = {"text": "hello"}
LABELS = {"task": "job_description_summary", "prompt_version": "v2"}


class SlowFake(FakeChatModel):
    """Each call takes `cost` seconds on the test clock (the clock is not a pydantic field: set after build)."""

    def _generate(self, messages: Any, stop: Any = None, run_manager: Any = None, **kwargs: Any) -> Any:
        clock: Clock = self.__dict__["_test_clock"]
        clock.now += self.__dict__["_test_cost"]
        return super()._generate(messages, stop, run_manager, **kwargs)


def slow(replies, clock: Clock, cost: float) -> SlowFake:
    model = SlowFake(replies)  # pyright: ignore[reportCallIssue]  (FakeChatModel's own __init__ takes the script)
    object.__setattr__(model, "_test_clock", clock)
    object.__setattr__(model, "_test_cost", cost)
    return model


def call(model, clock=None, **overrides):
    clock = clock or Clock()
    fields = {"max_tokens": 400, "budget_seconds": 30, "labels": LABELS, "timeout_seconds": 15, "max_retries": 2}
    return complete_chat(model, PROMPT, INPUTS, clock=clock, sleep=clock.sleep, **(fields | overrides))


def retry_info(seconds: int) -> error_details_pb2.RetryInfo:
    return error_details_pb2.RetryInfo(retry_delay=duration_pb2.Duration(seconds=seconds))


# --- a reply ------------------------------------------------------------------------------------------------------


def test_a_text_reply_is_an_llm_result_with_usage_and_the_old_finish_reason():
    model = FakeChatModel([fake_reply(" A summary. ", input_tokens=120, output_tokens=30, reasoning_tokens=4)])
    result = call(model)

    assert result.text == "A summary."
    assert (result.prompt_tokens, result.completion_tokens, result.reasoning_tokens) == (120, 30, 4)
    assert result.finish_reason == "stop" and result.attempts == 1
    messages, kwargs = model.calls[0]
    assert [m.type for m in messages] == ["system", "human"]
    assert kwargs["max_output_tokens"] == 400 and kwargs["timeout"] == 15


def test_a_reply_cut_off_by_the_token_cap_reads_length():
    result = call(FakeChatModel([fake_reply("Partial", finish_reason="MAX_TOKENS")]))
    assert result.finish_reason == "length"


def test_a_reply_without_usage_succeeds_with_unknown_tokens():  # EC16
    result = call(FakeChatModel([fake_reply("Ok.", input_tokens=None, output_tokens=None)]))
    assert result.prompt_tokens is None and result.completion_tokens is None


def test_an_empty_reply_is_a_bad_response_and_not_retried():
    model = FakeChatModel([fake_reply("   "), "never"])
    with pytest.raises(LLMBadResponseError):
        call(model)
    assert len(model.calls) == 1


def test_a_temperature_applies_to_this_call_only():
    model = FakeChatModel(["a", "b"])
    call(model, temperature=0.2)
    call(model)

    assert [kwargs["temperature"] for _, kwargs in model.calls] == [0.2, None]
    assert model.temperature is None  # the shared model is never changed


# --- the time budget ------------------------------------------------------------------------------------------------


def test_a_spent_budget_sends_nothing():  # FR4
    model = FakeChatModel(["never"])
    with pytest.raises(LLMTimeoutError):
        call(model, budget_seconds=0)
    assert model.calls == []


def test_each_attempt_gets_the_time_left_as_its_timeout():  # FR4
    model = FakeChatModel(["ok"])
    call(model, budget_seconds=4, timeout_seconds=15)
    assert model.calls[0][1]["timeout"] == 4


def test_an_almost_spent_budget_cuts_the_call_and_starts_no_retry_after_it(app_logs):  # EC7, AC3
    clock = Clock()
    model = slow([gx.DeadlineExceeded("slow"), "never"], clock, cost=2.0)
    with pytest.raises(LLMTimeoutError):
        call(model, clock, budget_seconds=2.0)

    assert len(model.calls) == 1 and model.calls[0][1]["timeout"] == 2.0
    assert clock.sleeps == []
    [giveup] = [r for r in app_logs.records if r.getMessage().startswith("retry_giveup")]
    assert giveup.fields["reason"] == "deadline" and giveup.fields["task"] == "job_description_summary"


# --- retries (U2 rules, on RetryPolicy) ---------------------------------------------------------------------------


def test_a_429_waits_at_least_its_retry_after_then_succeeds():  # EC5, AC4
    clock = Clock()
    model = FakeChatModel([gx.ResourceExhausted("quota", details=[retry_info(7)]), "ok"])
    result = call(model, clock)

    assert result.text == "ok" and result.attempts == 2
    assert clock.sleeps and clock.sleeps[0] >= 7


def test_a_5xx_is_retried_up_to_max_retries_then_given_up_with_the_task(app_logs):  # AC4
    clock = Clock()
    model = FakeChatModel([gx.ServiceUnavailable("down")] * 3 + ["never"])
    with pytest.raises(LLMServerError) as info:
        call(model, clock, max_retries=2)

    assert len(model.calls) == 3 and info.value.attempts == 3
    waits = [r for r in app_logs.records if r.getMessage().startswith("retry_wait")]
    assert len(waits) == 2 and all(w.fields["task"] == "job_description_summary" for w in waits)
    [giveup] = [r for r in app_logs.records if r.getMessage().startswith("retry_giveup")]
    assert giveup.fields["reason"] == "max_attempts"


def test_the_retry_count_follows_the_setting():
    model = FakeChatModel([gx.ServiceUnavailable("down")] * 5)
    with pytest.raises(LLMServerError):
        call(model, max_retries=0)
    assert len(model.calls) == 1


def test_a_4xx_is_not_retried():  # AC4
    model = FakeChatModel([gx.PermissionDenied("no"), "never"])
    with pytest.raises(LLMRequestError):
        call(model)
    assert len(model.calls) == 1


def test_an_unknown_exception_is_a_generic_llm_error_and_not_retried():  # EC6
    model = FakeChatModel([KeyError("odd"), "never"])
    with pytest.raises(LLMError) as info:
        call(model)
    assert type(info.value) is LLMError and len(model.calls) == 1


def test_a_rate_limit_that_escapes_carries_its_retry_after():  # EC5
    model = FakeChatModel([gx.ResourceExhausted("quota", details=[retry_info(40)])])
    with pytest.raises(LLMRateLimitError) as info:
        call(model, budget_seconds=30)  # the 40 s wait would end past the budget: give up instead
    assert info.value.retry_after == 40 and len(model.calls) == 1


# --- structured output ----------------------------------------------------------------------------------------------


class Reply(BaseModel):
    name: str
    skills: list[str]


def structured(model, **overrides) -> Structured[Reply]:
    clock = Clock()
    fields = {"max_tokens": 400, "budget_seconds": 30, "labels": LABELS, "timeout_seconds": 15, "max_retries": 2}
    return complete_structured(model, PROMPT, INPUTS, Reply, clock=clock, sleep=clock.sleep, **(fields | overrides))


def test_a_structured_reply_is_parsed_into_the_schema_with_usage():
    outcome = structured(FakeChatModel([fake_reply('{"name": "Ada", "skills": ["python"]}', input_tokens=50)]))
    assert outcome.value == Reply(name="Ada", skills=["python"]) and outcome.error is None
    assert outcome.result.prompt_tokens == 50


def test_a_reply_that_misses_the_schema_is_returned_as_an_error_not_raised():
    outcome = structured(FakeChatModel(['{"name": "Ada"}']))
    assert outcome.value is None and outcome.error is not None and outcome.error.startswith("schema:")
    assert "Ada" not in outcome.error  # never the reply text (it may be a résumé)
    assert outcome.result.text == '{"name": "Ada"}'


def test_a_transport_error_on_a_structured_call_is_retried_like_any_other():
    model = FakeChatModel([gx.ServiceUnavailable("down"), '{"name": "Ada", "skills": []}'])
    outcome = structured(model)
    assert outcome.value is not None and outcome.result.attempts == 2


# --- tracing --------------------------------------------------------------------------------------------------------


def traced(replies) -> tuple[FakeChatModel, FakeClient]:
    client = FakeClient()
    model = FakeChatModel(replies)
    model.callbacks = [TracerHandle(Tracer(client))]
    return model, client


def test_a_traced_model_records_one_generation_per_call_across_retries():  # FR5
    model, client = traced([gx.ServiceUnavailable("down"), fake_reply("ok", input_tokens=9)])
    call(model)

    [generation] = client.generations
    assert generation.kwargs["name"] == "job_description_summary"
    assert generation.final["metadata"]["attempts"] == 2
    assert generation.final["usage_details"]["input"] == 9


def test_a_traced_call_that_fails_records_the_error():
    model, client = traced([gx.PermissionDenied("no")])
    with pytest.raises(LLMRequestError):
        call(model)
    [generation] = client.generations
    assert generation.final["level"] == "ERROR" and "LLMRequestError" in generation.final["status_message"]


def test_an_untraced_model_runs_without_a_tracer():
    assert call(FakeChatModel(["ok"])).text == "ok"
