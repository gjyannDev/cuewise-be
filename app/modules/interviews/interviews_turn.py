"""One answer turn of the LLM interviewer: decide (follow up or move on), apply the code's limits, write the question.

The model suggests and the code enforces: the follow-up cap, the time checks and a follow-up's category live here,
not in a prompt, so no reply (or injected answer) can change them. One deadline is shared by every call of the turn;
the decide call is capped and leaves the write call a reserve, because the question is what the candidate sees.
Every failure has a fallback, so a turn never fails because of the LLM: the controller asks the bank instead.
"""

import logging
import uuid
from collections.abc import AsyncGenerator, Callable, Sequence
from contextlib import aclosing
from enum import StrEnum
from typing import NamedTuple

import anyio

from app.core.ai.context import ContextManager, ContextTooLargeError
from app.core.ai.provider import (
    ChatMessage,
    LLMError,
    LLMProvider,
    LLMResult,
    LLMTimeoutError,
)

from .interviews_constants import (
    DECIDE_MAX_SECONDS,
    DECISION_TASK,
    INTERVIEWER_STREAM_TASK,
    INTERVIEWER_TASK,
    MAX_FOLLOW_UPS,
    MAX_REPLY_ATTEMPTS,
    MIN_SECONDS_FOR_RETRY,
    MIN_SECONDS_FOR_WRITE,
    WRITE_RESERVE_SECONDS,
    FollowUpAction,
    QuestionCategory,
    TurnPhase,
)
from .interviews_context import InterviewerInputs
from .interviews_reply import (
    Decision,
    InterviewerReply,
    InvalidReplyError,
    parse_decision_reply,
    parse_interviewer_reply,
    parse_streamed_reply,
    split_header,
)
from .interviews_utils import thread_start

# One line per LLM call and one per answer turn: metadata only (ids, model, tokens, timing, reason codes), never
# question, answer, note or job-description text.
llm_logger = logging.getLogger("app.llm")


class TurnAction(StrEnum):
    """What the turn ends with, after the limits: the model can only ask for the first two."""

    follow_up = "follow_up"
    next_question = "next_question"
    complete = "complete"


class Deadline:
    """The turn's LLM time budget, set once and asked by every call (an injectable clock, so tests control time)."""

    def __init__(self, clock: Callable[[], float], seconds: float):
        self.clock = clock
        self.end = clock() + seconds

    def remaining(self) -> float:
        return self.end - self.clock()


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
            write = self._stream_write(
                session_id, plan.write_inputs, deadline, follow_up_category=plan.follow_up_category
            )
            async with aclosing(write) as events:
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

    async def _stream_write(
        self,
        session_id: uuid.UUID,
        inputs: InterviewerInputs,
        deadline: Deadline,
        *,
        follow_up_category: QuestionCategory | None,
    ) -> AsyncGenerator[Delta | Reset | Written]:
        """`_write` for interviewer_v5, streamed: question text as Deltas, then the Written (last). The same attempts
        and checks; but a draft was already shown, so one that fails is taken back (Reset) before the retry, and a
        provider failure after some text is retried too (the provider couldn't: it had already sent text).
        """
        try:
            built = self.context.build(INTERVIEWER_STREAM_TASK, inputs)
        except ContextTooLargeError:
            log_llm_call(
                logging.WARNING, session_id, "context_too_large", task=INTERVIEWER_STREAM_TASK, latency_ms=0, attempts=0
            )
            yield Written(None, [], None)
            return
        version = built.prompt_version
        earlier = [turn.question for turn in inputs.turns]
        results: list[LLMResult] = []
        for attempt in range(1, MAX_REPLY_ATTEMPTS + 1):
            remaining = deadline.remaining()
            if attempt > 1 and remaining < MIN_SECONDS_FOR_RETRY:
                break
            budget_left_ms = round(remaining * 1000)
            shown = False
            attempt_start = self.clock()
            finished: Draft | None = None
            try:
                draft = self._stream_draft(built.messages, remaining, deadline, follow_up_category)
                async with aclosing(draft) as chunks:
                    async for item in chunks:
                        if isinstance(item, Draft):
                            finished = item
                        else:
                            shown = True
                            yield Delta(item)
            except LLMError as exc:
                _log_error(session_id, exc, INTERVIEWER_STREAM_TASK, version, budget_left_ms)
                if shown:
                    yield Reset()
                if exc.after_output:
                    continue
                # Before any text, the provider already retried what was worth retrying.
                break
            except InvalidReplyError as exc:
                # A missing or broken CATEGORY line: nothing of it was shown.
                log_llm_call(
                    logging.WARNING,
                    session_id,
                    f"invalid_reply:{exc.reason}",
                    task=INTERVIEWER_STREAM_TASK,
                    prompt_version=version,
                    latency_ms=0,
                    attempts=1,
                    budget_left_ms=budget_left_ms,
                )
                continue
            except BaseException as exc:
                if isinstance(exc, Exception):
                    raise
                # The client left mid-call (closed or cancelled): the call stops, so no more tokens are generated. Its
                # usage is unknown (it comes at the end of a stream), so the line records that it was cut off.
                log_llm_call(
                    logging.INFO,
                    session_id,
                    "cancelled",
                    task=INTERVIEWER_STREAM_TASK,
                    prompt_version=version,
                    latency_ms=round((self.clock() - attempt_start) * 1000),
                    attempts=attempt,
                    budget_left_ms=budget_left_ms,
                )
                raise
            # `_stream_draft` ends with its Draft unless it raised, and every raise above leaves the attempt.
            assert finished is not None
            result = finished.result
            results.append(result)
            try:
                reply = parse_streamed_reply(
                    finished.text,
                    interview_type=inputs.interview_type,
                    earlier_questions=earlier,
                    category=finished.category,
                )
            except InvalidReplyError as exc:
                log_result(
                    logging.WARNING,
                    session_id,
                    f"invalid_reply:{exc.reason}",
                    result,
                    INTERVIEWER_STREAM_TASK,
                    version,
                    budget_left_ms,
                )
                if shown:
                    yield Reset()
                continue
            log_result(logging.INFO, session_id, "ok", result, INTERVIEWER_STREAM_TASK, version, budget_left_ms)
            yield Written(reply, results, version)
            return
        yield Written(None, results, version)

    async def _stream_draft(
        self,
        messages: Sequence[ChatMessage],
        remaining: float,
        deadline: Deadline,
        follow_up_category: QuestionCategory | None,
    ) -> AsyncGenerator[str | Draft]:
        """One streamed attempt: the question's text chunks (never the CATEGORY line), then the finished Draft.
        Raises InvalidReplyError for a bad CATEGORY line before any text, and LLMTimeoutError when the turn's deadline
        runs out mid-stream."""
        buffer, category, text = "", follow_up_category, ""
        result: LLMResult | None = None
        stream = self.llm.stream(messages, max_tokens=self.max_tokens, budget_seconds=remaining)
        async with aclosing(stream) as items:
            async for item in items:
                if isinstance(item, LLMResult):
                    result = item
                    continue
                if category is None:
                    buffer += item
                    split = split_header(buffer)
                    if split is None:
                        continue
                    category, item = split.category, split.text
                if item:
                    text += item
                    yield item
                if deadline.remaining() <= 0:
                    exc = LLMTimeoutError("the turn's time ran out mid-question")
                    exc.after_output = bool(text)
                    raise exc
        if category is None:
            # The reply ended inside its first line.
            split = split_header(buffer, final=True)
            assert split is not None
            category, text = split.category, split.text
        assert result is not None
        yield Draft(category, text, result)

    def plan_write(
        self, decision: Decision | None, inputs: InterviewerInputs, deadline: Deadline, *, last_main: bool
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
        """The write's result decides the outcome: a failed follow-up moves on, and the turn's summary line is logged."""
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
            llm_ms=round((self.budget_seconds - deadline.remaining()) * 1000),
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

    def _decide(
        self, session_id: uuid.UUID, inputs: InterviewerInputs, deadline: Deadline
    ) -> tuple[Decision | None, list[LLMResult], str | None]:
        """At most two attempts within the decide cap; any failure means "next_question" with no note."""
        try:
            built = self.context.build(DECISION_TASK, inputs)
        except ContextTooLargeError:
            log_llm_call(
                logging.WARNING,
                session_id,
                "context_too_large",
                task=DECISION_TASK,
                latency_ms=0,
                attempts=0,
            )
            return None, [], None
        version = built.prompt_version
        # Never past the write call's reserve: leftover time goes to the question the candidate sees.
        end = self.clock() + min(
            DECIDE_MAX_SECONDS, deadline.remaining() - WRITE_RESERVE_SECONDS
        )
        results: list[LLMResult] = []
        for attempt in range(1, MAX_REPLY_ATTEMPTS + 1):
            left = end - self.clock()
            if left <= 0 or (attempt > 1 and left < MIN_SECONDS_FOR_RETRY):
                break
            budget_left_ms = round(deadline.remaining() * 1000)
            try:
                result = self.llm.complete(
                    built.messages, max_tokens=self.max_tokens, budget_seconds=left
                )
            except LLMError as exc:
                _log_error(session_id, exc, DECISION_TASK, version, budget_left_ms)
                break
            results.append(result)
            if not result.text.strip():
                log_result(
                    logging.WARNING,
                    session_id,
                    "empty_reply",
                    result,
                    DECISION_TASK,
                    version,
                    budget_left_ms,
                )
                break
            try:
                decision = parse_decision_reply(result.text)
            except InvalidReplyError as exc:
                log_result(
                    logging.WARNING,
                    session_id,
                    f"invalid_reply:{exc.reason}",
                    result,
                    DECISION_TASK,
                    version,
                    budget_left_ms,
                )
                continue
            log_result(
                logging.INFO,
                session_id,
                "ok",
                result,
                DECISION_TASK,
                version,
                budget_left_ms,
                action=decision.action,
                gap=decision.gap or "-",
            )
            if decision.note_dropped:
                llm_logger.warning(
                    "note_dropped session=%s reason=%s",
                    session_id,
                    decision.note_dropped,
                )
            return decision, results, version
        return None, results, version

    def _write(
        self,
        session_id: uuid.UUID,
        inputs: InterviewerInputs,
        deadline: Deadline,
        *,
        follow_up_category: QuestionCategory | None,
    ) -> Written:
        """At most two attempts. Only a reply that came back but broke the contract is retried: a provider error was
        already retried inside the provider, and an empty reply would fail the same way.
        """
        try:
            built = self.context.build(INTERVIEWER_TASK, inputs)
        except ContextTooLargeError:
            # Even trimmed, the input is over the limit: the bank asks this one (the manager logged the sizes).
            log_llm_call(
                logging.WARNING,
                session_id,
                "context_too_large",
                task=INTERVIEWER_TASK,
                latency_ms=0,
                attempts=0,
            )
            return Written(None, [], None)
        version = built.prompt_version
        # The code-side repeat check always sees every earlier question, whatever the strategy sent.
        earlier = [turn.question for turn in inputs.turns]
        results: list[LLMResult] = []
        for attempt in range(1, MAX_REPLY_ATTEMPTS + 1):
            remaining = deadline.remaining()
            if attempt > 1 and remaining < MIN_SECONDS_FOR_RETRY:
                break
            budget_left_ms = round(remaining * 1000)
            try:
                result = self.llm.complete(
                    built.messages, max_tokens=self.max_tokens, budget_seconds=remaining
                )
            except LLMError as exc:
                _log_error(session_id, exc, INTERVIEWER_TASK, version, budget_left_ms)
                break
            results.append(result)
            if not result.text.strip():
                log_result(
                    logging.WARNING,
                    session_id,
                    "empty_reply",
                    result,
                    INTERVIEWER_TASK,
                    version,
                    budget_left_ms,
                )
                break
            try:
                reply = parse_interviewer_reply(
                    result.text,
                    interview_type=inputs.interview_type,
                    earlier_questions=earlier,
                    follow_up_category=follow_up_category,
                )
            except InvalidReplyError as exc:
                log_result(
                    logging.WARNING,
                    session_id,
                    f"invalid_reply:{exc.reason}",
                    result,
                    INTERVIEWER_TASK,
                    version,
                    budget_left_ms,
                )
                continue
            log_result(
                logging.INFO,
                session_id,
                "ok",
                result,
                INTERVIEWER_TASK,
                version,
                budget_left_ms,
            )
            if reply.note_dropped:
                llm_logger.warning(
                    "note_dropped session=%s reason=%s", session_id, reply.note_dropped
                )
            return Written(reply, results, version)
        return Written(None, results, version)


def _decision_label(decision: Decision) -> str:
    return f"{decision.action}:{decision.gap}" if decision.gap else str(decision.action)


def sum_known(values: Sequence[int | None]) -> int | None:
    known = [v for v in values if v is not None]
    return sum(known) if known else None


# --- log lines ---


def log_llm_call(
    level: int,
    session_id: uuid.UUID,
    outcome: str,
    *,
    task: str,
    prompt_version: str | None = None,
    model: str = "-",
    prompt_tokens: int | None = None,
    completion_tokens: int | None = None,
    # Part of prompt_tokens served from the provider's prompt cache / part of completion_tokens spent on hidden
    # reasoning. "-" when the provider doesn't report them.
    cached_tokens: int | None = None,
    reasoning_tokens: int | None = None,
    latency_ms: int,
    attempts: int,
    finish: str | None = None,
    # Time left on the turn deadline when the call started.
    budget_left_ms: int | None = None,
    # Decide calls only: what the model decided.
    action: str | None = None,
    gap: str | None = None,
) -> None:
    decided = "" if action is None else f" action={action} gap={gap or '-'}"
    llm_logger.log(
        level,
        "llm_call session=%s task=%s model=%s prompt_version=%s prompt_tokens=%s cached_tokens=%s "
        "completion_tokens=%s reasoning_tokens=%s latency_ms=%s attempts=%s finish=%s budget_left_ms=%s%s outcome=%s",
        session_id,
        task,
        model,
        prompt_version or "-",
        _shown(prompt_tokens),
        _shown(cached_tokens),
        _shown(completion_tokens),
        _shown(reasoning_tokens),
        latency_ms,
        attempts,
        finish or "-",
        _shown(budget_left_ms),
        decided,
        outcome,
    )


def log_result(
    level: int,
    session_id: uuid.UUID,
    outcome: str,
    result: LLMResult,
    task: str,
    prompt_version: str | None,
    budget_left_ms: int | None = None,
    **decided: str,
) -> None:
    log_llm_call(
        level,
        session_id,
        outcome,
        task=task,
        prompt_version=prompt_version,
        model=result.model,
        prompt_tokens=result.prompt_tokens,
        completion_tokens=result.completion_tokens,
        cached_tokens=result.cached_tokens,
        reasoning_tokens=result.reasoning_tokens,
        latency_ms=result.latency_ms,
        attempts=result.attempts,
        finish=result.finish_reason,
        budget_left_ms=budget_left_ms,
        **decided,
    )


def _log_error(
    session_id: uuid.UUID, exc: LLMError, task: str, version: str, budget_left_ms: int
) -> None:
    # Transient faults are expected now and then; a bad key or broken reply needs someone to look.
    log_llm_call(
        logging.WARNING if exc.retryable else logging.ERROR,
        session_id,
        type(exc).__name__,
        task=task,
        prompt_version=version,
        latency_ms=exc.latency_ms,
        attempts=exc.attempts,
        finish=exc.finish_reason,
        budget_left_ms=budget_left_ms,
    )


def log_turn_summary(
    session_id: uuid.UUID,
    *,
    decision: str,
    action: str,
    override: str | None = None,
    source: str,
    fallback: str | None = None,
    llm_ms: int = 0,
) -> None:
    """Why the turn ended as it did: the only place an overridden follow-up or a bank fallback is explained."""
    llm_logger.info(
        "turn_summary session=%s decision=%s action=%s override=%s source=%s fallback=%s llm_ms=%s",
        session_id,
        decision,
        action,
        override or "-",
        source,
        fallback or "-",
        llm_ms,
    )


def log_stream_summary(
    session_id: uuid.UUID,
    *,
    terminal: str,
    first_event_ms: int | None,
    first_token_ms: int | None,
    total_ms: int,
    resets: int,
    cancelled: bool,
) -> None:
    """How a streamed turn felt and ended: time to the first event and to the first question token (from the write
    call's start), total time, drafts taken back, and whether the client left. Metadata only, never text."""
    llm_logger.info(
        "stream_turn_summary session=%s terminal=%s first_event_ms=%s first_token_ms=%s total_ms=%s resets=%s "
        "cancelled=%s",
        session_id,
        terminal,
        _shown(first_event_ms),
        _shown(first_token_ms),
        total_ms,
        resets,
        str(cancelled).lower(),
    )


def _shown(value: int | None) -> str:
    return "-" if value is None else str(value)
