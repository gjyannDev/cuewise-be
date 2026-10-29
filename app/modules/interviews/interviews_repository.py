import uuid
from typing import cast

from sqlalchemy import CursorResult, select, update
from sqlalchemy.orm import Session

from .interviews_constants import SessionStatus
from .interviews_model import InterviewMessage, InterviewQuestion, InterviewSession


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

    def release(self) -> None:
        """End the read transaction before a slow call, so no connection sits idle in a transaction meanwhile.

        Every loaded object expires afterwards: callers copy what they need into plain values first.
        """
        self.db.rollback()

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

    def list_questions(self, session_id: uuid.UUID, up_to_position: int) -> list[InterviewQuestion]:
        return list(
            self.db.scalars(
                select(InterviewQuestion)
                .where(InterviewQuestion.session_id == session_id, InterviewQuestion.position <= up_to_position)
                .order_by(InterviewQuestion.position)
            )
        )

    def list_messages(self, session_id: uuid.UUID) -> list[InterviewMessage]:
        # UUIDv7 ids are time-ordered, so id order is the order they were saved.
        return list(
            self.db.scalars(
                select(InterviewMessage).where(InterviewMessage.session_id == session_id).order_by(InterviewMessage.id)
            )
        )

    def record_turn(
        self,
        answer: InterviewMessage,
        reaction: InterviewMessage,
        next_question: InterviewQuestion | None,
        expected_position: int,
        *,
        completes: bool,
    ) -> bool:
        """Save one whole turn in one commit: advance the session, the answer, the reaction and the next question.

        A compare-and-swap: the conditional UPDATE matches zero rows when another request already moved the session
        on (double-click, retry, a newer interview) or it is no longer in progress, and then nothing is saved.
        All or nothing, so a session never waits at a position that has no question.
        """
        advance = (
            {"status": SessionStatus.completed}
            if completes
            else {"current_position": InterviewSession.current_position + 1}
        )
        try:
            result = cast(
                CursorResult,
                self.db.execute(
                    update(InterviewSession)
                    .where(
                        InterviewSession.id == answer.session_id,
                        InterviewSession.status == SessionStatus.in_progress,
                        InterviewSession.current_position == expected_position,
                    )
                    .values(**advance)
                ),
            )
            if result.rowcount != 1:
                self.db.rollback()
                return False
            self.db.add_all([answer, reaction])
            if next_question is not None:
                next_question.session_id = answer.session_id
                self.db.add(next_question)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        return True

    def _abandon_in_progress(self, user_id: uuid.UUID) -> None:
        self.db.execute(
            update(InterviewSession)
            .where(InterviewSession.user_id == user_id, InterviewSession.status == SessionStatus.in_progress)
            .values(status=SessionStatus.abandoned)
        )
