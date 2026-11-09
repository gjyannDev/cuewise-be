"""Answer turns: request -> AnswerService, domain result -> AnswerOut, and the streamed turn's domain events -> SSE
frames. What the stream does (and logs) is decided in the service; this only names and shapes each event."""

import uuid
from collections.abc import AsyncGenerator
from contextlib import aclosing

from pydantic import BaseModel

from app.core.logging import request_id_ctx
from app.modules.auth.models.auth_model import User

from ..ai.interviews_turn import Delta, PhaseChanged, Reset
from ..constants.interviews_constants import StreamEvent
from ..schemas.interviews_schema import (
    AnswerIn,
    AnswerOut,
    QuestionDeltaOut,
    ReactionOut,
    ResetOut,
    SessionOut,
    StatusEventOut,
    StreamErrorOut,
    StreamEventOut,
)
from ..services.interviews_answer_service import (
    AnswerEvent,
    AnswerService,
    Reaction,
    ReactionChosen,
    TurnContext,
    TurnFailed,
    TurnResult,
    TurnSaved,
)
from .interviews_controller import question_out


class AnswerController:
    def __init__(self, service: AnswerService):
        self.service = service

    def answer(self, user: User, session_id: uuid.UUID, data: AnswerIn) -> AnswerOut:
        return answer_out(self.service.answer(user, session_id, data))

    def prepare_answer(self, user: User, session_id: uuid.UUID, data: AnswerIn) -> TurnContext:
        """The checks and reads before the stream opens (sync DB work: the route runs it in the threadpool)."""
        return self.service.prepare_answer(user, session_id, data)

    async def stream_answer(self, ctx: TurnContext, *, started_at: float) -> AsyncGenerator[StreamEventOut]:
        # A client that leaves closes the service's stream at once, so its summary log is written.
        async with aclosing(self.service.stream_answer(ctx, started_at=started_at)) as events:
            async for event in events:
                yield _frame(event)


def answer_out(result: TurnResult) -> AnswerOut:
    return AnswerOut(
        session=SessionOut.model_validate(result.session),
        reaction=_reaction_out(result.reaction),
        current_question=question_out(result.current_question),
    )


def _reaction_out(reaction: Reaction | None) -> ReactionOut | None:
    return None if reaction is None else ReactionOut(id=reaction.id, text=reaction.text)


def _frame(event: AnswerEvent) -> StreamEventOut:
    match event:
        case PhaseChanged(phase=phase):
            return _event(StreamEvent.status, StatusEventOut(phase=phase))
        case ReactionChosen(reaction=reaction):
            return _event(StreamEvent.reaction, ReactionOut(id=reaction.id, text=reaction.text))
        case Delta(text=text):
            return _event(StreamEvent.question_delta, QuestionDeltaOut(text=text))
        case Reset():
            return _event(StreamEvent.reset, ResetOut())
        case TurnSaved(result=result):
            return _event(StreamEvent.done, answer_out(result))
        case TurnFailed(code=code, message=message):
            return _error_event(code, message)
    raise AssertionError(f"unknown answer event {event!r}")


def _event(name: StreamEvent, data: BaseModel) -> StreamEventOut:
    return StreamEventOut(name, data)


def _error_event(code: str, message: str) -> StreamEventOut:
    request_id = request_id_ctx.get()
    return _event(
        StreamEvent.error,
        StreamErrorOut(code=code, message=message, request_id=None if request_id == "-" else request_id),
    )
