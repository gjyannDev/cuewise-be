"""A turn whose question cannot be written ends in one retryable error and saves nothing (U3c step 4: AC2, AC3, AC4;
EC3, EC3b, EC4, EC5, EC8). Blocking and streamed answers; the start is in test_start_llm.py."""

import json
import uuid

import pytest
from sqlalchemy import func, select

from app.core.ai.provider import LLMRequestError, LLMServerError
from app.core.config import settings
from app.modules.interviews.dependencies.models.interviews_model import (
    InterviewMessage,
    InterviewQuestion,
    InterviewSession,
)
from tests.provider_fakes import FakeStream

SERVER_DOWN = [LLMServerError("503 secret-vendor-host")] * (1 + settings.llm_max_retries)


def assert_nothing_saved(db, session_id):
    assert db.scalar(select(func.count()).select_from(InterviewMessage)) == 0
    assert db.scalar(select(func.count()).select_from(InterviewQuestion)) == 1  # only the first question
    assert db.get(InterviewSession, uuid.UUID(session_id)).current_position == 1


@pytest.fixture
def started(make_user, start_interview, llm, reply_json):
    llm.script(reply_json("Opening question?", "behavioral"))
    owner = make_user()
    created = start_interview(owner, interview_type="behavioral", question_count=3).json()
    return owner, created["session"]["id"], created["current_question"]["id"]


def assert_unavailable_body(body):
    error = body["error"]
    assert error["code"] == "INTERVIEWER_UNAVAILABLE"
    assert "try again" in error["message"].lower()
    assert "secret-vendor-host" not in json.dumps(body)


# --- blocking ---


def test_a_write_that_fails_ends_the_turn_and_saves_nothing(started, answer, llm, db):  # AC4, EC4
    owner, session_id, question_id = started
    llm.script(*SERVER_DOWN * 2)  # the first question was already written: these are the turn's calls

    r = answer(owner, session_id, question_id)

    assert r.status_code == 503
    assert_unavailable_body(r.json())
    assert_nothing_saved(db, session_id)


def test_two_invalid_writes_end_the_turn(started, answer, llm, db):  # AC3, EC3
    owner, session_id, question_id = started
    llm.script("not json", "still not json")

    r = answer(owner, session_id, question_id)

    assert r.status_code == 503
    assert_nothing_saved(db, session_id)
    assert len(llm.fake.calls) == 2


def test_a_failed_decide_also_ends_the_turn_without_a_write(started, answer, llm, db):  # EC3b
    owner, session_id, question_id = started
    llm.script_decide(*[LLMServerError("503")] * (1 + settings.llm_max_retries))

    r = answer(owner, session_id, question_id)

    assert r.status_code == 503
    assert_unavailable_body(r.json())
    assert_nothing_saved(db, session_id)
    assert len(llm.fake.calls) == 1  # only the opening question: no write call started after the failed decide


def test_the_last_answer_with_a_failed_decide_does_not_complete(make_user, start_interview, answer, llm, db):  # EC3b
    owner = make_user()
    created = start_interview(owner, question_count=1).json()
    llm.script_decide(LLMRequestError("bad key", status_code=401))

    r = answer(owner, created["session"]["id"], created["current_question"]["id"])

    assert r.status_code == 503
    assert db.get(InterviewSession, uuid.UUID(created["session"]["id"])).status == "in_progress"


def test_a_turn_that_fails_can_be_sent_again(started, answer, llm, db):  # the candidate resubmits the same answer
    owner, session_id, question_id = started
    llm.script(*SERVER_DOWN * 2)
    assert answer(owner, session_id, question_id).status_code == 503

    llm.script()  # the provider is back: every call now writes a valid question
    r = answer(owner, session_id, question_id)

    assert r.status_code == 201 and r.json()["current_question"]["position"] == 2


# --- streamed ---


def test_a_stream_with_every_provider_down_ends_in_one_error_event(started, stream_answer, llm, db):  # AC4, EC4
    owner, session_id, question_id = started
    llm.script(*SERVER_DOWN * 2)

    turn = stream_answer(owner, session_id, question_id)

    assert turn.names()[-1] == "error" and "done" not in turn.names()
    assert "reaction" not in turn.names()  # R3: no acknowledgement is shown for a turn that fails before any text
    [error] = turn.data("error")
    assert error["code"] == "INTERVIEWER_UNAVAILABLE" and error["request_id"]
    assert "secret-vendor-host" not in json.dumps(turn.events)
    assert_nothing_saved(db, session_id)


def test_a_stream_that_breaks_after_text_resets_then_fails(started, stream_answer, llm, db):  # AC2, EC5
    owner, session_id, question_id = started
    broken = FakeStream(["CATEGORY: behavioral\n", "How would "], error=LLMServerError("503"))
    llm.script(broken, broken)  # both attempts of the turn

    turn = stream_answer(owner, session_id, question_id)

    names = turn.names()
    assert names[-1] == "error" and "reset" in names
    assert names.index("reset") < names.index("error")  # the partial text is taken back before the failure
    assert turn.question() == ""
    assert_nothing_saved(db, session_id)


def test_a_failed_decide_ends_the_stream_in_an_error_event(started, stream_answer, llm, db):  # EC3b
    owner, session_id, question_id = started
    llm.script_decide(*[LLMServerError("503")] * (1 + settings.llm_max_retries))

    turn = stream_answer(owner, session_id, question_id)

    assert turn.names()[-1] == "error"
    assert turn.data("error")[0]["code"] == "INTERVIEWER_UNAVAILABLE"
    assert "question.delta" not in turn.names()
    assert_nothing_saved(db, session_id)
