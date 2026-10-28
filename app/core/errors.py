from typing import Any, ClassVar

from pydantic import BaseModel


class AppError(Exception):
    """Base for expected errors. Controllers raise these instead of HTTPException."""

    status_code: ClassVar[int] = 500
    code: ClassVar[str] = "INTERNAL_ERROR"
    headers: ClassVar[dict[str, str] | None] = None

    def __init__(self, message: str, details: Any = None, headers: dict[str, str] | None = None):
        super().__init__(message)
        self.message = message
        self.details = details
        # Instance copy so per-raise headers never mutate the class-level dict.
        self.response_headers = {**(type(self).headers or {}), **(headers or {})}


class BadRequestError(AppError):
    status_code, code = 400, "BAD_REQUEST"


class ForbiddenError(AppError):
    status_code, code = 403, "FORBIDDEN"


class NotFoundError(AppError):
    status_code, code = 404, "NOT_FOUND"


class ConflictError(AppError):
    status_code, code = 409, "CONFLICT"


class NotEnoughQuestionsError(ConflictError):
    code = "NOT_ENOUGH_QUESTIONS"


class UnauthorizedError(AppError):
    status_code, code = 401, "UNAUTHORIZED"
    headers = {"WWW-Authenticate": "Bearer"}


class InvalidCredentialsError(UnauthorizedError):
    code = "INVALID_CREDENTIALS"


class TokenMissingError(UnauthorizedError):
    code = "TOKEN_MISSING"


class TokenExpiredError(UnauthorizedError):
    code = "TOKEN_EXPIRED"


class TokenInvalidError(UnauthorizedError):
    code = "TOKEN_INVALID"


class ErrorBody(BaseModel):
    code: str
    message: str
    details: Any = None
    request_id: str | None = None


class ErrorResponse(BaseModel):
    error: ErrorBody
