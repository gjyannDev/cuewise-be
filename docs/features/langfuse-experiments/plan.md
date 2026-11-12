# Implementation Plan: Langfuse experiments for the interviews evals

## Overview
Move the eval tasks onto Langfuse SDK experiments so each run becomes a comparable run in the Langfuse UI, with run metadata (commit, prompt, model, notes) and stable score names. Phase 1 pilots `decide` and `retrieval`; after your go/no-go gate, Phase 2 moves `write`, `stream`, `feedback` and `generation`, posts your blind rank as `human_rank`, and removes the replaced code.

## Architecture & Design
- **One new `Tracer` method** (`core/ai/tracing.py`) wraps the SDK: sync the dataset by item id, fetch it, keep only the current case ids, call `run_experiment` with concurrency 1, and return a small record (run name, experiment id, URL) or `None` when nothing was recorded. The evals files still never import the SDK (convention from eval-langfuse).
- **One small new tooling module** (`tooling/interviews_eval_runs.py`) holds what both eval files share: read-only git state, the run metadata, the run name per repeat, the notes fingerprint, and a helper that runs the cases either as an experiment or in the plain local loop, finishing locally whatever the experiment did not run.
- **The task function never raises.** The SDK drops an item whose task raises (it vanishes from results and run scores), which breaks "a missing case is not a passing case". The task runs the case with the existing code (`run_decide_case`, the retrieval ranking), prints the same console lines, and returns a plain dict that carries the result and its scores. Errors come back as data (`errored`).
- **Scores come from existing code.** The item evaluator turns the dict's precomputed scores into evaluations (reusing `scores_for`, plus `errored`); the run evaluator calls the same `summarize` / `summarize_decisions` / retrieval averages the console uses, so console and Langfuse cannot disagree (AC4, AC5).
- **Retrieval reuses one per-case computation** for the console line and the scores, so the numbers are identical by construction.

## Spike findings (Step 0, done against installed `langfuse 5.1.0` source)
- `Langfuse.run_experiment(name, run_name, data, task, evaluators, run_evaluators, max_concurrency=50, metadata: Dict[str,str])` returns `ExperimentResult` with `run_name`, `item_results`, `run_evaluations`, `experiment_id`, `experiment_url` (None if the project id cannot be resolved).
- A **sync** task is called inline (`task(item=item)`), so a sync provider call works; with concurrency 1 the loop is simply blocked per item. Evaluators may return dicts (name, value, comment, data_type, ...), which are normalised to `Evaluation`.
- Metadata is attached to every item's trace. Item scores attach to the trace and task observation; run scores attach through `dataset_run_id == experiment_id`.
- **An experiment is recorded only through exported traces; no dataset-run API call is made.** Runs with the same `run_name` on the same dataset share one experiment id, so each repeat needs its own run name.
- Experiment traces get environment `sdk-experiment` (forced). A task that raises is logged and dropped from `item_results`.
- Items given as `DatasetItem` objects link to the dataset; `DatasetClient.items` is the full list, so filtering to current ids needs the `Langfuse`-level call.
- Still unverified (real runs, Steps 7 and 13): scores and metadata as shown in the UI, the compare view labels, v4 readiness, whether a repeated `score_id` updates the score on the server, and `stream` nesting.
- Phase 2 facts (read in the code and SDK): `create_score` takes `score_id`, `trace_id` and `observation_id`; `ExperimentItemResult` has `trace_id` and `item`; Langfuse may return dataset items in another order than the case file (the feedback level-gap pair needs the earlier case first); the app's own services use `Tracer.trace`, `score` and `set_trace_output`, so only the eval-runner loops are removable; `run_stream_case` calls `portal.call` from inside the task, which anyio allows from a thread that is not the portal's, and copies the caller's context for the streamed call.

## Spec Requirements -> Implementation
- Dataset runs, one result per current case (AC1, AC9, EC6, EC7) -> Steps 1, 4, 5
- Run metadata, git state, per-repeat names (AC2, EC5, EC10, EC11) -> Steps 2, 4
- Score names and run-level scores (AC3, AC4, AC5) -> Steps 4, 5
- Concurrency 1 (AC6) -> Step 1
- Unchanged console + final line (AC7) -> Steps 4, 5
- No keys / Langfuse failures / sync failure (AC8, EC1, EC2, EC3) -> Steps 1, 2, 4, 5
- Errored items (EC4) -> Steps 4, 5
- Retrieval preflight and case-set rules (AC10, EC8, EC9) -> Step 5
- Tests with fakes, no real calls (AC11) -> every step
- Gate (AC12) -> Step 7
- Docs (AC13) -> Step 6
- Phase 2 (AC14 to AC20, EC12 to EC19) -> Steps 8 to 15
- Run note (AC21, EC20 to EC22) -> Steps 1, 2, 4; rubric ratings and notes in the sheet (AC22, AC23, EC23, EC24) -> Steps 11, 12

## Implementation Steps

**Phase 1**
0. **Spike.** Done (findings above). — Test: skip
1. **`Tracer.run_experiment`** in `core/ai/tracing.py`. Guarded like the other `Tracer` methods (class name logged, never raised). Steps: return `None` when tracing is off; sync via the existing `upsert_dataset` and return `None` if it fails (EC3); fetch the dataset; keep only items whose id is in the current set, **in the order the caller gave them**, and return `None` if any current id is missing from the fetch (never run a partial set); call `run_experiment` with the given run name, optional description, string metadata, task, evaluators, run evaluators and `max_concurrency=1`; return a small record (run name, experiment id, URL, and **the trace id per item id** from the item results, which Phase 2 needs). — Test: first. Seam: `Tracer.run_experiment` with a fake client (user-confirmed). Slices: off tracer returns None and calls nothing (AC8, EC1); upsert failure returns None (EC3); only current ids reach the task, stale ignored (AC9, EC6); items reach the task in case-file order even when the fetch returns them reversed (AC6); an edited item's new input is what is upserted (EC7); concurrency is 1, run name, description and metadata reach the client (AC2, AC6, AC21); the record carries a trace id per item id; a client error during the run returns None, never raises (EC2); missing item after sync returns None.
2. **Run helpers module** `tooling/interviews_eval_runs.py`: read-only git commit and dirty marker (fixed arguments, `--no-optional-locks`, no shell; `unknown` when git is missing or fails); run metadata builder (strings only: task, commit, model, prompt version(s), flags, repeat number; retrieval extras: embedding model and dimensions, threshold, notes fingerprint); run name with a repeat suffix; fingerprint of the active chunks' content hashes; the run description built from `--note` (cut to 300 characters); the helper that runs cases as an experiment or locally and finishes only the cases the experiment did not run. — Test: first. Seam: those public functions (user-confirmed). Slices: all metadata values are strings (AC2); `-dirty` and `unknown` (EC10); `--prompt`/`--model` are what is recorded (EC11); distinct run names per repeat (EC5); fingerprint changes when one hash changes; no keys means the local loop with no SDK call (EC1); a None record after partial execution runs only the remaining cases (no repeated LLM calls); a blank note gives no description (EC20); a note over 300 characters is cut with an ellipsis (EC21).
3. **Console final line.** One line naming the run(s) and the link, or saying nothing was recorded (no keys, Langfuse failing, sync failed). Lives in the helpers module. — Test: first (through Steps 4 and 5).
4. **Wire `decide`** in `interviews_evals.main()`: for the decide task, each repeat builds the dataset items (existing `dataset_items`), looks cases up by item id, and runs through the helper. The task runs `_run_one` and `_print_case` exactly as today and returns a dict (verdict, scores, errored); the item evaluator uses `scores_for` plus an `errored` score; the run evaluator computes `pass_rate`, `decision_accuracy`, `over_probing_count`, `under_probing_count`, `errored_count` from the same results the console summary uses. Add a `--note` option to the CLI parser and pass it to the helper as the run description (ignored for tasks not yet moved, EC22). Other tasks keep today's loop untouched. — Test: first. Seam: `main()` with `FakeProvider` and an injected `Tracer` (existing, user-confirmed). Slices: keys set creates one run per repeat with one result per case (AC1); the note becomes every repeat's run description (AC21); metadata and per-repeat names (AC2, EC5); score names match the table (AC3); run scores equal the console summary (AC4); a provider error counts failed, `errored` true, run continues (EC4); console identical to a keyless run except the last line (AC7); no keys unchanged (AC8); Langfuse failing still exits 0 (EC2).
5. **Wire `retrieval`**: make `_run_retrieval` public (`run_retrieval`) taking the tracer and run metadata inputs; add a retrieval dataset builder (id prefix `retrieval:`, input = query, role, level; expected output = the note keys; metadata = kind); a preflight that stops with a clear message when the database is unreachable or no notes are ingested, before any call or run (EC8); one per-case computation shared by the console line and the scores (`vector_*`, `filter_*`, `errored`); run scores `vector_recall_at_5`, `vector_mrr`, `filter_recall_at_5`, `filter_mrr`, `errored_count`; the threshold sweep stays console-only. `--repeat` is ignored: one run (deviation D1). `run_rag_task` passes the tracer and settings for metadata. — Test: first. Seam: `run_retrieval` with `FakeEmbedder`, the SQLite `db` fixture and a fake client (user-confirmed). Slices: one run, one result per case (AC1); scores and run scores equal the console numbers (AC3, AC5); metadata has embedding model, threshold, fingerprint (AC2); stale and edited items (AC9); preflight with an empty corpus or a failing database stops with exit 1 and creates no run (AC10, EC8); label-set problems still refuse (EC9); an embedder error counts as errored and failed (EC4); keyless unchanged (AC7, AC8).
6. **Docs and learnings.** Add "compare runs in Langfuse" to `docs/evaluation-guide.md` for the moved tasks (score names, metadata keys, how to name a baseline; Parts 6 and 7 gain a Langfuse path; `sdk-experiment` environment note); write the feature's `learnings.md` explaining datasets, experiments, evaluators and why this shape. — Test: skip
7. **Real run and gate (yours).** With Langfuse keys set: `--task decide --repeat 2` on the unchanged prompt, then once with a changed prompt or model; `--task retrieval`. Verify in the UI: runs appear on the Experiments page, metadata and scores show, the compare view lines two runs up, errored items behave, the final-line link opens. Record the comparison and a go/no-go in `learnings.md` (AC12). — Test: after

**Phase 2** (starts only after the Step 7 gate says go)
8. **`Tracer.score` takes an optional stable score id**, passed to the SDK's `create_score`; behaviour without it is unchanged. — Test: first. Seam: `Tracer.score` with the fake client (existing, user-confirmed). Slices: the id reaches the client (AC17, EC13); no id, same call as today; a failing post is swallowed (EC17).
9. **`write` and `stream` join the experiment path** in `main()`. The decide task, the write task and the stream task share one path: the task runs `_run_one` and `_print_case` as today and returns a dict built from `trace_output` (verdict, reply, decided against expected, hints, case notes) plus tokens and the precomputed scores, so Langfuse shows the hints; the item evaluator is the Step 4 one; the run evaluators are per task kind (`pass_rate`, `errored_count`, `finish_length_count`, `avg_latency_ms`, and `avg_first_token_ms` for stream), computed with the existing `summarize`. Dataset name comes from `dataset_name` (stream shares write); metadata adds strategy, notes and summary flags and reasoning effort; the run name tells write from stream. `run_stream_case` keeps its portal call and context copy, now inside the task. — Test: first. Seam: `main()` with `FakeProvider` and an injected `Tracer`. Slices: a write run per repeat with one result per case (AC14); score names per the table (AC3); stream shares the write dataset but its runs are named and marked `task=stream` in their metadata; `avg_first_token_ms` only on stream runs; run scores equal the console summary; the output dict carries hints; an errored case continues (EC4); keyless unchanged (AC8). Nesting of stream generations: Test: after (Step 13).
10. **`feedback` joins the path.** `run_feedback` uses the same helper; the header line and per-case lines are unchanged; its closure keeps the dict of earlier results so `level_gap_check` still finds the earlier case (cases run in file order, AC6); per-case output is `feedback_trace_output` plus scores, with scores from `feedback_scores_for` and `errored`; run evaluators from `summarize_feedback` (`pass_rate`, `valid_reply_rate`, `overall_in_band_rate`, `quotes_rejected_count`, `template_text_count`, `errored_count`); with repeat above 1, after the last run each case's `criterion_spread_max` is posted with `Tracer.score` on that case's trace id from the last record, using a stable score id; the console spread line is unchanged. The `tracer.step` chains inside `run_feedback_case` nest under the item automatically. — Test: first. Seam: `main()` with `--task feedback` and `FakeProvider` (as the existing feedback tests). Slices: one run per repeat with one result per case (AC15); score names; order kept and the level-gap check sees the earlier result (AC6); an errored earlier case skips the gap check as today (EC18); spread posted only on the last run and only when repeating (EC19); run scores equal the console summary; keyless unchanged (AC8).
11. **`generation` joins the path.** Rename `_run_generation` to a public `run_generation`; add a generation dataset builder (item id `generation:<setup id>`, input the setup and job description, metadata the skills to look for). For each repeat and each arm, run the helper: the task does `_arm_notes`, `simulate_main_questions` and the `--pause-seconds` wait, and returns the notes' competencies, the questions, the mean prompt tokens, `start_ms` and an errored flag (a question with no token count means a provider error). The item evaluator is `run_scores` plus `prompt_tokens`, `start_ms`, `errored`; the run evaluators produce the `_mean` scores and `errored_count`. Metadata adds the arm, its prompt version (v5 for A, v6 for B and C), embedding model, threshold and notes fingerprint. The console table still comes from the collected results through `summarize_arm`; the sheet still uses repeat 1 and the key is unchanged, but under each question set it now has an optional `Rating:` line (four numbers from 1 to 5: fit, relevance, variety, specificity) and an optional `Note:` line, explained in its intro; `blind.traces.json` (setup, then arm, then trace id) is written only for recorded results (user-confirmed third file). — Test: first. Seam: `run_generation` with `FakeProvider`, `FakeEmbedder`, the `db` fixture and a fake client. Slices: three runs per repeat, one per arm, of one dataset (AC16); score names and run scores; arm metadata and prompt versions; the sheet has the Rating and Note lines under every set and still names no arm (AC22); console table, sheet and key identical with and without a tracer (AC16, AC7); traces file written when recorded and absent without keys (EC14); an arm failing for a setup leaves it off the sheet but recorded for the other arms (EC15); a provider error marks the item errored (EC4).
12. **`ranking` posts `human_rank`.** Rename `_run_ranking` to a public `run_ranking` taking the tracer; `run_rag_task` builds the eval tracer for ranking. After `read_rankings` accepts the sheet, read `blind.traces.json` if it exists; extend `read_rankings` to also return each set's rating and note, refusing a malformed `Rating:` line with its line number like the other sheet errors; for each graded setup and each arm with a trace id post `human_rank` (the arm's position, 1 = best), and when the set was rated also `human_fit`, `human_relevance`, `human_variety`, `human_specificity` and their mean `human_score` (a `-` relevance is skipped), and post a set's note as the comment on that arm's `human_rank`; every score id is the score name plus the trace id; count and print what was not posted; the tally printing, the refusal message and exit codes are unchanged. Nothing is posted when the sheet is refused (the existing refusal returns before). — Test: first. Seam: `run_ranking` with a fake client recording scores. Slices: ranks posted per arm result by position (AC17); a rated set posts the five rubric scores with the mean (AC23); a blank rating skips only the rubric scores (EC24); a malformed rating refuses the sheet and posts nothing (EC23); a note becomes the comment on that arm's rank (AC23); a second read posts the same score ids (EC13); a refused sheet posts nothing; a missing traces file or Langfuse off prints the tally and says why (EC12); an arm without a trace id is skipped and counted (EC16); a rejected post lets the rest continue (EC17).
13. **Phase 2 real runs and gate (yours).** With keys set, one run each of `write`, `stream`, `feedback --repeat 2`, `generation` and then rank the sheet and run `ranking` twice. Check in Langfuse: scores and metadata, the three arms side by side, `human_rank` present and not duplicated, stream generations nested under their case, spread on the last feedback run. Record in `learnings.md` (AC20). — Test: after
14. **Cleanup (AC18)**, only after Step 13 passes so the old path stays available until the new one is proven: remove the per-case trace-and-score loops and `set_trace_output` calls in the eval files, `run_tags`, `trace_input`, `feedback_trace_input`, the session label and `last_trace` bookkeeping, and the direct dataset upserts in the eval files, with their tests. Keep `Tracer.trace`, `score` and `set_trace_output`; confirm each removal with a search for remaining callers first. Run the full suite, ruff on touched files and `graphify update .`. — Test: after
15. **Docs (AC19).** Update `docs/evaluation-guide.md` Parts 6, 7 and 12 for the five Langfuse flows (run, compare, rank before opening traces, post and read `human_rank`, the `--note` habit, the rubric ratings and notes), and add Phase 2 to the feature's `learnings.md`. — Test: skip

## Affected Files & Patterns
- `app/core/ai/tracing.py` — `Tracer.run_experiment` and its small record (run name, experiment id, URL, trace id per item id); an optional stable `score_id` on `Tracer.score` (Phase 2); follow the `_safe` guard and class-name-only logging; reuse `upsert_dataset`. `Tracer.trace`, `score` and `set_trace_output` stay: the answer, start and feedback services use them.
- `app/modules/interviews/tooling/interviews_eval_runs.py` — new; imports neither eval file (avoids the existing import cycle); reused by every task in Phase 2.
- `app/modules/interviews/tooling/interviews_evals.py` — decide, then write and stream, through the shared path in `main()`; the `--note` option; an `errored` score wrapper around `scores_for`; pass the tracer to `run_rag_task` (already done); Phase 2 cleanup of the trace loop, `run_tags`, `trace_input`.
- `app/modules/interviews/tooling/interviews_feedback_evals.py` — `run_feedback` onto the shared path, spread posting, cleanup of its trace loop and `feedback_trace_input` (Phase 2).
- `app/modules/interviews/tooling/interviews_rag_evals.py` — public `run_retrieval`, retrieval dataset builder, preflight, shared per-case computation; Phase 2: public `run_generation` with its dataset builder and `blind.traces.json`, public `run_ranking` posting `human_rank`, the rubric scores and notes; the sheet builder and `read_rankings` gain the `Rating:` and `Note:` lines.
- Tests: `tests/core/ai/test_tracing.py` (seam 1 and the `score_id` slice), new `tests/modules/interviews/tooling/test_eval_runs.py` (seam 4), `test_evals.py` (decide, write, stream via `main()`), `test_feedback_evals.py` (feedback via `main()`), `test_rag_evals.py` (`run_retrieval`, `run_generation`, `run_ranking`), plus a shared fake Langfuse client with `get_dataset`, `run_experiment` and `create_score` that mimics the SDK (calls the task and evaluators per item in order, returns item results with trace ids, honours `max_concurrency`, applies the "raising task is dropped" rule so the tests prove our task never raises, and records every posted score).
- Docs: `docs/evaluation-guide.md`, `docs/features/langfuse-experiments/learnings.md`.
- New local file: `logs/blind.traces.json` next to the sheet (git-ignored, like the sheet and key).
- Reusable patterns: the `RecordingClient` and injected `Tracer(client, propagate=...)` pattern in `test_evals.py`; `dataset_items`, `scores_for`, `feedback_scores_for`; `summarize`, `summarize_decisions`, `summarize_feedback`, `summarize_arm`; `trace_output` and `feedback_trace_output` for the readable output with hints.
- Risks: experiments exist only as exported traces, so a down exporter records nothing (covered by EC2); same `run_name` on one dataset merges runs (per-repeat and per-arm suffix); Langfuse may return items in another order (the order is restored from the case file); the SDK may change (pinned `>=5.1.0`, the plan names the version spiked); a `human_rank` score attached to the trace may not show in the compare view the way the item scores do (checked in Step 13).

## Testing Strategy
- Framework & command: `uv run pytest tests/core/ai/test_tracing.py tests/modules/interviews/tooling -q` while working; `uv run pytest` before finishing; `uv run --with ruff ruff check <touched paths>` (do not reformat the repo); `graphify update .` after code changes.
- Coverage map:

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 1, 4, 5 | first | one result per current case |
| AC2 | 2, 4, 5 | first | strings only; retrieval extras |
| AC3 | 4, 5 | first | names from the spec table |
| AC4, AC5 | 4, 5 | first | run scores equal the console numbers |
| AC6 | 1, 10 | first | client receives `max_concurrency=1`; case-file order kept, also when the fetch is reversed |
| AC7 | 3, 4, 5, 11 | first | compare keyless output with keyed output minus the last line |
| AC8 | 1, 4, 5, 9, 10 | first | no SDK call without keys |
| AC9 | 1, 4, 5 | first | no duplicates, stale ignored, edit updates |
| AC10 | 5 | first | preflight stops before any call |
| AC11 | all | first | fakes only |
| AC12 | 7 | after | real Langfuse, yours |
| AC13 | 6 | skip | doc review |
| AC14 | 9 | first | stream nesting itself: after (Step 13) |
| AC15 | 10 | first | |
| AC16 | 11 | first | console table, sheet and key identical with and without a tracer |
| AC17 | 8, 12 | first | |
| AC18 | 14 | after | search for remaining callers, then full suite |
| AC19 | 15 | skip | doc review |
| AC20 | 13 | after | real Langfuse, yours |
| AC21 | 1, 2, 4 | first | description reaches the client; blank and long notes |
| AC22 | 11 | first | rating and note lines present, no arm named, parser reads filled and blank |
| AC23 | 12 | first | rubric scores, mean, comment, stable ids |
| EC1 to EC4 | 1, 2, 4, 5, 9, 10, 11 | first | |
| EC5 | 2, 4 | first | retrieval excepted (D1) |
| EC6, EC7 | 1, 4, 5 | first | |
| EC8, EC9 | 5 | first | |
| EC10, EC11 | 2 | first | |
| EC12, EC16, EC17 | 8, 12 | first | |
| EC13 | 8, 12 | first | same score id on a second read; that the server updates by id: after (Step 13) |
| EC14, EC15 | 11 | first | |
| EC18, EC19 | 10 | first | |
| EC20, EC21, EC22 | 2, 4 | first | |
| EC23, EC24 | 12 | first | |

- Must verify, not assume (Step 7, real Langfuse): the compare view labels and what it shows for metadata; scores on items and run-level scores in the UI; that `experiment_url` opens the right page; v4 readiness of the project (cutover Nov 16, 2026 on Cloud). (Step 13): the server updating a `human_rank` score posted twice with the same id; that a trace-level `human_rank` shows next to the item scores in the compare view; `stream` generations nested under their case; spread scores on the last feedback run; the three arm runs side by side; that the run description from `--note` is shown; whether the Experiments page averages item-level scores per run (so `human_score` can be compared across runs; if not, add a run-level mean).
- Open questions: none.
- Known baseline failures: `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`; `tests/modules/interviews/routes/test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only` (real-clock timing flake). Neither is in the affected area.

## Blockers & Resolutions
- Dataset runs need `run_experiment`, which reverses eval-langfuse's "keep the loop" decision -> resolved with you for the moved tasks only; unmoved tasks keep today's loop.
- A raising task drops the item -> the task catches and returns errors as data (EC4).
- Items missing after sync would hide cases -> `Tracer.run_experiment` returns None, the run falls back to local; never a partial experiment.
- Fallback after a partial experiment must not repeat LLM calls -> the helper runs only the remaining cases.
- git state must not touch your index -> read-only commands with `--no-optional-locks`.
- No keys or Langfuse down -> local loop, same output (EC1, EC2).

## Trade-offs & Rationale
- Extend `Tracer` instead of a new experiments module: it already owns every SDK call; one more method is the smallest change that keeps the "no SDK import in evals" rule.
- Scores computed in the task, evaluators pass them on: the checks need the full `CaseResult` (tokens, raw reply), which the serialised output would lose; reusing `scores_for` keeps names stable and avoids a second copy of the rules.
- Metadata instead of tags and session ids: the SDK forces environment `sdk-experiment` and groups by run name; the run's metadata carries what tags carried (user-confirmed).
- Retrieval ignores `--repeat`: deterministic, and each repeat would cost 21 embedding calls for the same numbers (user-confirmed).
- Phase 2 is fully planned now (user request) but still starts only after the Step 7 gate; if the gate changes how runs should look, Phase 2 steps are amended before they are built.
- A third local file (`blind.traces.json`) instead of putting trace ids in the key: the key keeps its single job (the blinding answer) and its reader is untouched (user-confirmed).
- Removal of the old loops comes last (Step 14), after the real Phase 2 runs, so the old path stays as a fallback and a comparison until the new one is proven.
- Keep `Tracer.trace`, `score` and `set_trace_output`: the application's services use them, so only the eval-runner's own loops and helpers are removed.
- Arms as runs: one experiment per repeat and arm costs three dataset syncs of five items instead of one, which is negligible, and it makes the compare view show A, B and C side by side.
- A rank is only relative within one sheet, so cross-run comparison uses the optional 1-to-5 rubric scores (a 4 means the same in every run); the rank stays because it is the fast, forced choice.
- Memory aids are small and optional: `--note` records the reason and prediction at run time, a per-set `Note:` records why you ranked as you did. The run-level mean of `human_score` is not posted; it is added only if the Experiments page does not aggregate item scores itself.
- Console unchanged: the existing guide and habits keep working while Langfuse becomes the comparison place.

## Deviations from Spec (to apply to spec.md)
- **D1:** `retrieval` always makes one run and ignores `--repeat` (spec AC1/EC5 say one run per repeat). Amended in spec.md.
- **D2:** moved tasks do not keep session id and tags; they appear under environment `sdk-experiment` on the Experiments page, and the metadata carries the run identity. This resolves the spec's tags/session assumption.
- **D3:** the sync-failure fallback (EC3) and the fallback after a partial experiment both run locally; only the remaining cases are run, so no LLM call repeats.
- **D4 (found in /implement, Phase 2):** Step 14's cleanup is done inside Steps 9 to 12, not after Step 13. Once a task moves, its old trace loop has no caller, and leaving it meant unused locals (lint) and untested code; the last commit still holds the old path if Step 13 needs it. Removed: `_run_traced`, `trace_input`, `run_tags`, `EVAL_USER`, `feedback_trace_input`, `_generation_input` and the session label; their `main()`-level tests were moved to the experiment fake with their assertions kept.
- **D5:** `generation` also runs the notes preflight (`_ready_notes`): with Docker off it used to wait about two minutes per interview and record runs with no notes.
- **D6:** run names say what was tested, then when, in local time (Step 7 finding: `decide/20261112-063054/r1` told the user nothing); `--note` is also copied into the metadata as `note`.
- **D7:** `Tracer.score` returns whether the score was sent, so `ranking` can count rejected posts (EC17).

## Project Rules Applied
- Project `CLAUDE.md`: tooling stays in `interviews/tooling/` with the `interviews_` prefix; tests mirror it; evals opt-in with mock LLM in unit tests; no raw content in logs (class names only); no new dependency (`langfuse` is already one); no git writes by the assistant (the helper only reads git state); graphify update after code changes; teach the why in learnings.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| graphify | eval runner, `Tracer`, dataset and score functions, related tests |
| lean-ctx | read the eval runner, retrieval runner, tracing, knowledge repository |
| langfuse (docs + skill references) | experiments, evaluators, datasets, compare view, Score Analytics notes |
| SDK source spike (`langfuse 5.1.0`) | task invocation, error handling, run grouping, metadata, URL, environment |
| grill-me | retrieval repeat, Phase 2 detail, run identity, test seams (all answered) |
| ponytail | scope cut: judge and monitoring out; one new module, one new `Tracer` method |
| security-review | skipped: no auth, no user data, synthetic cases, git called with fixed arguments and no shell |

## Ready to Implement
- All spec requirements mapped to steps; Phase 2 detailed (user request) and gated on the Step 7 result.
- Every step has a Test tag; every AC and EC is in the coverage map; Phase 2 seams confirmed by the user.
- Affected files identified.
- Blockers resolved; edge cases handled; trade-offs recorded.
- Deviations D1 to D3 flagged; D1 and D2 applied to spec.md.
