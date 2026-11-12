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
import json
import random
import time
import uuid
from collections.abc import Callable, Collection, Mapping, Sequence
from datetime import UTC, datetime
from pathlib import Path
from statistics import mean
from typing import Literal, NamedTuple

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter

from app.core.ai.embedder import Embedder, EmbeddingKind
from app.core.ai.provider import LLMError, LLMProvider
from app.core.ai.tracing import Tracer

from ..ai.interviews_context import CONTEXT_MANAGER, InterviewerInputs
from ..ai.interviews_reply import InvalidReplyError, parse_streamed_reply, split_header
from ..constants.interviews_constants import (
    INTERVIEWER_STREAM_TASK,
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

RETRIEVAL_CASES_PATH = MODULE_DIR / "data" / "retrieval_eval_cases.json"
GENERATION_KEYWORDS_PATH = MODULE_DIR / "data" / "generation_eval_keywords.json"
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


class RankingReport(NamedTuple):
    first: dict[str, int]
    graded: int


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
            lines.append("")
    return Sheet("\n".join(lines), key, excluded)


def read_rankings(text: str, key: Mapping[str, Mapping[str, str]]) -> RankingReport:
    """Every setup of the key must have one complete ranking; anything else is refused with its line, so no partial
    report is ever printed."""
    rankings: dict[str, list[str]] = {}
    setup, setup_line = None, 0
    for number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## Setup "):
            setup, setup_line = line.removeprefix("## Setup ").strip(), number
            if setup not in key:
                raise SheetError(f"line {number}: unknown setup {setup!r}")
        elif line.startswith("Ranking:") and setup is not None:
            rankings[setup] = _ranking(number, line.removeprefix("Ranking:"), key[setup])
            setup = None
    if setup is not None:
        raise SheetError(f"line {setup_line}: setup {setup!r} has no ranking")
    missing = [s for s in key if s not in rankings]
    if missing:
        raise SheetError(f"line {len(text.splitlines())}: no ranking for setup {', '.join(missing)}")
    first: dict[str, int] = dict.fromkeys(ARMS, 0)
    for setup_id, labels in rankings.items():
        first[key[setup_id][labels[0]]] += 1
    return RankingReport(first, len(rankings))


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
        # Reads your filled-in sheet: no model call at all.
        return _run_ranking(Path(args.sheet))
    from app.core.ai.factory import build_embedder, build_provider
    from app.core.ai.tracing import build_tracer
    from app.db.session import SessionLocal

    configs = settings.llm_provider_configs
    model = args.model or (configs[0].model if configs else None)
    if args.task == "generation":
        # Generation calls go to Langfuse under environment "eval", like the other eval tasks (no-op without keys).
        tracer = tracer or build_tracer(settings, environment="eval")
        if provider is None:
            provider = build_provider(settings, model=args.model, tracer=tracer)
    try:
        embedder = build_embedder(settings)
        if embedder is None:
            print("Embeddings are not configured: set LLM_GOOGLE_API_KEY in .env first.")
            return 1
        with SessionLocal() as db:
            repo = KnowledgeRepository(db)
            if args.task == "retrieval":
                return _run_retrieval(repo, embedder, pause=args.pause_seconds, sleep=time.sleep)
            if provider is None:
                print("LLM is not configured: set LLM_PROVIDERS and that vendor's LLM_<VENDOR>_* settings in .env first.")
                return 1
            return _run_generation(args, provider, embedder, repo, settings.llm_max_tokens, tracer=tracer, model=model)
    finally:
        if tracer is not None:
            tracer.close()


def _run_retrieval(
    repo: KnowledgeRepository, embedder: Embedder, *, pause: float, sleep: Callable[[float], None]
) -> int:
    cases = TypeAdapter(list[RetrievalCase]).validate_json(RETRIEVAL_CASES_PATH.read_text(encoding="utf-8"))
    problems = case_set_problems(cases)
    for problem in problems:
        print(f"label set: {problem}")
    if problems:
        return 1
    scored, expected, rows = [], [], []
    for i, case in enumerate(cases):
        if i and pause:
            sleep(pause)
        eligible = [c.note_key for c in repo.eligible_chunks(case.role, case.level)]
        [vector] = embedder.embed([case.query], kind=EmbeddingKind.query).vectors
        ranking = [(c.note_key, s) for c, s in repo.nearest_chunks(case.role, case.level, embedder.model, vector, len(eligible))]
        keys = [key for key, score in ranking if score >= RETRIEVAL_MIN_SIMILARITY]
        base = filter_baseline(eligible, case.expected, BASELINE_SEEDS)
        rows.append((recall_at_k(keys, case.expected), reciprocal_rank(keys, case.expected), *base))
        scored.append(ranking)
        expected.append(set(case.expected))
        print(f"{case.id:<24} {case.kind:<14} vector recall@5={rows[-1][0]:.2f} rr={rows[-1][1]:.2f}  "
              f"filter recall@5={base[0]:.2f} rr={base[1]:.2f}")  # fmt: skip
    print(f"\nthreshold used: {RETRIEVAL_MIN_SIMILARITY}")
    print(f"vector: recall@5={mean(r[0] for r in rows):.3f} MRR={mean(r[1] for r in rows):.3f}")
    print(f"filter: recall@5={mean(r[2] for r in rows):.3f} MRR={mean(r[3] for r in rows):.3f}  ({len(BASELINE_SEEDS)} orderings)")
    print("\nthreshold  recall@5  kept")
    for threshold, recall, kept in threshold_sweep(scored, expected, SWEEP_THRESHOLDS):
        print(f"{threshold:>9.2f}  {recall:>8.3f}  {kept:>4.1f}")
    return 0


def _run_generation(
    args: argparse.Namespace,
    provider: LLMProvider,
    embedder: Embedder,
    repo: KnowledgeRepository,
    max_tokens: int,
    *,
    tracer: Tracer | None = None,
    model: str | None = None,
) -> int:
    from ..tooling.interviews_evals import EVAL_CASES_PATH, EVAL_USER, load_cases

    tracer = tracer or Tracer(None)
    # Every trace of this run shares one Langfuse session, named by what was run and when.
    label = f"generation/{model or 'default'}/{datetime.now(UTC):%Y%m%d-%H%M%S}"
    data = json.loads(GENERATION_KEYWORDS_PATH.read_text(encoding="utf-8"))
    cases = {c.id: c for c in load_cases(EVAL_CASES_PATH) if c.id in data["setups"]}
    results: dict[str, list[list[WrittenQuestion]]] = {arm: [] for arm in ARMS}
    starts: dict[str, list[float]] = {arm: [] for arm in ARMS}
    skills: list[list[str]] = []
    sets: dict[str, dict[str, Sequence[str] | None]] = {}
    for setup_id, case in sorted(cases.items()):
        for repeat in range(1, args.repeat + 1):
            skills.append(data["setups"][setup_id])
            for arm in ARMS:
                with tracer.trace(
                    f"generation: {setup_id} arm {arm}",
                    user_id=EVAL_USER,
                    session_id=label,
                    input=_generation_input(case, arm),
                    tags=["task:generation", f"model:{model or 'default'}", f"arm:{arm}"],
                    metadata={"case_id": setup_id, "repeat": str(repeat), "arm": arm},
                ) as trace_id:
                    session_id = uuid.uuid5(uuid.NAMESPACE_URL, f"{setup_id}/{repeat}")
                    notes, start_ms = _arm_notes(arm, case, repo, embedder, session_id, tracer)
                    run = simulate_main_questions(
                        provider,
                        role=case.setup.role,
                        level=case.setup.level,
                        interview_type=case.setup.interview_type,
                        question_count=case.setup.question_count,
                        job_description=case.job_description,
                        notes=notes,
                        max_tokens=max_tokens,
                    )
                    tracer.set_trace_output(
                        {"notes": [n.competency for n in notes], "questions": [w.question for w in run]}
                    )
                for name, value in run_scores(run, data["competencies"], data["setups"][setup_id]):
                    tracer.score(trace_id, name, value)
                results[arm].append(run)
                starts[arm].append(start_ms)
                if repeat == 1:
                    questions = [w.question for w in run]
                    sets.setdefault(setup_id, {})[arm] = None if None in questions else [q for q in questions if q]
                time.sleep(args.pause_seconds)
    baseline = None
    print("arm  questions  valid  competencies  skill_coverage  prompt_tokens  added_tokens  start_ms")
    for arm in ARMS:
        s = summarize_arm(results[arm], data["competencies"], skills=skills, start_ms=starts[arm])
        baseline = s.prompt_tokens if baseline is None else baseline
        coverage = "-" if s.skill_coverage is None else f"{s.skill_coverage:.2f}"
        print(f"{arm:<4} {s.questions:>9}  {s.valid:>5}  {s.distinct_competencies:>12.2f}  {coverage:>14}  "
              f"{s.prompt_tokens:>13.0f}  {s.prompt_tokens - baseline:>12.0f}  {s.start_ms:>8.0f}")  # fmt: skip
    sheet = build_sheet(sets, seed=args.seed, contexts={sid: sheet_context(c) for sid, c in cases.items()})
    Path(args.sheet).write_text(sheet.text, encoding="utf-8")
    key_path = Path(args.sheet).with_suffix(".key.json")
    key_path.write_text(json.dumps(sheet.key, indent=2), encoding="utf-8")
    print(f"\nblind sheet: {args.sheet} ({len(sheet.key)} setups); key kept apart in {key_path}")
    if sheet.excluded:
        print(f"left out (an arm failed): {', '.join(sheet.excluded)}")
    if tracer.enabled:
        print(f"\nLangfuse session: {label} (rank the sheet first: the traces name each arm)")
    return 0


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


def _generation_input(case, arm: str) -> dict:
    """What the trace list shows for one arm's interview: the setup and the start of the job description."""
    setup = case.setup
    return {
        "arm": arm,
        "role": setup.role,
        "level": setup.level,
        "interview_type": setup.interview_type,
        "question_count": setup.question_count,
        "job_description": (case.job_description or "")[:300] or None,
    }


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


def _run_ranking(sheet_path: Path) -> int:
    key = json.loads(sheet_path.with_suffix(".key.json").read_text(encoding="utf-8"))
    try:
        report = read_rankings(sheet_path.read_text(encoding="utf-8"), key)
    except SheetError as exc:
        print(f"grading file refused: {exc}")
        return 1
    print(f"graded setups: {report.graded}")
    for arm in ARMS:
        print(f"arm {arm} ranked first: {report.first[arm]}")
    return 0
