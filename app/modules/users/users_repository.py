from collections.abc import Sequence

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.modules.auth.auth_model import User


class UsersRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self, limit: int, offset: int) -> Sequence[User]:
        return self.db.scalars(select(User).order_by(User.id).limit(limit).offset(offset)).all()

    def count(self) -> int:
        return self.db.scalar(select(func.count()).select_from(User)) or 0
