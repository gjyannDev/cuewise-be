from fastapi import HTTPException, status

from app.core.security import hash_password

from .model import User
from .repository import AuthRepository
from .schema import RegisterIn


class AuthController:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def register(self, data: RegisterIn) -> User:
        if self.repo.get_by_email(data.email):
            raise HTTPException(status.HTTP_409_CONFLICT, "Email already registered")
        return self.repo.create(data.email, hash_password(data.password))
