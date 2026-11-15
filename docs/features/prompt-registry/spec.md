# Feature: Prompt Registry (one place for prompt versions and routing)

## Problem
A developer cannot easily tell which prompt file an LLM call sends. The version names are plain strings in four separate spots of a 756-line `interviews_constants.py`. Which version a task uses is spread over constructor defaults and positional arguments: `WindowLedger` defaults to v4, `FullHistory` to v1, the streamed task hardcodes v5, and `WithInterviewData(plain, V7, V8)` receives the notes and profile versions positionally. Six prompt files are loaded into module globals at import time in `interviews_utils.py`, and the renderers take those globals as misleading `template=` defaults (`render_interviewer_v2_prompt` defaults to the v2 file although v4, v5, v7 and v8 pass their own). The reason each version exists lives only in comments above constants. The eval arms and the tests name versions by their own constants. `interviews` and `profile` each carry their own copy of `load_prompt` and `PROMPTS_DIR`.

## Goal
One file answers "which prompt does task X send when the call carries plain / notes / profile data, and why does each version exist", and what is sent to the model does not change. Measured by:
- a registry holds a catalog entry (status and one-line reason) for every file in `interviews/prompts/` and the routing tables from task and data variant to version;
- `WithInterviewData`, `build_context_manager`, the eval arms and the prompt loading read their versions from the registry, not from literals or positional arguments;
- guard tests fail when the catalog, the files and the routes drift apart;
- every payload the app sends is identical before and after (existing fingerprint and context tests pass with no assertion edited).

## Project Conventions
- Rule files consulted: `CLAUDE.md` (project root; there is no `.claude/` folder), `docs/features/layered-modules/spec.md` (spec style and the layer rules), the code via lean-ctx and a graphify query.
- Constraints from those rules:
  - Layer rules: the registry is a constants-type module and must not import upward (no controller, service, route or repository). Files keep the `interviews_` prefix and live in an existing folder (no new layer folder). Layer test `tests/test_layers.py` must stay green.
  - "Prompts are data, not inline strings": prompt text stays in versioned `.md` files; this feature changes where the version names live, not the text.
  - "Shared, feature-agnostic helpers go in `app/core/`, not duplicated across modules": the reason `load_prompt` moves to core.
  - Never edit a shipped prompt in place (stored replies and logs name the version).
  - Git: never commit, push or stage; `uv run pytest` and ruff after the change with real results reported; `graphify update .` at the end.
  - No new dependency.
- Decided with the user (this conversation):
  - In scope: the registry (catalog and routing tables), keyword-argument routing in `WithInterviewData` / `build_context_manager`, eval arms read from the registry, guard tests, lazy loading with startup validation, one shared `load_prompt` in `app/core`.
  - Out of scope: merging the `render_*_prompt` functions into one `render()`.
  - Dead versions get a status in the catalog; **no prompt file is moved or renamed** (tests read `prompts/interviewer_v1.md` by path, and `interviews_evals` lists `prompts/*.md`).
  - Old constant names (`INTERVIEWER_V8_PROMPT_VERSION`, ...) stay **permanently** as one-line aliases of the registry.
  - A live prompt that is missing or broken makes the app **refuse to start**.
  - Eval runs may use **any catalogued version**, archived ones included.
  - The eval-only `full_history` baseline (v1) is routed as an `experiment` version.
  - The profile module's prompt (`profile_extract_v1`) is **not** in the registry; that module only reuses the shared loader.
- Assumptions made explicit (say so if wrong):
  - Pure refactor: no prompt text, API, database, migration, log format or behavior change.
  - Status is recorded in the catalog for every version (including v6 as archived), because the "routes never point at an archived version" guard needs it.
  - `interviewer_v6` and `interviewer_v6_json` are not referenced by any constant or code today (verify in the plan).

## User Flow
The "user" is the developer working in the repo.

1. Opens the registry and reads the routing tables: for the JSON route (task `interviewer_turn`) and the stream route (`interviewer_stream`), the version for plain / notes / profile calls; the single version of the decision, summary and feedback tasks; the `experiment` full-history baseline.
2. Reads the catalog beside it: each version's status (live / experiment / archived) and the one line saying why it exists.
3. Ships a new prompt: adds the `.md` file, adds a catalog entry, changes one routing entry. The guard tests fail until all three agree.
4. Runs an eval arm or `--prompt <version>` and gets the version named in the registry; archived versions still run.
5. Starts the app: every live version is loaded and checked once; a broken one stops startup with an error naming it.

## Requirements

### Functional

**Registry** (one module in an existing folder, data only)
- Catalog: one entry per file in `interviews/prompts/` (17 today) with name (file stem), status and a one-line reason. The reasons come from the comments now above the constants.
- Initial statuses (confirm in the plan):

| Status | Versions |
|---|---|
| live | `interviewer_v4`, `interviewer_v5`, `interviewer_v7`, `interviewer_v7_json`, `interviewer_v8`, `interviewer_v8_json`, `follow_up_decision_v1`, `job_description_summary_v2`, `feedback_score_v2`, `feedback_write_v1` |
| experiment | `interviewer_v1` (full_history baseline) |
| archived | `interviewer_v2`, `interviewer_v3`, `interviewer_v6`, `interviewer_v6_json`, `feedback_score_v1`, `job_description_summary_v1` |

- Routing tables keyed by data variant (`plain`, `notes`, `profile`):
  - JSON route: plain `interviewer_v4`, notes `interviewer_v7_json`, profile `interviewer_v8_json`.
  - Stream route: plain `interviewer_v5`, notes `interviewer_v7`, profile `interviewer_v8`.
  - Single-version tasks: decision `follow_up_decision_v1`, summary `job_description_summary_v2`, feedback score `feedback_score_v2`, feedback write `feedback_write_v1`.
  - Full-history baseline: `interviewer_v1` (experiment).
- The registry docstring says how to add a version (file, catalog entry, route).

**Wiring**
- `WithInterviewData` takes its routing by keyword (the table, or `notes_version=` / `profile_version=`), never positional version names. Its behavior (variant choice, limits, the drop order profile then notes, the `counts` labels) is unchanged.
- `build_context_manager` has no version literal or positional version constant; its `prompts` override (the eval runner's `--prompt`) still works.
- Eval arms in `interviews_rag_evals.py` and the version helpers in `interviews_evals.py` / `interviews_feedback_evals.py` read versions from the registry and report the same version strings as before. `interviews_evals --prompt` lists every catalogued version.
- `interviews_constants.py` keeps the old `*_PROMPT_VERSION` names as one-line aliases of the registry (permanent); the long history comments move to the catalog's reasons.

**Loading**
- One `load_prompt` in `app/core/` (takes the prompts directory) with a cache; `interviews` and `profile` use it and no module keeps its own copy.
- The six import-time globals in `interviews_utils.py` (`INTERVIEWER_PROMPT`, `INTERVIEWER_V2_PROMPT`, `SUMMARY_PROMPT`, `DECISION_PROMPT`, `FEEDBACK_SCORE_PROMPT`, `FEEDBACK_WRITE_PROMPT`) and the `template=` defaults that point at them go away; the renderers get their template from the registry route at call time. The `render_*_prompt` functions stay separate (out of scope to merge).
- A startup check loads every live version once and verifies the placeholders in each file are all ones its renderer supplies; any failure stops startup with an error naming the version (and the placeholder).

**Guard tests** (new, under `tests/modules/interviews/`)
- Every file in `prompts/` has a catalog entry, and every entry has a file.
- Every routed version exists in the catalog and is `live` or `experiment`, never `archived`.
- The JSON and stream routing tables have the same variant keys, each covering `plain`, `notes` and `profile`.
- Every live version renders with no unfilled placeholder (reuses the approach of `test_context_prompts.py`).
- Each failure message names the task / variant / version or file involved.

### Non-Functional
- **Behavior**: identical payloads, `prompt_version` labels (log lines, Langfuse metadata, stored rows), status codes and question-bank fallbacks. No prompt `.md` file is edited or moved.
- **Security / privacy**: unchanged; no new data enters prompts or logs.
- **Performance**: no extra work per request; each prompt file is read once (cached) instead of at import.
- **Delivery**: `uv run pytest` and ruff show no new failure against the recorded baseline; `graphify update .` is run; nothing is committed.

## UX Requirements
N/A: no user-facing change. Developer ergonomics: failures name the version and the file.

## Constraints
- Importers of the version constants today include `interviews_context.py`, `interviews_utils.py`, `interviews_evals.py`, `interviews_rag_evals.py`, `interviews_feedback_evals.py` and several tests (`test_profile_context.py`, `test_context_strategies.py`, `test_context_prompts.py`); they keep working through the aliases.
- `test_context_prompts.py` reads `PROMPTS_DIR / "interviewer_v1.md"` by path, so file locations cannot change.
- `test_profile_context.py` holds recorded fingerprints of the no-profile payloads; it is the main proof that nothing sent changed.
- `profile` keeps its own `prompts/` folder and `PROFILE_PROMPT_VERSION`.

## Blockers
None blocking the spec. Left to the plan:
- Which existing folder holds the registry (`constants/` or `ai/`) so the layer test stays green.
- How the startup check and the guard test know which placeholders each renderer supplies without merging the renderers (declare a set per family, or render with sample values).
- The signature and location of the shared loader in `app/core/` (and whether the cache keys on directory plus version).
- Exact initial statuses (the table above is proposed from the code, not yet verified file by file).

## Edge Cases
- **EC1:** A new `.md` file is added to `prompts/` with no catalog entry -> the guard test fails and names the file.
- **EC2:** A catalog entry has no file -> the guard test fails and names the version.
- **EC3:** A routing table points at an `archived` version -> the guard test fails and names the task, variant and version.
- **EC4:** The JSON and stream tables differ in variant keys, or one lacks `plain`, `notes` or `profile` -> the guard test fails.
- **EC5:** A live prompt file is missing at startup -> the app refuses to start; the error names the version.
- **EC6:** A live prompt has a `{{placeholder}}` its renderer does not supply -> startup is refused and the guard test fails; the message names the version and the placeholder.
- **EC7:** An eval run asks for an archived version (for example `--prompt interviewer_v2`) -> it loads and runs like today; status does not block evals.
- **EC8:** An interview with no notes and no profile -> every payload is identical to before (the recorded fingerprints still match).
- **EC9:** A follow-up write of an interview that has notes or a profile -> still uses the plain version and carries neither block (existing test unchanged).
- **EC10:** A notes-and-profile interview is over the size limit -> the same trimming order as today (older history, then the profile, then the notes) and the same counts.
- **EC11:** Existing code or a test imports `INTERVIEWER_V8_PROMPT_VERSION` or another old constant -> it resolves to the string the routing table returns.
- **EC12:** The profile module builds its extraction prompt -> same text as before, loaded through the shared helper.
- **EC13:** `load_prompt` gets a version with no file (a typo in `--prompt`) -> the same `FileNotFoundError` as today, naming the path.
- **EC14:** `graphify-out/` is stale after the change -> `graphify update .` is run at the end.

## Acceptance Criteria
- [ ] **AC1:** The registry exists in one module and has a catalog entry (name, status, reason) for each of the 17 files in `interviews/prompts/`.
- [ ] **AC2:** The routing tables return, for the JSON route plain / notes / profile, `interviewer_v4` / `interviewer_v7_json` / `interviewer_v8_json`; for the stream route `interviewer_v5` / `interviewer_v7` / `interviewer_v8`; and `follow_up_decision_v1`, `job_description_summary_v2`, `feedback_score_v2`, `feedback_write_v1` and the `interviewer_v1` baseline for the other tasks (asserted by a test).
- [ ] **AC3:** No `"interviewer_v..."`, `"feedback_..._v..."`, `"follow_up_decision_v..."` or `"job_description_summary_v..."` string literal remains in `app/` outside the registry (and the alias lines it feeds); `WithInterviewData` and `build_context_manager` take versions by keyword from the registry.
- [ ] **AC4:** All existing tests pass with no assertion edited, including the recorded no-profile fingerprints in `test_profile_context.py`; the diff of `tests/` outside the new guard tests is imports only, or empty.
- [ ] **AC5:** The eval arms A to E resolve their versions through the registry and still report `interviewer_v5`, `interviewer_v7`, `interviewer_v7`, `interviewer_v8`, `interviewer_v8`; `interviews_evals --help` and its `--prompt` choices list all 17 versions.
- [ ] **AC6:** The guard tests listed under Functional exist and pass, and each has a case proving it fails (checked with synthetic data, not by editing app code).
- [ ] **AC7:** The six import-time prompt globals are gone from `interviews_utils.py`; importing `interviews_utils` reads no prompt file; prompts are read once through the cached shared `load_prompt`.
- [ ] **AC8:** The startup check exists, runs when the app starts, and fails with a message naming the version when a live file is missing or a placeholder is unsupplied (tested with synthetic input).
- [ ] **AC9:** `app/core/` holds the one `load_prompt`; `interviews` and `profile` both use it; no `def load_prompt` or `PROMPTS_DIR / f"{version}.md"` copy remains in either module.
- [ ] **AC10:** Each old `*_PROMPT_VERSION` constant is importable from `interviews_constants.py` and equals the registry value (asserted by a test).
- [ ] **AC11:** No file under `interviews/prompts/` or `profile/prompts/` is changed, moved or renamed; no Alembic file is added or changed.
- [ ] **AC12:** `uv run pytest` shows no new failure against the recorded baseline, ruff reports nothing new on the touched files, the layer test passes, and `graphify update .` has been run.

## Out of Scope
- Merging the `render_*_prompt` functions into one `render()` (touches many tests for no behavior gain; the guard test covers placeholders).
- Splitting `interviews_constants.py` or `interviews_context.py`.
- Composing prompts from shared fragments, and renaming or moving prompt files (shipped versions stay immutable and stored data names them).
- Putting the profile module's prompt in the registry.
- Logging the data variant per call, or changing the `prompt_version` label.
- Removing the old constant aliases.
- Editing older `docs/features/*`.
