"""The app's logging: structlog on top of the standard library's `logging`.

Every log line, from the app, from libraries (uvicorn, sqlalchemy, httpx) and from code still calling
`logging.getLogger(...)`, goes through one processor chain:

    merge context -> add logger, level, timestamp -> request_id default -> traceback -> redact -> render

The file always gets one JSON object per line; the console gets a readable view in debug and the same JSON otherwise.
Redaction runs before any renderer, so no output can skip it.
"""

import json
import logging
import sys
from collections.abc import Iterator, Mapping
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any, TextIO

import structlog
from structlog.typing import EventDict, Processor, WrappedLogger

LOG_FILE = Path("logs/app.log")
LOG_MAX_BYTES = 5 * 1024 * 1024
LOG_BACKUPS = 3

# Keys every JSON line has; anything else on the line is a field of the event.
RECORD_KEYS = ("timestamp", "level", "logger", "request_id", "event")

# A value logged under one of these keys (any depth, any case) is replaced before it is written. Key names only: a
# secret inside free text (a library's own message, an exception message) is not scanned.
SENSITIVE_KEYS = frozenset(
    {
        "answer",
        "resume",
        "job_description",
        "token",
        "access_token",
        "refresh_token",
        "password",
        "authorization",
        "api_key",
        "secret",
        "cookie",
    }
)
REDACTED = "[redacted]"

# What `get_logger` returns, for annotations; features name this, never structlog itself.
Logger = structlog.stdlib.BoundLogger

# ANSI SGR codes for the dev console.
DIM, BOLD, GREEN = "2", "1", "32"
LEVEL_COLORS = {
    "debug": "36",  # cyan
    "info": "32",  # green
    "warning": "33",  # yellow
    "error": "31",  # red
    "critical": "1;41",  # bold on red
}
# Enough to tell concurrent requests apart on screen; the file keeps the full ID.
SHORT_REQUEST_ID = 8

# Library loggers that log at INFO: their INFO lines include full request URLs, so only warnings and up are kept.
_ROOT_LEVEL = logging.WARNING
_UVICORN_LOGGERS = ("uvicorn", "uvicorn.error", "uvicorn.access")
_installed_handlers: list[logging.Handler] = []



# --- request context ---

# One dict per HTTP request, created by RequestContextMiddleware. FastAPI runs sync dependencies and endpoints in
# worker threads, each with a *copy* of the context: a value bound in one thread would never reach the next. Every
# copy points at the same dict, so a field bound anywhere in the request (the auth dependency binds `user`, a service
# binds `session`) shows up on every later line of that request, in any thread and in the streamed SSE response.
_request_fields: ContextVar[dict[str, Any] | None] = ContextVar("log_request_fields", default=None)


@contextmanager
def request_log_context(fields: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """Makes `fields` (at least `request_id`) part of every log line inside the block."""
    token = _request_fields.set(fields)
    try:
        yield fields
    finally:
        _request_fields.reset(token)


def bind_log_context(**fields: Any) -> None:
    """Adds fields to every later log line of the current request (or, outside a request, of the current context)."""
    current = _request_fields.get()
    if current is None:
        structlog.contextvars.bind_contextvars(**fields)
    else:
        current.update(fields)


def current_request_id() -> str | None:
    current = _request_fields.get()
    return None if current is None else current.get("request_id")


# --- processors ---


def _merge_request_fields(_logger: WrappedLogger, _method: str, event_dict: EventDict) -> EventDict:
    # A field the call passes itself wins over the request's.
    for key, value in (_request_fields.get() or {}).items():
        event_dict.setdefault(key, value)
    return event_dict


def _default_request_id(_logger: WrappedLogger, _method: str, event_dict: EventDict) -> EventDict:
    # Set by the request's log context; `-` outside a request.
    event_dict.setdefault("request_id", "-")
    return event_dict


def _redacted(key: object, value: Any) -> Any:
    if isinstance(key, str) and key.lower() in SENSITIVE_KEYS:
        return REDACTED
    if isinstance(value, Mapping):
        return {k: _redacted(k, v) for k, v in value.items()}
    if isinstance(value, list | tuple | set):
        return [_redacted(None, v) for v in value]
    return value


def redact_sensitive(_logger: WrappedLogger, _method: str, event_dict: EventDict) -> EventDict:
    """Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything renders the event."""
    return {k: _redacted(k, v) for k, v in event_dict.items()}


_SHARED: list[Processor] = [
    structlog.contextvars.merge_contextvars,
    _merge_request_fields,
    structlog.stdlib.add_logger_name,
    structlog.stdlib.add_log_level,
    structlog.stdlib.PositionalArgumentsFormatter(),
    structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
    _default_request_id,
    structlog.processors.StackInfoRenderer(),
    # The traceback becomes one `exception` string, so a crash stays one JSON line.
    structlog.processors.format_exc_info,
    redact_sensitive,
]


def _json(value: object) -> str:
    # UUIDs, datetimes, exceptions and anything else JSON can't encode are written as text, never raised.
    return str(value)


class ReadableRenderer:
    """Dev console: time, level, short request id, logger, event, then one aligned `key  value` row per field."""

    def __init__(self, use_color: bool) -> None:
        self.use_color = use_color

    def __call__(self, _logger: WrappedLogger, _method: str, event_dict: EventDict) -> str:
        event_dict = dict(event_dict)
        level = str(event_dict.pop("level", _method))
        level_color = LEVEL_COLORS.get(level, "")
        exception = event_dict.pop("exception", None)
        record = {key: event_dict.pop(key, "-") for key in RECORD_KEYS}
        fields = event_dict
        request_id = str(record["request_id"])[:SHORT_REQUEST_ID]
        header = " ".join(
            [
                self._paint(self._time(str(record["timestamp"])), DIM),
                self._paint(f"{level.upper():<7}", f"{BOLD};{level_color}"),
                self._paint(f"[{request_id:<{SHORT_REQUEST_ID}}]", DIM),
                self._paint(f"{record['logger']}:", DIM),
                self._paint(str(record["event"]), BOLD) if fields else str(record["event"]),
            ]
        )
        width = max((len(str(key)) for key in fields), default=0)
        lines = [header]
        lines += [
            f"    {self._paint(str(key).ljust(width), DIM)}  {self._value(str(key), value, level_color)}"
            for key, value in fields.items()
        ]
        if exception:
            lines.append(str(exception))
        return "\n".join(lines)

    @staticmethod
    def _time(timestamp: str) -> str:
        try:
            moment = datetime.fromisoformat(timestamp).astimezone()
        except ValueError:
            return timestamp
        return f"{moment:%H:%M:%S}.{moment.microsecond // 1000:03d}"

    def _value(self, key: str, value: Any, level_color: str) -> str:
        if value is None or value == "-":
            return self._paint("-", DIM)
        text = str(value).lower() if isinstance(value, bool) else str(value)
        if key == "outcome":
            # Success reads green; anything else takes the record's level colour (yellow warning, red error).
            ok = text == "ok" or text.endswith("_ok")
            return self._paint(text, f"{BOLD};{GREEN if ok else level_color}")
        return text

    def _paint(self, text: str, code: str) -> str:
        return f"\x1b[{code}m{text}\x1b[0m" if self.use_color and code else text


class _StderrHandler(logging.StreamHandler):
    """Writes to whatever `sys.stderr` is at the time of the write (test runners and reloaders swap it)."""

    def __init__(self) -> None:
        super().__init__()

    @property
    def stream(self) -> TextIO:  # type: ignore[override]
        return sys.stderr

    @stream.setter
    def stream(self, _value: TextIO) -> None:
        pass


def _formatter(renderer: Processor) -> structlog.stdlib.ProcessorFormatter:
    return structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=_SHARED,
        processors=[structlog.stdlib.ProcessorFormatter.remove_processors_meta, renderer],
    )


def _json_renderer() -> Processor:
    return structlog.processors.JSONRenderer(serializer=json.dumps, default=_json)


def setup_logging(debug: bool = False, log_file: Path = LOG_FILE, stream: TextIO | None = None) -> None:
    """Routes every logger through the processor chain. Safe to call again (tests do): it replaces only its own
    handlers, so pytest's capture handlers stay attached."""
    structlog.configure(
        processors=[structlog.stdlib.filter_by_level, *_SHARED, structlog.stdlib.ProcessorFormatter.wrap_for_formatter],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    console = logging.StreamHandler(stream) if stream is not None else _StderrHandler()
    # Colour codes only when a person is watching; piped or redirected output stays plain.
    use_color = (stream or sys.stderr).isatty()
    console.setFormatter(_formatter(ReadableRenderer(use_color) if debug else _json_renderer()))
    handlers: list[logging.Handler] = [console]
    file_error: OSError | None = None
    try:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = RotatingFileHandler(log_file, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUPS, encoding="utf-8")
    except OSError as exc:
        file_error = exc
    else:
        file_handler.setFormatter(_formatter(_json_renderer()))
        handlers.append(file_handler)

    root = logging.getLogger()
    for old in _installed_handlers:
        root.removeHandler(old)
        old.close()
    _installed_handlers[:] = handlers
    for handler in handlers:
        root.addHandler(handler)
    root.setLevel(_ROOT_LEVEL)

    app_logger = logging.getLogger("app")
    app_logger.handlers.clear()
    app_logger.propagate = True
    app_logger.setLevel(logging.DEBUG if debug else logging.INFO)
    # uvicorn installs its own handlers before the app loads; hand its records to the root handlers instead.
    for name in _UVICORN_LOGGERS:
        uvicorn_logger = logging.getLogger(name)
        uvicorn_logger.handlers.clear()
        uvicorn_logger.propagate = True
    # RequestContextMiddleware writes the access line (with request ID); silence the duplicate.
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)

    if file_error is not None:
        # The API keeps running on console logs alone; a broken disk must not take it down.
        get_logger("app.logging").warning("log_file_unavailable", path=str(log_file), error=type(file_error).__name__)


def get_logger(name: str) -> Logger:
    return structlog.get_logger(name)
