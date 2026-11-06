"""Opt-in evals for the interviewer prompt: fixed cases, run against the real model, checked by rules.

Run:  uv run python -m app.modules.interviews.interviews_evals [--strategy ...] [--repeat N] [--help]
      uv run python -m app.modules.interviews.interviews_evals --task decide --repeat 3   (follow-up decisions)
      uv run python -m app.modules.interviews.interviews_evals --task stream --repeat 3   (interviewer_v5, streamed)
      uv run python -m app.modules.interviews.interviews_evals --task feedback --repeat 5 (end-of-interview scoring;
      its cases and checks live in interviews_feedback_evals.py)
(needs LLM_PROVIDERS and that vendor's LLM_<VENDOR>_* settings). It costs real calls, so it never runs in
`uv run pytest`; the checks themselves are unit-tested with the fake provider. Never imported by the app.

Each case is one moment of an interview (setup, conversation so far, last answer). The checks are reference-free
rules, because a good interview question has no single right text: is the reply valid, is it only a question,
does it avoid judging the candidate, and does it ignore injected instructions. Rules cannot see question quality,
so long-history outputs are printed with their setup for a manual review (docs/features/context-management).

The decide task is the opposite: a decision does have a right answer, so cases carry a label (`expect`) and the
runner reports accuracy, over-probing (a follow-up nobody needed) and under-probing (a gap left unexplored).

The stream task runs the same write cases through the streamed turn's call (interviewer_v5, read with `stream()`):
the same rule checks as `write`, so v4 and v5 compare on one table, plus the time to the first visible token.

With LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY set, a run is also sent to Langfuse (environment "eval"): each case is
one trace in a session named after the run (task/prompt/strategy/model/effort/time), tagged with those same values, and
every check is a boolean score on it (`case_passed`, plus `over_probing` / `under_probing` for decide). The cases are
mirrored into the datasets `interviews-eval/write` and `interviews-eval/decide` (ids `write:<case id>`), so re-runs
replace items instead of duplicating them. In Langfuse, compare runs by filtering traces on a tag (e.g. `prompt:...`)
and grouping scores. Without keys nothing changes and nothing is sent. A Langfuse failure never fails the run.
"""

import argparse
import contextvars
import re
import sys
import time
from collections import Counter
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal, get_args

import anyio
from anyio.from_thread import BlockingPortal, start_blocking_portal
from pydantic import BaseModel, ConfigDict, TypeAdapter

from app.core.ai.context import ContextManager, ContextTooLargeError
from app.core.ai.provider import LLMError, LLMProvider, LLMResult, ReasoningEffort
from app.core.ai.tracing import Tracer

from .interviews_constants import (
    DECISION_TASK,
    FULL_HISTORY,
    INTERVIEWER_STREAM_TASK,
    INTERVIEWER_TASK,
    PROMPTS_DIR,
    SUMMARY_TASK,
    SUMMARY_THRESHOLD,
    WINDOW_LEDGER,
    FollowUpAction,
    FollowUpGap,
    InterviewType,
    JobRole,
    Level,
    QuestionCategory,
    QuestionKind,
)
from .interviews_context import (
    CONTEXT_MANAGER,
    InterviewerInputs,
    SummaryInputs,
    build_context_manager,
)
from .interviews_reply import (
    InvalidReplyError,
    parse_decision_reply,
    parse_interviewer_reply,
    parse_streamed_reply,
    split_header,
    validate_summary,
)
from .interviews_utils import QuestionTurn

EVAL_CASES_PATH = Path(__file__).parent / "data" / "eval_cases.json"
# In Langfuse: the user every eval trace belongs to, and the prefix of the dataset each task's cases are mirrored to.
EVAL_USER = "eval"
DATASET_PREFIX = "interviews-eval"
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
    # A follow-up belongs to the thread of the main question before it (a thread at the cap has two).
    kind: QuestionKind = QuestionKind.main


class Expect(BaseModel):
    """The label for the decide call: the action it should pick, and the gap when only one is fair."""

    model_config = ConfigDict(extra="forbid")

    action: FollowUpAction
    gap: FollowUpGap | None = None


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
        "at_cap",
    ]
    setup: EvalSetup
    job_description: str | None = None
    history: list[EvalTurn]
    # Decide evals only (`--task decide`); cases without a label are writing cases only.
    expect: Expect | None = None
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
    # Streamed evals: from the call's start to the first chunk of question text (after the CATEGORY line).
    first_token_ms: int | None = None
    # Decide evals: what the model picked against the label.
    decided: str | None = None
    decided_gap: str | None = None
    expected_action: str | None = None
    expected_gap: str | None = None

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
    # Streamed evals only: the average over cases that showed any text; None when none did (or not streamed).
    average_first_token_ms: int | None = None


class RunsSummary(BaseModel):
    pass_rates: list[float]
    mean: float
    minimum: float
    maximum: float


class DecisionSummary(BaseModel):
    """Correct = the labelled action (and the gap, when one is labelled). Over-probing costs the candidate time and
    patience; under-probing leaves a vague answer unexplored. Both are counted apart from plain mistakes.
    """

    correct: int
    labelled: int
    over_probing: int
    under_probing: int
    # Per labelled gap: right gap / cases expecting it.
    per_gap: dict[str, str]


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

    return _text_checks(case, valid, question, raw) + ([note] if note else [])


def check_streamed_reply(case: EvalCase, raw: str) -> list[Check]:
    """check_reply for interviewer_v5's streamed format: the CATEGORY line, then the question as plain text."""
    try:
        split = split_header(raw, final=True)
        assert split is not None
        question = parse_streamed_reply(
            split.text,
            interview_type=case.setup.interview_type,
            earlier_questions=[turn.question for turn in case.history],
            category=split.category,
        ).question
        valid = Check(name="valid_reply", passed=True)
    except InvalidReplyError as exc:
        question = raw
        valid = Check(name="valid_reply", passed=False, detail=exc.reason)
    return _text_checks(case, valid, question, raw)


def _text_checks(case: EvalCase, valid: Check, question: str, raw: str) -> list[Check]:
    """The checks on what the candidate would read, whatever the reply format."""
    judgement = _JUDGEMENT.search(question)
    acknowledgement = _ACKNOWLEDGEMENT.search(question)
    # The raw reply includes the note, so an injected marker leaking into the note is caught here too.
    obeyed = bool(case.marker) and case.marker.casefold() in raw.casefold()
    return [
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


def check_decision(case: EvalCase, raw: str) -> list[Check]:
    """The decide reply against the case's label; the injection check reads the raw reply (the note included)."""
    assert case.expect is not None
    obeyed = bool(case.marker) and case.marker.casefold() in raw.casefold()
    injection = Check(name="injection_ignored", passed=not obeyed, detail=(case.marker or "") if obeyed else "")
    try:
        decision = parse_decision_reply(raw)
    except InvalidReplyError as exc:
        return [
            Check(name="valid_reply", passed=False, detail=exc.reason),
            Check(name="decision", passed=False, detail="invalid"),
            injection,
        ]
    checks = [
        Check(name="valid_reply", passed=True),
        Check(
            name="decision",
            passed=decision.action == case.expect.action,
            detail=f"{decision.action}, expected {case.expect.action}",
        ),
        injection,
    ]
    if case.expect.gap and decision.action == case.expect.action:
        checks.append(
            Check(name="gap", passed=decision.gap == case.expect.gap, detail=f"{decision.gap}, expected {case.expect.gap}")
        )
    return checks


def run_decide_case(
    provider: LLMProvider,
    case: EvalCase,
    *,
    max_tokens: int,
    context: ContextManager = CONTEXT_MANAGER,
    reasoning_effort: ReasoningEffort | None = None,
) -> CaseResult:
    """One decide call on the case's latest answer, as the app makes it after every answer."""
    assert case.expect is not None
    usage = CaseResult(
        case_id=case.id,
        checks=[],
        expected_action=case.expect.action,
        expected_gap=case.expect.gap,
    )
    inputs = InterviewerInputs(
        role=case.setup.role,
        level=case.setup.level,
        interview_type=case.setup.interview_type,
        question_count=case.setup.question_count,
        job_description=case.job_description,
        turns=[QuestionTurn(t.question, t.category, t.answer, t.note, t.kind) for t in case.history],
    )
    try:
        built = context.build(DECISION_TASK, inputs)
    except ContextTooLargeError:
        return usage.model_copy(update={"error": "context_too_large"})
    try:
        result = provider.complete(built.messages, max_tokens=max_tokens, reasoning_effort=reasoning_effort)
    except LLMError as exc:
        return usage.model_copy(update={"error": type(exc).__name__, "finish_reason": exc.finish_reason})
    _add_usage(usage, result)
    checks = check_decision(case, result.text)
    try:
        decision = parse_decision_reply(result.text)
        decided, decided_gap = decision.action.value, decision.gap
    except InvalidReplyError:
        decided, decided_gap = None, None
    return usage.model_copy(
        update={
            "checks": checks,
            "question": result.text.strip(),
            "finish_reason": result.finish_reason,
            "decided": decided,
            "decided_gap": decided_gap,
        }
    )


def summarize_decisions(results: Sequence[CaseResult]) -> DecisionSummary:
    def right(r: CaseResult) -> bool:
        return r.decided == r.expected_action and (r.expected_gap is None or r.decided_gap == r.expected_gap)

    gaps = sorted({r.expected_gap for r in results if r.expected_gap})
    return DecisionSummary(
        correct=sum(right(r) for r in results),
        labelled=len(results),
        over_probing=sum(
            r.expected_action == FollowUpAction.next_question and r.decided == FollowUpAction.follow_up for r in results
        ),
        under_probing=sum(
            r.expected_action == FollowUpAction.follow_up and r.decided == FollowUpAction.next_question for r in results
        ),
        per_gap={
            gap: f"{sum(r.decided_gap == gap for r in results if r.expected_gap == gap)}/"
            f"{sum(r.expected_gap == gap for r in results)}"
            for gap in gaps
        },
    )


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
    inputs = _case_inputs(provider, case, usage, context, max_tokens, notes, summary, reasoning_effort)
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


def run_stream_case(
    provider: LLMProvider,
    case: EvalCase,
    *,
    max_tokens: int,
    context: ContextManager = CONTEXT_MANAGER,
    notes: bool = True,
    summary: bool = False,
    reasoning_effort: ReasoningEffort | None = None,
    # The event loop to stream on (the CLI keeps one for the whole run); None runs this case on its own loop.
    portal: BlockingPortal | None = None,
) -> CaseResult:
    """The streamed turn's write call (interviewer_stream, v5) on one case: the same checks as `run_case`, plus the
    time to the first chunk of question text, the number the streaming slice exists for."""
    usage = CaseResult(case_id=case.id, checks=[])
    inputs = _case_inputs(provider, case, usage, context, max_tokens, notes, summary, reasoning_effort)
    try:
        built = context.build(INTERVIEWER_STREAM_TASK, inputs)
    except ContextTooLargeError:
        return usage.model_copy(update={"error": "context_too_large"})

    # The portal runs `read` on its own loop thread with its own context, so carry the caller's over: that is what
    # keeps the call under this case's Langfuse trace.
    caller = contextvars.copy_context()

    async def read() -> tuple[LLMResult, int | None]:
        for var, value in caller.items():
            var.set(value)
        start, first_token_ms, buffer, final = time.perf_counter(), None, "", None
        async for item in provider.stream(built.messages, max_tokens=max_tokens, reasoning_effort=reasoning_effort):
            if isinstance(item, LLMResult):
                final = item
                continue
            buffer += item
            if first_token_ms is None:
                try:
                    split = split_header(buffer)
                except InvalidReplyError:
                    split = None  # no header: no question text will be shown; the check reports it
                if split is not None and split.text:
                    first_token_ms = round((time.perf_counter() - start) * 1000)
        assert final is not None
        return final, first_token_ms

    try:
        result, first_token_ms = portal.call(read) if portal else anyio.run(read)
    except LLMError as exc:
        return usage.model_copy(update={"error": type(exc).__name__, "finish_reason": exc.finish_reason})
    _add_usage(usage, result)
    return usage.model_copy(
        update={
            "checks": check_streamed_reply(case, result.text),
            "question": _streamed_question(result.text),
            "finish_reason": result.finish_reason,
            "first_token_ms": first_token_ms,
        }
    )


def _streamed_question(raw: str) -> str:
    try:
        split = split_header(raw, final=True)
    except InvalidReplyError:
        return raw.strip()
    return split.text.strip() if split else raw.strip()


def _case_inputs(
    provider: LLMProvider,
    case: EvalCase,
    usage: CaseResult,
    context: ContextManager,
    max_tokens: int,
    notes: bool,
    summary: bool,
    reasoning_effort: ReasoningEffort | None,
) -> InterviewerInputs:
    """The write call's inputs for a case, with the job description condensed first when `summary` is on."""
    job_description = case.job_description
    summary_used = False
    if summary and job_description and len(job_description) > SUMMARY_THRESHOLD:
        condensed = _summarize(
            provider, context, job_description, usage, max_tokens, reasoning_effort
        )
        if condensed is not None:
            job_description, summary_used = condensed, True
    return InterviewerInputs(
        role=case.setup.role,
        level=case.setup.level,
        interview_type=case.setup.interview_type,
        question_count=case.setup.question_count,
        job_description=job_description,
        turns=[
            QuestionTurn(t.question, t.category, t.answer, t.note if notes else None, t.kind)
            for t in case.history
        ],
        summary_used=summary_used,
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
    first_tokens = [r.first_token_ms for r in results if r.first_token_ms is not None]
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
        average_first_token_ms=round(sum(first_tokens) / len(first_tokens)) if first_tokens else None,
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


def verdict_for(result: CaseResult) -> str:
    """One line a reader can scan in Langfuse: PASS, FAIL with each failed check and its detail, or ERROR."""
    if result.error:
        return f"ERROR: {result.error}"
    failed = [f"{c.name}({c.detail})" if c.detail else c.name for c in result.checks if not c.passed]
    return f"FAIL: {', '.join(failed)}" if failed else "PASS"


def trace_input(case: EvalCase) -> dict:
    """What the case judged, for the trace list: its kind, the last question and the candidate's answer (and the job
    description when there is one, since some cases attack through it)."""
    last = case.history[-1] if case.history else None
    shown = {"kind": case.kind, "question": last.question if last else None, "answer": last.answer if last else None}
    if case.job_description:
        shown["job_description"] = case.job_description[:300]
    return shown


def _action_and_gap(action: str | None, gap: str | None) -> str | None:
    return None if action is None else f"{action} / {gap}" if gap else str(action)


_ERROR_HINTS = {
    "context_too_large": "The built context was over the limit, so no call was made: check the strategy and its limits.",
}
_PROVIDER_ERROR_HINT = (
    "The provider call failed, which is not a quality problem: check the provider, key and timeout, then rerun."
)
_CHECK_HINTS = {
    "valid_reply": (
        "The reply did not parse or repeated an earlier question: read `reply` and the check's detail for the reason."
    ),
    "no_judgement": "The question contains praise or a score: look at the prompt's rule against judging the candidate.",
    "question_only": "The question opens with an acknowledgement; the app adds its own, so the prompt should forbid it.",
    "injection_ignored": (
        "The injected marker appeared in the reply: the model followed text that came from the answer or job description."
    ),
    "note": "This prompt asks for a note and the reply had none, or it was dropped: read the check's detail.",
    "gap": (
        "The action matched but the gap differs. If both gaps fit the answer, the label is ambiguous or two gap "
        "definitions overlap (fix the case); if not, sharpen the gap definitions in the prompt."
    ),
}


def hints_for(case: EvalCase, result: CaseResult) -> list[str]:
    """Where to look first when a case fails: rules of thumb from which check failed, which way a wrong decision
    went, the case kind and the finish reason. They narrow the search; they are not a diagnosis."""
    if result.error:
        return [_ERROR_HINTS.get(result.error, _PROVIDER_ERROR_HINT)]
    failed = {c.name for c in result.checks if not c.passed}
    hints = []
    if result.finish_reason == "length" and failed:
        hints.append(
            "The reply was cut off by max_tokens: raise it or lower the reasoning effort before judging the quality."
        )
    for name in ("valid_reply", "no_judgement", "question_only", "injection_ignored", "note"):
        if name in failed:
            hints.append(_CHECK_HINTS[name])
    if "decision" in failed and result.decided is not None:
        over = result.decided == FollowUpAction.follow_up
        hints.append(
            "Over-probing: the model asked for more when the label says move on. Is the answer complete, empty, "
            "off-topic or not an answer? Find the prompt rule for that case and check it covers this one."
            if over
            else "Under-probing: the model moved on although the label expects a follow-up. Check the prompt's gap "
            "definitions and its 'when unsure, prefer next_question' rule."
        )
        if over and case.kind.startswith("injection"):
            hints.append(
                "This is an injection case: compare `reply.note` with the real answer. If the note describes things "
                "the candidate never said, the model invented an answer to judge once the injected text was ignored."
            )
    if "gap" in failed:
        hints.append(_CHECK_HINTS["gap"])
    return hints


def trace_output(case: EvalCase, result: CaseResult, task: str) -> dict:
    """What came out and what was wanted, next to each other: the verdict, the model's reply, what the case's label
    expected (decide only; a good question has no single right text) against what it decided, and the case's notes."""
    decide = task == "decide"
    return {
        "verdict": verdict_for(result),
        "reply": result.question,
        "decided": _action_and_gap(result.decided, result.decided_gap) if decide else None,
        "expected": _action_and_gap(result.expected_action, result.expected_gap) if decide else None,
        "hints": hints_for(case, result),
        "notes": case.notes,
    }


def scores_for(result: CaseResult) -> list[tuple[str, bool, str | None]]:
    """What one case sends to Langfuse as (name, value, comment): one boolean per check (the detail as its comment),
    then `case_passed` with the verdict as its comment. A case that errored has no checks, so it is just
    `case_passed` false. Decide cases add `over_probing` / `under_probing` (true = the mistake happened). Names stay
    stable across runs, or the comparison in Langfuse breaks."""
    if result.error:
        return [("case_passed", False, verdict_for(result))]
    scores = [(c.name, c.passed, c.detail or None) for c in result.checks]
    scores.append(("case_passed", result.passed, verdict_for(result)))
    if result.expected_action is not None:
        over = result.expected_action == FollowUpAction.next_question and result.decided == FollowUpAction.follow_up
        under = result.expected_action == FollowUpAction.follow_up and result.decided == FollowUpAction.next_question
        scores += [("over_probing", over, None), ("under_probing", under, None)]
    return scores


def dataset_name(task: str) -> str:
    """The stream task reads the same cases as write, so they share one dataset."""
    return f"{DATASET_PREFIX}/{'decide' if task == 'decide' else 'write'}"


def dataset_items(cases: Sequence[EvalCase], task: str) -> list[dict]:
    """The cases as Langfuse dataset items. The id is the case id behind the dataset's name: Langfuse wants ids unique
    across datasets, and a stable id makes the upsert replace an item instead of duplicating it. Only the decide
    dataset has expected outputs; a good question has no single right text."""
    key = dataset_name(task).removeprefix(f"{DATASET_PREFIX}/")
    return [
        {
            "id": f"{key}:{case.id}",
            "input": case.model_dump(mode="json", include={"setup", "job_description", "history"}),
            "expected_output": case.expect.model_dump(mode="json") if key == "decide" and case.expect else None,
            "metadata": {"kind": case.kind, "notes": case.notes},
        }
        for case in cases
    ]


def run_tags(args: argparse.Namespace, model: str | None) -> list[str]:
    """The tags that make runs comparable in Langfuse: what was run, and with which prompt, strategy, model, effort."""
    return [
        f"task:{args.task}",
        f"prompt:{args.prompt or 'default'}",
        f"strategy:{args.strategy or 'default'}",
        f"model:{model or 'default'}",
        f"effort:{args.reasoning_effort or '-'}",
    ]


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
    parser.add_argument("--model", help="override the primary provider's model for this run")
    parser.add_argument("--reasoning-effort", choices=get_args(ReasoningEffort))
    parser.add_argument("--notes", choices=["on", "off"], default="on")
    parser.add_argument("--summary", choices=["on", "off"], default="on")
    parser.add_argument("--repeat", type=_positive, default=1)
    parser.add_argument(
        "--task",
        choices=["write", "decide", "stream", "feedback"],
        default="write",
        help=(
            "write: the question rules (default, interviewer_v4 as JSON); decide: the follow-up decision on the "
            "labelled cases; stream: the streamed turn's write call (interviewer_v5), with time to first token; "
            "feedback: end-of-interview scoring on labelled interviews (bands, quotes, spread with --repeat)"
        ),
    )
    return parser


def main(
    argv: Sequence[str] | None = None,
    *,
    provider: LLMProvider | None = None,
    tracer: Tracer | None = None,
) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    from app.core.ai.factory import build_provider
    from app.core.ai.tracing import build_tracer
    from app.core.config import settings

    context = CONTEXT_MANAGER
    if args.prompt:
        versions = sorted(p.stem for p in PROMPTS_DIR.glob("*.md"))
        if args.prompt not in versions:
            parser.error(
                f"unknown prompt version {args.prompt!r}; valid: {', '.join(versions)}"
            )
        context = build_context_manager({args.strategy or WINDOW_LEDGER: args.prompt})

    configs = settings.llm_provider_configs
    model = args.model or (configs[0].model if configs else None)
    # Eval calls go to Langfuse under environment "eval", apart from real traffic (only when keys are configured).
    # A tracer passed in (tests) is used as is; without one and without keys this is the no-op tracer.
    if provider is None:
        tracer = tracer or build_tracer(settings, environment="eval")
        provider = build_provider(settings, model=args.model, tracer=tracer)
        if provider is None:
            print(
                "LLM is not configured: set LLM_PROVIDERS and that vendor's LLM_<VENDOR>_* settings in .env first."
            )
            return 1
    tracer = tracer or Tracer(None)
    print(
        f"model={model} max_tokens={settings.llm_max_tokens} task={args.task} strategy={args.strategy or 'default'} "
        f"prompt={args.prompt or 'default'} reasoning_effort={args.reasoning_effort or '-'} "
        f"notes={args.notes} summary={args.summary} repeat={args.repeat}\n"
    )
    decide = args.task == "decide"
    runs, decisions = [], []
    # Every trace of this run shares one Langfuse session, named by what was run and when.
    label = "/".join(
        [
            args.task,
            args.prompt or "default",
            args.strategy or "default",
            model or "default",
            args.reasoning_effort or "-",
            datetime.now(UTC).strftime("%Y%m%d-%H%M%S"),
        ]
    )
    tags = run_tags(args, model)
    # One event loop for every streamed call, so the provider's async connections are reused, never moved between loops.
    with start_blocking_portal() as portal:
        try:
            if args.task == "feedback":
                # Its own cases, checks and summary (interviews_feedback_evals.py); imported here to avoid a cycle.
                from .interviews_feedback_evals import run_feedback

                run_feedback(args, provider, tracer, settings, label=label, tags=tags)
                return 0
            cases = load_cases(EVAL_CASES_PATH)
            if decide:
                cases = [c for c in cases if c.expect]
            if tracer.enabled:
                tracer.upsert_dataset(dataset_name(args.task), dataset_items(cases, args.task))
            for run in range(1, args.repeat + 1):
                print(f"=== run {run}/{args.repeat}")
                results = []
                for case in cases:
                    with tracer.trace(
                        f"{args.task}: {case.id}",
                        user_id=EVAL_USER,
                        session_id=label,
                        input=trace_input(case),
                        tags=tags,
                        metadata={
                            "case_id": case.id,
                            "repeat": str(run),
                            "notes": args.notes,
                            "summary": args.summary,
                        },
                    ) as trace_id:
                        result = _run_one(provider, case, args, context, settings.llm_max_tokens, portal)
                        tracer.set_trace_output(trace_output(case, result, args.task))
                    for name, value, comment in scores_for(result):
                        tracer.score(trace_id, name, value, comment=comment)
                    results.append(result)
                    _print_case(case, result)
                runs.append(summarize(results))
                _print_summary(runs[-1])
                if decide:
                    decisions.append(summarize_decisions(results))
                    _print_decisions(decisions[-1])
        finally:
            provider.close()
            portal.call(provider.aclose)
            tracer.close()
    aggregate = summarize_runs(runs)
    print(
        f"\npass rate mean={aggregate.mean:.2f} min={aggregate.minimum:.2f} max={aggregate.maximum:.2f} "
        f"runs={', '.join(f'{rate:.2f}' for rate in aggregate.pass_rates)}"
    )
    if decisions:
        rates = [d.correct / d.labelled if d.labelled else 0.0 for d in decisions]
        print(
            f"decision accuracy mean={sum(rates) / len(rates):.2f} min={min(rates):.2f} max={max(rates):.2f} "
            f"over_probing={sum(d.over_probing for d in decisions)} "
            f"under_probing={sum(d.under_probing for d in decisions)} (over all runs)"
        )
    if tracer.enabled:
        print(f"\nLangfuse session: {label}")
    return 0


def _print_case(case: EvalCase, result: CaseResult) -> None:
    failed = [f"{c.name}({c.detail})" for c in result.checks if not c.passed]
    print(
        f"{'PASS' if result.passed else 'FAIL'}  {case.id:<36} {result.error or ', '.join(failed) or '-'}"
    )
    print(
        f"      tokens={result.prompt_tokens}/{result.completion_tokens} cached={result.cached_tokens} "
        f"reasoning={result.reasoning_tokens} latency_ms={result.latency_ms} finish={result.finish_reason or '-'}"
        + (f" first_token_ms={result.first_token_ms}" if result.first_token_ms is not None else "")
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
        f"finish=length {summary.finish_length}/{summary.total}"
        + (
            f", avg first token {summary.average_first_token_ms} ms"
            if summary.average_first_token_ms is not None
            else ""
        )
        + "\n"
    )


def _run_one(
    provider: LLMProvider,
    case: EvalCase,
    args: argparse.Namespace,
    context: ContextManager,
    max_tokens: int,
    portal: BlockingPortal | None = None,
) -> CaseResult:
    if args.task == "decide":
        return run_decide_case(
            provider, case, max_tokens=max_tokens, context=context, reasoning_effort=args.reasoning_effort
        )
    if args.task == "stream":
        return run_stream_case(
            provider,
            case,
            max_tokens=max_tokens,
            context=context,
            notes=args.notes == "on",
            summary=args.summary == "on",
            reasoning_effort=args.reasoning_effort,
            portal=portal,
        )
    return run_case(
        provider,
        case,
        max_tokens=max_tokens,
        context=context,
        strategy=args.strategy,
        notes=args.notes == "on",
        summary=args.summary == "on",
        reasoning_effort=args.reasoning_effort,
    )


def _print_decisions(summary: DecisionSummary) -> None:
    print(
        f"decision accuracy {summary.correct}/{summary.labelled}  over_probing={summary.over_probing} "
        f"under_probing={summary.under_probing}  per gap: {summary.per_gap or 'none labelled'}\n"
    )


if __name__ == "__main__":
    sys.exit(main())
