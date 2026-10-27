from typing import Annotated

from fastapi import APIRouter, status

from app.core.errors import ErrorResponse

from .auth_constants import Permission
from .auth_dependencies import AuthControllerDep, require_permissions
from .auth_model import User
from .auth_schema import LoginIn, MeOut, RegisterIn, TokenOut, UserOut

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={422: {"model": ErrorResponse}, 500: {"model": ErrorResponse}},
)


@router.post(
    "/register",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    responses={409: {"model": ErrorResponse}},
)
def register(data: RegisterIn, ctrl: AuthControllerDep):
    return ctrl.register(data)


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    responses={401: {"model": ErrorResponse}},
)
def login(data: LoginIn, ctrl: AuthControllerDep) -> TokenOut:
    return TokenOut(access_token=ctrl.login(data))


@router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    responses={401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}},
)
def me(
    user: Annotated[User, require_permissions(Permission.users_read_self)],
    ctrl: AuthControllerDep,
) -> MeOut:
    return ctrl.profile(user)
