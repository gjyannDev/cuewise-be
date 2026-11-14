"""Answer turns of an interview that uses the candidate's profile (resume-aware-interview Step 7; seam S4).

AC4, AC6, AC9, AC10, EC3, EC4. The profile is read live on every turn (before the read transaction is released), so a
DELETE or a replace takes effect on the next main question. Follow-ups and the decide call never carry it.
"""

import json
import uuid

import pytest
from sqlalchemy import select

from app.modules.interviews.constants.interviews_constants import (
    INTERVIEWER_V4_PROMPT_VERSION,
    INTERVIEWER_V8_JSON_PROMPT_VERSION,
    INTERVIEWER_V8_PROMPT_VERSION,
)
from app.modules.interviews.dependencies.models.interviews_model import (
    InterviewQuestion,
)
from app.modules.profile.schemas.profile_schema import CandidateProfile, Project, Role


def profile_of(marker: str) -> CandidateProfile:
    return CandidateProfile(
        skills=[f"{marker}-skill"],
        roles=[Role(title=f"{marker} Engineer", summary=f"{marker} summary.")],
        projects=[Project(name=f"{marker}-project", description=f"{marker} description.")],
    )


def sent(call) -> str:
    return "\n".join(m.content for m in call)


def question_at(db, session_id: str, position: int) -> InterviewQuestion:
    db.expire_all()
    query = select(InterviewQuestion).where(
        InterviewQuestion.session_id == uuid.UUID(session_id), InterviewQuestion.position == position
    )
    return db.scalars(query).one()


@pytest.fixture
def opted_in(start_interview, make_user, store_profile, llm):
    """A user with profile ZZOLD and an interview started with use_profile; returns (user, session_id, question_id)."""
    user = make_user()
    store_profile(user, profile_of("ZZOLD"))
    body = start_interview(user, use_profile=True).json()
    return user, body["session"]["id"], body["current_question"]["id"]


def test_each_main_write_of_a_turn_carries_the_profile(opted_in, answer, llm, db):  # AC4
    user, session_id, question_id = opted_in
    llm.script()  # fresh call log for this turn

    r = answer(user, session_id, question_id)

    assert r.status_code < 300
    [write_call] = llm.fake.calls
    assert "<candidate_profile>" in sent(write_call) and "ZZOLD-project" in sent(write_call)
    assert question_at(db, session_id, 2).prompt_version == INTERVIEWER_V8_JSON_PROMPT_VERSION


def test_profile_deleted_mid_interview_makes_later_questions_profile_free(
    opted_in, answer, llm, db, delete_profile
):  # AC9, EC3, AC5
    user, session_id, question_id = opted_in
    delete_profile(user)
    llm.script()

    r = answer(user, session_id, question_id)

    assert r.status_code < 300
    [write_call] = llm.fake.calls
    assert "<candidate_profile>" not in sent(write_call) and "ZZOLD" not in sent(write_call)
    assert question_at(db, session_id, 2).prompt_version == INTERVIEWER_V4_PROMPT_VERSION


def test_profile_replaced_mid_interview_is_used_from_the_next_question(
    opted_in, answer, llm, store_profile
):  # AC9, EC4
    user, session_id, question_id = opted_in
    store_profile(user, profile_of("ZZNEW"))
    llm.script()

    answer(user, session_id, question_id)

    [write_call] = llm.fake.calls
    assert "ZZNEW-project" in sent(write_call) and "ZZOLD" not in sent(write_call)


def test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile(
    opted_in, answer, llm, decision_json
):  # AC6
    user, session_id, question_id = opted_in
    llm.script_decide(decision_json("follow_up", "missing_result"))
    llm.script(json.dumps({"question": "What changed for the team after that?"}))

    r = answer(user, session_id, question_id)

    assert r.status_code < 300 and r.json()["current_question"]["question_kind"] == "follow_up"
    [decide_call] = llm.decide.calls
    [write_call] = llm.fake.calls
    assert "ZZOLD" not in sent(decide_call) and "ZZOLD" not in sent(write_call)


def test_the_streamed_turn_reads_the_profile_too(opted_in, stream_answer, llm, db):  # AC4 (stream route)
    user, session_id, question_id = opted_in
    llm.script()

    turn = stream_answer(user, session_id, question_id)

    assert turn.status_code == 200
    [write_call] = llm.fake.calls
    assert "ZZOLD-project" in sent(write_call)
    assert question_at(db, session_id, 2).prompt_version == INTERVIEWER_V8_PROMPT_VERSION


def test_a_turn_logs_no_profile_content(opted_in, answer, llm, app_logs):  # AC10
    user, session_id, question_id = opted_in

    answer(user, session_id, question_id)

    assert not [rec for rec in app_logs.records if "ZZOLD" in rec.getMessage()]
