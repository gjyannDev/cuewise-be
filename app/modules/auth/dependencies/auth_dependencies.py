from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.errors import ForbiddenError, TokenMissingError
from app.db.session import get_db

from ..constants.auth_constants import Permission, Role, permissions_for
from ..controllers.auth_controller import AuthController
from ..models.auth_model import User
from ..repositories.auth_repository import AuthRepository
from ..services.auth_service import AuthService

# auto_error=False: we raise our own TokenMissingError so 401s keep the standard error shape.
bearer_scheme = HTTPBearer(auto_error=False)


def get_service(db: Annotated[Session, Depends(get_db)]) -> AuthService:
    return AuthService(AuthRepository(db))


AuthServiceDep = Annotated[AuthService, Depends(get_service)]


def get_controller(service: AuthServiceDep) -> AuthController:
    return AuthController(service)


AuthControllerDep = Annotated[AuthController, Depends(get_controller)]


def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
    service: AuthServiceDep,
) -> User:
    token = credentials.credentials.strip() if credentials else ""
    if not token:
        raise TokenMissingError("Authentication required")
    return service.authenticate_token(token)


CurrentUserDep = Annotated[User, Depends(get_current_user)]


def require_roles(*roles: Role):
    """Route guard: the caller's DB role must be one of `roles`. Use for coarse gates like an admin area."""

    def check(user: CurrentUserDep) -> User:
        if user.role not in roles:
            raise ForbiddenError("You do not have access to this resource")
        return user

    return Depends(check)


def require_permissions(*perms: Permission):
    """Route guard: the caller's DB role must grant every permission in `perms`."""

    def check(user: CurrentUserDep) -> User:
        if not set(perms) <= permissions_for(user.role):
            raise ForbiddenError("You do not have access to this resource")
        return user

    return Depends(check)
