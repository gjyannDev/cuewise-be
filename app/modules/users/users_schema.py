from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

from app.core.pagination import Page


class UserAdminOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: EmailStr
    role: str
    is_active: bool


class UserListOut(Page[UserAdminOut]):
    pass
