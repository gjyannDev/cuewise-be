"""The job-description summary eval (`--task summary`): fixed long job descriptions, condensed by the app's summary
call, checked by rules. Called by `interviews_evals.main`; never imported by the app.

A summary replaces the original text on every later call of the interview, so it must be a real condensation that
keeps what the interviewer needs. Four things are measured per case:
- `valid_summary`: the app's own `validate_summary` accepts it (not empty, shorter than the original, within the cap,
  no markup), so the app would use it;
- `facts_kept`: the case's must-keep facts (role, seniority, key skills) are all in it;
- `injection_ignored`: text inside the job description asking for a marker word did not get it into the summary;
- token usage and latency per case (numbers, not pass/fail), so a call-layer change can be compared on cost too.

Each repeat is one Langfuse experiment run of the dataset `interviews-eval/summary`, like the other tasks.
"""

import argparse
import re
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import Any, Literal, Self

from pydantic import BaseModel, ConfigDict, TypeAdapter, model_validator

from app.core.ai.chat import ChatModel
from app.core.ai.tracing import ExperimentRun, Tracer

from ..ai.interviews_reply import InvalidReplyError, validate_summary
from ..ai.interviews_summary import summarize_job_description
from ..constants.interviews_constants import (
    MODULE_DIR,
    SUMMARY_THRESHOLD,
    SUMMARY_TIME_CAP_SECONDS,
)
from ..constants.interviews_prompt_registry import SUMMARY_VERSION
from .interviews_eval_runs import (
    Score,
    final_line,
    run_cases,
    run_description,
    run_metadata,
    run_name,
)

SUMMARY_EVAL_CASES_PATH = MODULE_DIR / "data" / "summary_eval_cases.json"
SUMMARY_DATASET = "interviews-eval/summary"


class Check(BaseModel):
    name: str
    passed: bool
    detail: str = ""


class SummaryEvalCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    kind: Literal["plain", "boilerplate", "very_long", "injection"]
    job_description: str
    # Facts the summary must keep; `a|b` accepts either spelling. Matched as whole words, ignoring case.
    must_keep: list[str]
    # Injection cases: the word the injected text asks for; the summary must not contain it.
    marker: str | None = None
    notes: str = ""

    @model_validator(mode="after")
    def _fits_the_task(self) -> Self:
        if len(self.job_description) <= SUMMARY_THRESHOLD:
            raise ValueError(
                f"case {self.id}: the job description must be over the summary threshold"
            )
        if self.kind == "injection" and not self.marker:
            raise ValueError(f"case {self.id}: an injection case needs a marker")
        return self


class SummaryCaseResult(BaseModel):
    case_id: str
    checks: list[Check]
    error: str | None = None
    summary: str | None = None
    prompt_tokens: int = 0
    completion_tokens: int = 0
    reasoning_tokens: int = 0
    latency_ms: int = 0
    finish_reason: str | None = None

    @property
    def passed(self) -> bool:
        return self.error is None and all(c.passed for c in self.checks)


def load_summary_cases(path: Path) -> list[SummaryEvalCase]:
    return TypeAdapter(list[SummaryEvalCase]).validate_json(path.read_bytes())


def _has_fact(text: str, fact: str) -> bool:
    return any(
        re.search(rf"(?<!\w){re.escape(spelling)}(?!\w)", text, re.IGNORECASE)
        for spelling in fact.split("|")
    )


def check_summary(case: SummaryEvalCase, text: str) -> list[Check]:
    try:
        validate_summary(case.job_description, text)
        valid = Check(name="valid_summary", passed=True)
    except InvalidReplyError as exc:
        valid = Check(name="valid_summary", passed=False, detail=exc.reason)
    missing = [fact for fact in case.must_keep if not _has_fact(text, fact)]
    obeyed = bool(case.marker) and case.marker.casefold() in text.casefold()
    return [
        valid,
        Check(name="facts_kept", passed=not missing, detail=", ".join(missing)),
        Check(
            name="injection_ignored",
            passed=not obeyed,
            detail=(case.marker or "") if obeyed else "",
        ),
    ]


def run_summary_case(chat_model: ChatModel, case: SummaryEvalCase, *, max_tokens: int) -> SummaryCaseResult:
    """The app's own summary call (`summarize_job_description`, as `InterviewsService` makes it): same messages, token
    limit, time cap and labels. The checks read the model's reply itself, also when the app would reject it."""
    outcome = summarize_job_description(chat_model, case.job_description, max_tokens=max_tokens)
    result = outcome.result
    if result is None:
        error = outcome.error
        return SummaryCaseResult(
            case_id=case.id,
            checks=[],
            error=type(error).__name__ if error else "no_result",
            finish_reason=error.finish_reason if error else None,
        )
    return SummaryCaseResult(
        case_id=case.id,
        checks=check_summary(case, result.text),
        summary=result.text.strip(),
        prompt_tokens=result.prompt_tokens or 0,
        completion_tokens=result.completion_tokens or 0,
        reasoning_tokens=result.reasoning_tokens or 0,
        latency_ms=result.latency_ms,
        finish_reason=result.finish_reason,
    )


def _verdict(result: SummaryCaseResult) -> str:
    if result.error:
        return f"ERROR: {result.error}"
    failed = [
        f"{c.name}({c.detail})" if c.detail else c.name
        for c in result.checks
        if not c.passed
    ]
    return f"FAIL: {', '.join(failed)}" if failed else "PASS"


def summary_scores_for(result: SummaryCaseResult) -> list[Score]:
    """One boolean per check, then `case_passed` and `errored` (an errored case has no checks)."""
    scores: list[Score] = [(c.name, c.passed, c.detail or None) for c in result.checks]
    scores.append(("case_passed", result.passed, _verdict(result)))
    scores.append(("errored", result.error is not None, result.error))
    return scores


def summary_run_scores(results: Sequence[SummaryCaseResult]) -> list[tuple[str, float]]:
    """The run-level numbers, from the same values the console prints. Averages are over the cases that answered."""
    answered = [r for r in results if r.error is None] or [
        SummaryCaseResult(case_id="-", checks=[])
    ]
    return [
        ("pass_rate", sum(r.passed for r in results) / len(results)),
        ("errored_count", sum(r.error is not None for r in results)),
        ("avg_prompt_tokens", sum(r.prompt_tokens for r in answered) / len(answered)),
        (
            "avg_completion_tokens",
            sum(r.completion_tokens for r in answered) / len(answered),
        ),
        ("avg_latency_ms", sum(r.latency_ms for r in answered) / len(answered)),
    ]


def _dataset_items(cases: Sequence[SummaryEvalCase]) -> list[dict[str, Any]]:
    return [
        {
            "id": f"summary:{case.id}",
            "input": {"job_description": case.job_description},
            "expected_output": {"must_keep": case.must_keep, "marker": case.marker},
            "metadata": {"kind": case.kind, "notes": case.notes},
        }
        for case in cases
    ]


def _trace_output(case: SummaryEvalCase, result: SummaryCaseResult) -> dict[str, Any]:
    return {"verdict": _verdict(result), "summary": result.summary, "notes": case.notes}


def run_summary(
    args: argparse.Namespace,
    chat_model: ChatModel,
    tracer: Tracer,
    settings: Any,
    *,
    model: str | None,
    commit: str,
    stamp: str,
    wait: Callable[[], None],
) -> None:
    cases = load_summary_cases(SUMMARY_EVAL_CASES_PATH)
    max_tokens = settings.llm_max_tokens
    print(
        f"summary: max_tokens={max_tokens} time_cap={SUMMARY_TIME_CAP_SECONDS}s cases={len(cases)}\n"
    )
    item_by_case = dict(zip((c.id for c in cases), _dataset_items(cases), strict=True))
    description = run_description(args.note)
    records: list[ExperimentRun | None] = []
    rates: list[float] = []

    def run_one(case: SummaryEvalCase) -> SummaryCaseResult:
        wait()
        result = run_summary_case(chat_model, case, max_tokens=max_tokens)

        _print_case(case, result)
        return result

    for repeat in range(1, args.repeat + 1):
        print(f"=== run {repeat}/{args.repeat}")
        results, record = run_cases(
            tracer,
            dataset=SUMMARY_DATASET,
            cases=cases,
            item_of=lambda case: item_by_case[case.id],
            run_one=run_one,
            output_of=_trace_output,
            scores_of=summary_scores_for,
            run_scores_of=summary_run_scores,
            name="summary",
            run_name=run_name(
                "summary",
                stamp,
                repeat,
                label=f"{SUMMARY_VERSION}/{model or 'default-model'}",
            ),
            metadata=run_metadata(
                task="summary",
                commit=commit,
                model=model,
                prompts={"summary": SUMMARY_VERSION},
                repeat=repeat,
                flags={
                    "max_tokens": max_tokens,
                    "time_cap_seconds": SUMMARY_TIME_CAP_SECONDS,
                },
                extra={"note": description},
            ),
            description=description,
        )
        records.append(record)
        rates.append(sum(r.passed for r in results) / len(results))
        _print_summary(results)
    print(f"pass rate runs={', '.join(f'{rate:.2f}' for rate in rates)}")
    print(f"\n{final_line(records, enabled=tracer.enabled)}")


def _print_case(case: SummaryEvalCase, result: SummaryCaseResult) -> None:
    failed = [f"{c.name}({c.detail})" for c in result.checks if not c.passed]
    print(
        f"{'PASS' if result.passed else 'FAIL'}  {case.id:<36} {result.error or ', '.join(failed) or '-'}"
    )
    print(
        f"      tokens={result.prompt_tokens}/{result.completion_tokens} reasoning={result.reasoning_tokens} "
        f"latency_ms={result.latency_ms} finish={result.finish_reason or '-'}"
    )
    print(f"      summary={result.summary!r}\n")


def _print_summary(results: Sequence[SummaryCaseResult]) -> None:
    failures: dict[str, int] = {}
    for check in (c for r in results for c in r.checks if not c.passed):
        failures[check.name] = failures.get(check.name, 0) + 1
    scores = dict(summary_run_scores(results))
    print(
        f"passed {sum(r.passed for r in results)}/{len(results)}  failed checks: {failures or 'none'}  "
        f"errored {int(scores['errored_count'])}"
    )
    print(
        f"avg tokens {scores['avg_prompt_tokens']:.0f} in / {scores['avg_completion_tokens']:.0f} out, "
        f"avg latency {scores['avg_latency_ms']:.0f} ms\n"
    )
