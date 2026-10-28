import uuid
from typing import Annotated

from fastapi import APIRouter, status

from app.core.errors import ErrorResponse
from app.modules.auth.auth_constants import Permission
from app.modules.auth.auth_dependencies import require_permissions
from app.modules.auth.auth_model import User

from .interviews_dependencies import InterviewsControllerDep
from .interviews_schema import InterviewCreateIn, InterviewOut

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


@router.post("", status_code=status.HTTP_201_CREATED, responses={409: {"model": ErrorResponse}})
def start_interview(
    data: InterviewCreateIn,
    user: Annotated[User, require_permissions(Permission.interviews_create)],
    ctrl: InterviewsControllerDep,
) -> InterviewOut:
    return ctrl.start(user, data)


@router.get("/{session_id}", status_code=status.HTTP_200_OK, responses={404: {"model": ErrorResponse}})
def get_interview(
    session_id: uuid.UUID,
    user: Annotated[User, require_permissions(Permission.interviews_read_self)],
    ctrl: InterviewsControllerDep,
) -> InterviewOut:
    return ctrl.get(user, session_id)
