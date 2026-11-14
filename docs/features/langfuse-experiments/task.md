# Implementation: Langfuse experiments for the interviews evals

## Status
Phase 1 built; Step 7 gate: **go** (you compared two real `decide` runs in Langfuse on 2026-11-12 and asked for Phase
2). Phase 2 Steps 8-12, 14 and 15 built and tested with fakes. **Waiting on Step 13: your real Phase 2 runs.** Nothing
committed.

## Completed Steps
- [x] 0. Spike (findings in plan.md)
- [x] 1. `Tracer.run_experiment` + `ExperimentRun` (`app/core/ai/tracing.py`)
- [x] 2. Run helpers module `app/modules/interviews/tooling/interviews_eval_runs.py` (git state, metadata, run name, notes fingerprint, run description, `run_cases`)
- [x] 3. Console final line (`final_line`, same module)
- [x] 4. `decide` as an experiment run in `interviews_evals.main()`; `--note` option; `experiment_scores_for`, `decide_run_scores`
- [x] 5. `retrieval` as an experiment run: public `run_retrieval`, `retrieval_item`, preflight `_ready_notes`, `retrieval_run_scores`; `run_rag_task` builds the eval tracer for retrieval and passes `--note`
- [x] 6. Docs: `docs/evaluation-guide.md` (intro, task table, `--note`/`--pause-seconds` flags, section 6a "Compare experiment runs", eval-log rule, gaps list); module docstrings; `learnings.md`
- [x] 7. Real run and gate: **go**. Two `decide` command runs compared in the UI (eval log in learnings.md §7). Finding: run names were only a time, so they now say what was tested (D6). `retrieval` real run still to do.
- [x] 8. `Tracer.score` takes an optional stable `score_id` and returns whether it was sent (D7)
- [x] 9. `write` and `stream` as experiment runs (`interviewer_prompt_version`, `write_run_scores`); stream shares the write dataset, marked `task=stream`
- [x] 10. `feedback` as experiment runs (`run_feedback` on `run_cases`, `feedback_run_scores`, spread posted on the last run with stable ids)
- [x] 11. `generation` as one run per repeat and arm (`run_generation`, `generation_item`, `generation_run_scores`, `ArmInterview`); sheet gains optional `Rating:` and `Note:` lines; `<sheet>.traces.json`; notes preflight (D5)
- [x] 12. `ranking` posts `human_rank`, the rubric scores and `human_score`, and notes as comments (`run_ranking`, `read_rankings` extended, `_rating`)
- [ ] 13. Phase 2 real runs and gate (yours)
- [x] 14. Cleanup of the replaced eval-runner code, done inside Steps 9-12 (D4)
- [x] 15. Docs: evaluation guide (every task, section 6a with the scores table and the ranking flow), learnings Phase 2

## Current Step
### 13. Phase 2 real runs (yours)
With Langfuse keys set, Docker up and the notes ingested:
1. `... --task write --repeat 2 --note "baseline"`, then `... --task stream --note "baseline"`.
2. `... --task feedback --repeat 2 --note "baseline"`.
3. `... --task retrieval --note "baseline"`.
4. `... --task generation --repeat 1 --pause-seconds 15 --sheet logs/blind.md --note "baseline"`; rank `logs/blind.md` (optionally rate and note sets) **before** opening Langfuse; `... --task ranking --sheet logs/blind.md`, then run ranking a second time.
5. Check in Langfuse: runs named by what they tested; metadata, description and scores present; the three generation arms side by side; `human_rank` (and ratings) on the arm results and not duplicated after the second ranking; stream generations nested under their case; `criterion_spread_max` on the last feedback run; whether the Experiments page averages item scores (needed to compare `human_score` across runs).
6. Paste what you saw; it goes into `learnings.md` §7 (AC20).

## Changes Made
Suggested commit message (you commit):

    feat(evals): record decide and retrieval runs as Langfuse experiments

    Each decide repeat and each retrieval run is now a Langfuse experiment run of its dataset, so two runs can be
    compared case by case in the Langfuse UI instead of diffing saved console output. Runs carry metadata (commit,
    model, prompt version, flags; for retrieval the embedding model, threshold and a notes fingerprint), an optional
    --note as their description, per-case scores (plus `errored`) and run scores computed from the console's own
    summaries. Cases run one at a time in case-file order; the task never raises, a Langfuse failure falls back to
    running the rest locally, and without keys the console is unchanged except a last line saying nothing was
    recorded. Retrieval now stops before any call when the database is down or the notes are not ingested.

    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

Files: `app/core/ai/tracing.py`, `app/modules/interviews/tooling/{interviews_eval_runs.py (new), interviews_evals.py, interviews_rag_evals.py}`, `tests/fake_langfuse.py` (new), `tests/core/ai/test_tracing.py`, `tests/modules/interviews/tooling/{test_eval_runs.py (new), test_retrieval_eval.py (new), test_evals.py}`, `docs/evaluation-guide.md`, `docs/features/langfuse-experiments/{spec,plan,task,learnings}.md`.

Phase 2 suggested commit message (you commit; Phase 1's message above covers Steps 1-6):

    feat(evals): every eval task records Langfuse experiment runs; ranking posts your judgement

    write, stream, feedback and generation now record each repeat as a Langfuse experiment run (generation: one run per
    arm, so A, B and C sit side by side), named by what they tested and carrying metadata, per-case and run scores. The
    blind sheet gains optional Rating and Note lines; ranking posts human_rank, the rubric scores and their mean onto
    each arm's result with stable ids, so a second read updates rather than duplicates. The trace-per-case loops,
    session labels and run tags the experiments replace are removed. generation stops before any call when the notes
    are not ready. A follow_up_decision_v2 prompt (completeness first) is added as an experiment; the app still uses v1.

    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

## Test Results
- Phase 2: `uv run pytest`: 1605 passed, 6 skipped, 2 failed (both baseline: `test_config`, timing-flaky `test_turn_budget`). Tooling tests 261 passed. `uv run --with ruff ruff check .`: 64 (baseline). C901 at 15: clean. `graphify update .` run.
- Step 8: `test_tracing.py` 50 passed (2 new). Step 9: `test_evals.py` (write/stream section rewritten on the experiment fake). Step 10: `test_feedback_evals.py` (main-level tests rewritten). Steps 11-12: new `test_generation_eval.py` (18 tests).
- Step 12 retry: 1 of 2 attempts used. `test_a_rejected_post_lets_the_rest_go_on_and_is_counted` expected `(Langfuse rejected them)` but the message is `(Langfuse rejected them; see the warnings above)`; the test's wording was wrong, the behaviour right.
- Step 1: `tests/core/ai/test_tracing.py` 48 passed (10 new).
- Step 2-3: `tests/modules/interviews/tooling/test_eval_runs.py` 19 passed (new file).
- Step 4: `tests/modules/interviews/tooling/test_evals.py` 87 passed (10 new test functions, one parametrized three ways; 8 decide tests migrated, see Deviations).
- Step 5: `tests/modules/interviews/tooling/test_retrieval_eval.py` 11 passed (new file).
- Full suite: `uv run pytest`: 1578 passed, 6 skipped, 1 failed (baseline `test_config`, below). The timing-flaky baseline passed this run.
- `uv run --with ruff ruff check .`: 64 errors, same as the recorded baseline; none in touched files. C901 at 15 on `app/modules/interviews` and `app/core/ai`: clean (`main` was 17 after Step 4; the trace loop moved into `_run_traced`).
- `graphify update .` run.

## Tests Pending
- Step 13 (AC20): real runs of write, stream, feedback, retrieval, generation and ranking; checks listed under Current Step.
- `retrieval` real run (left from Step 7).
- Confirming which `decide` pair was v1 via `prompt.decision` in its metadata. (`follow_up_decision_v2`: decided 2026-11-14, keep v1; the uncommitted v2 file is gone, so its contract test was removed. The v2 text survives in the traces of `decide/20261112-063054`.)

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | every current item once, named run, URL, trace id per item | spec | AC1 | pass |
| T2 | 1 | off tracer: None, nothing called | spec | AC8, EC1 | pass |
| T3 | 1 | case-file order kept when the fetch is reversed | spec | AC6 | pass |
| T4 | 1 | removed case not run, its item kept | spec | AC9, EC6 | pass |
| T5 | 1 | edited case updates its item; run sees the new input | spec | AC9, EC7 | pass |
| T6 | 1 | concurrency 1, run name, description, metadata reach the SDK | spec | AC2, AC6, AC21 | pass |
| T7 | 1 | item and run evaluators reach the run | spec | AC3 | pass |
| T8 | 1 | sync fails / item missing / run fails / fails mid-run: None, never raises, class name only | spec | EC2, EC3 | pass |
| T9 | 2 | metadata all strings, missing value is a dash | spec | AC2 | pass |
| T10 | 2 | git: clean hash read-only, `-dirty`, `unknown` | spec | AC2, EC10 | pass |
| T11 | 2 | unique run name per repeat and arm | spec | EC5 | pass |
| T12 | 2 | notes fingerprint changes with one note, not with order | spec | AC2 | pass |
| T13 | 2 | blank note: no description; long note cut to 300 | spec | EC20, EC21 | pass |
| T14 | 2 | no keys: all local, no SDK call | spec | EC1, AC8 | pass |
| T15 | 2 | keys: one run, BOOLEAN/NUMERIC scores, run score | spec | AC1, AC3 | pass |
| T16 | 2 | readable output carries the scores | inferred | readable results | pass |
| T17 | 2 | Langfuse failing: every case runs exactly once | spec | EC2, EC3 | pass |
| T18 | 2 | a bug in a case re-raised after the run; the case ran once | code-derived | SDK drops raising items | pass |
| T19 | 3 | last line names runs and links, or says why not recorded | spec | AC7 | pass |
| T20 | 4 | decide: one run per repeat, one result per labelled case, distinct names | spec | AC1, EC5 | pass |
| T21 | 4 | decide metadata: commit, model, prompt, effort, repeat | spec | AC2, EC11 | pass |
| T22 | 4 | `--note` is every repeat's description | spec | AC21 | pass |
| T23 | 4 | decide case scores incl. over/under-probing and errored | spec | AC3 | pass |
| T24 | 4 | run scores equal the console summary | spec | AC4 | pass |
| T25 | 4 | provider error: failed, errored, run goes on | spec | EC4 | pass |
| T26 | 4 | console identical with/without keys except the last line | spec | AC7, AC8 | pass |
| T27 | 4 | keyless: git not read, no Langfuse call | spec | AC8, EC1 | pass |
| T28 | 4 | Langfuse failures: each case once, exit 0, "not recorded" | spec | EC2, EC3 | pass |
| T29 | 4 | decide dataset mirrors labelled cases; no duplicates on re-run | spec | AC9 | pass |
| T30 | 5 | retrieval: one run, one result per case, item shape | spec | AC1, D1 | pass |
| T31 | 5 | retrieval metadata: embedding model and size, threshold, fingerprint, description | spec | AC2, AC21 | pass |
| T32 | 5 | case and run scores equal the console numbers | spec | AC3, AC5 | pass |
| T33 | 5 | output shows the top notes and the expected ones | inferred | readable results | pass |
| T34 | 5 | embedder error: failed, errored, run goes on | spec | EC4 | pass |
| T35 | 5 | console identical with/without keys except the last line | spec | AC7, AC8 | pass |
| T36 | 5 | no notes / other embedding model / DB down: stop before any call | spec | AC10, EC8 | pass |
| T37 | 5 | label-set rules still refuse | spec | EC9 | pass |
| T38 | 5 | `run_rag_task` passes the note, no repeat for retrieval | spec | D1, AC21 | pass |

## Open Questions
- None for Phase 1. Everything UI-side is checked by you in Step 7.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits` (pre-existing).
- `tests/modules/interviews/routes/test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only` (pre-existing, real-clock timing flake; passed this run).

## Known Issues
- An unreachable Postgres can take about two minutes to fail (driver connect timeout), so the retrieval preflight still waits that long before printing its message. Not changed here.
- Steps 2-5 slices after the first ones passed on first run because the code written for the first slice already handled them; they were kept as regression tests.

## Deviations from Plan
- Phase 2 deviations D4-D7 are recorded in plan.md: cleanup done inside Steps 9-12 (old loops became unreachable), notes preflight for generation, readable run names, `Tracer.score` returns whether sent.
- Finding: the migrated tests for write/stream/feedback keep every assertion the old trace-path tests made (scores per check, detail comments, error class, hints, readable output, dataset mirror, stream nesting, outage) on the experiment fake; the trace-input shape tests now check the dataset item (the case itself) because experiment results show the item as their input. `test_without_langfuse_the_output_has_no_langfuse_line` became `test_without_langfuse_only_the_last_line_mentions_it` (spec AC7: a last line always says what was recorded). The eval-langfuse "a failed dataset upsert still scores the cases" behaviour changed on purpose: with no synced dataset nothing is recorded (spec EC3).
- Finding (Step 7, your first real runs): run names were only a time (`decide/20261112-063054/r1`) in UTC, so in the Langfuse list you could not tell the baseline from the new run, and the time did not match the list's local timestamp. -> Run names now say what was tested before when: `decide/<prompt version>/<model>/<local time>/r<n>` and `retrieval/threshold-<t>/notes-<fingerprint>/<local time>/r1`; `--note` is also copied into the run metadata as `note`. Tests: `test_eval_runs.py::test_a_run_name_says_what_was_tested_before_when_it_ran`, `test_evals.py::test_the_run_name_says_which_prompt_and_model_it_tested`, the note assertions in `test_each_run_carries_what_produced_it` and the retrieval metadata test. -> plan.md unchanged (naming detail).
- Finding: 8 existing `test_evals.py` tests checked `decide` through the old trace-per-case path, which Step 4 replaces on purpose (spec: decide moves to experiments). -> Each was moved onto the experiment fake with all its assertions kept (verdict, decided vs expected, reply, hints, case_passed comment, over/under-probing, dataset mirror); none deleted or loosened. `hints_of` reads decide hints from the experiment output. -> plan.md unchanged (consistent with Step 4).
- Finding: retrieval's preflight also stops when the ingested notes were embedded with another model (otherwise every case scores 0 silently). -> In scope of EC8 ("notes are ingested" for the embedder in use); covered by `test_notes_embedded_with_another_model_stop_before_any_call_or_run`.
- Finding: an embedder error used to crash the retrieval run; it is now an errored, failed case (EC4), printed as `ERROR: <class>` on its line.
- Finding: `main()` went to C901 17 after Step 4. -> The old per-case trace loop moved into `_run_traced` (no behaviour change; all old tests pass).
- Finding: `run_rag_task` now builds the eval tracer for retrieval too and opens the database through a small `_session()` helper (so a test can pass its own session).

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 0 | langfuse | SDK source spike (in plan.md) |
| all | lean-ctx | reads, searches, test runs |
| all | graphify | plan findings reused; `graphify update .` after code changes |
| 1-5 | tdd / test | red -> green per slice at the confirmed seams |

## Links
- Spec: docs/features/langfuse-experiments/spec.md
- Plan: docs/features/langfuse-experiments/plan.md
- Learnings: docs/features/langfuse-experiments/learnings.md

---

## Validation Checklist (Phase 1, before your gate)
- [x] Phase 1 code steps (1-6) complete
- [x] Full test suite green apart from the recorded baseline
- [x] Phase 1 code acceptance criteria (AC1-AC11, AC13, AC21) met and covered by passing tests; AC12 is your Step 7
- [x] Open Questions: none
- [x] No skipped, deleted or loosened tests; migrated tests listed under Deviations
- [x] task.md updated
- [x] learnings.md written; pending items match Tests Pending
- [ ] Commits (yours)
- [ ] Step 7 gate (yours)
