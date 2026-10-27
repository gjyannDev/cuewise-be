import logging
import logging.config
from contextvars import ContextVar
from pathlib import Path

LOG_FILE = Path("logs/app.log")
LOG_FORMAT = "%(asctime)s %(levelname)-7s [%(request_id)s] %(name)s: %(message)s"

# Set per request by RequestContextMiddleware; read by every log line.
request_id_ctx: ContextVar[str] = ContextVar("request_id", default="-")


class RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_ctx.get()
        return True


def setup_logging(debug: bool = False) -> None:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {"request_id": {"()": RequestIdFilter}},
            "formatters": {"default": {"format": LOG_FORMAT}},
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
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
