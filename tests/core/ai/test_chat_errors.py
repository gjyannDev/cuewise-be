"""`to_llm_error`: every exception the LangChain/Gemini call layer can raise leaves `core/ai` as one of our LLMError
types (spec FR2, AC2). Real `google.api_core` exception objects; no network."""

import pytest
from google.api_core import exceptions as gx
from google.protobuf import duration_pb2
from google.rpc import error_details_pb2
from langchain_core.exceptions import OutputParserException
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError

from app.core.ai.chat_errors import to_llm_error
from app.core.ai.provider import (
    LLMBadResponseError,
    LLMError,
    LLMRateLimitError,
    LLMRequestError,
    LLMServerError,
    LLMTimeoutError,
)


def _retry_info(seconds: int, nanos: int = 0) -> error_details_pb2.RetryInfo:
    return error_details_pb2.RetryInfo(retry_delay=duration_pb2.Duration(seconds=seconds, nanos=nanos))


def test_a_429_with_retry_info_is_a_rate_limit_carrying_its_retry_after():  # EC5
    error = to_llm_error(gx.ResourceExhausted("quota", details=[_retry_info(7, 500_000_000)]))
    assert type(error) is LLMRateLimitError
    assert error.retry_after == 7.5 and error.status_code == 429 and error.retryable


def test_a_429_without_retry_info_is_a_rate_limit_with_no_retry_after():
    error = to_llm_error(gx.TooManyRequests("slow down"))
    assert type(error) is LLMRateLimitError and error.retry_after is None


def test_a_deadline_exceeded_is_a_timeout():  # EC7
    error = to_llm_error(gx.DeadlineExceeded("too slow"))
    assert type(error) is LLMTimeoutError and error.retryable


def test_a_python_timeout_is_a_timeout():
    assert type(to_llm_error(TimeoutError("read timed out"))) is LLMTimeoutError


@pytest.mark.parametrize("exc", [gx.ServiceUnavailable("down"), gx.InternalServerError("boom"), gx.BadGateway("gw")])
def test_a_5xx_is_a_server_error_with_its_status(exc):
    error = to_llm_error(exc)
    assert type(error) is LLMServerError and error.status_code == exc.code and error.retryable


@pytest.mark.parametrize("exc", [gx.PermissionDenied("no"), gx.NotFound("model"), gx.Unauthenticated("key")])
def test_a_4xx_is_a_request_error_and_not_retryable(exc):
    error = to_llm_error(exc)
    assert type(error) is LLMRequestError and error.status_code == exc.code and not error.retryable


def test_the_wrapped_invalid_argument_is_read_through_its_cause():
    try:
        try:
            raise gx.InvalidArgument("bad schema")
        except gx.InvalidArgument as inner:
            raise ChatGoogleGenerativeAIError("Invalid argument provided to Gemini") from inner
    except ChatGoogleGenerativeAIError as outer:
        error = to_llm_error(outer)
    assert type(error) is LLMRequestError and error.status_code == 400


def test_an_integration_error_with_no_google_cause_is_a_request_error():
    # e.g. a message type Gemini can't take: sending it again fails the same way.
    assert type(to_llm_error(ChatGoogleGenerativeAIError("unsupported message"))) is LLMRequestError


def test_an_unparsable_reply_is_a_bad_response():
    assert type(to_llm_error(OutputParserException("not json"))) is LLMBadResponseError


def test_one_of_our_errors_passes_through_unchanged():
    original = LLMServerError("already mapped", status_code=502)
    assert to_llm_error(original) is original


def test_the_original_exception_is_kept_as_the_cause():
    exc = gx.ServiceUnavailable("down")
    assert to_llm_error(exc).__cause__ is exc


def test_an_unknown_exception_is_a_generic_error_logged_by_class_only(log_lines):  # EC6
    error = to_llm_error(KeyError("candidate secret résumé text"))

    assert type(error) is LLMError and not error.retryable
    assert "résumé" not in str(error)
    [line] = log_lines.events("llm_error_unmapped")
    assert line["error_class"] == "KeyError"
    assert "résumé" not in log_lines.path.read_text(encoding="utf-8")
