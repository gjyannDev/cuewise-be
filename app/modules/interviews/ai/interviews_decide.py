"""The decide step of an answer turn: the model suggests following up or moving on, with a gap and a running note."""

import logging
import uuid
from collections.abc import Callable

from app.core.ai.context import ContextManager, ContextTooLargeError
from app.core.ai.provider import LLMError, LLMProvider, LLMResult

from ..ai.interviews_context import InterviewerInputs
from ..ai.interviews_reply import Decision, InvalidReplyError, parse_decision_reply
from ..ai.interviews_reply_attempts import ReplyAttempts
from ..ai.interviews_turn_limits import Deadline
from ..ai.interviews_turn_log import llm_logger, log_llm_call, log_llm_error, log_result
from ..constants.interviews_constants import (
    DECIDE_MAX_SECONDS,
    DECISION_TASK,
    WRITE_RESERVE_SECONDS,
)


def decide(
    llm: LLMProvider,
    context: ContextManager,
    session_id: uuid.UUID,
    inputs: InterviewerInputs,
    deadline: Deadline,
    *,
    max_tokens: int,
    clock: Callable[[], float],
) -> tuple[Decision | None, list[LLMResult], str | None]:
    """At most two attempts within the decide cap; any failure means "next_question" with no note."""
    try:
        built = context.build(DECISION_TASK, inputs)
    except ContextTooLargeError:
        log_llm_call(
            logging.WARNING,
            "context_too_large",
            task=DECISION_TASK,
            latency_ms=0,
            attempts=0,
        )
        return None, [], None
    version = built.prompt_version
    # Never past the write call's reserve: leftover time goes to the question the candidate sees.
    end = clock() + min(
        DECIDE_MAX_SECONDS, deadline.remaining() - WRITE_RESERVE_SECONDS
    )
    results: list[LLMResult] = []
    for _, left in ReplyAttempts(lambda: end - clock()):
        budget_left_ms = round(deadline.remaining() * 1000)
        try:
            result = llm.complete(
                built.messages,
                max_tokens=max_tokens,
                budget_seconds=left,
                trace_labels={"task": DECISION_TASK, "prompt_version": version, "budget_left_ms": budget_left_ms},
            )
        except LLMError as exc:
            log_llm_error(exc, DECISION_TASK, version, budget_left_ms)
            break
        results.append(result)
        if not result.text.strip():
            log_result(
                logging.WARNING,
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
                f"invalid_reply:{exc.reason}",
                result,
                DECISION_TASK,
                version,
                budget_left_ms,
            )
            continue
        log_result(
            logging.INFO,
            "ok",
            result,
            DECISION_TASK,
            version,
            budget_left_ms,
            action=decision.action,
            gap=decision.gap or "-",
        )
        if decision.note_dropped:
            llm_logger.warning("note_dropped", reason=decision.note_dropped)
        return decision, results, version
    return None, results, version
