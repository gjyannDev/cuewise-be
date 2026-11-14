"""Starting an interview with the candidate's profile (resume-aware-interview Step 6; seam S4).

AC2, AC4, AC8, AC10, EC1, EC9, EC10. The profile is read live through the profile service, for the owner only, before
any model or embedding call; without one the start is refused and nothing is created.
"""

import uuid

import pytest
from sqlalchemy import select

from app.core.ai.fake import FakeEmbedder
from app.main import app
from app.modules.interviews.constants.interviews_constants import (
    INTERVIEWER_V8_JSON_PROMPT_VERSION,
    PROFILE_REQUIRED_MESSAGE,
    SessionStatus,
)
from app.modules.interviews.dependencies.interviews_shared_dependencies import (
    get_embedder,
)
from app.modules.interviews.dependencies.models.interviews_model import (
    InterviewQuestion,
    InterviewSession,
)
from app.modules.profile.models.profile_model import CandidateProfileRow
from app.modules.profile.schemas.profile_schema import CandidateProfile, Project, Role

JOB = "We build Python REST APIs for payments."


def profile_of(marker: str) -> CandidateProfile:
    """A synthetic profile whose every free-text field carries `marker`, so a leak anywhere is easy to find."""
    return CandidateProfile(
        skills=[f"{marker}-skill"],
        roles=[Role(title=f"{marker} Engineer", organization=f"{marker}-org", summary=f"{marker} summary.")],
        projects=[Project(name=f"{marker}-project", description=f"{marker} description.", technologies=["Go"])],
    )


@pytest.fixture
def embedder():
    fake = FakeEmbedder({})
    app.dependency_overrides[get_embedder] = lambda: fake
    yield fake
    app.dependency_overrides.pop(get_embedder, None)


def sessions(db, user) -> list[InterviewSession]:
    db.expire_all()
    return list(db.scalars(select(InterviewSession).where(InterviewSession.user_id == user.id)))


def first_question(db, response) -> InterviewQuestion:
    db.expire_all()
    session_id = uuid.UUID(response.json()["session"]["id"])
    return db.scalars(select(InterviewQuestion).where(InterviewQuestion.session_id == session_id)).one()


def sent(calls) -> str:
    return "\n".join(m.content for call in calls for m in call)


# --- refused ---


def test_flag_on_without_a_stored_profile_is_409_and_nothing_is_created_or_sent(
    start_interview, make_user, db, llm, embedder
):  # AC2, EC1
    user = make_user()

    r = start_interview(user, use_profile=True, job_description=JOB)

    assert r.status_code == 409
    assert r.json()["error"]["code"] == "PROFILE_REQUIRED"
    assert r.json()["error"]["message"] == PROFILE_REQUIRED_MESSAGE
    assert sessions(db, user) == []
    assert llm.fake.calls == [] and llm.decide.calls == []
    assert embedder.calls == []


def test_a_refused_start_leaves_the_interview_in_progress_alone(start_interview, make_user, db, llm):  # inferred
    user = make_user()
    assert start_interview(user).status_code == 201

    assert start_interview(user, use_profile=True).status_code == 409

    [only] = sessions(db, user)
    assert only.status == SessionStatus.in_progress


def test_another_users_profile_does_not_count(start_interview, make_user, store_profile, db, llm):  # AC8
    owner, other = make_user("owner@example.com"), make_user("other@example.com")
    store_profile(other, profile_of("ZZOTHER"))

    r = start_interview(owner, use_profile=True)

    assert r.status_code == 409 and sessions(db, owner) == []


def test_a_stored_profile_that_no_longer_validates_counts_as_none(
    start_interview, make_user, store_profile, db, llm, app_logs
):  # plan risk: a later schema change
    user = make_user()
    store_profile(user, profile_of("ZZALPHA"))
    row = db.scalars(select(CandidateProfileRow).where(CandidateProfileRow.user_id == user.id)).one()
    row.profile = {**row.profile, "skills": ["ZZALPHA"] * 99}  # over today's cap
    db.commit()

    r = start_interview(user, use_profile=True)

    assert r.status_code == 409 and r.json()["error"]["code"] == "PROFILE_REQUIRED"
    assert llm.fake.calls == []
    [line] = [rec.getMessage() for rec in app_logs.records if rec.getMessage().startswith("profile_unusable")]
    assert "ZZALPHA" not in line


# --- with a profile ---


def test_flag_on_with_a_profile_writes_the_first_question_with_it(
    start_interview, make_user, store_profile, db, llm
):  # AC1, AC3, AC4
    user = make_user()
    store_profile(user, profile_of("ZZALPHA"))

    r = start_interview(user, use_profile=True, job_description=JOB)

    assert r.status_code == 201
    assert r.json()["session"]["use_profile"] is True
    assert sessions(db, user)[0].use_profile is True
    [call] = llm.fake.calls
    assert "<candidate_profile>" in call[1].content and "ZZALPHA-project" in call[1].content
    assert "ZZALPHA-org" not in call[1].content  # organization is never sent (minimization)
    assert first_question(db, r).prompt_version == INTERVIEWER_V8_JSON_PROMPT_VERSION


def test_flag_off_never_reads_or_sends_an_existing_profile(
    start_interview, make_user, store_profile, db, llm
):  # EC2
    user = make_user()
    store_profile(user, profile_of("ZZALPHA"))

    r = start_interview(user, job_description=JOB)

    assert r.status_code == 201 and r.json()["session"]["use_profile"] is False
    assert "ZZALPHA" not in sent(llm.fake.calls)
    assert first_question(db, r).prompt_version != INTERVIEWER_V8_JSON_PROMPT_VERSION


def test_each_interview_gets_only_its_owners_profile(start_interview, make_user, store_profile, llm):  # AC8, EC10
    alice, bob = make_user("alice@example.com"), make_user("bob@example.com")
    store_profile(alice, profile_of("ZZALICE"))
    store_profile(bob, profile_of("ZZBOB"))

    start_interview(alice, use_profile=True)
    start_interview(bob, use_profile=True)

    alice_call, bob_call = llm.fake.calls
    assert "ZZALICE" in sent([alice_call]) and "ZZBOB" not in sent([alice_call])
    assert "ZZBOB" in sent([bob_call]) and "ZZALICE" not in sent([bob_call])


def test_with_the_llm_off_the_bank_asks_and_nothing_of_the_profile_is_stored(
    start_interview, make_user, store_profile, db
):  # EC9 (no llm fixture: the LLM is off)
    user = make_user()
    store_profile(user, profile_of("ZZALPHA"))

    r = start_interview(user, use_profile=True)

    assert r.status_code == 201
    question = first_question(db, r)
    assert question.source == "bank" and question.prompt_version is None
    assert "ZZALPHA" not in question.text


def test_no_profile_content_in_logs_or_the_response(
    start_interview, make_user, store_profile, llm, app_logs
):  # AC10
    user = make_user()
    store_profile(user, profile_of("ZZALPHA"))

    r = start_interview(user, use_profile=True, job_description=JOB)

    assert r.status_code == 201
    assert "ZZALPHA" not in r.text
    assert not [rec for rec in app_logs.records if "ZZALPHA" in rec.getMessage()]
