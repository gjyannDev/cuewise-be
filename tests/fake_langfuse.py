"""A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and scores, recorded in memory.

It mimics what the SDK (5.1.0) does that our code relies on: items are upserted by id, a dataset is fetched as a list
of items, `run_experiment` calls the task once per item in the given order, drops an item whose task raises (as the
SDK does, so tests can prove our tasks never raise), runs the item evaluators on each output and the run evaluators
on the results, and returns the run name, an experiment id, a URL and a trace id per item.
"""

from contextlib import contextmanager
from contextvars import ContextVar
from types import SimpleNamespace

# The item whose task is running, as the SDK's OpenTelemetry context would carry it: a call made inside a task (also on
# another thread, when the caller copies its context) sees it.
current_item: ContextVar[str | None] = ContextVar("current_item", default=None)


class FakeLangfuse:
    def __init__(
        self, *, fail_upsert=False, fail_run=False, fail_after=None, reverse_fetch=False, missing=(), fail_scores=False
    ):
        self.fail_upsert, self.fail_run, self.fail_after = fail_upsert, fail_run, fail_after
        self.reverse_fetch, self.missing, self.fail_scores = reverse_fetch, set(missing), fail_scores
        self.datasets: dict[str, dict[str, dict]] = {}
        self.experiments: list[dict] = []
        self.task_calls: list[str] = []
        self.dropped: list[str] = []
        self.scores: list[dict] = []
        self.run_scores: list[dict] = []
        self.observations: list[dict] = []
        self.outputs: dict[str, object] = {}
        self.flushed = self.shut_down = 0

    # --- datasets -----------------------------------------------------------------------------------------------

    def create_dataset(self, *, name, **_):
        if self.fail_upsert:
            raise RuntimeError("langfuse down")
        self.datasets.setdefault(name, {})

    def create_dataset_item(self, *, dataset_name, id, **fields):
        if self.fail_upsert:
            raise RuntimeError("langfuse down")
        self.datasets.setdefault(dataset_name, {})[id] = {"id": id, **fields}

    def get_dataset(self, name, **_):
        stored = [item for item_id, item in self.datasets.get(name, {}).items() if item_id not in self.missing]
        if self.reverse_fetch:
            stored = stored[::-1]
        items = [
            SimpleNamespace(
                id=item["id"],
                dataset_id=f"ds-{name}",
                input=item.get("input"),
                expected_output=item.get("expected_output"),
                metadata=item.get("metadata"),
            )
            for item in stored
        ]
        return SimpleNamespace(name=name, items=items)

    # --- experiments --------------------------------------------------------------------------------------------

    def run_experiment(
        self,
        *,
        name,
        data,
        task,
        run_name=None,
        description=None,
        evaluators=(),
        run_evaluators=(),
        max_concurrency=50,
        metadata=None,
        **_,
    ):
        if self.fail_run:
            raise RuntimeError("langfuse down")
        self.experiments.append(
            {
                "name": name,
                "run_name": run_name,
                "description": description,
                "max_concurrency": max_concurrency,
                "metadata": metadata,
                "item_ids": [item.id for item in data],
            }
        )
        results = []
        for position, item in enumerate(data):
            if self.fail_after is not None and position >= self.fail_after:
                raise RuntimeError("langfuse lost the run")
            self.task_calls.append(item.id)
            trace_id = f"trace-{run_name}-{item.id}"
            token = current_item.set(item.id)
            try:
                output = task(item=item)
            except Exception:  # noqa: BLE001  the SDK drops a raising task's item; so does the fake
                self.dropped.append(item.id)
                continue
            finally:
                current_item.reset(token)
            evaluations = []
            self.outputs[trace_id] = output
            for evaluator in evaluators:
                found = evaluator(
                    input=item.input, output=output, expected_output=item.expected_output, metadata=item.metadata
                )
                evaluations += found if isinstance(found, list) else [found]
            self.scores += [{"trace_id": trace_id, "run_name": run_name, **e} for e in evaluations]
            results.append(
                SimpleNamespace(
                    item=item,
                    output=output,
                    evaluations=[SimpleNamespace(**e) for e in evaluations],
                    trace_id=trace_id,
                )
            )
        run_evaluations = []
        for evaluator in run_evaluators:
            found = evaluator(item_results=results)
            run_evaluations += found if isinstance(found, list) else [found]
        self.run_scores += [{"run_name": run_name, **e} for e in run_evaluations]
        return SimpleNamespace(
            run_name=run_name,
            experiment_id=f"exp-{run_name}",
            experiment_url=f"https://langfuse.test/experiments/{run_name}",
            item_results=results,
            run_evaluations=run_evaluations,
        )

    # --- the rest of what Tracer may touch -----------------------------------------------------------------------

    def create_score(self, **kwargs):
        if self.fail_scores:
            raise RuntimeError("langfuse rejected the score")
        self.scores.append(kwargs)

    @contextmanager
    def start_as_current_observation(self, **kwargs):
        """A step (chain) or span opened inside a task: recorded with the item it belongs to and what it ends with."""
        record = {**kwargs, "item": current_item.get()}
        self.observations.append(record)
        yield SimpleNamespace(trace_id="trace-step", update=lambda **fields: record.update(fields), end=lambda: None)

    def start_observation(self, **kwargs):
        """A check (guardrail) or generation started inside a task."""
        record = {**kwargs, "item": current_item.get()}
        self.observations.append(record)
        return SimpleNamespace(update=lambda **fields: record.update(fields), end=lambda: None)

    def update_current_span(self, **_):
        pass

    def flush(self):
        self.flushed += 1

    def shutdown(self):
        self.shut_down += 1

    # --- helpers for assertions ---------------------------------------------------------------------------------

    def item_scores(self, run_name=None):
        return [s for s in self.scores if run_name is None or s.get("run_name") == run_name]

    def run_score(self, run_name, name):
        [score] = [s for s in self.run_scores if s["run_name"] == run_name and s["name"] == name]
        return score
