from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from .auth_constants import Permission


class RegisterIn(BaseModel):
    # forbid: a client must not be able to smuggle in fields like "role".
    model_config = ConfigDict(extra="forbid")

    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class LoginIn(BaseModel):
    model_config = ConfigDict(extra="forbid")

    email: EmailStr
    # No password-strength rules on login (don't hint at them); max_length caps hashing cost.
    password: str = Field(min_length=1, max_length=128)


class TokenOut(BaseModel):
    access_token: str
    token_type: Literal["bearer"] = "bearer"


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: EmailStr


class MeOut(BaseModel):
    id: UUID
    email: EmailStr
    role: str
    permissions: list[Permission]
