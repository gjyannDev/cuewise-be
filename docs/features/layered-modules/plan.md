# Implementation Plan: Layered Modules (route -> controller -> service -> repository)

## Overview
Move `auth`, `users` and `interviews` into one folder per layer and split today's "controller" (really a service) into a thin controller plus a service, with no change in behavior, API, database or prompts.

## Architecture & Design
Request flow is route -> controller -> service -> repository. Layer folders live inside each feature module; the `<feature>_` filename prefix stays. Delivery is module by module (rules, then `auth` and `users` as a rehearsal, then `interviews`, then the test folders), and every step ends green against the recorded baseline.

Design decisions this plan makes (the spec left them open):
- **Services return fully loaded values.** A service returns ORM rows it has already loaded or refreshed, or plain NamedTuples, so a controller's mapping never touches the database. This follows the code's existing pattern (`InterviewSetup`, `TurnContext`: "plain values that survive the end of a transaction"). It matters because the stream and transcribe controllers run on the event loop, while today the response is built inside the worker thread (`finish_answer` runs through `to_thread`).
- **The answer stream is split by who knows what.** The answer service yields domain events (status, reaction, delta, reset, done with the turn result, failed with code and message), and keeps the trace, the error handling and `log_stream_summary`, so logs stay identical. The controller only maps each domain event to an SSE frame (`StreamEventOut`), including the error frame with the request id.
- **Shared code (EC9, user-confirmed):** one new file `utils/interviews_session_utils.py` holds `InterviewSetup`, `Thread`, the bank-question and LLM-question builders, the interviewer-inputs builder and a single `owned_session` check. It replaces the copy in the feedback controller. No service imports another.
- **Upload checks stay in the transcription service** (user-confirmed), together with the per-transcription log line, so a rejected upload is still logged. The route reads the bytes and the controller passes bytes and content type through.
- **Resource folders:** `data/`, `prompts/`, `templates/` stay at the module root; one `MODULE_DIR` constant in `constants/interviews_constants.py` (the module root, two levels up from that file) replaces the five `Path(__file__).parent` expressions.
- **Dependencies:** each controller and service gets its own `get_*` provider in `dependencies/`; the route depends on the four `*ControllerDep`. Providers tests override today (`get_llm_provider`, `get_bank`, `get_clock`, `get_context_manager`, `get_tracer`) keep their names.
- **Layer check:** a stdlib `ast` test with a pure `check_layers` function (see step 3).

## Spec Requirements -> Implementation
- Layer responsibilities and layout (Functional) -> steps 4, 5, 7, 8
- Interviews mapping and the four services -> steps 5, 6, 7, 8
- Auth and users services/controllers, `create_admin` -> step 4
- Layer check -> step 3 (extended to each module as it is migrated: steps 4 and 8)
- Moves that must keep working (resources, CLIs, model discovery) -> steps 4, 5, 10
- Documentation -> steps 2 and 10
- Tests mirror the layers; only imports and wiring change -> steps 4, 5, 7, 8, 9
- Non-functional (identical behavior, security, delivery) -> step 1 baseline, a gate at every step, step 10

## Implementation Steps
Every step ends with the gate: `uv run pytest` shows no failure beyond the one known baseline failure, and `uv run --with ruff ruff check .` reports no more than the baseline 77 errors. Files move with plain `mv`; nothing is staged or committed.

1. **Baseline** (record only): save to the scratchpad the pytest result and collect-only count, the ruff error count, `app.openapi()` as sorted JSON, a table/column snapshot of `Base.metadata`, and `git status` of `alembic/versions`. — Test: skip
2. **Rules first:** update `CLAUDE.md` (architecture tree, file naming, layer rules, cross-feature entry is the service, ownership checks in services, workflow wording) and the "controllers raise these" docstrings in `core/errors.py`. — Test: skip
3. **Layer checker, test first** (`tests/test_layers.py`). Seam: `check_layers(files)` taking a path-to-source mapping and returning violation messages (user-confirmed), plus one test that runs it on the real `app/` tree for the modules migrated so far. Thin slices, one behavior each, in this order: (a) clean sources give no violations; (b) a route importing a service or repository; (c) a controller importing a repository; (d) a service importing a controller or route; (e) a service importing an `*Out` schema (makes AC3 mechanical); (f) a repository importing a service, controller or route; (g) a feature importing another feature's repository; (h) a layer file left at a module root; (i) the real-tree test, starting with an empty module list. — Test: first
4. **auth and users (rehearsal):**
   - Create the folders (only those with a file), move files, rename `AuthController` to `AuthService` and `UsersController` to `UsersService`, and add thin `AuthController` and `UsersController`: `MeOut` and `UserListOut` are built in the controllers, the services return rows, a total and the `User`.
   - Update `dependencies/`, routes, `app/main.py`, `app/db/models.py` (model discovery), and `app/scripts/create_admin.py` (calls the service).
   - Update tests' imports and wiring (`test_register_errors` builds a service, then a controller).
   - Add `auth` and `users` to the layer check's module list. — Test: after
5. **interviews: pure moves.** No logic change. Move routes, repository, schemas, model, dependencies, utils and constants to their folders; `interviews_turn`, `interviews_feedback_turn`, `interviews_context`, `interviews_reply`, `interviews_feedback` to `ai/`; evals, feedback evals, report, report render and log to `tooling/`. Rename the two old controllers to `services/interviews_service.py` (class `InterviewsService`, still whole) and `services/interviews_feedback_service.py`. Introduce `MODULE_DIR` and switch the five loaders to it. Update `app/main.py`, `app/db/models.py`, `app/scripts/*`, the "Run:" docstring lines in tooling, and the tests' imports. — Test: skip
6. **Shared helpers:** create `utils/interviews_session_utils.py` and make the services use it (incl. the feedback service's owned-session check). — Test: after
7. **Split the fat service** into `interviews_service` (start, get, list, transcript, job-description summary), `interviews_answer_service` (prepare, answer, finish, domain-event stream, `TurnContext`), `interviews_transcription_service` (prepare, transcribe, audio checks, log line); the feedback service is unchanged beyond the rename. Services return domain values and import no `*Out` schema. Rewire `dependencies/` for the three services. — Test: after
8. **Thin controllers and routes:** four controllers, one per service. They build `InterviewOut`, `InterviewListOut` (incl. the list-item mapping), `TranscriptOut` (via the existing `build_transcript`), `AnswerOut`, `TranscriptionOut`, the SSE frames (`_event`, `_error_event`) and `feedback_out`, and carry the 201 vs 200 flag. The single `APIRouter` depends on the four `*ControllerDep`; the route keeps `run_in_threadpool`, `UploadFile.read` and `EventSourceResponse`. Add `interviews` to the layer check's module list. — Test: after
9. **Mirror the tests:** move each interviews test under `routes/`, `ai/`, `tooling/`, `utils/` or `services/` by what it calls (user-confirmed rule: HTTP client means routes; an `ai/` unit means ai; and so on), keep `conftest.py` at the module test root, keep the files whole. Same for `auth` and `users`. — Test: skip
10. **Docs and final verification:** update `docs/evaluation-guide.md` (evals command), confirm no living doc names an old path, then check every AC (list in Testing Strategy), run `graphify update .`, and report. — Test: skip

## Affected Files & Patterns
- `app/modules/{auth,users,interviews}/*`: moved, split or renamed as above. `app/main.py`, `app/db/models.py`, `app/scripts/create_admin.py`, `app/scripts/interview_report.py`, `app/scripts/usage_report.py`: import paths. `alembic/versions` and `alembic/env.py`: untouched (env imports `app.db.models` only).
- `tests/modules/**`: imports, wiring and folder moves. New: `tests/test_layers.py`. Docs: `CLAUDE.md`, `docs/evaluation-guide.md`, this feature's folder. `docs/features/*` others untouched.
- Patterns to follow: plain-value NamedTuples across transactions (`InterviewSetup`, `TurnContext`); one `APIRouter` per feature; `Depends` providers with `Annotated` aliases; tests override providers by function object; structured errors from `core/errors.py` raised in services.
- Risks:
  - **R1 blocking I/O in controllers:** a controller mapping an ORM row that is not loaded would query the database on the event loop. Mitigation: services return loaded values (design decision above); review each mapping in the stream and transcribe controllers.
  - **R2 resource paths:** missed loaders. Mitigation: one `MODULE_DIR`; the bank, prompt, rubric, eval and report tests cover all five.
  - **R3 import cycles** from the new folders. Mitigation: empty `__init__.py`, no re-exports, shared helpers in `utils/`.
  - **R4 test collection:** `pythonpath` is `["."]`, tests have no `__init__.py`, and no basename is duplicated today, so folders need no package files; keep basenames unique.
  - **R5 `build_transcript` lives in `utils/` and builds `TranscriptItemOut`:** it stays as-is and the controller calls it, so services still build no `*Out`.
  - **R6 churn on `dependencies/` and routes** across steps 5 to 8. Accepted: each step keeps the suite green and is easy to bisect.
  - **R7 stale graph** until `graphify update .` (step 10).

## Testing Strategy
- Framework and commands: `pytest`. While working `uv run pytest tests/modules/<feature>`; at each gate `uv run pytest`. Collect count: `uv run pytest --collect-only -q`. Lint: `uv run --with ruff ruff check .` (ruff is not a declared dependency, so `uv run ruff` fails; `--with` adds nothing to the project).
- Baseline (recorded before any change): 1205 passed, 1 skipped, 1 failed, 1207 collected. Ruff: 77 errors, and 109 files would be reformatted (no `[tool.ruff]` config).
- Coverage map:

| Spec ID | Step | Test mode | Notes |
|---|---|---|---|
| AC1 | 3, 4, 8 | first | checker rule (h) plus tree listing at step 10 |
| AC2 | 4, 5, 10 | first | root rule (h); old paths gone checked by listing |
| AC3 | 3 | first | checker rules (b) to (e) |
| AC4 | 7, 8 | after | existing endpoint tests; listing of services and controllers |
| AC5 | 8 | after | stream and transcribe tests; SSE helpers, `feedback_out` and `_question_out` in controllers (checked by search). Amended: audio checks stay in the transcription service |
| AC6 | 4 | after | auth tests, `test_create_admin`; ownership/permission tests |
| AC7 | 3 | first | synthetic sources per rule |
| AC8 | 1, every gate | after | no new failure and the same collected count (plus layer-test cases) versus baseline; see deviations |
| AC9 | 1, 10 | after | OpenAPI JSON diff against the step 1 snapshot |
| AC10 | 5, 10 | after | the two `--help` runs; bank, prompt, rubric, eval, report tests |
| AC11 | 9, 10 | skip | listing; test count equal to baseline |
| AC12 | 2, 10 | skip | search of docs and docstrings |
| AC13 | 10 | skip | `git status` of `alembic/versions` |
| AC14 | every gate, 10 | skip | ruff versus baseline; `git status`; `graphify update .`; see deviations |
| EC1 | 5, 10 | after | `MODULE_DIR`; resource tests |
| EC2 | 5, 10 | after | old module command fails, new one runs |
| EC3 | 1, 10 | after | `Base.metadata` snapshot diff; `alembic check` only if a local database exists (assumption — verify) |
| EC4 | 4, 7, 8 | after | existing override tests |
| EC5 | 3 | first | rules (b) to (g) |
| EC6 | 3, 8 | first | rule (g); interviews imports auth's dependencies, constants, models and services |
| EC7 | 7, 8 | after | `test_answer_stream`, `test_stream_answer`, `test_stream_turn` |
| EC8 | 8 | after | `test_feedback_endpoint` (201, then 200 with no LLM call) |
| EC9 | 6, 7 | first/after | helper file; checker plus a search for cross-service imports |
| EC10 | 3, 4, 8 | first | module list in the real-tree test grows |
| EC11 | 9 | skip | rule-based placement, files kept whole |
| EC12 | 4, 10 | after | `test_create_admin`, `test_usage_report_script` |
| EC13 | 10 | skip | `graphify update .` |
| EC14 | 4, 5 | skip | only folders with files are created |

- Must verify, not assume: EC3 `alembic check` (needs a database); the event-loop safety of the stream mapping (R1; the tests do not detect blocking I/O, so it is a review item at step 8).
- Open questions: none. EC9 and the test placement were decided with the user.
- Known baseline failures: `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits` (the `llm_max_tokens` default is 4000, the test expects 800); unrelated and left as is.

## Blockers & Resolutions
- Shared code placement (EC9) -> `utils/interviews_session_utils.py` (user-confirmed).
- AC5 vs the transcription log line -> audio checks stay in the transcription service; spec AC5 amended (user-confirmed).
- Test placement -> by what the test calls (user-confirmed); each file is classified by reading it in step 9.
- Layer-check seam -> `check_layers` over a path-to-source mapping (user-confirmed).
- Intermediate states (route calling a not-yet-split service) -> `interviews` joins the layer check only at step 8.

## Deviations from the spec (approved by the user; spec.md updated to match)
- **AC8** says `uv run pytest` passes. It cannot literally, because one unrelated test already fails. Proposed reading: no new failure and the same collected count.
- **AC14** says `ruff check` and `ruff format --check` pass. Today ruff reports 77 errors and wants 109 files reformatted, and ruff is not a declared dependency. Proposed reading: no more than 77 errors, new files formatted, no repo-wide reformat.
- **Layer check** also forbids a service importing an `*Out` schema. This only makes AC3 mechanical.

## Trade-offs & Rationale
- Controller layer that earns its keep -> it owns response building, SSE framing and the 200/201 flag; `auth` and `users` controllers stay near pass-through because the rule is "never skip a layer".
- Services return loaded values, not response models -> keeps controllers free of database access, at the cost of a few new NamedTuples (the turn result, the domain stream events).
- Service owns stream errors and telemetry -> logs stay identical; the controller only converts to frames.
- A shared helper file rather than a fifth service or a base class -> no service depends on another; one small file removes the duplicated owned-session check.
- Module-by-module with the layer check growing -> the small modules prove the pattern before the large one; the checker never fails on half-migrated code.
- No shims and no `git mv` -> the old paths stop existing; nothing is staged.

## Project Rules Applied
- `CLAUDE.md` "Git Rules": no commit, push, stage, amend or reset; plain `mv`.
- `CLAUDE.md` "Tooling" and "Workflow": lean-ctx and graphify first, `graphify update .` last, tests and lint after each step with real results.
- `CLAUDE.md` "Don'ts": no edit to applied migrations, no new dependency (the layer test uses `ast`; ruff runs through `--with`, not added).
- `CLAUDE.md` "AI Engineering": provider abstraction, prompts as data files and mocked-LLM tests are untouched.
- Rules changed by this feature (step 2): architecture tree, file naming, layer direction, cross-feature entry point, where ownership is enforced.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | signatures and line reads of the controllers, route, dependencies, repository, reply, feedback and context modules; import and path counts |
| graphify | spec-time query on module layering (reused, not repeated) |
| grill-me (via AskUserQuestion) | EC9 helper placement, upload-check conflict, test placement rule, layer-check seam |
| ponytail | not invoked: no new dependency or abstraction; shared code is one file rather than a fifth service |
| tdd | not invoked: the layer-check seam was named and confirmed through the questions |

## Ready to Implement
- All spec requirements mapped to steps
- Every step has a Test tag; every AC# and EC# mapped in Testing Strategy
- Affected files identified
- Blockers resolved, edge cases handled
- Trade-offs documented with rationale
- Deviations from spec: AC5, AC8, AC14 and the extra layer rule are approved and written into spec.md
