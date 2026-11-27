"""The blocking write step: the interviewer writes the next question (or a follow-up) as one JSON reply, on the
LangChain call layer (U3b1)."""

import logging
import uuid

from app.core.ai.chat import ChatModel, complete_chat, fixed_prompt
from app.core.ai.context import ContextManager, ContextTooLargeError
from app.core.ai.provider import LLMError, LLMResult

from ..ai.interviews_context import InterviewerInputs, write_trace_labels
from ..ai.interviews_reply import InvalidReplyError, parse_interviewer_reply
from ..ai.interviews_reply_attempts import ReplyAttempts
from ..ai.interviews_turn_limits import Deadline
from ..ai.interviews_turn_log import llm_logger, log_llm_call, log_llm_error, log_result
from ..ai.interviews_turn_types import Written
from ..constants.interviews_constants import (
    INTERVIEWER_TASK,
    QuestionCategory,
)


def write(
    model: ChatModel,
    context: ContextManager,
    session_id: uuid.UUID,
    inputs: InterviewerInputs,
    deadline: Deadline,
    *,
    follow_up_category: QuestionCategory | None,
    max_tokens: int,
) -> Written:
    """At most two attempts. Only a reply that came back but broke the contract is retried: a transport error was
    already retried by the call helper, and an empty reply (the helper's `LLMBadResponseError`) would fail the same
    way.
    """
    try:
        built = context.build(INTERVIEWER_TASK, inputs)
    except ContextTooLargeError:
        # Even trimmed, the input is over the limit: the bank asks this one (the manager logged the sizes).
        log_llm_call(
            logging.WARNING,
            "context_too_large",
            task=INTERVIEWER_TASK,
            latency_ms=0,
            attempts=0,
        )
        return Written(None, [], None)
    version = built.prompt_version
    prompt = fixed_prompt(built.messages)
    # The code-side repeat check always sees every earlier question, whatever the strategy sent.
    earlier = [turn.question for turn in inputs.turns]
    results: list[LLMResult] = []
    for _, remaining in ReplyAttempts(deadline.remaining):
        budget_left_ms = round(remaining * 1000)
        try:
            result = complete_chat(
                model,
                prompt,
                {},
                max_tokens=max_tokens,
                budget_seconds=remaining,
                labels=write_trace_labels(INTERVIEWER_TASK, built, budget_left_ms),
            )
        except LLMError as exc:
            log_llm_error(exc, INTERVIEWER_TASK, version, budget_left_ms)
            break
        results.append(result)
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
                f"invalid_reply:{exc.reason}",
                result,
                INTERVIEWER_TASK,
                version,
                budget_left_ms,
            )
            continue
        log_result(
            logging.INFO,
            "ok",
            result,
            INTERVIEWER_TASK,
            version,
            budget_left_ms,
        )
        if reply.note_dropped:
            llm_logger.warning("note_dropped", reason=reply.note_dropped)
        return Written(reply, results, version)
    return Written(None, results, version)
