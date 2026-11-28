"""Shared by the interviews services: the session as plain values and ownership.

Kept here (not in one service) so no service imports another.
"""

import uuid
from typing import NamedTuple

from app.core.errors import NotFoundError
from app.modules.auth.models.auth_model import User
from app.modules.profile.schemas.profile_schema import CandidateProfile

from ..constants.interviews_constants import (
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
)
from ..dependencies.models.interviews_model import InterviewSession
from ..repositories.interviews_repository import InterviewsRepository
from .interviews_knowledge_utils import ReferenceNote


class InterviewSetup(NamedTuple):
    """The session fields the interviewer needs, as plain values that survive the end of a transaction."""

    session_id: uuid.UUID
    role: JobRole
    level: Level
    interview_type: InterviewType
    question_count: int
    job_description: str | None
    # Sent instead of job_description when present (made once at start for long descriptions).
    job_description_summary: str | None = None
    # Picked once at start and stored with the interview; empty for interviews without notes (and older ones).
    reference_notes: tuple[ReferenceNote, ...] = ()
    # The owner's profile, read live for this request when the interview opted in; never stored on the interview.
    profile: CandidateProfile | None = None


class Thread(NamedTuple):
    """The main question the answered question belongs to (itself, or a follow-up's parent), as plain values."""

    main_id: uuid.UUID
    main_number: int
    category: QuestionCategory


def owned_session(repo: InterviewsRepository, user: User, session_id: uuid.UUID) -> InterviewSession:
    session = repo.get_for_user(session_id, user.id)
    if session is None:
        raise NotFoundError("Interview not found")
    return session
