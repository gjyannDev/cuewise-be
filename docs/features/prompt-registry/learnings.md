# Learn: Prompt registry (one place for prompt versions and routing)

**Concepts:** prompt versioning, routing a prompt by task and data variant, guard tests, fail-fast startup checks.
**Status:** built and tested 2026-11-15; a pure refactor (no prompt text and no payload changed), so there is no eval run to make.

## 1. Why it exists
Before this, answering "what does the streamed turn send when the interview has a profile?" took four files. The
version names were strings in four separate spots of the 756-line `interviews_constants.py`. The choice of version was
spread over constructor defaults (`WindowLedger` v4, `FullHistory` v1), a hardcoded v5 for the stream task, and two
positional arguments (`WithInterviewData(plain, V7, V8)`) that did not say which was notes and which was profile. Why
each version existed lived only in comments. With 17 prompt files, and more coming with every experiment, that does
not scale.

## 2. What it is
One data-only module, `app/modules/interviews/constants/interviews_prompt_registry.py`, holds:
- a **catalog**: every prompt file, with a status (`live`, `experiment`, `archived`) and one line saying why it exists;
- **routing tables**: for each interviewer task, which version goes with which data variant;
- the single version of every other task.

```
                      plain            notes                profile
interviewer_turn      interviewer_v4   interviewer_v7_json  interviewer_v8_json   (INTERVIEWER_JSON)
interviewer_stream    interviewer_v5   interviewer_v7       interviewer_v8        (INTERVIEWER_STREAM)
full_history (eval baseline) interviewer_v1 · decision follow_up_decision_v1 · summary job_description_summary_v2
feedback_score feedback_score_v2 · feedback_write feedback_write_v1                (SINGLE_ROUTES)
```

Code asks the registry ("the stream route, profile variant") instead of naming a version. Guard tests keep the
catalog, the files and the routes in agreement, and a startup check refuses to start the app if a routed prompt is
missing or has a placeholder its renderer cannot fill.

## 3. When to use it
| Do this | When | Why / limit |
|---|---|---|
| Add a version: new `.md`, catalog entry, change one route | Any prompt change | Shipped files are never edited in place; stored replies, logs and traces name the version |
| Set the old version to `archived` | It is no longer routed or compared | The guard refuses routes to archived versions; `--prompt` still runs it |
| Set it to `experiment` | Only the eval runner uses it as a baseline | Routable (full_history), never the live default |
| Use `--prompt <version>` | An ablation against any catalogued version | Replaces only the plain version of the chosen strategy |
| Keep using the old `*_PROMPT_VERSION` names | Existing imports, tests, docs | Permanent aliases of the registry; change versions in the registry, never in the aliases |

**I'd revisit this when** a second module (profile) gets several prompt versions or routes: then the registry pattern
should move to core with one registry per module, instead of profile keeping a single constant.

## 4. How it works

| Option | Trade-off | Chosen? |
|---|---|---|
| Registry as data in `constants/`, check function in `utils/` | Constants can re-export it without importing upward | **Yes** |
| Registry in `ai/` or `utils/` | `interviews_constants.py` would import from a folder that imports constants | No |
| A registry class that also loads and renders | That is the merged renderer the spec put out of scope | No (YAGNI) |
| Placeholder check: render each routed version with sample values | The renderer stays the one source of truth | **Yes** |
| Placeholder check: declared placeholder sets | A second list that can drift from the renderer | No |

One streamed answer turn on an interview with a profile, through the code:
1. At startup, `lifespan` runs `check_prompts()` first (`app/main.py:24`). It renders every routed version through its
   real renderer (`app/modules/interviews/utils/interviews_prompt_utils.py:46`) and raises one `PromptCheckError`
   listing every problem.
2. `build_context_manager` builds the stream task from the routing table: plain `INTERVIEWER_STREAM[Data.plain]`, and
   `notes_version=` / `profile_version=` by keyword (`app/modules/interviews/ai/interviews_context.py:553`). The table
   itself is `app/modules/interviews/constants/interviews_prompt_registry.py:89`.
3. Each `WindowLedger` loads its template through `load_prompt` (`interviews_context.py:157`), which calls the cached
   core loader (`app/modules/interviews/utils/interviews_utils.py:124` -> `app/core/ai/prompts.py:8`).
4. On the turn, `WithInterviewData.build` sees a profile on a main-question write (`interviews_context.py:327`) and
   uses the profile ledger (`interviews_context.py:303`): the reply is labelled `prompt_version=interviewer_v8`, the
   same string as before the refactor.

## 5. What can go wrong
| Failure | What the user sees | What the code does | Proof (test name) |
|---|---|---|---|
| A new `.md` with no catalog entry | Nothing (CI fails) | Guard names the file | `test_the_catalog_matches_the_prompt_files`, `test_a_file_without_an_entry_and_an_entry_without_a_file_are_named` |
| A route points at an archived version | Nothing (CI fails) | Guard names task, variant, version | `test_a_route_to_an_archived_or_unknown_version_is_named` |
| JSON and stream tables drift apart | Nothing (CI fails) | Guard names the missing variant | `test_a_table_missing_a_variant_is_named` |
| A routed prompt file is missing at startup | The app does not start | `PromptCheckError` names the version, before the provider is built | `test_a_missing_routed_file_is_named`, `test_a_failed_prompt_check_stops_startup_before_the_provider_is_built` |
| A prompt gains a `{{placeholder}}` its renderer lacks | The app does not start | Error names version and placeholder | `test_a_placeholder_the_renderer_does_not_supply_is_named` |
| Someone writes `"interviewer_v8"` in app code again | Nothing (CI fails) | AST scan names file and line | `test_no_version_name_is_written_outside_the_registry` |
| An old constant name drifts from the registry | — | Alias test fails | `test_the_old_constant_names_are_aliases_of_the_registry` |
| The refactor changed what is sent | Different questions | Recorded fingerprints fail | `test_profile_context.py` (unchanged, passing) |

## 6. Try it yourself
1. Predict first: which tests fail if you add an empty `app/modules/interviews/prompts/interviewer_v9.md`? Then run
   `uv run pytest tests/modules/interviews/constants -q` and compare. Delete the file afterwards.
2. Predict: which tests fail if you change `INTERVIEWER_STREAM[Data.profile]` to `"interviewer_v6"`? (The literal sits
   inside the registry, so the AST scan allows it.) Run `uv run pytest tests/modules/interviews/constants -q`, then
   compare with your prediction. Revert.
3. Run `uv run python -m app.modules.interviews.tooling.interviews_evals --prompt interviewer_v99`: the error lists
   all 17 catalogued versions, archived ones included.

## 7. What surprised me
- **Not every prompt is lazy.** Importing `interviews_utils` now reads no prompt file, but importing
  `interviews_context` still does: `CONTEXT_MANAGER = build_context_manager()` (`interviews_context.py:568`) builds
  every strategy, and each strategy's `__init__` loads its template. So a missing JSON-route file still fails at
  import, before `check_prompts` runs. The check's added value is the placeholder rendering, and the one combined
  error message.
- **The ruff gate and import order.** Every new import from `interviews_prompt_registry` landed out of alphabetical
  order (it sorts after `interviews_constants`); four `I001` fixes over the feature, all with `ruff check --fix`.
- **One test was already doing the EC7 job.** `test_the_interviewer_prompt_recorded_is_the_one_used` runs
  `--prompt interviewer_v2`, which is now archived, so "evals can run archived versions" needed no new test.
- Measurements (`uv run pytest`, 2026-11-15): baseline 2343 passed, 6 skipped, 1 failed (`test_config`, unrelated);
  after 2366 passed, 6 skipped, the same 1 failed. 23 new tests. `ruff check .`: 66 errors before and after, none in a
  touched file.

### Eval log (AI features only)
No eval run: no prompt text or payload changed (the recorded fingerprints prove it), so a run would measure the model,
not this change.

## 8. Check your understanding
1. Why does the catalog keep archived versions instead of deleting their files?
2. When would you mark a version `experiment` rather than `archived`?
3. How does the startup check find a placeholder the renderer cannot fill, without a list of placeholders?
4. What if someone passes `--prompt interviewer_v7` for the JSON route: which data variants change?

<details>
<summary>Reference answers (write yours first)</summary>

1. Stored interview rows, logs and Langfuse traces name the version; deleting the file would leave them unexplained,
   and old eval comparisons could not be repeated with `--prompt`.
2. When a route may still send it outside live traffic, as the eval-only `full_history` baseline does (interviewer_v1).
   Archived is for versions nothing routes to any more.
3. It renders each routed version through its real renderer with sample values; `render_template` raises `KeyError` on
   a placeholder it has no value for, and the check turns that into "version: no value for {{name}}".
4. Only the plain one: `build_context_manager` puts `--prompt` into the plain `WindowLedger`; notes and profile writes
   keep `INTERVIEWER_JSON[Data.notes]` and `[Data.profile]`.
</details>

## 9. Go deeper / Still open
- Spec: `docs/features/prompt-registry/spec.md`; plan: `docs/features/prompt-registry/plan.md`; task: `task.md`.
- Out of scope, next candidates: merging the `render_*_prompt` functions into one; splitting `interviews_constants.py`
  and `interviews_context.py`; logging the data variant per call next to `prompt_version`.
- Known limitation: `render_interviewer_v2_prompt` still falls back to the archived `interviewer_v2` file when no
  template is passed (behavior kept; every app caller passes its own).
