"""The profile-extraction eval: synthetic résumés through the real upload pipeline, scored against hand labels.

    uv run python -m app.modules.profile.tooling.profile_evals --model gemini-3.5-flash-lite --repeat 2 [--pause-seconds 2.5]

Each case in data/profile_eval_cases.json is built into a real PDF or DOCX and goes through the same steps as an
upload (read -> scrub -> extract -> parse -> ground), so the numbers describe the shipped pipeline, not the prompt
alone. Scores per case: skills precision and recall, role count match, title recall, and whether a hidden injection
was ignored (profile_eval_scoring.py). With Langfuse keys, each repeat is one experiment run on the dataset
`profile-eval/extract`; the extraction call itself stays redacted in the trace (synthetic data or not), the run's
items and outputs are the synthetic cases and their profiles.
"""

import argparse
import json
import time
from collections.abc import Callable, Sequence
from pathlib import Path
from statistics import mean
from typing import Literal, NamedTuple

from pydantic import BaseModel, ConfigDict

from app.core.ai.provider import LLMProvider, LLMResult
from app.core.ai.tracing import ExperimentRun, Tracer

# The experiment helpers every eval shares; dev tooling, not app code (lifting them to core is a later refactor).
from app.modules.interviews.tooling.interviews_eval_runs import (
    Score,
    final_line,
    git_commit,
    pacer,
    run_cases,
    run_description,
    run_metadata,
    run_name,
    run_stamp,
)

from ..ai.profile_extract import ExtractionFailedError, extract_profile
from ..ai.profile_reply import EmptyProfileError
from ..constants.profile_constants import PROFILE_PROMPT_VERSION
from ..schemas.profile_schema import CandidateProfile
from ..utils.profile_resume_utils import ResumeRefusal, read_resume
from ..utils.profile_utils import ground_profile, scrub_contacts
from .profile_eval_scoring import ExpectedProfile, ProfileScore, score_profile
from .profile_resume_files import Rect, Text, make_docx, make_pdf

CASES_PATH = Path(__file__).resolve().parent.parent / "data" / "profile_eval_cases.json"
DATASET = "profile-eval/extract"
TASK = "profile"


class EvalCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    notes: str = ""
    layout: Literal["one_column", "two_column", "dark_sidebar", "docx"]
    main: list[str]
    sidebar: list[str] = []
    table: list[list[str]] = []
    hidden: list[str] = []
    expect: ExpectedProfile


class CaseResult(NamedTuple):
    outcome: str  # ok, refused:<reason>, empty_profile, extraction_failed:<reason>
    profile: CandidateProfile | None
    score: ProfileScore | None
    hidden_chars: int
    ungrounded: int
    results: list[LLMResult]


def load_cases(path: Path = CASES_PATH) -> list[EvalCase]:
    return [EvalCase.model_validate(case) for case in json.loads(path.read_text(encoding="utf-8"))["cases"]]


def build_file(case: EvalCase) -> bytes:
    """The case as the file a candidate would upload. Hidden lines are white (PDF) or hidden runs (DOCX)."""
    if case.layout == "docx":
        paragraphs = [[(line, {})] for line in case.main]
        paragraphs += [[(line, {"hidden": True})] for line in case.hidden]
        return make_docx(paragraphs, table=case.table or None)
    items: list = []
    left = 40 if case.sidebar else 72
    main_x = 200 if case.sidebar else left
    if case.layout == "dark_sidebar":
        items.append(Rect(0, 0, 180, 792, color=(0.12, 0.16, 0.3)))
    sidebar_color = (1, 1, 1) if case.layout == "dark_sidebar" else 0.0
    items += [Text(left, 720 - i * 18, line, color=sidebar_color) for i, line in enumerate(case.sidebar)]
    items += [Text(main_x, 720 - i * 18, line) for i, line in enumerate(case.main)]
    items += [Text(main_x, 300 - i * 14, line, color=1.0) for i, line in enumerate(case.hidden)]
    return make_pdf([items])


def run_case(llm: LLMProvider, case: EvalCase, *, max_tokens: int, clock: Callable[[], float] = time.monotonic) -> CaseResult:
    try:
        resume = read_resume(build_file(case))
    except ResumeRefusal as exc:
        return CaseResult(f"refused:{exc.reason}", None, None, 0, 0, [])
    try:
        extraction = extract_profile(llm, scrub_contacts(resume.text), max_tokens=max_tokens, clock=clock)
        profile, ungrounded = ground_profile(extraction.profile, extraction.model_input)
    except ExtractionFailedError as exc:
        return CaseResult(f"extraction_failed:{exc.reason}", None, None, resume.hidden_chars, 0, exc.results)
    except EmptyProfileError:
        return CaseResult("empty_profile", None, None, resume.hidden_chars, 0, [])
    return CaseResult("ok", profile, score_profile(profile, case.expect), resume.hidden_chars, ungrounded, extraction.results)


def case_scores(result: CaseResult) -> list[Score]:
    scores: list[Score] = [("valid_profile", result.outcome == "ok", None if result.outcome == "ok" else result.outcome)]
    if result.score is not None:
        s = result.score
        scores += [
            ("skills_precision", s.skills_precision, None),
            ("skills_recall", s.skills_recall, None),
            ("role_count_match", s.role_count_match, None),
            ("title_recall", s.title_recall, None),
            ("injection_ignored", s.injection_ignored, None),
            ("ungrounded", float(result.ungrounded), None),
        ]
    return scores


def summary(results: Sequence[CaseResult]) -> dict[str, float]:
    scored = [r.score for r in results if r.score is not None]

    def avg(values: list[float]) -> float:
        return round(mean(values), 3) if values else 0.0

    return {
        "valid": float(len(scored)),
        "skills_precision": avg([s.skills_precision for s in scored]),
        "skills_recall": avg([s.skills_recall for s in scored]),
        "role_count_match": avg([float(s.role_count_match) for s in scored]),
        "title_recall": avg([s.title_recall for s in scored]),
        "injection_ignored": avg([float(s.injection_ignored) for s in scored]),
        "prompt_tokens": float(sum(r.prompt_tokens or 0 for c in results for r in c.results)),
        "completion_tokens": float(sum(r.completion_tokens or 0 for c in results for r in c.results)),
    }


def _print_case(case: EvalCase, result: CaseResult) -> None:
    status = "PASS" if result.outcome == "ok" and result.score and result.score.injection_ignored else "FAIL"
    print(f"{status}  {case.id:<22} {result.outcome}")
    if result.score:
        s = result.score
        print(
            f"      precision={s.skills_precision:.2f} recall={s.skills_recall:.2f} roles={s.role_count_match} "
            f"titles={s.title_recall:.2f} injection_ignored={s.injection_ignored} "
            f"hidden_chars={result.hidden_chars} ungrounded={result.ungrounded}"
        )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Profile-extraction eval on synthetic résumés.")
    parser.add_argument("--model", help="override the primary provider's model for this run")
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--pause-seconds", type=float, default=0.0, help="wait between cases (free-tier limits)")
    parser.add_argument("--note", help="why you are running this (and what you expect): the Langfuse run's description")
    return parser


def main(
    argv: Sequence[str] | None = None,
    *,
    provider: LLMProvider | None = None,
    tracer: Tracer | None = None,
    sleep: Callable[[float], None] = time.sleep,
) -> int:
    args = _parser().parse_args(argv)
    from app.core.ai.factory import build_provider
    from app.core.ai.tracing import build_tracer
    from app.core.config import settings

    configs = settings.llm_provider_configs
    model = args.model or (configs[0].model if configs else None)
    if provider is None:
        tracer = tracer or build_tracer(settings, environment="eval")
        provider = build_provider(settings, model=args.model, tracer=tracer)
        if provider is None:
            print("LLM is not configured: set LLM_PROVIDERS and that vendor's LLM_<VENDOR>_* settings in .env first.")
            return 1
    tracer = tracer or Tracer(None)
    cases = load_cases()
    print(f"model={model} prompt={PROFILE_PROMPT_VERSION} cases={len(cases)} repeat={args.repeat}\n")
    wait = pacer(args.pause_seconds, sleep=sleep)
    commit, stamp = git_commit(), run_stamp()
    items = {
        case.id: {
            "id": f"extract:{case.id}",
            "input": case.model_dump(mode="json", include={"layout", "main", "sidebar", "table", "hidden"}),
            "expected_output": case.expect.model_dump(mode="json"),
            "metadata": {"notes": case.notes},
        }
        for case in cases
    }

    def run_one(case: EvalCase) -> CaseResult:
        wait()
        result = run_case(provider, case, max_tokens=settings.llm_max_tokens)
        _print_case(case, result)
        return result

    runs: list[dict[str, float]] = []
    records: list[ExperimentRun | None] = []
    for repeat in range(1, args.repeat + 1):
        results, record = run_cases(
            tracer,
            dataset=DATASET,
            cases=cases,
            item_of=lambda case: items[case.id],
            run_one=run_one,
            output_of=lambda case, result: {
                "outcome": result.outcome,
                "profile": result.profile.model_dump() if result.profile else None,
                "hidden_chars": result.hidden_chars,
                "ungrounded": result.ungrounded,
            },
            scores_of=case_scores,
            run_scores_of=lambda done: list(summary(done).items()),
            name=TASK,
            run_name=run_name(TASK, stamp, repeat, label=f"{PROFILE_PROMPT_VERSION}/{model or 'default-model'}"),
            metadata=run_metadata(
                task=TASK, commit=commit, model=model, prompts={"extract": PROFILE_PROMPT_VERSION}, repeat=repeat,
                flags={"pause_seconds": args.pause_seconds},
            ),
            description=run_description(args.note),
        )
        records.append(record)
        runs.append(summary(results))
        print(f"\nrun {repeat}: " + " ".join(f"{key}={value}" for key, value in runs[-1].items()) + "\n")

    if len(runs) > 1:
        for key in ("skills_precision", "skills_recall", "title_recall", "injection_ignored"):
            values = [run[key] for run in runs]
            print(f"{key}: mean={mean(values):.3f} min={min(values):.3f} max={max(values):.3f}")
    print(final_line(records, enabled=tracer.enabled))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
