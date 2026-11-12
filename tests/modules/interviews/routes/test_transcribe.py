import uuid

import pytest

from app.core.ai.provider import (
    LLMBadResponseError,
    LLMRateLimitError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)
from app.core.ai.transcriber import TranscriptionResult
from app.modules.interviews.constants.interviews_constants import (
    ROLE_KEYTERMS,
    TRANSCRIPTION_MAX_BYTES,
    JobRole,
)
from app.modules.interviews.dependencies.models.interviews_model import InterviewSession

# The `transcribe` fixture's default recording (conftest.WEBM_AUDIO): a WebM header and padding.
WEBM_AUDIO = b"\x1a\x45\xdf\xa3" + b"\x00" * 256


@pytest.fixture
def started(make_user, start_interview):
    """An owner with a started backend interview: (owner, session_id)."""
    owner = make_user(email="owner@example.com")
    return owner, start_interview(owner, question_count=3).json()["session"]["id"]


def code(response) -> str:
    return response.json()["error"]["code"]


# --- success (AC2) ---


def test_owner_gets_the_transcript_of_their_recording(transcribe, started, stt):  # AC2
    owner, session_id = started
    stt.script("I would add an index on the foreign key.")

    r = transcribe(owner, session_id)

    assert r.status_code == 200
    assert r.json() == {"text": "I would add an index on the foreign key."}
    [(audio, content_type, _)] = stt.fake.calls
    assert audio == WEBM_AUDIO
    assert content_type == "audio/webm;codecs=opus"


@pytest.mark.parametrize("role", [JobRole.backend, JobRole.frontend])
def test_the_interviews_role_picks_the_keyterms(transcribe, make_user, start_interview, stt, role):  # spike
    owner = make_user(email="owner@example.com")
    session_id = start_interview(owner, role=role.value).json()["session"]["id"]

    transcribe(owner, session_id)

    [(_, _, keyterms)] = stt.fake.calls
    assert keyterms == ROLE_KEYTERMS[role]


def test_nothing_is_stored(transcribe, started, client, auth_header):  # AC9: the transcript is not an answer
    owner, session_id = started

    transcribe(owner, session_id)

    items = client.get(f"/api/v1/interviews/{session_id}/messages", headers=auth_header(owner)).json()["items"]
    assert [item["kind"] for item in items] == ["question"]


# --- who may transcribe (AC3, EC17) ---


def test_no_token_is_401(transcribe, started, stt):  # AC3
    _, session_id = started

    r = transcribe(None, session_id, headers={})

    assert r.status_code == 401
    assert stt.fake.calls == []


def test_foreign_and_missing_sessions_are_the_same_404(transcribe, started, make_user, stt):  # AC3, EC17
    _, session_id = started
    stranger = make_user(email="stranger@example.com")

    foreign = transcribe(stranger, session_id)
    missing = transcribe(stranger, uuid.uuid7())

    assert foreign.status_code == missing.status_code == 404
    assert stt.fake.calls == []


@pytest.mark.parametrize("ending", ["abandoned", "completed"])
def test_a_session_not_in_progress_is_409(transcribe, started, db, stt, ending):  # AC3, EC17
    owner, session_id = started
    db.get(InterviewSession, uuid.UUID(session_id)).status = ending
    db.commit()

    r = transcribe(owner, session_id)

    assert r.status_code == 409
    assert code(r) == "SESSION_NOT_IN_PROGRESS"
    assert stt.fake.calls == []


# --- not configured (AC6, EC22) ---


def test_no_transcriber_configured_is_503(transcribe, started, stt):  # AC6, EC22
    owner, session_id = started
    stt.disable()

    r = transcribe(owner, session_id)

    assert r.status_code == 503
    assert code(r) == "TRANSCRIPTION_UNAVAILABLE"


# --- the upload itself (AC4, EC15) ---


def test_a_request_without_a_file_part_is_422(transcribe, started, stt):  # AC4
    owner, session_id = started

    r = transcribe(owner, session_id, audio=None)

    assert r.status_code == 422
    assert stt.fake.calls == []


def test_an_empty_file_is_no_speech(transcribe, started, stt):  # AC4
    owner, session_id = started

    r = transcribe(owner, session_id, audio=b"")

    assert r.status_code == 422
    assert code(r) == "NO_SPEECH"
    assert stt.fake.calls == []


@pytest.mark.parametrize(
    ("audio", "content_type"),
    [
        (WEBM_AUDIO, "video/webm"),
        (WEBM_AUDIO, "application/octet-stream"),
        (b"RIFF\x24\x00\x00\x00WAVEfmt " + b"\x00" * 64, "audio/webm"),
        (b"<html><body>not audio</body></html>", "audio/ogg"),
    ],
)
def test_a_disallowed_type_or_mismatched_signature_is_415(transcribe, started, stt, audio, content_type):  # AC4
    owner, session_id = started

    r = transcribe(owner, session_id, audio=audio, content_type=content_type)

    assert r.status_code == 415
    assert code(r) == "UNSUPPORTED_AUDIO"
    assert stt.fake.calls == []


def test_over_3_mb_is_413(transcribe, started, stt):  # AC4, EC15
    owner, session_id = started

    r = transcribe(owner, session_id, audio=WEBM_AUDIO + b"\x00" * TRANSCRIPTION_MAX_BYTES)

    assert r.status_code == 413
    assert code(r) == "AUDIO_TOO_LARGE"
    assert stt.fake.calls == []


def test_exactly_3_mb_is_accepted(transcribe, started, stt):  # inferred: the cap is inclusive
    owner, session_id = started
    audio = WEBM_AUDIO + b"\x00" * (TRANSCRIPTION_MAX_BYTES - len(WEBM_AUDIO))

    assert transcribe(owner, session_id, audio=audio).status_code == 200


# --- what the vendor heard (AC5, EC6, EC16, EC20) ---


def test_a_blank_transcript_is_no_speech(transcribe, started, stt):  # AC5, EC6
    owner, session_id = started
    stt.script("")

    r = transcribe(owner, session_id)

    assert r.status_code == 422
    assert code(r) == "NO_SPEECH"


def test_a_reported_duration_over_125_s_is_too_long(transcribe, started, stt):  # AC5, EC16
    owner, session_id = started
    stt.script("A very long answer.", duration=126.0)

    r = transcribe(owner, session_id)

    assert r.status_code == 422
    assert code(r) == "AUDIO_TOO_LONG"
    assert "long answer" not in r.text


def test_125_s_or_an_unreported_duration_is_accepted(transcribe, started, stt):  # inferred: the limit is inclusive
    owner, session_id = started
    stt.script(TranscriptionResult(text="ok", duration_seconds=125.0, model="m", latency_ms=1, attempts=1))
    assert transcribe(owner, session_id).status_code == 200

    stt.script("ok", duration=None)
    assert transcribe(owner, session_id).status_code == 200


def test_a_transcript_over_2000_characters_is_capped(transcribe, started, stt):  # AC5, EC20
    owner, session_id = started
    stt.script("word " * 500)

    text = transcribe(owner, session_id).json()["text"]

    assert len(text) <= 2000
    assert text == ("word " * 500)[:2000].strip()


# --- vendor failures (AC6, EC13) ---


@pytest.mark.parametrize(
    "error",
    [
        LLMTimeoutError("timed out"),
        LLMRateLimitError("rate limited", status_code=429),
        LLMServerError("down", status_code=503),
        LLMRequestError("bad key", status_code=401),
        LLMRequestError("no credit", status_code=402),
        LLMBadResponseError("garbage"),
    ],
)
def test_every_vendor_failure_is_a_generic_503(transcribe, started, stt, error):  # AC6, EC13
    owner, session_id = started
    stt.script(error)

    r = transcribe(owner, session_id)

    assert r.status_code == 503
    assert code(r) == "TRANSCRIPTION_UNAVAILABLE"
    assert str(error) not in r.text


# --- rate limit (AC7, EC21) ---


def test_the_11th_recording_in_a_minute_is_429_without_calling_the_vendor(
    transcribe, started, make_user, start_interview, stt
):  # AC7, EC21
    owner, session_id = started
    for _ in range(10):
        assert transcribe(owner, session_id).status_code == 200

    r = transcribe(owner, session_id)

    assert r.status_code == 429
    assert code(r) == "RATE_LIMITED"
    assert 1 <= int(r.headers["retry-after"]) <= 60
    assert len(stt.fake.calls) == 10

    other = make_user(email="other@example.com")
    other_session = start_interview(other).json()["session"]["id"]
    assert transcribe(other, other_session).status_code == 200


# --- logs (AC9) ---


def test_one_metadata_line_is_logged_without_audio_text_or_key(transcribe, started, stt, app_logs):  # AC9
    owner, session_id = started
    stt.script("My secret answer about caching.")

    transcribe(owner, session_id)

    lines = [r.getMessage() for r in app_logs.records if r.name == "app.stt"]
    assert len(lines) == 1
    [line] = lines
    assert f"session={session_id}" in line
    assert f"user={owner.id}" in line
    assert f"bytes={len(WEBM_AUDIO)}" in line
    assert "content_type=audio/webm" in line
    assert "duration_s=12.5" in line
    assert "model=fake-stt" in line
    assert "outcome=ok" in line
    everything = " ".join(r.getMessage() for r in app_logs.records)
    assert "secret answer" not in everything


def test_a_failure_logs_its_outcome_code(transcribe, started, stt, app_logs):  # AC9
    owner, session_id = started
    stt.script("")

    transcribe(owner, session_id)

    [line] = [r.getMessage() for r in app_logs.records if r.name == "app.stt"]
    assert "outcome=NO_SPEECH" in line
