from datetime import datetime
from typing import Annotated, Literal, NamedTuple, Self
from urllib.parse import urlsplit
from uuid import UUID

from pydantic import (
    AfterValidator,
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    model_validator,
)

from app.core.pagination import Page

from ..constants.interviews_constants import (
    CATEGORY_CRITERIA,
    JOB_DESCRIPTION_MAX_LENGTH,
    JOB_PASTE_MAX_CHARS,
    JOB_URL_MAX_LENGTH,
    MAX_ANSWER_LENGTH,
    MAX_QUESTION_COUNT,
    MIN_QUESTION_COUNT,
    SCORE_MAX,
    SCORE_MIN,
    Criterion,
    FeedbackStatus,
    InterviewType,
    JobRole,
    JobTextFormat,
    Level,
    LevelGroup,
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


class RubricCriterion(BaseModel):
    """One criterion of the feedback rubric: what it asks, an anchor per score, and what each level group needs."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    category: QuestionCategory
    question: NonBlankStr
    levels: dict[int, NonBlankStr]
    expectations: dict[LevelGroup, NonBlankStr]

    @model_validator(mode="after")
    def _complete(self) -> Self:
        if sorted(self.levels) != list(range(SCORE_MIN, SCORE_MAX + 1)):
            raise ValueError(f"needs one anchor for each score {SCORE_MIN}-{SCORE_MAX}")
        if set(self.expectations) != set(LevelGroup):
            raise ValueError("needs an expectation for every level group")
        return self


class Rubric(BaseModel):
    """The feedback rubric file: ground truth for every score, versioned like a prompt."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    version: NonBlankStr
    criteria: dict[Criterion, RubricCriterion]

    @model_validator(mode="after")
    def _covers_every_criterion(self) -> Self:
        if set(self.criteria) != set(Criterion):
            raise ValueError(f"missing criteria: {sorted(set(Criterion) - set(self.criteria))}")
        wrong = [c for c, entry in self.criteria.items() if c not in CATEGORY_CRITERIA[entry.category]]
        if wrong:
            raise ValueError(f"criteria in the wrong category: {wrong}")
        return self


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
    # Opt-in: send the stored résumé profile to the model on main questions. strict: "true" and 1 are refused.
    use_profile: bool = Field(default=False, strict=True)


class SessionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    role: JobRole
    level: Level
    interview_type: InterviewType
    question_count: int
    job_description: str | None
    use_profile: bool
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


class InterviewListItemOut(BaseModel):
    """One row of the history table. No job description or interview content: the row is all the table needs."""

    id: UUID
    role: JobRole
    level: Level
    interview_type: InterviewType
    status: SessionStatus
    question_count: int
    # Main questions finished, 0..question_count; follow-ups don't count ("answered 2 of 5").
    answered_count: int
    created_at: datetime


class InterviewListOut(Page[InterviewListItemOut]):
    pass


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


class TranscriptionOut(BaseModel):
    """POST /interviews/{id}/transcriptions: what the candidate said, for them to review. Not saved as an answer."""

    model_config = ConfigDict(extra="forbid")

    text: str


def _job_url(value: str) -> str:
    """Shape only: http(s), a host, a valid port, no credentials. Whether the address may be reached is the fetcher's
    job (it re-checks every redirect too). Messages never echo the URL."""
    parts = urlsplit(value)
    try:
        parts.port  # noqa: B018 - raises on a non-numeric or out-of-range port
    except ValueError as exc:
        raise ValueError("the port is not valid") from exc
    if parts.scheme.lower() not in {"http", "https"}:
        raise ValueError("only http and https links are accepted")
    if not parts.hostname:
        raise ValueError("the link has no host")
    if "@" in parts.netloc:
        raise ValueError("links with a user name or password are not accepted")
    return value


class JobUrlIn(BaseModel):
    """POST /interviews/job-url: a job posting link to read the job description from."""

    model_config = ConfigDict(extra="forbid")

    url: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1, max_length=JOB_URL_MAX_LENGTH),
        AfterValidator(_job_url),
    ]


class JobTextIn(BaseModel):
    """POST /interviews/job-text: a whole posting page the candidate copied from their own browser (for sites that
    block our fetch). Send the clipboard's HTML copy when there is one, else its plain text."""

    model_config = ConfigDict(extra="forbid")

    content: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=JOB_PASTE_MAX_CHARS)]
    format: JobTextFormat


class JobUrlOut(BaseModel):
    """The posting's text for the candidate to review and edit, then send as `job_description` when starting. Also the
    response of POST /interviews/job-text (same shape, same rules)."""

    model_config = ConfigDict(extra="forbid")

    text: str
    truncated: bool = Field(description=f"True when the text was cut to {JOB_DESCRIPTION_MAX_LENGTH} characters.")


# --- End-of-interview feedback (POST and GET /interviews/{id}/feedback) ---


class FeedbackEvidenceOut(BaseModel):
    criterion: Criterion
    # Verified by the code: these exact words appear in the candidate's answers to this question.
    quote: str
    reason: str


class FeedbackQuestionOut(BaseModel):
    main_number: int
    category: QuestionCategory
    # The main question's text.
    question: str
    # Every criterion of the question's category, each 1 to 5.
    scores: dict[Criterion, int]
    note: str | None
    evidence: list[FeedbackEvidenceOut]


class FeedbackOut(BaseModel):
    """The stored feedback. Scores and text only once `generated`; `enough_evidence` false = nothing was scored.

    Never returned: token usage, prompt versions, the model, who wrote the text (model or template), failure details,
    the job description, the user id.
    """

    id: UUID
    interview_id: UUID
    status: FeedbackStatus
    enough_evidence: bool | None
    # Out of 5, one decimal, computed by the app (the mean of every criterion score).
    overall: float | None
    summary: str | None
    strengths: list[str]
    improvements: list[str]
    next_steps: list[str]
    questions: list[FeedbackQuestionOut]
    rubric_version: str
    created_at: datetime


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
