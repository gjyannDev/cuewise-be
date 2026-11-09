from ..constants.auth_constants import permissions_for
from ..models.auth_model import User
from ..schemas.auth_schema import LoginIn, MeOut, RegisterIn, TokenOut, UserOut
from ..services.auth_service import AuthService


class AuthController:
    """Request -> service call, domain result -> response schema."""

    def __init__(self, service: AuthService):
        self.service = service

    def register(self, data: RegisterIn) -> UserOut:
        return UserOut.model_validate(self.service.register(data))

    def login(self, data: LoginIn) -> TokenOut:
        return TokenOut(access_token=self.service.login(data))

    def profile(self, user: User) -> MeOut:
        return MeOut(id=user.id, email=user.email, role=user.role, permissions=sorted(permissions_for(user.role)))
