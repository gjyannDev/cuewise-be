# Implementation: Interview History List (backend)

## Status
Ready for review / PR (8 of 8 steps done). Not committed: the user commits manually.

## Completed Steps
- [x] 1. Shared pagination module (`app/core/pagination.py`)
- [x] 2. Refactor `GET /users` onto it
- [x] 3. Interviews schemas
- [x] 4. Index and migration
- [x] 5. Repository
- [x] 6. `answered_count` rule
- [x] 7. Controller and route
- [x] 8. Verify and close

## Changes Made
- `app/core/pagination.py` (new): `DEFAULT_PAGE_SIZE`/`MAX_PAGE_SIZE`, `PageParams`, `page_params` dependency, `PageDep`, generic `Page[T]`.
- `app/modules/users/`: route takes `PageDep`; controller takes `PageParams`; `UserListOut` subclasses `Page[UserAdminOut]`; `users_constants.py` deleted (its two constants moved to core). OpenAPI for `GET /users` compared before/after: identical.
- `app/modules/interviews/interviews_schema.py`: `InterviewListItemOut`, `InterviewListOut`.
- `app/modules/interviews/interviews_model.py`: index `ix_interview_sessions_user_id_id` (user_id, id).
- `alembic/versions/a72345efd4c2_add_interview_sessions_user_index.py` (new, revises `e3b8f41a6c27`).
- `app/modules/interviews/interviews_repository.py`: `_history_filter`, `list_for_user` (rows + current main number via correlated subquery), `count_for_user`.
- `app/modules/interviews/interviews_utils.py`: `answered_main_questions`.
- `app/modules/interviews/interviews_controller.py`: `list_interviews`.
- `app/modules/interviews/interviews_route.py`: `GET /interviews` (`limit`, `offset`, `status`).
- `tests/modules/interviews/test_list_interviews.py` (new, 23 tests).
- Suggested commit message (user runs it):

  feat(interviews): list a candidate's interview history with shared pagination

  GET /api/v1/interviews returns the caller's interviews newest first, every status, with answered_count
  (main questions finished). Pagination (PageParams, Page[T]) moves to app/core and GET /users uses it unchanged.
  Adds an index on interview_sessions (user_id, id) for the newest-first list.

## Test Results
- `tests/modules/interviews/test_list_interviews.py`: 23 passed.
- `tests/modules/users`: 11 passed (unchanged).
- Full suite: 1008 passed, 1 skipped, 1 failed (baseline, see below).
- Alembic on local PostgreSQL: upgrade -> downgrade -> upgrade OK; `alembic check`: no drift.
- PostgreSQL EXPLAIN of the newest-first query: Index Only Scan Backward using `ix_interview_sessions_user_id_id`.

## Tests Pending
- None.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 7 | empty history -> empty page with defaults | spec | AC1, AC9, EC1 | pass |
| T2 | 3, 7 | item has exactly the table fields; no job description, no user_id | spec | AC2, EC13 | pass |
| T3 | 5 | only the caller's interviews listed and counted | spec | AC3, EC2 | pass |
| T4 | 5 | newest first, in-progress on top | spec | AC4, EC14 | pass |
| T5 | 5 | limit/offset window and total | spec | AC5 | pass |
| T6 | 1 | limit 0/101/abc, offset -1 -> 422 | spec | AC5, EC3 | pass |
| T7 | 5 | offset past the end -> empty items, real total | spec | AC5, EC4 | pass |
| T8 | 5 | status filter narrows items and total (x3) | spec | AC6, EC6 | pass |
| T9 | 7 | unknown status -> 422 | spec | AC6, EC5 | pass |
| T10 | 5 | all three statuses without a filter, abandoned with 0 answers | spec | AC7, EC9 | pass |
| T11 | 6 | answered_count after plain turns (in progress 1, completed 2) | spec | AC8, EC8 | pass |
| T12 | 6 | follow-ups don't count: pending follow-up of main 2 -> 1, completed -> 2 | spec | AC8, EC7, EC8 | pass |
| T13 | 6 | session with every question stored up front, abandoned at position 3 -> 2 | spec | AC8, EC10 | pass |
| T14 | 7 | no token -> 401 | spec | AC10, EC11 | pass |
| T15 | 7 | no permission -> 403 | spec | AC10, EC11 | pass |
| T16 | 7 | in-progress row resumes with GET /{id} and /messages | spec | AC11 | pass |
| T17 | 5 | 2 history queries for limit 1 and limit 5 | spec | AC12 | pass |
| T18 | 7 | route documents 401/403/422/500 with ErrorResponse | code-derived | router responses | pass |
| T19 | 2 | existing `GET /users` tests unchanged | spec | AC14 | pass |

## Open Questions
- None.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`: the local shell sets `LLM_MAX_TOKENS=2000`, so the documented default (800) isn't what loads. Environment, not code. Still failing.
- `tests/modules/interviews/test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`: timing-sensitive (`budget_left_ms` 29999 vs 30000). Failed in the baseline run, passed in the final run.

## Known Issues
- Ruff could not be run: it is not a project dependency, and `uvx` is blocked by the lean-ctx shell allowlist. The editor's ruff showed no diagnostics on the open route file; a stdlib AST pass found no unused imports and no new lines over 120 characters. Run `ruff check .` once it is available.
- `CLAUDE.md` lists `uv run ruff ...` as a common command, but ruff is not in `pyproject.toml`'s dev group.

## Deviations from Plan
- Index is plain (user_id, id), not (user_id, id DESC): a btree serves the descending order by scanning backwards, confirmed by EXPLAIN on PostgreSQL. plan.md Step 4 updated. Meets the spec ("index-backed newest-first list").
- AC12 test counts only the history's own statements: the auth user lookup runs only on the first request in a test (the shared test session's identity map caches the user afterwards), which is a test artifact, not page-size dependent. Found by printing the statements (attempt 1 failed, attempt 2 passed).

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 1-2 | lean-ctx, graphify | callers of the users pagination constants; OpenAPI before/after diff |
| 4 | lean-ctx | alembic head, autogenerate review, PostgreSQL upgrade/downgrade and EXPLAIN |
| 5-7 | tdd (HTTP seam, user-confirmed) | red -> green: slice 1 (405 -> 200), slice 8 (stub 0 -> rule) |
| 8 | graphify | `graphify update .` (2978 nodes) |

## Links
- Spec: docs/features/interview-history/spec.md
- Plan: docs/features/interview-history/plan.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite green except the recorded baseline failure (no build step in this project; `compileall` OK)
- [x] Every spec.md acceptance criterion met by actual code and covered by a passing spec test (AC13 verified on PostgreSQL, not in pytest)
- [x] Open Questions resolved or explicitly surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [x] Commits documented (suggested message above; nothing committed)
- [x] No open blockers
- [x] Code follows project rules (CLAUDE.md)
- [x] No unresolved plan deviations
