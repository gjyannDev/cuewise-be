"""The job-description summary (made once at interview start), on the LangChain call layer (U3a).

A long job description is condensed once, so every later call of the interview sends less. The chain is LCEL's
`prompt | model`: the prompt is the summary task's messages as our context manager builds them from
`job_description_summary_v2.md` (same text, same version, same `context_build` log as before the migration), and
`complete_chat` runs it with the summary's own time cap. One attempt at the content: any failure keeps the original
text and never blocks the interview. Usage is logged, never the text.
"""

import logging
from typing import NamedTuple

from app.core.ai.chat import ChatModel, complete_chat, fixed_prompt
from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMError, LLMResult

from ..constants.interviews_constants import SUMMARY_TASK, SUMMARY_TIME_CAP_SECONDS
from .interviews_context import CONTEXT_MANAGER, SummaryInputs
from .interviews_reply import InvalidReplyError, validate_summary
from .interviews_turn_log import log_llm_call, log_result


class SummaryOutcome(NamedTuple):
    """What one summary call gave: the usable summary (None when it can't replace the original), the model's reply
    with its usage (None when the call failed), and the failure (None when the model answered). The app uses
    `summary`; the evals score the reply itself and count its tokens."""

    summary: str | None
    result: LLMResult | None
    error: LLMError | None


def summarize_job_description(
    model: ChatModel, job_description: str, *, max_tokens: int, context: ContextManager = CONTEXT_MANAGER
) -> SummaryOutcome:
    """One summary call; see `SummaryOutcome`. A reply that `validate_summary` rejects gives `summary=None`."""
    built = context.build(SUMMARY_TASK, SummaryInputs(job_description))
    try:
        result = complete_chat(
            model,
            fixed_prompt(built.messages),
            {},
            max_tokens=max_tokens,
            budget_seconds=SUMMARY_TIME_CAP_SECONDS,
            labels={"task": SUMMARY_TASK, "prompt_version": built.prompt_version},
        )
    except LLMError as exc:
        log_llm_call(
            logging.WARNING,
            f"summary_failed:{type(exc).__name__}",
            task=SUMMARY_TASK,
            prompt_version=built.prompt_version,
            latency_ms=exc.latency_ms,
            attempts=exc.attempts,
            finish=exc.finish_reason,
        )
        return SummaryOutcome(None, None, exc)
    try:
        summary = validate_summary(job_description, result.text)
    except InvalidReplyError as exc:
        log_result(logging.WARNING, f"summary_invalid:{exc.reason}", result, SUMMARY_TASK, built.prompt_version)
        return SummaryOutcome(None, result, None)
    log_result(logging.INFO, "summary_ok", result, SUMMARY_TASK, built.prompt_version)
    return SummaryOutcome(summary, result, None)
