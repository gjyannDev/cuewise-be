"""The interviewer's log lines: one per LLM call, one per answer turn and one per streamed turn."""

import logging
import uuid
from collections.abc import Sequence

from app.core.ai.provider import LLMError, LLMResult

# One line per LLM call and one per answer turn: metadata only (ids, model, tokens, timing, reason codes), never
# question, answer, note or job-description text.
llm_logger = logging.getLogger("app.llm")
# Embedding calls and retrieval (knowledge-base RAG), apart from the chat calls above; the same metadata-only rule.
rag_logger = logging.getLogger("app.rag")


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


def log_llm_error(
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
    # The interview it was for (retrieval at start); None for ingestion.
    session_id: uuid.UUID | None = None,
) -> None:
    """One line per embedding call (ingest or retrieval): metadata only, never the embedded text."""
    rag_logger.log(
        level,
        "embedding_call session=%s purpose=%s kind=%s model=%s input_tokens=%s latency_ms=%s attempts=%s outcome=%s",
        session_id or "-",
        purpose,
        kind,
        model,
        _shown(input_tokens),
        latency_ms,
        attempts,
        outcome,
    )


def log_retrieval(
    level: int,
    session_id: uuid.UUID,
    *,
    mode: str | None,
    scores: Sequence[float | None],
    outcome: str,
    latency_ms: int,
) -> None:
    """Which reference notes an interview got at start: mode, count, scores and the reason code. Never the query or
    note text."""
    rag_logger.log(
        level,
        "retrieval session=%s mode=%s count=%s scores=%s latency_ms=%s outcome=%s",
        session_id,
        mode or "-",
        len(scores),
        ",".join("-" if s is None else f"{s:.3f}" for s in scores) or "-",
        latency_ms,
        outcome,
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
