import logging
import logging.config
import re
import sys
from contextvars import ContextVar
from pathlib import Path

LOG_FILE = Path("logs/app.log")
LOG_FORMAT = "%(asctime)s %(levelname)-7s [%(request_id)s] %(name)s: %(message)s"

# Set per request by RequestContextMiddleware; read by every log line.
request_id_ctx: ContextVar[str] = ContextVar("request_id", default="-")

# ANSI SGR codes for the dev console.
DIM, BOLD, GREEN = "2", "1", "32"
LEVEL_COLORS = {
    logging.DEBUG: "36",  # cyan
    logging.INFO: "32",  # green
    logging.WARNING: "33",  # yellow
    logging.ERROR: "31",  # red
    logging.CRITICAL: "1;41",  # bold on red
}
# Enough to tell concurrent requests apart on screen; the file keeps the full ID.
SHORT_REQUEST_ID = 8
_FIELD = re.compile(r"\w+=\S*")


class RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_ctx.get()
        return True


def split_fields(message: str) -> tuple[str, list[tuple[str, str]]]:
    """`llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message comes back whole, no fields."""
    event, *tokens = message.split() or [""]
    if not tokens or not all(_FIELD.fullmatch(token) for token in tokens):
        return message, []
    return event, [
        (key, value) for key, _, value in (token.partition("=") for token in tokens)
    ]


class ConsoleFormatter(logging.Formatter):
    """Dev console only: colours, and one field per line for `event key=value ...` records.

    The file handler keeps LOG_FORMAT (one line per record), so logs/app.log stays greppable and colour-free.
    """

    def __init__(self, use_color: bool = True) -> None:
        super().__init__(datefmt="%H:%M:%S")
        self.use_color = use_color

    def format(self, record: logging.LogRecord) -> str:
        level_color = LEVEL_COLORS.get(record.levelno, "")
        event, fields = split_fields(record.getMessage())
        request_id = str(getattr(record, "request_id", "-"))[:SHORT_REQUEST_ID]
        header = " ".join(
            [
                self._paint(
                    f"{self.formatTime(record, self.datefmt)}.{int(record.msecs):03d}",
                    DIM,
                ),
                self._paint(f"{record.levelname:<7}", f"{BOLD};{level_color}"),
                self._paint(f"[{request_id:<{SHORT_REQUEST_ID}}]", DIM),
                self._paint(f"{record.name}:", DIM),
                self._paint(event, BOLD) if fields else event,
            ]
        )
        width = max((len(key) for key, _ in fields), default=0)
        lines = [header]
        lines += [
            f"    {self._paint(key.ljust(width), DIM)}  {self._value(key, value, level_color)}"
            for key, value in fields
        ]
        if record.exc_info:
            lines.append(self.formatException(record.exc_info))
        return "\n".join(lines)

    def _value(self, key: str, value: str, level_color: str) -> str:
        if value == "-":
            return self._paint(value, DIM)
        if key == "outcome":
            # Success reads green; anything else takes the record's level colour (yellow warning, red error).
            ok = value == "ok" or value.endswith("_ok")
            return self._paint(value, f"{BOLD};{GREEN if ok else level_color}")
        return value

    def _paint(self, text: str, code: str) -> str:
        return f"\x1b[{code}m{text}\x1b[0m" if self.use_color and code else text


def setup_logging(debug: bool = False) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    # Colour codes only when a person is watching; piped or redirected output stays plain.
    use_color = sys.stderr.isatty()
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {"request_id": {"()": RequestIdFilter}},
            "formatters": {
                "default": {"format": LOG_FORMAT},
                "console": {"()": ConsoleFormatter, "use_color": use_color},
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "console",
                    "filters": ["request_id"],
                },
                "file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": str(LOG_FILE),
                    "maxBytes": 5 * 1024 * 1024,
                    "backupCount": 3,
                    "encoding": "utf-8",
                    "formatter": "default",
                    "filters": ["request_id"],
                },
            },
            "loggers": {
                "app": {
                    "handlers": ["console", "file"],
                    "level": "DEBUG" if debug else "INFO",
                    "propagate": False,
                },
                # RequestContextMiddleware writes the access line (with request ID); silence the duplicate.
                "uvicorn.access": {"level": "WARNING"},
            },
        }
    )
