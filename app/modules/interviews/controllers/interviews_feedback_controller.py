"""End-of-interview feedback: request -> FeedbackService, stored row -> FeedbackOut, plus whether it was just made."""

import uuid

from app.modules.auth.models.auth_model import User

from ..ai.interviews_feedback import StoredResult
from ..constants.interviews_constants import (
    FEEDBACK_INSUFFICIENT_MESSAGE,
    FeedbackStatus,
)
from ..dependencies.models.interviews_model import InterviewFeedback
from ..schemas.interviews_schema import (
    FeedbackEvidenceOut,
    FeedbackOut,
    FeedbackQuestionOut,
)
from ..services.interviews_feedback_service import FeedbackService


class FeedbackController:
    def __init__(self, service: FeedbackService):
        self.service = service

    def get(self, user: User, session_id: uuid.UUID) -> FeedbackOut:
        return feedback_out(self.service.get(user, session_id))

    def generate(self, user: User, session_id: uuid.UUID) -> tuple[FeedbackOut, bool]:
        """The feedback and True when generated now (201), False when it was already stored (200)."""
        feedback, created = self.service.generate(user, session_id)
        return feedback_out(feedback), created


def feedback_out(feedback: InterviewFeedback) -> FeedbackOut:
    """What the client sees. Scores and text only once generated, so a half-written or failed row never shows any."""
    generated = feedback.status == FeedbackStatus.generated
    result = (
        StoredResult.model_validate(feedback.result)
        if generated and feedback.enough_evidence and feedback.result is not None
        else None
    )
    summary = FEEDBACK_INSUFFICIENT_MESSAGE if generated and feedback.enough_evidence is False else None
    return FeedbackOut(
        id=feedback.id,
        interview_id=feedback.session_id,
        status=FeedbackStatus(feedback.status),
        enough_evidence=feedback.enough_evidence,
        overall=feedback.overall if result else None,
        summary=result.summary if result else summary,
        strengths=result.strengths if result else [],
        improvements=result.improvements if result else [],
        next_steps=result.next_steps if result else [],
        questions=[
            FeedbackQuestionOut(
                main_number=q.main_number,
                category=q.category,
                question=q.question,
                scores=q.scores,
                note=q.note,
                evidence=[FeedbackEvidenceOut(criterion=e.criterion, quote=e.quote, reason=e.reason) for e in q.evidence],
            )
            for q in (result.questions if result else [])
        ],
        rubric_version=feedback.rubric_version,
        created_at=feedback.created_at,
    )
