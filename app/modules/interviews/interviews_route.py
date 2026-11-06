import time
import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Query, Response, UploadFile, status
from fastapi.concurrency import run_in_threadpool
from sse_starlette.sse import EventSourceResponse

from app.core.errors import ErrorResponse
from app.core.pagination import PageDep
from app.modules.auth.auth_constants import Permission
from app.modules.auth.auth_dependencies import require_permissions
from app.modules.auth.auth_model import User

from .interviews_constants import (
    STREAM_PING_SECONDS,
    TRANSCRIPTION_MAX_BYTES,
    HistorySortColumn,
    SessionStatus,
    SortDirection,
)
from .interviews_dependencies import (
    FeedbackControllerDep,
    InterviewsControllerDep,
    limit_feedback,
    limit_transcriptions,
)
from .interviews_schema import (
    AnswerIn,
    AnswerOut,
    FeedbackOut,
    InterviewCreateIn,
    InterviewListOut,
    InterviewOut,
    TranscriptionOut,
    TranscriptOut,
)
from .interviews_utils import sse_frames

router = APIRouter(
    prefix="/interviews",
    tags=["interviews"],
    responses={
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)

# The contract for the client, shown in the OpenAPI docs of the stream route.
STREAM_DESCRIPTION = """\
Server-Sent Events, one per line pair (`event:` name, `data:` one line of JSON), in this order:

- `status` `{"phase": "received"}` at once, then `{"phase": "deciding"}` and `{"phase": "writing"}` as the turn runs
- `reaction` (a ReactionOut) before the next question, when the interview moves on or completes
- `question.delta` `{"text": ...}` chunks of the next question (append them)
- `reset` `{}`: discard the question text so far; another draft or the final question follows
- `done` (an AnswerOut, the same body POST /messages returns): the turn is saved
- `error` `{"code", "message", "request_id"}`: a generic message; nothing was saved
  (`QUESTION_NOT_CURRENT`: another submit of this question won, reload the interview)

Every stream ends with exactly one `done` or `error`. Comment lines (`: ping`) keep an idle connection open.
Closing the connection before `done` saves nothing: the same question is still current.
Errors before the stream opens (401, 403, 404, 409, 422) are plain JSON, like POST /messages."""


@router.post(
    "", status_code=status.HTTP_201_CREATED, responses={409: {"model": ErrorResponse}}
)
def start_interview(
    data: InterviewCreateIn,
    user: Annotated[User, require_permissions(Permission.interviews_create)],
    ctrl: InterviewsControllerDep,
) -> InterviewOut:
    return ctrl.start(user, data)


@router.get("", status_code=status.HTTP_200_OK)
def list_interviews(
    user: Annotated[User, require_permissions(Permission.interviews_read_self)],
    ctrl: InterviewsControllerDep,
    page: PageDep,
    # Named apart from `fastapi.status`; the client still sends `?status=`.
    status_filter: Annotated[SessionStatus | None, Query(alias="status")] = None,
    sort_by: HistorySortColumn = HistorySortColumn.created_at,
    sort_dir: SortDirection = SortDirection.desc,
) -> InterviewListOut:
    """The caller's own interviews (every status), newest first by default. `sort_by` / `sort_dir` sort the whole
    history, not just the page; ties are newest first. Under the default order the `in_progress` one, if any, is the
    first item; it can be continued with GET /interviews/{id} and its /messages."""
    return ctrl.list_interviews(user, status_filter, sort_by, sort_dir, page)


@router.get(
    "/{session_id}",
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorResponse}},
)
def get_interview(
    session_id: uuid.UUID,
    user: Annotated[User, require_permissions(Permission.interviews_read_self)],
    ctrl: InterviewsControllerDep,
) -> InterviewOut:
    return ctrl.get(user, session_id)


@router.post(
    "/{session_id}/messages",
    status_code=status.HTTP_201_CREATED,
    responses={404: {"model": ErrorResponse}, 409: {"model": ErrorResponse}},
)
def answer_question(
    session_id: uuid.UUID,
    data: AnswerIn,
    user: Annotated[User, require_permissions(Permission.interviews_answer)],
    ctrl: InterviewsControllerDep,
) -> AnswerOut:
    return ctrl.answer(user, session_id, data)


@router.post(
    "/{session_id}/messages/stream",
    status_code=status.HTTP_200_OK,
    response_class=EventSourceResponse,
    responses={
        200: {"description": STREAM_DESCRIPTION, "content": {"text/event-stream": {}}},
        404: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
    },
)
async def answer_question_stream(
    session_id: uuid.UUID,
    data: AnswerIn,
    user: Annotated[User, require_permissions(Permission.interviews_answer)],
    ctrl: InterviewsControllerDep,
) -> EventSourceResponse:
    started_at = time.perf_counter()
    # The checks (and the sync DB reads) run before the stream opens, so they fail as plain JSON errors.
    ctx = await run_in_threadpool(ctrl.prepare_answer, user, session_id, data)
    return EventSourceResponse(
        sse_frames(ctrl.stream_answer(ctx, started_at=started_at)), ping=STREAM_PING_SECONDS
    )


@router.get(
    "/{session_id}/messages",
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorResponse}},
)
def get_transcript(
    session_id: uuid.UUID,
    user: Annotated[User, require_permissions(Permission.interviews_read_self)],
    ctrl: InterviewsControllerDep,
) -> TranscriptOut:
    return ctrl.transcript(user, session_id)


@router.post(
    "/{session_id}/feedback",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(limit_feedback)],
    responses={
        200: {"model": FeedbackOut, "description": "Already generated: the stored feedback, no new LLM call."},
        404: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
        429: {"model": ErrorResponse},
        502: {"model": ErrorResponse},
        503: {"model": ErrorResponse},
    },
)
def generate_feedback(
    session_id: uuid.UUID,
    response: Response,
    user: Annotated[User, require_permissions(Permission.interviews_feedback)],
    ctrl: FeedbackControllerDep,
) -> FeedbackOut:
    """Score and write the feedback on a completed interview, once; the request waits for it (several seconds).

    201: generated now (or too few answers to assess: `enough_evidence` false, no scores). 200: already generated,
    the same body. 409 `INTERVIEW_NOT_COMPLETED` or `FEEDBACK_IN_PROGRESS`. 502 `FEEDBACK_FAILED`: no scores could be
    produced, POST again to retry. 503 `FEEDBACK_UNAVAILABLE`: the LLM is off."""
    feedback, created = ctrl.generate(user, session_id)
    if not created:
        response.status_code = status.HTTP_200_OK
    return feedback


@router.get(
    "/{session_id}/feedback",
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorResponse}},
)
def get_feedback(
    session_id: uuid.UUID,
    user: Annotated[User, require_permissions(Permission.interviews_feedback)],
    ctrl: FeedbackControllerDep,
) -> FeedbackOut:
    """The stored feedback in any status (`generating`, `generated`, `failed`); never calls the LLM. Scores and text
    appear only once `generated`. 404 `FEEDBACK_NOT_FOUND` when none was requested yet."""
    return ctrl.get(user, session_id)


@router.post(
    "/{session_id}/transcriptions",
    status_code=status.HTTP_200_OK,
    response_model=TranscriptionOut,
    dependencies=[Depends(limit_transcriptions)],
    responses={
        404: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
        413: {"model": ErrorResponse},
        415: {"model": ErrorResponse},
        429: {"model": ErrorResponse},
        503: {"model": ErrorResponse},
    },
)
async def transcribe_answer(
    session_id: uuid.UUID,
    audio: UploadFile,
    user: Annotated[User, require_permissions(Permission.interviews_answer)],
    ctrl: InterviewsControllerDep,
) -> TranscriptionOut:
    """A recorded answer (multipart part `audio`: WebM, OGG, MP4 or WAV, up to 3 MB) as text for the candidate to
    review. Nothing is saved; the text becomes an answer only if they send it to /messages."""
    role = await run_in_threadpool(ctrl.prepare_transcription, user, session_id)
    # One byte past the cap is enough to know it's too large, and the rest is never held in memory.
    data = await audio.read(TRANSCRIPTION_MAX_BYTES + 1)
    return await ctrl.transcribe(user, session_id, role, data, audio.content_type or "")
