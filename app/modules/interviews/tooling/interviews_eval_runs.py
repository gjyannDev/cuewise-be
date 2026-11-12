"""What every eval task moved onto Langfuse experiments shares (langfuse-experiments).

An *experiment run* is one execution of a task over a Langfuse dataset: one result per case, with scores, linked to
the dataset's items so two runs can be compared case by case in the Langfuse UI. These helpers build what a run
carries (metadata, name, description), run the cases either as such a run or locally, and say on the console what
was recorded. Imports neither eval module, so both can use it.
"""

import hashlib
import subprocess
from collections.abc import Callable, Iterable, Mapping, Sequence
from datetime import datetime
from typing import Any

from app.core.ai.tracing import ExperimentRun, Tracer

# The run description shows a reason and a prediction next to the run, not an essay.
DESCRIPTION_MAX_LENGTH = 300
# (name, value, comment): a bool becomes a BOOLEAN score, a number a NUMERIC one.
Score = tuple[str, bool | float, str | None]


def git_commit(*, run: Callable[..., subprocess.CompletedProcess[str]] = subprocess.run) -> str:
    """The short commit hash, `-dirty` when the working tree has changes, `unknown` when git can't say. Read-only:
    fixed arguments, no shell, and `--no-optional-locks` so it never touches the index."""

    def git(*args: str) -> str:
        done = run(
            ["git", "--no-optional-locks", *args], capture_output=True, text=True, check=True, timeout=5
        )
        return done.stdout.strip()

    try:
        head = git("rev-parse", "--short", "HEAD")
        dirty = bool(git("status", "--porcelain"))
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    if not head:
        return "unknown"
    return f"{head}-dirty" if dirty else head


def run_metadata(
    *,
    task: str,
    commit: str,
    model: str | None,
    prompts: Mapping[str, str | None],
    repeat: int,
    flags: Mapping[str, object],
    extra: Mapping[str, object] | None = None,
) -> dict[str, str]:
    """What produced a run, as the strings Langfuse stores: the run explains itself when it is read months later."""

    def text(value: object) -> str:
        return "-" if value is None else str(value)

    meta = {"task": task, "commit": commit, "model": text(model), "repeat": str(repeat)}
    meta |= {f"prompt.{key}": text(value) for key, value in prompts.items()}
    meta |= {f"flag.{key}": text(value) for key, value in flags.items()}
    meta |= {key: text(value) for key, value in (extra or {}).items()}
    return meta


def run_name(task: str, stamp: str, repeat: int, arm: str | None = None, *, label: str | None = None) -> str:
    """Unique per command, repeat and arm (Langfuse merges runs that share a name on one dataset), and readable in a
    list: `label` says what the run tested (a prompt version and model, a threshold and notes), before when it ran."""
    parts = [task, *([label] if label else []), stamp, f"r{repeat}", *([f"arm-{arm}"] if arm else [])]
    return "/".join(parts)


def run_stamp() -> str:
    """Local time, as the Langfuse list shows the run's start: the name and the timestamp column then match."""
    return datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")


def notes_fingerprint(content_hashes: Iterable[str]) -> str:
    """A short id for the ingested notes: changes when any note changes, not when the order does."""
    return hashlib.sha256("\n".join(sorted(content_hashes)).encode()).hexdigest()[:12]


def run_description(note: str | None) -> str | None:
    """`--note` as the run's description: blank gives none, a long one is cut."""
    text = (note or "").strip()
    if not text:
        return None
    return text if len(text) <= DESCRIPTION_MAX_LENGTH else text[: DESCRIPTION_MAX_LENGTH - 1] + "…"


def run_cases[C, R](
    tracer: Tracer,
    *,
    dataset: str,
    cases: Sequence[C],
    item_of: Callable[[C], Mapping[str, Any]],
    run_one: Callable[[C], R],
    output_of: Callable[[C, R], dict[str, Any]],
    scores_of: Callable[[R], list[Score]],
    run_scores_of: Callable[[list[R]], list[tuple[str, float]]],
    name: str,
    run_name: str,
    metadata: Mapping[str, str],
    description: str | None = None,
) -> tuple[list[R], ExperimentRun | None]:
    """Run every case once, in order, as one Langfuse experiment run; whatever the run did not get to (no keys,
    Langfuse failing) runs locally afterwards, so no case is skipped and no LLM call is repeated. Returns the results
    in case order and the run's record (None when nothing was recorded).

    The task given to Langfuse never raises: the SDK would drop that case from the run, and a missing case must not
    look like a passing one. Provider errors are already results (the case's own runner returns them); a real bug is
    held and re-raised after the run, so it still stops the command as it does without Langfuse."""
    items = [item_of(case) for case in cases]
    by_item = {item["id"]: case for item, case in zip(items, cases, strict=True)}
    results: dict[str, R] = {}
    # The SDK hands each evaluator the exact object the task returned; the scores (with their comments) are kept
    # beside it rather than inside the output Langfuse displays.
    scored: dict[int, tuple[dict[str, Any], list[Score]]] = {}
    crashed: list[Exception] = []

    def task(*, item: Any, **_: Any) -> dict[str, Any]:
        if crashed:
            return {"skipped": "an earlier case crashed"}
        case = by_item[item.id]
        try:
            result = run_one(case)
        except Exception as exc:  # noqa: BLE001  held, then re-raised after the run (see the docstring)
            crashed.append(exc)
            return {"error": type(exc).__name__}
        results[item.id] = result
        scores = scores_of(result)
        output = output_of(case, result) | {"scores": {score_name: value for score_name, value, _ in scores}}
        scored[id(output)] = (output, scores)
        return output

    def item_scores(*, output: Any, **_: Any) -> list[dict[str, Any]]:
        scores = scored[id(output)][1] if id(output) in scored else []
        return [_evaluation(score_name, value, comment) for score_name, value, comment in scores]

    def run_scores(**_: Any) -> list[dict[str, Any]]:
        done = [results[item["id"]] for item in items if item["id"] in results]
        if not done:
            return []
        return [{"name": key, "value": float(value), "data_type": "NUMERIC"} for key, value in run_scores_of(done)]

    record = tracer.run_experiment(
        dataset=dataset,
        items=items,
        name=name,
        run_name=run_name,
        task=task,
        evaluators=[item_scores],
        run_evaluators=[run_scores],
        metadata=metadata,
        description=description,
    )
    if crashed:
        raise crashed[0]
    for item in items:
        if item["id"] not in results:
            results[item["id"]] = run_one(by_item[item["id"]])
    return [results[item["id"]] for item in items], record


def _evaluation(name: str, value: bool | float, comment: str | None) -> dict[str, Any]:
    if isinstance(value, bool):
        return {"name": name, "value": 1.0 if value else 0.0, "data_type": "BOOLEAN", "comment": comment}
    return {"name": name, "value": float(value), "data_type": "NUMERIC", "comment": comment}


def final_line(records: Sequence[ExperimentRun | None], *, enabled: bool) -> str:
    """The console's last line: which Langfuse runs to open, or why nothing was recorded."""
    if not enabled:
        return "Langfuse: not recorded (no LANGFUSE keys set)."
    done = [record for record in records if record is not None]
    if not done:
        return "Langfuse: not recorded (Langfuse failed or the dataset could not be synced; see the warnings above)."
    names = "; ".join(f"{r.run_name} ({r.url})" if r.url else r.run_name for r in done)
    missing = len(records) - len(done)
    if missing:
        return f"Langfuse runs: {names}; {missing} of {len(records)} runs not recorded (see the warnings above)."
    return f"Langfuse runs: {names}"
