"""`extract_profile` on the LangChain layer: structured output inside the existing attempt loop (U3a spec FR9, AC7,
AC8, EC8-EC12, EC14). The fake chat model; no network. The upload route's HTTP behavior is in
tests/modules/profile/routes/test_profile_routes.py."""

import json

import pytest
from google.api_core import exceptions as gx

from app.core.ai.chat_fake import FakeChatModel, fake_reply
from app.core.ai.chat_tracing import TracerHandle
from app.core.ai.tracing import REDACTED, Tracer
from app.core.config import settings
from app.modules.profile.ai.profile_extract import (
    ExtractionFailedError,
    extract_profile,
)
from app.modules.profile.ai.profile_reply import EmptyProfileError
from app.modules.profile.constants.profile_constants import (
    MAX_SKILLS,
    PROFILE_PROMPT_VERSION,
    PROFILE_TASK,
    PROFILE_TEMPERATURE,
    PROFILE_TOTAL_SECONDS,
)
from tests.core.ai.test_retry import Clock
from tests.core.ai.test_tracing import FakeClient
from tests.modules.profile.profile_fixtures import RESUME_LINES, profile_json

TEXT = "\n".join(RESUME_LINES[1:])  # the scrubbed résumé (no contact line)


@pytest.fixture(autouse=True)
def no_retry_waits(monkeypatch):
    # Transport retries are RetryPolicy's (tests/core/ai); here one transport error ends the extraction at once.
    monkeypatch.setattr(settings, "llm_max_retries", 0)


def extract(model, clock=None):
    return extract_profile(model, TEXT, max_tokens=4000, clock=clock or Clock())


def test_a_valid_first_reply_is_the_profile_after_one_call():
    model = FakeChatModel([fake_reply(profile_json(), input_tokens=900, output_tokens=200)])
    extraction = extract(model)

    assert extraction.profile.skills[0] == "Python" and len(model.calls) == 1
    assert extraction.results[0].prompt_tokens == 900
    [(messages, kwargs)] = model.calls
    assert str(messages[1].content).startswith("<resume>\n")  # fenced as data, after the system prompt
    assert kwargs["temperature"] == PROFILE_TEMPERATURE and kwargs["timeout"] <= PROFILE_TOTAL_SECONDS


def test_an_invalid_then_a_valid_reply_is_the_profile_after_two_calls():  # EC8
    model = FakeChatModel(["Sure! Here is the profile:", profile_json()])
    extraction = extract(model)
    assert len(model.calls) == 2 and len(extraction.results) == 2


@pytest.mark.parametrize(
    ("replies", "reason"),
    [
        (["nope", "nope"], "invalid_reply:schema"),
        (['{"skills": "Python"}', '{"name": "Ana"}'], "invalid_reply:schema"),
        (["", ""], "empty_reply"),
    ],
    ids=["not-json", "off-schema", "empty"],
)
def test_two_invalid_replies_fail_the_extraction_with_the_last_reason(replies, reason):  # EC9
    model = FakeChatModel(replies)
    with pytest.raises(ExtractionFailedError) as info:
        extract(model)
    assert info.value.reason == reason and len(model.calls) == 2


def test_a_valid_reply_with_no_skills_and_no_roles_is_an_empty_profile_and_not_retried():  # EC10
    model = FakeChatModel([profile_json(skills=[], roles=[], projects=[]), profile_json()])
    with pytest.raises(EmptyProfileError):
        extract(model)
    assert len(model.calls) == 1


@pytest.mark.parametrize(
    ("error", "reason"),
    [(gx.DeadlineExceeded("slow"), "LLMTimeoutError"), (gx.ServiceUnavailable("down"), "LLMServerError")],
)
def test_a_transport_error_fails_the_extraction_named_after_our_error(error, reason):  # EC11
    model = FakeChatModel([error, profile_json()])
    with pytest.raises(ExtractionFailedError) as info:
        extract(model)
    assert info.value.reason == reason and len(model.calls) == 1


def test_over_cap_and_duplicate_fields_are_trimmed_and_merged():  # EC12
    skills = ["Python", "python", "PYTHON", "Redis"] + [f"Skill {i}" for i in range(60)]
    model = FakeChatModel([profile_json(skills=skills)])
    profile = extract(model).profile
    assert profile.skills[:2] == ["Python", "Redis"] and len(profile.skills) == MAX_SKILLS


def test_a_fenced_json_reply_is_read():  # Gemini sometimes wraps JSON in a code fence
    model = FakeChatModel([f"```json\n{profile_json()}\n```"])
    assert extract(model).profile.skills[0] == "Python"


def test_the_trace_is_redacted_but_keeps_usage_and_labels():  # EC14, AC8
    client = FakeClient()
    model = FakeChatModel([fake_reply(profile_json(), input_tokens=900, output_tokens=200)])
    model.callbacks = [TracerHandle(Tracer(client))]

    extract(model)

    [generation] = client.generations
    assert generation.kwargs["input"] == REDACTED and generation.final["output"] == REDACTED
    assert generation.kwargs["name"] == PROFILE_TASK
    assert generation.final["metadata"]["prompt_version"] == PROFILE_PROMPT_VERSION
    assert generation.final["usage_details"]["input"] == 900
    dumped = json.dumps(generation.final, default=str) + json.dumps(generation.kwargs, default=str)
    assert "Acme" not in dumped and "Python" not in dumped


def test_no_time_left_sends_nothing():
    model = FakeChatModel([profile_json()])

    class Late(Clock):
        def __call__(self) -> float:  # the budget is spent before the first attempt
            self.now += PROFILE_TOTAL_SECONDS + 1
            return self.now

    with pytest.raises(ExtractionFailedError) as info:
        extract(model, Late())
    assert info.value.reason == "no_time" and model.calls == []


def test_the_schema_given_to_the_model_requires_every_field():
    # Regression (U3a comparison eval): with defaults nothing was required, and Gemini left roles out and padded skills.
    from app.modules.profile.ai.profile_reply import ModelProfile

    schema = ModelProfile.model_json_schema()
    assert schema["required"] == ["skills", "roles", "projects"]
    assert schema["$defs"]["ModelRole"]["required"] == ["title", "organization", "period", "summary"]
    assert schema["$defs"]["ModelProject"]["required"] == ["name", "description", "technologies"]
