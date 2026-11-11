"""Ingest the reference notes into the database (knowledge-base RAG).

    uv run python -m app.modules.interviews.tooling.interviews_knowledge_ingest [--corpus DIR] [--pause-seconds S]

Validates every note first (nothing is written if one is invalid), then embeds only new or changed chunks. Safe to run
again at any time: unchanged chunks cost nothing, and a run that stopped halfway finishes the rest. Spends real
embedding calls, so it needs LLM_GOOGLE_API_KEY and the pgvector database (README, "Development database").
"""

import argparse
import sys
import time
from collections.abc import Callable, Sequence
from pathlib import Path

from sqlalchemy.orm import Session

from app.core.ai.embedder import Embedder

from ..constants.interviews_constants import KNOWLEDGE_DIR
from ..repositories.interviews_knowledge_repository import KnowledgeRepository
from ..services.interviews_knowledge_service import IngestError, ingest_corpus
from ..utils.interviews_knowledge_utils import (
    CorpusError,
    load_corpus,
    source_share_problem,
)

# The free tier allows on the order of 100 embedding calls a minute; one per second stays well under it.
DEFAULT_PAUSE_SECONDS = 1.0


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate the reference notes and embed new or changed chunks.")
    parser.add_argument("--corpus", type=Path, default=KNOWLEDGE_DIR, help="folder of note files (*.md)")
    parser.add_argument(
        "--pause-seconds", type=float, default=DEFAULT_PAUSE_SECONDS, help="wait between embedding calls"
    )
    return parser


def main(
    argv: Sequence[str] | None = None,
    *,
    embedder: Embedder | None = None,
    db: Session | None = None,
    sleep: Callable[[float], None] = time.sleep,
) -> int:
    args = _parser().parse_args(argv)
    try:
        corpus = load_corpus(args.corpus)
    except CorpusError as exc:
        print(f"invalid note, nothing was ingested: {exc}")
        return 1
    problem = source_share_problem(corpus.notes)
    for warning in [*corpus.warnings, *([problem] if problem else [])]:
        print(f"warning: {warning}")

    from app.core.ai.factory import build_embedder
    from app.core.config import settings
    from app.db.session import SessionLocal

    own_embedder = embedder is None
    embedder = embedder or build_embedder(settings)
    if embedder is None:
        print("Embeddings are not configured: set LLM_GOOGLE_API_KEY in .env first.")
        return 1
    own_db = db is None
    db = db or SessionLocal()
    try:
        counts = ingest_corpus(
            corpus.chunks, embedder, KnowledgeRepository(db), pause_seconds=args.pause_seconds, sleep=sleep
        )
    except IngestError as exc:
        print(f"ingest stopped: {exc}\nWhat was stored is kept; run it again to finish the rest.")
        return 1
    finally:
        if own_db:
            db.close()
        if own_embedder:
            embedder.close()
    print(
        f"new={counts.new} changed={counts.changed} unchanged={counts.unchanged} retired={counts.retired} "
        f"deleted={counts.deleted}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
