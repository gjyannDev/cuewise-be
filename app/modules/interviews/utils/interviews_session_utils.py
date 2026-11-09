"""Shared by the interviews services: the session as plain values, ownership, and the two ways a question is made.

Kept here (not in one service) so no service imports another.
"""

import random
import uuid
from collections.abc import Sequence
from typing import NamedTuple

from app.core.ai.provider import LLMResult
from app.core.errors import NotFoundError
from app.modules.auth.models.auth_model import User

from ..ai.interviews_context import InterviewerInputs
from ..ai.interviews_turn import Written, sum_known
from ..constants.interviews_constants import (
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
    QuestionKind,
    QuestionSource,
)
from ..models.interviews_model import InterviewQuestion, InterviewSession
from ..repositories.interviews_repository import InterviewsRepository
from ..schemas.interviews_schema import BankQuestion
from .interviews_utils import QuestionTurn, pick_fallback_question


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


def interviewer_inputs(setup: InterviewSetup, turns: Sequence[QuestionTurn]) -> InterviewerInputs:
    return InterviewerInputs(
        role=setup.role,
        level=setup.level,
        interview_type=setup.interview_type,
        question_count=setup.question_count,
        job_description=setup.job_description_summary or setup.job_description,
        turns=turns,
        summary_used=setup.job_description_summary is not None,
    )


def bank_question(
    bank: list[BankQuestion],
    rng: random.Random,
    setup: InterviewSetup,
    position: int,
    main_number: int,
    used_bank_ids: set[str],
) -> InterviewQuestion:
    """The fallback when the LLM is off, fails, runs out of time or keeps breaking the contract."""
    picked = pick_fallback_question(
        bank,
        setup.role,
        setup.level,
        setup.interview_type,
        main_number,
        used_bank_ids,
        rng,
    )
    return InterviewQuestion(
        position=position,
        main_number=main_number,
        kind=QuestionKind.main,
        text=picked.text,
        category=picked.type,
        bank_id=picked.id,
        source=QuestionSource.bank,
    )


def llm_question(
    written: Written,
    results: Sequence[LLMResult],
    position: int,
    main_number: int,
    *,
    kind: QuestionKind = QuestionKind.main,
    thread: Thread | None = None,
    decision_version: str | None = None,
) -> InterviewQuestion:
    """A question the LLM wrote; `results` is every call of the turn, so the stored usage is what the turn cost.

    A follow-up takes its thread's main question as parent and its category, whatever the model would have chosen.
    """
    reply = written.reply
    assert reply is not None
    return InterviewQuestion(
        position=position,
        main_number=main_number,
        kind=kind,
        parent_question_id=thread.main_id if thread else None,
        text=reply.question,
        category=thread.category if thread else reply.category,
        source=QuestionSource.llm,
        model=written.results[-1].model,
        prompt_version=written.prompt_version,
        decision_prompt_version=decision_version,
        prompt_tokens=sum_known([r.prompt_tokens for r in results]),
        completion_tokens=sum_known([r.completion_tokens for r in results]),
        latency_ms=sum(r.latency_ms for r in results),
    )
