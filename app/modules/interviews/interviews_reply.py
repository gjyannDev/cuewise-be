"""The contract for what the interviewer LLM must reply, and the check that enforces it.

Model output is untrusted: it is parsed and validated here before anything uses it. A reply that fails
raises InvalidReplyError with a short machine-readable reason (logged, never shown to users).
"""

import json
import re
from collections.abc import Sequence
from typing import Annotated, NamedTuple

from pydantic import BaseModel, ConfigDict, StringConstraints, ValidationError

from .interviews_constants import (
    MAX_QUESTION_LENGTH,
    NOTE_MAX_LENGTH,
    SUMMARY_MAX_LENGTH,
    InterviewType,
    QuestionCategory,
)
from .interviews_utils import APP_TAG

# One optional ```json fence around the whole reply; anything before or after it makes the reply invalid.
_FENCE = re.compile(r"^```(?:json)?\s*(.*?)\s*```$", re.DOTALL)
_QUESTION_MARKS = ("?", "？")


class InvalidReplyError(Exception):
    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


class _RawReply(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=MAX_QUESTION_LENGTH)]
    category: QuestionCategory
    # Checked separately: a bad note is dropped, it never costs a usable question.
    note: object = None


class InterviewerReply(NamedTuple):
    question: str
    category: QuestionCategory
    note: str | None = None
    # Why a note that was present got dropped (logged); None when it was fine or absent.
    note_dropped: str | None = None


def parse_interviewer_reply(
    raw: str, *, interview_type: InterviewType, earlier_questions: Sequence[str]
) -> InterviewerReply:
    text = raw.strip()
    if text.startswith("```"):
        fenced = _FENCE.match(text)
        if fenced is None:
            raise InvalidReplyError("fence")
        text = fenced.group(1)

    try:
        data = json.loads(text)
    except ValueError as exc:
        raise InvalidReplyError("not_json") from exc
    if not isinstance(data, dict):
        raise InvalidReplyError("not_object")

    try:
        reply = _RawReply.model_validate(data)
    except ValidationError as exc:
        raise InvalidReplyError("schema") from exc

    if sum(reply.question.count(mark) for mark in _QUESTION_MARKS) > 1:
        raise InvalidReplyError("multiple_questions")
    if interview_type != InterviewType.mixed and reply.category != QuestionCategory(interview_type):
        raise InvalidReplyError("category")
    if _normalized(reply.question) in {_normalized(q) for q in earlier_questions}:
        raise InvalidReplyError("repeat")

    if reply.note is None:
        return InterviewerReply(reply.question, reply.category)
    try:
        return InterviewerReply(reply.question, reply.category, note=validate_note(reply.note))
    except InvalidReplyError as exc:
        return InterviewerReply(reply.question, reply.category, note_dropped=exc.reason)


def _normalized(question: str) -> str:
    return " ".join(question.casefold().split())


def validate_note(value: object) -> str:
    """A running note is optional model output about the latest answer; it is sent again on later calls."""
    if not isinstance(value, str):
        raise InvalidReplyError("not_text")
    note = value.strip()
    if not note:
        raise InvalidReplyError("empty")
    if len(note) > NOTE_MAX_LENGTH:
        raise InvalidReplyError("too_long")
    if APP_TAG.search(note):
        raise InvalidReplyError("markup")
    return note


def validate_summary(original: str, text: str) -> str:
    """The job-description summary replaces the original on every later call, so it must be a real condensation."""
    summary = text.strip()
    if not summary:
        raise InvalidReplyError("empty")
    if len(summary) >= len(original.strip()):
        raise InvalidReplyError("not_shorter")
    if len(summary) > SUMMARY_MAX_LENGTH:
        raise InvalidReplyError("too_long")
    if APP_TAG.search(summary) or "```" in summary:
        raise InvalidReplyError("markup")
    return summary
