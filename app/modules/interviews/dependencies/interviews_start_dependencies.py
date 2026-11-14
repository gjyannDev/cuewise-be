import random
from collections.abc import Callable
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.ai.context import ContextManager
from app.core.ai.embedder import Embedder
from app.core.ai.provider import LLMProvider
from app.core.ai.tracing import Tracer
from app.core.config import settings
from app.db.session import get_db
from app.modules.profile.dependencies.profile_dependencies import get_profile_service
from app.modules.profile.services.profile_service import ProfileService

from ..controllers.interviews_controller import InterviewsController
from ..dependencies.interviews_shared_dependencies import (
    get_bank,
    get_clock,
    get_context_manager,
    get_embedder,
    get_llm_provider,
    get_tracer,
)
from ..repositories.interviews_knowledge_repository import KnowledgeRepository
from ..repositories.interviews_repository import InterviewsRepository
from ..schemas.interviews_schema import BankQuestion
from ..services.interviews_retrieval_service import RetrievalService
from ..services.interviews_service import InterviewsService


def get_retrieval_service(
    db: Annotated[Session, Depends(get_db)],
    embedder: Annotated[Embedder | None, Depends(get_embedder)],
    llm: Annotated[LLMProvider | None, Depends(get_llm_provider)],
    clock: Annotated[Callable[[], float], Depends(get_clock)],
    tracer: Annotated[Tracer, Depends(get_tracer)],
) -> RetrievalService:
    return RetrievalService(KnowledgeRepository(db), embedder, llm_on=llm is not None, tracer=tracer, clock=clock)


def get_interviews_service(
    db: Annotated[Session, Depends(get_db)],
    bank: Annotated[list[BankQuestion], Depends(get_bank)],
    llm: Annotated[LLMProvider | None, Depends(get_llm_provider)],
    clock: Annotated[Callable[[], float], Depends(get_clock)],
    context: Annotated[ContextManager, Depends(get_context_manager)],
    tracer: Annotated[Tracer, Depends(get_tracer)],
    retrieval: Annotated[RetrievalService, Depends(get_retrieval_service)],
    profiles: Annotated[ProfileService, Depends(get_profile_service)],
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
        retrieval=retrieval,
        profiles=profiles,
    )


def get_interviews_controller(
    service: Annotated[InterviewsService, Depends(get_interviews_service)],
) -> InterviewsController:
    return InterviewsController(service)


InterviewsControllerDep = Annotated[InterviewsController, Depends(get_interviews_controller)]
