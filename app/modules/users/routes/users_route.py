from fastapi import APIRouter, status

from app.core.errors import ErrorResponse
from app.core.pagination import PageDep
from app.modules.auth.constants.auth_constants import Permission
from app.modules.auth.dependencies.auth_dependencies import require_permissions

from ..dependencies.users_dependencies import UsersControllerDep
from ..schemas.users_schema import UserListOut

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


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    dependencies=[require_permissions(Permission.users_read)],
)
def list_users(ctrl: UsersControllerDep, page: PageDep) -> UserListOut:
    return ctrl.list_users(page)
