# Implementation Plan: UUID primary keys

## Overview
Replace auto-increment integer ids with app-generated UUIDv7 on every table (today only `users`), as required by the new CLAUDE.md rule, so ids in URLs, responses and JWT `sub` are not guessable.

## Architecture & Design
A small shared mixin in `app/db/` gives any model a `Uuid` primary key defaulting to `uuid.uuid7()` (stdlib, Python 3.14), so future tables inherit the rule instead of repeating it. `User` uses the mixin. Everything that touched an integer id (JWT `sub`, repository lookup, response schemas) switches to `UUID`. The schema change is one new hand-written Alembic revision that drops and recreates `users` (user-confirmed; local data is discarded). No spec.md exists: requirements below come from the CLAUDE.md rule and the request.

## Requirements (no spec; derived) -> Implementation
- R1 `users.id` is a UUIDv7 generated in the app, no DB-side default -> Steps 1, 3
- R2 Shared mixin so every future table gets the same key -> Step 1
- R3 JWT `sub` carries the UUID string; non-UUID `sub` is rejected -> Step 2
- R4 Response schemas expose `id` as UUID (JSON string) -> Step 1
- R5 `GET /users` still lists in creation order (`id` ascending) -> Step 1
- R6 Docs and memory no longer describe integer ids -> Step 4

Edge cases (condition -> outcome):
- E1 Token issued before the change (integer `sub`) -> 401 `TOKEN_INVALID`
- E2 `sub` is not a valid UUID -> 401 `TOKEN_INVALID`
- E3 Two users created back to back -> list order equals creation order (depends on `uuid7` being monotonic in one process; verify)
- E4 Migration applied to a DB with existing users -> table recreated empty; admin re-created with the script
- E5 Downgrade -> recreates the integer-key table (empty); data is not restored

## Implementation Steps
1. **Mixin, model, schemas.** Add `app/db/mixins.py` with a UUID primary key mixin (`Uuid` column, `default=uuid.uuid7`). `User` inherits it and drops its own `id`. Change `id` to `UUID` in `UserOut`, `MeOut`, `UserAdminOut`; `get_by_id` takes a `UUID`. `users` ordering stays `id` ascending. — Test: first. Seam: HTTP via TestClient. Slices: `/auth/me` returns an `id` that parses as a UUID with version 7; register response id is a UUID; `/users` items carry UUID ids and come back in creation order across 5 quick inserts (R1, R4, R5, E3).
2. **Tokens.** `create_token(user_id: UUID, role)` writes the canonical string as `sub`; `authenticate_token` parses `sub` with `UUID(...)` and maps a parse error to `TokenInvalidError`. — Test: first. Seam: `create_token`/`decode_token` and HTTP guard routes. Slices: round trip keeps the exact UUID string; `sub="1"` (old integer token) is `TOKEN_INVALID`; `sub="not-a-uuid"` is `TOKEN_INVALID`; deleted/deactivated user cases still 401 (R3, E1, E2).
3. **Migration.** New hand-written revision after `965af3737bf4` (autogenerate would try an unsafe integer-to-uuid cast): drop `users` (and its email index), recreate it with a `Uuid` primary key, unique indexed `email`, `password_hash`, `role` and `is_active` with their existing server defaults. Downgrade drops it and recreates the integer-key version. Review the generated SQL before applying. — Test: after (manual on Postgres: upgrade, confirm `id` is type uuid and the table is empty, run `create_admin`, downgrade then upgrade again; `alembic check` shows no drift) (R1, E4, E5).
4. **Docs and memory.** Update `docs/features/rbac/{spec,plan,task}.md` where they say integer ids (`sub` is "user id", pagination "ordered by id") to say UUID; add the new plan's task log under this feature; add one line to the architecture memory. CLAUDE.md already has the rule. — Test: skip (R6).
5. **Wrap-up.** Update remaining fixtures/tests that assumed integers (`tests/core/test_tokens.py` uses `sub="1"` and `"42"`; guard tests build tokens by hand). Run `uv run pytest`, `uv tool run ruff check app tests`, `alembic check`. Do not commit. — Test: skip.

## Affected Files & Patterns
- `app/db/mixins.py` (new) — shared UUID key mixin.
- `app/modules/auth/auth_model.py`, `auth_schema.py`, `auth_repository.py`, `auth_controller.py` — UUID typing, `sub` parsing.
- `app/core/tokens.py` — `user_id` typed `UUID`.
- `app/modules/users/users_schema.py`, `users_repository.py` — `id` type; ordering unchanged.
- `alembic/versions/` — one new revision; applied revisions untouched.
- `tests/core/test_tokens.py`, `tests/modules/auth/test_guards.py`, `tests/conftest.py` — adjust integer assumptions.
- `docs/features/rbac/*`, memory note — wording.
- Patterns to follow: existing mixin-free `Base` in `app/db/session.py` (mixin sits beside it, not inside); route/controller/repository layering; sync routes.
- Risks: every issued token becomes invalid (accepted); the local `users` row and its password are deleted by the migration; SQLite test DB stores UUIDs as strings, which sort the same as Postgres bytes for UUIDv7, but ordering across the same millisecond relies on `uuid7` monotonicity (verified by the E3 slice).

## Testing Strategy
- Framework & command: pytest, `uv run pytest`; lint `uv tool run ruff check app tests`.
- Confirmed seams: HTTP endpoints via TestClient, `create_token`/`decode_token`, the admin script's `main` (unchanged). Migration verified manually on Postgres (user-confirmed).

| Check | Step | Test mode | Notes |
|-------|------|-----------|-------|
| R1, R4 | 1 | first | me/register/users ids parse as UUIDv7 |
| R5, E3 | 1 | first | 5 quick inserts list in creation order |
| R3, E1, E2 | 2 | first | integer and malformed `sub` -> TOKEN_INVALID |
| R1, E4, E5 | 3 | after | manual Postgres run, `alembic check` |
| R6 | 4 | skip | docs only |

- Must verify, not assume: `uuid.uuid7()` exists on the installed Python and is monotonic for back-to-back calls; SQLAlchemy `Uuid` round-trips on both SQLite (tests) and Postgres; Pydantic serializes `UUID` ids as strings in responses.
- Open questions: none.
- Known baseline failures: none (100 passing before this change).

## Blockers & Resolutions
- No blockers.
- Existing data -> user chose drop and recreate; re-create the admin afterwards with the script.
- Autogenerate would attempt an integer-to-uuid type change that fails on Postgres -> hand-write the revision.

## Trade-offs & Rationale
- UUIDv7 over v4: time-ordered, so new rows append to the key index; stdlib, no dependency.
- App-generated only (user-confirmed): works on any Postgres version; raw SQL inserts must supply ids.
- Drop and recreate (user-confirmed): simplest, safe SQL; costs the one local user.
- Shared mixin even with one table: the CLAUDE.md rule covers every table, and four lines prevents drift.

## Project Rules Applied
- `CLAUDE.md` IDs rule -> UUIDv7, `Uuid` column, ids as strings in routes, schemas and JWT `sub`.
- `CLAUDE.md` DB -> schema change only through a new Alembic revision; applied revisions are not edited.
- `CLAUDE.md` testing/git -> tests first at confirmed seams; do not commit.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | found every integer-id use (tokens, controller, repository, schemas, tests) |
| grill-me | migration strategy, DB default, test seams (answered) |
| ponytail | stdlib `uuid7`, no new dependency, no DB-side default, one mixin |
| security-review | inline: removes enumerable ids; invalid `sub` stays a generic 401 |
| graphify | skipped: no `graphify-out/` |

## Ready to Implement
- All requirements mapped to steps
- Every step has a Test tag; every check mapped in Testing Strategy
- Affected files identified
- Blockers resolved, edge cases handled
- Trade-offs documented with rationale
- No spec.md (by request); requirements derived from CLAUDE.md and the request
