"""Retrieval at interview start: pick up to 6 reference notes for the interview's role, level and job description.

Retrieval-augmented generation (RAG) means giving the model relevant text it was not trained on, found at request
time, instead of hoping it knows. Here the "relevant text" is curated interview notes, chosen once per interview:

1. Filter: only notes scoped to the interview's role (or every role) and level. These come from the interview setup,
   never from the job description, so a job description that says "only show senior notes" can't change them.
2. Rank (vector mode): embed the job description (its summary when there is one) as a query and order the eligible
   notes by cosine similarity; keep the top 6 above the threshold.
3. Fall back (filter mode): with no job description, or when ranking isn't possible (no embedder, an error, the time
   cap, nothing similar enough), pick up to 6 eligible notes in an order seeded by the interview id.

Nothing here can fail an interview: the worst case is no notes, and the interview runs exactly as before.
"""

import logging
import time
import uuid
from collections.abc import Callable
from typing import NamedTuple

from sqlalchemy.exc import SQLAlchemyError

from app.core.ai.embedder import Embedder, EmbeddingKind, EmbeddingSizeError
from app.core.ai.provider import LLMError, LLMRateLimitError, LLMTimeoutError
from app.core.ai.tracing import Step, Tracer

from ..ai.interviews_turn_log import log_embedding_call, log_retrieval
from ..constants.interviews_constants import (
    KNOWLEDGE_VECTOR_SIZE,
    RETRIEVAL_MIN_SIMILARITY,
    RETRIEVAL_TIME_CAP_SECONDS,
    RETRIEVAL_TOP_K,
    RetrievalDegrade,
    RetrievalMode,
    RetrievalSkip,
)
from ..repositories.interviews_knowledge_repository import (
    EligibleChunk,
    KnowledgeRepository,
)
from ..utils.interviews_knowledge_utils import (
    ReferenceNote,
    pick_filter_notes,
    query_text,
)

RETRIEVAL_PURPOSE = "retrieval"
OK = "ok"


class Retrieval(NamedTuple):
    # None when retrieval was skipped (no notes).
    mode: RetrievalMode | None
    notes: list[ReferenceNote]
    # "ok", "retrieval_degraded:<reason>" or "retrieval_skipped:<reason>".
    outcome: str


class RetrievalService:
    def __init__(
        self,
        repo: KnowledgeRepository,
        embedder: Embedder | None,
        *,
        # False = the LLM is off and the bank asks every question: notes would never be read.
        llm_on: bool,
        tracer: Tracer | None = None,
        clock: Callable[[], float] = time.monotonic,
        cap_seconds: float = RETRIEVAL_TIME_CAP_SECONDS,
        top_k: int = RETRIEVAL_TOP_K,
        min_similarity: float = RETRIEVAL_MIN_SIMILARITY,
        vector_size: int = KNOWLEDGE_VECTOR_SIZE,
    ):
        self.repo = repo
        self.embedder = embedder
        self.llm_on = llm_on
        self.tracer = tracer or Tracer(None)
        self.clock = clock
        self.cap_seconds = cap_seconds
        self.top_k = top_k
        self.min_similarity = min_similarity
        self.vector_size = vector_size

    def retrieve(
        self,
        session_id: uuid.UUID,
        role: str,
        level: str,
        *,
        summary: str | None,
        job_description: str | None,
    ) -> Retrieval:
        start = self.clock()
        if not self.llm_on:
            # Nothing is read or embedded, so there is nothing to trace; the log line still says why there are no notes.
            return self._finish(session_id, _skipped(RetrievalSkip.llm_off), start, None)
        with self.tracer.step(RETRIEVAL_PURPOSE, metadata={"role": role, "level": level}) as step:
            return self._finish(session_id, self._retrieve(session_id, role, level, query_text(summary, job_description)), start, step)

    def _finish(self, session_id: uuid.UUID, result: Retrieval, start: float, step: Step | None) -> Retrieval:
        scores = [note.score for note in result.notes]
        log_retrieval(
            _log_level(result.outcome),
            session_id,
            mode=result.mode,
            scores=scores,
            outcome=result.outcome,
            latency_ms=round((self.clock() - start) * 1000),
        )
        if step is not None:
            # Ids, counts, scores and codes only: the job description is personal data.
            step.finish(
                output={
                    "mode": result.mode,
                    "count": len(result.notes),
                    "chunk_ids": [str(note.chunk_id) for note in result.notes],
                    "scores": scores,
                    "outcome": result.outcome,
                }
            )
        return result

    def _retrieve(self, session_id: uuid.UUID, role: str, level: str, query: str | None) -> Retrieval:
        try:
            eligible = self.repo.eligible_chunks(role, level)
        except SQLAlchemyError:
            self.repo.release()
            return _skipped(RetrievalSkip.db_error)
        # Don't hold a transaction open while waiting on the embedding call.
        self.repo.release()
        if not eligible:
            return _skipped(RetrievalSkip.no_match)
        if query is None:
            return self._filter(eligible, session_id, OK)
        vector, degraded = self._embed(session_id, query)
        if degraded is not None:
            return self._filter(eligible, session_id, f"retrieval_degraded:{degraded}")
        assert vector is not None and self.embedder is not None
        try:
            nearest = self.repo.nearest_chunks(role, level, self.embedder.model, vector, self.top_k)
        except SQLAlchemyError:
            self.repo.release()
            return _skipped(RetrievalSkip.db_error)
        kept = [(chunk, score) for chunk, score in nearest if score >= self.min_similarity]
        if not kept:
            return self._filter(eligible, session_id, f"retrieval_degraded:{RetrievalDegrade.below_threshold}")
        notes = [
            ReferenceNote(chunk.id, chunk.competency, chunk.text, rank, round(score, 4))
            for rank, (chunk, score) in enumerate(kept, start=1)
        ]
        return Retrieval(RetrievalMode.vector, notes, OK)

    def _embed(self, session_id: uuid.UUID, query: str) -> tuple[list[float] | None, RetrievalDegrade | None]:
        if self.embedder is None:
            return None, RetrievalDegrade.not_configured
        if self.embedder.dimensions != self.vector_size:
            return None, RetrievalDegrade.size_mismatch
        try:
            result = self.embedder.embed([query], kind=EmbeddingKind.query, budget_seconds=self.cap_seconds)
        except LLMError as exc:
            log_embedding_call(
                logging.WARNING,
                purpose=RETRIEVAL_PURPOSE,
                kind=EmbeddingKind.query,
                model=self.embedder.model,
                outcome=type(exc).__name__,
                latency_ms=exc.latency_ms,
                attempts=exc.attempts,
                session_id=session_id,
            )
            return None, _degrade_reason(exc)
        log_embedding_call(
            logging.INFO,
            purpose=RETRIEVAL_PURPOSE,
            kind=EmbeddingKind.query,
            model=result.model,
            outcome=OK,
            latency_ms=result.latency_ms,
            attempts=result.attempts,
            input_tokens=result.input_tokens,
            session_id=session_id,
        )
        [vector] = result.vectors
        if len(vector) != self.vector_size:
            return None, RetrievalDegrade.size_mismatch
        return vector, None

    def _filter(self, eligible: list[EligibleChunk], session_id: uuid.UUID, outcome: str) -> Retrieval:
        picked = pick_filter_notes(eligible, session_id, self.top_k)
        notes = [ReferenceNote(chunk.id, chunk.competency, chunk.text, rank, None) for rank, chunk in enumerate(picked, start=1)]
        return Retrieval(RetrievalMode.filter, notes, outcome)


def _skipped(reason: RetrievalSkip) -> Retrieval:
    return Retrieval(None, [], f"retrieval_skipped:{reason}")


def _log_level(outcome: str) -> int:
    # A degrade or a database error is worth a look; no notes because the LLM is off or none match is expected.
    if outcome.startswith("retrieval_degraded") or outcome.endswith(RetrievalSkip.db_error):
        return logging.WARNING
    return logging.INFO


def _degrade_reason(exc: LLMError) -> RetrievalDegrade:
    if isinstance(exc, EmbeddingSizeError):
        return RetrievalDegrade.size_mismatch
    if isinstance(exc, LLMRateLimitError):
        return RetrievalDegrade.rate_limited
    if isinstance(exc, LLMTimeoutError):
        return RetrievalDegrade.timeout
    return RetrievalDegrade.embedder_error
