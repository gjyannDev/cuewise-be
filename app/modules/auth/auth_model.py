from sqlalchemy import String, true
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base

from .auth_constants import Role


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str]
    # Plain string column, not a native DB enum, so adding a role needs no ALTER TYPE migration.
    role: Mapped[str] = mapped_column(String(32), default=Role.user, server_default=Role.user.value)
    is_active: Mapped[bool] = mapped_column(default=True, server_default=true())
