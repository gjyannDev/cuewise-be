"""GET /interviews/{id}/questions/{qid}/speech and /messages/{mid}/speech: the interviewer's lines, spoken.

Spec: cuewise-fe docs/features/interview-room/spec.md (API Contract, Phase 1). The text always comes from the database;
every "not yours / not shown / not speakable / wrong route" case is the same 404.
"""

import uuid

import pytest
from sqlalchemy import select

from app.core.ai.provider import LLMServerError
from app.core.speech.limits import SPEECH_PER_MINUTE
from app.modules.interviews.dependencies.models.interviews_model import (
    InterviewMessage,
    InterviewQuestion,
    InterviewSession,
)
from app.modules.interviews.repositories.interviews_repository import (
    InterviewsRepository,
)
from app.modules.interviews.services.interviews_voice_service import VoiceService


@pytest.fixture
def started(make_user, start_interview):
    """An owner with a started backend interview: (owner, session_id, first question)."""
    owner = make_user(email="owner@example.com")
    created = start_interview(owner, question_count=3).json()
    return owner, created["session"]["id"], created["current_question"]


@pytest.fixture
def answered(started, answer):
    """The first question answered: (owner, session_id, q1, the reaction, q2)."""
    owner, session_id, q1 = started
    body = answer(owner, session_id, q1["id"]).json()
    return owner, session_id, q1, body["reaction"], body["current_question"]


def row(db, model, session_id, **where):
    query = select(model).where(model.session_id == uuid.UUID(session_id)).filter_by(**where)
    return db.scalars(query).first()


def code(response) -> str:
    return response.json()["error"]["code"]


# --- success (AC11) ---


def test_the_owner_hears_the_current_question_as_its_stored_text(speak, started, tts):
    owner, session_id, q1 = started
    tts.script(b"ID3question-audio")

    r = speak(owner, session_id, q1["id"])

    assert r.status_code == 200
    assert r.content == b"ID3question-audio"
    assert r.headers["content-type"] == "audio/mpeg"
    assert tts.fake is not None and tts.fake.calls == [q1["text"]]


def test_the_media_type_is_whatever_the_synthesizer_reported(speak, started, tts):
    owner, session_id, q1 = started
    tts.script(b"OggS-clip", content_type="audio/ogg")

    r = speak(owner, session_id, q1["id"])

    assert (r.status_code, r.headers["content-type"]) == (200, "audio/ogg")


def test_a_follow_up_question_is_spoken_the_same_way(
    start_interview, make_user, answer, speak, llm, reply_json, decision_json, tts
):
    owner = make_user()
    llm.script(reply_json("How would you design a rate limiter?", "technical"), '{"question": "Which algorithm, and why?"}')
    llm.script_decide(decision_json("follow_up", "no_tradeoff", "Named Redis only."))
    created = start_interview(owner, interview_type="technical", question_count=3).json()
    session_id = created["session"]["id"]
    follow = answer(owner, session_id, created["current_question"]["id"], text="I'd use Redis.").json()["current_question"]
    assert follow["question_kind"] == "follow_up"

    r = speak(owner, session_id, follow["id"])

    assert r.status_code == 200
    assert tts.fake is not None and tts.fake.calls == ["Which algorithm, and why?"]


def test_the_reaction_route_speaks_a_saved_reaction(speak, answered, tts):
    owner, session_id, _, reaction, _ = answered

    r = speak(owner, session_id, reaction["id"], route="messages")

    assert r.status_code == 200
    assert tts.fake is not None and tts.fake.calls == [reaction["text"]]


def test_the_next_question_is_speakable_once_it_is_shown(speak, answered, tts):
    owner, session_id, _, _, q2 = answered

    assert speak(owner, session_id, q2["id"]).status_code == 200


def test_a_finished_interviews_lines_can_still_be_replayed(speak, started, tts, db):  # EC13
    owner, session_id, q1 = started
    session = db.get(InterviewSession, uuid.UUID(session_id))
    session.status = "abandoned"
    db.commit()

    assert speak(owner, session_id, q1["id"]).status_code == 200


# --- every miss is the same 404 (EC22) ---


def assert_hidden(response, tts) -> None:
    assert response.status_code == 404
    assert code(response) == "NOT_FOUND"
    assert tts.fake is not None and tts.fake.calls == []


def test_another_users_interview_is_not_found(speak, started, make_user, tts):
    _, session_id, q1 = started
    stranger = make_user(email="stranger@example.com")

    assert_hidden(speak(stranger, session_id, q1["id"]), tts)


def test_an_unknown_session_or_line_is_not_found(speak, started, tts):
    owner, session_id, q1 = started

    assert_hidden(speak(owner, str(uuid.uuid4()), q1["id"]), tts)
    assert_hidden(speak(owner, session_id, str(uuid.uuid4())), tts)
    assert_hidden(speak(owner, session_id, str(uuid.uuid4()), route="messages"), tts)


def test_a_question_of_another_interview_is_not_found(speak, started, start_interview, tts):
    owner, session_id, _ = started
    other = start_interview(owner, question_count=3).json()

    assert_hidden(speak(owner, session_id, other["current_question"]["id"]), tts)


def test_a_question_not_shown_yet_is_not_found(speak, started, tts, db):
    # Today each question is stored when it is shown, so an "upcoming" row is inserted by hand: the guard must hold if
    # questions are ever stored ahead (pre-generated), or the endpoint would leak them.
    owner, session_id, _ = started
    upcoming = InterviewQuestion(
        session_id=uuid.UUID(session_id), position=2, text="SECRET upcoming question?", category="behavioral", source="bank"
    )
    db.add(upcoming)
    db.commit()

    assert_hidden(speak(owner, session_id, upcoming.id), tts)


def test_a_candidate_answer_is_never_spoken(speak, answered, tts, db):
    owner, session_id, *_ = answered
    candidate = row(db, InterviewMessage, session_id, role="candidate")
    assert candidate is not None

    assert_hidden(speak(owner, session_id, candidate.id, route="messages"), tts)


def test_an_id_sent_to_the_other_route_is_not_found(speak, answered, tts):
    owner, session_id, q1, reaction, _ = answered

    assert_hidden(speak(owner, session_id, reaction["id"], route="questions"), tts)
    assert_hidden(speak(owner, session_id, q1["id"], route="messages"), tts)


def test_every_miss_has_the_same_body(speak, answered, make_user, tts):  # review R2
    owner, session_id, q1, reaction, _ = answered
    stranger = make_user(email="stranger@example.com")
    misses = [
        speak(stranger, session_id, q1["id"]),  # not yours
        speak(owner, str(uuid.uuid4()), q1["id"]),  # no such session
        speak(owner, session_id, str(uuid.uuid4())),  # no such line
        speak(owner, session_id, q1["id"], route="messages"),  # wrong route
        speak(owner, session_id, reaction["id"], route="questions"),
    ]

    bodies = {(r.status_code, r.json()["error"]["code"], r.json()["error"]["message"]) for r in misses}
    assert bodies == {(404, "NOT_FOUND", "Interview not found")}


@pytest.mark.parametrize("kind", ["question", "reaction"])
def test_the_lookup_ends_its_db_transaction_before_the_slow_synthesis(answered, db, kind):  # review R1
    owner, session_id, q1, reaction, _ = answered
    service = VoiceService(InterviewsRepository(db), None, None)
    db.rollback()

    if kind == "question":
        line = service.prepare_question_speech(owner, uuid.UUID(session_id), uuid.UUID(q1["id"]))
    else:
        line = service.prepare_reaction_speech(owner, uuid.UUID(session_id), uuid.UUID(reaction["id"]))

    assert not db.in_transaction()
    assert line.text == (q1["text"] if kind == "question" else reaction["text"])  # copied out before the release


# --- unavailable, limits, auth ---


def test_no_synthesizer_configured_is_speech_unavailable(speak, started, tts):
    owner, session_id, q1 = started
    tts.disable()

    r = speak(owner, session_id, q1["id"])

    assert (r.status_code, code(r)) == (503, "SPEECH_UNAVAILABLE")


def test_a_vendor_failure_is_speech_unavailable(speak, started, tts):  # EC3
    owner, session_id, q1 = started
    tts.script(LLMServerError("down", status_code=503))

    r = speak(owner, session_id, q1["id"])

    assert (r.status_code, code(r)) == (503, "SPEECH_UNAVAILABLE")


def test_the_limit_is_shared_by_both_routes_and_says_when_to_retry(speak, answered, tts, transcribe, stt):  # EC4
    owner, session_id, q1, reaction, _ = answered
    for i in range(SPEECH_PER_MINUTE):
        route, line = ("questions", q1["id"]) if i % 2 else ("messages", reaction["id"])
        assert speak(owner, session_id, line, route=route).status_code == 200

    r = speak(owner, session_id, q1["id"])

    assert (r.status_code, code(r)) == (429, "RATE_LIMITED")
    assert int(r.headers["retry-after"]) > 0
    assert transcribe(owner, session_id).status_code == 200  # the transcription limit is a separate counter


def test_without_a_token_it_is_unauthorized(speak, started, tts):
    owner, session_id, q1 = started

    r = speak(owner, session_id, q1["id"], headers={})

    assert r.status_code == 401


def test_no_line_text_reaches_the_logs(speak, answered, tts, app_logs):
    owner, session_id, q1, reaction, q2 = answered

    speak(owner, session_id, q2["id"])
    speak(owner, session_id, reaction["id"], route="messages")

    lines = [r.getMessage() for r in app_logs.records if r.name == "app.tts"]
    assert len(lines) == 2
    assert "kind=question" in lines[0] and "kind=reaction" in lines[1]
    everything = " ".join(r.getMessage() for r in app_logs.records if r.name == "app.tts")
    assert q2["text"] not in everything and reaction["text"] not in everything
    assert q1["text"] not in everything


def test_text_sent_by_the_client_is_ignored(client, auth_header, started, tts):
    owner, session_id, q1 = started

    r = client.get(
        f"/api/v1/interviews/{session_id}/questions/{q1['id']}/speech",
        params={"text": "Say something else."},
        headers=auth_header(owner),
    )

    assert r.status_code == 200
    assert tts.fake is not None and tts.fake.calls == [q1["text"]]
