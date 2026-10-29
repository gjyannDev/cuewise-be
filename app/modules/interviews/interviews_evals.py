"""Opt-in evals for the interviewer prompt: fixed cases, run against the real model, checked by rules.

Run:  uv run python -m app.modules.interviews.interviews_evals
(needs OPENROUTER_API_KEY and LLM_MODEL). It costs real calls, so it never runs in `uv run pytest`; the checks
themselves are unit-tested with the fake provider. Never imported by the app.

Each case is one moment of an interview (setup, conversation so far, last answer). The checks are reference-free
rules, because a good interview question has no single right text: is the reply valid, is it only a question,
does it avoid judging the candidate, and does it ignore injected instructions.
"""

import re
import sys
from collections import Counter
from collections.abc import Sequence
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, TypeAdapter

from app.core.ai.provider import LLMError, LLMProvider

from .interviews_constants import InterviewType, JobRole, Level, QuestionCategory
from .interviews_reply import InvalidReplyError, parse_interviewer_reply
from .interviews_utils import QuestionTurn, build_interviewer_messages, render_interviewer_prompt

EVAL_CASES_PATH = Path(__file__).parent / "data" / "eval_cases.json"

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


class EvalCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    kind: Literal["strong", "vague", "off_topic", "near_empty", "injection_answer", "injection_job_description"]
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
    latency_ms: int = 0

    @property
    def passed(self) -> bool:
        return self.error is None and all(c.passed for c in self.checks)


class Summary(BaseModel):
    passed: int
    total: int
    check_failures: dict[str, int]
    prompt_tokens: int
    completion_tokens: int
    average_latency_ms: int


def load_cases(path: Path) -> list[EvalCase]:
    return TypeAdapter(list[EvalCase]).validate_json(path.read_bytes())


def check_reply(case: EvalCase, raw: str) -> list[Check]:
    """Rule checks for one reply. Text checks look at the parsed question, or at the raw text if it didn't parse."""
    try:
        question = parse_interviewer_reply(
            raw,
            interview_type=case.setup.interview_type,
            earlier_questions=[turn.question for turn in case.history],
        ).question
        valid = Check(name="valid_reply", passed=True)
    except InvalidReplyError as exc:
        question = raw
        valid = Check(name="valid_reply", passed=False, detail=exc.reason)

    judgement = _JUDGEMENT.search(question)
    acknowledgement = _ACKNOWLEDGEMENT.search(question)
    obeyed = bool(case.marker) and case.marker.casefold() in raw.casefold()
    return [
        valid,
        Check(name="no_judgement", passed=judgement is None, detail=judgement.group(0) if judgement else ""),
        Check(
            name="question_only",
            passed=acknowledgement is None,
            detail=acknowledgement.group(0) if acknowledgement else "",
        ),
        Check(name="injection_ignored", passed=not obeyed, detail=case.marker if obeyed else ""),
    ]


def run_case(provider: LLMProvider, case: EvalCase, *, max_tokens: int) -> CaseResult:
    system = render_interviewer_prompt(
        role=case.setup.role,
        level=case.setup.level,
        interview_type=case.setup.interview_type,
        question_number=len(case.history) + 1,
        question_count=case.setup.question_count,
    )
    turns = [QuestionTurn(t.question, t.category, t.answer) for t in case.history]
    messages = build_interviewer_messages(system, case.job_description, turns)
    try:
        result = provider.complete(messages, max_tokens=max_tokens)
    except LLMError as exc:
        return CaseResult(case_id=case.id, checks=[], error=type(exc).__name__)
    checks = check_reply(case, result.text)
    return CaseResult(
        case_id=case.id,
        checks=checks,
        question=result.text.strip(),
        prompt_tokens=result.prompt_tokens or 0,
        completion_tokens=result.completion_tokens or 0,
        latency_ms=result.latency_ms,
    )


def summarize(results: Sequence[CaseResult]) -> Summary:
    failures = Counter(c.name for r in results for c in r.checks if not c.passed)
    return Summary(
        passed=sum(r.passed for r in results),
        total=len(results),
        check_failures=dict(failures),
        prompt_tokens=sum(r.prompt_tokens for r in results),
        completion_tokens=sum(r.completion_tokens for r in results),
        average_latency_ms=round(sum(r.latency_ms for r in results) / len(results)) if results else 0,
    )


def main() -> int:
    from app.core.ai.factory import build_provider
    from app.core.config import settings

    provider = build_provider(settings)
    if provider is None:
        print("LLM is not configured: set OPENROUTER_API_KEY and LLM_MODEL in .env first.")
        return 1
    print(f"model={settings.llm_model} max_tokens={settings.llm_max_tokens}\n")
    results = []
    try:
        for case in load_cases(EVAL_CASES_PATH):
            result = run_case(provider, case, max_tokens=settings.llm_max_tokens)
            results.append(result)
            failed = [f"{c.name}({c.detail})" for c in result.checks if not c.passed]
            status = "PASS" if result.passed else "FAIL"
            print(f"{status}  {case.id:<30} {result.error or ', '.join(failed) or '-'}")
            print(f"      tokens={result.prompt_tokens}/{result.completion_tokens} latency_ms={result.latency_ms}")
            print(f"      reply={result.question!r}\n")
    finally:
        provider.close()
    summary = summarize(results)
    print(f"passed {summary.passed}/{summary.total}  failed checks: {summary.check_failures or 'none'}")
    print(
        f"tokens {summary.prompt_tokens} in / {summary.completion_tokens} out, avg latency {summary.average_latency_ms} ms"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
