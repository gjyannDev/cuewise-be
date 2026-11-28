"""One answer turn of the LLM interviewer: decide (follow up or move on), apply the code's limits, write the question.

The model suggests and the code enforces: the follow-up cap, the time checks and a follow-up's category live in code
(interviews_turn_limits.py), not in a prompt, so no reply (or injected answer) can change them. One deadline is shared
by every call of the turn; the decide call is capped and leaves the write call a reserve, because the question is what
the candidate sees. A failure that leaves no question (a failed decide, a failed or unusable write, no time left) ends
the turn with `InterviewerFailedError`: nothing replaces the question, and the answer service saves nothing and
answers with a retryable error.

This file only orchestrates; each step lives in its own file: interviews_decide.py, interviews_write.py (blocking),
interviews_write_stream.py (streamed), interviews_turn_limits.py, interviews_turn_types.py and interviews_turn_log.py.
"""

import uuid
from collections.abc import AsyncGenerator, Callable
from contextlib import aclosing

import anyio

from app.core.ai.chat import ChatModel
from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMResult

from ..ai.interviews_context import InterviewerInputs
from ..ai.interviews_decide import decide
from ..ai.interviews_reply import Decision
from ..ai.interviews_turn_limits import Deadline, fail_undecided, plan_write, settle
from ..ai.interviews_turn_types import (
    ActionKnown,
    InterviewerFailedError,
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
        chat_model: ChatModel,
        context: ContextManager,
        *,
        max_tokens: int,
        budget_seconds: float,
        clock: Callable[[], float],
    ):
        # Every call of the turn (decide, the blocking and the streamed write) runs on the LangChain chat model (U3b1).
        self.chat_model = chat_model
        self.context = context
        self.max_tokens = max_tokens
        self.budget_seconds = budget_seconds
        self.clock = clock

    def first_question(
        self, session_id: uuid.UUID, inputs: InterviewerInputs
    ) -> Written:
        """The interview's first question; raises `InterviewerFailedError` when none could be written."""
        written = self._write(
            session_id,
            inputs,
            Deadline(self.clock, self.budget_seconds),
            follow_up_category=None,
        )
        if written.reply is None:
            raise InterviewerFailedError("write_failed")
        return written

    def answer_turn(
        self, session_id: uuid.UUID, inputs: InterviewerInputs, *, last_main: bool
    ) -> TurnOutcome:
        deadline = Deadline(self.clock, self.budget_seconds)
        decision, decide_results, decision_version = self._decide(
            session_id, inputs, deadline
        )
        if decision is None:
            fail_undecided(deadline, budget_seconds=self.budget_seconds)
        plan = self.plan_write(decision, inputs, deadline, last_main=last_main)
        written = None
        if plan.write_inputs is not None:
            written = self._write(
                session_id, plan.write_inputs, deadline, follow_up_category=plan.follow_up_category
            )
        return self.settle(
            session_id, plan, decision, decide_results, decision_version, written, deadline
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
        if decision is None:
            fail_undecided(deadline, budget_seconds=self.budget_seconds)
        plan = self.plan_write(decision, inputs, deadline, last_main=last_main)
        if plan.action != TurnAction.follow_up:
            yield ActionKnown(plan.action)
        written = None
        if plan.write_inputs is not None:
            yield PhaseChanged(TurnPhase.writing)
            write_events = stream_write(
                self.chat_model,
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
            session_id, plan, decision, decide_results, decision_version, written, deadline
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
    ) -> TurnOutcome:
        return settle(
            session_id,
            plan,
            decision,
            decide_results,
            decision_version,
            written,
            deadline,
            budget_seconds=self.budget_seconds,
        )

    def _decide(
        self, session_id: uuid.UUID, inputs: InterviewerInputs, deadline: Deadline
    ) -> tuple[Decision | None, list[LLMResult], str | None]:
        return decide(
            self.chat_model, self.context, session_id, inputs, deadline, max_tokens=self.max_tokens, clock=self.clock
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
            self.chat_model,
            self.context,
            session_id,
            inputs,
            deadline,
            follow_up_category=follow_up_category,
            max_tokens=self.max_tokens,
        )
