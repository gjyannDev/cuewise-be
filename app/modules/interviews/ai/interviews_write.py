"""The blocking write step: the interviewer writes the next question (or a follow-up) as one JSON reply."""

import logging
import uuid

from app.core.ai.context import ContextManager, ContextTooLargeError
from app.core.ai.provider import LLMError, LLMProvider, LLMResult

from ..ai.interviews_context import InterviewerInputs
from ..ai.interviews_reply import InvalidReplyError, parse_interviewer_reply
from ..ai.interviews_turn_limits import Deadline
from ..ai.interviews_turn_log import llm_logger, log_llm_call, log_llm_error, log_result
from ..ai.interviews_turn_types import Written
from ..constants.interviews_constants import (
    INTERVIEWER_TASK,
    MAX_REPLY_ATTEMPTS,
    MIN_SECONDS_FOR_RETRY,
    QuestionCategory,
)


def write(
    llm: LLMProvider,
    context: ContextManager,
    session_id: uuid.UUID,
    inputs: InterviewerInputs,
    deadline: Deadline,
    *,
    follow_up_category: QuestionCategory | None,
    max_tokens: int,
) -> Written:
    """At most two attempts. Only a reply that came back but broke the contract is retried: a provider error was
    already retried inside the provider, and an empty reply would fail the same way.
    """
    try:
        built = context.build(INTERVIEWER_TASK, inputs)
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
            result = llm.complete(
                built.messages,
                max_tokens=max_tokens,
                budget_seconds=remaining,
                trace_labels={"task": INTERVIEWER_TASK, "prompt_version": version, "budget_left_ms": budget_left_ms},
            )
        except LLMError as exc:
            log_llm_error(session_id, exc, INTERVIEWER_TASK, version, budget_left_ms)
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
