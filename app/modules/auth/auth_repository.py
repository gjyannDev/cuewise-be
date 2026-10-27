from sqlalchemy import select
from sqlalchemy.orm import Session

from .auth_constants import Role
from .auth_model import User


class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        return self.db.scalar(select(User).where(User.email == email))

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.get(User, user_id)

    def create(self, email: str, password_hash: str, role: Role = Role.user) -> User:
        user = User(email=email, password_hash=password_hash, role=role)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def set_role(self, user: User, role: Role) -> User:
        user.role = role
        self.db.commit()
        self.db.refresh(user)
        return user
