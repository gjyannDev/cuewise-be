# Implementation Plan: Eval runs in Langfuse (scores + datasets)

> No `spec.md` exists (user approved planning without one). The AC/EC IDs below are defined here, not inherited.
> Deviation to note: a spec would normally settle "what a good run looks like"; these criteria stand in for it.

## Overview
Make the existing opt-in eval runner (`interviews_evals.py`) push its results to Langfuse: every check becomes a score on the case's trace, every run is tagged so prompt versions and models can be compared, and `eval_cases.json` is mirrored into Langfuse Datasets.

## Architecture & Design
The runner keeps its loop, `--repeat` summaries and terminal output. Each case runs inside one trace, so the provider's generations nest under it. After the case, the checks are posted as scores on that trace. All SDK calls live on `Tracer` in `core/ai/tracing.py` (guarded, no-op without keys, log class name only), so `interviews_evals.py` still never imports langfuse. Cases are upserted into one Dataset per task before the runs start.

## Decisions (grilled with the user)
- Run model: keep the loop and attach scores; no rewrite onto `run_experiment`.
- SDK boundary: extend `Tracer`; no new module, no SDK import in the evals file.
- Dataset sync: `eval_cases.json` stays the source of truth in git; each run upserts items by id.
- Run tags: prompt version, strategy, model, reasoning effort. Task, notes/summary flags and repeat index also go in metadata (cheap, same call). Git SHA left out.
- Test seams: `Tracer` (with an injected fake client) and `main()` (with `FakeProvider`). Both user-confirmed.

## Spike findings (step 0, done)
- `create_score` takes `trace_id`, a float value and `data_type` BOOLEAN or NUMERIC. `propagate_attributes` takes `session_id`, `user_id`, `tags` and `metadata`. `create_dataset_item` upserts by `id`. All public.
- Dataset-to-run linking is NOT public in 5.1.0: there is no per-item `run()` helper. `run_experiment` links items to a run through private "experiment" attributes set by `_propagate_attributes(experiment=...)`. Writing those from the loop would depend on SDK internals.
- anyio's `BlockingPortal.call` runs the task in the portal's own context, so the caller's trace context does not reach the streamed call (EC3 was real).

## Deviations from the first version of this plan (found during /implement)
- Dataset runs (the "run cases as experiments" part of the original ask) are NOT done. Cases are mirrored into datasets, but runs are compared through sessions, tags and scores, not the Dataset Runs view. Doing it properly means moving the loop onto `run_experiment`, which the user chose against. Pending the user's decision.
- AC3: `decision_correct` is dropped (it duplicated the `decision` and `gap` checks); decide cases score `over_probing` and `under_probing` instead.
- Step 6: fixed with a small context copy in `run_stream_case` (stdlib `contextvars`), tested through `main()` as Test: first instead of `after`. Still worth one look on a real Langfuse run.
- `Tracer.trace` reads the trace id with `getattr` so a span without one cannot skip propagation.

## Plan-defined criteria
| ID | Criterion |
|----|-----------|
| AC1 | Each case's trace carries one boolean score per check (name = check name, comment = check detail) and one `case_passed` score. |
| AC2 | A case that ended in an error (provider error, context too large) scores `case_passed` false with the error class as comment. |
| AC3 | Decide runs also score `decision_correct`, so over/under-probing shows in Langfuse. |
| AC4 | Every trace of one run shares a session id (the run label) and carries tags/metadata for prompt, strategy, model, effort, task. |
| AC5 | Cases are upserted into `interviews-eval/<write or decide>`; re-running creates no duplicates. Stream runs use the write dataset. |
| AC6 | Dataset item ids are unique across datasets (task prefix) and stable per case id. |
| AC7 | Without Langfuse keys the runner behaves exactly as today: same output, same exit code, no SDK call. |
| AC8 | Terminal output is unchanged except one line at the end naming the run label to look for in Langfuse. |
| EC1 | Langfuse down or a wrong key: the run finishes, prints its results, exits 0; failures are logged by class name only. |
| EC2 | Dataset upsert fails: scoring still happens; the run is not aborted. |
| EC3 | Stream task: the call runs on the portal's event loop thread, so the trace context may not reach it (see Risks). The generation must still nest under the case's trace. |
| EC4 | `--repeat N`: N traces per case, distinguishable by repeat index in metadata, all in one session. |
| EC5 | Score names stay stable across runs (same check, same name), or comparison breaks. |
| EC6 | Eval content is synthetic, so sending full text is fine here; real user data never goes through this path. |

## Implementation Steps
0. **Spike: confirm the langfuse 5.1.0 API** before coding. Check, in the installed source: `create_score` with `trace_id` and BOOLEAN; `propagate_attributes` accepts tags, metadata, session id; `create_dataset` is idempotent and `create_dataset_item` upserts by id; and how a trace is linked to a dataset item and a run name in 5.1 (the old `item.run()` helper is not in `datasets.py`; linking now seems to go through the experiments API). Write the answers into "Spike findings" below. Decides step 5's shape. — Test: after
1. **`Tracer.trace` returns the trace id and takes tags/metadata.** It yields the id (None when off) and passes tags and metadata to the propagate call. The two controller call sites do not bind the yielded value, so they are unaffected. — Test: first. Seam: `Tracer.trace` with the fake client used in `tests/core/ai/test_tracing.py`. Slices: off tracer yields None; enabled yields the id; tags and metadata reach propagate (AC4); a failing start is swallowed (EC1).
2. **`Tracer.score`.** Guarded, no-op when off; boolean or numeric, optional comment; one call per score, the SDK batches. — Test: first. Seam: `Tracer.score`. Slices: boolean check score (AC1); comment carries detail; failure swallowed (EC1); off tracer makes no call (AC7).
3. **`Tracer.upsert_dataset`.** Creates the dataset if needed, then upserts items by id; guarded. — Test: first. Seam: `Tracer.upsert_dataset`. Slices: items created with given ids (AC5, AC6); second call sends the same ids (no duplicates); a failure is swallowed and reported to the caller as "not synced" (EC2).
4. **Score mapping in the evals module.** A small pure function turns a `CaseResult` into the list of scores: one per check, `case_passed`, `decision_correct` for decide, error class as comment on error cases. Used only by `main()`. — Test: first. Seam: `main()` with `FakeProvider` and a fake-client `Tracer` (assert the scores that reach the client, not the helper). Slices: passing case (AC1); failing check with detail; provider error case (AC2); decide case (AC3).
5. **Wire `main()`.** Add a `tracer` argument beside `provider` (so tests can inject one). Build a run label from task, prompt, strategy, model, effort and a timestamp; open one trace per case run with session id = label and tags/metadata (AC4, EC4); post scores after the case; upsert the dataset before the loop (AC5); print the one-line run label hint at the end (AC8). Shape of dataset linking follows the spike. — Test: first. Seam: `main()`. Slices: no keys, output unchanged (AC7); keys on, scores and tags sent; `--repeat 2` gives two traces per case (EC4); Langfuse failing still exits 0 (EC1); upsert failing still scores (EC2); dataset name per task (AC5).
6. **Stream task trace context.** Make sure the generation made on the portal thread nests under the case's trace: open the trace inside the coroutine the portal runs, or pass the context across. Choice follows the spike. — Test: after (depends on the SDK's context handling; check against a real Langfuse run).
7. **Docs.** Add the new behavior and the "how to compare in Langfuse" note to the module docstring and the Run section; no new doc file. — Test: skip.

## Affected Files & Patterns
- `app/core/ai/tracing.py` — `Tracer.trace` (yield id, tags, metadata), new `score` and `upsert_dataset`; follow the `_safe` decorator and the class-name-only logging rule.
- `app/modules/interviews/interviews_evals.py` — `main()` (tracer argument, run label, per-case trace, scoring, dataset upsert), score mapping, `run_stream_case` for EC3.
- `tests/core/ai/test_tracing.py` — new Tracer tests; reuse its fake client.
- `tests/modules/interviews/test_evals.py` — new `main()` tests; reuse `FakeProvider` and the `decision()` / `reply()` helpers.
- No change: `eval_cases.json`, prompts, the controller, config (keys and base URL already exist).
- Risks:
  - Langfuse 5.1.0 is newer than my background knowledge; step 0 verifies the API rather than assuming it.
  - Dataset-to-run linking may need the experiments API rather than the loop; if so, the "compare runs on a dataset" view may need a small change in step 5, while scores, tags and sessions still work for comparison.
  - Context propagation across the portal thread (EC3).
  - Scores are sent in batches; `tracer.close()` already flushes at the end of `main()`.

## Testing Strategy
- Framework & command: `uv run pytest tests/core/ai/test_tracing.py tests/modules/interviews/test_evals.py`, then the full `uv run pytest`; lint with `uv run ruff check . && uv run ruff format .`.
- Coverage map:

| ID | Step | Test mode | Notes |
|----|------|-----------|-------|
| AC1 | 2, 4 | first | boolean score per check |
| AC2 | 4 | first | error cases |
| AC3 | 4 | first | decide only |
| AC4 | 1, 5 | first | session, tags, metadata |
| AC5 | 3, 5 | first | per-task dataset |
| AC6 | 3 | first | prefixed ids |
| AC7 | 2, 5 | first | no keys, no change |
| AC8 | 5 | first | one extra output line |
| EC1 | 1, 2, 5 | first | outage never fails the run |
| EC2 | 3, 5 | first | upsert failure isolated |
| EC3 | 6 | after | verify on a real stream run |
| EC4 | 5 | first | repeat index |
| EC5 | 4 | first | score name list asserted |
| EC6 | none | n/a | covered by design; eval cases are synthetic |

- Must verify, not assume: SDK signatures (step 0); that scores appear on the right trace; that tags/session show in the UI; that dataset linking works as designed; that stream generations nest under the trace. One real run of `--task write --repeat 2` and one `--task decide` with keys set, then look at Langfuse.
- Open questions: none carried. EC6 has no test because it is a constraint, not a behavior.
- Known baseline failures: not run yet. Run the two test files first in `/implement` and record any failures.

## Blockers & Resolutions
- Unknown 5.1 dataset-linking API -> step 0 spike before any code.
- Portal thread may drop the trace context (EC3) -> step 6, verified on a real run.
- Score names drifting between runs (EC5) -> one list of names in the mapping, asserted in tests.
- Eval outage must never fail a run (EC1) -> reuse the `_safe` guard for every new call.

## Trade-offs & Rationale
- Keep the loop instead of `run_experiment`: you keep `--repeat` stats, the three tasks and all existing tests; cost is that dataset-run linking may need extra work (see Risks).
- Scores as booleans per check instead of one number: failures are filterable by check name in the UI.
- Do not score tokens and latency: the generation already carries usage and latency, Langfuse computes cost, and duplicating them adds noise.
- One dataset per task, ids prefixed by task: Langfuse requires item ids to be globally unique.
- Not in this plan (deliberately): LLM-as-judge for question relevance, Langfuse-side evaluators, CI runs. That is the next slice once scores flow.

## Project Rules Applied
- `CLAUDE.md` (AI Engineering Guidelines) -> evals stay opt-in, out of `pytest`; real-model calls stay separate; the LLM is mocked in unit tests; no raw content in logs.
- `tracing.py` docstring rule -> nothing outside `core/ai/` imports the Langfuse SDK; failures log the class name only.
- `CLAUDE.md` (Don'ts) -> no new dependency; `langfuse>=5.1.0` is already installed.
- `CLAUDE.md` (Git) -> nothing committed; run `graphify update .` after implementing.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | read the runner, `tracing.py`, tests, and the installed langfuse source |
| graphify | one query on provider tracing and eval wiring (result truncated, used for orientation only) |
| grill-me | asked as five decisions via AskUserQuestion; all answered, all recommended options taken except tags (user chose prompt/strategy and model/effort) |
| llm-evaluation | confirmed what the harness already covers and what is left (judge, stored history) |
| not used | understand-anything (no graph), ponytail (design already minimal), security-review (synthetic data, no new auth surface) |

## Ready to Implement
- All plan-defined criteria mapped to steps; every step has a Test tag
- Affected files identified
- Seams user-confirmed: `Tracer`, `main()`
- Open risk: step 0 can change step 5 and 6; do it first
- Deviation: no spec.md (user-approved)
