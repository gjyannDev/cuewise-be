import random
from typing import Annotated

from fastapi import Depends, Request
from sqlalchemy.orm import Session

from app.core.ai.provider import LLMProvider
from app.core.config import settings
from app.db.session import get_db

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


def get_controller(
    db: Annotated[Session, Depends(get_db)],
    bank: Annotated[list[BankQuestion], Depends(get_bank)],
    llm: Annotated[LLMProvider | None, Depends(get_llm_provider)],
) -> InterviewsController:
    return InterviewsController(InterviewsRepository(db), bank, random.Random(), llm, settings.llm_max_tokens)


InterviewsControllerDep = Annotated[InterviewsController, Depends(get_controller)]
