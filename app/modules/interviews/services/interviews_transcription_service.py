"""Voice answers: speech to text, for the candidate to review before sending. Nothing is stored."""

import logging
import uuid

from app.core.ai.provider import LLMError
from app.core.ai.transcriber import Transcriber, TranscriptionResult
from app.core.errors import (
    AppError,
    AudioTooLargeError,
    AudioTooLongError,
    NoSpeechError,
    SessionNotInProgressError,
    TranscriptionUnavailableError,
    UnsupportedAudioError,
)
from app.modules.auth.models.auth_model import User

from ..constants.interviews_constants import (
    MAX_ANSWER_LENGTH,
    ROLE_KEYTERMS,
    TRANSCRIPTION_MAX_BYTES,
    TRANSCRIPTION_MAX_SECONDS,
    JobRole,
    SessionStatus,
)
from ..repositories.interviews_repository import InterviewsRepository
from ..utils.interviews_session_utils import owned_session
from ..utils.interviews_utils import audio_container

# One metadata line per transcription. Never the audio or the transcript (both are the candidate's personal data).
stt_logger = logging.getLogger("app.stt")


class TranscriptionService:
    def __init__(self, repo: InterviewsRepository, transcriber: Transcriber | None):
        self.repo = repo
        # None = voice answers off: the transcription endpoint answers 503.
        self.transcriber = transcriber

    def prepare_transcription(self, user: User, session_id: uuid.UUID) -> JobRole:
        """Only the owner of an interview in progress may transcribe for it; returns the interview's role (it picks
        the keyterms). Sync DB read, run before the upload is looked at (the route calls it in the threadpool, like
        `prepare_answer`)."""
        session = owned_session(self.repo, user, session_id)
        if session.status != SessionStatus.in_progress:
            raise SessionNotInProgressError("This interview is not in progress")
        return JobRole(session.role)

    async def transcribe(
        self, user: User, session_id: uuid.UUID, role: JobRole, audio: bytes, content_type: str
    ) -> str:
        """What the candidate said in `audio`. Nothing is stored: the text only becomes an answer if they send it.

        `audio` may be one byte over the cap (the route reads no further), which is how "too large" is detected.
        The upload checks run here, inside the try, so a rejected upload still writes its log line.
        """
        result: TranscriptionResult | None = None
        outcome, cause = "ok", "-"
        try:
            self._check_audio(audio, content_type)
            if self.transcriber is None:
                raise TranscriptionUnavailableError("Voice answers aren't available right now")
            try:
                result = await self.transcriber.transcribe(
                    audio, content_type=content_type, keyterms=ROLE_KEYTERMS[role]
                )
            except LLMError as exc:
                cause = f"{type(exc).__name__}:{exc.status_code or '-'}:attempts={exc.attempts}"
                raise TranscriptionUnavailableError("Voice answers aren't available right now") from exc
            if not result.text:
                raise NoSpeechError("We couldn't hear any speech in that recording")
            if result.duration_seconds is not None and result.duration_seconds > TRANSCRIPTION_MAX_SECONDS:
                raise AudioTooLongError("Recordings are limited to 2 minutes")
            return result.text[:MAX_ANSWER_LENGTH].strip()
        except AppError as exc:
            outcome = exc.code
            raise
        finally:
            stt_logger.info(
                "transcription user=%s session=%s bytes=%s content_type=%s duration_s=%s model=%s latency_ms=%s "
                "attempts=%s cause=%s outcome=%s",
                user.id,
                session_id,
                len(audio),
                content_type.split(";", 1)[0].strip() or "-",
                "-" if result is None or result.duration_seconds is None else result.duration_seconds,
                "-" if result is None else result.model,
                "-" if result is None else result.latency_ms,
                "-" if result is None else result.attempts,
                cause,
                outcome,
            )

    @staticmethod
    def _check_audio(audio: bytes, content_type: str) -> None:
        if len(audio) > TRANSCRIPTION_MAX_BYTES:
            raise AudioTooLargeError("Recordings are limited to 3 MB")
        if not audio:
            raise NoSpeechError("We couldn't hear any speech in that recording")
        if audio_container(content_type, audio[:16]) is None:
            raise UnsupportedAudioError("That recording format isn't supported")
