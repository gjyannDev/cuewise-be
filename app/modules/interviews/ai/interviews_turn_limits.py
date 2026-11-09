"""The code's say over an answer turn: the shared deadline, the follow-up cap and time checks, and the outcome.

The model suggests and the code enforces, so no reply (or injected answer) can change these rules.
"""

import uuid
from collections.abc import Callable

from app.core.ai.provider import LLMResult

from ..ai.interviews_context import InterviewerInputs
from ..ai.interviews_reply import Decision
from ..ai.interviews_turn_log import log_turn_summary
from ..ai.interviews_turn_types import TurnAction, TurnOutcome, WritePlan, Written
from ..constants.interviews_constants import (
    MAX_FOLLOW_UPS,
    MIN_SECONDS_FOR_WRITE,
    FollowUpAction,
    QuestionCategory,
)
from ..utils.interviews_utils import thread_start


class Deadline:
    """The turn's LLM time budget, set once and asked by every call (an injectable clock, so tests control time)."""

    def __init__(self, clock: Callable[[], float], seconds: float):
        self.clock = clock
        self.end = clock() + seconds

    def remaining(self) -> float:
        return self.end - self.clock()


def apply_limits(
    decision: Decision | None,
    follow_ups_left: int,
    seconds_left: float,
    *,
    last_main: bool,
) -> tuple[TurnAction, str | None]:
    """The code's say over the model's: returns the action and why it overrode the decision (None if it didn't)."""
    wanted, override = (
        (decision.action if decision else FollowUpAction.next_question),
        None,
    )
    if wanted == FollowUpAction.follow_up and follow_ups_left <= 0:
        wanted, override = FollowUpAction.next_question, "cap_reached"
    elif wanted == FollowUpAction.follow_up and seconds_left < MIN_SECONDS_FOR_WRITE:
        wanted, override = FollowUpAction.next_question, "no_time"
    if wanted == FollowUpAction.next_question and last_main:
        return TurnAction.complete, override
    return TurnAction(wanted), override


def plan_write(
    decision: Decision | None, inputs: InterviewerInputs, deadline: Deadline, *, last_main: bool
) -> WritePlan:
    """After the decision: the code's limits pick the action, and whether a write call runs, with which inputs."""
    start = thread_start(inputs.turns)
    follow_ups_left = MAX_FOLLOW_UPS - (len(inputs.turns) - 1 - start)
    action, override = apply_limits(
        decision, follow_ups_left, deadline.remaining(), last_main=last_main
    )
    if action == TurnAction.complete:
        return WritePlan(action, override, None, None, None)
    if deadline.remaining() < MIN_SECONDS_FOR_WRITE:
        return WritePlan(action, override, "no_time", None, None)
    following_up = action == TurnAction.follow_up
    write_inputs = inputs._replace(
        mode=FollowUpAction(action),
        gap=decision.gap if following_up and decision else None,
    )
    category = QuestionCategory(inputs.turns[start].category) if following_up else None
    return WritePlan(action, override, None, write_inputs, category)


def settle(
    session_id: uuid.UUID,
    plan: WritePlan,
    decision: Decision | None,
    decide_results: list[LLMResult],
    decision_version: str | None,
    written: Written | None,
    deadline: Deadline,
    *,
    last_main: bool,
    budget_seconds: float,
) -> TurnOutcome:
    """The write's result decides the outcome: a failed follow-up moves on, and the turn's summary line is logged.
    `budget_seconds` is the turn's whole budget, so the summary can say how much of it the LLM calls used."""
    action, fallback = plan.action, plan.fallback
    if written is not None and written.reply is None:
        fallback = "write_failed"
    if fallback and action == TurnAction.follow_up:
        # No follow-up after all: move on as if the model had said so.
        action = TurnAction.complete if last_main else TurnAction.next_question

    results = decide_results + (written.results if written else [])
    source = (
        "-" if action == TurnAction.complete else ("bank" if fallback else "llm")
    )
    log_turn_summary(
        session_id,
        decision="none" if decision is None else _decision_label(decision),
        action=action,
        override=plan.override,
        source=source,
        fallback=fallback,
        llm_ms=round((budget_seconds - deadline.remaining()) * 1000),
    )
    note = decision.note if decision else None
    if note is None and written and written.reply:
        note = (
            written.reply.note
        )  # older prompts (v3 ablations) still write the note themselves
    return TurnOutcome(
        action,
        written if fallback is None else None,
        note,
        results,
        decision_version,
    )


def _decision_label(decision: Decision) -> str:
    return f"{decision.action}:{decision.gap}" if decision.gap else str(decision.action)
