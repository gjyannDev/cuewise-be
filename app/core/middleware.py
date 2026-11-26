import re
import time
from typing import Any
from uuid import uuid4

from starlette.types import ASGIApp, Message, Receive, Scope, Send

from app.core.logging import get_logger, request_log_context

logger = get_logger("app.request")

# A client-supplied id ends up in logs and headers, so only accept a safe shape.
_SAFE_REQUEST_ID = re.compile(r"[A-Za-z0-9_-]{1,64}")


class RequestContextMiddleware:
    """Assigns each request an id, echoes it as X-Request-ID, and logs one access line.

    Pure ASGI (not BaseHTTPMiddleware) so it doesn't break streaming responses.
    """

    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        incoming = dict(scope["headers"]).get(b"x-request-id", b"").decode("latin-1")
        request_id = incoming if _SAFE_REQUEST_ID.fullmatch(incoming) else uuid4().hex
        # The request's log fields (request_id now; user and session once known), shared by every log line of the
        # request. Kept in scope state too, for the 500 handler, which runs after this middleware has exited.
        log_fields: dict[str, Any] = {"request_id": request_id}
        state = scope.setdefault("state", {})
        state["request_id"] = request_id
        state["log_fields"] = log_fields
        status_code = 500  # stays 500 if the app raises before sending a response
        start = time.perf_counter()

        async def send_with_request_id(message: Message) -> None:
            nonlocal status_code
            if message["type"] == "http.response.start":
                status_code = message["status"]
                headers = list(message.get("headers", []))
                # Error handlers already set it; don't send it twice.
                if not any(name.lower() == b"x-request-id" for name, _ in headers):
                    headers.append((b"x-request-id", request_id.encode()))
                message["headers"] = headers
            await send(message)

        with request_log_context(log_fields):
            try:
                await self.app(scope, receive, send_with_request_id)
            finally:
                duration_ms = (time.perf_counter() - start) * 1000
                log = logger.warning if status_code >= 500 else logger.info
                log(
                    "http_request",
                    method=scope["method"],
                    path=scope["path"],
                    status=status_code,
                    duration_ms=round(duration_ms, 1),
                )
