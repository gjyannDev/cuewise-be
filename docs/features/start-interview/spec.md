# Feature: Start an Interview (backend)

## Problem
A candidate can log in but cannot practice anything yet: there is no way to say what they want to practice (role, level, type, how many questions) and no interview session or question data exists in the API. The client's "Start interview" form has nothing to submit to and the chat screen has no first question to show.

## Goal
A logged-in candidate submits an interview setup and gets back a **saved session** plus its **first question**, and can fetch that session again later. Measured by: `POST /api/v1/interviews` with a valid setup returns 201 with a persisted session and exactly one question (position 1), drawn from a hand-written question bank that matches the chosen role, level and type.

## Project Conventions
- Rule files consulted: `CLAUDE.md` (project root; there is no `.claude/` directory), `docs/features/rbac/spec.md` (existing auth/permission pattern). No `graphify-out/` exists, so code orientation was done with lean-ctx.
- Constraints those rules impose on this feature:
  - Layers: route -> controller -> repository. New module `app/modules/interviews/` with files prefixed `interviews_` (`interviews_route.py`, `interviews_controller.py`, `interviews_repository.py`, `interviews_schema.py`, `interviews_utils.py`, plus `interviews_model.py` / `interviews_constants.py` / `interviews_dependencies.py` as needed). Models are registered in `app/db/models.py` so Alembic sees them.
  - IDs: every new table's primary key and every foreign key to it is a UUID (UUIDv7 via `UUIDPrimaryKeyMixin`); routes and schemas carry the UUID as a string; no integer ids are exposed or accepted.
  - Pydantic schemas on all input, `extra="forbid"`, constrained lengths/enums; `response_model` and explicit `status_code` on every route; `responses=` documents 401/403/404/409/422 using the shared `ErrorResponse`.
  - Errors use `core/errors.py` (structured, generic client messages, details in logs with request ID). Authorization via `require_permissions(...)`; ownership is enforced in the controller, not only authentication.
  - Schema changes only via a new Alembic migration; applied migrations are not edited.
  - Do not log raw user content: `job_description` must never appear in logs (CLAUDE.md privacy rule).
  - AI guidelines: this story makes **no** LLM calls and adds no new dependency. `job_description` is untrusted user text that a later story will put into prompts, so it is validated and bounded now.
  - Tests under `tests/modules/interviews/` (happy path, validation errors, auth/authz failures); run `uv run pytest` and `uv run ruff check .`.
  - Do not commit or push.
- Decided with the user (deviations / choices):
  - Role is a fixed enum, not free text, because a hand-written bank can only cover roles that were written for.
  - OpenRouter / LLM work is deferred to the next story (story 3, "Chat with the interviewer": interviewer prompt, model adapter, SSE streaming, follow-ups, saved messages). Until then the question bank is a **defined mock-up** (placeholder questions that make the flow work end to end), not final content.
  - One in-progress session per user; starting a new one auto-abandons the previous (no end endpoint in this story).

## User Flow
1. The candidate fills the setup form (role, level, interview type, number of questions, optionally a job description) and submits.
2. The client calls `POST /api/v1/interviews` with the bearer token.
3. The API validates the setup, picks questions from the bank, abandons any previous in-progress session of that user, saves the new session with its questions, and returns the session plus the first question.
4. The client navigates to the chat screen and shows the first question.
5. If the page is reloaded, the client calls `GET /api/v1/interviews/{id}` and gets the session and its current question again.

## Requirements

### Functional
- **Setup fields** (`POST /api/v1/interviews` body, `extra="forbid"`):
  - `role`: one of `frontend`, `backend`, `fullstack`, `mobile`, `data`.
  - `level`: one of `intern`, `junior`, `mid`, `senior`.
  - `interview_type`: one of `behavioral`, `technical`, `mixed`.
  - `question_count`: integer 1-10.
  - `job_description`: optional string, at most 2000 characters after trimming; surrounding whitespace is trimmed; an empty or whitespace-only value is stored as null. Stored now, not used by any logic yet.
- **Question bank**: a hand-written JSON file inside the module. Each entry has `id` (unique string), `text`, `type` (`behavioral` or `technical`), `roles` (list of the five roles and/or the bank-only tag `general`, which matches every role) and `levels` (list of levels). It is loaded and validated with Pydantic; an invalid file (duplicate id, empty text, unknown role/level/type, empty `roles`/`levels`) stops the app from starting with a clear error rather than failing at request time.
- **Question selection** (pure logic, separate from the DB):
  - A question is eligible when its type matches, its `levels` contain the requested level, and its `roles` contain the requested role or `general`.
  - Selection is a random sample without repeats (a bank question appears at most once per session).
  - `behavioral` / `technical`: all questions come from that type.
  - `mixed`: split about evenly between behavioral and technical; when `question_count` is odd the extra one is behavioral; behavioral and technical questions are interleaved in the final order (behavioral first).
  - If fewer eligible questions exist than requested (for `mixed`, per type), nothing is created and the request fails with 409 `NOT_ENOUGH_QUESTIONS`; the error details include how many are available so the user can lower the count. The API never silently returns fewer questions than asked.
- **Tables** (one new Alembic migration):
  - `interview_sessions`: id, user_id (FK to users), role, level, interview_type, question_count, job_description (nullable), status (`in_progress` or `abandoned`; plain string column, not a native DB enum; `completed` is added by the answering story), created_at.
  - `interview_questions`: id, session_id (FK to the session), position (1..N, unique within the session), text, category (`behavioral` or `technical`), bank_id (the bank entry it came from).
- **Snapshot**: question text is copied into `interview_questions` at creation. Later edits to the bank file never change existing sessions.
- **One active session per user**: creating a session sets the same user's existing `in_progress` session (if any) to `abandoned`, and creates the new one as `in_progress`, in a single transaction. If anything fails, nothing is persisted and the previous session is unchanged. The database itself guarantees at most one `in_progress` session per user.
- `POST /api/v1/interviews` -> 201. Response: the session (`id`, `role`, `level`, `interview_type`, `question_count`, `job_description`, `status`, `created_at`) and `current_question` (`id`, `position`, `text`, `category`) which is position 1. Only the first question is returned; later questions are never included. `bank_id` is not exposed.
- `GET /api/v1/interviews/{session_id}` -> 200 with the same shape. `current_question` is the question at position 1 (no answering exists yet, so the current question is always the first). Works for `abandoned` sessions too; `status` tells the client.
- **Ownership**: a session that does not exist and a session owned by another user both return the identical 404 `NOT_FOUND`, so ids cannot be probed. Checked in the controller.
- **Permissions**: two new code-defined permissions, `interviews:create` and `interviews:read_self`, held by both `admin` and `user`, enforced with `require_permissions` on the routes. `/auth/me` therefore lists them for both roles.
- The router is registered under `/api/v1` in `main.py` with prefix `/interviews` and a tag.

### Non-Functional
- Security: both endpoints are default-deny (no token -> 401 before any business logic). Responses are whitelisted via `response_model`. `job_description` is never logged.
- Atomicity: session creation (abandon previous + insert session + insert questions) is all-or-nothing.
- Determinism: selection logic can be tested by controlling the random source; no test depends on a real random outcome.
- Performance: the bank is loaded once, not re-read per request. No numeric latency target at this scale.

## UX Requirements
- Error responses use the existing structured shape (`error.code`, `message`, `request_id`); validation failures use the existing 422 shape so the client can map them to form fields.
- The enum values above are the contract the client form (validated with Zod) must mirror exactly.
- The `NOT_ENOUGH_QUESTIONS` error carries the available count so the client can show "only N questions available for this setup".

## Constraints
- No LLM / OpenRouter calls, no new dependencies in this story.
- Python >= 3.14, FastAPI, sync SQLAlchemy `Session` (as in the existing modules), Alembic, `uv`.
- The bank is a **mock-up**: a small, clearly placeholder set written during implementation (not final interview content). It must be enough to run a 5-question session for any valid setup: at least 5 `general` behavioral and 5 `general` technical entries tagged with all four levels, plus a few role-specific entries so every role, level and type appears at least once. Counts above what the mock bank holds (e.g. 10 with `mixed`) may legitimately return `NOT_ENOUGH_QUESTIONS`.
- The mock must stay replaceable: story 3 will have an LLM drive the interview (asking, following up, streaming). Only the question source may change then; the session/question tables, endpoints and selection function seam stay as specified here. The bank is not expected to be thrown away, since it remains a deterministic baseline and fallback.
- Client is the Next.js app; it calls FastAPI server-to-server with the bearer token (see RBAC spec). No cookie handling in the API.

## Blockers
- None. (The mock bank is written during implementation and tests use their own small fixture banks, so nothing waits on final question content.)

## Edge Cases
Format: condition -> expected outcome.

- **EC1:** `POST /api/v1/interviews` or `GET /api/v1/interviews/{id}` with no/invalid/expired token -> 401 with the existing `TOKEN_*` codes.
- **EC2:** Authenticated user whose role lacks the required permission -> 403 `FORBIDDEN`.
- **EC3:** `role`, `level` or `interview_type` not in its enum (including wrong case) -> 422; no session created.
- **EC4:** `question_count` of 0, 11, negative, non-integer, or missing -> 422; no session created.
- **EC5:** Body contains an unknown field (e.g. `status`, `user_id`) -> 422 (`extra="forbid"`); the client can never set server-owned fields.
- **EC6:** `job_description` longer than 2000 characters after trimming -> 422; exactly 2000 characters -> accepted.
- **EC7:** `job_description` is empty or whitespace-only -> accepted and stored/returned as null; omitted -> null.
- **EC8:** Bank has fewer eligible questions than `question_count` -> 409 `NOT_ENOUGH_QUESTIONS` with the available count in details; no session created and the user's previous in-progress session is left untouched.
- **EC9:** `mixed` with `question_count` 1 -> one behavioral question; with 5 -> 3 behavioral + 2 technical, interleaved starting with behavioral.
- **EC10:** `mixed` where one type has enough eligible questions but the other does not -> 409 `NOT_ENOUGH_QUESTIONS` (no silent rebalancing).
- **EC11:** A `general`-tagged question is eligible for every role; a question tagged only `backend` is never selected for `frontend`.
- **EC12:** The same bank question is never selected twice in one session.
- **EC13:** User already has an in-progress session and starts another -> the old one becomes `abandoned`, the new one `in_progress`; `GET` on the old id still returns 200 with `status: abandoned`.
- **EC14:** Two concurrent `POST` requests from the same user -> exactly one `in_progress` session remains; the request that loses the race returns 409 `CONFLICT` and creates nothing.
- **EC15:** A database error while saving questions -> no session row is left behind and the previous session is not abandoned; the client gets the generic 500 error shape.
- **EC16:** The bank file is edited after a session was created -> that session's questions are unchanged.
- **EC17:** The bank file is invalid (duplicate id, empty text, unknown enum value, empty `roles`/`levels`) -> the app fails to start with a clear error message.
- **EC18:** `GET` for a session id that does not exist -> 404 `NOT_FOUND`.
- **EC19:** `GET` for a session owned by a different user -> the identical 404 `NOT_FOUND` (same body apart from `request_id`).
- **EC20:** `GET /api/v1/interviews/not-a-uuid` -> 422.
- **EC21:** A second user (or admin) never sees another user's session through any endpoint -> admins get no special read access to others' sessions in this story.

## Acceptance Criteria
Specific, testable criteria with an observable outcome:

- [ ] **AC1:** A new Alembic migration creates `interview_sessions` and `interview_questions` with UUID primary keys and UUID foreign keys; upgrading a database that already has users succeeds and downgrading removes the two tables.
- [ ] **AC2:** `POST /api/v1/interviews` with a valid body and token returns 201, persists one session row for the caller (`status=in_progress`) and `question_count` question rows with positions 1..N, and the response contains the session fields plus `current_question` at position 1 only (EC9, EC12).
- [ ] **AC3:** Every question of the created session is eligible for the requested role, level and type per the selection rules, and no `bank_id` repeats within a session (EC11, EC12).
- [ ] **AC4:** `mixed` produces the even behavioral/technical split with the extra question behavioral when odd, interleaved starting with behavioral (EC9), and rejects with 409 when either type lacks enough eligible questions (EC10).
- [ ] **AC5:** When fewer eligible questions exist than requested, `POST` returns 409 `NOT_ENOUGH_QUESTIONS` whose details include the available count, creates nothing, and leaves any existing in-progress session unchanged (EC8).
- [ ] **AC6:** Invalid bodies return 422 and create nothing: bad enum values, `question_count` outside 1-10, unknown fields, `job_description` over 2000 characters (EC3-EC6); an empty/whitespace `job_description` is stored as null and 2000 characters is accepted (EC6, EC7).
- [ ] **AC7:** Starting a new interview abandons the user's previous in-progress session in the same transaction; afterwards the user has exactly one `in_progress` session, and the old one is still readable with `status: abandoned` (EC13).
- [ ] **AC8:** A failure while saving questions rolls back everything: no new session row and the previous session is not abandoned (EC15).
- [ ] **AC9:** The database prevents two `in_progress` sessions for one user; the losing concurrent request returns 409 `CONFLICT` (EC14).
- [ ] **AC10:** `GET /api/v1/interviews/{session_id}` returns 200 with the session and `current_question` (position 1) for the owner, including for `abandoned` sessions; it never returns questions beyond position 1 (EC13).
- [ ] **AC11:** Missing and foreign session ids return identical 404 `NOT_FOUND` bodies apart from `request_id`; a malformed id returns 422 (EC18-EC21).
- [ ] **AC12:** Both endpoints return 401 without a valid token and 403 for a caller lacking the permission; `interviews:create` and `interviews:read_self` are in the role->permission map for `admin` and `user`, a test asserts that mapping, and `/auth/me` lists them (EC1, EC2).
- [ ] **AC13:** Question text is snapshotted: changing the bank content after creation does not change a stored session's questions (EC16).
- [ ] **AC14:** The bank is validated at load time by Pydantic: an invalid bank file raises a clear error at startup (EC17); the shipped mock `questions.json` loads, covers both types, all five roles and all four levels, and can supply a 5-question session (all three interview types) for every role and level combination.
- [ ] **AC15:** Selection logic is unit-tested in isolation from the DB with a controlled random source and fixture banks.
- [ ] **AC16:** Response models never expose `bank_id`, other users' data, or ORM objects; OpenAPI documents 401/403/404/409/422 for the new routes with the shared `ErrorResponse`.
- [ ] **AC17:** No log line produced by these endpoints contains `job_description` content.
- [ ] **AC18:** Existing tests that depend on the permission list (e.g. `/auth/me` or the role map) are updated; `uv run pytest` and `uv run ruff check .` both pass.

## Out of Scope
- Any LLM / OpenRouter call, prompt files, model adapter, SSE streaming, follow-up questions (max 2 per question), saved chat messages, or answer evaluation: all of story 3 ("Chat with the interviewer"), so this one stays a plain data slice.
- Final, curated question content: the bank here is a mock-up to prove the flow.
- Submitting answers, advancing to the next question, completing a session, scoring or feedback: the answering story. (`completed` status and a `current_position` are added then.)
- An "end interview" endpoint, listing/history of sessions, deleting sessions: nothing needs them yet; auto-abandon covers the one-active rule.
- Using `job_description` for question selection or prompting: stored only.
- Free-text roles, `system_design` type, custom/user-authored questions, difficulty tuning, time limits: the bank and form stay small.
- Admin access to other users' sessions: not needed; revisit if a support/admin view appears.
- Rate limiting: CLAUDE.md requires it eventually; deferred with the LLM story, when requests start costing money.
- The Next.js form, Zod schema and chat screen: separate frontend work (this spec only fixes the contract they mirror).
