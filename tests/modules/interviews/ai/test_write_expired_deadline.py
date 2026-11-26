"""U2 EC17: with the turn's time already used up, write and write-stream make no LLM call and hand back no reply.

Before U2 these two loops always made their first call, even at zero time left (with a timeout of zero or less).
The shared `ReplyAttempts` header now stops before it, like decide and the feedback turn already did, and the turn
falls back to the question bank.
"""

import json
import uuid

import pytest

from app.core.ai.fake import FakeProvider
from app.modules.interviews.ai.interviews_context import (
    CONTEXT_MANAGER,
    InterviewerInputs,
)
from app.modules.interviews.ai.interviews_turn_limits import Deadline
from app.modules.interviews.ai.interviews_turn_types import Written
from app.modules.interviews.ai.interviews_write import write
from app.modules.interviews.ai.interviews_write_stream import stream_write
from app.modules.interviews.constants.interviews_constants import (
    InterviewType,
    JobRole,
    Level,
)
from app.modules.interviews.utils.interviews_utils import QuestionTurn

QUESTION = "How would you make a payment retry safe to repeat?"


def inputs() -> InterviewerInputs:
    return InterviewerInputs(
        role=JobRole.backend,
        level=Level.mid,
        interview_type=InterviewType.technical,
        question_count=5,
        job_description=None,
        turns=[QuestionTurn("Question 1 about queues?", "technical", "Answer 1 text.")],
    )


def expired() -> Deadline:
    return Deadline(lambda: 0.0, 0)  # no time left from the start


def test_write_makes_no_call_once_the_deadline_has_passed():
    llm = FakeProvider(default=json.dumps({"question": QUESTION, "category": "technical"}))

    written = write(llm, CONTEXT_MANAGER, uuid.uuid7(), inputs(), expired(), follow_up_category=None, max_tokens=200)

    assert llm.calls == []
    assert written.reply is None and written.results == []


@pytest.mark.anyio
async def test_stream_write_makes_no_call_once_the_deadline_has_passed():
    llm = FakeProvider(default=f"CATEGORY: technical\n{QUESTION}")

    items = [
        item
        async for item in stream_write(
            llm,
            CONTEXT_MANAGER,
            uuid.uuid7(),
            inputs(),
            expired(),
            follow_up_category=None,
            max_tokens=200,
            clock=lambda: 0.0,
        )
    ]

    assert llm.calls == []
    assert items == [Written(None, [], items[-1].prompt_version)]
