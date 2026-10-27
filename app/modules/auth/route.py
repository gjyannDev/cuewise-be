from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db

from .controller import AuthController
from .repository import AuthRepository
from .schema import RegisterIn, UserOut

router = APIRouter(prefix="/auth", tags=["auth"])


def get_controller(db: Session = Depends(get_db)) -> AuthController:
    return AuthController(AuthRepository(db))


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(data: RegisterIn, ctrl: AuthController = Depends(get_controller)):
    return ctrl.register(data)
