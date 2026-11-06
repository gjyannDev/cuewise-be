"""Hints for feedback failures: where to look first, shown in Langfuse next to the failure (live traces and eval runs).

Code-derived: every reason code the contract can raise must have a hint, so a new code without one fails here."""

import inspect
import re

import pytest

from app.core.ai import provider
from app.modules.interviews import interviews_feedback, interviews_reply
from app.modules.interviews.interviews_feedback_turn import hint_for

RAISED = re.compile(r'InvalidReplyError\("(\w+)"\)')


def reason_codes() -> set[str]:
    source = inspect.getsource(interviews_feedback) + inspect.getsource(interviews_reply.load_object)
    return set(RAISED.findall(source)) | {"truncated"}


def test_every_reason_the_contract_can_raise_has_a_hint():
    codes = reason_codes()

    assert {"quote_not_found", "criteria", "not_json", "format", "count"} <= codes  # the scan found them
    assert [code for code in sorted(codes) if hint_for(f"invalid_reply:{code}") is None] == []


@pytest.mark.parametrize(
    "code",
    ["empty_reply", "no_time", "retry_skipped:no_time", "context_too_large"]
    + [cls.__name__ for cls in vars(provider).values() if isinstance(cls, type) and issubclass(cls, provider.LLMError)],
)
def test_every_other_failure_has_a_hint(code):
    assert hint_for(code)


def test_a_rate_limit_hint_says_it_is_not_a_quality_problem():
    assert "not a quality problem" in hint_for("LLMRateLimitError")


def test_success_and_unknown_codes_have_no_hint():
    assert hint_for("ok") is None and hint_for(None) is None and hint_for("invalid_reply:never_heard_of_it") is None
