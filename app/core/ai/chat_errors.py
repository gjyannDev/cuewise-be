"""Map what the LangChain/Gemini call layer raises to our LLMError types (spec FR2).

Nothing vendor-shaped leaves `core/ai`: services and feature code only ever catch LLMError and its subclasses, as
they did with the hand-built provider. The Google SDK raises `google.api_core` exceptions, each carrying the HTTP
status as `.code`; langchain-google-genai re-raises some of them wrapped (its `ChatGoogleGenerativeAIError`, with the
Google error as `__cause__`), so the cause chain is searched, not only the outer exception.
"""

from google.api_core import exceptions as google_errors
from langchain_core.exceptions import OutputParserException
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError

from app.core.logging import get_logger

from .provider import (
    LLMBadResponseError,
    LLMError,
    LLMRateLimitError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)

logger = get_logger("app.llm")


def to_llm_error(exc: BaseException) -> LLMError:
    """The LLMError for `exc`, with `exc` as its cause. Messages are fixed text: a vendor message may echo the request,
    so it never reaches our errors or logs."""
    if isinstance(exc, LLMError):
        return exc
    error = _mapped(exc)
    error.__cause__ = exc
    return error


def _mapped(exc: BaseException) -> LLMError:
    google = _google_error(exc)
    if google is not None:
        return _from_status(google)
    if isinstance(exc, TimeoutError):
        return LLMTimeoutError("LLM request timed out")
    if isinstance(exc, OutputParserException):
        return LLMBadResponseError("LLM reply did not match the expected format")
    if isinstance(exc, ChatGoogleGenerativeAIError):
        # Raised by the integration itself for a request it can't send (e.g. an unsupported message): not transient.
        return LLMRequestError("LLM request rejected")
    # Only the class name: the message could carry anything, including the user's text.
    logger.warning("llm_error_unmapped", error_class=type(exc).__name__)
    return LLMError("LLM call failed")


def _google_error(exc: BaseException) -> google_errors.GoogleAPICallError | None:
    seen: set[int] = set()
    current: BaseException | None = exc
    while current is not None and id(current) not in seen:
        if isinstance(current, google_errors.GoogleAPICallError):
            return current
        seen.add(id(current))
        current = current.__cause__ or current.__context__
    return None


def _from_status(exc: google_errors.GoogleAPICallError) -> LLMError:
    status = exc.code
    if isinstance(exc, google_errors.DeadlineExceeded):
        return LLMTimeoutError("LLM request timed out", status_code=status)
    if status == 429:
        return LLMRateLimitError("LLM rate limited", status_code=status, retry_after=_retry_after(exc))
    if status is not None and status >= 500:
        return LLMServerError("LLM provider error", status_code=status)
    return LLMRequestError("LLM request rejected", status_code=status)


def _retry_after(exc: google_errors.GoogleAPICallError) -> float | None:
    """Seconds from the error's `google.rpc.RetryInfo` detail (Google's Retry-After); None when it has none."""
    for detail in exc.details or ():
        delay = getattr(detail, "retry_delay", None)
        if delay is not None:
            seconds = delay.ToTimedelta().total_seconds()
            return seconds if seconds >= 0 else None
    return None
