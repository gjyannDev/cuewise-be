from datetime import datetime
from typing import Annotated, Literal
from uuid import UUID

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, StringConstraints

from .interviews_constants import (
    JOB_DESCRIPTION_MAX_LENGTH,
    MAX_QUESTION_COUNT,
    MIN_QUESTION_COUNT,
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
    SessionStatus,
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


class InterviewOut(BaseModel):
    session: SessionOut
    current_question: QuestionOut
