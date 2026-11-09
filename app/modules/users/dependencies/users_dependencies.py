from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from ..controllers.users_controller import UsersController
from ..repositories.users_repository import UsersRepository
from ..services.users_service import UsersService


def get_service(db: Annotated[Session, Depends(get_db)]) -> UsersService:
    return UsersService(UsersRepository(db))


def get_controller(service: Annotated[UsersService, Depends(get_service)]) -> UsersController:
    return UsersController(service)


UsersControllerDep = Annotated[UsersController, Depends(get_controller)]
