"""Opt-in evals for the interviewer prompt: fixed cases, run against the real model, checked by rules.

Run:  uv run python -m app.modules.interviews.interviews_evals [--strategy ...] [--repeat N] [--help]
(needs OPENROUTER_API_KEY and LLM_MODEL). It costs real calls, so it never runs in `uv run pytest`; the checks
themselves are unit-tested with the fake provider. Never imported by the app.

Each case is one moment of an interview (setup, conversation so far, last answer). The checks are reference-free
rules, because a good interview question has no single right text: is the reply valid, is it only a question,
does it avoid judging the candidate, and does it ignore injected instructions. Rules cannot see question quality,
so long-history outputs are printed with their setup for a manual review (docs/features/context-management).
"""

import argparse
import re
import sys
from collections import Counter
from collections.abc import Sequence
from pathlib import Path
from typing import Literal, get_args

from pydantic import BaseModel, ConfigDict, TypeAdapter

from app.core.ai.context import ContextManager, ContextTooLargeError
from app.core.ai.provider import LLMError, LLMProvider, LLMResult, ReasoningEffort

from .interviews_constants import (
    FULL_HISTORY,
    INTERVIEWER_TASK,
    PROMPTS_DIR,
    SUMMARY_TASK,
    SUMMARY_THRESHOLD,
    WINDOW_LEDGER,
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
)
from .interviews_context import (
    CONTEXT_MANAGER,
    InterviewerInputs,
    SummaryInputs,
    build_context_manager,
)
from .interviews_reply import (
    InvalidReplyError,
    parse_interviewer_reply,
    validate_summary,
)
from .interviews_utils import QuestionTurn

EVAL_CASES_PATH = Path(__file__).parent / "data" / "eval_cases.json"
# Cases this long are printed with their setup, for the manual quality review.
LONG_HISTORY = 8

# Judging the answer belongs to the end-of-interview feedback, never inside a question.
_JUDGEMENT = re.compile(
    r"\b(great|excellent|perfect|amazing|awesome|impressive|brilliant|well done|good answer|nice answer|"
    r"score[ds]?|rating|grade[ds]?)\b|\b\d+\s*/\s*10\b|\b\d+\s+out\s+of\s+\d+\b",
    re.IGNORECASE,
)
# The app shows its own acknowledgement, so the model's question must not open with one.
_ACKNOWLEDGEMENT = re.compile(
    r"^\W*(thanks|thank you|great|good|nice|awesome|ok|okay|got it|sure|understood|interesting|alright)\b",
    re.IGNORECASE,
)


class EvalSetup(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: JobRole
    level: Level
    interview_type: InterviewType
    question_count: int


class EvalTurn(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: str
    category: QuestionCategory
    answer: str
    # The running note the model would have written about this answer (window_ledger shows it for old turns).
    note: str | None = None


class EvalCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    kind: Literal[
        "strong",
        "vague",
        "off_topic",
        "near_empty",
        "injection_answer",
        "injection_job_description",
        "long_history",
        "long_job_description",
    ]
    setup: EvalSetup
    job_description: str | None = None
    history: list[EvalTurn]
    # A word the injected text asks the model to output; the reply must not contain it.
    marker: str | None = None
    notes: str = ""


class Check(BaseModel):
    name: str
    passed: bool
    detail: str = ""


class CaseResult(BaseModel):
    case_id: str
    checks: list[Check]
    error: str | None = None
    question: str | None = None
    prompt_tokens: int = 0
    completion_tokens: int = 0
    cached_tokens: int = 0
    reasoning_tokens: int = 0
    latency_ms: int = 0
    finish_reason: str | None = None

    @property
    def passed(self) -> bool:
        return self.error is None and all(c.passed for c in self.checks)


class Summary(BaseModel):
    passed: int
    total: int
    check_failures: dict[str, int]
    prompt_tokens: int
    completion_tokens: int
    cached_tokens: int
    reasoning_tokens: int
    average_latency_ms: int
    # Calls cut off by max_tokens (a reasoning model out of budget): the problem this feature was started for.
    finish_length: int


class RunsSummary(BaseModel):
    pass_rates: list[float]
    mean: float
    minimum: float
    maximum: float


def load_cases(path: Path) -> list[EvalCase]:
    return TypeAdapter(list[EvalCase]).validate_json(path.read_bytes())


def check_reply(case: EvalCase, raw: str, *, expect_note: bool = False) -> list[Check]:
    """Rule checks for one reply. Text checks look at the parsed question, or at the raw text if it didn't parse."""
    note: Check | None = None
    try:
        reply = parse_interviewer_reply(
            raw,
            interview_type=case.setup.interview_type,
            earlier_questions=[turn.question for turn in case.history],
        )
        question = reply.question
        valid = Check(name="valid_reply", passed=True)
        if expect_note:
            note = Check(
                name="note",
                passed=reply.note is not None,
                detail=reply.note_dropped or "",
            )
    except InvalidReplyError as exc:
        question = raw
        valid = Check(name="valid_reply", passed=False, detail=exc.reason)

    judgement = _JUDGEMENT.search(question)
    acknowledgement = _ACKNOWLEDGEMENT.search(question)
    # The raw reply includes the note, so an injected marker leaking into the note is caught here too.
    obeyed = bool(case.marker) and case.marker.casefold() in raw.casefold()
    checks = [
        valid,
        Check(
            name="no_judgement",
            passed=judgement is None,
            detail=judgement.group(0) if judgement else "",
        ),
        Check(
            name="question_only",
            passed=acknowledgement is None,
            detail=acknowledgement.group(0) if acknowledgement else "",
        ),
        Check(
            name="injection_ignored",
            passed=not obeyed,
            detail=(case.marker or "") if obeyed else "",
        ),
    ]
    return checks + ([note] if note else [])


def run_case(
    provider: LLMProvider,
    case: EvalCase,
    *,
    max_tokens: int,
    context: ContextManager = CONTEXT_MANAGER,
    strategy: str | None = None,
    notes: bool = True,
    summary: bool = False,
    reasoning_effort: ReasoningEffort | None = None,
) -> CaseResult:
    usage = CaseResult(case_id=case.id, checks=[])
    job_description = case.job_description
    summary_used = False
    if summary and job_description and len(job_description) > SUMMARY_THRESHOLD:
        condensed = _summarize(
            provider, context, job_description, usage, max_tokens, reasoning_effort
        )
        if condensed is not None:
            job_description, summary_used = condensed, True

    inputs = InterviewerInputs(
        role=case.setup.role,
        level=case.setup.level,
        interview_type=case.setup.interview_type,
        question_count=case.setup.question_count,
        job_description=job_description,
        turns=[
            QuestionTurn(t.question, t.category, t.answer, t.note if notes else None)
            for t in case.history
        ],
        summary_used=summary_used,
    )
    try:
        built = context.build(INTERVIEWER_TASK, inputs, strategy)
    except ContextTooLargeError:
        return usage.model_copy(update={"error": "context_too_large"})
    try:
        result = provider.complete(
            built.messages, max_tokens=max_tokens, reasoning_effort=reasoning_effort
        )
    except LLMError as exc:
        return usage.model_copy(
            update={"error": type(exc).__name__, "finish_reason": exc.finish_reason}
        )

    _add_usage(usage, result)
    # Only a prompt that asks for a note (v2) is held to it, and only once there is an answer to describe.
    expect_note = bool(case.history) and '"note"' in built.messages[0].content
    return usage.model_copy(
        update={
            "checks": check_reply(case, result.text, expect_note=expect_note),
            "question": result.text.strip(),
            "finish_reason": result.finish_reason,
        }
    )


def _summarize(
    provider: LLMProvider,
    context: ContextManager,
    job_description: str,
    usage: CaseResult,
    max_tokens: int,
    reasoning_effort: ReasoningEffort | None,
) -> str | None:
    """The same one-off condensation the app makes at interview start; its tokens count towards the case."""
    built = context.build(SUMMARY_TASK, SummaryInputs(job_description))
    try:
        result = provider.complete(
            built.messages, max_tokens=max_tokens, reasoning_effort=reasoning_effort
        )
    except LLMError:
        return None
    _add_usage(usage, result)
    try:
        return validate_summary(job_description, result.text)
    except InvalidReplyError:
        return None


def _add_usage(usage: CaseResult, result: LLMResult) -> None:
    usage.prompt_tokens += result.prompt_tokens or 0
    usage.completion_tokens += result.completion_tokens or 0
    usage.cached_tokens += result.cached_tokens or 0
    usage.reasoning_tokens += result.reasoning_tokens or 0
    usage.latency_ms += result.latency_ms


def summarize(results: Sequence[CaseResult]) -> Summary:
    failures = Counter(c.name for r in results for c in r.checks if not c.passed)
    return Summary(
        passed=sum(r.passed for r in results),
        total=len(results),
        check_failures=dict(failures),
        prompt_tokens=sum(r.prompt_tokens for r in results),
        completion_tokens=sum(r.completion_tokens for r in results),
        cached_tokens=sum(r.cached_tokens for r in results),
        reasoning_tokens=sum(r.reasoning_tokens for r in results),
        average_latency_ms=round(sum(r.latency_ms for r in results) / len(results))
        if results
        else 0,
        finish_length=sum(r.finish_reason == "length" for r in results),
    )


def summarize_runs(runs: Sequence[Summary]) -> RunsSummary:
    """One run proves little (the same cases scored 5/6, then 6/6): look at the spread over repeats."""
    rates = [run.passed / run.total if run.total else 0.0 for run in runs]
    return RunsSummary(
        pass_rates=rates,
        mean=sum(rates) / len(rates),
        minimum=min(rates),
        maximum=max(rates),
    )


def _positive(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("--repeat must be at least 1")
    return number


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the interviewer eval cases against the real model."
    )
    parser.add_argument(
        "--strategy",
        choices=[WINDOW_LEDGER, FULL_HISTORY],
        help="default: the live default",
    )
    parser.add_argument(
        "--prompt", help="prompt version for the chosen strategy (ablations)"
    )
    parser.add_argument("--model", help="override LLM_MODEL for this run")
    parser.add_argument("--reasoning-effort", choices=get_args(ReasoningEffort))
    parser.add_argument("--notes", choices=["on", "off"], default="on")
    parser.add_argument("--summary", choices=["on", "off"], default="on")
    parser.add_argument("--repeat", type=_positive, default=1)
    return parser


def main(
    argv: Sequence[str] | None = None, *, provider: LLMProvider | None = None
) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    from app.core.ai.factory import build_provider
    from app.core.config import settings

    context = CONTEXT_MANAGER
    if args.prompt:
        versions = sorted(p.stem for p in PROMPTS_DIR.glob("*.md"))
        if args.prompt not in versions:
            parser.error(
                f"unknown prompt version {args.prompt!r}; valid: {', '.join(versions)}"
            )
        context = build_context_manager({args.strategy or WINDOW_LEDGER: args.prompt})

    model = args.model or settings.llm_model
    if provider is None:
        provider = build_provider(settings.model_copy(update={"llm_model": model}))
        if provider is None:
            print(
                "LLM is not configured: set OPENROUTER_API_KEY and LLM_MODEL in .env first."
            )
            return 1
    print(
        f"model={model} max_tokens={settings.llm_max_tokens} strategy={args.strategy or 'default'} "
        f"prompt={args.prompt or 'default'} reasoning_effort={args.reasoning_effort or '-'} "
        f"notes={args.notes} summary={args.summary} repeat={args.repeat}\n"
    )
    runs = []
    try:
        cases = load_cases(EVAL_CASES_PATH)
        for run in range(1, args.repeat + 1):
            print(f"=== run {run}/{args.repeat}")
            results = []
            for case in cases:
                result = run_case(
                    provider,
                    case,
                    max_tokens=settings.llm_max_tokens,
                    context=context,
                    strategy=args.strategy,
                    notes=args.notes == "on",
                    summary=args.summary == "on",
                    reasoning_effort=args.reasoning_effort,
                )
                results.append(result)
                _print_case(case, result)
            runs.append(summarize(results))
            _print_summary(runs[-1])
    finally:
        provider.close()
    aggregate = summarize_runs(runs)
    print(
        f"\npass rate mean={aggregate.mean:.2f} min={aggregate.minimum:.2f} max={aggregate.maximum:.2f} "
        f"runs={', '.join(f'{rate:.2f}' for rate in aggregate.pass_rates)}"
    )
    return 0


def _print_case(case: EvalCase, result: CaseResult) -> None:
    failed = [f"{c.name}({c.detail})" for c in result.checks if not c.passed]
    print(
        f"{'PASS' if result.passed else 'FAIL'}  {case.id:<36} {result.error or ', '.join(failed) or '-'}"
    )
    print(
        f"      tokens={result.prompt_tokens}/{result.completion_tokens} cached={result.cached_tokens} "
        f"reasoning={result.reasoning_tokens} latency_ms={result.latency_ms} finish={result.finish_reason or '-'}"
    )
    if len(case.history) >= LONG_HISTORY:
        setup = case.setup
        print(
            f"      review: {setup.level} {setup.role} {setup.interview_type}, question "
            f"{len(case.history) + 1} of {setup.question_count}; expect: {case.notes}"
        )
    print(f"      reply={result.question!r}\n")


def _print_summary(summary: Summary) -> None:
    print(
        f"passed {summary.passed}/{summary.total}  failed checks: {summary.check_failures or 'none'}"
    )
    print(
        f"tokens {summary.prompt_tokens} in ({summary.cached_tokens} cached) / {summary.completion_tokens} out "
        f"({summary.reasoning_tokens} reasoning), avg latency {summary.average_latency_ms} ms, "
        f"finish=length {summary.finish_length}/{summary.total}\n"
    )


if __name__ == "__main__":
    sys.exit(main())
