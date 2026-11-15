"""The generic half of every speech call: checks, vendor failures -> one 503, and one metadata log line.

Interview-agnostic on purpose. The caller (a feature's voice adapter) passes the vendor, the limits that are its own
business (keyterms, a text cap) and the fields to log. This module never names a session, a question or a role, so a
new speech feature reuses it instead of copying it. Plain functions: there is no state to hold (vendors are passed in).
"""

import logging
from collections.abc import Sequence

from app.core.ai.provider import LLMError
from app.core.ai.synthesizer import SpeechSynthesizer, SynthesisResult
from app.core.ai.transcriber import Transcriber, TranscriptionResult
from app.core.errors import (
    AppError,
    AudioTooLargeError,
    AudioTooLongError,
    NoSpeechError,
    SpeechUnavailableError,
    TranscriptionUnavailableError,
    UnsupportedAudioError,
)

from .audio import TRANSCRIPTION_MAX_BYTES, TRANSCRIPTION_MAX_SECONDS, audio_container

# One metadata line per call. Never the audio or the text (both are the user's personal data).
stt_logger = logging.getLogger("app.stt")
tts_logger = logging.getLogger("app.tts")

LogFields = Sequence[tuple[str, object]]

_TRANSCRIPTION_UNAVAILABLE = "Voice answers aren't available right now"
_SPEECH_UNAVAILABLE = "The interviewer's voice isn't available right now"
_NO_SPEECH = "We couldn't hear any speech in that recording"


async def transcribe(
    transcriber: Transcriber | None,
    audio: bytes,
    *,
    content_type: str,
    keyterms: Sequence[str],
    max_chars: int,
    log_fields: LogFields,
) -> str:
    """What was said in `audio`, cut to `max_chars` and trimmed.

    `audio` may be one byte over the cap (the route reads no further), which is how "too large" is detected. The
    upload checks run inside the try, so a rejected upload still writes its log line.
    """
    result: TranscriptionResult | None = None
    outcome, cause = "ok", "-"
    try:
        _check_audio(audio, content_type)
        if transcriber is None:
            raise TranscriptionUnavailableError(_TRANSCRIPTION_UNAVAILABLE)
        try:
            result = await transcriber.transcribe(audio, content_type=content_type, keyterms=keyterms)
        except LLMError as exc:
            cause = _cause(exc)
            raise TranscriptionUnavailableError(_TRANSCRIPTION_UNAVAILABLE) from exc
        if not result.text:
            raise NoSpeechError(_NO_SPEECH)
        if result.duration_seconds is not None and result.duration_seconds > TRANSCRIPTION_MAX_SECONDS:
            raise AudioTooLongError("Recordings are limited to 2 minutes")
        return result.text[:max_chars].strip()
    except AppError as exc:
        outcome = exc.code
        raise
    except Exception as exc:
        # Not handled here (it becomes a 500), but the log line must not call it a success.
        outcome, cause = "error", type(exc).__name__
        raise
    finally:
        _log(
            stt_logger,
            "transcription",
            log_fields,
            bytes=len(audio),
            content_type=content_type.split(";", 1)[0].strip() or "-",
            duration_s="-" if result is None or result.duration_seconds is None else result.duration_seconds,
            model="-" if result is None else result.model,
            latency_ms="-" if result is None else result.latency_ms,
            attempts="-" if result is None else result.attempts,
            cause=cause,
            outcome=outcome,
        )


async def synthesize(synthesizer: SpeechSynthesizer | None, text: str, *, log_fields: LogFields) -> SynthesisResult:
    """`text` spoken by the configured voice, as one whole clip. The caller decides what may be spoken (the text must
    come from its own stored data, never from the request); this only speaks it, maps failures and logs metadata."""
    result: SynthesisResult | None = None
    outcome, cause = "ok", "-"
    try:
        if synthesizer is None:
            raise SpeechUnavailableError(_SPEECH_UNAVAILABLE)
        try:
            result = await synthesizer.synthesize(text)
        except LLMError as exc:
            cause = _cause(exc)
            raise SpeechUnavailableError(_SPEECH_UNAVAILABLE) from exc
        return result
    except AppError as exc:
        outcome = exc.code
        raise
    except Exception as exc:
        # Not handled here (it becomes a 500), but the log line must not call it a success.
        outcome, cause = "error", type(exc).__name__
        raise
    finally:
        _log(
            tts_logger,
            "speech",
            log_fields,
            characters=len(text),
            model="-" if result is None else result.model,
            latency_ms="-" if result is None else result.latency_ms,
            attempts="-" if result is None else result.attempts,
            cause=cause,
            outcome=outcome,
        )


def _check_audio(audio: bytes, content_type: str) -> None:
    if len(audio) > TRANSCRIPTION_MAX_BYTES:
        raise AudioTooLargeError("Recordings are limited to 3 MB")
    if not audio:
        raise NoSpeechError(_NO_SPEECH)
    if audio_container(content_type, audio[:16]) is None:
        raise UnsupportedAudioError("That recording format isn't supported")


def _cause(exc: LLMError) -> str:
    return f"{type(exc).__name__}:{exc.status_code or '-'}:attempts={exc.attempts}"


def _log(logger: logging.Logger, event: str, log_fields: LogFields, **metrics: object) -> None:
    """`<event> <caller's fields> <metrics>` as key=value pairs, in that order. Values go through %-formatting, so a
    value can't inject format codes."""
    pairs = [*log_fields, *metrics.items()]
    logger.info(" ".join([event, *(f"{key}=%s" for key, _ in pairs)]), *(value for _, value in pairs))
