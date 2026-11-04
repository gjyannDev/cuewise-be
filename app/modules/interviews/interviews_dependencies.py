import random
import time
from collections.abc import Callable
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
from app.modules.auth.auth_constants import Permission
from app.modules.auth.auth_dependencies import require_permissions
from app.modules.auth.auth_model import User

from .interviews_constants import TRANSCRIPTIONS_PER_MINUTE
from .interviews_context import CONTEXT_MANAGER
from .interviews_controller import InterviewsController
from .interviews_repository import InterviewsRepository
from .interviews_schema import BankQuestion
from .interviews_utils import QUESTION_BANK

# One per process: every request shares the counts (see core/rate_limit.py for the multi-instance caveat).
TRANSCRIPTION_LIMITER = RateLimiter(limit=TRANSCRIPTIONS_PER_MINUTE, window_seconds=60)


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


def get_controller(
    db: Annotated[Session, Depends(get_db)],
    bank: Annotated[list[BankQuestion], Depends(get_bank)],
    llm: Annotated[LLMProvider | None, Depends(get_llm_provider)],
    clock: Annotated[Callable[[], float], Depends(get_clock)],
    context: Annotated[ContextManager, Depends(get_context_manager)],
    tracer: Annotated[Tracer, Depends(get_tracer)],
    transcriber: Annotated[Transcriber | None, Depends(get_transcriber)],
) -> InterviewsController:
    return InterviewsController(
        InterviewsRepository(db),
        bank,
        random.Random(),
        llm,
        settings.llm_max_tokens,
        llm_budget_seconds=settings.llm_total_budget_seconds,
        clock=clock,
        context=context,
        tracer=tracer,
        transcriber=transcriber,
    )


InterviewsControllerDep = Annotated[InterviewsController, Depends(get_controller)]
