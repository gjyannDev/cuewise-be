from collections.abc import Callable
from typing import Literal
from uuid import UUID

from pydantic import EmailStr, TypeAdapter

from app.core.errors import ConflictError, InvalidCredentialsError, TokenInvalidError
from app.core.security import hash_password, verify_password
from app.core.tokens import create_token, decode_token

from .auth_constants import Role, permissions_for
from .auth_model import User
from .auth_repository import AuthRepository
from .auth_schema import LoginIn, MeOut, RegisterIn
from .auth_utils import DUMMY_PASSWORD_HASH

_email_adapter = TypeAdapter(EmailStr)


class AuthController:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def register(self, data: RegisterIn) -> User:
        if self.repo.get_by_email(data.email):
            raise ConflictError("Email already registered", {"field": "email"})
        return self.repo.create(data.email, hash_password(data.password))

    def login(self, data: LoginIn) -> str:
        user = self.repo.get_by_email(data.email)
        # Always verify (against a dummy hash on a miss) so every failure takes the same time.
        password_ok = verify_password(data.password, user.password_hash if user else DUMMY_PASSWORD_HASH)
        if user is None or not password_ok or not user.is_active:
            raise InvalidCredentialsError("Invalid email or password")
        return create_token(user.id, user.role)

    def authenticate_token(self, token: str) -> User:
        claims = decode_token(token)
        try:
            user_id = UUID(claims["sub"])
        except ValueError as exc:
            raise TokenInvalidError("Access token is invalid") from exc
        user = self.repo.get_by_id(user_id)
        # Re-checked every request: deactivation takes effect without waiting for token expiry.
        if user is None or not user.is_active:
            raise TokenInvalidError("Access token is invalid")
        return user

    def profile(self, user: User) -> MeOut:
        return MeOut(id=user.id, email=user.email, role=user.role, permissions=sorted(permissions_for(user.role)))

    def ensure_admin(self, email: str, get_password: Callable[[], str]) -> Literal["created", "promoted", "unchanged"]:
        """Create `email` as an admin, or promote it if it exists. Safe to run repeatedly."""
        email = _email_adapter.validate_python(email)
        user = self.repo.get_by_email(email)
        if user is None:
            # Same validation as public registration, so a bootstrap admin can't have a weak password.
            data = RegisterIn(email=email, password=get_password())
            self.repo.create(data.email, hash_password(data.password), role=Role.admin)
            return "created"
        if user.role == Role.admin:
            return "unchanged"
        self.repo.set_role(user, Role.admin)
        return "promoted"
