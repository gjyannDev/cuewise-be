from app.core.errors import ConflictError
from app.core.security import hash_password

from .model import User
from .repository import AuthRepository
from .schema import RegisterIn


class AuthController:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def register(self, data: RegisterIn) -> User:
        if self.repo.get_by_email(data.email):
            raise ConflictError("Email already registered", {"field": "email"})
        return self.repo.create(data.email, hash_password(data.password))
