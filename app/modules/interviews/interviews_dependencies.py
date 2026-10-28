import random
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from .interviews_controller import InterviewsController
from .interviews_repository import InterviewsRepository
from .interviews_schema import BankQuestion
from .interviews_utils import QUESTION_BANK


def get_bank() -> list[BankQuestion]:
    """The question source; tests override it with a fixture bank."""
    return QUESTION_BANK


def get_controller(
    db: Annotated[Session, Depends(get_db)],
    bank: Annotated[list[BankQuestion], Depends(get_bank)],
) -> InterviewsController:
    return InterviewsController(InterviewsRepository(db), bank, random.Random())


InterviewsControllerDep = Annotated[InterviewsController, Depends(get_controller)]
