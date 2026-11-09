import random
import time
from collections.abc import Callable
from datetime import UTC, datetime
from typing import Annotated

from fastapi import Depends, Request
from sqlalchemy.orm import Session

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMProvider
from app.core.ai.tracing import Tracer
from app.core.ai.transcriber import Transcriber
from app.core.config import settings
from app.core.errors import RateLimitedError
from app.core.rate_limit import RateLimiter
from app.db.session import get_db
from app.modules.auth.constants.auth_constants import Permission
from app.modules.auth.dependencies.auth_dependencies import require_permissions
from app.modules.auth.models.auth_model import User

from ..ai.interviews_context import CONTEXT_MANAGER
from ..constants.interviews_constants import (
    FEEDBACKS_PER_MINUTE,
    TRANSCRIPTIONS_PER_MINUTE,
)
from ..controllers.interviews_answer_controller import AnswerController
from ..controllers.interviews_controller import InterviewsController
from ..controllers.interviews_feedback_controller import FeedbackController
from ..controllers.interviews_transcription_controller import TranscriptionController
from ..repositories.interviews_repository import InterviewsRepository
from ..schemas.interviews_schema import BankQuestion
from ..services.interviews_answer_service import AnswerService
from ..services.interviews_feedback_service import FeedbackService
from ..services.interviews_service import InterviewsService
from ..services.interviews_transcription_service import TranscriptionService
from ..utils.interviews_utils import QUESTION_BANK

# One per process: every request shares the counts (see core/rate_limit.py for the multi-instance caveat).
TRANSCRIPTION_LIMITER = RateLimiter(limit=TRANSCRIPTIONS_PER_MINUTE, window_seconds=60)
FEEDBACK_LIMITER = RateLimiter(limit=FEEDBACKS_PER_MINUTE, window_seconds=60)


def get_bank() -> list[BankQuestion]:
    """The question source; tests override it with a fixture bank."""
    return QUESTION_BANK


def get_llm_provider(request: Request) -> LLMProvider | None:
    """Built once at startup (app lifespan); None when no key is configured or the lifespan didn't run."""
    return getattr(request.app.state, "llm_provider", None)


def get_transcriber(request: Request) -> Transcriber | None:
    """Built once at startup (app lifespan); None when no Deepgram key is configured or the lifespan didn't run."""
    return getattr(request.app.state, "transcriber", None)


def get_transcription_limiter() -> RateLimiter:
    """Tests swap in a fresh limiter so counts never leak between them."""
    return TRANSCRIPTION_LIMITER


def limit_transcriptions(
    user: Annotated[User, require_permissions(Permission.interviews_answer)],
    limiter: Annotated[RateLimiter, Depends(get_transcription_limiter)],
) -> None:
    """Per-user cap on transcriptions, checked before the upload goes anywhere that costs money."""
    retry_after = limiter.hit(str(user.id))
    if retry_after is not None:
        raise RateLimitedError(
            "Too many recordings. Wait a moment and try again.", headers={"Retry-After": str(retry_after)}
        )


def get_tracer(request: Request) -> Tracer:
    """Built once at startup (app lifespan); a disabled tracer when the lifespan didn't run."""
    return getattr(request.app.state, "tracer", None) or Tracer(None)


def get_clock() -> Callable[[], float]:
    """Monotonic clock for the per-turn LLM time budget; tests swap in a fake one."""
    return time.monotonic


def get_context_manager() -> ContextManager:
    """Decides what each LLM call sends; tests swap in one with a tiny limit."""
    return CONTEXT_MANAGER


def get_interviews_service(
    db: Annotated[Session, Depends(get_db)],
    bank: Annotated[list[BankQuestion], Depends(get_bank)],
    llm: Annotated[LLMProvider | None, Depends(get_llm_provider)],
    clock: Annotated[Callable[[], float], Depends(get_clock)],
    context: Annotated[ContextManager, Depends(get_context_manager)],
    tracer: Annotated[Tracer, Depends(get_tracer)],
) -> InterviewsService:
    return InterviewsService(
        InterviewsRepository(db),
        bank,
        random.Random(),
        llm,
        settings.llm_max_tokens,
        llm_budget_seconds=settings.llm_total_budget_seconds,
        clock=clock,
        context=context,
        tracer=tracer,
    )


def get_interviews_controller(
    service: Annotated[InterviewsService, Depends(get_interviews_service)],
) -> InterviewsController:
    return InterviewsController(service)


InterviewsControllerDep = Annotated[InterviewsController, Depends(get_interviews_controller)]


def get_answer_service(
    db: Annotated[Session, Depends(get_db)],
    bank: Annotated[list[BankQuestion], Depends(get_bank)],
    llm: Annotated[LLMProvider | None, Depends(get_llm_provider)],
    clock: Annotated[Callable[[], float], Depends(get_clock)],
    context: Annotated[ContextManager, Depends(get_context_manager)],
    tracer: Annotated[Tracer, Depends(get_tracer)],
) -> AnswerService:
    return AnswerService(
        InterviewsRepository(db),
        bank,
        random.Random(),
        llm,
        settings.llm_max_tokens,
        llm_budget_seconds=settings.llm_total_budget_seconds,
        clock=clock,
        context=context,
        tracer=tracer,
    )


def get_answer_controller(service: Annotated[AnswerService, Depends(get_answer_service)]) -> AnswerController:
    return AnswerController(service)


AnswerControllerDep = Annotated[AnswerController, Depends(get_answer_controller)]


def get_transcription_service(
    db: Annotated[Session, Depends(get_db)],
    transcriber: Annotated[Transcriber | None, Depends(get_transcriber)],
) -> TranscriptionService:
    return TranscriptionService(InterviewsRepository(db), transcriber)


def get_transcription_controller(
    service: Annotated[TranscriptionService, Depends(get_transcription_service)],
) -> TranscriptionController:
    return TranscriptionController(service)


TranscriptionControllerDep = Annotated[TranscriptionController, Depends(get_transcription_controller)]


def get_feedback_limiter() -> RateLimiter:
    """Tests swap in a fresh limiter so counts never leak between them."""
    return FEEDBACK_LIMITER


def limit_feedback(
    user: Annotated[User, require_permissions(Permission.interviews_feedback)],
    limiter: Annotated[RateLimiter, Depends(get_feedback_limiter)],
) -> None:
    """Per-user cap on feedback requests, checked before anything that can cost an LLM call."""
    retry_after = limiter.hit(str(user.id))
    if retry_after is not None:
        raise RateLimitedError(
            "Too many feedback requests. Wait a moment and try again.", headers={"Retry-After": str(retry_after)}
        )


def _utc_now() -> datetime:
    return datetime.now(UTC)


def get_now() -> Callable[[], datetime]:
    """Wall-clock time for stored timestamps (the feedback claim and its stale takeover); tests swap in a fake one."""
    return _utc_now


def get_feedback_service(
    db: Annotated[Session, Depends(get_db)],
    llm: Annotated[LLMProvider | None, Depends(get_llm_provider)],
    clock: Annotated[Callable[[], float], Depends(get_clock)],
    now: Annotated[Callable[[], datetime], Depends(get_now)],
    context: Annotated[ContextManager, Depends(get_context_manager)],
    tracer: Annotated[Tracer, Depends(get_tracer)],
) -> FeedbackService:
    return FeedbackService(
        InterviewsRepository(db),
        llm,
        context=context,
        clock=clock,
        now=now,
        tracer=tracer,
        budget_seconds=settings.feedback_total_budget_seconds,
        stale_margin_seconds=settings.feedback_stale_margin_seconds,
        score_max_tokens=settings.feedback_score_max_tokens,
        write_max_tokens=settings.feedback_write_max_tokens,
        score_temperature=settings.feedback_score_temperature,
    )


FeedbackServiceDep = Annotated[FeedbackService, Depends(get_feedback_service)]


def get_feedback_controller(service: FeedbackServiceDep) -> FeedbackController:
    return FeedbackController(service)


FeedbackControllerDep = Annotated[FeedbackController, Depends(get_feedback_controller)]
