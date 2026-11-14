from typing import Annotated

from fastapi import APIRouter, Depends, File, status
from fastapi.concurrency import run_in_threadpool
from fastapi.exceptions import RequestValidationError

from app.core.errors import ErrorResponse

from ..constants.profile_constants import RESUME_MAX_BYTES
from ..dependencies.profile_dependencies import (
    ProfileControllerDep,
    ProfileUser,
    limit_resume_uploads,
)
from ..schemas.profile_schema import ProfileOut, ResumeUploadIn

router = APIRouter(
    prefix="/profile",
    tags=["profile"],
    responses={
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)


@router.post(
    "/resume",
    status_code=status.HTTP_200_OK,
    response_model=ProfileOut,
    dependencies=[Depends(limit_resume_uploads)],
    responses={
        413: {"model": ErrorResponse},
        415: {"model": ErrorResponse},
        429: {"model": ErrorResponse},
        502: {"model": ErrorResponse},
        503: {"model": ErrorResponse},
    },
)
async def upload_resume(
    form: Annotated[ResumeUploadIn, File()],
    user: ProfileUser,
    ctrl: ProfileControllerDep,
) -> ProfileOut:
    """A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes the signed-in user's profile,
    replacing any previous one; the response is what was understood. The file and its text are never stored.

    413 `RESUME_TOO_LARGE`, 415 `RESUME_UNSUPPORTED`, 422 `RESUME_UNREADABLE` (encrypted, scanned, no résumé in it),
    502 `PROFILE_EXTRACTION_FAILED` (try again), 503 `PROFILE_UNAVAILABLE`. A failed upload keeps the old profile."""
    # One byte past the cap is enough to know it's too large, and the rest is never held in memory.
    data = await form.file.read(RESUME_MAX_BYTES + 1)
    if not data:
        raise RequestValidationError([{"loc": ("body", "file"), "msg": "The file is empty", "type": "value_error"}])
    return await run_in_threadpool(ctrl.upload, user, data)


@router.get("", status_code=status.HTTP_200_OK, response_model=ProfileOut, responses={404: {"model": ErrorResponse}})
def get_profile(user: ProfileUser, ctrl: ProfileControllerDep) -> ProfileOut:
    """The signed-in user's profile; 404 `PROFILE_NOT_FOUND` before the first upload."""
    return ctrl.get(user)


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(user: ProfileUser, ctrl: ProfileControllerDep) -> None:
    """Remove the signed-in user's profile for good; 204 also when there was none."""
    ctrl.delete(user)
