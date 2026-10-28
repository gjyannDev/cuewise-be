import uuid

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from .interviews_constants import SessionStatus
from .interviews_model import InterviewQuestion, InterviewSession


class InterviewsRepository:
    def __init__(self, db: Session):
        self.db = db

    def start(self, session: InterviewSession, questions: list[InterviewQuestion]) -> InterviewSession:
        """Abandon the user's active session and save the new one with its questions, all or nothing."""
        try:
            # Before the insert, so the one-in-progress-per-user index never sees two rows.
            self._abandon_in_progress(session.user_id)
            self.db.add(session)
            self.db.flush()  # assigns session.id for the questions' foreign key
            for question in questions:
                question.session_id = session.id
            self.db.add_all(questions)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        self.db.refresh(session)
        return session

    def get_for_user(self, session_id: uuid.UUID, user_id: uuid.UUID) -> InterviewSession | None:
        # Keyed on the owner too, so "missing" and "someone else's" are indistinguishable.
        return self.db.scalar(
            select(InterviewSession).where(InterviewSession.id == session_id, InterviewSession.user_id == user_id)
        )

    def get_question(self, session_id: uuid.UUID, position: int) -> InterviewQuestion | None:
        return self.db.scalar(
            select(InterviewQuestion).where(
                InterviewQuestion.session_id == session_id, InterviewQuestion.position == position
            )
        )

    def _abandon_in_progress(self, user_id: uuid.UUID) -> None:
        self.db.execute(
            update(InterviewSession)
            .where(InterviewSession.user_id == user_id, InterviewSession.status == SessionStatus.in_progress)
            .values(status=SessionStatus.abandoned)
        )
