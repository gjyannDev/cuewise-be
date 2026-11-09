"""One answer turn of the LLM interviewer: decide (follow up or move on), apply the code's limits, write the question.

The model suggests and the code enforces: the follow-up cap, the time checks and a follow-up's category live in code
(interviews_turn_limits.py), not in a prompt, so no reply (or injected answer) can change them. One deadline is shared
by every call of the turn; the decide call is capped and leaves the write call a reserve, because the question is what
the candidate sees. Every failure has a fallback, so a turn never fails because of the LLM: the answer service asks the
bank instead.

This file only orchestrates; each step lives in its own file: interviews_decide.py, interviews_write.py (blocking),
interviews_write_stream.py (streamed), interviews_turn_limits.py, interviews_turn_types.py and interviews_turn_log.py.
"""

import uuid
from collections.abc import AsyncGenerator, Callable
from contextlib import aclosing

import anyio

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMProvider, LLMResult

from ..ai.interviews_context import InterviewerInputs
from ..ai.interviews_decide import decide
from ..ai.interviews_reply import Decision
from ..ai.interviews_turn_limits import Deadline, plan_write, settle
from ..ai.interviews_turn_types import (
    ActionKnown,
    PhaseChanged,
    Settled,
    TurnAction,
    TurnEvent,
    TurnOutcome,
    WritePlan,
    Written,
)
from ..ai.interviews_write import write
from ..ai.interviews_write_stream import stream_write
from ..constants.interviews_constants import QuestionCategory, TurnPhase


class Interviewer:
    def __init__(
        self,
        llm: LLMProvider,
        context: ContextManager,
        *,
        max_tokens: int,
        budget_seconds: float,
        clock: Callable[[], float],
    ):
        self.llm = llm
        self.context = context
        self.max_tokens = max_tokens
        self.budget_seconds = budget_seconds
        self.clock = clock

    def first_question(
        self, session_id: uuid.UUID, inputs: InterviewerInputs
    ) -> Written:
        return self._write(
            session_id,
            inputs,
            Deadline(self.clock, self.budget_seconds),
            follow_up_category=None,
        )

    def answer_turn(
        self, session_id: uuid.UUID, inputs: InterviewerInputs, *, last_main: bool
    ) -> TurnOutcome:
        deadline = Deadline(self.clock, self.budget_seconds)
        decision, decide_results, decision_version = self._decide(
            session_id, inputs, deadline
        )
        plan = self.plan_write(decision, inputs, deadline, last_main=last_main)
        written = None
        if plan.write_inputs is not None:
            written = self._write(
                session_id, plan.write_inputs, deadline, follow_up_category=plan.follow_up_category
            )
        return self.settle(
            session_id, plan, decision, decide_results, decision_version, written, deadline, last_main=last_main
        )

    async def stream_turn(
        self, session_id: uuid.UUID, inputs: InterviewerInputs, *, last_main: bool
    ) -> AsyncGenerator[TurnEvent]:
        """The same turn as `answer_turn` (same decide, limits and fallbacks), telling the caller what it is doing
        and streaming the question as it is written (interviewer_v5). The decide call is blocking, so it runs in a
        worker thread and the event loop stays free; if the caller stops listening (the client left), it finishes in
        its thread and its result is dropped. The write call streams, and closing this turn cancels it.
        """
        deadline = Deadline(self.clock, self.budget_seconds)
        yield PhaseChanged(TurnPhase.deciding)
        decision, decide_results, decision_version = await anyio.to_thread.run_sync(
            self._decide, session_id, inputs, deadline, abandon_on_cancel=True
        )
        plan = self.plan_write(decision, inputs, deadline, last_main=last_main)
        if plan.action != TurnAction.follow_up:
            yield ActionKnown(plan.action)
        written = None
        if plan.write_inputs is not None:
            yield PhaseChanged(TurnPhase.writing)
            write_events = stream_write(
                self.llm,
                self.context,
                session_id,
                plan.write_inputs,
                deadline,
                follow_up_category=plan.follow_up_category,
                max_tokens=self.max_tokens,
                clock=self.clock,
            )
            async with aclosing(write_events) as events:
                async for event in events:
                    if isinstance(event, Written):
                        written = event
                    else:
                        yield event
        outcome = self.settle(
            session_id, plan, decision, decide_results, decision_version, written, deadline, last_main=last_main
        )
        if plan.action == TurnAction.follow_up:
            yield ActionKnown(outcome.action)
        yield Settled(outcome)

    # Kept as methods, not direct calls to the module functions: tests patch `Interviewer.plan_write` to inject a
    # crash mid-turn (test_answer_stream.py).
    def plan_write(
        self, decision: Decision | None, inputs: InterviewerInputs, deadline: Deadline, *, last_main: bool
    ) -> WritePlan:
        return plan_write(decision, inputs, deadline, last_main=last_main)

    def settle(
        self,
        session_id: uuid.UUID,
        plan: WritePlan,
        decision: Decision | None,
        decide_results: list[LLMResult],
        decision_version: str | None,
        written: Written | None,
        deadline: Deadline,
        *,
        last_main: bool,
    ) -> TurnOutcome:
        return settle(
            session_id,
            plan,
            decision,
            decide_results,
            decision_version,
            written,
            deadline,
            last_main=last_main,
            budget_seconds=self.budget_seconds,
        )

    def _decide(
        self, session_id: uuid.UUID, inputs: InterviewerInputs, deadline: Deadline
    ) -> tuple[Decision | None, list[LLMResult], str | None]:
        return decide(
            self.llm, self.context, session_id, inputs, deadline, max_tokens=self.max_tokens, clock=self.clock
        )

    def _write(
        self,
        session_id: uuid.UUID,
        inputs: InterviewerInputs,
        deadline: Deadline,
        *,
        follow_up_category: QuestionCategory | None,
    ) -> Written:
        return write(
            self.llm,
            self.context,
            session_id,
            inputs,
            deadline,
            follow_up_category=follow_up_category,
            max_tokens=self.max_tokens,
        )
