"""The speech gateway: the generic half of every speech call (checks, vendor errors -> 503, one metadata log line).

It knows nothing about interviews: the caller passes the vendor, the limits and the fields to log.
"""

import pytest

from app.core.ai.fake import FakeSynthesizer, FakeTranscriber
from app.core.ai.provider import (
    LLMBadResponseError,
    LLMRateLimitError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)
from app.core.ai.synthesizer import SynthesisResult
from app.core.ai.transcriber import TranscriptionResult
from app.core.errors import AppError
from app.core.speech import gateway
from app.core.speech.audio import TRANSCRIPTION_MAX_BYTES

pytestmark = pytest.mark.anyio

WEBM = b"\x1a\x45\xdf\xa3" + b"\x00" * 64
FIELDS = (("user", "u-1"), ("session", "s-1"))


@pytest.fixture
def anyio_backend():
    return "asyncio"


async def transcribe(transcriber, audio=WEBM, content_type="audio/webm;codecs=opus", keyterms=(), max_chars=2000):
    return await gateway.transcribe(
        transcriber, audio, content_type=content_type, keyterms=keyterms, max_chars=max_chars, log_fields=FIELDS
    )


def stt_lines(app_logs) -> list[str]:
    return [r.getMessage() for r in app_logs.records if r.name == "app.stt"]


async def code_of(call) -> str:
    with pytest.raises(AppError) as exc:
        await call
    return exc.value.code


# --- transcribe ---


async def test_the_text_comes_back_trimmed_and_capped_with_the_keyterms_passed_on():
    fake = FakeTranscriber(["  " + "a" * 30 + "  "])

    text = await transcribe(fake, keyterms=("Redis",), max_chars=12)

    assert text == "a" * 10  # cut to 12 characters first, then trimmed (the order the endpoint always used)
    [(audio, content_type, keyterms)] = fake.calls
    assert (audio, content_type, keyterms) == (WEBM, "audio/webm;codecs=opus", ("Redis",))


async def test_no_transcriber_configured_is_unavailable():
    assert await code_of(transcribe(None)) == "TRANSCRIPTION_UNAVAILABLE"


@pytest.mark.parametrize(
    "error",
    [
        LLMTimeoutError("slow"),
        LLMRateLimitError("busy"),
        LLMServerError("down"),
        LLMRequestError("bad key", status_code=401),
        LLMBadResponseError("junk"),
    ],
)
async def test_every_vendor_failure_is_unavailable(error):
    assert await code_of(transcribe(FakeTranscriber([error]))) == "TRANSCRIPTION_UNAVAILABLE"


async def test_a_blank_transcript_is_no_speech():
    assert await code_of(transcribe(FakeTranscriber([""]))) == "NO_SPEECH"


async def test_a_reported_duration_over_the_limit_is_too_long():
    assert await code_of(transcribe(FakeTranscriber(["hello"], duration=126))) == "AUDIO_TOO_LONG"


@pytest.mark.parametrize(
    ("audio", "content_type", "expected"),
    [
        (WEBM + b"\x00" * TRANSCRIPTION_MAX_BYTES, "audio/webm", "AUDIO_TOO_LARGE"),
        (b"", "audio/webm", "NO_SPEECH"),
        (WEBM, "audio/mpeg", "UNSUPPORTED_AUDIO"),
        (b"OggS" + b"\x00" * 16, "audio/webm", "UNSUPPORTED_AUDIO"),
    ],
    ids=["too-large", "empty", "type-not-allowed", "signature-mismatch"],  # short ids: the audio is 3 MB
)
async def test_a_bad_upload_is_refused_before_the_vendor_is_called(audio, content_type, expected):
    fake = FakeTranscriber()

    assert await code_of(transcribe(fake, audio=audio, content_type=content_type)) == expected
    assert fake.calls == []


async def test_one_log_line_with_the_callers_fields_and_never_the_text(app_logs):
    result = TranscriptionResult(text="SECRET answer", duration_seconds=3.5, model="nova-3", latency_ms=42, attempts=2)

    await transcribe(FakeTranscriber([result]))

    assert stt_lines(app_logs) == [
        (
            "transcription user=u-1 session=s-1 bytes=68 content_type=audio/webm duration_s=3.5 model=nova-3 "
            "latency_ms=42 attempts=2 cause=- outcome=ok"
        )
    ]
    assert "SECRET" not in " ".join(r.getMessage() for r in app_logs.records)


async def test_a_failure_logs_its_outcome_and_the_vendor_cause(app_logs):
    error = LLMServerError("down", status_code=503)
    error.attempts = 2

    await code_of(transcribe(FakeTranscriber([error])))

    [line] = stt_lines(app_logs)
    assert line.endswith("cause=LLMServerError:503:attempts=2 outcome=TRANSCRIPTION_UNAVAILABLE")
    assert line.startswith("transcription user=u-1 session=s-1 bytes=68 content_type=audio/webm duration_s=- model=-")


# --- synthesize ---

SPEAK_FIELDS = (("user", "u-1"), ("session", "s-1"), ("id", "q-1"), ("kind", "question"))


async def synthesize(synthesizer, text="Tell me about a time you led a migration."):
    return await gateway.synthesize(synthesizer, text, log_fields=SPEAK_FIELDS)


def tts_lines(app_logs) -> list[str]:
    return [r.getMessage() for r in app_logs.records if r.name == "app.tts"]


async def test_the_spoken_clip_comes_back_as_the_vendor_made_it():
    fake = FakeSynthesizer([b"ID3clip"], content_type="audio/ogg")

    result = await synthesize(fake)

    assert (result.audio, result.content_type) == (b"ID3clip", "audio/ogg")
    assert fake.calls == ["Tell me about a time you led a migration."]


async def test_no_synthesizer_configured_is_speech_unavailable():
    assert await code_of(synthesize(None)) == "SPEECH_UNAVAILABLE"


@pytest.mark.parametrize(
    "error",
    [
        LLMTimeoutError("slow"),
        LLMRateLimitError("busy"),
        LLMServerError("down"),
        LLMRequestError("bad key", status_code=401),
        LLMBadResponseError("junk"),
    ],
)
async def test_every_speech_vendor_failure_is_speech_unavailable(error):
    assert await code_of(synthesize(FakeSynthesizer([error]))) == "SPEECH_UNAVAILABLE"


async def test_one_speech_log_line_with_the_callers_fields_and_never_the_text(app_logs):
    result = SynthesisResult(
        audio=b"ID3", content_type="audio/mpeg", model="aura-asteria-en", characters=40, latency_ms=330, attempts=1
    )
    text = "SECRET question text, spoken to the user."

    await synthesize(FakeSynthesizer([result]), text=text)

    assert tts_lines(app_logs) == [
        (
            f"speech user=u-1 session=s-1 id=q-1 kind=question characters={len(text)} model=aura-asteria-en "
            "latency_ms=330 attempts=1 cause=- outcome=ok"
        )
    ]
    assert "SECRET" not in " ".join(r.getMessage() for r in app_logs.records)


async def test_a_speech_failure_logs_its_outcome_and_the_vendor_cause(app_logs):
    error = LLMRateLimitError("busy", status_code=429)
    error.attempts = 2

    await code_of(synthesize(FakeSynthesizer([error]), text="Hi."))

    assert tts_lines(app_logs) == [
        (
            "speech user=u-1 session=s-1 id=q-1 kind=question characters=3 model=- latency_ms=- attempts=- "
            "cause=LLMRateLimitError:429:attempts=2 outcome=SPEECH_UNAVAILABLE"
        )
    ]


async def test_no_synthesizer_still_logs_one_line(app_logs):
    await code_of(synthesize(None, text="Hi."))

    [line] = tts_lines(app_logs)
    assert line.endswith("cause=- outcome=SPEECH_UNAVAILABLE")


class _Broken:
    """A vendor adapter with a bug: it raises something that isn't an LLMError."""

    async def transcribe(self, *_, **__):
        raise RuntimeError("adapter bug")

    async def synthesize(self, *_):
        raise RuntimeError("adapter bug")


async def test_an_unexpected_error_is_logged_as_an_error_and_still_raised(app_logs):  # review R5
    with pytest.raises(RuntimeError):
        await transcribe(_Broken())
    with pytest.raises(RuntimeError):
        await synthesize(_Broken(), text="Hi.")

    [stt] = stt_lines(app_logs)
    [tts] = tts_lines(app_logs)
    assert stt.endswith("cause=RuntimeError outcome=error")
    assert tts.endswith("cause=RuntimeError outcome=error")
