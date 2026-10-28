# Implementation Plan: Start an Interview (backend)

## Overview
Add an `interviews` module so a logged-in candidate can create a saved interview session (role, level, type, question count, optional job description) from a mock question bank, get the first question back, and re-fetch the session later.

## Architecture & Design
New feature module `app/modules/interviews/` following the `auth/` layout (route -> controller -> repository, plus schema, utils, constants, dependencies, model). Question content lives in a validated JSON bank loaded once at import (fail fast, same style as `settings = Settings()`); a pure `select_questions` function picks questions with an injected random source, so it is the single seam story 3 can swap or wrap. Creating a session is one transaction: abandon the caller's current `in_progress` session, insert the new session, insert its snapshotted questions, commit once. A partial unique index on `user_id` where `status = 'in_progress'` is the real guarantee behind "one active session per user"; the existing global `IntegrityError` handler turns a lost race into the 409 `CONFLICT` the spec wants.

## Module Structure & Layer Rules
Request flow is strictly **route -> controller -> repository**; layers only call downward, never skip or import upward. Every file is prefixed `interviews_`.

| File | Owns | Must not contain |
|------|------|------------------|
| `interviews_route.py` | path, verb, `status_code`, `response_model`, `responses=`, permission dependency; one `APIRouter` with `prefix="/interviews"` and `tags` | business logic, DB calls, raw `HTTPException` |
| `interviews_controller.py` | orchestration: choose questions, enforce ownership, raise `AppError` subclasses, build response schemas | HTTP objects (`Request`, status codes), SQL |
| `interviews_repository.py` | all SQLAlchemy access, transaction boundary (commit/rollback) | business rules (eligibility, limits, ownership decisions) |
| `interviews_schema.py` | every Pydantic model: create input, question/session output, bank entry; `extra="forbid"` on input, ORM never returned directly | logic beyond field validation |
| `interviews_utils.py` | feature-local helpers: `load_bank`, `select_questions` (no DB, no HTTP, random source injected) | session/request state |
| `interviews_constants.py` | enums (`StrEnum`) and limits (max description length, count bounds, bank path); no magic strings elsewhere | behavior |
| `interviews_model.py` | SQLAlchemy models only | queries |
| `interviews_dependencies.py` | `Depends` wiring: repository -> controller, bank provider | logic |

Best practices applied: type hints everywhere; dependency injection via `Depends` (DB session, controller, bank), no globals except the once-loaded bank behind a dependency so tests can override it; sync `def` handlers to match the existing sync `Session` (no blocking I/O in `async def`); one responsibility per function; no bare `except`; specific structured errors from `core/errors.py` with generic client messages; reuse existing code (`UUIDPrimaryKeyMixin`, `require_permissions`, `ErrorResponse`, the global `IntegrityError` handler) before writing new; `ruff` clean.

## Spec Requirements -> Implementation
- New permissions `interviews:create` / `interviews:read_self` (admin + user) -> Step 1
- Bank file, Pydantic validation, fail-fast load, mock content -> Step 2
- Eligibility, no repeats, mixed split/interleave, not-enough-questions -> Step 3
- `interview_sessions` / `interview_questions` tables, UUID keys, partial unique index, migration -> Step 4
- Request/response schemas, `job_description` trimming/limit, `NOT_ENOUGH_QUESTIONS` error -> Step 5
- `POST /api/v1/interviews` (abandon previous, snapshot, atomic, 409 on race), router registered -> Step 6
- `GET /api/v1/interviews/{session_id}` with ownership -> 404 -> Step 7
- OpenAPI error docs, logging hygiene, ruff/pytest, graph update -> Step 8

## Implementation Steps
1. **Constants and permissions.** Create `interviews_constants.py` (enums for job role, level, interview type, question category, session status; `job_description` max length, question-count bounds). Add the two `Permission` values and map them for both roles in `auth_constants.py`. Update existing tests that assert permission sets (`test_me.py`, `test_permissions.py`). — Test: first (seam: `permissions_for(role)` and `GET /auth/me`)
2. **Question bank.** `interviews_schema.py` gets the bank-entry model (strict: unique ids, non-empty text, enums, non-empty roles/levels, `general` tag allowed only in the bank). `interviews_utils.py` gets `load_bank(path)` (read + validate, raise a clear error) and a module-level load of the shipped `data/questions.json`. Write the mock bank: at least 5 `general` behavioral and 5 `general` technical entries tagged with all four levels, plus a few role-specific ones so every role/level/type appears. — Test: first (seam: `load_bank(path)`)
3. **Selection logic.** `select_questions(bank, role, level, interview_type, count, rng)` in `interviews_utils.py`: eligibility filter, random sample without repeats, even `mixed` split with extra behavioral on odd counts and interleaving starting with behavioral, raises `NotEnoughQuestionsError` carrying the available count (per-type for `mixed`, no rebalancing). The error class is added to `core/errors.py` in this step because selection raises it. — Test: first (seam: `select_questions`, thin slices: single type, eligibility, no repeats, mixed 1/5, shortage)
4. **Models and migration.** `interviews_model.py` with `InterviewSession` and `InterviewQuestion` (both on `UUIDPrimaryKeyMixin`; UUID FKs; status stored as a plain string like `User.role`; unique `(session_id, position)`; partial unique index on `user_id` where status is `in_progress`, declared for both PostgreSQL and SQLite so tests exercise it). Register in `app/db/models.py`. Autogenerate one Alembic migration and review it by hand (partial index kwargs, downgrade drops both tables). — Test: after (migration needs real Postgres; constraint behavior is covered by step 6 tests)
5. **Schemas and error.** `interviews_schema.py`: `InterviewCreateIn` (`extra="forbid"`, enum fields, count 1-10, `job_description` stripped, blank -> None, max 2000), `QuestionOut` (no `bank_id`), `SessionOut`, and `InterviewOut` = `{session, current_question}` (nested, so the session fields map 1:1 from the model). `NotEnoughQuestionsError` already exists from step 3. — Test: first (observed through the POST seam in step 6)
6. **Create session.** Repository: bulk-UPDATE the caller's `in_progress` sessions to `abandoned` *before* inserting the new session (so the unique index never sees two), add session + questions, one commit, explicit rollback on any exception. Controller: select questions (bank injected), call repo, build response with position 1 only. `interviews_dependencies.py`: controller dependency and an overridable bank dependency. Route: `POST /interviews` guarded by `require_permissions(interviews_create)`, 201, `responses=` for 401/403/409/422. Register router in `main.py`. — Test: first (seam: `POST /api/v1/interviews`)
7. **Read session.** Repository query by `(session_id, user_id)` so "missing" and "someone else's" are the same code path; controller raises `NotFoundError`; route `GET /interviews/{session_id}` guarded by `interviews_read_self`, returns the position-1 question, works for `abandoned`. — Test: first (seam: `GET /api/v1/interviews/{id}`)
8. **Verify and close.** `alembic upgrade head`, `downgrade -1`, `upgrade head` against the dev Postgres (with an existing user row present); `uv run ruff check . && uv run ruff format .`; `uv run pytest`; `graphify update .`. — Test: skip

## Affected Files & Patterns
- New: `app/modules/interviews/` (`__init__`, `interviews_constants`, `interviews_model`, `interviews_schema`, `interviews_utils`, `interviews_repository`, `interviews_controller`, `interviews_dependencies`, `interviews_route`, `data/questions.json`); one file in `alembic/versions/`; `tests/modules/interviews/`.
- Edited: `app/modules/auth/auth_constants.py` (permissions), `app/core/errors.py` (new error), `app/db/models.py` (register models), `app/main.py` (router), `tests/modules/auth/test_me.py` and `test_permissions.py` (permission sets).
- Patterns to follow: `auth_dependencies.py` (controller `Annotated` dep, `require_permissions`), `auth_route.py` (`responses=` with `ErrorResponse`), `auth_repository.py` (commit/refresh in repo), existing global `IntegrityError` -> 409 handler, `conftest.py` fixtures (`client`, `db`, `make_user`, `auth_header`, `app_logs`).
- Risks: the migration must create the partial index with the right dialect kwargs (autogenerate may omit them); UPDATE-before-INSERT ordering matters or the unique index fires on the happy path; `package-data`: the JSON file is read by path relative to the module, so it works from the repo but would need packaging if the app is ever built as a wheel.

## Testing Strategy
- Framework & command: pytest on in-memory SQLite via existing fixtures; `uv run pytest tests/modules/interviews`, then the full `uv run pytest`; lint with `uv run ruff check .`. Tests use their own small fixture banks via the bank dependency override, never the mock file (except the shipped-file test).
- Test seams (user-confirmed): `select_questions`, `load_bank`, `POST`/`GET /api/v1/interviews`, `permissions_for` + `/auth/me`.
- Concurrency (user-confirmed approach): deterministic. Insert two `in_progress` rows for one user directly -> `IntegrityError`; two different users each hold one; API test with the abandon step bypassed -> 409 `CONFLICT`.

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 4, 8 | after | migration up/down on dev Postgres with existing users |
| AC2 | 6 | first | 201, rows persisted, only position 1 returned |
| AC3, EC11, EC12 | 3 | first | eligibility, `general` tag, no repeats |
| AC4, EC9, EC10 | 3, 6 | first | split, interleave, no rebalancing |
| AC5, EC8 | 3, 6 | first | 409 with available count; nothing created; old session untouched |
| AC6, EC3-EC7 | 5, 6 | first | validation via POST; 2000 ok / 2001 rejected; blank -> null |
| AC7, EC13 | 6 | first | previous becomes `abandoned`, still readable |
| AC8, EC15 | 6 | first | force a failure while saving questions; assert no new row, old unchanged |
| AC9, EC14 | 4, 6 | first | deterministic constraint tests |
| AC10 | 7 | first | owner read, abandoned read, no questions beyond position 1 |
| AC11, EC18-EC21 | 7 | first | identical 404 bodies; bad UUID -> 422; admin gets no special access |
| AC12, EC1, EC2 | 1, 6, 7 | first | 401/403, permission map, `/auth/me` list |
| AC13, EC16 | 6 | first | mutate the bank after creation, stored text unchanged |
| AC14, EC17 | 2 | first | invalid bank variants raise; shipped file covers types/roles/levels and supports 5 questions for all three types |
| AC15 | 3 | first | seeded `random.Random` and fixture banks |
| AC16 | 5, 8 | first | OpenAPI documents 401/403/404/409/422; no `bank_id` in responses |
| AC17 | 6, 8 | first | `app_logs` assertions: `job_description` text never appears |
| AC18 | 1, 8 | after | full pytest + ruff green |

- Must verify, not assume: migration on real Postgres (partial index created, upgrade with existing users, downgrade clean); real concurrent POSTs on Postgres (SQLite cannot race); that the app refuses to start with a bad shipped bank (checked once manually by corrupting a copy).
- Open questions: none; every EC has a stated outcome.
- Known baseline failures: none seen (tests not run during planning).

## Known Follow-ups (story 3: Chat with the interviewer)
Deliberate simplifications here that the LLM story will revisit; none need work now.
- `current_question` is always position 1 -> add a `current_position` column (new migration) and return the right question from `GET`.
- `status` has only `in_progress` / `abandoned` -> add `completed` (plain string column, no DB enum change).
- New `messages` table (answers, interviewer replies, follow-ups) referencing `interview_questions`; the question snapshot keeps transcripts stable.
- `select_questions` is a plain function -> wrap or replace it if the LLM picks or rewrites questions; extract a provider interface only when a second source exists. The mock bank stays as fallback and eval baseline.
- Sync `Session` vs SSE streaming -> decide async handlers vs a streaming response around a sync client; affects the new chat route only.
- No ORM relationships between session and questions -> add them if loading a full transcript needs it.
- Rate limiting on the interview endpoints -> add once requests cost money.
- Prompts as versioned files, model adapter, token/latency logging, and `job_description` as untrusted prompt input follow the CLAUDE.md AI guidelines.

## Blockers & Resolutions
- No blockers in the spec. Mock bank content -> written in Step 2, tests use fixture banks.
- Lost race between two concurrent POSTs -> partial unique index plus the existing `IntegrityError` handler (409 `CONFLICT`); no new handler needed.
- Abandon + insert in one transaction without tripping the index -> bulk UPDATE first, then insert, single commit, explicit rollback on failure.
- Unmapped/foreign session ids -> one query keyed on `(id, user_id)` gives identical 404s.

## Trade-offs & Rationale
- Eager bank load at import -> satisfies "fails to start" with the same pattern as `settings`; a lifespan hook would add machinery for no benefit.
- No ORM relationships between session and questions -> the endpoints only need "session" and "question at position 1"; queries stay explicit and cheap. Revisit in story 3 when the whole transcript is needed.
- `status` and role/level/type as plain strings validated by Pydantic enums, not DB enums -> adding `completed` or a new role needs no `ALTER TYPE` migration (same call as `User.role`).
- Selection as a pure function, no provider interface yet -> YAGNI (ponytail): extract an interface when the LLM source actually exists in story 3.
- `NotEnoughQuestionsError` in `core/errors.py` -> all structured errors already live there.
- Deterministic concurrency tests instead of a Postgres test rig -> no new test infrastructure; the DB constraint is what carries the guarantee, and it is verified manually on Postgres.

## Project Rules Applied
- `CLAUDE.md` layering (route -> controller -> repository), `interviews_` file prefixes, mandatory `_schema.py` (Pydantic) and `_utils.py`, plus `_constants.py` / `_model.py` / `_dependencies.py`; thin routes, no business logic or SQL outside controller/repository (see Module Structure & Layer Rules).
- UUIDv7 primary keys via `UUIDPrimaryKeyMixin`; UUIDs as strings in schemas.
- Pydantic `extra="forbid"`, `response_model` + `status_code` + `responses=` on every route; ownership enforced in the controller; permissions via `require_permissions`.
- Alembic only for schema changes, new migration, reviewed by hand; no new dependencies.
- Privacy: `job_description` never logged; no LLM, no prompts in this story.
- Do not commit or push; run `graphify update .` after code changes.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | read config/db/auth module, conftest, exception handlers, existing tests to match patterns |
| graphify | not available (no `graphify-out/` in the repo); skipped |
| grill-me | confirmed test seams and the deterministic concurrency-test approach |
| ponytail | kept the design lean: pure selection function, no provider interface, no relationships, no new dependency |
| tdd | seams named per `Test: first` step; thin-slice order listed in step 3 |
| security-review | auth/ownership surface covered: default-deny, identical 404s, extra=forbid, no content logging |

## Ready to Implement
- All spec requirements mapped to steps
- Every step has a Test tag; every AC#/EC# mapped in Testing Strategy
- Affected files identified
- Blockers resolved, edge cases handled
- Trade-offs documented with rationale
- No deviations from spec
