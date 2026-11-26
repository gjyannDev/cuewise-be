"""The interviewer's log events: one per LLM call, one per answer turn and one per streamed turn.

Metadata only (ids, model, tokens, timing, reason codes), never question, answer, note or job-description text.
`session` (and `user`) are not passed here: the service binds them once per request (`bind_log_context`), and every
line of that request carries them. A value the provider didn't report is logged as null.
"""

import logging
from collections.abc import Sequence

from app.core.ai.provider import LLMError, LLMResult
from app.core.logging import get_logger

llm_logger = get_logger("app.llm")
# Embedding calls and retrieval (knowledge-base RAG), apart from the chat calls above; the same metadata-only rule.
rag_logger = get_logger("app.rag")


def sum_known(values: Sequence[int | None]) -> int | None:
    known = [v for v in values if v is not None]
    return sum(known) if known else None


# --- log lines ---


def log_llm_call(
    level: int,
    outcome: str,
    *,
    task: str,
    prompt_version: str | None = None,
    model: str = "-",
    prompt_tokens: int | None = None,
    completion_tokens: int | None = None,
    # Part of prompt_tokens served from the provider's prompt cache / part of completion_tokens spent on hidden
    # reasoning. Null when the provider doesn't report them.
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
    decided = {} if action is None else {"action": action, "gap": gap or "-"}
    llm_logger.log(
        level,
        "llm_call",
        task=task,
        model=model,
        prompt_version=prompt_version or "-",
        prompt_tokens=prompt_tokens,
        cached_tokens=cached_tokens,
        completion_tokens=completion_tokens,
        reasoning_tokens=reasoning_tokens,
        latency_ms=latency_ms,
        attempts=attempts,
        finish=finish or "-",
        budget_left_ms=budget_left_ms,
        **decided,
        outcome=outcome,
    )


def log_result(
    level: int,
    outcome: str,
    result: LLMResult,
    task: str,
    prompt_version: str | None,
    budget_left_ms: int | None = None,
    **decided: str,
) -> None:
    log_llm_call(
        level,
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


def log_llm_error(exc: LLMError, task: str, version: str, budget_left_ms: int) -> None:
    # Transient faults are expected now and then; a bad key or broken reply needs someone to look.
    log_llm_call(
        logging.WARNING if exc.retryable else logging.ERROR,
        type(exc).__name__,
        task=task,
        prompt_version=version,
        latency_ms=exc.latency_ms,
        attempts=exc.attempts,
        finish=exc.finish_reason,
        budget_left_ms=budget_left_ms,
    )


def log_turn_summary(
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
        "turn_summary",
        decision=decision,
        action=action,
        override=override or "-",
        source=source,
        fallback=fallback or "-",
        llm_ms=llm_ms,
    )


def log_embedding_call(
    level: int,
    *,
    purpose: str,
    kind: str,
    model: str,
    outcome: str,
    latency_ms: int,
    attempts: int,
    input_tokens: int | None = None,
) -> None:
    """One line per embedding call (ingest or retrieval): metadata only, never the embedded text. At retrieval the
    interview's `session` comes from the request; ingestion has none."""
    rag_logger.log(
        level,
        "embedding_call",
        purpose=purpose,
        kind=kind,
        model=model,
        input_tokens=input_tokens,
        latency_ms=latency_ms,
        attempts=attempts,
        outcome=outcome,
    )


def log_retrieval(
    level: int,
    *,
    mode: str | None,
    scores: Sequence[float | None],
    outcome: str,
    latency_ms: int,
    profile_notes: int = 0,
) -> None:
    """Which reference notes an interview got at start: mode, count, scores, how many the candidate profile's query
    added, and the reason code. Never the query, the profile or note text."""
    rag_logger.log(
        level,
        "retrieval",
        mode=mode or "-",
        count=len(scores),
        # The same 3-decimal, comma-joined text as the old log line, so reports read both alike.
        scores=",".join("-" if s is None else f"{s:.3f}" for s in scores) or "-",
        latency_ms=latency_ms,
        outcome=outcome,
        profile_notes=profile_notes,
    )


def log_stream_summary(
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
        "stream_turn_summary",
        terminal=terminal,
        first_event_ms=first_event_ms,
        first_token_ms=first_token_ms,
        total_ms=total_ms,
        resets=resets,
        cancelled=cancelled,
    )
