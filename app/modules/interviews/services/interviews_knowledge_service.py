"""Ingestion: turn the validated note chunks into stored rows with their embeddings, idempotently.

Idempotent means running it twice changes nothing the second time: each chunk carries a hash of its content, so an
unchanged chunk is skipped without an embedding call (calls cost time and free-tier quota). A changed chunk becomes a
new row and the old one is retired, so an interview that already uses the old text keeps it. Each chunk is committed
on its own: if the embedder fails halfway, what was stored stays, and the next run only does the rest.
"""

import logging
import time
from collections.abc import Callable, Sequence
from typing import NamedTuple

from app.core.ai.embedder import Embedder, EmbeddingKind
from app.core.ai.provider import LLMError

from ..ai.interviews_turn_log import log_embedding_call
from ..constants.interviews_constants import KNOWLEDGE_VECTOR_SIZE
from ..repositories.interviews_knowledge_repository import KnowledgeRepository
from ..utils.interviews_knowledge_utils import NoteChunk, embedding_text

INGEST_PURPOSE = "ingest"


class IngestCounts(NamedTuple):
    new: int
    changed: int
    unchanged: int
    # Active rows whose note or section is gone from the corpus.
    retired: int
    # Retired rows no interview points at, removed at the end.
    deleted: int


class IngestError(Exception):
    """Ingestion stopped; the message names the chunk (or the setting) and the reason, never note text."""


def ingest_corpus(
    chunks: Sequence[NoteChunk],
    embedder: Embedder,
    repo: KnowledgeRepository,
    *,
    vector_size: int = KNOWLEDGE_VECTOR_SIZE,
    # Wait between embedding calls, to stay under the vendor's calls-per-minute limit.
    pause_seconds: float = 0.0,
    sleep: Callable[[float], None] = time.sleep,
) -> IngestCounts:
    if embedder.dimensions != vector_size:
        raise IngestError(
            f"EMBEDDING_DIMENSIONS is {embedder.dimensions} but the vector column holds {vector_size}: another size "
            "needs a new migration and a full re-ingest"
        )
    stored = {row.note_key: row for row in repo.active_chunks()}
    new = changed = unchanged = calls = 0
    for chunk in chunks:
        row = stored.pop(chunk.note_key, None)
        # Vectors of another model can't be compared with this one's, so such rows count as changed.
        if row is not None and row.content_hash == chunk.content_hash and row.embedding_model == embedder.model:
            unchanged += 1
            continue
        if calls and pause_seconds:
            sleep(pause_seconds)
        calls += 1
        repo.add(chunk, _embed(chunk, embedder, vector_size), embedder.model, replaces=row)
        if row is None:
            new += 1
        else:
            changed += 1
    gone = list(stored.values())
    repo.retire(gone)
    return IngestCounts(new, changed, unchanged, len(gone), repo.delete_unreferenced_retired())


def _embed(chunk: NoteChunk, embedder: Embedder, vector_size: int) -> list[float]:
    try:
        result = embedder.embed([embedding_text(chunk)], kind=EmbeddingKind.document)
    except LLMError as exc:
        log_embedding_call(
            logging.WARNING,
            purpose=INGEST_PURPOSE,
            kind=EmbeddingKind.document,
            model=embedder.model,
            outcome=type(exc).__name__,
            latency_ms=exc.latency_ms,
            attempts=exc.attempts,
        )
        raise IngestError(f"{chunk.note_key}: embedding failed ({type(exc).__name__})") from exc
    log_embedding_call(
        logging.INFO,
        purpose=INGEST_PURPOSE,
        kind=EmbeddingKind.document,
        model=result.model,
        outcome="ok",
        latency_ms=result.latency_ms,
        attempts=result.attempts,
        input_tokens=result.input_tokens,
    )
    [vector] = result.vectors
    if len(vector) != vector_size:
        raise IngestError(f"{chunk.note_key}: the embedding has {len(vector)} numbers, the column holds {vector_size}")
    return vector
