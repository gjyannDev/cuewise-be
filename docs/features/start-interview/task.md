# Implementation: Start an Interview (backend)

## Status
Ready for PR (8 of 8 steps complete). Not committed: the user commits manually.

## Completed Steps
- [x] 1. Constants and permissions
- [x] 2. Question bank (loader, validation, mock `questions.json`)
- [x] 3. Selection logic
- [x] 4. Models and migration
- [x] 5. Schemas and error
- [x] 6. Create session (POST)
- [x] 7. Read session (GET)
- [x] 8. Verify and close

## Changes Made
Suggested commit (user runs it):

    feat(interviews): start an interview session from a mock question bank

    - interviews module (route -> controller -> repository, schema, utils, constants, model, dependencies)
    - POST /api/v1/interviews and GET /api/v1/interviews/{id}
    - interview_sessions / interview_questions tables, one in-progress session per user (partial unique index)
    - interviews:create / interviews:read_self permissions for admin and user
    - validated mock question bank; LLM-driven questions come in story 3

Files:
- New: `app/modules/interviews/` (`interviews_constants`, `_model`, `_schema`, `_utils`, `_repository`, `_controller`, `_dependencies`, `_route`, `data/questions.json`), `alembic/versions/08449683e428_create_interview_sessions_and_questions.py`, `tests/modules/interviews/` (conftest + 3 test files).
- Edited: `app/modules/auth/auth_constants.py`, `app/core/errors.py`, `app/db/models.py`, `app/main.py`, `tests/modules/auth/test_me.py`, `tests/modules/auth/test_permissions.py`.

## Test Results
- Full suite: 232 passed (baseline 106 + 126 new). `uv run pytest`.
- Lint (new/changed files): `uvx ruff check --line-length 120` clean; new files formatted with `uvx ruff format --line-length 120`.
- Manual verification on dev Postgres:
  - `alembic upgrade head` -> `downgrade -1` -> `upgrade head` clean with 2 existing users; partial index created as `... (user_id) WHERE status = 'in_progress'`.
  - Two `in_progress` inserts for one user inside a rolled-back transaction -> `UniqueViolation`; 0 rows left.
  - App import with a corrupted bank file -> refused: "Invalid question bank bad_bank.json: ...".

## Tests Pending
- None.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | admin/user permission sets include interview permissions | spec | AC12 | pass |
| T2 | 1 | `/auth/me` lists interview permissions for both roles | spec | AC12 | pass |
| T3 | 2 | valid bank loads typed entries | spec | AC14 | pass |
| T4 | 2 | duplicate id / blank text / unknown role, level, type / empty roles, levels -> clear error | spec | AC14, EC17 | pass |
| T5 | 2 | unknown field, empty bank -> error | inferred | typo'd key; every request would 409 | pass |
| T6 | 2 | shipped bank covers both types, all roles and levels | spec | AC14 | pass |
| T7 | 3 | single type returns N of that type | spec | AC2, AC3 | pass |
| T8 | 3 | role/general/level eligibility | spec | AC3, EC11 | pass |
| T9 | 3 | no repeats | spec | EC12 | pass |
| T10 | 3 | mixed 1 -> behavioral; 5 -> B,T,B,T,B; 4 -> B,T,B,T | spec/inferred | AC4, EC9 | pass |
| T11 | 3 | shortage -> 409 NOT_ENOUGH_QUESTIONS with requested/available | spec | AC5, EC8 | pass |
| T12 | 3 | mixed short on one type rejected, no rebalancing | spec | EC10 | pass |
| T13 | 3 | same seed -> same selection | spec | AC15 | pass |
| T14 | 3 | shipped bank supports 5 questions for all 60 role x level x type combos | spec | AC14 | pass |
| T15 | 6 | POST 201: saved session, positions 1..N, only first question returned, no bank_id | spec | AC2, AC16 | pass |
| T16 | 6 | stored questions fit setup, distinct | spec | AC3 | pass |
| T17 | 6 | mixed via API split/interleaved | spec | AC4 | pass |
| T18 | 6 | 409 leaves existing session untouched; mixed shortage creates nothing | spec | AC5, EC8, EC10 | pass |
| T19 | 6 | 14 invalid bodies -> 422, nothing created | spec | AC6, EC3-EC6 | pass |
| T20 | 6 | job_description: 2000 ok, trimmed, blank/empty/omitted -> null | spec | EC6, EC7 | pass |
| T21 | 6 | second start abandons first | spec | AC7, EC13 | pass |
| T22 | 6 | two users each keep their own in_progress session | inferred | user asked: per-user, not global | pass |
| T23 | 6 | failure while saving questions rolls back everything | spec | AC8, EC15 | pass |
| T24 | 6 | DB rejects two in_progress rows for one user | spec | AC9, EC14 | pass |
| T25 | 6 | lost race -> 409 CONFLICT, nothing created | spec | AC9, EC14 | pass |
| T26 | 6 | bank edits never change a saved session | spec | AC13, EC16 | pass |
| T27 | 6 | POST 401 without token, 403 without permission | spec | AC12, EC1, EC2 | pass |
| T28 | 6 | job_description never in logs | spec | AC17 | pass |
| T29 | 7 | owner GET returns same body as POST | spec | AC10 | pass |
| T30 | 7 | abandoned session still readable | spec | AC10, EC13 | pass |
| T31 | 7 | missing and foreign session -> identical 404 | spec | AC11, EC18, EC19 | pass |
| T32 | 7 | admin can't read another user's session | spec | EC21 | pass |
| T33 | 7 | malformed id -> 422 | spec | EC20 | pass |
| T34 | 7 | GET 401 / 403 | spec | AC12 | pass |
| T35 | 7 | OpenAPI documents 401/403/404/409/422/500 with ErrorResponse | spec | AC16 | pass |

## Open Questions
- None.

## Baseline Failures
- `ruff` is not a project dependency (`uv run ruff` fails). Via `uvx ruff`, pre-existing findings remain untouched: 17 lint findings (UP007/I001/UP035 in the autogenerated Alembic files and `alembic/env.py`, RUF012 in `core/errors.py`) and format diffs at ruff's default 88-char width (existing code uses ~120, e.g. `auth_constants.py`'s `except ValueError, KeyError:`). The new migration follows the same autogenerated style as the existing ones.

## Known Issues
- Real parallel HTTP requests were not fired; the guarantee is the partial unique index, verified on Postgres directly (see Test Results).
- `graphify-out/` is new and untracked: decide whether to commit it or add it to `.gitignore`.

## Deviations from Plan
- `NotEnoughQuestionsError` added in step 3 (not 5) because selection raises it -> plan.md step 3/5 updated.
- Response shape is nested `{session: {...}, current_question: {...}}` -> plan.md step 5 updated; spec content unchanged (same fields). The client should read `data.session.id`.
- Test helpers exposed as fixtures (`make_bank_question`, `bank`, `start_interview`) since test folders have no `__init__.py`.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| all | lean-ctx | exploration, test runs, migrations |
| all | graphify | built the graph, queried auth/permissions/repository relations, refreshed at the end |
| all | find-skills | searched SQLAlchemy/Alembic skills: all under 25 installs, none installed |
| all | ponytail | no provider interface, no ORM relationships, no new deps, `ponytail:` note on position-1 |
| all | fastapi | `Annotated` deps, return types, sync `def` with sync Session, router-level prefix/tags/responses |
| 1-3, 5-7 | tdd / test | red -> green at the confirmed seams; spec/inferred tagging |

## Links
- Spec: docs/features/start-interview/spec.md
- Plan: docs/features/start-interview/plan.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite + build green (not just per-step tests)
- [x] Every spec.md acceptance criterion met by actual code and covered by a passing spec test (or verification noted)
- [x] Open Questions resolved or explicitly surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [ ] Commits documented (user commits manually; message suggested above)
- [x] No open blockers
- [x] Code follows project rules (CLAUDE.md)
- [x] No unresolved plan deviations
