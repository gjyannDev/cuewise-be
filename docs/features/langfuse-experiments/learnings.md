# Learn: Langfuse experiments for the interviews evals

> Status: **every eval task records Langfuse experiment runs; built and tested with fakes.** The Step 7 gate said
> **go** after two real `decide` command runs on 2026-11-12 (eval log below). Phase 2's real runs (Step 13) are
> **pending**: anything about the Langfuse UI for write, stream, feedback, generation and ranking is from the docs and
> the SDK source until then.

## 1. Why it exists
Comparing eval runs meant saving console output to files and diffing them, and a number found a month later could not
say which prompt, model, commit or notes produced it. Langfuse can compare runs case by case, but only *dataset runs*
(experiment runs), and the old runner sent loose traces grouped by a session label, which Langfuse cannot line up.

## 2. What it is
- **Dataset:** the cases, stored in Langfuse as items (`input`, `expected_output`, `metadata`) with stable ids.
- **Experiment run:** one execution of a task over a dataset. Each case's result is linked to its item, so two runs of
  the same dataset can be compared item by item. In SDK 5.1.0 the only supported way to make one is
  `Langfuse.run_experiment` (the older per-item helpers are gone).
- **Evaluators:** functions that turn an output into scores. *Item* evaluators score one case; *run* evaluators score the
  whole run (an average, a count). Ours only pass on scores our existing code already computed.
- **Run metadata:** strings stored on the run (commit, model, prompt version, flags, notes fingerprint). It is what makes
  an old run explain itself.

## 3. When to use it
- Every task (`write`, `stream`, `decide`, `feedback`, `retrieval`, `generation`) records this way whenever Langfuse
  keys are set; `ranking` posts your judgement onto generation's results. Compare two runs in the Langfuse UI instead of
  diffing files (`docs/evaluation-guide.md`, section 6a).
- Without keys, nothing changes: the console output is the same and the last line says nothing was recorded.

## 4. How it works
**One `decide` repeat, walked through:**
1. `main()` reads the git state once, only when keys are set (`app/modules/interviews/tooling/interviews_evals.py:846`;
   `git_commit`, `app/modules/interviews/tooling/interviews_eval_runs.py:23`: read-only, `--no-optional-locks`, no
   shell).
2. `_run_as_experiment` (`interviews_evals.py:914`) builds the run name (`run_name`, `interviews_eval_runs.py:65`: what
   was tested, then the local time, then the repeat, because Langfuse merges runs that share a name), the metadata
   (`run_metadata`, `:43`) and the description from `--note` (`run_description`, `:82`).
3. `run_cases` (`interviews_eval_runs.py:90`) hands Langfuse a task (`:120`) that runs one case with the existing code,
   prints the same console lines, and returns a readable output (verdict, reply, hints, notes, scores).
4. `Tracer.run_experiment` (`app/core/ai/tracing.py:249`) syncs the dataset by id, fetches it, keeps only the current
   ids **in the case-file order**, and calls the SDK with `max_concurrency=1` (`:283`). It returns `None` on any
   Langfuse problem and never raises.
5. The item evaluator (`interviews_eval_runs.py:135`) turns each case's precomputed scores into Langfuse scores
   (`experiment_scores_for`, `interviews_evals.py:710`: the old check scores plus `errored`). The run evaluator
   (`:139`) calls `decide_run_scores` (`interviews_evals.py:716`), built from the same `summarize` and
   `summarize_decisions` the console uses, so the console and Langfuse cannot disagree.
6. Anything the experiment did not get to (no keys, Langfuse failing mid-run) runs locally afterwards (`:158`), so no
   case is skipped and no LLM call is repeated.
7. After the repeats, the last line names the runs and their links, or says why nothing was recorded (`final_line`,
   `interviews_eval_runs.py:170`, printed at `interviews_evals.py:885`).

**The other tasks** go through the same `run_cases`:
- `write` and `stream` share the path above with their own run scores (`write_run_scores`, `interviews_evals.py:900`)
  and the interviewer prompt they actually used (`interviewer_prompt_version`, `:889`).
- `feedback` (`run_feedback`, `app/modules/interviews/tooling/interviews_feedback_evals.py:497`) keeps the earlier
  results of the repeat so the senior/junior pair still finds its junior case, and after the last repeat posts each
  case's spread with a stable id (`_post_spread`, `:596`).
- `retrieval` (`run_retrieval`, `app/modules/interviews/tooling/interviews_rag_evals.py:485`) is one run, stops before
  any call when the notes aren't ready (`_ready_notes`, `:569`), and feeds one per-case computation (`_retrieval_row`,
  `:598`) to both the console line and the scores.
- `generation` (`run_generation`, `interviews_rag_evals.py:651`) makes one run per repeat and arm of the dataset of
  setups, then writes the sheet, the key and `<sheet>.traces.json` (`_write_traces`, `:803`; a stale file is removed
  when nothing was recorded).
- `ranking` (`run_ranking`, `interviews_rag_evals.py:843`) reads the sheet (`read_rankings`, `:349`, now also optional
  ratings via `_rating`, `:388`, and notes) and posts `human_rank`, the rubric scores and their mean with ids built from
  the score name and the trace id (`_post_judgements`, `:861`).

**Decisions and why:**
- *The task never raises.* The SDK silently drops an item whose task raises, so a crashed case would vanish from the run
  and its averages. Provider errors are already results; a real bug is held and re-raised after the run
  (`interviews_eval_runs.py:157`), so it still stops the command.
- *Scores are computed by our code, not by Langfuse.* The checks need the full `CaseResult`; reusing `scores_for` keeps
  names stable between runs.
- *Metadata instead of tags and sessions.* Experiment traces get the environment `sdk-experiment`; the run's metadata
  carries what tags carried.
- *Cases in file order, one at a time.* Free-tier limits, and feedback's level-gap pair needs the earlier case.
- *Generation arms as separate runs.* The compare view then shows A, B and C side by side for the same setups.
- *Ranks plus optional ratings.* A rank only says "better than the other two in this sheet"; a 1-to-5 rating means the
  same in every run, so it is what compares across runs.
- *Stable score ids for anything posted after a run.* Spread and your judgement are posted later; a second post with
  the same id updates the score instead of adding one (to confirm on the server in Step 13).
- *Fail open.* No keys, a down Langfuse or a failed sync never changes the console results or the exit code.

## 5. What can go wrong
| Failure | What happens | Test |
|---|---|---|
| No Langfuse keys | runs locally, same console, last line says not recorded; git is not read | `tests/modules/interviews/tooling/test_evals.py::test_without_keys_decide_makes_no_langfuse_call` |
| Langfuse down, sync failing, or failing mid-run | every case still runs once, exit 0, last line says not recorded | `test_evals.py::test_a_langfuse_failure_still_runs_every_case_once_and_exits_0`, `tests/core/ai/test_tracing.py::test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only` |
| A provider error on one case | case fails, `errored` is true, the run goes on | `test_evals.py::test_a_provider_error_is_a_failed_errored_case_and_the_run_goes_on` |
| A bug in a case's code | re-raised after the run, as without Langfuse | `tests/modules/interviews/tooling/test_eval_runs.py::test_a_bug_in_a_case_still_stops_the_run_as_it_does_locally` |
| Langfuse returns items in another order | the run keeps the case-file order | `test_tracing.py::test_items_run_in_the_callers_order_even_when_langfuse_returns_them_reversed` |
| A case removed from the file | not run again; its old item stays | `test_tracing.py::test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse` |
| Two repeats with the same name | prevented: names are unique per repeat | `test_eval_runs.py::test_each_repeat_gets_its_own_run_name_so_langfuse_never_merges_them` |
| Docker off or no notes for retrieval | stops before any call with how to fix it | `tests/modules/interviews/tooling/test_retrieval_eval.py::test_an_unreachable_database_stops_with_how_to_start_it`, `::test_no_notes_ingested_stops_before_any_call_or_run` |
| Console and Langfuse disagreeing | prevented: run scores come from the console's own summaries | `test_evals.py::test_the_run_scores_equal_what_the_console_prints`, `::test_write_run_scores_equal_what_the_console_prints`, `test_retrieval_eval.py::test_case_and_run_scores_equal_the_console_numbers`, `tests/modules/interviews/tooling/test_feedback_evals.py::test_the_run_scores_equal_the_console_summary` |
| Langfuse reorders feedback's items | the senior case still runs after its junior case | `test_feedback_evals.py::test_cases_run_in_file_order_so_the_senior_case_finds_its_junior_pair` |
| A streamed call losing its case | the context is copied onto the stream's thread | `test_evals.py::test_streamed_calls_run_inside_their_case` |
| A stale traces file next to a new sheet | removed when nothing was recorded, so ranking never posts onto an old run | `tests/modules/interviews/tooling/test_generation_eval.py::test_without_keys_no_traces_file_is_written_and_a_stale_one_is_removed` |
| A malformed rating | the sheet is refused with its line and nothing is posted | `test_generation_eval.py::test_a_malformed_rating_refuses_the_sheet_and_posts_nothing` |
| Ranking twice | the same score ids, so the scores update | `test_generation_eval.py::test_reading_the_sheet_twice_posts_the_same_score_ids` |
| Langfuse rejecting posts | the rest go on; the count is printed | `test_generation_eval.py::test_a_rejected_post_lets_the_rest_go_on_and_is_counted` |

Not covered: an unreachable Postgres can take about two minutes to fail (the driver's connect timeout), so the
retrieval preflight still waits that long before printing its message.

## 6. Try it yourself
1. Predict, then run `uv run pytest tests/modules/interviews/tooling/test_eval_runs.py -k fails -q`. If Langfuse fails
   after the first case, how many times does each case run? (Once: the rest run locally.)
2. In `tests/fake_langfuse.py`, the fake drops an item whose task raises, as the SDK does. Remove the `try`/`except`
   around `run_one` in `run_cases`' task (`app/modules/interviews/tooling/interviews_eval_runs.py:112`) and predict how
   often the crashing case runs. (Twice: the SDK drops it, the next cases still run, then the local fallback runs it
   again and only then does the error surface. `test_eval_runs.py::test_a_bug_in_a_case_still_stops_the_run_as_it_does_locally`
   fails on `ran == ["a", "b"]`.)
3. Predict: you rank a sheet `Y > X > Z` and rate set X `4 - 3 5`. Which scores land on X's arm result, and what is
   its `human_score`? (`human_rank` 2, `human_fit` 4, `human_variety` 3, `human_specificity` 5, no `human_relevance`,
   `human_score` 4.0.) Check against `test_generation_eval.py::test_a_rating_posts_the_rubric_scores_and_their_mean_and_a_note_becomes_the_comment`.
4. Real runs: `decide` done (below); the other tasks are **pending** (Step 13).

## 7. What surprised me
- **The SDK drops a case whose task raises.** It logs the error and leaves the case out of the results and the run
  scores, so a crash would look like a smaller, cleaner run. Hence "the task never raises".
- **An experiment run exists only as exported traces.** There is no "create run" call; a down exporter records nothing,
  and two runs that share a name on one dataset become one run.
- **Experiment traces always land in `sdk-experiment`.** The SDK forces that environment, so a filter on `eval` will not
  find them.
- **The first real comparison could not be read.** The run names were only a UTC time (`decide/20261112-061726/r2`),
  the list's timestamps were local, and the score columns had no labels in a copy-paste. You could not tell the baseline
  from the new run. Names now say what was tested first (prompt version and model), then the local time, and `--note`
  is copied into the metadata. Score columns are listed alphabetically.
- **The decide comparison was a trade, exactly as predicted.** v2 (completeness first) removed the one over-probe and
  added one under-probe; accuracy stayed at 0.87, and both repeats of each version gave the same scores.
- **Moving `decide` broke seven old tests on purpose.** They checked the replaced trace path; each was moved to the
  experiment fake with all its assertions kept (verdict, decision vs expected, reply, hints, over/under-probing, the
  dataset mirror), none was deleted or loosened.

**Eval log** (one row per real run; numbers read from the Langfuse runs list on 2026-11-12):

| Run (local) | What changed | Versions | Summary numbers | Failures by type | Decision |
|------|--------|----------|-----------------|------------------|----------|
| 11-12 14:17 `decide/20261112-061726/r1,r2` | none: baseline | `follow_up_decision_v1` (assumed: the earlier pair; confirm `prompt.decision` in the run metadata); model in metadata | r2: decision_accuracy 0.87, pass_rate 0.87, over_probing 1, under_probing 0, errored 0; valid 15/15, injection ignored 15/15; about $0.005 a run, 4.3 s per case | 1 over-probe → quality | baseline |
| 11-12 14:30 `decide/20261112-063054/r1,r2` | `follow_up_decision_v2`: decide completeness first | `follow_up_decision_v2` (assumed, as above) | r1 and r2 the same: decision_accuracy 0.87, pass_rate 0.87, over_probing 0, under_probing 1, errored 0; about $0.005 a run, 3.6 to 4.9 s per case | 1 under-probe → quality | a trade, no gain: keep v1 recommended; **your decision pending** |
| pending | `--task retrieval` | pending | pending | pending | pending |

**Go/no-go gate (AC12): go** (2026-11-12). The two `decide` pairs above lined up case by case in Langfuse's runs list;
the comparison worked once the run names and the alphabetical score columns were understood, and led to the readable
run names (plan D6). You then asked for Phase 2.

## 8. Check your understanding
1. Why does each repeat get its own run name?
2. Why are the run scores computed by our code instead of by a Langfuse evaluator that reads the outputs?
3. Why does the task function catch every exception?
4. Why does `retrieval` ignore `--repeat`?
5. Where do you look for these runs in Langfuse, and why not under environment `eval`?

<details>
<summary>Answers</summary>

1. Langfuse derives one experiment from the dataset and the run name; two repeats with one name would merge into one
   run and hide the run-to-run noise.
2. The console summary already computes them from the full results (tokens, raw reply, checks). Reusing that code means
   the console and Langfuse cannot disagree, and score names stay stable.
3. The SDK drops an item whose task raises, so the case would silently disappear from the run. Provider errors are
   returned as results; a real bug is held and re-raised after the run.
4. With fixed notes and embeddings the result is the same every time; each repeat would cost 21 embedding calls for
   identical numbers.
5. On the Experiments page, under the dataset. The SDK puts experiment traces in the environment `sdk-experiment`.

</details>

## 9. Go deeper / Still open
- Step 13 (yours): real runs of write, stream, feedback, retrieval, generation and ranking (twice); the checks are
  listed in `task.md` under Current Step. Then the eval log rows above, and AC20.
- Your decision on `follow_up_decision_v2`, and confirming which `decide` pair was v1 from its metadata.
- Whether the Experiments page averages item scores per run (needed to compare `human_score` across runs; otherwise
  add a run-level mean), and whether a repeated score id updates on the server.
- Check your Langfuse project's v4 readiness (cutover Nov 16, 2026 on Cloud).
- Later, separate specs: an AI judge for generation calibrated on your `human_rank`/ratings (Score Analytics), and
  monitoring real interviews.
