from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.errors import ErrorResponse
from app.db.session import get_db

from .controller import AuthController
from .repository import AuthRepository
from .schema import RegisterIn, UserOut

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={422: {"model": ErrorResponse}, 500: {"model": ErrorResponse}},
)


def get_controller(db: Session = Depends(get_db)) -> AuthController:  # noqa: B008
    return AuthController(AuthRepository(db))


@router.post(
    "/register",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    responses={409: {"model": ErrorResponse}},
)
def register(data: RegisterIn, ctrl: AuthController = Depends(get_controller)):  # noqa: B008
    return ctrl.register(data)
