import random
import time
from collections.abc import Callable
from typing import Annotated

from fastapi import Depends, Request
from sqlalchemy.orm import Session

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMProvider
from app.core.config import settings
from app.db.session import get_db

from .interviews_context import CONTEXT_MANAGER
from .interviews_controller import InterviewsController
from .interviews_repository import InterviewsRepository
from .interviews_schema import BankQuestion
from .interviews_utils import QUESTION_BANK


def get_bank() -> list[BankQuestion]:
    """The question source; tests override it with a fixture bank."""
    return QUESTION_BANK


def get_llm_provider(request: Request) -> LLMProvider | None:
    """Built once at startup (app lifespan); None when no key is configured or the lifespan didn't run."""
    return getattr(request.app.state, "llm_provider", None)


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
    )


InterviewsControllerDep = Annotated[InterviewsController, Depends(get_controller)]
