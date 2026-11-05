# Feature: Interview History List (backend)

## Problem
The web app's History page needs to show a candidate all of their previous interviews in a table and let them pick up the one that is still in progress. The API cannot do this: it only has per-id endpoints (`GET /interviews/{id}` and its `/messages`), so the client has no way to learn which interviews exist, what state they are in, or how far along they got.

## Goal
A logged-in candidate can fetch a **paginated, newest-first list of their own interviews** (every status: `in_progress`, `completed`, `abandoned`), each row carrying enough to render a table row and to decide whether it can be continued. Measured by: `GET /api/v1/interviews` returns 200 with only the caller's interviews, correct `total`, and a per-row `answered_count`; the single `in_progress` row can be continued with the existing `GET /interviews/{id}` and `/messages` endpoints with no change to them.

## Project Conventions
- Rule files consulted: `CLAUDE.md` (project root; there is no `.claude/` directory), `docs/features/start-interview/spec.md` (sessions, one-in-progress rule), the existing paginated list `GET /users` (`app/modules/users/`). graphify and lean-ctx used for orientation.
- Constraints those rules impose on this feature:
  - Layers: route -> controller -> repository inside `app/modules/interviews/`, files prefixed `interviews_`; schemas in `interviews_schema.py`. No business logic in the route, no SQL in the controller.
  - Pagination follows the existing `GET /users` contract so clients see one convention: query params `limit` (1-100, default 20) and `offset` (>= 0); response `{items, total, limit, offset}`. List endpoints must paginate (CLAUDE.md).
  - IDs are UUIDs as strings; ordering uses the time-ordered UUIDv7 id (no extra sort column).
  - `response_model`/typed return, explicit `status_code`, `responses=` documenting 401/403/422 with the shared `ErrorResponse`.
  - Authorization: `require_permissions(Permission.interviews_read_self)` (already held by `admin` and `user`; no new permission). Ownership is enforced in the controller/repository query: the list is always scoped to the caller.
  - Schema change only through a new Alembic migration; applied migrations are not edited.
  - Privacy: the list must not expose or log `job_description`, its summary, answers, or any interview content.
  - Tests under `tests/modules/interviews/` (happy path, validation errors, auth/authz failures); run `uv run pytest` and `uv run ruff check .`. Run `graphify update .` afterwards. Do not commit or push.
- Decided with the user:
  - Abandoned interviews are listed like any other (including ones abandoned with zero answers).
  - `answered_count` counts **main questions finished**, not individual answers, so it never exceeds `question_count`.
  - The `status` filter takes one optional value.

## User Flow
1. The candidate opens the History page; the client calls `GET /api/v1/interviews?limit=20&offset=0`.
2. The API returns that page of the candidate's interviews, newest first, plus `total` for the pager.
3. The table shows role, level, type, status, "answered X of N" and date. The candidate may narrow it with `?status=completed` (or `abandoned`, `in_progress`).
4. On the one row with `status = in_progress`, the client offers **Continue**: it calls the existing `GET /interviews/{id}` (current question) and `GET /interviews/{id}/messages` (chat so far) and resumes answering.
5. Rows with `completed` or `abandoned` have no Continue action; the backend does not allow answering them.

## Requirements

### Functional
- **Endpoint:** `GET /api/v1/interviews`, 200.
  - Query: `limit` (int 1-100, default 20), `offset` (int >= 0, default 0), `status` (optional; one of `in_progress`, `completed`, `abandoned`), `sort_by` (one of `created_at`, `role`, `level`, `interview_type`, `status`; default `created_at`), `sort_dir` (`asc` or `desc`; default `desc`). Added with the frontend table rework (`cuewise-fe/docs/features/interview-history/plan.md`).
  - Response: `{items: [...], total, limit, offset}`; `total` is the number of the caller's interviews matching the filter (all statuses when no filter), independent of `limit`/`offset`.
- **Scope:** only interviews owned by the authenticated user are listed or counted. Other users' interviews never appear, whatever the role.
- **Order:** newest first (most recently started first) by default, stable across requests. `sort_by` / `sort_dir` sort the whole filtered history server-side by the column's stored value (not its label); `created_at` uses the UUIDv7 id; ties are newest first (`id desc`), so pages never overlap or skip a row.
- **Item fields:** `id`, `role`, `level`, `interview_type`, `status`, `question_count`, `answered_count`, `created_at`. Nothing else: no `job_description`, no summary, no `user_id`, no question or answer text, no usage metadata.
- **`answered_count`** = number of main questions the candidate has finished:
  - `completed` -> equals `question_count`.
  - `in_progress` and `abandoned` -> the main-question number of the question the interview was waiting on, minus 1. A pending follow-up of main question 3 therefore counts 2.
  - Always between 0 and `question_count`.
- **Continue support:** no change to existing endpoints. At most one row is `in_progress` per user (existing database guarantee), and it is always the newest row, so it is the first item of an unfiltered first page under the default order.
- **Shared pagination (`app/core/pagination.py`):** the pagination contract lives once in `app/core/`, as composition and not base classes (decided with the user: no `BaseRepository`/`BaseService`, as only pagination is duplicated today):
  - a `PageParams` dependency (`limit` 1-100 default 20, `offset` >= 0) and a generic `Page[T]` response model (`items`, `total`, `limit`, `offset`);
  - both `GET /users` and `GET /interviews` use them. `GET /users` is refactored with **no change in behavior or response shape**, and its page-size constants move from `users_constants.py` to the shared module.
- **Index:** listing a user's interviews newest-first must be index-backed (new migration adding an index on the interviews table for the owner and newest-first order).
- **Empty:** a user with no interviews (or none matching the filter) gets 200 with `items: []`, `total: 0`.

### Non-Functional
- Fetching a page issues a fixed, small number of queries regardless of page size (no per-row query).
- Response size is bounded by `limit <= 100` and excludes free-text fields.
- Security: default-deny auth; the endpoint is unreachable without a valid token and the `interviews:read_self` permission; another user's data cannot be inferred from `total`.

## UX Requirements
(For the client; the backend only has to supply the data.)
- Table row can be rendered from one item with no extra request (status label, "answered X of N", date from `created_at`).
- Continue is shown only when `status == in_progress`.
- Errors use the shared structured error body with a generic message and `request_id`.

## Constraints
- No LLM calls and no new dependency.
- The History page itself is built in the separate front-end project.
- Pagination is offset-based, matching `GET /users`.
- Sessions created before follow-up questions existed (their `main_number` defaults to the question position) must give correct counts.

## Blockers
- None. Nothing depends on an external system.

## Edge Cases
Format: condition -> expected outcome.

- **EC1:** User has no interviews -> 200, `items: []`, `total: 0`, echoed `limit`/`offset`.
- **EC2:** Another user has interviews -> none of them appear in `items`, and `total` excludes them.
- **EC3:** `limit=0`, `limit=101`, `limit=abc`, or `offset=-1` -> 422 structured error, nothing queried.
- **EC4:** `offset` beyond `total` -> 200, `items: []`, `total` still the real count.
- **EC5:** `status` is not one of the three values (e.g. `status=done`) -> 422.
- **EC6:** `status=abandoned` filter -> only abandoned rows; `total` is the count of abandoned rows only.
- **EC7:** In-progress interview waiting on a follow-up of main question 2 -> `answered_count` = 1.
- **EC8:** Completed interview (any number of follow-ups) -> `answered_count` = `question_count`.
- **EC9:** Interview started and abandoned before any answer -> listed, `status = abandoned`, `answered_count` = 0.
- **EC10:** Interview from before follow-ups existed (all questions stored up front) -> `answered_count` = its current position minus 1 while not completed.
- **EC11:** No token / invalid token -> 401; valid token without `interviews:read_self` -> 403.
- **EC12:** User starts a new interview between two page requests -> the new row is first and rows may shift by one, so an item can repeat on the next page; accepted for offset pagination.
- **EC13:** An interview with a `job_description` -> the field (and its summary) is absent from the item.
- **EC14:** Two interviews created in quick succession -> ordered by creation, newest first, never reordered between calls.
- **EC15:** `sort_by` or `sort_dir` not one of the listed values (e.g. `sort_by=progress`, `sort_dir=up`) -> 422.
- **EC16:** Sorting by a column with equal values (e.g. two `backend` rows) -> tied rows newest first; walking the pages gives every row exactly once.

## Acceptance Criteria

- [x] **AC1:** `GET /api/v1/interviews` with a valid token returns 200 with `{items, total, limit, offset}`; defaults are `limit=20`, `offset=0`.
- [x] **AC2:** Items contain exactly `id`, `role`, `level`, `interview_type`, `status`, `question_count`, `answered_count`, `created_at`; `job_description`, its summary and `user_id` are never present (EC13).
- [x] **AC3:** Only the caller's interviews are returned and counted; with interviews of two users, each sees only their own (EC2).
- [x] **AC4:** Items are ordered newest first (EC14); the `in_progress` interview, when one exists, is the first item.
- [x] **AC5:** `limit` and `offset` page the results; `total` is the full count for the filter; `limit` outside 1-100 or `offset` < 0 gives 422 (EC3); an `offset` past the end gives an empty page with the real `total` (EC4).
- [x] **AC6:** `?status=` accepts `in_progress`, `completed` or `abandoned`, filters both `items` and `total` (EC6), and any other value gives 422 (EC5).
- [x] **AC7:** All three statuses are listed when no filter is given, including abandoned interviews with no answers (EC9).
- [x] **AC8:** `answered_count` follows the definition above: `question_count` for completed (EC8), main question number - 1 otherwise, including a pending follow-up (EC7) and pre-follow-up sessions (EC10).
- [x] **AC9:** An empty history returns 200 with `items: []` and `total: 0` (EC1).
- [x] **AC10:** Without a token the endpoint returns 401; without `interviews:read_self` it returns 403 (EC11).
- [x] **AC11:** The row of an `in_progress` interview can be resumed with the unchanged `GET /interviews/{id}` and `/messages` (checked by an existing-endpoint call in a test).
- [x] **AC12:** A page is produced with a constant number of queries independent of `limit` (checked by a test that counts queries for two page sizes).
- [x] **AC14:** `GET /users` uses the shared pagination and behaves exactly as before: the existing `tests/modules/users/test_list_users.py` passes unchanged, and `GET /users` and `GET /interviews` share one `PageParams` and one `Page[T]` (no duplicated `limit`/`offset` definitions or page-size constants left in `users`).
- [x] **AC15:** `sort_by` / `sort_dir` order the whole filtered history (all five columns, both directions), with ties newest first and no page overlap (EC16); unknown values give 422 (EC15); no params keep the AC4 order; the query count stays constant (AC12).
- [x] **AC13:** The new migration applies and downgrades cleanly and adds the owner/newest-first index; `uv run pytest` and `uv run ruff check .` pass.

## Out of Scope
- The History page UI (separate front-end project).
- Resuming an abandoned or completed interview: the existing rules stay (only `in_progress` accepts answers; starting a new interview abandons the old one).
- Deleting, renaming, archiving or restarting interviews.
- Text search, date-range filters, multi-status filter, multi-column sort, and label/semantic ordering (e.g. seniority for `level`): no client need yet (YAGNI). Single-column sorting was added later (AC15).
- A `BaseRepository` / `BaseService` (generic CRUD or business-logic base classes): only pagination is duplicated, and the repositories and controllers differ too much. Revisit if four or more repositories end up with identical methods.
- Cursor pagination; offset matches `GET /users` and is enough at personal-history sizes.
- Scores, feedback or report links per interview.
- Admin views of other users' interviews.
- A "current/active interview" shortcut endpoint: the first item of the list already identifies it.
