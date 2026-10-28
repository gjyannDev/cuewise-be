import random
import uuid

from app.core.errors import NotFoundError
from app.modules.auth.auth_model import User

from .interviews_constants import FIRST_POSITION
from .interviews_model import InterviewQuestion, InterviewSession
from .interviews_repository import InterviewsRepository
from .interviews_schema import (
    BankQuestion,
    InterviewCreateIn,
    InterviewOut,
    QuestionOut,
    SessionOut,
)
from .interviews_utils import select_questions


class InterviewsController:
    def __init__(
        self, repo: InterviewsRepository, bank: list[BankQuestion], rng: random.Random
    ):
        self.repo = repo
        self.bank = bank
        self.rng = rng

    def start(self, user: User, data: InterviewCreateIn) -> InterviewOut:
        picked = select_questions(
            self.bank,
            data.role,
            data.level,
            data.interview_type,
            data.question_count,
            self.rng,
        )
        session = InterviewSession(user_id=user.id, **data.model_dump())
        # Copy the text now: later bank edits must not change a session already started.
        questions = [
            InterviewQuestion(
                position=position, text=q.text, category=q.type, bank_id=q.id
            )
            for position, q in enumerate(picked, start=FIRST_POSITION)
        ]
        self.repo.start(session, questions)
        return InterviewOut(
            session=SessionOut.model_validate(session),
            current_question=QuestionOut.model_validate(questions[0]),
        )

    def get(self, user: User, session_id: uuid.UUID) -> InterviewOut:
        session = self.repo.get_for_user(session_id, user.id)
        if session is None:
            raise NotFoundError("Interview not found")
        # ponytail: always position 1 until answering exists (story 3 adds current_position).
        question = self.repo.get_question(session.id, FIRST_POSITION)
        return InterviewOut(
            session=SessionOut.model_validate(session),
            current_question=QuestionOut.model_validate(question),
        )
