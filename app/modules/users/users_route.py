from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.core.errors import ErrorResponse
from app.db.session import get_db
from app.modules.auth.auth_constants import Permission
from app.modules.auth.auth_dependencies import require_permissions

from .users_constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE
from .users_controller import UsersController
from .users_repository import UsersRepository
from .users_schema import UserListOut

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)


def get_controller(db: Annotated[Session, Depends(get_db)]) -> UsersController:
    return UsersController(UsersRepository(db))


UsersControllerDep = Annotated[UsersController, Depends(get_controller)]


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[require_permissions(Permission.users_read)],
)
def list_users(
    ctrl: UsersControllerDep,
    limit: Annotated[int, Query(ge=1, le=MAX_PAGE_SIZE)] = DEFAULT_PAGE_SIZE,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> UserListOut:
    return ctrl.list_users(limit, offset)
