"""Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider wrapper (one generation per LLM call).

A fake Langfuse client records what the SDK would be told, so no test touches the network. langfuse-tracing AC2-AC10.
"""

import contextlib
from contextlib import contextmanager

import pytest

from app.core.ai.fake import FakeProvider, FakeStream
from app.core.ai.provider import ChatMessage, LLMResult, LLMServerError, LLMTimeoutError
from app.core.ai.tracing import Tracer, TracingProvider, build_tracer
from app.core.config import Settings

pytestmark = pytest.mark.anyio

MESSAGES = [ChatMessage(role="system", content="Be brief."), ChatMessage(role="user", content="Hello there")]
LABELS = {"task": "interviewer", "prompt_version": "v3", "budget_left_ms": 12000}


class FakeObservation:
    def __init__(self, client, kwargs):
        self.kwargs, self.updates, self.ended = kwargs, [], 0
        self.trace_id = "trace-1"
        self._client = client

    def update(self, **kwargs):
        if self._client.fail:
            raise RuntimeError("langfuse down")
        self.updates.append(kwargs)

    def end(self):
        self.ended += 1

    @property
    def final(self) -> dict:
        merged = dict(self.kwargs)
        for update in self.updates:
            merged.update(update)
        return merged


class FakeClient:
    def __init__(self, fail=False):
        self.fail = fail
        self.generations: list[FakeObservation] = []
        self.traces: list[FakeObservation] = []
        self.scores: list[dict] = []
        self.datasets: list[dict] = []
        self.dataset_items: list[dict] = []
        self.span_updates: list[dict] = []
        self.flushed = self.shut_down = 0

    def start_observation(self, **kwargs):
        if self.fail:
            raise RuntimeError("langfuse down")
        gen = FakeObservation(self, kwargs)
        self.generations.append(gen)
        return gen

    @contextmanager
    def start_as_current_observation(self, **kwargs):
        if self.fail:
            raise RuntimeError("langfuse down")
        span = FakeObservation(self, kwargs)
        self.traces.append(span)
        yield span
        span.end()

    def flush(self):
        self.flushed += 1
        if self.fail:
            raise RuntimeError("flush failed")

    def create_score(self, **kwargs):
        if self.fail:
            raise RuntimeError("langfuse down")
        self.scores.append(kwargs)

    def create_dataset(self, **kwargs):
        if self.fail:
            raise RuntimeError("langfuse down")
        self.datasets.append(kwargs)

    def create_dataset_item(self, **kwargs):
        if self.fail:
            raise RuntimeError("langfuse down")
        self.dataset_items.append(kwargs)

    def update_current_span(self, **kwargs):
        if self.fail:
            raise RuntimeError("langfuse down")
        self.span_updates.append(kwargs)

    def shutdown(self):
        self.shut_down += 1


@pytest.fixture
def propagated():
    return []


@pytest.fixture
def client():
    return FakeClient()


@pytest.fixture
def tracer(client, propagated):
    @contextmanager
    def fake_propagate(**attrs):
        propagated.append(attrs)
        yield

    return Tracer(client, propagate=fake_propagate)


def result(text="Tell me about a bug.", **overrides):
    fields = dict(
        text=text, model="gemini-test", prompt_tokens=40, completion_tokens=12, latency_ms=350, finish_reason="stop",
        attempts=1, cached_tokens=8, reasoning_tokens=3,
    )
    return LLMResult(**{**fields, **overrides})


def traced(tracer, *replies):
    return TracingProvider(FakeProvider(replies), tracer)


async def drain(stream):
    return [item async for item in stream]


# --- complete ---------------------------------------------------------------------------------------------------


def test_complete_records_one_generation_with_full_content_and_usage(tracer, client):  # AC2, AC4
    provider = traced(tracer, result())

    out = provider.complete(MESSAGES, max_tokens=100, trace_labels=LABELS)

    assert out.text == "Tell me about a bug."
    [gen] = client.generations
    final = gen.final
    assert final["as_type"] == "generation"
    assert final["name"] == "interviewer"
    assert final["input"] == [{"role": "system", "content": "Be brief."}, {"role": "user", "content": "Hello there"}]
    assert final["output"] == "Tell me about a bug."
    assert final["model"] == "gemini-test"
    assert final["usage_details"] == {
        "input": 40, "output": 12, "input_cached_tokens": 8, "output_reasoning_tokens": 3,
    }
    assert final["metadata"] == {
        "task": "interviewer", "prompt_version": "v3", "budget_left_ms": 12000,
        "attempts": 1, "finish_reason": "stop", "latency_ms": 350,
    }
    assert gen.ended == 1


def test_missing_usage_is_omitted_never_guessed(tracer, client):  # AC4, EC8
    provider = traced(tracer, result(prompt_tokens=None, completion_tokens=None, cached_tokens=None, reasoning_tokens=None))

    provider.complete(MESSAGES, max_tokens=100)

    assert "usage_details" not in client.generations[0].final


def test_retried_call_is_one_generation_with_attempts(tracer, client):  # AC5
    provider = traced(tracer, result(attempts=3))

    provider.complete(MESSAGES, max_tokens=100, trace_labels=LABELS)

    assert len(client.generations) == 1
    assert client.generations[0].final["metadata"]["attempts"] == 3


def test_failed_call_is_marked_error_and_the_same_exception_is_raised(tracer, client):  # AC6, EC5
    error = LLMServerError("LLM provider error", status_code=503)
    error.attempts, error.latency_ms = 3, 900
    provider = traced(tracer, error)

    with pytest.raises(LLMServerError) as raised:
        provider.complete(MESSAGES, max_tokens=100, trace_labels=LABELS)

    assert raised.value is error
    final = client.generations[0].final
    assert final["level"] == "ERROR"
    assert final["status_message"] == "LLMServerError status=503"
    assert final["metadata"]["attempts"] == 3
    assert client.generations[0].ended == 1


def test_sdk_failure_never_changes_the_llm_result(propagated):  # AC9, EC4
    broken = Tracer(FakeClient(fail=True), propagate=lambda **_: contextlib.nullcontext())
    provider = traced(broken, result())

    assert provider.complete(MESSAGES, max_tokens=100, trace_labels=LABELS).text == "Tell me about a bug."


def test_sdk_failure_does_not_mask_the_llm_error():  # AC9, EC4, EC5
    broken = Tracer(FakeClient(fail=True), propagate=lambda **_: contextlib.nullcontext())
    provider = traced(broken, LLMTimeoutError("LLM request timed out"))

    with pytest.raises(LLMTimeoutError):
        provider.complete(MESSAGES, max_tokens=100)


def test_disabled_tracer_is_a_pass_through():  # AC8, EC1
    provider = TracingProvider(FakeProvider([result()]), Tracer(None))

    assert provider.complete(MESSAGES, max_tokens=100, trace_labels=LABELS).text == "Tell me about a bug."


def test_call_without_labels_still_gets_a_name(tracer, client):  # EC9
    traced(tracer, result()).complete(MESSAGES, max_tokens=100)

    assert client.generations[0].final["name"] == "llm-call"


# --- stream -----------------------------------------------------------------------------------------------------


async def test_stream_records_the_joined_text_and_final_usage(tracer, client):  # AC3, AC4
    provider = traced(tracer, result("What was the bug"))

    items = await drain(provider.stream(MESSAGES, max_tokens=100, trace_labels=LABELS))

    assert isinstance(items[-1], LLMResult)
    [gen] = client.generations
    assert gen.final["output"] == "What was the bug"
    assert gen.final["usage_details"]["input"] == 40
    assert gen.final["metadata"]["finish_reason"] == "stop"
    assert gen.ended == 1


async def test_stream_closed_early_is_warning_cancelled_with_partial_text(tracer, client):  # AC7, EC6, EC7
    provider = traced(tracer, FakeStream(["One ", "two ", "three"]))

    stream = provider.stream(MESSAGES, max_tokens=100, trace_labels=LABELS)
    assert await anext(stream) == "One "
    assert await anext(stream) == "two "
    await stream.aclose()

    [gen] = client.generations
    assert gen.final["level"] == "WARNING"
    assert gen.final["status_message"] == "cancelled"
    assert gen.final["output"] == "One two "
    assert gen.ended == 1


async def test_stream_closed_after_the_final_result_stays_a_success(tracer, client):  # AC7
    provider = traced(tracer, result("Done."))

    stream = provider.stream(MESSAGES, max_tokens=100)
    async for item in stream:
        if isinstance(item, LLMResult):
            break
    await stream.aclose()

    assert "level" not in client.generations[0].final
    assert client.generations[0].ended == 1


async def test_stream_failure_is_error_with_partial_text_and_reraised(tracer, client):  # AC6
    error = LLMServerError("LLM connection failed")
    provider = traced(tracer, FakeStream(["Half "], error=error))

    with pytest.raises(LLMServerError) as raised:
        await drain(provider.stream(MESSAGES, max_tokens=100, trace_labels=LABELS))

    assert raised.value is error
    final = client.generations[0].final
    assert final["level"] == "ERROR"
    assert final["output"] == "Half "
    assert client.generations[0].ended == 1


async def test_stream_sdk_failure_does_not_change_the_stream():  # AC9
    broken = Tracer(FakeClient(fail=True), propagate=lambda **_: contextlib.nullcontext())
    provider = traced(broken, result("Fine."))

    items = await drain(provider.stream(MESSAGES, max_tokens=100))

    assert items[-1].text == "Fine."


# --- trace boundary ---------------------------------------------------------------------------------------------


def test_trace_sets_name_user_session_environment_and_input(tracer, client, propagated):  # AC1, AC2
    with tracer.trace("answer-turn", user_id="u-1", session_id="s-1", input={"answer": "I fixed it"}):
        pass

    [span] = client.traces
    assert span.kwargs["name"] == "answer-turn"
    assert span.kwargs["input"] == {"answer": "I fixed it"}
    assert propagated == [{"user_id": "u-1", "session_id": "s-1"}]


def test_trace_with_a_broken_sdk_still_runs_the_body_and_keeps_its_exception():  # AC9
    broken = Tracer(FakeClient(fail=True), propagate=lambda **_: contextlib.nullcontext())
    ran = []

    with broken.trace("answer-turn", user_id="u", session_id="s"):
        ran.append(True)
    with pytest.raises(ValueError):
        with broken.trace("answer-turn", user_id="u", session_id="s"):
            raise ValueError("business error")

    assert ran == [True]


def test_trace_yields_the_trace_id_so_scores_can_attach_to_it(tracer):  # eval-langfuse AC1
    with tracer.trace("eval-case", user_id="eval", session_id="run-1") as trace_id:
        assert trace_id == "trace-1"


def test_trace_yields_none_when_tracing_is_off_or_broken():  # eval-langfuse AC7, EC1
    broken = Tracer(FakeClient(fail=True), propagate=lambda **_: contextlib.nullcontext())

    with Tracer(None).trace("eval-case", user_id="eval", session_id="run-1") as off:
        pass
    with broken.trace("eval-case", user_id="eval", session_id="run-1") as failed:
        pass

    assert (off, failed) == (None, None)


def test_trace_passes_tags_and_metadata_to_every_observation_under_it(tracer, propagated):  # eval-langfuse AC4
    with tracer.trace(
        "eval-case", user_id="eval", session_id="run-1", tags=["prompt:v4"], metadata={"repeat": "1"}
    ):
        pass

    assert propagated == [
        {"user_id": "eval", "session_id": "run-1", "tags": ["prompt:v4"], "metadata": {"repeat": "1"}}
    ]


# --- scores and datasets (eval runs) ----------------------------------------------------------------------------


def test_a_check_becomes_a_boolean_score_on_the_trace_with_its_detail(tracer, client):  # eval-langfuse AC1
    tracer.score("trace-1", "no_judgement", False, comment="great")
    tracer.score("trace-1", "case_passed", True)

    assert client.scores == [
        {"trace_id": "trace-1", "name": "no_judgement", "value": 0.0, "data_type": "BOOLEAN", "comment": "great"},
        {"trace_id": "trace-1", "name": "case_passed", "value": 1.0, "data_type": "BOOLEAN", "comment": None},
    ]


def test_score_makes_no_call_without_a_trace_id_or_when_tracing_is_off(client):  # eval-langfuse AC7
    Tracer(client).score(None, "case_passed", True)
    Tracer(None).score("trace-1", "case_passed", True)

    assert client.scores == []


def test_score_failure_is_swallowed(app_logs):  # eval-langfuse EC1
    Tracer(FakeClient(fail=True)).score("trace-1", "case_passed", True)

    [warning] = [r for r in app_logs.records if r.name == "app.llm"]
    assert "score" in warning.getMessage() and "RuntimeError" in warning.getMessage()


def test_the_trace_output_is_set_on_the_current_trace(tracer, client):  # eval-langfuse readable traces
    with tracer.trace("eval-case", user_id="eval", session_id="run-1"):
        tracer.set_trace_output({"verdict": "PASS"})

    assert client.span_updates == [{"output": {"verdict": "PASS"}}]


def test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises(app_logs):
    Tracer(None).set_trace_output({"verdict": "PASS"})
    Tracer(FakeClient(fail=True)).set_trace_output({"verdict": "PASS"})

    [warning] = [r for r in app_logs.records if r.name == "app.llm"]
    assert "RuntimeError" in warning.getMessage()


ITEMS = [
    {"id": "write:strong-1", "input": {"answer": "a"}, "expected_output": None, "metadata": {"kind": "strong"}},
    {"id": "write:vague-1", "input": {"answer": "b"}, "expected_output": None, "metadata": {"kind": "vague"}},
]


def test_upsert_dataset_creates_the_dataset_then_each_item_with_its_own_id(tracer, client):  # eval-langfuse AC5, AC6
    assert tracer.upsert_dataset("interviews-eval/write", ITEMS) is True

    assert [d["name"] for d in client.datasets] == ["interviews-eval/write"]
    assert [i["id"] for i in client.dataset_items] == ["write:strong-1", "write:vague-1"]
    assert all(i["dataset_name"] == "interviews-eval/write" for i in client.dataset_items)


def test_upserting_twice_sends_the_same_ids_so_nothing_duplicates(tracer, client):  # eval-langfuse AC5
    tracer.upsert_dataset("interviews-eval/write", ITEMS)
    tracer.upsert_dataset("interviews-eval/write", ITEMS)

    ids = [i["id"] for i in client.dataset_items]
    assert ids == ["write:strong-1", "write:vague-1"] * 2


def test_upsert_dataset_reports_false_when_off_or_failing_and_never_raises():  # eval-langfuse AC7, EC2
    assert Tracer(None).upsert_dataset("d", ITEMS) is False
    assert Tracer(FakeClient(fail=True)).upsert_dataset("d", ITEMS) is False


# --- flush / shutdown -------------------------------------------------------------------------------------------


def test_close_flushes_then_shuts_down(tracer, client):  # AC10
    tracer.close()

    assert (client.flushed, client.shut_down) == (1, 1)


def test_close_survives_a_failing_flush():  # AC10, EC10
    client = FakeClient(fail=True)

    Tracer(client).close()

    assert client.shut_down == 1


def test_close_on_a_disabled_tracer_does_nothing():  # AC8
    Tracer(None).close()


# --- build_tracer -----------------------------------------------------------------------------------------------


def _settings(monkeypatch, **env):
    for name in ("LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_BASE_URL", "APP_ENV"):
        monkeypatch.delenv(name, raising=False)
    for name, value in env.items():
        monkeypatch.setenv(name, value)
    return Settings(_env_file=None)  # pyright: ignore[reportCallIssue]


def test_no_keys_builds_a_disabled_tracer_without_warning(monkeypatch, app_logs):  # AC8, EC1
    tracer = build_tracer(_settings(monkeypatch))

    assert tracer.enabled is False
    assert [r for r in app_logs.records if r.name == "app.llm"] == []


def test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value(monkeypatch, app_logs):  # AC8, EC2
    tracer = build_tracer(_settings(monkeypatch, LANGFUSE_PUBLIC_KEY="pk-lf-secretvalue"))

    assert tracer.enabled is False
    [warning] = [r for r in app_logs.records if r.name == "app.llm"]
    assert "LANGFUSE" in warning.getMessage()
    assert "secretvalue" not in warning.getMessage()


def test_both_keys_build_an_enabled_tracer(monkeypatch):  # AC1
    tracer = build_tracer(
        _settings(monkeypatch, LANGFUSE_PUBLIC_KEY="pk-lf-test", LANGFUSE_SECRET_KEY="sk-lf-test", LANGFUSE_BASE_URL="http://localhost:9"),
        environment="eval",
    )

    assert tracer.enabled is True
    tracer.close()
