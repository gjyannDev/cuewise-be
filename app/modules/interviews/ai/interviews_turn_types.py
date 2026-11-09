"""What one answer turn of the LLM interviewer hands around: its action, its results, its plan and its stream events."""

from enum import StrEnum
from typing import NamedTuple

from app.core.ai.provider import LLMResult

from ..ai.interviews_context import InterviewerInputs
from ..ai.interviews_reply import InterviewerReply
from ..constants.interviews_constants import QuestionCategory, TurnPhase


class TurnAction(StrEnum):
    """What the turn ends with, after the limits: the model can only ask for the first two."""

    follow_up = "follow_up"
    next_question = "next_question"
    complete = "complete"


class Written(NamedTuple):
    reply: InterviewerReply | None
    # Every attempt that came back, valid or not (their usage is summed onto the stored question).
    results: list[LLMResult]
    prompt_version: str | None


class TurnOutcome(NamedTuple):
    action: TurnAction
    # None: the bank asks the next main question (or nothing, when the turn completes the interview).
    written: Written | None
    note: str | None
    # Every call of the turn, decide and write.
    results: list[LLMResult]
    decision_prompt_version: str | None


class WritePlan(NamedTuple):
    """What the turn does after the decision, before the write call: shared by the JSON and the streamed turn."""

    action: TurnAction
    # Why the code overrode the model's decision (cap_reached, no_time), or None.
    override: str | None
    # "no_time" when no write call is started; the write's own failure is added later by `settle`.
    fallback: str | None
    # The write call's inputs; None when no write call runs (the turn completes, or there is no time).
    write_inputs: InterviewerInputs | None
    # A follow-up inherits its main question's category; None in next-question mode.
    follow_up_category: QuestionCategory | None


# --- What a streamed turn yields (Interviewer.stream_turn), in order: deciding, [writing], the action, the outcome ---


class PhaseChanged(NamedTuple):
    phase: TurnPhase


class ActionKnown(NamedTuple):
    """The turn's final action, sent only once nothing can change it (a follow-up only after its write succeeded)."""

    action: TurnAction


class Settled(NamedTuple):
    outcome: TurnOutcome


class Delta(NamedTuple):
    """The next chunk of the question being written (shown as it arrives)."""

    text: str


class Reset(NamedTuple):
    """The question text streamed so far is taken back: that draft failed, another one (or the bank's) follows."""


TurnEvent = PhaseChanged | ActionKnown | Delta | Reset | Settled


class Draft(NamedTuple):
    """One streamed write attempt, finished: the category (from its CATEGORY line, or a follow-up's inherited one),
    the question text without that line, and the call's result."""

    category: QuestionCategory
    text: str
    result: LLMResult
