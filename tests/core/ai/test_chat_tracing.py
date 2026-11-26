"""The LangChain tracing callback (spec FR5, AC8, EC14, EC15): one Langfuse generation per call, through our Tracer,
with the same labels, redaction and usage as `TracingProvider`. A fake chat model and a recording Langfuse client; no
network."""

from app.core.ai.chat_fake import FakeChatModel
from app.core.ai.chat_tracing import ChatTrace
from app.core.ai.provider import LLMResult, LLMServerError
from app.core.ai.tracing import REDACT_LABEL, REDACTED, Tracer
from tests.core.ai.test_tracing import FakeClient

LABELS = {"task": "job_description_summary", "prompt_version": "job_description_summary_v2"}
MESSAGES = [("system", "Summarize the job description."), ("human", "<job_description>\nA role\n</job_description>")]


def result(**overrides) -> LLMResult:
    fields = {
        "text": "A summary.",
        "model": "gemini-test",
        "prompt_tokens": 120,
        "completion_tokens": 30,
        "reasoning_tokens": 4,
        "latency_ms": 850,
        "finish_reason": "STOP",
        "attempts": 1,
    }
    return LLMResult(**(fields | overrides))


def traced_call(client, labels=LABELS, *, attempts=1, params=None):
    trace = ChatTrace(Tracer(client), labels, params or {"max_tokens": 4000})
    model = FakeChatModel()
    for _ in range(attempts):
        model.invoke(MESSAGES, config={"callbacks": [trace]})
    return trace


def test_a_call_records_one_generation_with_its_messages_labels_and_usage():
    client = FakeClient()
    traced_call(client).succeed(result())

    [generation] = client.generations
    assert generation.kwargs["name"] == "job_description_summary"
    assert generation.kwargs["as_type"] == "generation"
    assert generation.kwargs["input"] == [
        {"role": "system", "content": "Summarize the job description."},
        {"role": "user", "content": "<job_description>\nA role\n</job_description>"},
    ]
    assert generation.kwargs["model_parameters"] == {"max_tokens": 4000}
    final = generation.final
    assert final["output"] == "A summary." and final["model"] == "gemini-test"
    assert final["usage_details"] == {"input": 120, "output": 30, "output_reasoning_tokens": 4}
    assert final["metadata"]["prompt_version"] == "job_description_summary_v2"
    assert final["metadata"]["latency_ms"] == 850 and generation.ended == 1


def test_retried_attempts_are_still_one_generation_with_the_attempt_count():  # like TracingProvider
    client = FakeClient()
    traced_call(client, attempts=3).succeed(result(attempts=3))

    [generation] = client.generations
    assert generation.final["metadata"]["attempts"] == 3


def test_a_redacted_call_records_the_placeholder_for_input_and_output():  # EC14, AC8
    client = FakeClient()
    traced_call(client, {**LABELS, REDACT_LABEL: True}).succeed(result(text="Ada, Python, 5 years"))

    [generation] = client.generations
    assert generation.kwargs["input"] == REDACTED
    assert generation.final["output"] == REDACTED
    assert "Ada" not in repr(generation.final) and "job_description" not in repr(generation.kwargs["input"])
    assert generation.final["usage_details"]["input"] == 120  # cost stays visible


def test_a_failed_call_records_an_error_with_the_error_class():
    client = FakeClient()
    error = LLMServerError("down", status_code=503)
    error.attempts = 3
    traced_call(client).fail(error)

    [generation] = client.generations
    assert generation.final["level"] == "ERROR"
    assert generation.final["status_message"] == "LLMServerError status=503"
    assert generation.final["metadata"]["attempts"] == 3


def test_a_call_that_never_reached_the_model_still_records_its_failure():  # budget spent before the first attempt
    client = FakeClient()
    ChatTrace(Tracer(client), LABELS, {}).fail(LLMServerError("not sent"))

    [generation] = client.generations
    assert generation.kwargs["input"] == [] and generation.final["level"] == "ERROR"


def test_a_langfuse_failure_never_fails_the_call(app_logs):  # EC15
    client = FakeClient(fail=True)
    trace = traced_call(client)
    trace.succeed(result())  # must not raise

    assert client.generations == []
    assert any(r.getMessage().startswith("langfuse_failed") for r in app_logs.records)


def test_a_disabled_tracer_records_nothing():
    trace = ChatTrace(Tracer(None), LABELS, {})
    FakeChatModel().invoke(MESSAGES, config={"callbacks": [trace]})
    trace.succeed(result())  # nothing to record, nothing raised
