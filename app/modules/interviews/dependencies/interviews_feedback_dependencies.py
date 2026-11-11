from collections.abc import Callable
from datetime import datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMProvider
from app.core.ai.tracing import Tracer
from app.core.config import settings
from app.core.errors import RateLimitedError
from app.core.rate_limit import RateLimiter
from app.db.session import get_db
from app.modules.auth.constants.auth_constants import Permission
from app.modules.auth.dependencies.auth_dependencies import require_permissions
from app.modules.auth.models.auth_model import User

from ..constants.interviews_constants import FEEDBACKS_PER_MINUTE
from ..controllers.interviews_feedback_controller import FeedbackController
from ..dependencies.interviews_shared_dependencies import (
    get_clock,
    get_context_manager,
    get_llm_provider,
    get_now,
    get_tracer,
)
from ..repositories.interviews_repository import InterviewsRepository
from ..services.interviews_feedback_service import FeedbackService

# One per process: every request shares the counts (see core/rate_limit.py for the multi-instance caveat).
FEEDBACK_LIMITER = RateLimiter(limit=FEEDBACKS_PER_MINUTE, window_seconds=60)


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
