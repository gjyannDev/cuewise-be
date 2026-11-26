"""The job-description summary on the LangChain layer (`summarize_job_description`, spec FR8, AC6, EC3, EC4, EC6):
same messages, time cap, validation and log lines as before the migration. The fake chat model; no network."""

import pytest
from google.api_core import exceptions as gx

from app.core.ai.chat_fake import FakeChatModel, fake_reply
from app.core.ai.chat_tracing import TracerHandle
from app.core.ai.tracing import Tracer
from app.core.config import settings
from app.modules.interviews.ai.interviews_summary import summarize_job_description
from app.modules.interviews.constants.interviews_constants import (
    SUMMARY_TASK,
    SUMMARY_TIME_CAP_SECONDS,
)
from app.modules.interviews.constants.interviews_prompt_registry import SUMMARY_VERSION
from tests.core.ai.test_tracing import FakeClient

JD = "We build booking software for fitness studios in TypeScript and React, with a Python API. " * 9
SUMMARY = "Booking software for fitness studios: TypeScript, React, Python API."


@pytest.fixture(autouse=True)
def no_retry_waits(monkeypatch):
    # Retries are RetryPolicy's (tested in tests/core/ai); here a transport error should fail at once.
    monkeypatch.setattr(settings, "llm_max_retries", 0)


def llm_lines(app_logs):
    return [r.getMessage() for r in app_logs.records if r.name == "app.llm"]


def test_a_valid_summary_is_returned_and_logged_as_ok(app_logs):
    model = FakeChatModel([fake_reply(SUMMARY, input_tokens=420, output_tokens=30)])

    assert summarize_job_description(model, JD, max_tokens=4000).summary == SUMMARY

    [line] = [m for m in llm_lines(app_logs) if "outcome=summary" in m]
    assert "outcome=summary_ok" in line and f"prompt_version={SUMMARY_VERSION}" in line and "prompt_tokens=420" in line
    assert "fitness" not in " ".join(llm_lines(app_logs))  # usage is logged, never the text


def test_the_call_sends_the_apps_summary_messages_within_its_time_cap():
    model = FakeChatModel([SUMMARY])
    summarize_job_description(model, JD, max_tokens=4000)

    [(messages, kwargs)] = model.calls
    assert [m.type for m in messages] == ["system", "human"]
    assert "<job_description>" in str(messages[1].content) and "Python API." in str(messages[1].content)
    assert kwargs["timeout"] <= SUMMARY_TIME_CAP_SECONDS and kwargs["max_output_tokens"] == 4000


def test_braces_in_the_job_description_are_sent_as_text_not_read_as_a_template():
    jd = JD + " Our stack: {python} and {{react}}."
    model = FakeChatModel([SUMMARY])
    summarize_job_description(model, jd, max_tokens=4000)
    assert "{python} and {{react}}" in str(model.calls[0][0][1].content)


def test_a_transport_failure_keeps_the_original_and_logs_its_class(app_logs):  # EC3
    model = FakeChatModel([gx.DeadlineExceeded("slow")])

    assert summarize_job_description(model, JD, max_tokens=4000).summary is None
    assert any("outcome=summary_failed:LLMTimeoutError" in m for m in llm_lines(app_logs))


@pytest.mark.parametrize(("reply", "reason"), [(JD + " more", "not_shorter"), ("x" * 501, "too_long")])
def test_an_invalid_summary_keeps_the_original_and_logs_why(app_logs, reply, reason):  # EC4
    model = FakeChatModel([reply])

    assert summarize_job_description(model, JD, max_tokens=4000).summary is None
    assert any(f"outcome=summary_invalid:{reason}" in m for m in llm_lines(app_logs))


def test_an_empty_reply_is_a_failed_summary(app_logs):  # the helper's empty check, as the old provider's
    assert summarize_job_description(FakeChatModel(["  "]), JD, max_tokens=4000).summary is None
    assert any("outcome=summary_failed:LLMBadResponseError" in m for m in llm_lines(app_logs))


def test_an_unknown_exception_keeps_the_original(app_logs):  # EC6
    assert summarize_job_description(FakeChatModel([KeyError("odd")]), JD, max_tokens=4000).summary is None
    assert any("outcome=summary_failed:LLMError" in m for m in llm_lines(app_logs))


def test_the_generation_carries_the_summary_task_and_prompt_version():  # FR5, AC8
    client = FakeClient()
    model = FakeChatModel([SUMMARY])
    model.callbacks = [TracerHandle(Tracer(client))]

    summarize_job_description(model, JD, max_tokens=4000)

    [generation] = client.generations
    assert generation.kwargs["name"] == SUMMARY_TASK
    assert generation.kwargs["metadata"] == {"task": SUMMARY_TASK, "prompt_version": SUMMARY_VERSION}
    assert generation.final["output"] == SUMMARY  # the summary is not redacted (as today)
