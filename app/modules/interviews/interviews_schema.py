from datetime import datetime
from typing import Annotated, Literal, NamedTuple
from uuid import UUID

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, StringConstraints

from .interviews_constants import (
    JOB_DESCRIPTION_MAX_LENGTH,
    MAX_ANSWER_LENGTH,
    MAX_QUESTION_COUNT,
    MIN_QUESTION_COUNT,
    InterviewType,
    JobRole,
    Level,
    MessageKind,
    MessageRole,
    QuestionCategory,
    QuestionKind,
    SessionStatus,
    StreamEvent,
    TurnPhase,
)

NonBlankStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class BankQuestion(BaseModel):
    """One entry of the hand-written question bank file."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: NonBlankStr
    text: NonBlankStr
    type: QuestionCategory
    roles: list[JobRole | Literal["general"]] = Field(min_length=1)
    levels: list[Level] = Field(min_length=1)


def _unique_ids(bank: list[BankQuestion]) -> list[BankQuestion]:
    ids = [q.id for q in bank]
    duplicates = sorted({i for i in ids if ids.count(i) > 1})
    if duplicates:
        raise ValueError(f"duplicate question ids: {duplicates}")
    return bank


QuestionBank = Annotated[list[BankQuestion], Field(min_length=1), AfterValidator(_unique_ids)]


class InterviewCreateIn(BaseModel):
    # forbid: server-owned fields like status or user_id can never come from the client.
    model_config = ConfigDict(extra="forbid")

    role: JobRole
    level: Level
    interview_type: InterviewType
    # strict: reject "3" and 2.5 instead of coercing them.
    question_count: int = Field(ge=MIN_QUESTION_COUNT, le=MAX_QUESTION_COUNT, strict=True)
    # Untrusted text a later story puts into prompts: trimmed, bounded, blank stored as null.
    job_description: Annotated[
        str | None,
        StringConstraints(strip_whitespace=True, max_length=JOB_DESCRIPTION_MAX_LENGTH),
        AfterValidator(lambda v: v or None),
    ] = None


class SessionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    role: JobRole
    level: Level
    interview_type: InterviewType
    question_count: int
    job_description: str | None
    status: SessionStatus
    created_at: datetime


class QuestionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    position: int
    text: str
    category: QuestionCategory
    # Read from the row's `kind`; named so it can't be confused with a transcript item's kind.
    question_kind: QuestionKind = Field(validation_alias="kind")
    # The main question this belongs to ("Question 3 of 5"); a follow-up shares its main question's number.
    main_number: int


class InterviewOut(BaseModel):
    session: SessionOut
    # None once the session is completed.
    current_question: QuestionOut | None


class AnswerIn(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # The question being answered; must be the session's current one, so a double-click can't answer the next.
    question_id: UUID
    # Untrusted text that goes to the LLM: trimmed and bounded (it is resent on every later turn).
    answer: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=MAX_ANSWER_LENGTH)]


class ReactionOut(BaseModel):
    id: UUID
    text: str


class AnswerOut(BaseModel):
    session: SessionOut
    # A predefined acknowledgement when the interview moves to the next main question or completes; None when the
    # next question is a follow-up (it comes straight away, with nothing in between).
    reaction: ReactionOut | None
    # The next question, or None when this answer completed the session.
    current_question: QuestionOut | None


class TranscriptItemOut(BaseModel):
    """One line of the chat as the user saw it. Usage metadata (model, tokens) is never part of it."""

    id: UUID
    question_id: UUID
    position: int
    role: MessageRole
    kind: MessageKind
    text: str
    # None for questions: they are stored when the session starts, not when they are shown.
    created_at: datetime | None
    # Of the question this item belongs to (answers and reactions share their question's).
    question_kind: QuestionKind
    main_number: int


class TranscriptOut(BaseModel):
    # Bounded by the 10-question cap and 2 follow-ups each (at most 90 items), so deliberately not paginated.
    items: list[TranscriptItemOut]


# --- Streamed answer turn (POST /interviews/{id}/messages/stream): the `data` of each SSE event ---
# The reaction event's data is a ReactionOut (the same id and text `done` returns), and `done` carries an AnswerOut.


class _StreamEventData(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class StatusEventOut(_StreamEventData):
    phase: TurnPhase


class QuestionDeltaOut(_StreamEventData):
    """The next chunk of the question being written; the client appends it to the text so far."""

    text: str


class ResetOut(_StreamEventData):
    """Discard the question text streamed so far: that draft failed and another one (or a bank question) follows."""


class StreamErrorOut(_StreamEventData):
    """Terminal. A generic message and a code the client can act on; never exception, LLM or answer text."""

    code: str
    message: str
    request_id: str | None


class StreamEventOut(NamedTuple):
    """One event of a streamed turn as the controller yields it; the route encodes it as SSE."""

    event: StreamEvent
    data: BaseModel
