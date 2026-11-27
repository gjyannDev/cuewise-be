"""The decide step of an answer turn: the model suggests following up or moving on, with a gap and a running note.

On the LangChain call layer with structured output (U3b1): the model is given `ModelDecision` (every field required)
as a JSON schema through `complete_structured`. `parse_decision_reply` still reads the reply text as a second check,
so the gap and note rules keep their one home.
"""

import logging
import time
import uuid
from collections.abc import Callable

from app.core.ai.chat import ChatModel, complete_structured, fixed_prompt
from app.core.ai.context import ContextManager, ContextTooLargeError
from app.core.ai.provider import LLMError, LLMResult

from ..ai.interviews_context import InterviewerInputs
from ..ai.interviews_model_schemas import ModelDecision
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
    model: ChatModel,
    context: ContextManager,
    session_id: uuid.UUID,
    inputs: InterviewerInputs,
    deadline: Deadline,
    *,
    max_tokens: int,
    clock: Callable[[], float],
    sleep: Callable[[float], None] = time.sleep,
) -> tuple[Decision | None, list[LLMResult], str | None]:
    """At most two attempts within the decide cap; any failure means "next_question" with no note. Transport errors
    are retried by the call helper (on `clock`, waiting with `sleep`), never by this loop; an empty reply is the
    helper's `LLMBadResponseError` and is not retried either."""
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
    prompt = fixed_prompt(built.messages)
    # Never past the write call's reserve: leftover time goes to the question the candidate sees.
    end = clock() + min(
        DECIDE_MAX_SECONDS, deadline.remaining() - WRITE_RESERVE_SECONDS
    )
    results: list[LLMResult] = []
    for _, left in ReplyAttempts(lambda: end - clock()):
        budget_left_ms = round(deadline.remaining() * 1000)
        try:
            outcome = complete_structured(
                model,
                prompt,
                {},
                ModelDecision,
                max_tokens=max_tokens,
                budget_seconds=left,
                labels={"task": DECISION_TASK, "prompt_version": version, "budget_left_ms": budget_left_ms},
                clock=clock,
                sleep=sleep,
            )
        except LLMError as exc:
            log_llm_error(exc, DECISION_TASK, version, budget_left_ms)
            break
        result = outcome.result
        results.append(result)
        try:
            # The parser first, for its precise reason codes; then the schema, which an accepted reply must still fit.
            decision = parse_decision_reply(result.text)
            if outcome.value is None:
                raise InvalidReplyError("schema")
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
