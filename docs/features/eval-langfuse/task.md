# Implementation: Eval runs in Langfuse (scores + datasets)

## Status
Code done, automated tests green. Needs a real Langfuse run (see Tests Pending) and a decision on dataset runs (see Open Questions). Not committed.

## Completed Steps
- [x] 0. Spike: Langfuse 5.1.0 API (findings in plan.md)
- [x] 1. `Tracer.trace` yields the trace id; takes tags and metadata
- [x] 2. `Tracer.score`
- [x] 3. `Tracer.upsert_dataset`
- [x] 4. Score mapping (`scores_for`) in `interviews_evals.py`
- [x] 5. `main()` wiring: `tracer` argument, run session, tags, per-case trace, scores, dataset upsert, run label line
- [x] 6. Stream task keeps the trace context (context copy in `run_stream_case`)
- [x] 7. Module docstring

## Changes Made
Follow-up (readable traces): each trace is named `<task>: <case id>`; its input is the case's kind, last question and answer (plus the first 300 chars of the job description); its output is `verdict` (PASS, `FAIL: check(detail), ...` or `ERROR: class`), the model's `reply`, `decided` vs `expected` (decide only) and the case `notes`. `case_passed` carries the same verdict as its comment. New `Tracer.set_trace_output`. Also fixed two pyright errors in `Generation._finish` (explicit `_obs is None` guard).

Also added `hints` to the trace output (`hints_for`): rule-of-thumb pointers on where to look first, chosen from the failed check, the direction of a wrong decision (over- or under-probing), the case kind (injection cases point at an invented answer), a `length` finish reason, and provider errors. They are heuristics, not a diagnosis; a passing case has an empty list.

No commits (user commits manually). Suggested message:
feat(evals): send eval checks to Langfuse as scores and mirror the cases into datasets

Files: `app/core/ai/tracing.py`, `app/modules/interviews/interviews_evals.py`, `tests/core/ai/test_tracing.py`, `tests/modules/interviews/test_evals.py`, `docs/features/eval-langfuse/{plan,task}.md`.

## Test Results
Full suite: 868 passed, 1 skipped, 1 failed (baseline, below). New tests: 7 in `test_tracing.py` (trace id, tags/metadata, score, upsert), 12 in `test_evals.py` (through `main()`).

## Tests Pending
- Real run with Langfuse keys set (costs a few LLM calls): `uv run python -m app.modules.interviews.interviews_evals --task write --repeat 2` and `--task decide`. Check in Langfuse: scores on each trace, one session per run, tags, the two datasets, and (stream) that the generation sits under the case trace.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | trace yields id; None when off or broken | spec | AC1, AC7, EC1 | pass |
| T2 | 1 | tags and metadata reach propagate | spec | AC4 | pass |
| T3 | 2 | boolean score with detail comment; no call when off or no id; failure swallowed | spec | AC1, AC7, EC1 | pass |
| T4 | 3 | dataset then items by id; twice sends same ids; false when off or failing | spec | AC5, AC6, AC7, EC2 | pass |
| T5 | 4-5 | every check scored, `case_passed` = AND of checks | spec | AC1, EC5 | pass |
| T6 | 4-5 | failed check keeps its detail; provider error scores only `case_passed` with error class | spec | AC1, AC2 | pass |
| T7 | 4-5 | decide scores over/under probing | spec | AC3 | pass |
| T8 | 5 | one session, tags, metadata, repeat index, session line printed | spec | AC4, AC8, EC4 | pass |
| T9 | 5 | no tracer: no Langfuse line | spec | AC7, AC8 | pass |
| T10 | 5 | Langfuse outage and failed upsert do not change the run | spec | EC1, EC2 | pass |
| T11 | 5 | write/decide/stream dataset names, task-prefixed ids, decide labels | spec | AC5, AC6 | pass |
| T12 | 6 | streamed call runs inside its case trace | spec | EC3 | pass |

## Open Questions
- Dataset runs: Langfuse 5.1.0 only links runs to dataset items through `run_experiment` (private attributes otherwise). Move the loop onto `run_experiment`, or stay with sessions, tags and scores? -> needs decision from: user.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`: expects `llm_max_tokens` 800, gets 4000. Not touched by this change.

## Known Issues
- `ruff` is not in the project environment (`uv run ruff` fails); I checked imports and errors with `uvx ruff` only. Its default rules flag older code (blind `except`), so I did not treat those as mine.

## Deviations from Plan
- See plan.md "Deviations" (dataset runs not done; AC3 changed; step 6 tested first). Approved by: pending user.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 0 | lean-ctx, graphify | read installed langfuse source and the runner |
| 1-6 | tdd flow (by hand) | red then green per step, seams `Tracer` and `main()` |

## Links
- Plan: docs/features/eval-langfuse/plan.md
