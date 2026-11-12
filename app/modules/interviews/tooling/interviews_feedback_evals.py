"""Opt-in evals for end-of-interview feedback (`interviews_evals --task feedback`): labelled interviews, scored by the
real model through the same steps the API runs, checked against expected bands.

Run:  uv run python -m app.modules.interviews.tooling.interviews_evals --task feedback --repeat 5 --model gemini-3.5-flash-lite
It costs real calls (two per case and repeat), so it never runs in `uv run pytest`; the checks are unit-tested with a
fake grader. A good score has no single right value, but a band does: a strong answer should land high, a weak one low,
an injected order must not move it, and the same answer should score lower at a higher level. With `--repeat N` the run
also reports the spread: how far a criterion's score moves when nothing changes but the dice (starting target: 1).

With Langfuse keys set, each case and repeat is one trace (environment "eval", the run's tags), its checks are boolean
scores, the spread is a numeric score on each case's last trace, and the cases are mirrored into the dataset
`interviews-eval/feedback`. The cases are synthetic, so their answers may go to Langfuse; real interviews never do here.
"""

import argparse
import time
import uuid
from collections import Counter
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import Any, Literal, Self, TypedDict

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, model_validator

from app.core.ai.context import ContextManager
from app.core.ai.provider import LLMProvider, LLMResult
from app.core.ai.tracing import ExperimentRun, Tracer

from ..ai.interviews_context import (
    CONTEXT_MANAGER,
    FeedbackScoreInputs,
    FeedbackWriteInputs,
)
from ..ai.interviews_feedback import (
    FeedbackThread,
    ThreadTurn,
    assess_evidence,
    compute_overall,
    stored_scores,
)
from ..ai.interviews_feedback_turn import FeedbackGenerator, hint_for
from ..constants.interviews_constants import (
    CATEGORY_CRITERIA,
    FEEDBACK_SCORE_PROMPT_VERSION,
    FEEDBACK_WRITE_PROMPT_VERSION,
    MODULE_DIR,
    SCORE_MAX,
    SCORE_MIN,
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
    QuestionKind,
    TextSource,
)
from ..tooling.interviews_evals import DATASET_PREFIX, Check
from .interviews_eval_runs import (
    final_line,
    run_cases,
    run_description,
    run_metadata,
    run_name,
)

FEEDBACK_EVAL_CASES_PATH = MODULE_DIR / "data" / "feedback_eval_cases.json"
FEEDBACK_DATASET = f"{DATASET_PREFIX}/feedback"
# Starting target from the spec: a criterion's score moves at most this much across repeats. Tuned after real runs.
SPREAD_TARGET = 1
# The same answers at a higher level must score at least this much lower overall. The bands alone can't show it: they
# overlap, so a real run's senior 4.4 against the junior's 4.5 was reported only as the senior being out of band.
LEVEL_GAP = 0.5


class Band(BaseModel):
    model_config = ConfigDict(extra="forbid")

    low: float = Field(ge=SCORE_MIN, le=SCORE_MAX)
    high: float = Field(ge=SCORE_MIN, le=SCORE_MAX)

    @model_validator(mode="after")
    def _ordered(self) -> Self:
        if self.low > self.high:
            raise ValueError("low must not be above high")
        return self

    def holds(self, value: float) -> bool:
        return self.low <= value <= self.high

    def __str__(self) -> str:
        return f"{self.low:g}-{self.high:g}"


class FeedbackEvalSetup(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: JobRole
    level: Level
    interview_type: InterviewType


class FeedbackEvalTurn(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: str
    answer: str
    kind: QuestionKind = QuestionKind.main


class FeedbackEvalQuestion(BaseModel):
    """One main question with its follow-ups, as the score call sees a thread."""

    model_config = ConfigDict(extra="forbid")

    category: QuestionCategory
    turns: list[FeedbackEvalTurn] = Field(min_length=1)


class FeedbackEvalCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    kind: Literal[
        "strong",
        "weak",
        "mixed",
        "injection_answer",
        "injection_job_description",
        "near_empty",
        "voice",
        "level_junior",
        "level_senior",
        "follow_up",
    ]
    setup: FeedbackEvalSetup
    job_description: str | None = None
    questions: list[FeedbackEvalQuestion] = Field(min_length=1)
    # What a sound grader gives: an overall band, or "too little to assess" (then no scores at all).
    expect_overall: Band | None = None
    expect_insufficient: bool = False
    # "<main number>:<criterion>" -> band, only where the answer makes it clear.
    expect_criteria: dict[str, Band] = Field(default_factory=dict)
    # An earlier case with the same answers at a lower level: this case's overall must be LEVEL_GAP below its overall.
    lower_than: str | None = None
    notes: str = ""

    @model_validator(mode="after")
    def _labels_fit_the_case(self) -> Self:
        if (self.expect_overall is None) == (not self.expect_insufficient):
            raise ValueError("a case expects either an overall band or an insufficient result")
        for key in self.expect_criteria:
            number, _, criterion = key.partition(":")
            if not number.isdigit() or not 1 <= int(number) <= len(self.questions):
                raise ValueError(f"{key}: no such main question")
            category = self.questions[int(number) - 1].category
            if criterion not in {c.value for c in CATEGORY_CRITERIA[category]}:
                raise ValueError(f"{key}: not a criterion of a {category.value} question")
        return self

    def threads(self) -> list[FeedbackThread]:
        return [
            FeedbackThread(
                number,
                q.category,
                q.turns[0].question,
                tuple(ThreadTurn(t.question, t.answer, t.kind) for t in q.turns),
            )
            for number, q in enumerate(self.questions, start=1)
        ]


class FeedbackCaseResult(BaseModel):
    case_id: str
    checks: list[Check]
    # The score call's failure code (no scores at all), as the API would store it.
    error: str | None = None
    insufficient: bool = False
    overall: float | None = None
    # "<main number>:<criterion>" -> score.
    scores: dict[str, int] = Field(default_factory=dict)
    text_source: TextSource | None = None
    # Why the template wrote the text (the write call's failure code), when it did.
    write_failure: str | None = None
    quotes_rejected: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    latency_ms: int = 0
    finish_length: int = 0

    @property
    def passed(self) -> bool:
        return self.error is None and all(c.passed for c in self.checks)


class FeedbackSummary(BaseModel):
    passed: int
    total: int
    check_failures: dict[str, int]
    # The score call produced valid scores (or a valid "not enough evidence").
    valid: int
    insufficient: int
    quotes_rejected: int
    overall_in_band: int
    overall_labelled: int
    template_texts: int
    prompt_tokens: int
    completion_tokens: int
    average_latency_ms: int
    finish_length: int


def load_feedback_cases(path: Path) -> list[FeedbackEvalCase]:
    cases = TypeAdapter(list[FeedbackEvalCase]).validate_json(path.read_bytes())
    seen: set[str] = set()
    for case in cases:
        # Earlier only: the pair is checked as soon as the later case has run, within the same repeat.
        if case.lower_than is not None and case.lower_than not in seen:
            raise ValueError(f"{case.id}: lower_than must name an earlier case, got {case.lower_than!r}")
        seen.add(case.id)
    return cases


def level_gap_check(
    case: FeedbackEvalCase, result: FeedbackCaseResult, earlier: dict[str, FeedbackCaseResult]
) -> Check | None:
    """The pair's check, or None when there is nothing to compare: no pair, or either side has no overall (an error or
    "not enough evidence"), which is reported on its own and is not a level problem."""
    other = earlier.get(case.lower_than) if case.lower_than else None
    if other is None or other.overall is None or result.overall is None:
        return None
    gap = round(other.overall - result.overall, 1)
    passed = gap >= LEVEL_GAP
    detail = "" if passed else f"{result.overall} vs {other.case_id} {other.overall}: gap {gap:g}, needs {LEVEL_GAP:g}"
    return Check(name="level_gap", passed=passed, detail=detail)


def check_feedback(
    case: FeedbackEvalCase,
    *,
    insufficient: bool,
    overall: float | None = None,
    scores: dict[str, int] | None = None,
    quotes_rejected: int = 0,
    text_source: TextSource | None = None,
    write_failure: str | None = None,
) -> list[Check]:
    """The case's labels against what came out. Check names stay stable: Langfuse compares runs by them."""
    if case.expect_insufficient:
        return [Check(name="insufficient", passed=insufficient, detail="" if insufficient else "it was scored")]
    if insufficient or overall is None:
        return [Check(name="enough_evidence", passed=False, detail="not enough evidence")]
    assert case.expect_overall is not None
    scores = scores or {}
    checks = [
        Check(name="enough_evidence", passed=True),
        _band_check("overall_in_band", case.expect_overall, overall),
    ]
    checks += [_band_check(f"criterion:{key}", band, scores.get(key)) for key, band in case.expect_criteria.items()]
    checks.append(
        Check(name="quotes_verified", passed=quotes_rejected == 0, detail=f"{quotes_rejected} rejected" if quotes_rejected else "")
    )
    written_by_llm = text_source == TextSource.llm
    checks.append(
        Check(
            name="write_valid",
            passed=written_by_llm,
            detail="" if written_by_llm else f"template used ({write_failure or 'unknown'})",
        )
    )
    return checks


def _band_check(name: str, band: Band, value: float | None) -> Check:
    passed = value is not None and band.holds(value)
    return Check(name=name, passed=passed, detail="" if passed else f"{value} not in {band}")


def run_feedback_case(
    provider: LLMProvider,
    case: FeedbackEvalCase,
    *,
    score_max_tokens: int,
    write_max_tokens: int,
    score_temperature: float,
    budget_seconds: float,
    context: ContextManager = CONTEXT_MANAGER,
    clock: Callable[[], float] = time.monotonic,
    tracer: Tracer | None = None,
) -> FeedbackCaseResult:
    """One case through the same pre-check, score call, write call and template fallback the API runs."""
    threads = case.threads()
    if not assess_evidence(threads):
        return FeedbackCaseResult(case_id=case.id, insufficient=True, checks=check_feedback(case, insufficient=True))
    generator = FeedbackGenerator(
        provider,
        context,
        score_max_tokens=score_max_tokens,
        write_max_tokens=write_max_tokens,
        score_temperature=score_temperature,
        clock=clock,
        tracer=tracer,
    )
    session_id = uuid.uuid5(uuid.NAMESPACE_URL, f"feedback-eval:{case.id}")
    deadline = generator.deadline(budget_seconds)
    setup = case.setup
    scored = generator.score(
        session_id,
        FeedbackScoreInputs(setup.role, setup.level, setup.interview_type, case.job_description, threads),
        deadline,
    )
    usage = _usage(scored.results)
    if scored.result is None:
        return FeedbackCaseResult(
            case_id=case.id, checks=[], error=scored.failure, quotes_rejected=scored.quotes_rejected, **usage
        )
    if not scored.result.enough_evidence:
        return FeedbackCaseResult(
            case_id=case.id, insufficient=True, checks=check_feedback(case, insufficient=True), **usage
        )
    overall = compute_overall(scored.result.questions)
    written = generator.write(
        session_id,
        FeedbackWriteInputs(
            setup.role, setup.level, setup.interview_type, overall, stored_scores(threads, scored.result.questions)
        ),
        [t.main_number for t in threads],
        deadline,
    )
    text_source = TextSource.llm if written.text is not None else TextSource.template
    scores = {f"{q.main_number}:{c.value}": v for q in scored.result.questions for c, v in q.scores.items()}
    return FeedbackCaseResult(
        case_id=case.id,
        checks=check_feedback(
            case,
            insufficient=False,
            overall=overall,
            scores=scores,
            quotes_rejected=scored.quotes_rejected,
            text_source=text_source,
            write_failure=written.failure,
        ),
        overall=overall,
        scores=scores,
        text_source=text_source,
        write_failure=written.failure,
        quotes_rejected=scored.quotes_rejected,
        **_usage([*scored.results, *written.results]),
    )


class _Usage(TypedDict):
    """The four usage fields of FeedbackCaseResult, so `**_usage(...)` is checked field by field."""

    prompt_tokens: int
    completion_tokens: int
    latency_ms: int
    finish_length: int


def _usage(results: Sequence[LLMResult]) -> _Usage:
    return {
        "prompt_tokens": sum(r.prompt_tokens or 0 for r in results),
        "completion_tokens": sum(r.completion_tokens or 0 for r in results),
        "latency_ms": sum(r.latency_ms for r in results),
        "finish_length": sum(r.finish_reason == "length" for r in results),
    }


def summarize_feedback(results: Sequence[FeedbackCaseResult]) -> FeedbackSummary:
    in_band = [c for r in results for c in r.checks if c.name == "overall_in_band"]
    return FeedbackSummary(
        passed=sum(r.passed for r in results),
        total=len(results),
        check_failures=dict(Counter(c.name for r in results for c in r.checks if not c.passed)),
        valid=sum(r.error is None for r in results),
        insufficient=sum(r.insufficient for r in results),
        quotes_rejected=sum(r.quotes_rejected for r in results),
        overall_in_band=sum(c.passed for c in in_band),
        overall_labelled=len(in_band),
        template_texts=sum(r.text_source == TextSource.template for r in results),
        prompt_tokens=sum(r.prompt_tokens for r in results),
        completion_tokens=sum(r.completion_tokens for r in results),
        average_latency_ms=round(sum(r.latency_ms for r in results) / len(results)) if results else 0,
        finish_length=sum(r.finish_length for r in results),
    )


def criterion_spread(runs: Sequence[Sequence[FeedbackCaseResult]]) -> dict[str, int]:
    """Per case: the largest gap between the highest and lowest score any one criterion got across the repeats that
    scored it. Cases scored in fewer than two repeats have no spread."""
    seen: dict[str, dict[str, list[int]]] = {}
    for results in runs:
        for r in results:
            for key, value in r.scores.items():
                seen.setdefault(r.case_id, {}).setdefault(key, []).append(value)
    return {
        case_id: max(max(v) - min(v) for v in keys.values())
        for case_id, keys in seen.items()
        if any(len(v) > 1 for v in keys.values())
    }


# --- Langfuse ---


def _verdict(result: FeedbackCaseResult) -> str:
    if result.error:
        return f"ERROR: {result.error}"
    failed = [f"{c.name}({c.detail})" if c.detail else c.name for c in result.checks if not c.passed]
    return f"FAIL: {', '.join(failed)}" if failed else "PASS"


# Where to look first when a feedback case fails a check, like the decide and write tasks' hints. Rules of thumb that
# narrow the search; they are not a diagnosis.
_CHECK_HINTS = {
    "overall_in_band": (
        "The overall is outside the expected band: compare the per-criterion scores with the rubric anchors. If the "
        "scores are fair, the band is wrong (fix the case); if not, tighten the prompt or the rubric's level line."
    ),
    "criterion": (
        "A criterion's score is outside its band: read that criterion's anchors and the case's notes, then the "
        "evidence reason the model gave for it in the score generation's output."
    ),
    "quotes_verified": (
        "A quote was rejected on the first attempt and the retry passed: compare the rejected quote with the answer; "
        "frequent rejections cost a call each and point at the evidence rule."
    ),
    "level_gap": (
        "The same answers did not score clearly lower at the higher level: compare both cases' per-criterion scores. "
        "The levels should differ on the criteria whose experienced line asks for more (depth, trade-offs)."
    ),
    "insufficient": (
        "Expected 'not enough evidence', but the interview was scored: check the code pre-check's thresholds "
        "(15 words, half the main questions) against the case's answers."
    ),
    "enough_evidence": (
        "Expected scores, but the code pre-check or the model found too little to assess: count the words of each "
        "main answer, then read the model's enough_evidence rule in the prompt."
    ),
}


def feedback_hints_for(result: FeedbackCaseResult) -> list[str]:
    """Where to look first for each failed check (or the error), in the order the checks ran."""
    if result.error:
        hint = hint_for(result.error)
        return [hint] if hint else []
    hints: list[str] = []
    for check in result.checks:
        if check.passed:
            continue
        if check.name == "write_valid":
            hint = hint_for(result.write_failure)
        else:
            hint = _CHECK_HINTS.get(check.name.split(":", 1)[0])
        if hint and hint not in hints:
            hints.append(hint)
    return hints


def feedback_dataset_items(cases: Sequence[FeedbackEvalCase]) -> list[dict[str, Any]]:
    """The cases as dataset items: the interview as input, the bands as the expected output (stable ids, so a re-run
    replaces items instead of duplicating them)."""
    return [
        {
            "id": f"feedback:{case.id}",
            "input": case.model_dump(mode="json", include={"setup", "job_description", "questions"}),
            "expected_output": {
                "insufficient": case.expect_insufficient,
                "overall": case.expect_overall.model_dump() if case.expect_overall else None,
                "criteria": {key: band.model_dump() for key, band in case.expect_criteria.items()},
            },
            "metadata": {"kind": case.kind, "notes": case.notes},
        }
        for case in cases
    ]


def feedback_trace_output(case: FeedbackEvalCase, result: FeedbackCaseResult) -> dict[str, Any]:
    """What came out next to what was wanted: the verdict, the overall against its band, the scores."""
    return {
        "verdict": _verdict(result),
        "overall": result.overall,
        "expected_overall": case.expect_overall.model_dump() if case.expect_overall else None,
        "insufficient": result.insufficient,
        "scores": result.scores,
        "text_source": result.text_source,
        "quotes_rejected": result.quotes_rejected,
        "hints": feedback_hints_for(result),
        "notes": case.notes,
    }


def feedback_scores_for(result: FeedbackCaseResult) -> list[tuple[str, bool, str | None]]:
    """(name, value, comment) per check, plus `valid_reply` and `case_passed`. An errored case has no checks."""
    if result.error:
        return [("valid_reply", False, result.error), ("case_passed", False, _verdict(result))]
    scores = [("valid_reply", True, None)]
    scores += [(c.name, c.passed, c.detail or None) for c in result.checks]
    scores.append(("case_passed", result.passed, _verdict(result)))
    return scores


# --- the run (called by interviews_evals.main for --task feedback) ---


def run_feedback(
    args: argparse.Namespace,
    provider: LLMProvider,
    tracer: Tracer,
    settings: Any,
    *,
    model: str | None,
    commit: str,
    stamp: str,
) -> None:
    """Every case, in file order, once per repeat; each repeat is one Langfuse experiment run of the feedback dataset.
    The console is unchanged apart from its last line, which names the runs (or says why nothing was recorded)."""
    cases = load_feedback_cases(FEEDBACK_EVAL_CASES_PATH)
    print(
        f"feedback: score_max_tokens={settings.feedback_score_max_tokens} "
        f"write_max_tokens={settings.feedback_write_max_tokens} temperature={settings.feedback_score_temperature} "
        f"budget={settings.feedback_total_budget_seconds}s cases={len(cases)}\n"
    )
    item_by_case = dict(zip((c.id for c in cases), feedback_dataset_items(cases), strict=True))
    description = run_description(args.note)
    runs: list[list[FeedbackCaseResult]] = []
    records: list[ExperimentRun | None] = []
    for run in range(1, args.repeat + 1):
        print(f"=== run {run}/{args.repeat}")
        # Cases run in file order, so a later case of a level pair finds its earlier case here.
        earlier: dict[str, FeedbackCaseResult] = {}

        def run_one(case: FeedbackEvalCase, earlier: dict[str, FeedbackCaseResult] = earlier) -> FeedbackCaseResult:
            result = run_feedback_case(
                provider,
                case,
                score_max_tokens=settings.feedback_score_max_tokens,
                write_max_tokens=settings.feedback_write_max_tokens,
                score_temperature=settings.feedback_score_temperature,
                budget_seconds=settings.feedback_total_budget_seconds,
                tracer=tracer,
            )
            gap = level_gap_check(case, result, earlier)
            if gap is not None:
                result.checks.append(gap)
            earlier[case.id] = result
            _print_case(result)
            return result

        results, record = run_cases(
            tracer,
            dataset=FEEDBACK_DATASET,
            cases=cases,
            item_of=lambda case: item_by_case[case.id],
            run_one=run_one,
            output_of=feedback_trace_output,
            scores_of=lambda result: [*feedback_scores_for(result), ("errored", result.error is not None, result.error)],
            run_scores_of=feedback_run_scores,
            name="feedback",
            run_name=run_name("feedback", stamp, run, label=f"{FEEDBACK_SCORE_PROMPT_VERSION}/{model or 'default-model'}"),
            metadata=run_metadata(
                task="feedback",
                commit=commit,
                model=model,
                prompts={"score": FEEDBACK_SCORE_PROMPT_VERSION, "write": FEEDBACK_WRITE_PROMPT_VERSION},
                repeat=run,
                flags={
                    "score_max_tokens": settings.feedback_score_max_tokens,
                    "write_max_tokens": settings.feedback_write_max_tokens,
                    "score_temperature": settings.feedback_score_temperature,
                    "budget_seconds": settings.feedback_total_budget_seconds,
                },
                extra={"note": description},
            ),
            description=description,
        )
        records.append(record)
        runs.append(results)
        _print_summary(summarize_feedback(results))
    if args.repeat > 1:
        spread = criterion_spread(runs)
        _post_spread(tracer, records[-1], spread)
        over = sorted(case_id for case_id, value in spread.items() if value > SPREAD_TARGET)
        print(
            f"criterion spread max={max(spread.values(), default=0)} (target <= {SPREAD_TARGET}); "
            f"cases over target: {', '.join(over) or 'none'}"
        )
    print(f"\n{final_line(records, enabled=tracer.enabled)}")


def feedback_run_scores(results: Sequence[FeedbackCaseResult]) -> list[tuple[str, float]]:
    """The run-level numbers of a feedback run, from the summary the console prints."""
    summary = summarize_feedback(results)
    in_band = summary.overall_in_band / summary.overall_labelled if summary.overall_labelled else 0.0
    return [
        ("pass_rate", summary.passed / summary.total),
        ("valid_reply_rate", summary.valid / summary.total),
        ("overall_in_band_rate", in_band),
        ("quotes_rejected_count", summary.quotes_rejected),
        ("template_text_count", summary.template_texts),
        ("errored_count", sum(r.error is not None for r in results)),
    ]


def _post_spread(tracer: Tracer, last_run: ExperimentRun | None, spread: dict[str, int]) -> None:
    """Each case's spread on its result in the last run, with a stable id so a repost updates it."""
    if last_run is None:
        return
    for case_id, value in spread.items():
        trace_id = last_run.trace_ids.get(f"feedback:{case_id}")
        tracer.score(trace_id, "criterion_spread_max", float(value), score_id=f"criterion_spread_max-{trace_id}")


def _print_case(result: FeedbackCaseResult) -> None:
    print(f"{'PASS' if result.passed else 'FAIL'}  {result.case_id:<32} {_verdict(result)}")
    print(
        f"      overall={result.overall if result.overall is not None else '-'} insufficient={result.insufficient} "
        f"text={result.text_source or '-'} quotes_rejected={result.quotes_rejected} "
        f"tokens={result.prompt_tokens}/{result.completion_tokens} latency_ms={result.latency_ms}"
    )
    for hint in feedback_hints_for(result):
        print(f"      hint: {hint}")
    print()


def _print_summary(summary: FeedbackSummary) -> None:
    print(
        f"passed {summary.passed}/{summary.total}  valid replies {summary.valid}/{summary.total}  "
        f"overall in band {summary.overall_in_band}/{summary.overall_labelled}  insufficient {summary.insufficient}  "
        f"quotes rejected {summary.quotes_rejected}  template texts {summary.template_texts}"
    )
    print(
        f"failed checks: {summary.check_failures or 'none'}\n"
        f"tokens {summary.prompt_tokens} in / {summary.completion_tokens} out, avg latency "
        f"{summary.average_latency_ms} ms per case, finish=length {summary.finish_length}\n"
    )
