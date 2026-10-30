import uuid

import pytest
from sqlalchemy import select

from app.core.ai.provider import LLMResult, LLMTimeoutError
from app.modules.interviews.interviews_constants import SUMMARY_THRESHOLD, SUMMARY_TIME_CAP_SECONDS
from app.modules.interviews.interviews_model import InterviewSession

LONG_JD = ("We build booking software for fitness studios in TypeScript and React, with a Python API. " * 9)[:900]
SUMMARY = "Booking software for fitness studios: TypeScript, React, Python API."


def stored_session(db, session_id):
    return db.scalars(select(InterviewSession).where(InterviewSession.id == uuid.UUID(session_id))).one()


def test_a_long_job_description_is_summarised_once_and_used_in_every_call(
    start_interview, make_user, answer, llm, reply_json, db
):  # AC8, EC9
    assert len(LONG_JD) > SUMMARY_THRESHOLD
    owner = make_user()
    llm.script(SUMMARY, reply_json("Opening question?", "behavioral"))
    created = start_interview(owner, job_description=LONG_JD, question_count=3).json()

    answer(owner, created["session"]["id"], created["current_question"]["id"])

    summary_call, first_call, second_call = llm.fake.calls
    assert "Python API." in summary_call[1].content
    assert llm.fake.budgets[0] == SUMMARY_TIME_CAP_SECONDS
    for call in (first_call, second_call):
        assert SUMMARY in call[1].content and LONG_JD not in " ".join(m.content for m in call)
    assert stored_session(db, created["session"]["id"]).job_description_summary == SUMMARY


@pytest.mark.parametrize("jd", [None, "Build APIs with FastAPI.", "x" * SUMMARY_THRESHOLD])
def test_a_short_or_missing_job_description_makes_no_extra_call(start_interview, make_user, llm, db, jd):  # EC8
    created = start_interview(make_user(), job_description=jd).json()

    assert len(llm.fake.calls) == 1
    assert stored_session(db, created["session"]["id"]).job_description_summary is None


@pytest.mark.parametrize(
    "failure",
    [LLMTimeoutError("slow"), "", LONG_JD + " more", "x" * 501],
    ids=["timeout", "empty", "not-shorter", "too-long"],
)
def test_an_unusable_summary_keeps_the_original_and_the_interview_starts(
    start_interview, make_user, answer, llm, reply_json, db, app_logs, failure
):  # AC9, EC10, EC11
    owner = make_user()
    llm.script(failure, reply_json("Opening question?", "behavioral"))

    r = start_interview(owner, job_description=LONG_JD, question_count=3)

    assert r.status_code == 201 and r.json()["current_question"]["text"] == "Opening question?"
    assert "fitness studios" in llm.fake.calls[1][1].content
    assert stored_session(db, r.json()["session"]["id"]).job_description_summary is None
    assert any("outcome=summary" in rec.getMessage() for rec in app_logs.records if rec.name == "app.llm")
    assert all("fitness" not in rec.getMessage() for rec in app_logs.records)


def test_garbage_for_the_summary_still_completes_an_interview(
    start_interview, make_user, answer, llm, reply_json
):  # AC9
    owner = make_user()
    llm.script("```not a summary```")
    created = start_interview(owner, job_description=LONG_JD, question_count=2).json()

    r = answer(owner, created["session"]["id"], created["current_question"]["id"])
    r = answer(owner, created["session"]["id"], r.json()["current_question"]["id"])

    assert r.json()["session"]["status"] == "completed"


def test_the_summary_is_never_returned_and_never_logged(
    start_interview, make_user, llm, reply_json, client, auth_header, app_logs
):  # AC10, AC11
    owner = make_user()
    llm.script(SUMMARY, reply_json("Opening question?", "behavioral"))

    r = start_interview(owner, job_description=LONG_JD)
    current = client.get(f"/api/v1/interviews/{r.json()['session']['id']}", headers=auth_header(owner))

    assert "Booking software" not in r.text + current.text
    assert all("Booking software" not in rec.getMessage() for rec in app_logs.records)


def test_summary_usage_is_logged_with_its_own_prompt_version(start_interview, make_user, llm, reply_json, app_logs):
    usage = LLMResult(
        text=SUMMARY, model="m", prompt_tokens=420, completion_tokens=30, latency_ms=7, finish_reason="stop", attempts=1
    )
    llm.script(usage, reply_json("Opening question?", "behavioral"))

    start_interview(make_user(), job_description=LONG_JD)

    [line] = [r.getMessage() for r in app_logs.records if r.name == "app.llm" and "summary" in r.getMessage()]
    assert "prompt_version=job_description_summary_v2" in line and "prompt_tokens=420" in line
    assert "outcome=summary_ok" in line


def test_without_an_llm_no_summary_is_made(start_interview, make_user, db):  # EC16
    created = start_interview(make_user(), job_description=LONG_JD).json()

    assert stored_session(db, created["session"]["id"]).job_description_summary is None
