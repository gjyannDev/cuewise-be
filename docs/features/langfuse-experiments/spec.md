# Feature: Langfuse experiments for the interviews evals

## Problem
Eval runs are hard to compare. Each run prints to the terminal and, for the older tasks, sends traces and scores to Langfuse grouped only by a session label. Langfuse's run-to-run comparison works on **dataset runs**, and the current runner does not create any, so the user compares runs by saving console output to `.md`/`.txt` files, diffing them and working out noise by hand. Nothing in a run records which commit, prompt, model or notes produced the numbers, so a result found a month later cannot be explained. The new knowledge-base evals (`retrieval`, `generation`) have no Langfuse dataset at all.

## Goal
Make a run of an eval task (started with the same CLI command as today) show up in Langfuse as a **dataset run**: one result per case, scores with stable names, and metadata saying exactly what was tested, so two runs can be compared in the Langfuse UI without saving or diffing files.

Measurable:
- After the pilot (`decide`, `retrieval`), the user can pick any two runs in Langfuse and see per-case score changes, with no file diff (checked by the go/no-go gate, AC12).
- Every moved run carries the metadata fields listed in AC2.
- A run without Langfuse keys behaves exactly as today.

## Project Conventions
- Rule files consulted: project `CLAUDE.md` (no `.claude/rules/`), `docs/evaluation-guide.md`, `docs/features/eval-langfuse/{plan,task}.md`, `docs/features/knowledge-base-rag/`.
- Constraints they impose:
  - Evals are opt-in and never run in `uv run pytest`; tests use fakes (LLM, embedder and a recording Langfuse client) and make no real call.
  - AI guidelines: log metadata only (class names, not raw content); eval data is synthetic; no secrets in code; no new dependency without a stated reason (`langfuse` is already a dependency, installed `5.1.0`).
  - Tooling lives in `app/modules/interviews/tooling/` with the `interviews_` prefix; tests mirror it under `tests/modules/interviews/tooling/`.
  - Existing convention from the earlier eval-langfuse feature: Langfuse SDK calls sit behind `Tracer` in `core/ai/tracing.py`, and the evals files do not import the SDK.
  - Teach as you build: the learnings file explains datasets, experiments and evaluators and why this design was chosen.
  - Git: no commits, branches, staging or pushes by the assistant.

## User Flow
1. The user changes something AI-related (a prompt, a note, a threshold, a model) and runs the matching command, for example `uv run python -m app.modules.interviews.tooling.interviews_evals --task decide --repeat 3`.
2. The terminal prints the same PASS/FAIL lines and summary as today, plus a last line naming the Langfuse run(s).
3. In Langfuse the user opens Experiments, selects a baseline run and the new run, sees which cases changed score, filters to the items below a threshold, and opens a failing item's trace.
4. The user writes one eval-log row (the baseline run's name, the new run's name, the decision) in the feature's `learnings.md`.
5. Phase 2 only: after `--task ranking` unblinds a generation sheet, each arm's result in Langfuse also carries the user's rank.

## Requirements

### Functional

**Phase 1: pilot (`decide`, `retrieval`)**
- With Langfuse keys set, each of these tasks creates one dataset run per repeat in a Langfuse dataset (`interviews-eval/decide`, a new `interviews-eval/retrieval`), with one result per current case.
- The dataset is synced from the case file by stable item id before the run. Re-running never duplicates items. Items for cases no longer in the file are ignored (the run covers current cases only).
- Run metadata (all string values) records: the task, the git commit (short hash, with a `-dirty` marker when the working tree has uncommitted changes, `unknown` when git is unavailable), the model, the prompt version(s) in effect, the repeat number, and the eval flags used. For `retrieval` also the embedding model and dimensions, the similarity threshold in force, and a short fingerprint of the ingested notes that changes when any note changes.
- Scores use fixed names (table below), named after what they measure, identical in every run.
- Cases run one at a time (concurrency 1) and in the order of the case file, so free-tier rate limits are not hit by the runner itself and pairs that depend on an earlier case still work.
- A case that ends in an error (rate limit, provider error, context too large) counts as failed with the error class as the comment, is also flagged by an `errored` score, and the run continues.
- `--repeat N` creates N separate runs, each with the same metadata plus its repeat number. Exception: `retrieval` always makes one run and ignores `--repeat` (its result is deterministic and each repeat would cost the same embedding calls again).
- A baseline is not a stored flag: the user chooses it in the compare view and names it in the eval-log row.
- `retrieval` checks before it creates a run that the database is reachable and notes are ingested, and stops with a clear message if not.
- The terminal output of the moved tasks is unchanged (case lines, summary, sweep) plus one final line naming the run(s) and, when the SDK provides it, a link.
- The tasks not yet moved keep today's behaviour (per-case trace, scores, session, tags) until their phase.
- The retrieval threshold sweep stays console-only.
- `--note "<why I'm running this>"` is optional. When given, it becomes the description of every run that command creates (cut to 300 characters), so the reason and the prediction travel with the run. A blank note adds nothing.

**Gate between phases**
- Phase 2 does not start until the user has compared two real runs of `decide` in the Langfuse UI and recorded in `learnings.md` whether the comparison replaces the `.md` comparing.

**Phase 2: rollout**
- `write`, `stream`, `feedback` and `generation` follow the same rules as Phase 1 (dataset runs, metadata, named scores, errored handling, unchanged terminal output, cases in file order, concurrency 1).
- **`write` and `stream`:** one shared dataset (`interviews-eval/write`); the run's metadata says which task it was. Each result's output in Langfuse carries what the older traces showed: the verdict, the reply, the decided-against-expected pair where relevant, the hints and the case notes. `stream` keeps each generation nested under its case's result.
- **`feedback`:** dataset `interviews-eval/feedback` (the bands as expected output). Cases run in file order so the senior/junior pair finds the earlier case's result. With `--repeat N` above 1, each case's `criterion_spread_max` is posted after the last repeat on that case's result in the last run, as today's spread line is printed.
- **`generation`:** dataset `interviews-eval/generation`, one item per setup. For every repeat, each arm (A, B, C) is its own run of that dataset, so the compare view shows the arms side by side. Each result carries the keyword scores, cost and retrieval time; the run carries the arm and the prompt version it used. The console table stays as it is. The blind sheet and its key stay local files; the sheet gains an optional `Rating:` line and an optional `Note:` line under each question set. A third local file, `blind.traces.json` next to the sheet, saves the Langfuse trace id per setup and arm (only for results that were recorded).
- **`ranking`:** after it reads a valid sheet, each graded setup's arm results (found through the traces file) get a score `human_rank` (1 = ranked first). The score has a stable id derived from the trace id, so reading the same sheet twice updates rather than duplicates. Optionally, each question set can carry a `Rating:` line with four whole numbers from 1 to 5 (fit to role and level, relevance to the job description, variety, specificity; relevance may be `-` for a setup with no job description) and a `Note:` line with a one-line reason. After unblinding, a rated set's arm result also gets `human_fit`, `human_relevance`, `human_variety`, `human_specificity` and their mean `human_score`, and a note becomes the comment on that arm's `human_rank`. Ratings let two runs be compared directly, because a 4 means the same in both, unlike a rank, which is only relative within one sheet. Both lines are optional per set. Posting happens only after the ranking is read and unblinded, never before.
- Because experiment traces name the arm, ranking must stay before opening them in Langfuse; the guide says so.

**Score names**

| Task | Per case | Per run |
|---|---|---|
| `decide` | the existing check names (`decision`, `gap`, `valid_reply`, `injection_ignored`), `case_passed`, `over_probing`, `under_probing`, `errored` | `pass_rate`, `decision_accuracy`, `over_probing_count`, `under_probing_count`, `errored_count` |
| `retrieval` | `vector_recall_at_5`, `vector_reciprocal_rank`, `filter_recall_at_5`, `filter_reciprocal_rank`, `errored` | `vector_recall_at_5`, `vector_mrr`, `filter_recall_at_5`, `filter_mrr`, `errored_count` |
| Phase 2 | per case `write`/`stream`: the existing check names, `case_passed`, `errored`; `feedback`: `valid_reply`, the existing check names, `case_passed`, `errored`, and `criterion_spread_max` (last repeat, when repeating); `generation` (per setup and arm): `valid_share`, `distinct_competencies`, `skill_coverage` (only when the setup lists skills), `prompt_tokens` (mean per question), `start_ms`, `errored`; `ranking`: `human_rank` on each arm's result, and when the set was rated `human_fit`, `human_relevance`, `human_variety`, `human_specificity`, `human_score` | `write`/`stream`: `pass_rate`, `errored_count`, `finish_length_count`, `avg_latency_ms`, plus `avg_first_token_ms` for `stream`; `feedback`: `pass_rate`, `valid_reply_rate`, `overall_in_band_rate`, `quotes_rejected_count`, `template_text_count`, `errored_count`; `generation` (per arm run): `valid_share_mean`, `distinct_competencies_mean`, `skill_coverage_mean`, `prompt_tokens_mean`, `start_ms_mean`, `errored_count` |

### Non-Functional
- No extra LLM or embedding calls compared with today for the same task and flags.
- A Langfuse problem (down, wrong key, slow) never fails or changes a run's results; failures are logged by class name only.
- Eval data sent to Langfuse is synthetic only; real interview content never goes through this path.
- Metadata values stay short strings (commit hash, version names), no secrets and no case text beyond what traces already hold.

## UX Requirements
- The final terminal line says what was recorded, for example the run name(s), or that nothing was recorded (no keys, Langfuse failing).
- Error and fallback messages say what to do (set the keys, start Docker, run the ingest) in plain words.
- Score names and metadata keys are documented in `docs/evaluation-guide.md` and the feature's `learnings.md`, so reading the compare view needs no source code.

## Constraints
- SDK: `langfuse 5.1.0`. `run_experiment` is the only supported way to create dataset runs in this version; it takes `run_name`, a `metadata` mapping of strings, sync or async tasks, item and run-level evaluators, and `max_concurrency` (default 50).
- Free-tier LLM and embedding limits: runs must stay sequential, and the call count per task is unchanged.
- No new dependency; no change to application (non-tooling) code.
- Reverses one decision of the earlier eval-langfuse plan ("keep the loop, no rewrite onto `run_experiment`") for the moved tasks only, because dataset runs cannot be created any other supported way.

## Blockers
- None. Every decision is settled with the user. The assumptions below are checked in the plan's spike before any code is written.

### Assumptions to verify (external system behaviour)
- `dataset.run_experiment` in `langfuse 5.1.0` accepts a sync task, honours `run_name`, string `metadata` and `max_concurrency=1`, and attaches item scores to the dataset run's items and run-level scores to the run.
- ~~Traces created by an experiment can still carry the tags/session the older runs use.~~ Resolved in the plan: they do not; experiment traces use environment `sdk-experiment` and the run's metadata carries the run identity.
- The result object exposes a run name and, if available, a URL for the final terminal line.
- The Langfuse project is ready for the v4 cutover (Cloud: Nov 16, 2026), and the comparison view (including the Cloud-only Fast Preview beta) is available in the user's project with the labels the docs describe.
- Posting a score with a stable id twice updates rather than duplicates it (used by the Phase 2 re-post).
- `stream` and `generation` keep working inside `run_experiment` despite the earlier finding that the portal's thread does not inherit the trace context.
- The run `description` set from `--note` is shown in the Langfuse UI for an experiment run.
- The Experiments page averages item-level scores per run, so `human_score` can be compared across runs; if it does not, a run-level mean is added later.

## Edge Cases
Format: condition -> expected outcome.

- **EC1:** Langfuse keys are missing -> the task runs and prints exactly as today, makes no SDK call, exits 0, and the final line says nothing was recorded in Langfuse.
- **EC2:** Langfuse is down, slow or the key is wrong while a run is in progress -> the run finishes, prints its full results, exits 0, logs the failure by class name only, and the final line says the run was not (fully) recorded.
- **EC3:** The dataset sync fails (cannot create or upsert items) -> the run still executes on the local cases and prints its results; no dataset run is recorded and the final line says so.
- **EC4:** A case errors (rate limit, provider error, context too large) -> it counts as failed with the error class as comment, carries `errored`, and the run continues with the remaining cases.
- **EC5:** `--repeat 3` -> three separate runs, each with the same metadata and its own repeat number (`retrieval` excepted: one run).
- **EC6:** A case is removed or renamed in the case file -> the next run covers only the current case ids; the old Langfuse item and its history stay untouched.
- **EC7:** A case's input is edited but its id is kept -> the sync updates the item; earlier runs keep the outputs they stored.
- **EC8:** `retrieval` is started with Docker off or no notes ingested -> it stops before creating a run, prints how to fix it (start Docker, run the ingest), and exits non-zero.
- **EC9:** The retrieval case file breaks its own rules (too few synonym/vague/role-boundary cases, duplicate ids) -> the task refuses to run, as today.
- **EC10:** git is unavailable or the folder is not a repository -> the commit metadata is `unknown` and the run proceeds; uncommitted changes -> the commit carries `-dirty`.
- **EC11:** The user passes `--prompt` or `--model` -> the metadata records the prompt and model actually used, not the defaults.
- **EC12:** Phase 2: Langfuse is off or unreachable during `--task ranking`, or the sheet has no traces file -> the tally prints locally as today, no scores are posted, and the output says why.
- **EC13:** Phase 2: ranking is read twice for the same sheet -> each arm result still has one `human_rank` (the second read updates it through the stable score id) (assumption — verify the server updates by id).
- **EC14:** Phase 2: `generation` is run without Langfuse keys -> the blind sheet and key are written as today; no traces file is written; nothing is recorded in Langfuse.
- **EC15:** Phase 2: an arm fails for a setup, so that setup is left off the sheet -> the arms that did run are still recorded in Langfuse; ranking never posts for that setup.
- **EC16:** Phase 2: a graded setup has no trace id in the traces file (that arm result was not recorded) -> no score is posted for it, the others are, and the output counts what was not posted.
- **EC17:** Phase 2: a score post is rejected by Langfuse during ranking -> the remaining posts continue and the tally still prints; the output counts the failures.
- **EC18:** Phase 2 feedback: the earlier case of a senior/junior pair errored -> its `level_gap` check is skipped exactly as today.
- **EC19:** Phase 2 feedback with `--repeat 1` -> no spread score is posted (as today, no spread line).
- **EC20:** `--note` is empty or only spaces -> no description is set.
- **EC21:** `--note` is longer than 300 characters -> it is cut to 300 characters with an ellipsis.
- **EC22:** `--note` is given without Langfuse keys, or for a task not yet moved -> it is ignored, with no error.
- **EC23:** Phase 2: a `Rating:` line is malformed (not four values, a value outside 1 to 5, or `-` anywhere but relevance) -> the sheet is refused with the line number, like any other sheet error, and nothing is posted.
- **EC24:** Phase 2: a set has no `Rating:` line -> its rank is still posted, with no rubric scores for it.

## Acceptance Criteria

**Phase 1**
- [ ] **AC1:** With keys set, `--task decide` and `--task retrieval` each create one dataset run per repeat in `interviews-eval/decide` and `interviews-eval/retrieval`, with exactly one result per case in the current case file.
- [ ] **AC2:** Every such run's metadata contains the task, commit (with `-dirty` or `unknown` where EC10 applies), model, prompt version(s), repeat number and flags; `retrieval` runs also contain embedding model and dimensions, similarity threshold and the notes fingerprint. All values are strings.
- [ ] **AC3:** The scores each task sends match the score-names table exactly, with the same names in every run.
- [ ] **AC4:** For `decide`, run-level `pass_rate` and `decision_accuracy` equal the values the console summary prints for the same run.
- [ ] **AC5:** For `retrieval`, run-level `vector_recall_at_5`, `vector_mrr`, `filter_recall_at_5` and `filter_mrr` equal the console summary within rounding.
- [ ] **AC6:** Cases execute one at a time and in the order of the case file (also when Langfuse returns the dataset items in another order); a test with two cases shows the second does not start before the first finishes.
- [ ] **AC7:** The console output of both tasks is byte-identical to today's except for the added final line (name(s) of the run(s), a link when available, or the not-recorded message).
- [ ] **AC8:** Without keys, both tasks behave as EC1: same output, no SDK call, exit code 0.
- [ ] **AC9:** Re-running a task creates no duplicate dataset items; a removed case is not run (EC6); an edited case input updates its item (EC7).
- [ ] **AC10:** EC8 holds: with the database unreachable or no notes ingested, `retrieval` creates no run, prints the fix and exits non-zero.
- [ ] **AC11:** `uv run pytest` covers AC1 to AC10 and EC1 to EC11 with a fake LLM provider, a fake embedder and a recording Langfuse client, and makes no real call.
- [ ] **AC12 (gate):** `learnings.md` records a comparison of two real `decide` runs made in the Langfuse UI (baseline against a changed prompt or model), the run names, and a go/no-go decision on Phase 2.
- [ ] **AC13:** `docs/evaluation-guide.md` explains how to start a run and compare two runs in Langfuse for the moved tasks (score names, metadata keys, how to pick and name a baseline), replacing "save the output and diff" for those tasks.

**Phase 2**
- [ ] **AC14:** `write` and `stream` satisfy AC1 to AC9 for `interviews-eval/write` (the run metadata names the task); their scores match the table, run scores equal the console summary, and each result's output carries verdict, reply and hints.
- [ ] **AC15:** `feedback` satisfies AC1 to AC9 for `interviews-eval/feedback`; cases run in file order; with `--repeat N` above 1, `criterion_spread_max` is posted for each case on the last run (EC19: not at 1).
- [ ] **AC16:** `generation` records, per repeat, one run per arm in `interviews-eval/generation` with the per-setup scores and per-arm run scores in the table; the console table, blind sheet and key are identical to today's for the same results; with keys, `blind.traces.json` maps each setup and arm to its trace id (EC14, EC15).
- [ ] **AC17:** After `--task ranking` reads a valid sheet, each graded arm result found in the traces file carries `human_rank` (1 = best) with a stable score id; a refused sheet posts nothing; EC12, EC13, EC16 and EC17 hold.
- [ ] **AC18:** Eval-runner code the experiments fully replace is removed, not left unused: the per-case trace-and-score loops in the evals files, the run tags and trace-input helpers, and the direct dataset upserts. `Tracer.trace`, `Tracer.score` and `Tracer.set_trace_output` stay, because the application services use them.
- [ ] **AC19:** `docs/evaluation-guide.md` describes the Langfuse flow for `write`, `stream`, `feedback`, `generation` and `ranking`, including "rank before opening the traces".
- [ ] **AC20 (Phase 2 gate):** `learnings.md` records one real run each of `write`, `stream`, `feedback` and `generation` plus `ranking`, with these checked in the Langfuse UI: scores and metadata present, the three arms side by side, `human_rank` visible and not duplicated on a second read, `stream` generations nested under their case, and spread scores on the last feedback run.
- [ ] **AC21 (Phase 1):** `--note` text becomes the description of every run the command creates; a blank note sets none; a note over 300 characters is cut (EC20, EC21, EC22).
- [ ] **AC22 (Phase 2):** the generated blind sheet has an optional `Rating:` line and `Note:` line under every question set, explained in its intro, still names no arm, and is read correctly whether those lines are filled or left blank.
- [ ] **AC23 (Phase 2):** after ranking, each rated set posts the five rubric scores on its arm result and each note posts as the comment on that arm's `human_rank`, all with stable ids; EC23 and EC24 hold.

## Out of Scope
- **AI judge for generation and Score Analytics validation.** Needs 2 to 3 of the user's own rankings first; its own spec.
- **Monitoring and online evaluators on real interviews.** Needs a decision about sending real interview content to a model; its own spec.
- **Annotation queues, dashboards, alerts.** Not needed for comparing runs.
- **Langfuse Prompt Management and UI-started experiments.** They only run a prompt plus a model, not the retrieval/DB pipeline, and would move prompts out of versioned repo files.
- **CI gating (`langfuse/experiment-action`).** Would spend real API calls on every change; revisit with a paid tier.
- **Changing case files, eval checks, prompts, retrieval logic or any application code.** This feature only changes how runs are recorded.
- **Recording the retrieval threshold sweep as scores.** Console-only for now; add if threshold tuning becomes frequent.
