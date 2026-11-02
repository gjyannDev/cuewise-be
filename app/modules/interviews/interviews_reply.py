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
    FollowUpAction,
    FollowUpGap,
    InterviewType,
    QuestionCategory,
)
from .interviews_utils import APP_TAG

# One optional ```json fence around the whole reply; anything before or after it makes the reply invalid.
_FENCE = re.compile(r"^```(?:json)?\s*(.*?)\s*```$", re.DOTALL)
_QUESTION_MARKS = ("?", "？")
# interviewer_v5's first line in next-question mode. "CATEGORY: behavioral" is 20 characters; a longer first line
# with no newline yet is question text, not a header.
_HEADER = re.compile(r"^\s*category\s*:\s*(\w+)\s*$", re.IGNORECASE)
_HEADER_MAX_LENGTH = 32


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


class _RawFollowUp(BaseModel):
    """A follow-up carries no category: it inherits its main question's, so the model can't break the category rule."""

    model_config = ConfigDict(extra="forbid")

    question: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=MAX_QUESTION_LENGTH)]
    note: object = None


class InterviewerReply(NamedTuple):
    question: str
    category: QuestionCategory
    note: str | None = None
    # Why a note that was present got dropped (logged); None when it was fine or absent.
    note_dropped: str | None = None


def parse_interviewer_reply(
    raw: str,
    *,
    interview_type: InterviewType,
    earlier_questions: Sequence[str],
    # Set = follow-up mode: the reply is the question only and gets this category (the main question's).
    follow_up_category: QuestionCategory | None = None,
) -> InterviewerReply:
    data = _load_object(raw)

    try:
        if follow_up_category is None:
            reply = _RawReply.model_validate(data)
            category = reply.category
        else:
            reply = _RawFollowUp.model_validate(data)
            category = follow_up_category
    except ValidationError as exc:
        raise InvalidReplyError("schema") from exc

    _check_question(reply.question, category, interview_type, earlier_questions)

    if reply.note is None:
        return InterviewerReply(reply.question, category)
    try:
        return InterviewerReply(reply.question, category, note=validate_note(reply.note))
    except InvalidReplyError as exc:
        return InterviewerReply(reply.question, category, note_dropped=exc.reason)


class HeaderSplit(NamedTuple):
    category: QuestionCategory
    # The question text after the header line, so far.
    text: str


def split_header(buffer: str, *, final: bool = False) -> HeaderSplit | None:
    """interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read before any text is shown.

    `buffer` is every chunk so far. None while the line isn't complete; `final` = the reply ended, so its end ends the
    line. Raises InvalidReplyError("header") as soon as the first line can't be a header, so no text of a reply
    without one is ever streamed.
    """
    end = buffer.find("\n")
    if end < 0 and not final:
        if len(buffer.lstrip()) > _HEADER_MAX_LENGTH:
            raise InvalidReplyError("header")
        return None
    line, rest = (buffer, "") if end < 0 else (buffer[:end], buffer[end + 1 :])
    match = _HEADER.match(line)
    if match is None or match.group(1).lower() not in set(QuestionCategory):
        raise InvalidReplyError("header")
    return HeaderSplit(QuestionCategory(match.group(1).lower()), rest.lstrip())


def parse_streamed_reply(
    text: str,
    *,
    interview_type: InterviewType,
    earlier_questions: Sequence[str],
    # From the header (next-question mode) or the main question's (a follow-up inherits it).
    category: QuestionCategory,
) -> InterviewerReply:
    """interviewer_v5's finished question text, checked like a v4 reply. It was already shown while it streamed, so a
    reply that fails here is taken back (a `reset` event) by the caller."""
    question = text.strip()
    if question.startswith(("{", "```")):
        raise InvalidReplyError("not_text")
    if not question or len(question) > MAX_QUESTION_LENGTH:
        raise InvalidReplyError("schema")
    _check_question(question, category, interview_type, earlier_questions)
    return InterviewerReply(question, category)


def _check_question(
    question: str, category: QuestionCategory, interview_type: InterviewType, earlier_questions: Sequence[str]
) -> None:
    """The rules every written question must pass, whatever format it came in."""
    if sum(question.count(mark) for mark in _QUESTION_MARKS) > 1:
        raise InvalidReplyError("multiple_questions")
    if interview_type != InterviewType.mixed and category != QuestionCategory(interview_type):
        raise InvalidReplyError("category")
    if _normalized(question) in {_normalized(q) for q in earlier_questions}:
        raise InvalidReplyError("repeat")


def _normalized(question: str) -> str:
    return " ".join(question.casefold().split())


def _load_object(raw: str) -> dict:
    """The reply as a JSON object: one optional fence around it, nothing else before or after."""
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
    return data


class _RawDecision(BaseModel):
    model_config = ConfigDict(extra="forbid")

    action: FollowUpAction
    gap: FollowUpGap | None = None
    note: object = None


class Decision(NamedTuple):
    action: FollowUpAction
    gap: FollowUpGap | None = None
    note: str | None = None
    note_dropped: str | None = None


def parse_decision_reply(raw: str) -> Decision:
    """The decide call suggests; the code still applies the follow-up cap and the time check afterwards."""
    try:
        reply = _RawDecision.model_validate(_load_object(raw))
    except ValidationError as exc:
        raise InvalidReplyError("schema") from exc
    if reply.action == FollowUpAction.follow_up and reply.gap is None:
        raise InvalidReplyError("missing_gap")
    if reply.action == FollowUpAction.next_question and reply.gap is not None:
        raise InvalidReplyError("unexpected_gap")

    if reply.note is None:
        return Decision(reply.action, reply.gap)
    try:
        return Decision(reply.action, reply.gap, note=validate_note(reply.note))
    except InvalidReplyError as exc:
        return Decision(reply.action, reply.gap, note_dropped=exc.reason)


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
