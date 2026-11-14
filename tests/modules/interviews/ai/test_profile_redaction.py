"""resume-aware-interview Step 5: a write whose prompt carries the profile is labelled `redact` (AC10).

The calls go through the real tracing wrapper with a fake Langfuse client, so the test sees what Langfuse would get:
no prompt or reply text for a profile-carrying call, but its task, prompt version and usage still recorded.
"""

import json
import uuid
from contextlib import nullcontext

import pytest

from app.core.ai.fake import FakeProvider
from app.core.ai.tracing import REDACT_LABEL, REDACTED, Tracer, TracingProvider
from app.modules.interviews.ai.interviews_context import (
    CONTEXT_MANAGER,
    InterviewerInputs,
)
from app.modules.interviews.ai.interviews_turn_limits import Deadline
from app.modules.interviews.ai.interviews_turn_types import Written
from app.modules.interviews.ai.interviews_write import write
from app.modules.interviews.ai.interviews_write_stream import stream_write
from app.modules.interviews.constants.interviews_constants import (
    INTERVIEWER_V4_PROMPT_VERSION,
    INTERVIEWER_V5_PROMPT_VERSION,
    INTERVIEWER_V8_JSON_PROMPT_VERSION,
    INTERVIEWER_V8_PROMPT_VERSION,
    FollowUpAction,
    FollowUpGap,
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
)
from app.modules.interviews.utils.interviews_utils import QuestionTurn
from app.modules.profile.schemas.profile_schema import CandidateProfile, Role
from tests.fake_langfuse import FakeLangfuse

PROFILE = CandidateProfile(skills=["ZZSKILL-Kafka"], roles=[Role(title="Engineer", summary="ZZSUMMARY ledger work.")])
QUESTION = "How would you make a payment retry safe to repeat?"


def inputs(**overrides) -> InterviewerInputs:
    values = {
        "role": JobRole.backend,
        "level": Level.mid,
        "interview_type": InterviewType.technical,
        "question_count": 5,
        "job_description": "Payments APIs in Python.",
        "turns": [QuestionTurn("Question 1 about queues?", "technical", "Answer 1 text.")],
    }
    return InterviewerInputs(**(values | overrides))


def traced(reply: str) -> tuple[TracingProvider, FakeLangfuse]:
    langfuse = FakeLangfuse()
    tracer = Tracer(langfuse, propagate=lambda **_: nullcontext())
    return TracingProvider(FakeProvider(default=reply), tracer), langfuse


def generations(langfuse: FakeLangfuse) -> list[dict]:
    return [o for o in langfuse.observations if o.get("as_type") == "generation"]


def run_write(data: InterviewerInputs) -> tuple[Written, dict]:
    reply = {"question": QUESTION} if data.mode == FollowUpAction.follow_up else {"question": QUESTION, "category": "technical"}
    provider, langfuse = traced(json.dumps(reply))
    clock = lambda: 0.0
    category = QuestionCategory.technical if data.mode == FollowUpAction.follow_up else None
    written = write(
        provider,
        CONTEXT_MANAGER,
        uuid.uuid7(),
        data,
        Deadline(clock, 30),
        follow_up_category=category,
        max_tokens=200,
    )
    [generation] = generations(langfuse)
    return written, generation


async def run_stream_write(data: InterviewerInputs) -> tuple[Written, dict]:
    provider, langfuse = traced(f"CATEGORY: technical\n{QUESTION}")
    clock = lambda: 0.0
    category = QuestionCategory.technical if data.mode == FollowUpAction.follow_up else None
    items = [
        item
        async for item in stream_write(
            provider,
            CONTEXT_MANAGER,
            uuid.uuid7(),
            data,
            Deadline(clock, 30),
            follow_up_category=category,
            max_tokens=200,
            clock=clock,
        )
    ]
    [generation] = generations(langfuse)
    return items[-1], generation


def assert_redacted(generation: dict, version: str) -> None:
    assert generation["input"] == REDACTED and generation["output"] == REDACTED
    assert generation["metadata"][REDACT_LABEL] is True
    assert generation["metadata"]["prompt_version"] == version
    assert "ZZ" not in repr(generation) and QUESTION not in repr(generation)


def assert_traced_in_full(generation: dict) -> None:
    assert generation["input"] != REDACTED and generation["output"] != REDACTED
    assert REDACT_LABEL not in generation["metadata"]


def test_a_main_write_with_the_profile_is_redacted_but_keeps_its_metadata():  # AC10
    written, generation = run_write(inputs(candidate_profile=PROFILE))

    assert written.reply is not None and written.reply.question == QUESTION
    assert_redacted(generation, INTERVIEWER_V8_JSON_PROMPT_VERSION)
    assert generation.get("usage_details") or generation.get("usage")  # tokens still recorded


def test_a_main_write_without_the_profile_is_traced_as_today():  # AC10, EC2
    _, generation = run_write(inputs())

    assert_traced_in_full(generation)
    assert generation["metadata"]["prompt_version"] == INTERVIEWER_V4_PROMPT_VERSION


def test_a_follow_up_write_of_a_profile_interview_is_not_redacted():  # AC6: no profile in it, nothing to hide
    _, generation = run_write(
        inputs(candidate_profile=PROFILE, mode=FollowUpAction.follow_up, gap=FollowUpGap.no_example)
    )

    assert_traced_in_full(generation)


@pytest.mark.anyio
async def test_a_streamed_main_write_with_the_profile_is_redacted():  # AC10
    written, generation = await run_stream_write(inputs(candidate_profile=PROFILE))

    assert written.reply is not None
    assert_redacted(generation, INTERVIEWER_V8_PROMPT_VERSION)


@pytest.mark.anyio
async def test_a_streamed_main_write_without_the_profile_is_traced_as_today():  # AC10, EC2
    _, generation = await run_stream_write(inputs())

    assert_traced_in_full(generation)
    assert generation["metadata"]["prompt_version"] == INTERVIEWER_V5_PROMPT_VERSION
