"""Interview lifecycle: request -> InterviewsService, domain result -> response schema."""

import uuid

from app.core.pagination import PageParams
from app.modules.auth.models.auth_model import User

from ..constants.interviews_constants import (
    HistorySortColumn,
    InterviewType,
    JobRole,
    Level,
    SessionStatus,
    SortDirection,
)
from ..models.interviews_model import InterviewQuestion
from ..schemas.interviews_schema import (
    InterviewCreateIn,
    InterviewListItemOut,
    InterviewListOut,
    InterviewOut,
    QuestionOut,
    SessionOut,
    TranscriptOut,
)
from ..services.interviews_service import InterviewsService, InterviewState
from ..utils.interviews_utils import build_transcript


class InterviewsController:
    def __init__(self, service: InterviewsService):
        self.service = service

    def start(self, user: User, data: InterviewCreateIn) -> InterviewOut:
        return interview_out(self.service.start(user, data))

    def get(self, user: User, session_id: uuid.UUID) -> InterviewOut:
        return interview_out(self.service.get(user, session_id))

    def list_interviews(
        self,
        user: User,
        status: SessionStatus | None,
        sort_by: HistorySortColumn,
        sort_dir: SortDirection,
        page: PageParams,
    ) -> InterviewListOut:
        history = self.service.list_interviews(user, status, sort_by, sort_dir, page)
        items = [
            InterviewListItemOut(
                id=s.id,
                role=JobRole(s.role),
                level=Level(s.level),
                interview_type=InterviewType(s.interview_type),
                status=SessionStatus(s.status),
                question_count=s.question_count,
                answered_count=answered,
                created_at=s.created_at,
            )
            for s, answered in history.rows
        ]
        return InterviewListOut(items=items, total=history.total, limit=page.limit, offset=page.offset)

    def transcript(self, user: User, session_id: uuid.UUID) -> TranscriptOut:
        transcript = self.service.transcript(user, session_id)
        return TranscriptOut(items=build_transcript(transcript.questions, transcript.messages))


def interview_out(state: InterviewState) -> InterviewOut:
    return InterviewOut(session=SessionOut.model_validate(state.session), current_question=question_out(state.current_question))


def question_out(question: InterviewQuestion | None) -> QuestionOut | None:
    return None if question is None else QuestionOut.model_validate(question)
