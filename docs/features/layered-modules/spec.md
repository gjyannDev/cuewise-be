# Feature: Layered Modules (route -> controller -> service -> repository)

## Problem
Every feature module is a flat folder where the layer is only a filename suffix (`interviews/` holds 20 `.py` files side by side), and the layer called "controller" is really a service: `interviews_controller.py` (728 lines) mixes business rules, LLM orchestration and repository calls with request-level work (response shaping, SSE framing, upload checks, the 200 vs 201 choice). Two methods are very complex (`stream_answer` cyclomatic complexity 28, `transcribe` 26). The name also clashes with the usual meaning of "controller" (the thin HTTP layer), so the structure is hard to read and the real service logic has no home.

## Goal
Every feature module has one folder per layer, and the request flows through four layers with one job each. Behavior does not change. Measured by:
- `auth/`, `users/` and `interviews/` contain no layer file at the module root; each layer lives in its own folder (see Functional);
- the former `InterviewsController` is gone: its logic lives in four services, with four thin controllers in front of them;
- `uv run pytest` and `uv run --with ruff ruff check .` show no new failure or error against the recorded baseline after every delivery step, with no test assertion edited;
- the OpenAPI document is identical before and after.

## Project Conventions
- Rule files consulted: `CLAUDE.md` (project root; there is no `.claude/rules/`), `docs/evaluation-guide.md` (the evals command path), the existing specs under `docs/features/` for style. graphify (`graph.json`), lean-ctx and the code were used for orientation.
- This feature **changes** these `CLAUDE.md` rules, which therefore must be updated first:
  - "Architecture: Modular, Feature-Driven": the request flow becomes route -> controller -> service -> repository; the tree shows layer folders.
  - "File naming": the `<feature>_` prefix stays, now inside the layer folder (`services/interviews_service.py`).
  - "Layers only call downward" and "Features don't import each other's repositories; go through the other feature's controller": the cross-feature entry point becomes the other feature's **service**.
  - "Enforce authorization (ownership checks) in controllers": ownership checks live in **services**.
  - `core/errors.py` docstrings that say "controllers raise these" become "services raise these".
- Constraints those rules impose on this feature, which stay in force:
  - Git: never commit, push, stage, amend or reset. Files are moved with plain `mv`, not `git mv`.
  - Alembic: no new migration and no edit to applied ones (a pure refactor).
  - Tooling: lean-ctx for exploration and edits, `graphify update .` after the code changes, `uv run pytest` and ruff after each step with real results reported.
  - Schemas, security, error handling and AI guidelines are unchanged: services keep raising the structured errors from `core/errors.py`; no raw errors reach clients.
- Decided with the user (this conversation):
  - **Layer folders inside each feature module** (not top-level `app/services/` etc.).
  - **Four layers**: route (HTTP declaration) -> controller (thin) -> service (business logic) -> repository (database).
  - **Services return domain objects** (ORM rows, dataclasses). **Controllers build the response schemas** (`feedback_out`, `_question_out`, SSE `StreamEventOut`).
  - **`data/`, `prompts/` and `templates/` stay at the module root**; one shared module-root constant replaces the five `Path(__file__).parent` expressions.
  - **Delivery module by module**: 1) `CLAUDE.md` rules, 2) `auth` and `users` as a rehearsal, 3) `interviews`, 4) mirror the folders in `tests/`.
  - **Interviews gets 4 services and 4 controllers, 1:1**, behind a single `APIRouter` (one router per feature stays).
  - **An automated import-direction test** (stdlib `ast`, no new dependency).
  - **`interviews_utils.py` and `interviews_constants.py` move as-is** into `utils/` and `constants/`.
  - **Living docs only**: `CLAUDE.md` and `docs/evaluation-guide.md` are updated; the older `docs/features/*` stay as written.
  - The `<feature>_` filename prefix stays; non-layer interviews files go to `ai/` and `tooling/`.
- Assumptions made explicit (say so if wrong):
  - Pure refactor: no API, database, migration, prompt or behavior change.
  - Routes keep the framework plumbing they have today (`run_in_threadpool`, `UploadFile.read`, `EventSourceResponse`, setting the 200 status).
  - No compatibility shims: the old module paths simply stop existing.

## User Flow
The "user" is the developer working in the repo.

1. Opens a feature folder and sees one folder per layer, with the same names in every feature.
2. Follows a request: `routes/<feature>_route.py` -> `controllers/<feature>_controller.py` -> `services/<feature>_service.py` -> `repositories/<feature>_repository.py`.
3. Finds business rules, ownership checks and LLM orchestration only in `services/`, and response shaping, SSE framing and upload checks only in `controllers/`.
4. If a change breaks the layer direction (for example a route importing a repository), the layer test fails and names the file and the import.
5. Runs the offline tools from their new path, for example `uv run python -m app.modules.interviews.tooling.interviews_evals --task feedback`.

## Requirements

### Functional

**Layer responsibilities**
- **route**: path, status code, dependencies, `response_model`, `responses=`. Calls controllers only.
- **controller**: maps validated input to a service call and the domain result to a response schema; owns HTTP-shaped decisions (200 vs 201 flag, SSE event framing, upload content-type and size checks). No repository, no LLM, no database session.
- **service**: business rules, ownership checks, state transitions, LLM orchestration, repository calls. Raises the structured errors. Returns domain objects, never response (`*Out`) schemas.
- **repository**: database access only.

**Target layout per feature module**
```
app/modules/<feature>/
  routes/  controllers/  services/  repositories/  schemas/  utils/      (always present)
  models/  dependencies/  constants/                                      (only when the feature has them)
  ai/  tooling/                                                           (interviews only)
  data/  prompts/  templates/                                             (interviews only, stay at the module root)
```
- Every file keeps its `<feature>_` prefix: `services/interviews_service.py`, `routes/auth_route.py`.
- Each folder has an empty `__init__.py` (no re-exports).

**Interviews mapping**

| Today | Target |
|---|---|
| `interviews_route.py` | `routes/` |
| `interviews_controller.py` (728 lines) | 4 services in `services/` and 4 controllers in `controllers/` (below) |
| `interviews_feedback_controller.py` | `services/interviews_feedback_service.py` + `controllers/interviews_feedback_controller.py` (`feedback_out` moves to the controller) |
| `interviews_repository.py` | `repositories/` |
| `interviews_schema.py` | `schemas/` |
| `interviews_model.py` | `models/` |
| `interviews_dependencies.py` | `dependencies/` |
| `interviews_utils.py`, `interviews_constants.py` | `utils/`, `constants/` (as-is) |
| `interviews_turn.py`, `interviews_feedback_turn.py`, `interviews_context.py`, `interviews_reply.py`, `interviews_feedback.py` | `ai/` |
| `interviews_evals.py`, `interviews_feedback_evals.py`, `interviews_report.py`, `interviews_report_render.py`, `interviews_log.py` | `tooling/` (offline only, used by `app/scripts` and tests) |

**The four interviews services** (each with a controller of the same name)
- `interviews_service`: start, get, list, transcript, plus question selection and the job-description summary.
- `interviews_answer_service`: prepare an answer, finish it, and the streamed answer.
- `interviews_transcription_service`: audio transcription.
- `interviews_feedback_service`: generate and get the feedback (the former `FeedbackController`).

**Auth and users**: `AuthController` becomes `AuthService` (`register`, `login`, `authenticate_token`, `ensure_admin`) with a thin `AuthController` in front for the routes; `UsersController` likewise. `app/scripts/create_admin.py` and any non-HTTP caller use the **service**.

**Layer check**
- One test under `tests/` using stdlib `ast`. It fails when: a route imports a service or repository; a controller imports a repository; a service imports a controller, a route or a response (`*Out`) schema; a repository imports a service, controller or route; any feature imports another feature's repository.
- The message names the file and the forbidden import.

**Moves that must keep working**
- The module-root resource folders (`data/`, `prompts/`, `templates/`) are found from every moved file.
- CLIs run from their new paths (`app.modules.interviews.tooling.*`, `app.scripts.*`).
- `app/db/models.py` still registers every model, so Alembic discovery is unchanged.

**Documentation**
- `CLAUDE.md` (architecture tree, file naming, layer rules, ownership-check rule, workflow wording) and `docs/evaluation-guide.md` (the evals command) are updated.
- Comments and docstrings that call the business-logic layer "controller" are updated.
- Older `docs/features/*` are not edited.

**Tests**
- `tests/modules/<feature>/` mirrors the layer folders; each existing test file moves under the layer it mainly exercises.
- Tests that built a controller directly (`AuthController(repo)`, the interviews fixtures) now build the service, and the controller around it where they go through one. Only imports and wiring change; no assertion changes and no test is deleted.

### Non-Functional
- **Behavior**: identical responses, status codes, SSE events, error codes, logs and database writes. Log lines stay readable by the log parser (logger names are fixed strings like `app.llm`, not module paths, so the move does not change them).
- **Security**: default-deny auth and ownership checks are unchanged, only relocated from the controller to the service; the existing authorization tests keep passing.
- **Delivery**: each step ends with `uv run pytest` and `uv run ruff check . && uv run ruff format --check .` green, and the result is reported.
- **Performance**: no change expected; no new dependency.

## UX Requirements
N/A: no user-facing change. Developer ergonomics: the `<feature>_` prefix keeps open tabs and tracebacks unambiguous (two files are never both just `service.py`).

## Constraints
- Python files move with plain `mv`; nothing is staged, committed or pushed.
- Scope of the move: 32 files in `app/` and 49 files in `tests/` and `app/scripts` import from the modules, plus `app/main.py` and `app/db/models.py`; Alembic versions do not import the modules.
- Five resource loaders use `Path(__file__).parent`: `interviews_constants.py` (3), `interviews_evals.py`, `interviews_feedback_evals.py`, `interviews_report_render.py`.
- Tests override dependencies by function object (`get_llm_provider`, `get_bank`, `get_clock`, `get_controller`); the overrides must target the same functions in their new module.

## Blockers
None blocking the spec. Two decisions are left to the plan:
- Where the code shared by the lifecycle and answer services lives (see EC9).
- The file-by-file placement of the 39 interviews test files into layer folders.

## Edge Cases
- **EC1:** A moved file loads the question bank, a prompt, the rubric, the eval cases or the report template -> it finds the file in the module-root `data/`, `prompts/` or `templates/` exactly as before; the bank, prompt, rubric, eval and report tests pass.
- **EC2:** Someone runs the old command `python -m app.modules.interviews.interviews_evals` -> it fails with "No module named" (no shim); the new `...tooling.interviews_evals` path runs with `--help`.
- **EC3:** Alembic autogenerate runs after the move -> it detects no change and produces no operations (assumption — verify a local database is available to run it).
- **EC4:** A test overrides `get_llm_provider`, `get_bank`, `get_clock` or the controller dependency -> the override still applies, because the test imports the same function from its new module.
- **EC5:** A route imports a service, a controller imports a repository, a service imports a controller, or one feature imports another's repository -> the layer test fails and names the file and import.
- **EC6:** `interviews` needs `auth` (permissions, `User`, `require_permissions`) -> it imports auth's `dependencies`, `constants`, `models` and `services`, never auth's `repositories`.
- **EC7:** An answer stream is cut by the client, hits an LLM error or finishes -> the same `done` or `error` event, the same "nothing saved before done" rule and the same request-id error body as today.
- **EC8:** The feedback is already generated and POSTed again -> 200 with the stored body and no new LLM call; the first generation is 201. The service returns the feedback and whether it was just created; the controller or route sets the status.
- **EC9:** The lifecycle service and the answer service both need next-question selection and the summary -> no service imports another service's private members and there is no import cycle between services. Where that shared code lives: expected: unknown (decided in the plan; the condition above is the requirement).
- **EC10:** Only some modules are migrated -> `uv run pytest` is green at every step; the layer test covers the modules already migrated and covers all three at the end.
- **EC11:** A test exercises several layers (for example an endpoint test that reaches the service) -> its file is placed under the layer it mainly targets; the file is kept, not split, and its assertions are unchanged.
- **EC12:** A script such as `app.scripts.create_admin`, `usage_report` or `interview_report` runs -> same output as before; `test_create_admin` and `test_usage_report_script` pass.
- **EC13:** `graphify-out/` is stale after the move -> `graphify update .` is run at the end.
- **EC14:** A folder would hold no file (for example `users/` has no model, dependencies or constants) -> that folder is not created.

## Acceptance Criteria
- [ ] **AC1:** `auth/`, `users/` and `interviews/` have the layer folders listed under Functional; the module root contains only those folders, `__init__.py`, and for interviews `data/`, `prompts/`, `templates/`.
- [ ] **AC2:** Every moved file keeps its `<feature>_` prefix, and the old paths (for example `interviews_controller.py` at the module root) no longer exist.
- [ ] **AC3:** No file in `controllers/` imports a repository, `app.core.ai`, or the database session; no file in `routes/` imports a service or repository; no file in `services/` imports a controller or route, or constructs a response (`*Out`) schema.
- [ ] **AC4:** Interviews has `interviews_service`, `interviews_answer_service`, `interviews_transcription_service` and `interviews_feedback_service`, and a controller of the same name for each; the single `APIRouter` depends on the four controllers; the 728-line `interviews_controller.py` is gone.
- [ ] **AC5:** `feedback_out`, the `_question_out` mapping and the SSE event framing (`_event`, `_error_event`) live in controllers; the upload content-type and size checks stay in the transcription service, with the per-transcription log line, so a rejected upload is still logged (amended in the plan: the check runs inside the same try/finally as that log line).
- [ ] **AC6:** `AuthService` and `UsersService` exist; `create_admin.py` calls the service; ownership and permission checks are enforced in services.
- [ ] **AC7:** The import-direction test exists and passes, and has cases proving it fails on each forbidden import rule (checked with synthetic source, not by editing app code).
- [ ] **AC8:** `uv run pytest` shows no new failure compared with the recorded baseline (one unrelated test, `test_llm_settings_default_to_off_with_documented_limits`, already fails) and the same number of collected tests as before plus only the layer-test cases, and no existing assertion is edited (the diff of `tests/` shows imports, wiring and moves only).
- [ ] **AC9:** `app.openapi()` before and after the whole change is identical (compared as JSON, captured before step 2 and again at the end).
- [ ] **AC10:** `python -m app.modules.interviews.tooling.interviews_evals --help` and `python -m app.scripts.interview_report --help` run; the five resource loaders resolve through one module-root constant.
- [ ] **AC11:** `tests/modules/<feature>/` mirrors the layer folders and every previous test file is present.
- [ ] **AC12:** `CLAUDE.md` and `docs/evaluation-guide.md` are updated as listed; no file under `docs/features/` other than this feature's own is modified; comments and docstrings no longer call the business-logic layer "controller".
- [ ] **AC13:** No file under `alembic/versions/` is added or changed.
- [ ] **AC14:** `uv run --with ruff ruff check .` reports no more than the baseline 77 errors, new files are formatted, and there is no repo-wide reformat (ruff is not a declared dependency); `graphify update .` has run; `git status` shows only unstaged working-tree changes (nothing staged, committed or pushed).

## Out of Scope
- Splitting `interviews_utils.py` and `interviews_constants.py`, or the internal complexity of `ai/` classes such as `Interviewer` (a structure change only; a separate follow-up).
- Any change to endpoints, schemas, database tables, migrations, prompts, LLM behavior or logging output.
- Top-level layer folders, renaming `core/`, `db/` or `app/scripts/`, and moving `data/`, `prompts/` or `templates/`.
- Compatibility shims at the old module paths.
- Rewriting the older `docs/features/*` specs, plans and learnings (they record the code as it was).
- A new dependency such as an import-linter package (the layer test uses the standard library).
