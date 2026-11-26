"""The interview voice adapter: the only interview code that touches speech. Nothing is stored.

Only the interview rules live here: ownership, in progress (to transcribe), "already shown" and "an interviewer line"
(to speak), the role's keyterms and the answer cap. The generic speech checks, vendor errors and log lines are the
speech gateway's (`app/core/speech/gateway.py`).
"""

import uuid
from dataclasses import dataclass
from typing import Literal, NamedTuple

from app.core.ai.synthesizer import SpeechSynthesizer
from app.core.ai.transcriber import Transcriber
from app.core.errors import NotFoundError, SessionNotInProgressError
from app.core.logging import bind_log_context
from app.core.speech import gateway
from app.modules.auth.models.auth_model import User

from ..constants.interviews_constants import (
    MAX_ANSWER_LENGTH,
    ROLE_KEYTERMS,
    JobRole,
    SessionStatus,
)
from ..repositories.interviews_repository import InterviewsRepository
from ..utils.interviews_session_utils import owned_session

LineKind = Literal["question", "reaction"]
# The same message as `owned_session`'s, for every miss (not yours, unknown, not shown yet, a candidate answer, the
# wrong route), so neither the code nor the body tells which one applied.
_LINE_NOT_FOUND = "Interview not found"


@dataclass(frozen=True)
class SpeakableLine:
    """A stored interviewer line that passed every check, with its text copied out of the database. Only the
    `prepare_*_speech` methods make one, and `speak` takes nothing else: the spoken text can't come from a request."""

    session_id: uuid.UUID
    line_id: uuid.UUID
    kind: LineKind
    text: str


class SpokenLine(NamedTuple):
    audio: bytes
    content_type: str


class VoiceService:
    def __init__(
        self,
        repo: InterviewsRepository,
        transcriber: Transcriber | None,
        synthesizer: SpeechSynthesizer | None = None,
    ):
        self.repo = repo
        # None = voice answers off: the transcription endpoint answers 503.
        self.transcriber = transcriber
        # None = the interviewer's voice is off: the speech endpoints answer 503.
        self.synthesizer = synthesizer

    def prepare_transcription(self, user: User, session_id: uuid.UUID) -> JobRole:
        """Only the owner of an interview in progress may transcribe for it; returns the interview's role (it picks
        the keyterms). Sync DB read, run before the upload is looked at (the route calls it in the threadpool, like
        `prepare_answer`). The read transaction ends here, so no connection waits on the upload or on Deepgram."""
        bind_log_context(session=str(session_id))
        session = owned_session(self.repo, user, session_id)
        if session.status != SessionStatus.in_progress:
            raise SessionNotInProgressError("This interview is not in progress")
        role = JobRole(session.role)
        self.repo.release()
        return role

    async def transcribe(
        self, user: User, session_id: uuid.UUID, role: JobRole, audio: bytes, content_type: str
    ) -> str:
        """What the candidate said in `audio`. Nothing is stored: the text only becomes an answer if they send it."""
        return await gateway.transcribe(
            self.transcriber,
            audio,
            content_type=content_type,
            keyterms=ROLE_KEYTERMS[role],
            max_chars=MAX_ANSWER_LENGTH,
        )

    def prepare_question_speech(self, user: User, session_id: uuid.UUID, question_id: uuid.UUID) -> SpeakableLine:
        """A question (main or follow-up) the owner has already been shown. No status check: a finished interview can
        still be replayed. Sync DB read (the route runs it in the threadpool); the connection is released before the
        slow synthesis."""
        bind_log_context(session=str(session_id))
        session = owned_session(self.repo, user, session_id)
        question = self.repo.get_shown_question(session.id, question_id, session.current_position)
        if question is None:
            raise NotFoundError(_LINE_NOT_FOUND)
        line = SpeakableLine(session.id, question.id, "question", question.text)
        self.repo.release()
        return line

    def prepare_reaction_speech(self, user: User, session_id: uuid.UUID, message_id: uuid.UUID) -> SpeakableLine:
        """An interviewer reaction of the owner's interview; a candidate answer is never spoken. Same flow as
        `prepare_question_speech`."""
        bind_log_context(session=str(session_id))
        session = owned_session(self.repo, user, session_id)
        reaction = self.repo.get_interviewer_reaction(session.id, message_id)
        if reaction is None:
            raise NotFoundError(_LINE_NOT_FOUND)
        line = SpeakableLine(session.id, reaction.id, "reaction", reaction.content)
        self.repo.release()
        return line

    async def speak(self, user: User, line: SpeakableLine) -> SpokenLine:
        """The prepared line as one audio clip."""
        result = await gateway.synthesize(
            self.synthesizer,
            line.text,
            log_fields=(("id", line.line_id), ("kind", line.kind)),
        )
        return SpokenLine(audio=result.audio, content_type=result.content_type)
