# Implementation Plan: Role-Based Access Control (single JWT)

## Overview
Add login, a single signed JWT, DB-backed current-user resolution, and role/permission route guards, plus an admin-only paginated user list and an admin bootstrap script.

## Architecture & Design
Token helpers live in `core/tokens.py`, separate from password hashing in `core/security.py` (role passed as a plain string so core never imports modules). The auth module gains `constants.py` (Role, Permission, ROLE_PERMISSIONS, `permissions_for`) and `dependencies.py` (`get_controller`, `get_current_user`, `require_roles`, `require_permissions`). Guards are per-route `Depends(...)`, never middleware. `get_current_user` goes dependency -> `AuthController` -> repository and reloads the user from the DB every request. A new `users` module owns `GET /users` and reuses auth's guards. Routers are mounted under `/api/v1` in `main.py`; `/health` stays at the root.

## Spec Requirements -> Implementation
- Config/secret/issuer/audience/TTL, PyJWT, `.env.example` (AC12, EC18) -> Step 1
- Role/Permission/ROLE_PERMISSIONS/`permissions_for` (AC16, EC21) -> Step 3
- Token create/decode with pinned alg, exp/iss/aud (AC2, EC3-EC6) -> Step 4
- `role` + `is_active` columns and migration (AC1, EC19) -> Step 5
- Login, register hardening, token-to-user resolution (AC2, AC3, AC9, EC9, EC10, EC13, EC16) -> Step 6
- `get_current_user`, `require_roles`, `require_permissions` (AC4, AC8, AC17, AC18, EC1-EC8, EC12, EC20) -> Step 7
- `/auth/me`, `/api/v1` prefix, existing test path updates (AC5, AC10, AC13) -> Step 8
- `GET /users` paginated, admin-only (AC6, AC7, AC13, EC11, EC14, EC15) -> Step 9
- Admin bootstrap script (AC11, EC17) -> Step 10
- Log hygiene (AC14), lint/tests (AC15), no auth middleware (AC19) -> Steps 6, 7, 11

## Implementation Steps
1. **Config and dependency.** `uv add pyjwt`. Extend `core/config.py` with required `jwt_secret_key` (min length 32, no default so startup fails when unset), `jwt_algorithm` (HS256), `access_token_expire_minutes` (60), `jwt_issuer`, `jwt_audience`. Update `.env.example` and the `conftest.py` env defaults. Also add the shared test fixtures here: in-memory SQLite engine (static pool) created from `Base.metadata`, a `get_db` override, and helpers to create a user with a given role and mint a token. — Test: after (Settings validation; seam not in the confirmed list, so keep it to one small test)
2. **Folded into Step 1** (test infrastructure) so later steps can start red. — Test: skip
3. **Constants.** `modules/auth/constants.py`: `Role` StrEnum (admin, user), `Permission` StrEnum (`users:read`, `users:read_self`), `ROLE_PERMISSIONS` (admin: both; user: read_self), `permissions_for(role)` returning a frozenset; unknown role returns empty and logs a warning. Also pagination bounds (default 20, max 100) for Step 9. — Test: first. Seam: `permissions_for`. Slices: admin set, user set, unknown role is empty and logged (AC16, EC21).
4. **Token helpers.** In `core/tokens.py`: `create_token(user_id, role)` (claims sub as string, role, iat, exp, iss, aud) and `decode_token(token)` (algorithms list pinned to settings, require exp/iat/iss/aud/sub, map expired to `TokenExpiredError`, any other PyJWT failure to `TokenInvalidError`). — Test: first. Seam: `create_token`/`decode_token`. Slices: round-trip claims and `exp - iat` equal TTL; expired; tampered payload; wrong secret; `alg: none`; wrong iss; wrong aud (AC2, EC3-EC6).
5. **Model and migration.** Add `role` (String column with a Python StrEnum, not a native Postgres enum, so adding roles needs no ALTER TYPE; default user) and `is_active` (Boolean, default true) to `User`, both with server defaults. Generate a new Alembic revision with autogenerate, review it, make sure existing rows are backfilled; never edit the applied revision. — Test: after (manual `alembic upgrade head` on a Postgres DB that already has users; SQLite `create_all` covers the model in tests) (AC1, EC19)
6. **Login, register, resolution.** Add `LoginIn`, `TokenOut`, `MeOut` and set `extra="forbid"` on `LoginIn` and `RegisterIn` in `schema.py`. Repository: `get_by_id`. Controller: `login` (look up by email; verify the password against a precomputed dummy hash when the user is missing or inactive; any failure raises `InvalidCredentialsError` with one shared message) and `authenticate_token` (decode, parse sub as int, load user, reject missing/inactive with `TokenInvalidError`). Dummy hash constant goes in `utils.py`. Never log tokens, passwords or hashes. — Test: first. Seam: `POST /api/v1/auth/login` and `/register` via TestClient. Slices: valid login returns bearer token with claims; unknown email; wrong password; inactive user (identical bodies except request_id); malformed email/missing fields is 422; register with an extra `role` field is 422 and a normal register stores role user; password and token absent from captured logs (AC2, AC3, AC9, AC14, EC9, EC10, EC13, EC16).
7. **Dependencies.** `modules/auth/dependencies.py`: move `get_controller` here (`route.py` keeps importing it, so the existing override in tests still works); `get_current_user` using `HTTPBearer(auto_error=False)` and raising `TokenMissingError` for a missing header, wrong scheme or empty token; `require_roles(*roles)` and `require_permissions(*perms)` (all must be held) that both authorize from the DB user, never the token's role claim. — Test: first. Seam: HTTP through a test-only router (the existing conftest pattern) that mounts one route per guard. Slices: no header; non-bearer scheme; expired; tampered; wrong iss/aud; non-integer sub; deleted user; inactive user (all 401 with `WWW-Authenticate`); role changed in DB after minting (stale claim ignored, both directions); `require_roles` allow/deny; `require_permissions` allow, deny, and partial of several (AC4, AC8, AC17, AC18, EC1-EC8, EC12, EC20).
8. **Auth routes and versioning.** Add `POST /login` and `GET /me` (guard: `require_permissions(Permission.users_read_self)`, returns id, email, role, permissions) to `route.py` with `responses=` for 401/403/422/500. In `main.py` include routers with prefix `/api/v1`. Update existing tests that call `/auth/register` (`test_error_handling.py`, `test_register_errors.py`) to the new path; `/health` tests untouched. — Test: first. Seam: HTTP. Slices: me with valid token returns the right fields and no password_hash; old `/auth/register` is 404; OpenAPI lists ErrorResponse for the new routes; existing suite stays green (AC5, AC10, AC13).
9. **Users module.** New `modules/users/` with `route.py` (`GET /users`, guard `require_permissions(Permission.users_read)`, query `limit` ge 1 le 100 default 20 and `offset` ge 0 default 0, `responses=` for 401/403/422), `controller.py`, `repository.py` (list ordered by id plus a count query, selecting from the `User` model), `schema.py` (`UserAdminOut` with id, email, role, is_active; `UserListOut` envelope with items, total, limit, offset), `utils.py` (kept minimal; nothing speculative), `__init__.py`. Register the router in `main.py`. Mirror under `tests/modules/users/`. — Test: first. Seam: `GET /api/v1/users` via TestClient on SQLite. Slices: admin gets 200; user gets 403; defaults and id ordering; limit 101, limit 0, negative offset are 422; offset beyond total is empty items with correct total; OpenAPI documents the errors (AC6, AC7, AC13, EC11, EC14, EC15).
10. **Admin script.** `app/scripts/create_admin.py` with a `main(email, prompt_password)` function plus an argparse entry point (run via `uv run python -m app.scripts.create_admin <email>`). Creates the user as admin (password via `getpass`, same 8-128 length rule as registration) or promotes an existing user without touching the password; idempotent. Goes through the auth controller/repository, not raw SQL. — Test: first. Seam: `main`. Slices: new email is created as admin; existing user is promoted and hash unchanged; second run is a no-op (AC11, EC17).
11. **Wrap-up.** `uv run ruff check .` and `uv run ruff format .`, `uv run pytest`, manual Postgres migration check from Step 5, confirm `main.py` adds no auth middleware, review the diff for secrets in logs. Run `graphify update .` only if `graphify-out/` exists. Do not commit. — Test: skip (AC15, AC19)

## Affected Files & Patterns
- `pyproject.toml`, `uv.lock` — add `pyjwt`.
- `app/core/config.py`, `.env.example` — new JWT settings; required secret.
- `app/core/tokens.py` (new) — JWT create/decode; `app/core/security.py` keeps only Argon2 password hashing.
- `app/modules/auth/`: `constants.py` (new), `dependencies.py` (new), `model.py`, `schema.py`, `repository.py`, `controller.py`, `route.py`, `utils.py` (new).
- `app/modules/users/` (new, 6 files) and `app/scripts/create_admin.py` (new, plus `__init__.py`).
- `app/main.py` — `/api/v1` prefix, register users router.
- `alembic/versions/` — one new revision after `46007a5a1ad3`.
- `tests/conftest.py` plus new tests under `tests/modules/auth/`, `tests/modules/users/`, `tests/core/`, `tests/scripts/`; two existing test files get new paths.
- Patterns to follow: route/controller/repository split and `get_controller` Depends factory in the current auth module; `AppError` subclasses and the structured error handlers; `create_autospec` repo overrides for pure controller tests; the conftest test-router trick for guard tests.
- Risks: moving to `/api/v1` is a breaking path change (only tests use it today); `extra="forbid"` changes register behavior for unknown fields; `get_controller` moving files must keep `route.get_controller` importable for the existing override; SQLite differs from Postgres, so the migration is verified manually.

## Testing Strategy
- Framework & command: pytest, `uv run pytest` (path `tests/`, mirrors `app/modules`); lint `uv run ruff check .`.
- Confirmed seams: HTTP endpoints via TestClient, `create_token`/`decode_token`, `permissions_for`, the admin script's `main`. No private helpers are tested directly.

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1, EC19 | 5 | after | manual Postgres upgrade with existing rows |
| AC2 | 4, 6 | first | claims, TTL, login response |
| AC3, EC9, EC10 | 6 | first | identical error bodies |
| AC4, EC1-EC8 | 7 (EC3-EC6 also 4) | first | each with WWW-Authenticate |
| AC5 | 8 | first | |
| AC6, EC11 | 9 | first | |
| AC7, EC14, EC15 | 9 | first | |
| AC8, EC12 | 7 | first | both directions |
| AC9, EC13 | 6 | first | extra role field is 422 |
| AC10 | 8 | first | old path 404, suite green |
| AC11, EC17 | 10 | first | |
| AC12, EC18 | 1 | after | Settings without secret raises |
| AC13 | 8, 9 | first | OpenAPI ErrorResponse refs |
| AC14 | 6, 7 | first | log capture via `app_logs` fixture |
| AC15 | 11 | skip | |
| AC16, EC21 | 3 | first | |
| AC17, EC20 | 7 (me field in 8) | first | |
| AC18 | 7 | first | |
| AC19 | 11 | skip | inspect `main.py` |
| EC16 | 6 | first | |

- Must verify, not assume: the Alembic revision on real Postgres with existing rows; that `HTTPBearer(auto_error=False)` returns nothing for a non-bearer scheme or empty token on the pinned FastAPI version; that the installed PyJWT enforces string `sub` and the required-claims option as expected; login timing parity (a test checks the unknown-email path still runs a password verification; real timing is not asserted).
- Open questions: none; every EC has a stated outcome.
- Known baseline failures: not run yet; run `uv run pytest` once before Step 1 to record the baseline.

## Blockers & Resolutions
- No spec blockers.
- Spec was silent on `/users` placement and response shape -> new `users` module and an items/total/limit/offset envelope (user-confirmed); spec updated to match.
- EC13 allowed ignore-or-422 -> chose 422 via `extra="forbid"`.
- No test DB existed -> in-memory SQLite fixture (user-confirmed); Postgres behaviour checked manually.

## Trade-offs & Rationale
- Dependencies, not middleware: middleware cannot see per-route requirements and needs a public-path allowlist.
- PyJWT over hand-rolled HS256: stdlib has no JWT support and rolling crypto is a security risk.
- String-backed role, not a native DB enum: adding roles later needs no migration of an enum type.
- Permissions in code with one lookup function: cheap to edit now, table-ready later.
- DB re-check per request: one indexed primary-key lookup buys instant role changes and deactivation, which stands in for token revocation.
- No rate limiting, refresh tokens or logout: deferred in the spec.
- Sync routes and sync Session: matches the existing code rather than mixing styles.
- Cookie owned by the Next.js server (BFF), not FastAPI: keeps the API stateless and header-based, and avoids CORS-with-credentials and CSRF work here. The API needs no change if the client later moves to cookies or another store.

## Project Rules Applied
- `CLAUDE.md` layers -> route/controller/repository per module; `schema.py` and `utils.py` in every module; guards in `dependencies.py`.
- `CLAUDE.md` security -> validate exp/iss/aud/alg explicitly, default-deny, `extra="forbid"`, `response_model` on every route, no secrets in logs, config only from env, structured errors.
- `CLAUDE.md` DB -> Alembic revision only, no `create_all` in the app; the SQLite `create_all` is test-only.
- `CLAUDE.md` testing -> tests mirror modules, cover auth/authz failures; run tests and report real results; do not commit.
- Deviations: 60-minute TTL instead of "short-lived", rate limiting deferred (both user-approved in the spec).

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | read existing auth module, config, errors, session, conftest, migration, tests |
| grill-me | users-module placement, test DB, list shape, test seams (all answered) |
| ponytail | kept PyJWT as the only new dependency; no permissions tables, no middleware, no extra abstractions |
| security-review | auth surface checked inline against CLAUDE.md security rules (no separate skill run) |
| graphify | skipped: no `graphify-out/` in this repo |

## Implementation Deviations (recorded during /implement)
- Superseded by `docs/features/uuid-primary-keys/`: user ids are UUIDv7, not integers. Where this plan says "parse sub as int" or integer ids, read UUID.
- Post-implementation rename (user request): feature-module files are prefixed with their folder name (`auth/auth_controller.py`, `users/users_route.py`, ...). Bare names elsewhere in this plan (`constants.py`, `dependencies.py`, ...) refer to these prefixed files. Token helpers moved from `core/security.py` to `core/tokens.py`.
- Step 6 pulled forward the `/api/v1` mount and `POST /login` from Step 8, because Step 6's seam is the versioned login endpoint.
- Pagination bounds live in `modules/users/constants.py`, not auth's constants: they belong to the users feature.
- `ensure_admin` lives on `AuthController` (the script is a thin wrapper), and validates the email before lookup so the CLI can't create a near-duplicate.
- The users module keeps its `get_controller` in `route.py` (the auth module's original pattern); only auth needed a `dependencies.py` for the shared guards.
- Ruff: lint run via `uv tool run ruff` (ruff is not a project dependency). `ruff format` was not applied: the repo has no ruff config and the existing code is not formatted to ruff's defaults, so formatting would rewrite unrelated files.

## Ready to Implement
- All spec requirements mapped to steps
- Every step has a Test tag; every AC#/EC# mapped in Testing Strategy
- Affected files identified
- Blockers resolved, edge cases handled
- Trade-offs documented with rationale
- Deviations from spec: none contradicting; additions (users module, list envelope, EC13 as 422) recorded in the spec
