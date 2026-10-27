from pydantic import BaseModel, ConfigDict, EmailStr


class UserAdminOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    role: str
    is_active: bool


class UserListOut(BaseModel):
    items: list[UserAdminOut]
    total: int
    limit: int
    offset: int
