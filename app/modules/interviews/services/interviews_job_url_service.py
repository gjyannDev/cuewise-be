"""Read a job description from a posting link or a pasted page (Slice 8b), then fit it to the job-description cap.

Link: safe fetch -> extract. Paste (for sites that block our fetch): the candidate's own browser copied the page, so
nothing is fetched -> clean. Both then share one tail: the job-term check and the cut, so the same rules apply.

Nothing is stored and no model is called. The text goes back to the candidate, who reviews it and starts the interview
with it as an ordinary `job_description`, so it reaches a model only through that path and its delimiters.

Every failure becomes a generic error; the real cause is logged. One line per request with sizes and the outcome:
never the URL (a query string can carry tokens), never the page or pasted text.
"""

import time
from typing import NamedTuple
from urllib.parse import urlsplit

from app.core.errors import (
    JobTextUnreadableError,
    JobUrlUnreachableError,
    JobUrlUnreadableError,
)
from app.core.logging import get_logger
from app.core.safe_fetch import (
    ResponseUnreadableError,
    SafeFetcher,
    UrlUnreachableError,
)
from app.modules.auth.models.auth_model import User

from ..constants.interviews_constants import (
    JOB_DESCRIPTION_MAX_LENGTH,
    JOB_TEXT_UNREADABLE_MESSAGE,
    JOB_URL_UNREACHABLE_MESSAGE,
    JOB_URL_UNREADABLE_MESSAGE,
    JobTextFormat,
)
from ..utils.interviews_job_url_utils import (
    extract_job_text,
    looks_like_job_posting,
    pasted_job_text,
    truncate_on_word,
)

# `user` comes from the request's log context (bound by the auth dependency).
job_url_logger = get_logger("app.job_url")


class JobText(NamedTuple):
    text: str
    truncated: bool


def _fit(text: str | None) -> JobText:
    """The shared tail: a posting with enough text, cut to the job-description cap."""
    if text is None:
        raise ResponseUnreadableError("too_little_text")
    # Judged on the whole text, before the cut: a long posting's terms may sit past 2000 characters.
    if not looks_like_job_posting(text):
        raise ResponseUnreadableError("not_a_posting")
    return JobText(*truncate_on_word(text, JOB_DESCRIPTION_MAX_LENGTH))


def _sizes(result: JobText | None) -> dict[str, object]:
    return {"chars": None, "truncated": None} if result is None else {"chars": len(result.text), "truncated": result.truncated}


class JobUrlService:
    def __init__(self, fetcher: SafeFetcher):
        self.fetcher = fetcher

    def import_job_text(self, user: User, url: str) -> JobText:
        started = time.perf_counter()
        outcome, size, result = "ok", None, None
        try:
            page = self.fetcher.fetch(url)
            size = page.size
            result = _fit(extract_job_text(page.html))
            return result
        except UrlUnreachableError as exc:
            outcome = f"unreachable:{exc.reason}"
            raise JobUrlUnreachableError(JOB_URL_UNREACHABLE_MESSAGE) from exc
        except ResponseUnreadableError as exc:
            outcome = f"unreadable:{exc.reason}"
            raise JobUrlUnreadableError(JOB_URL_UNREADABLE_MESSAGE) from exc
        finally:
            job_url_logger.info(
                "job_url",
                source="url",
                host=urlsplit(url).hostname or "-",
                bytes=size,
                **_sizes(result),
                latency_ms=round((time.perf_counter() - started) * 1000),
                outcome=outcome,
            )

    def import_pasted_text(self, user: User, content: str, content_format: JobTextFormat) -> JobText:
        started = time.perf_counter()
        outcome, result = "ok", None
        try:
            result = _fit(pasted_job_text(content, content_format))
            return result
        except ResponseUnreadableError as exc:
            outcome = f"unreadable:{exc.reason}"
            raise JobTextUnreadableError(JOB_TEXT_UNREADABLE_MESSAGE) from exc
        finally:
            job_url_logger.info(
                "job_url",
                source="paste",
                format=content_format,
                in_chars=len(content),
                **_sizes(result),
                latency_ms=round((time.perf_counter() - started) * 1000),
                outcome=outcome,
            )
