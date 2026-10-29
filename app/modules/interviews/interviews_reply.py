"""The contract for what the interviewer LLM must reply, and the check that enforces it.

Model output is untrusted: it is parsed and validated here before anything uses it. A reply that fails
raises InvalidReplyError with a short machine-readable reason (logged, never shown to users).
"""

import json
import re
from collections.abc import Sequence
from typing import Annotated

from pydantic import BaseModel, ConfigDict, StringConstraints, ValidationError

from .interviews_constants import MAX_QUESTION_LENGTH, InterviewType, QuestionCategory

# One optional ```json fence around the whole reply; anything before or after it makes the reply invalid.
_FENCE = re.compile(r"^```(?:json)?\s*(.*?)\s*```$", re.DOTALL)
_QUESTION_MARKS = ("?", "？")


class InvalidReplyError(Exception):
    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


class InterviewerReply(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=MAX_QUESTION_LENGTH)]
    category: QuestionCategory


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
        reply = InterviewerReply.model_validate(data)
    except ValidationError as exc:
        raise InvalidReplyError("schema") from exc

    if sum(reply.question.count(mark) for mark in _QUESTION_MARKS) > 1:
        raise InvalidReplyError("multiple_questions")
    if interview_type != InterviewType.mixed and reply.category != QuestionCategory(interview_type):
        raise InvalidReplyError("category")
    if _normalized(reply.question) in {_normalized(q) for q in earlier_questions}:
        raise InvalidReplyError("repeat")
    return reply


def _normalized(question: str) -> str:
    return " ".join(question.casefold().split())
