"""Opt-in evals for the knowledge-base RAG (Slice 8a): does retrieval find the right notes, and do the notes make better
questions?

    uv run python -m app.modules.interviews.tooling.interviews_evals --task retrieval
    uv run python -m app.modules.interviews.tooling.interviews_evals --task generation --repeat 3 --sheet blind.md
    uv run python -m app.modules.interviews.tooling.interviews_evals --task ranking --sheet blind.md

**Retrieval** embeds each labelled query (data/retrieval_eval_cases.json: a job-description-like text, a role and level,
and the `note_key`s that should come back) and reports recall@5 and MRR for vector ranking and for the filter-only
baseline, plus a sweep of similarity thresholds (pick the threshold from it, never guess it).
- recall@5: of the notes that should come back, the share that is in the first five.
- MRR (mean reciprocal rank): 1 / the position of the first right note, averaged; 1.0 = always first.
With Langfuse keys set it is also one Langfuse experiment run of `interviews-eval/retrieval` (one run, whatever
`--repeat` says: the result is deterministic): per case the vector and filter recall@5 and reciprocal rank, per run the
four averages, and metadata naming the embedding model, the threshold and a fingerprint of the ingested notes. It stops
before any call when the database is down or the notes are not ingested.

**Generation** writes the main questions of the setups listed in data/generation_eval_keywords.json three ways: arm A
no notes (interviewer_v5), B filter-only notes, C vector notes (interviewer_v6). Per arm: distinct competencies per
interview and job-description skill coverage (keyword rules, so wording can game them), valid replies, prompt tokens per
question and retrieval time at start. It also writes a blind sheet: the arms' question sets under neutral labels in a
seeded random order, the key in a separate file, for you to rank. With Langfuse keys set, every setup x repeat x arm is
one trace (environment "eval", tagged `arm:A|B|C`, one session per run) holding the retrieval step, each question's
full prompt and reply, and its keyword scores. Rank the sheet before opening those traces: they name the arm.

**Ranking** reads that sheet back once filled in and reports how often each arm ranked first: the main quality signal,
because the rule metrics are gameable.

These cost real calls (embeddings and LLM) and need the pgvector database with the corpus ingested; they never run in
`uv run pytest`. The pure parts below are unit-tested.
"""

import argparse
import itertools
import json
import random
import re
import time
import uuid
from collections.abc import Callable, Collection, Mapping, Sequence
from pathlib import Path
from statistics import mean
from typing import Any, Literal, NamedTuple

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter
from sqlalchemy.exc import SQLAlchemyError

from app.core.ai.embedder import Embedder, EmbeddingKind
from app.core.ai.provider import LLMError, LLMProvider
from app.core.ai.tracing import ExperimentRun, Tracer

from ..ai.interviews_context import CONTEXT_MANAGER, InterviewerInputs
from ..ai.interviews_reply import InvalidReplyError, parse_streamed_reply, split_header
from ..constants.interviews_constants import (
    INTERVIEWER_STREAM_TASK,
    INTERVIEWER_V5_PROMPT_VERSION,
    INTERVIEWER_V6_PROMPT_VERSION,
    MODULE_DIR,
    RETRIEVAL_MIN_SIMILARITY,
    InterviewType,
    JobRole,
    Level,
)
from ..repositories.interviews_knowledge_repository import KnowledgeRepository
from ..services.interviews_retrieval_service import RetrievalService
from ..utils.interviews_knowledge_utils import ReferenceNote, pick_filter_notes
from ..utils.interviews_utils import QuestionTurn
from .interviews_eval_runs import (
    Score,
    final_line,
    git_commit,
    notes_fingerprint,
    run_cases,
    run_description,
    run_metadata,
    run_name,
    run_stamp,
)

RETRIEVAL_CASES_PATH = MODULE_DIR / "data" / "retrieval_eval_cases.json"
GENERATION_KEYWORDS_PATH = MODULE_DIR / "data" / "generation_eval_keywords.json"
RETRIEVAL_DATASET = "interviews-eval/retrieval"
GENERATION_DATASET = "interviews-eval/generation"
RAG_TASKS = ("retrieval", "generation", "ranking")
ARMS = ("A", "B", "C")
LABELS = ("X", "Y", "Z")
RECALL_K = 5
# The filter-only baseline is random by design; averaging over a fixed set of orderings makes it comparable run to run.
BASELINE_SEEDS = [uuid.UUID(int=seed) for seed in range(1, 21)]
SWEEP_THRESHOLDS = [0.0, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
# Every simulated answer is the same neutral one, so the questions differ only because of the arm.
CANNED_ANSWER = "I would start from the requirements, compare two options, and explain the trade-off I chose."
MIN_CASES = 15
REQUIRED_KINDS = {"synonym": 3, "vague": 1, "role_boundary": 1}


CaseKind = Literal["plain", "synonym", "vague", "role_boundary"]


class RetrievalCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    # synonym: names a competency in other words; vague: says little; role_boundary: sits between two roles.
    kind: CaseKind
    role: JobRole
    level: Level
    query: str
    expected: list[str] = Field(min_length=1)


class SheetError(Exception):
    """The grading file can't be read; the message starts with the line and gives the reason."""


class Sheet(NamedTuple):
    text: str
    # setup id -> {label: arm}; kept apart from the sheet so the ranking stays blind.
    key: dict[str, dict[str, str]]
    # Setups where an arm failed to produce a full question set (left out, counted).
    excluded: list[str]


# Your 1-to-5 rating of one question set: fit, relevance (None for "-"), variety, specificity.
Rating = tuple[int, int | None, int, int]
RATING_NAMES = ("human_fit", "human_relevance", "human_variety", "human_specificity")


class RankingReport(NamedTuple):
    first: dict[str, int]
    graded: int
    # setup id -> labels best first; and, when filled in, each set's rating and note (setup -> label -> value).
    rankings: dict[str, list[str]]
    ratings: dict[str, dict[str, Rating]]
    notes: dict[str, dict[str, str]]


class WrittenQuestion(NamedTuple):
    # None when the reply broke the format or rules (the live app would ask the bank instead).
    question: str | None
    prompt_tokens: int | None


class ArmSummary(NamedTuple):
    questions: int
    valid: int
    distinct_competencies: float
    skill_coverage: float | None
    prompt_tokens: float
    start_ms: float


# --- retrieval metrics ---


def recall_at_k(ranked: Sequence[str], expected: Collection[str], k: int = RECALL_K) -> float:
    return len(set(ranked[:k]) & set(expected)) / len(expected)


def reciprocal_rank(ranked: Sequence[str], expected: Collection[str]) -> float:
    return next((1 / position for position, key in enumerate(ranked, start=1) if key in expected), 0.0)


def filter_baseline(
    eligible: Sequence[str], expected: Collection[str], seeds: Sequence[uuid.UUID], *, k: int = RECALL_K
) -> tuple[float, float]:
    """What filter mode alone would score: recall@k and reciprocal rank averaged over fixed seeded orderings."""
    orderings = [pick_filter_notes(eligible, seed, len(eligible)) for seed in seeds]
    return mean(recall_at_k(o, expected, k) for o in orderings), mean(reciprocal_rank(o, expected) for o in orderings)


def threshold_sweep(
    scored: Sequence[Sequence[tuple[str, float]]],
    expected: Sequence[Collection[str]],
    thresholds: Sequence[float],
    *,
    k: int = RECALL_K,
) -> list[tuple[float, float, float]]:
    """(threshold, mean recall@k, mean notes kept) per threshold: a higher threshold drops weak matches, and with
    them, sometimes, right ones."""
    rows = []
    for threshold in thresholds:
        kept = [[key for key, score in ranking if score >= threshold] for ranking in scored]
        rows.append(
            (
                threshold,
                mean(recall_at_k(keys, want, k) for keys, want in zip(kept, expected, strict=True)),
                mean(min(len(keys), k) for keys in kept),
            )
        )
    return rows


def case_set_problems(cases: Sequence[RetrievalCase]) -> list[str]:
    problems = []
    if len(cases) < MIN_CASES:
        problems.append(f"{len(cases)} labelled queries; at least {MIN_CASES} are needed")
    for kind, needed in REQUIRED_KINDS.items():
        found = sum(c.kind == kind for c in cases)
        if found < needed:
            problems.append(f"{found} {kind} queries; at least {needed} are needed")
    ids = [c.id for c in cases]
    problems += [f"duplicate case id {i!r}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    return problems


# --- generation metrics ---


def competencies_of(question: str, keywords: Mapping[str, Sequence[str]]) -> set[str]:
    text = question.lower()
    return {name for name, words in keywords.items() if any(word.lower() in text for word in words)}


def skill_coverage(questions: Sequence[str], skills: Sequence[str]) -> float | None:
    """The share of the job description's skills that at least one question mentions; None without listed skills."""
    if not skills:
        return None
    text = " ".join(questions).lower()
    return sum(skill.lower() in text for skill in skills) / len(skills)


def simulate_main_questions(
    llm: LLMProvider,
    *,
    role: JobRole,
    level: Level,
    interview_type: InterviewType,
    question_count: int,
    job_description: str | None,
    notes: Sequence[ReferenceNote],
    max_tokens: int,
) -> list[WrittenQuestion]:
    """One interview's main questions through the streamed writer's text format (the same prompt for every arm, v5
    or v6), with a canned neutral answer between them and no decide call or follow-ups."""
    turns: list[QuestionTurn] = []
    written: list[WrittenQuestion] = []
    for _ in range(question_count):
        inputs = InterviewerInputs(
            role, level, interview_type, question_count, job_description, turns, reference_notes=notes
        )
        built = CONTEXT_MANAGER.build(INTERVIEWER_STREAM_TASK, inputs)
        try:
            result = llm.complete(
                built.messages,
                max_tokens=max_tokens,
                trace_labels={"task": INTERVIEWER_STREAM_TASK, "prompt_version": built.prompt_version},
            )
        except LLMError:
            written.append(WrittenQuestion(None, None))
            continue
        try:
            header = split_header(result.text, final=True)
            assert header is not None
            reply = parse_streamed_reply(
                header.text,
                interview_type=interview_type,
                earlier_questions=[t.question for t in turns],
                category=header.category,
            )
        except InvalidReplyError:
            written.append(WrittenQuestion(None, result.prompt_tokens))
            continue
        written.append(WrittenQuestion(reply.question, result.prompt_tokens))
        turns.append(QuestionTurn(reply.question, reply.category, CANNED_ANSWER))
    return written


def run_scores(
    run: Sequence[WrittenQuestion], keywords: Mapping[str, Sequence[str]], skills: Sequence[str]
) -> list[tuple[str, float]]:
    """One interview's keyword scores, for its Langfuse trace: the same rules the arm summary averages."""
    questions = [w.question for w in run if w.question]
    scores = [
        ("valid_share", len(questions) / len(run) if run else 0.0),
        ("distinct_competencies", float(len(set().union(*(competencies_of(q, keywords) for q in questions))))),
    ]
    coverage = skill_coverage(questions, skills)
    if coverage is not None:
        scores.append(("skill_coverage", coverage))
    return scores


def summarize_arm(
    interviews: Sequence[Sequence[WrittenQuestion]],
    keywords: Mapping[str, Sequence[str]],
    *,
    skills: Sequence[Sequence[str]],
    start_ms: Sequence[float],
) -> ArmSummary:
    valid = [[w.question for w in run if w.question] for run in interviews]
    coverages = [c for qs, s in zip(valid, skills, strict=True) if (c := skill_coverage(qs, s)) is not None]
    tokens = [w.prompt_tokens for run in interviews for w in run if w.prompt_tokens is not None]
    return ArmSummary(
        questions=sum(len(run) for run in interviews),
        valid=sum(len(qs) for qs in valid),
        distinct_competencies=mean(len(set().union(*(competencies_of(q, keywords) for q in qs))) for qs in valid),
        skill_coverage=mean(coverages) if coverages else None,
        prompt_tokens=mean(tokens) if tokens else 0.0,
        start_ms=mean(start_ms) if start_ms else 0.0,
    )


# --- the blind sheet ---


def build_sheet(
    sets: Mapping[str, Mapping[str, Sequence[str] | None]],
    *,
    seed: int,
    contexts: Mapping[str, Sequence[str]] | None = None,
) -> Sheet:
    """One block per setup with the three question sets under X/Y/Z in a seeded random order. A setup where an arm
    has no full set is left out (and listed), so every graded setup compares all three. `contexts` maps a setup to the
    lines you judge against (role, level, job description); they are quoted so they can never read as a ranking."""
    rng = random.Random(seed)
    lines = [
        "# Blind ranking",
        "For each setup, rank the three question sets from best to worst on the Ranking line, e.g. `Ranking: Y > X > Z`.",
        "Judge each set against the setup's role, level and job description (the quoted lines under its heading).",
        (
            "Optional, under each set: `Rating:` four whole numbers from 1 to 5, in this order: fit (role and level), "
            "relevance (job description; `-` when there is none), variety, specificity, e.g. `Rating: 4 5 3 4`; and "
            "`Note:` one line on why you ranked it so."
        ),
        "",
    ]
    key: dict[str, dict[str, str]] = {}
    excluded = []
    for setup_id in sorted(sets):
        arms = sets[setup_id]
        if any(not arms.get(arm) for arm in ARMS):
            excluded.append(setup_id)
            continue
        order = list(ARMS)
        rng.shuffle(order)
        key[setup_id] = dict(zip(LABELS, order, strict=True))
        lines.append(f"## Setup {setup_id}")
        for context in (contexts or {}).get(setup_id, ()):
            lines.append(f"> {context}".rstrip())
        lines += ["", "Ranking:", ""]
        for label, arm in key[setup_id].items():
            lines.append(f"### {label}")
            lines += [f"{n}. {q}" for n, q in enumerate(arms[arm] or [], start=1)]
            lines += ["Rating:", "Note:", ""]
    return Sheet("\n".join(lines), key, excluded)


def read_rankings(text: str, key: Mapping[str, Mapping[str, str]]) -> RankingReport:
    """Every setup of the key must have one complete ranking; anything else, and any malformed rating, is refused with
    its line, so no partial report is ever printed and nothing is ever posted from a broken sheet. Ratings and notes
    are optional per set."""
    rankings: dict[str, list[str]] = {}
    ratings: dict[str, dict[str, Rating]] = {}
    notes: dict[str, dict[str, str]] = {}
    awaiting, setup_line = None, 0  # the setup whose Ranking line is still to come
    setup = label = None  # where a Rating or Note line belongs
    for number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## Setup "):
            awaiting = setup = line.removeprefix("## Setup ").strip()
            setup_line, label = number, None
            if setup not in key:
                raise SheetError(f"line {number}: unknown setup {setup!r}")
        elif line.startswith("Ranking:") and awaiting is not None:
            rankings[awaiting] = _ranking(number, line.removeprefix("Ranking:"), key[awaiting])
            awaiting = None
        elif line.startswith("### ") and setup is not None:
            label = line.removeprefix("### ").strip()
        elif line.startswith("Rating:") and setup is not None and label is not None:
            rating = _rating(number, line.removeprefix("Rating:"))
            if rating is not None:
                ratings.setdefault(setup, {})[label] = rating
        elif line.startswith("Note:") and setup is not None and label is not None:
            note = line.removeprefix("Note:").strip()
            if note:
                notes.setdefault(setup, {})[label] = note
    if awaiting is not None:
        raise SheetError(f"line {setup_line}: setup {awaiting!r} has no ranking")
    missing = [s for s in key if s not in rankings]
    if missing:
        raise SheetError(f"line {len(text.splitlines())}: no ranking for setup {', '.join(missing)}")
    first: dict[str, int] = dict.fromkeys(ARMS, 0)
    for setup_id, labels in rankings.items():
        first[key[setup_id][labels[0]]] += 1
    return RankingReport(first, len(rankings), rankings, ratings, notes)


def _rating(number: int, raw: str) -> Rating | None:
    """`fit relevance variety specificity`, whole numbers 1 to 5; relevance may be `-` (no job description). Blank:
    not rated."""
    parts = [part for part in re.split(r"[\s,]+", raw.strip()) if part]
    if not parts:
        return None
    problem = f"line {number}: a rating is four whole numbers from 1 to 5 (fit relevance variety specificity)"
    if len(parts) != 4:
        raise SheetError(problem)
    values: list[int | None] = []
    for position, part in enumerate(parts):
        if part == "-" and position == 1:
            values.append(None)
        elif part.isdigit() and 1 <= int(part) <= 5:
            values.append(int(part))
        else:
            raise SheetError(f"{problem}; relevance alone may be '-'")
    fit, relevance, variety, specificity = values
    assert fit is not None and variety is not None and specificity is not None
    return fit, relevance, variety, specificity


def _ranking(number: int, raw: str, labels: Mapping[str, str]) -> list[str]:
    ranked = [part.strip().upper() for part in raw.split(">") if part.strip()]
    if not ranked:
        raise SheetError(f"line {number}: no ranking")
    for label in ranked:
        if label not in labels:
            raise SheetError(f"line {number}: unknown label {label!r}")
    repeated = next((label for i, label in enumerate(ranked) if label in ranked[:i]), None)
    if repeated:
        raise SheetError(f"line {number}: repeated label {repeated!r}")
    if len(ranked) != len(labels):
        raise SheetError(f"line {number}: rank all three ({', '.join(labels)})")
    return ranked


# --- the runners (real calls) ---


def run_rag_task(
    args: argparse.Namespace, provider: LLMProvider | None, settings, tracer: Tracer | None = None
) -> int:
    if args.task == "ranking":
        # Reads your filled-in sheet (no model call), then posts your judgement onto each arm's Langfuse result.
        from app.core.ai.tracing import build_tracer

        tracer = tracer or build_tracer(settings, environment="eval")
        try:
            return run_ranking(Path(args.sheet), tracer=tracer)
        finally:
            tracer.close()
    from app.core.ai.factory import build_embedder, build_provider
    from app.core.ai.tracing import build_tracer

    configs = settings.llm_provider_configs
    model = args.model or (configs[0].model if configs else None)
    # Both record their runs in Langfuse (no-op without keys): retrieval as an experiment run, generation as traces.
    tracer = tracer or build_tracer(settings, environment="eval")
    if args.task == "generation" and provider is None:
        provider = build_provider(settings, model=args.model, tracer=tracer)
    try:
        embedder = build_embedder(settings)
        if embedder is None:
            print("Embeddings are not configured: set LLM_GOOGLE_API_KEY in .env first.")
            return 1
        with _session() as db:
            repo = KnowledgeRepository(db)
            if args.task == "retrieval":
                # Deterministic for fixed notes and embeddings: one run, whatever --repeat says.
                return run_retrieval(repo, embedder, tracer=tracer, pause=args.pause_seconds, note=args.note)
            if provider is None:
                print("LLM is not configured: set LLM_PROVIDERS and that vendor's LLM_<VENDOR>_* settings in .env first.")
                return 1
            return run_generation(args, provider, embedder, repo, settings.llm_max_tokens, tracer=tracer, model=model)
    finally:
        tracer.close()


def _session():
    from app.db.session import SessionLocal

    return SessionLocal()


class RetrievalRow(NamedTuple):
    """One retrieval case's outcome: the ranking by meaning and its metrics, the filter baseline's, or an error."""

    case: RetrievalCase
    ranking: list[tuple[str, float]]
    vector_recall: float
    vector_rr: float
    filter_recall: float
    filter_rr: float
    error: str | None


def run_retrieval(
    repo: KnowledgeRepository,
    embedder: Embedder,
    *,
    tracer: Tracer,
    pause: float = 0.0,
    sleep: Callable[[float], None] = time.sleep,
    note: str | None = None,
    cases: Sequence[RetrievalCase] | None = None,
) -> int:
    """Rank the notes for every labelled query and score where the right note landed, as one Langfuse experiment
    run (console unchanged). Stops before any call when the label set breaks its rules or the notes aren't ready."""
    cases = list(cases) if cases is not None else _retrieval_cases()
    problems = case_set_problems(cases)
    for problem in problems:
        print(f"label set: {problem}")
    if problems:
        return 1
    active = _ready_notes(repo, embedder)
    if active is None:
        return 1
    position = itertools.count()

    def run_one(case: RetrievalCase) -> RetrievalRow:
        if next(position) and pause:
            sleep(pause)
        row = _retrieval_row(case, repo, embedder)
        _print_retrieval_row(row)
        return row

    fingerprint = notes_fingerprint(chunk.content_hash for chunk in active)
    description = run_description(note)
    rows, record = run_cases(
        tracer,
        dataset=RETRIEVAL_DATASET,
        cases=cases,
        item_of=retrieval_item,
        run_one=run_one,
        output_of=lambda case, row: {
            "kind": case.kind,
            "expected": case.expected,
            "top_notes": [{"note": key, "score": round(score, 4)} for key, score in row.ranking[:RECALL_K]],
            "error": row.error,
        },
        scores_of=_retrieval_scores,
        run_scores_of=retrieval_run_scores,
        name="retrieval",
        # What a retrieval run tests is the threshold and the notes: the name says so, so runs can be told apart.
        run_name=run_name(
            "retrieval", run_stamp(), 1, label=f"threshold-{RETRIEVAL_MIN_SIMILARITY}/notes-{fingerprint[:6]}"
        ),
        metadata=run_metadata(
            task="retrieval",
            commit=git_commit() if tracer.enabled else "unknown",
            model=None,
            prompts={},
            repeat=1,
            flags={"recall_k": RECALL_K},
            extra={
                "embedding_model": embedder.model,
                "embedding_dimensions": embedder.dimensions,
                "threshold": RETRIEVAL_MIN_SIMILARITY,
                "notes_fingerprint": fingerprint,
                "note": description,
            },
        ),
        description=description,
    )
    totals = dict(retrieval_run_scores(rows))
    print(f"\nthreshold used: {RETRIEVAL_MIN_SIMILARITY}")
    print(f"vector: recall@5={totals['vector_recall_at_5']:.3f} MRR={totals['vector_mrr']:.3f}")
    print(f"filter: recall@5={totals['filter_recall_at_5']:.3f} MRR={totals['filter_mrr']:.3f}  ({len(BASELINE_SEEDS)} orderings)")
    print("\nthreshold  recall@5  kept")
    sweep = threshold_sweep([row.ranking for row in rows], [set(row.case.expected) for row in rows], SWEEP_THRESHOLDS)
    for threshold, recall, kept in sweep:
        print(f"{threshold:>9.2f}  {recall:>8.3f}  {kept:>4.1f}")
    print(f"\n{final_line([record], enabled=tracer.enabled)}")
    return 0


def _retrieval_cases() -> list[RetrievalCase]:
    return TypeAdapter(list[RetrievalCase]).validate_json(RETRIEVAL_CASES_PATH.read_text(encoding="utf-8"))


def _ready_notes(repo: KnowledgeRepository, embedder: Embedder) -> list[Any] | None:
    """The active notes, or None after saying how to fix the database or the ingest (no call is made either way)."""
    try:
        active = repo.active_chunks()
    except SQLAlchemyError:
        print("The database is not reachable: start it with `docker compose up -d`, then run the eval again.")
        return None
    if not active:
        print(
            "No notes are ingested: run `uv run python -m app.modules.interviews.tooling.interviews_knowledge_ingest` "
            "first."
        )
        return None
    if not any(chunk.embedding_model == embedder.model for chunk in active):
        print(f"The ingested notes were embedded with another model, not {embedder.model}: run the ingest again.")
        return None
    return active


def retrieval_item(case: RetrievalCase) -> dict[str, Any]:
    """A labelled query as a dataset item: what is searched, and the notes that should come back."""
    return {
        "id": f"retrieval:{case.id}",
        "input": {"query": case.query, "role": case.role.value, "level": case.level.value},
        "expected_output": {"notes": case.expected},
        "metadata": {"kind": case.kind},
    }


def _retrieval_row(case: RetrievalCase, repo: KnowledgeRepository, embedder: Embedder) -> RetrievalRow:
    eligible = [c.note_key for c in repo.eligible_chunks(case.role, case.level)]
    base = filter_baseline(eligible, case.expected, BASELINE_SEEDS)
    try:
        [vector] = embedder.embed([case.query], kind=EmbeddingKind.query).vectors
    except LLMError as exc:
        return RetrievalRow(case, [], 0.0, 0.0, *base, error=type(exc).__name__)
    nearest = repo.nearest_chunks(case.role, case.level, embedder.model, vector, len(eligible))
    ranking = [(chunk.note_key, score) for chunk, score in nearest]
    keys = [key for key, score in ranking if score >= RETRIEVAL_MIN_SIMILARITY]
    return RetrievalRow(
        case, ranking, recall_at_k(keys, case.expected), reciprocal_rank(keys, case.expected), *base, error=None
    )


def _print_retrieval_row(row: RetrievalRow) -> None:
    case = row.case
    vector = (
        f"ERROR: {row.error}" if row.error else f"vector recall@5={row.vector_recall:.2f} rr={row.vector_rr:.2f}"
    )
    print(f"{case.id:<24} {case.kind:<14} {vector}  filter recall@5={row.filter_recall:.2f} rr={row.filter_rr:.2f}")


def _retrieval_scores(row: RetrievalRow) -> list[Score]:
    return [
        ("vector_recall_at_5", row.vector_recall, None),
        ("vector_reciprocal_rank", row.vector_rr, None),
        ("filter_recall_at_5", row.filter_recall, None),
        ("filter_reciprocal_rank", row.filter_rr, None),
        ("errored", row.error is not None, row.error),
    ]


def retrieval_run_scores(rows: Sequence[RetrievalRow]) -> list[tuple[str, float]]:
    """The run's averages, as the console prints them: an errored case counts as a miss."""
    return [
        ("vector_recall_at_5", mean(r.vector_recall for r in rows)),
        ("vector_mrr", mean(r.vector_rr for r in rows)),
        ("filter_recall_at_5", mean(r.filter_recall for r in rows)),
        ("filter_mrr", mean(r.filter_rr for r in rows)),
        ("errored_count", sum(r.error is not None for r in rows)),
    ]


class ArmInterview(NamedTuple):
    """One arm's main questions for one setup: the notes it got, what it wrote, retrieval time, the skills looked for."""

    notes: tuple[str, ...]
    questions: list[WrittenQuestion]
    start_ms: float
    skills: list[str]


def run_generation(
    args: argparse.Namespace,
    provider: LLMProvider,
    embedder: Embedder,
    repo: KnowledgeRepository,
    max_tokens: int,
    *,
    tracer: Tracer,
    model: str | None = None,
) -> int:
    """Every setup written three ways (arm A no notes, B filter notes, C vector notes); per repeat, each arm is one
    Langfuse experiment run of the setups, so the arms sit side by side. The console table, the blind sheet and its
    key are unchanged; a third local file maps each setup and arm to its result, so ranking can post your rank."""
    from ..tooling.interviews_evals import EVAL_CASES_PATH, load_cases

    data = json.loads(GENERATION_KEYWORDS_PATH.read_text(encoding="utf-8"))
    by_id = {c.id: c for c in load_cases(EVAL_CASES_PATH) if c.id in data["setups"]}
    setups = [by_id[setup_id] for setup_id in sorted(by_id)]
    active = _ready_notes(repo, embedder)
    if active is None:
        return 1
    fingerprint = notes_fingerprint(chunk.content_hash for chunk in active)
    commit = git_commit() if tracer.enabled else "unknown"
    stamp, description = run_stamp(), run_description(args.note)
    items = {c.id: generation_item(c, data["setups"][c.id]) for c in setups}
    results: dict[str, list[list[WrittenQuestion]]] = {arm: [] for arm in ARMS}
    starts: dict[str, list[float]] = {arm: [] for arm in ARMS}
    sets: dict[str, dict[str, Sequence[str] | None]] = {}
    traces: dict[str, dict[str, str]] = {}
    records: list[ExperimentRun | None] = []
    for repeat in range(1, args.repeat + 1):
        for arm in ARMS:
            prompt = INTERVIEWER_V5_PROMPT_VERSION if arm == "A" else INTERVIEWER_V6_PROMPT_VERSION

            def run_one(case, arm: str = arm, repeat: int = repeat) -> ArmInterview:
                session_id = uuid.uuid5(uuid.NAMESPACE_URL, f"{case.id}/{repeat}")
                notes, start_ms = _arm_notes(arm, case, repo, embedder, session_id, tracer)
                questions = simulate_main_questions(
                    provider,
                    role=case.setup.role,
                    level=case.setup.level,
                    interview_type=case.setup.interview_type,
                    question_count=case.setup.question_count,
                    job_description=case.job_description,
                    notes=notes,
                    max_tokens=max_tokens,
                )
                time.sleep(args.pause_seconds)
                return ArmInterview(tuple(n.competency for n in notes), questions, start_ms, data["setups"][case.id])

            rows, record = run_cases(
                tracer,
                dataset=GENERATION_DATASET,
                cases=setups,
                item_of=lambda case: items[case.id],
                run_one=run_one,
                output_of=lambda _case, row: {
                    "notes": list(row.notes),
                    "questions": [w.question for w in row.questions],
                    "start_ms": round(row.start_ms),
                },
                scores_of=lambda row: _generation_scores(row, data["competencies"]),
                run_scores_of=lambda rows: generation_run_scores(rows, data["competencies"]),
                name="generation",
                run_name=run_name("generation", stamp, repeat, arm, label=f"{prompt}/{model or 'default-model'}"),
                metadata=run_metadata(
                    task="generation",
                    commit=commit,
                    model=model,
                    prompts={"interviewer": prompt},
                    repeat=repeat,
                    flags={"max_tokens": max_tokens, "pause_seconds": args.pause_seconds, "seed": args.seed},
                    extra={
                        "arm": arm,
                        "embedding_model": embedder.model,
                        "embedding_dimensions": embedder.dimensions,
                        "threshold": RETRIEVAL_MIN_SIMILARITY,
                        "notes_fingerprint": fingerprint,
                        "note": description,
                    },
                ),
                description=description,
            )
            records.append(record)
            for case, row in zip(setups, rows, strict=True):
                results[arm].append(row.questions)
                starts[arm].append(row.start_ms)
                if repeat == 1:
                    questions = [w.question for w in row.questions]
                    sets.setdefault(case.id, {})[arm] = None if None in questions else [q for q in questions if q]
                    if record is not None and (trace_id := record.trace_ids.get(f"generation:{case.id}")):
                        traces.setdefault(case.id, {})[arm] = trace_id
    skills = [data["setups"][c.id] for _ in range(args.repeat) for c in setups]
    baseline = None
    print("arm  questions  valid  competencies  skill_coverage  prompt_tokens  added_tokens  start_ms")
    for arm in ARMS:
        s = summarize_arm(results[arm], data["competencies"], skills=skills, start_ms=starts[arm])
        baseline = s.prompt_tokens if baseline is None else baseline
        coverage = "-" if s.skill_coverage is None else f"{s.skill_coverage:.2f}"
        print(f"{arm:<4} {s.questions:>9}  {s.valid:>5}  {s.distinct_competencies:>12.2f}  {coverage:>14}  "
              f"{s.prompt_tokens:>13.0f}  {s.prompt_tokens - baseline:>12.0f}  {s.start_ms:>8.0f}")  # fmt: skip
    sheet = build_sheet(sets, seed=args.seed, contexts={c.id: sheet_context(c) for c in setups})
    Path(args.sheet).write_text(sheet.text, encoding="utf-8")
    key_path = Path(args.sheet).with_suffix(".key.json")
    key_path.write_text(json.dumps(sheet.key, indent=2), encoding="utf-8")
    _write_traces(Path(args.sheet), traces)
    print(f"\nblind sheet: {args.sheet} ({len(sheet.key)} setups); key kept apart in {key_path}")
    if sheet.excluded:
        print(f"left out (an arm failed): {', '.join(sheet.excluded)}")
    line = final_line(records, enabled=tracer.enabled)
    if any(records):
        line += " Rank the sheet before opening these runs: they name the arm."
    print(f"\n{line}")
    return 0


def generation_item(case, skills: list[str]) -> dict[str, Any]:
    """A setup as a dataset item: the interview setup and job description, and the skills its questions should touch."""
    return {
        "id": f"generation:{case.id}",
        "input": case.model_dump(mode="json", include={"setup", "job_description"}),
        "expected_output": None,
        "metadata": {"skills": skills},
    }


def _generation_scores(row: ArmInterview, keywords: Mapping[str, Sequence[str]]) -> list[Score]:
    tokens = [w.prompt_tokens for w in row.questions if w.prompt_tokens is not None]
    # A question with no token count is a provider error (an invalid reply still counts its tokens).
    errored = any(w.prompt_tokens is None for w in row.questions)
    return [
        *((name, value, None) for name, value in run_scores(row.questions, keywords, row.skills)),
        ("prompt_tokens", mean(tokens) if tokens else 0.0, None),
        ("start_ms", row.start_ms, None),
        ("errored", errored, "a provider error on at least one question" if errored else None),
    ]


def generation_run_scores(rows: Sequence[ArmInterview], keywords: Mapping[str, Sequence[str]]) -> list[tuple[str, float]]:
    """One arm's averages over the setups, from the same per-setup scores Langfuse shows."""
    per_row = [{name: value for name, value, _ in _generation_scores(row, keywords)} for row in rows]
    scores = [
        (f"{name}_mean", mean(float(r[name]) for r in per_row))
        for name in ("valid_share", "distinct_competencies", "prompt_tokens", "start_ms")
    ]
    coverage = [float(r["skill_coverage"]) for r in per_row if "skill_coverage" in r]
    if coverage:
        scores.append(("skill_coverage_mean", mean(coverage)))
    scores.append(("errored_count", sum(bool(r["errored"]) for r in per_row)))
    return scores


def _write_traces(sheet: Path, traces: dict[str, dict[str, str]]) -> None:
    """The sheet's third file: setup, then arm, then the Langfuse trace of that arm's result. A stale one from an
    earlier run is removed when nothing was recorded, so ranking can never post onto the wrong run."""
    path = sheet.with_suffix(".traces.json")
    if traces:
        path.write_text(json.dumps(traces, indent=2), encoding="utf-8")
    else:
        path.unlink(missing_ok=True)


def sheet_context(case) -> list[str]:
    """What a ranker judges the questions against: the interview's setup and the full job description (never the arm)."""
    setup = case.setup
    lines = [
        f"**Role:** {setup.role} | **Level:** {setup.level} | **Type:** {setup.interview_type} | "
        + f"**Questions:** {setup.question_count}"
    ]
    if case.job_description:
        lines += ["**Job description:**", *case.job_description.strip().splitlines()]
    else:
        lines.append("**Job description:** none given (judge on role and level only)")
    return lines


def _arm_notes(arm: str, case, repo: KnowledgeRepository, embedder: Embedder, session_id: uuid.UUID, tracer: Tracer):
    """A: no notes. B: filter mode (no job description given to retrieval). C: vector mode on the job description."""
    if arm == "A":
        return (), 0.0
    service = RetrievalService(repo, embedder, llm_on=True, tracer=tracer)
    start = time.monotonic()
    found = service.retrieve(
        session_id,
        case.setup.role,
        case.setup.level,
        summary=None,
        job_description=case.job_description if arm == "C" else None,
    )
    return tuple(found.notes), (time.monotonic() - start) * 1000


def run_ranking(sheet_path: Path, *, tracer: Tracer) -> int:
    """Read your filled-in sheet, print how often each arm ranked first, then post your judgement to each arm's
    result in Langfuse: `human_rank` (1 = best), and for a rated set the four rubric scores and their mean
    `human_score`; a set's note becomes the comment on its rank. Every score has a stable id, so reading the sheet
    again updates rather than duplicates. A refused sheet posts nothing."""
    key = json.loads(sheet_path.with_suffix(".key.json").read_text(encoding="utf-8"))
    try:
        report = read_rankings(sheet_path.read_text(encoding="utf-8"), key)
    except SheetError as exc:
        print(f"grading file refused: {exc}")
        return 1
    print(f"graded setups: {report.graded}")
    for arm in ARMS:
        print(f"arm {arm} ranked first: {report.first[arm]}")
    print(f"\n{_post_judgements(report, key, sheet_path.with_suffix('.traces.json'), tracer)}")
    return 0


def _post_judgements(
    report: RankingReport, key: Mapping[str, Mapping[str, str]], traces_path: Path, tracer: Tracer
) -> str:
    """Post every rank (and rating) to its arm's result; returns the line saying what was posted and what was not."""
    if not tracer.enabled:
        return "Langfuse: nothing posted (no LANGFUSE keys set)."
    if not traces_path.exists():
        return f"Langfuse: nothing posted (no traces file {traces_path.name}: the generation run was not recorded)."
    traces = json.loads(traces_path.read_text(encoding="utf-8"))
    ranks = rated = unrecorded = rejected = 0
    for setup, labels in report.rankings.items():
        for position, label in enumerate(labels, start=1):
            trace_id = traces.get(setup, {}).get(key[setup][label])
            if not trace_id:
                unrecorded += 1
                continue
            note = report.notes.get(setup, {}).get(label)
            sent = [tracer.score(trace_id, "human_rank", float(position), comment=note, score_id=f"human_rank-{trace_id}")]
            rating = report.ratings.get(setup, {}).get(label)
            if rating is not None:
                given = [(name, value) for name, value in zip(RATING_NAMES, rating, strict=True) if value is not None]
                sent += [tracer.score(trace_id, name, float(value), score_id=f"{name}-{trace_id}") for name, value in given]
                mean_value = mean(value for _, value in given)
                sent.append(tracer.score(trace_id, "human_score", mean_value, score_id=f"human_score-{trace_id}"))
                rated += 1
            if all(sent):
                ranks += 1
            else:
                rejected += 1
    parts = [f"Langfuse: posted {ranks} ranks" + (f" and {rated} ratings" if rated else "")]
    if unrecorded:
        parts.append(f"{unrecorded} not posted (no recorded result)")
    if rejected:
        parts.append(f"{rejected} not posted (Langfuse rejected them; see the warnings above)")
    return "; ".join(parts) + "."
