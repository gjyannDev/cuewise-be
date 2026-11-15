# Implementation Plan: Prompt Registry

## Overview
Add one registry module that holds every prompt version (catalog with status and reason, plus the task and data-variant routing tables), make the code, evals and aliases read from it, share one cached `load_prompt` in `app/core`, and add a startup check and guard tests. Nothing sent to the model changes.

## Architecture & Design
- **Registry** (`interviews/constants/interviews_prompt_registry.py`): data only. It defines the version-name constants (with their current names), a `Data` enum (plain, notes, profile), a `Status` enum, the catalog of 17 entries, the JSON and stream routing tables, and the single-version names (decision, summary, feedback score and write, full-history baseline). `interviews_constants.py` re-exports the old names from it, so every existing import keeps working.
- **Loading**: `app/core/ai/prompts.py` gets one cached `load_prompt(prompts_dir, version)`. `interviews_utils.py` binds it to `PROMPTS_DIR`; `profile_extract.py` calls it with its own folder. The six import-time globals in `interviews_utils.py` go away; the renderers resolve their template at call time.
- **Startup check**: `check_prompts(load)` in a new `utils/interviews_prompt_utils.py` renders every routed version through its real renderer with sample values (a missing file or unsupplied placeholder raises one error naming each problem). `lifespan` in `app/main.py` calls it.
- **Wiring**: `build_context_manager`, `WindowLedger`/`FullHistory` defaults, the eval arms, `interviewer_prompt_version` and the `--prompt` choices read the registry. The `WithInterviewData` signature stays; its two app call sites pass `notes_version=` and `profile_version=` by keyword.

## Approaches Considered

| Approach | Trade-offs | Chosen? |
|----------|-----------|---------|
| A. Registry as data in `constants/`, pure check function in `utils/` | Constants can re-export it with no upward import; the layer test stays green; small diff | **Yes**: spec decided the shape; `constants/` is the only folder `interviews_constants.py` may import from |
| B. Registry in `ai/` or `utils/` | `interviews_constants.py` would import upward from a folder that already imports constants | No: reverses the dependency direction |
| C. Registry that also loads and renders (class with methods) | One object does everything, but it is the merged renderer the spec put out of scope and mixes data with logic | No: YAGNI (ponytail) |
| Placeholder check 1: render with sample values through the real renderers | One source of truth (the renderer); needs a small per-family sample table | **Yes** (user choice) |
| Placeholder check 2: declared placeholder sets in the registry | Cheap, but a second list that can drift from the renderer | No |
| `WithInterviewData` refactor to a variant to ledger dict | Easier reading inside the class, but rewrites `build()` and the budget-dropping logic | No: call-site keywords meet the spec with no behavior risk (user choice) |

## Spec Requirements -> Implementation
- Catalog of 17 files with status and reason (AC1) -> Step 3
- Routing tables and single-version names (AC2) -> Step 3
- Old names stay as aliases (AC10) -> Step 4
- No version literals outside the registry (AC3) -> Steps 4, 8, 9, 11
- Keyword routing in `WithInterviewData` / `build_context_manager` (AC3) -> Step 8
- Eval arms and `--prompt` read the registry (AC5) -> Step 9
- Guard tests (AC6) -> Steps 3, 6
- Lazy loading, no import-time globals (AC7) -> Step 5
- Startup check (AC8) -> Steps 6, 7
- One shared `load_prompt` in core, profile reuses it (AC9) -> Steps 2, 5, 10
- No prompt file changed, no migration, tests green, graphify (AC11, AC12) -> Steps 1, 11 and the gate after every step
- Payloads unchanged (AC4, EC8, EC9, EC10) -> existing fingerprint and context tests, run as the gate

## Implementation Steps
Checkpoint interval: every 3 steps (after steps 3, 6, 9 and 11).

Gate commands (run after every step): `uv run pytest`, `uv run --with ruff ruff check .`, and `uv run pytest tests/test_layers.py`.

1. **Record the baseline** — Files: none — Verify: `uv run pytest` and `uv run --with ruff ruff check .`; write any failing test names into "Known baseline failures" below — Test: skip (no code; the later steps are measured against these results)
2. **Shared cached loader in core** — Files: `app/core/ai/prompts.py` (new), `tests/core/ai/test_prompts.py` (new) — Verify: `uv run pytest tests/core/ai/test_prompts.py` + gates — Test: first. Seam: `load_prompt(prompts_dir, version)` (user-confirmed). Slices, one at a time: returns the text of `<dir>/<version>.md` (AC9); a second call for the same dir and version does not read the file again; the same version name in two directories gives two texts; an unknown version raises `FileNotFoundError` naming the path (EC13).
3. **Registry module and guard tests** — Files: `app/modules/interviews/constants/interviews_prompt_registry.py` (new), `tests/modules/interviews/constants/test_prompt_registry.py` (new) — Verify: `uv run pytest tests/modules/interviews/constants/test_prompt_registry.py` + gates — Test: first. Seam: the registry's public data (`CATALOG`, the routing tables) (user-confirmed). Slices: catalog names equal the stems of `prompts/*.md` (EC1, EC2); every catalog entry has a status and a non-empty reason (AC1); JSON and stream tables cover plain, notes and profile with the same keys (EC4); no routed version is archived (EC3); the tables return exactly today's versions (AC2). Each rule is a small pure helper in the test file that takes data, with a synthetic failing case beside it (AC6). The registry docstring explains how to add a version; the version-history comments from `interviews_constants.py` become the catalog reasons.
4. **Old names become aliases** — Files: `app/modules/interviews/constants/interviews_constants.py`, `tests/modules/interviews/constants/test_prompt_registry.py` — Verify: `uv run pytest tests/modules/interviews` + gates — Test: after (one test: each old `*_PROMPT_VERSION` equals its registry value, EC11, AC10). Delete the version-string lines and their comments; re-export the same names from the registry (explicit re-export form so ruff does not flag them). `PROMPTS_DIR` stays here.
5. **Lazy loading in `interviews_utils.py`** — Files: `app/modules/interviews/utils/interviews_utils.py`, `tests/modules/interviews/utils/test_interviewer_messages.py` — Verify: `uv run pytest tests/modules/interviews tests/core` + gates — Test: skip (behavior-preserving; the fingerprint test `test_profile_context.py`, `test_context_prompts.py` and `test_feedback_prompts.py` must pass unchanged). Replace `def load_prompt` with the core loader bound to `PROMPTS_DIR`; delete the six globals; each `render_*_prompt` takes `template: str | None = None` and loads its registry version when it is None (decision and summary gain the parameter so the check can pass a template). Before making `template` required on the v2 renderer, confirm no caller omits it; otherwise default to the v2 file. The one approved test edit: `test_prompt_comes_from_the_versioned_file` uses `load_prompt(INTERVIEWER_PROMPT_VERSION)` instead of the removed global.
6. **Startup check** — Files: `app/modules/interviews/utils/interviews_prompt_utils.py` (new), `tests/modules/interviews/utils/test_prompt_check.py` (new) — Verify: `uv run pytest tests/modules/interviews/utils/test_prompt_check.py` + gates — Test: first. Seam: `check_prompts(load=...)` (user-confirmed). Slices: with the real files it passes (AC8); a loader that cannot find a routed version raises an error naming it (EC5); a template with a placeholder the renderer does not supply raises an error naming version and placeholder (EC6); several problems are reported together in one error. The renderers are called with sample values, one per family: interviewer (baseline renderer and v2-style renderer), decision, summary, feedback score, feedback write.
7. **Run the check at app start** — Files: `app/main.py`, `tests/test_startup_prompts.py` (new) — Verify: `uv run pytest tests/test_startup_prompts.py` + gates — Test: after (depends on the FastAPI lifespan). `lifespan` calls `check_prompts()` before building the provider; the test patches the check to raise and asserts startup fails, and that the normal startup still works (EC5, EC6 at app level).
8. **Wire the routing into `interviews_context.py`** — Files: `app/modules/interviews/ai/interviews_context.py` — Verify: `uv run pytest tests/modules/interviews/ai tests/modules/interviews/routes` + gates — Test: skip (pure wiring; `test_profile_context.py` fingerprints, `test_context_strategies.py`, `test_reference_note_context.py` and the follow-up tests cover EC8, EC9, EC10 and must pass with no edit). Defaults of `FullHistory` and `WindowLedger`, the two `WithInterviewData(...)` calls (keywords `notes_version=` / `profile_version=`), the stream `WindowLedger`, and the single-version names all come from the registry; the ten version imports shrink to the registry's routes.
9. **Evals read the registry** — Files: `app/modules/interviews/tooling/interviews_evals.py`, `interviews_rag_evals.py`, `interviews_feedback_evals.py`, `tests/modules/interviews/tooling/test_generation_arms.py` — Verify: `uv run pytest tests/modules/interviews/tooling` and `uv run python -m app.modules.interviews.tooling.interviews_evals --help` + gates — Test: after (one new test: `ARM_PROMPTS` A to E equal v5, v7, v7, v8, v8 from the registry, and the `--prompt` choices include every catalogued version, archived ones too, EC7, AC5). `interviewer_prompt_version` uses the stream, JSON and baseline routes; the `--prompt` validation uses the catalog names instead of the directory glob; `PROMPTS_DIR` is no longer imported there.
10. **Profile module uses the shared loader** — Files: `app/modules/profile/ai/profile_extract.py` — Verify: `uv run pytest tests/modules/profile tests/modules/interviews/ai/test_profile_redaction.py` + gates — Test: skip (wiring; the existing profile route and redaction tests cover EC12). Remove its own `load_prompt`; `build_messages` calls the core loader with its folder and `PROFILE_PROMPT_VERSION`; the folder path constant stays.
11. **Final guard and close-out** — Files: `tests/modules/interviews/constants/test_prompt_registry.py`; run `graphify update .` — Verify: full gates, plus `git diff --stat -- app/modules/interviews/prompts app/modules/profile/prompts alembic/versions` shows nothing — Test: after (one test: walk the source of `app/` with `ast` and fail on any string literal equal to a catalogued version name outside the registry, AC3). `graphify update .` last (EC14).

## Affected Files & Patterns
- New: `app/core/ai/prompts.py`; `interviews/constants/interviews_prompt_registry.py`; `interviews/utils/interviews_prompt_utils.py`.
- Changed: `interviews_constants.py` (aliases), `interviews_utils.py` (lazy loading, renderer defaults), `interviews_context.py` (routing), the three tooling files (versions and `--prompt`), `profile_extract.py` (shared loader), `app/main.py` (check at startup).
- Tests: new `tests/core/ai/test_prompts.py`, `tests/modules/interviews/constants/test_prompt_registry.py`, `tests/modules/interviews/utils/test_prompt_check.py`, `tests/test_startup_prompts.py`; edited `test_interviewer_messages.py` (one test) and `test_generation_arms.py` (one added test).
- Patterns to follow: the explicit-constants style of `interviews_constants.py`; the synthetic-source style of `tests/test_layers.py` for guard tests with failing cases; the existing `lifespan` in `app/main.py`.
- Risks: the layer test (`tests/test_layers.py`) only polices routes, controllers, services and repositories, so the new files are not constrained by it but must still import downward only; `app/core/ai/prompts.py` must not import any feature module.

## Testing Strategy
- Framework & command: `pytest` (`testpaths = ["tests"]`); `uv run pytest <path>` per step.
- Gate commands: `uv run pytest`, `uv run --with ruff ruff check .`, `uv run pytest tests/test_layers.py`; `graphify update .` at the end (CLAUDE.md).
- Coverage map:

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 3 | first | catalog and reasons |
| AC2 | 3 | first | tables return today's versions |
| AC3 | 4, 8, 9, 11 | after | literal scan in step 11 |
| AC4 | every step (gate) | skip | existing tests, one approved edit in step 5 |
| AC5 | 9 | after | arms and `--prompt` choices |
| AC6 | 3, 6 | first | each guard has a synthetic failing case |
| AC7 | 5 | skip | existing prompt tests; `interviews_utils` import reads no file |
| AC8 | 6, 7 | first, after | check function, then lifespan |
| AC9 | 2, 5, 10 | first, skip, skip | core loader tested in step 2 |
| AC10 | 4 | after | alias equality |
| AC11 | 11 | after | `git diff --stat` on prompts and alembic |
| AC12 | 1, 11 | skip | baseline compared with final gates |
| EC1, EC2 | 3 | first | |
| EC3, EC4 | 3 | first | |
| EC5, EC6 | 6, 7 | first, after | |
| EC7 | 9 | after | archived version accepted by `--prompt` |
| EC8, EC9, EC10 | 5, 8 | skip | fingerprints and follow-up tests, unchanged |
| EC11 | 4 | after | |
| EC12 | 10 | skip | profile tests |
| EC13 | 2 | first | |
| EC14 | 11 | skip | `graphify update .` |

- Must verify, not assume: `interviewer_v6*` has no reference anywhere (search before marking it archived); no caller omits `template` on the v2 renderer; no test depends on a prompt being re-read from disk after a change (the cache); the proposed statuses match each file (the live, experiment and archived lists in the spec); ruff accepts the explicit re-export form.
- Open questions: none (every EC has an expected outcome).
- Known baseline failures: to be recorded in step 1 (the earlier layered-modules work noted `test_llm_settings_default_to_off_with_documented_limits`; not rechecked).

## Blockers & Resolutions
- Where the registry lives -> `interviews/constants/` (Approaches Considered).
- How placeholders are checked without merging renderers -> render with sample values (user choice).
- Shared loader signature -> `load_prompt(prompts_dir, version)`, cached on both arguments, in `app/core/ai/prompts.py`.
- Initial statuses -> from the spec table; step 3 verifies each against the files and the references.
- AC4 conflict (one test uses a removed global) -> edit that one test (user choice); a second small deviation: `WithInterviewData` keeps its signature and only the app call sites use keywords (user choice).

## Trade-offs & Rationale
- Keeping the renderers separate means the check needs a small sample table per family; the alternative, a merged renderer, was put out of scope.
- A cache on the loader means a prompt file edited while the app runs is not reread; acceptable because shipped versions are never edited in place.
- Re-exporting through `interviews_constants.py` keeps about 30 imports untouched; the cost is one extra indirection for readers, documented in the registry docstring.

## Project Rules Applied
- `CLAUDE.md` layers -> the registry is a constants file, the check a utils file; nothing imports upward; core knows no feature.
- `CLAUDE.md` "Prompts are data" -> prompt text untouched; only versions and routing move.
- `CLAUDE.md` DRY and "shared helpers in `app/core/`" -> one `load_prompt`.
- `CLAUDE.md` Git rules -> nothing is committed, staged or pushed.
- `CLAUDE.md` workflow -> tests and ruff after each step, `graphify update .` at the end.
- `CLAUDE.md` Don'ts -> no new dependency, no edit to a shipped prompt or an applied migration.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | importers of `load_prompt`, the version constants, `WithInterviewData`, `build_context_manager`; the layer test; `main.py` lifespan |
| graphify | one query on the prompt, context and eval modules (heavily truncated; the searches above gave the detail) |
| grilling | placeholder approach, the test edit, the `WithInterviewData` signature, test seams (all user-confirmed) |
| ponytail | applied directly: no merged renderer, no dispatch rewrite, no declared placeholder sets |

## Ready to Implement
- All spec requirements mapped to steps; every step has a Test tag
- Every AC and EC mapped in Testing Strategy; no uncovered IDs
- Gate commands listed; every step names its files and verification command
- Approaches Considered filled; checkpoint interval set (every 3 steps)
- Blockers resolved; two deviations from the spec (one test edit, `WithInterviewData` call sites only) approved by the user
