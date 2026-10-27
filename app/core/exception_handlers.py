import logging
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, OperationalError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.config import settings
from app.core.errors import AppError
from app.core.logging import request_id_ctx

logger = logging.getLogger("app.errors")

_HTTP_CODES = {
    400: "BAD_REQUEST",
    401: "UNAUTHORIZED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    405: "METHOD_NOT_ALLOWED",
    409: "CONFLICT",
    429: "TOO_MANY_REQUESTS",
}


def _error_response(
    request: Request,
    status_code: int,
    code: str,
    message: str,
    details: Any = None,
    headers: Mapping[str, str] | None = None,
) -> JSONResponse:
    request_id = getattr(request.state, "request_id", None)
    headers = {**(headers or {}), **({"X-Request-ID": request_id} if request_id else {})}
    body = {"error": {"code": code, "message": message, "details": details, "request_id": request_id}}
    return JSONResponse(status_code=status_code, content=body, headers=headers)


def _raise_location(exc: BaseException) -> str:
    """'(path/to/file.py:42 func)' of the innermost frame, i.e. where the error was raised."""
    tb = exc.__traceback__
    if tb is None:
        return ""
    while tb.tb_next:
        tb = tb.tb_next
    code = tb.tb_frame.f_code
    filename = Path(code.co_filename)
    try:
        shown = filename.resolve().relative_to(Path.cwd()).as_posix()
    except ValueError:  # outside the project (or on another drive)
        shown = filename.name
    return f" ({shown}:{tb.tb_lineno} {code.co_name})"


async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    log = logger.error if exc.status_code >= 500 else logger.info
    log("%s: %s%s", exc.code, exc.message, _raise_location(exc))
    return _error_response(request, exc.status_code, exc.code, exc.message, exc.details, exc.response_headers)


async def validation_error_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    # Deliberately omit Pydantic's "input" so submitted passwords/tokens are never echoed back.
    details = [
        {"field": ".".join(str(part) for part in err["loc"]), "issue": err["msg"], "type": err["type"]}
        for err in exc.errors()
    ]
    logger.info("VALIDATION_ERROR: %s", details)
    return _error_response(request, 422, "VALIDATION_ERROR", "Request validation failed", details)


async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    code = _HTTP_CODES.get(exc.status_code, "HTTP_ERROR")
    return _error_response(request, exc.status_code, code, str(exc.detail), headers=exc.headers)


async def integrity_error_handler(request: Request, exc: IntegrityError) -> JSONResponse:
    # DB text names tables/constraints, so it goes to logs only.
    logger.warning("IntegrityError: %s", exc.orig)
    return _error_response(request, 409, "CONFLICT", "Resource conflicts with existing data")


async def operational_error_handler(request: Request, exc: OperationalError) -> JSONResponse:
    logger.error("DATABASE_UNAVAILABLE: %s", exc.orig)
    return _error_response(request, 503, "DATABASE_UNAVAILABLE", "Database is unavailable")


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    # Runs in ServerErrorMiddleware, outside RequestContextMiddleware, after it reset the
    # context var, so restore the request id from scope state while logging.
    request_id = getattr(request.state, "request_id", None)
    token = request_id_ctx.set(request_id or "-")
    try:
        logger.exception("Unhandled %s: %s", type(exc).__name__, exc, exc_info=exc)
    finally:
        request_id_ctx.reset(token)
    details = {"type": type(exc).__name__, "message": str(exc)} if settings.debug else None
    return _error_response(request, 500, "INTERNAL_ERROR", "An unexpected error occurred", details)


def register_exception_handlers(app: FastAPI) -> None:
    # Any: Starlette types handlers as taking plain Exception, so specific signatures don't type-check.
    handlers: list[tuple[type[Exception], Any]] = [
        (AppError, app_error_handler),
        (RequestValidationError, validation_error_handler),
        (StarletteHTTPException, http_exception_handler),
        (IntegrityError, integrity_error_handler),
        (OperationalError, operational_error_handler),
        (Exception, unhandled_exception_handler),
    ]
    for exc_class, handler in handlers:
        app.add_exception_handler(exc_class, handler)
