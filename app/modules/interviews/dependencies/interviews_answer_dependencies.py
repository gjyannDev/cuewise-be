import random
from collections.abc import Callable
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.ai.chat import ChatModel
from app.core.ai.context import ContextManager
from app.core.ai.dependencies import get_chat_model
from app.core.ai.tracing import Tracer
from app.core.config import settings
from app.db.session import get_db
from app.modules.profile.dependencies.profile_dependencies import get_profile_service
from app.modules.profile.services.profile_service import ProfileService

from ..controllers.interviews_answer_controller import AnswerController
from ..dependencies.interviews_shared_dependencies import (
    get_bank,
    get_clock,
    get_context_manager,
    get_tracer,
)
from ..repositories.interviews_repository import InterviewsRepository
from ..schemas.interviews_schema import BankQuestion
from ..services.interviews_answer_service import AnswerService


def get_answer_service(
    db: Annotated[Session, Depends(get_db)],
    bank: Annotated[list[BankQuestion], Depends(get_bank)],
    chat_model: Annotated[ChatModel | None, Depends(get_chat_model)],
    clock: Annotated[Callable[[], float], Depends(get_clock)],
    context: Annotated[ContextManager, Depends(get_context_manager)],
    tracer: Annotated[Tracer, Depends(get_tracer)],
    profiles: Annotated[ProfileService, Depends(get_profile_service)],
) -> AnswerService:
    return AnswerService(
        InterviewsRepository(db),
        bank,
        random.Random(),
        chat_model,
        settings.llm_max_tokens,
        llm_budget_seconds=settings.llm_total_budget_seconds,
        clock=clock,
        context=context,
        tracer=tracer,
        profiles=profiles,
    )


def get_answer_controller(service: Annotated[AnswerService, Depends(get_answer_service)]) -> AnswerController:
    return AnswerController(service)


AnswerControllerDep = Annotated[AnswerController, Depends(get_answer_controller)]
