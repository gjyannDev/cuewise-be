import logging

import pytest

from app.core.ai.provider import LLMBadResponseError, LLMRequestError, LLMResult, LLMServerError, LLMTimeoutError

ANSWER = "My answer mentions the ACME-42 incident and my phone number 555-0100."
REACTION = "Handling the ACME-42 incident calmly shows ownership."
JOB_DESCRIPTION = "Confidential: ACME migration roadmap"


@pytest.fixture
def started(make_user, start_interview):
    owner = make_user()
    created = start_interview(owner, question_count=3, job_description=JOB_DESCRIPTION).json()
    return owner, created["session"]["id"], created["current_question"]


def llm_records(app_logs):
    return [r for r in app_logs.records if r.name == "app.llm"]


def test_one_log_line_per_call_with_usage_fields(answer, started, llm, app_logs):  # AC15, concept 9
    owner, session_id, q1 = started
    llm.script(
        LLMResult(
            text=REACTION,
            model="vendor/model-x",
            prompt_tokens=212,
            completion_tokens=18,
            latency_ms=1840,
            finish_reason="stop",
            attempts=2,
        )
    )

    answer(owner, session_id, q1["id"], text=ANSWER)

    [record] = llm_records(app_logs)
    assert record.levelno == logging.INFO
    message = record.getMessage()
    for expected in (
        f"session={session_id}",
        "model=vendor/model-x",
        "prompt_version=reaction_v1",
        "prompt_tokens=212",
        "completion_tokens=18",
        "latency_ms=1840",
        "attempts=2",
        "finish=stop",
        "outcome=ok",
    ):
        assert expected in message
    assert record.request_id != "-"  # tied to the HTTP request that caused it


def test_reply_cut_off_by_max_tokens_is_visible_in_the_log(answer, started, llm, app_logs):  # EC16
    owner, session_id, q1 = started
    llm.script(
        LLMResult(
            text="Handling the incident",
            model="m",
            prompt_tokens=10,
            completion_tokens=4,
            latency_ms=5,
            finish_reason="length",
            attempts=1,
        )
    )

    r = answer(owner, session_id, q1["id"])

    assert r.json()["reaction"]["text"] == "Handling the incident"
    assert "finish=length" in llm_records(app_logs)[0].getMessage()


@pytest.mark.parametrize(
    ("failure", "level", "outcome"),
    [
        (LLMTimeoutError("timed out"), logging.WARNING, "outcome=LLMTimeoutError"),
        (LLMServerError("503", status_code=503), logging.WARNING, "outcome=LLMServerError"),
        (LLMRequestError("bad key", status_code=401), logging.ERROR, "outcome=LLMRequestError"),
        (LLMBadResponseError("garbage"), logging.ERROR, "outcome=LLMBadResponseError"),
        ("   ", logging.WARNING, "outcome=empty_reply"),
    ],
    ids=["timeout", "server-error", "bad-key", "bad-response", "blank"],
)
def test_failures_are_logged_once_at_the_right_level(
    answer, started, llm, app_logs, failure, level, outcome
):  # EC11, EC12
    owner, session_id, q1 = started
    if isinstance(failure, Exception):
        failure.attempts = 3
    llm.script(failure)

    answer(owner, session_id, q1["id"])

    [record] = llm_records(app_logs)
    assert record.levelno == level
    assert outcome in record.getMessage()
    assert f"session={session_id}" in record.getMessage()


def test_failure_line_reports_attempts(answer, started, llm, app_logs):  # EC11
    owner, session_id, q1 = started
    error = LLMServerError("503", status_code=503)
    error.attempts = 3
    llm.script(error)

    answer(owner, session_id, q1["id"])

    assert "attempts=3" in llm_records(app_logs)[0].getMessage()


def test_no_personal_text_or_secret_reaches_any_log(answer, started, llm, app_logs):  # AC15, privacy
    owner, session_id, q1 = started
    llm.script(REACTION, LLMRequestError("bad key", status_code=401))

    q2 = answer(owner, session_id, q1["id"], text=ANSWER).json()["current_question"]
    answer(owner, session_id, q2["id"], text=ANSWER)

    everything = "\n".join(r.getMessage() for r in app_logs.records)
    for secret in ("ACME-42", "555-0100", "ACME migration", REACTION):
        assert secret not in everything


def test_no_llm_line_when_the_llm_is_off(answer, started, app_logs):  # EC18
    owner, session_id, q1 = started

    answer(owner, session_id, q1["id"])

    assert llm_records(app_logs) == []
