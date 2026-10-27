import logging
import re
import time
from uuid import uuid4

from starlette.types import ASGIApp, Message, Receive, Scope, Send

from app.core.logging import request_id_ctx

logger = logging.getLogger("app.request")

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
        # Context var for log lines; scope state for the 500 handler, which runs after this exits.
        scope.setdefault("state", {})["request_id"] = request_id
        token = request_id_ctx.set(request_id)
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

        try:
            await self.app(scope, receive, send_with_request_id)
        finally:
            duration_ms = (time.perf_counter() - start) * 1000
            log = logger.warning if status_code >= 500 else logger.info
            log("%s %s -> %s (%.1fms)", scope["method"], scope["path"], status_code, duration_ms)
            request_id_ctx.reset(token)
