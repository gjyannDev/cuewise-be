import uuid
from collections.abc import Mapping, Sequence
from datetime import datetime
from typing import Any, cast

from sqlalchemy import (
    ColumnElement,
    CursorResult,
    UnaryExpression,
    and_,
    func,
    or_,
    select,
    update,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..constants.interviews_constants import (
    FeedbackStatus,
    HistorySortColumn,
    SessionStatus,
    SortDirection,
)
from ..models.interviews_knowledge_model import InterviewSessionChunk, KnowledgeChunk
from ..models.interviews_model import (
    InterviewFeedback,
    InterviewMessage,
    InterviewQuestion,
    InterviewSession,
)
from ..utils.interviews_knowledge_utils import ReferenceNote

# UUIDv7 ids are time-ordered, so `created_at` sorts by id: start order, served by ix_interview_sessions_user_id_id.
_HISTORY_SORT_COLUMNS = {
    HistorySortColumn.created_at: InterviewSession.id,
    HistorySortColumn.role: InterviewSession.role,
    HistorySortColumn.level: InterviewSession.level,
    HistorySortColumn.interview_type: InterviewSession.interview_type,
    HistorySortColumn.status: InterviewSession.status,
}


def _history_filter(user_id: uuid.UUID, status: SessionStatus | None) -> list[ColumnElement[bool]]:
    """The rows one user's history lists and counts: always only their own, optionally of one status."""
    conditions = [InterviewSession.user_id == user_id]
    if status is not None:
        conditions.append(InterviewSession.status == status)
    return conditions


def _history_order(sort_by: HistorySortColumn, sort_dir: SortDirection) -> list[UnaryExpression]:
    """The requested column (its stored value, not the label), then `id desc` so ties are newest first and pages
    never overlap or skip a row."""
    column = _HISTORY_SORT_COLUMNS[sort_by]
    order = [column.asc() if sort_dir == SortDirection.asc else column.desc()]
    if sort_by != HistorySortColumn.created_at:
        order.append(InterviewSession.id.desc())
    return order


class InterviewsRepository:
    def __init__(self, db: Session):
        self.db = db

    def start(
        self,
        session: InterviewSession,
        questions: list[InterviewQuestion],
        note_refs: Sequence[InterviewSessionChunk] = (),
    ) -> InterviewSession:
        """Abandon the user's active session and save the new one with its questions and its reference notes, all or
        nothing."""
        try:
            # Before the insert, so the one-in-progress-per-user index never sees two rows.
            self._abandon_in_progress(session.user_id)
            self.db.add(session)
            self.db.flush()  # assigns session.id for the questions' foreign key
            for row in [*questions, *note_refs]:
                row.session_id = session.id
            self.db.add_all([*questions, *note_refs])
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

    def refresh(self, *rows: object | None) -> None:
        """Reload rows a commit expired, so reading their fields later needs no database call."""
        for row in rows:
            if row is not None:
                self.db.refresh(row)

    def reference_notes(self, session_id: uuid.UUID) -> list[ReferenceNote]:
        """The notes stored for this interview at start, rank order; none for interviews without (or from before) them.
        Read from the rows the interview points at, so a later re-ingest never changes them."""
        rows = self.db.execute(
            select(
                KnowledgeChunk.id,
                KnowledgeChunk.competency,
                KnowledgeChunk.text,
                InterviewSessionChunk.rank,
                InterviewSessionChunk.score,
            )
            .join(KnowledgeChunk, KnowledgeChunk.id == InterviewSessionChunk.chunk_id)
            .where(InterviewSessionChunk.session_id == session_id)
            .order_by(InterviewSessionChunk.rank)
        )
        return [ReferenceNote(*row) for row in rows]

    def get_for_user(self, session_id: uuid.UUID, user_id: uuid.UUID) -> InterviewSession | None:
        # Keyed on the owner too, so "missing" and "someone else's" are indistinguishable.
        return self.db.scalar(
            select(InterviewSession).where(InterviewSession.id == session_id, InterviewSession.user_id == user_id)
        )

    def list_for_user(
        self,
        user_id: uuid.UUID,
        status: SessionStatus | None,
        sort_by: HistorySortColumn,
        sort_dir: SortDirection,
        limit: int,
        offset: int,
    ) -> list[tuple[InterviewSession, int | None]]:
        """A page of the user's sessions in the requested order, each with the main-question number of the question it
        waits on (None if that row is missing). One query: the number comes from a correlated subquery, not a query per
        row."""
        current_main_number = (
            select(InterviewQuestion.main_number)
            .where(
                InterviewQuestion.session_id == InterviewSession.id,
                InterviewQuestion.position == InterviewSession.current_position,
            )
            .scalar_subquery()
        )
        rows = self.db.execute(
            select(InterviewSession, current_main_number)
            .where(*_history_filter(user_id, status))
            .order_by(*_history_order(sort_by, sort_dir))
            .limit(limit)
            .offset(offset)
        )
        return [(session, main_number) for session, main_number in rows]

    def count_for_user(self, user_id: uuid.UUID, status: SessionStatus | None) -> int:
        return (
            self.db.scalar(select(func.count()).select_from(InterviewSession).where(*_history_filter(user_id, status)))
            or 0
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

    def get_session(self, session_id: uuid.UUID) -> InterviewSession | None:
        """Any user's session, by id: for the report script only (the API always goes through get_for_user)."""
        return self.db.get(InterviewSession, session_id)

    def latest_sessions(self, limit: int) -> list[InterviewSession]:
        # UUIDv7 ids are time-ordered, so the highest ids are the newest interviews.
        return list(self.db.scalars(select(InterviewSession).order_by(InterviewSession.id.desc()).limit(limit)))

    def list_session_questions(self, session_id: uuid.UUID) -> list[InterviewQuestion]:
        return list(
            self.db.scalars(
                select(InterviewQuestion)
                .where(InterviewQuestion.session_id == session_id)
                .order_by(InterviewQuestion.position)
            )
        )

    def list_all_questions(self) -> list[InterviewQuestion]:
        """Every stored question, grouped by interview in creation order (UUIDv7), for the usage report script."""
        return list(
            self.db.scalars(
                select(InterviewQuestion).order_by(InterviewQuestion.session_id, InterviewQuestion.position)
            )
        )

    def record_turn(
        self,
        answer: InterviewMessage,
        reaction: InterviewMessage | None,
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
            # No reaction before a follow-up: it comes straight after the answer.
            self.db.add_all([m for m in (answer, reaction) if m is not None])
            if next_question is not None:
                next_question.session_id = answer.session_id
                self.db.add(next_question)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        return True

    # --- end-of-interview feedback ---

    def get_feedback(self, session_id: uuid.UUID) -> InterviewFeedback | None:
        return self.db.scalar(select(InterviewFeedback).where(InterviewFeedback.session_id == session_id))

    def insert_feedback(self, feedback: InterviewFeedback) -> bool:
        """The first claim of an interview's feedback. False when another request inserted first: the unique
        session_id lets only one of two simultaneous requests win."""
        try:
            self.db.add(feedback)
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            return False
        return True

    def reclaim_feedback(self, session_id: uuid.UUID, started_at: datetime, stale_before: datetime) -> bool:
        """Take over a `failed` row, or a `generating` one whose request died (started before `stale_before`).

        A compare-and-swap, like record_turn: the age check is part of the UPDATE (never done in Python), so of two
        requests only one matches, and a fresh `generating` or a `generated` row is never touched. Stored scores are
        kept, so a takeover only has to write the text.
        """
        result = cast(
            CursorResult,
            self.db.execute(
                update(InterviewFeedback)
                .where(
                    InterviewFeedback.session_id == session_id,
                    or_(
                        InterviewFeedback.status == FeedbackStatus.failed,
                        and_(
                            InterviewFeedback.status == FeedbackStatus.generating,
                            InterviewFeedback.started_at < stale_before,
                        ),
                    ),
                )
                .values(status=FeedbackStatus.generating, started_at=started_at, finished_at=None, failure_reason=None)
                # No in-Python evaluation against loaded rows: SQLite hands back timezone-naive datetimes, and the
                # commit below expires every loaded object anyway.
                .execution_options(synchronize_session=False)
            ),
        )
        if result.rowcount != 1:
            self.db.rollback()
            return False
        self.db.commit()
        return True

    def update_claimed_feedback(
        self, feedback_id: uuid.UUID, claimed_at: datetime, values: Mapping[str, Any]
    ) -> bool:
        """Write to the row only while this request still holds its claim (still `generating`, same `started_at`).
        False = another request took it over meanwhile, and nothing was written."""
        result = cast(
            CursorResult,
            self.db.execute(
                update(InterviewFeedback)
                .where(
                    InterviewFeedback.id == feedback_id,
                    InterviewFeedback.status == FeedbackStatus.generating,
                    InterviewFeedback.started_at == claimed_at,
                )
                .values(**values)
                .execution_options(synchronize_session=False)
            ),
        )
        if result.rowcount != 1:
            self.db.rollback()
            return False
        self.db.commit()
        return True

    def _abandon_in_progress(self, user_id: uuid.UUID) -> None:
        self.db.execute(
            update(InterviewSession)
            .where(InterviewSession.user_id == user_id, InterviewSession.status == SessionStatus.in_progress)
            .values(status=SessionStatus.abandoned)
        )
