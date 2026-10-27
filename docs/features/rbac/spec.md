# Feature: Role-Based Access Control (single JWT)

## Problem
The API can register users but has no login, no way to identify the caller on later requests, and no way to restrict endpoints by who the caller is. Every route is effectively public, and there is no concept of an administrator.

## Goal
Authenticated users get one JWT from `POST /api/v1/auth/login`; protected routes identify the caller from it and enforce role-based access. Measured by: an admin-only route returns 200 for an admin and 403 for a regular user, and 401 for a missing, expired, tampered or otherwise unusable token.

## Project Conventions
- Rule files consulted: `CLAUDE.md` (project root; there is no `.claude/` directory). No `graphify-out/` exists, so code orientation was done with lean-ctx.
- Constraints those rules impose on this feature:
  - Layers: route -> controller -> repository; every module keeps `schema.py` and `utils.py`; authorization (permission checks) is enforced via `Depends(...)`, not inside routers' bodies.
  - Config only from env via `core/config.py`; `.env.example` must be updated.
  - JWT: validate `exp`, `iss`, `aud`, signature and pin the algorithm explicitly; default-deny.
  - Errors use `core/errors.py` (`TokenMissingError`, `TokenExpiredError`, `TokenInvalidError`, `InvalidCredentialsError`, `ForbiddenError`); generic client messages, details in logs with request ID; never log tokens, passwords or hashes.
  - Schema changes only through a new Alembic migration; applied migrations are not edited.
  - List endpoints are paginated; explicit `status_code`, `response_model`, and `responses=` on every route.
  - New dependencies must be justified (a JWT library is needed; the stdlib has no JWT support).
  - Tests under `tests/modules/auth/` (and `tests/modules/users/`), covering happy path, validation, and auth/authz failures; run `uv run pytest` and `uv run ruff check .`.
  - Do not commit or push.
- Deviations from CLAUDE.md, decided with the user:
  - Token lifetime defaults to 60 min (CLAUDE.md says "short-lived"); there is no refresh token, so users re-login after expiry.
  - Rate limiting on auth endpoints is deferred (see Out of Scope).

## User Flow
1. A user registers via `POST /api/v1/auth/register` (always receives role `user`).
2. They log in via `POST /api/v1/auth/login` with email + password and receive a bearer token.
3. They call protected routes with a bearer token in the `Authorization` header. `GET /api/v1/auth/me` returns their own profile.
4. An admin calls `GET /api/v1/users` and receives a paginated user list; a regular user calling it is refused.
5. The first admin is created by an operator running a CLI script that creates or promotes a user by email.

## Requirements

### Functional
- `User` gains a `role` (string enum: `admin`, `user`; default `user`) and `is_active` (default true), added through a new Alembic migration. Existing rows get `role=user`, `is_active=true`.
- `POST /api/v1/auth/login` accepts email + password and returns `{access_token, token_type: "bearer"}`.
  - Wrong email, wrong password and inactive account all return the same `INVALID_CREDENTIALS` 401 with the same message.
- Token is a signed JWT with claims `sub` (the user's UUID as a string), `role`, `iat`, `exp`, `iss`, `aud`; lifetime from config (default 60 min).
- Decoding validates signature, algorithm (pinned), `exp`, `iss`, `aud`; failures map to `TOKEN_EXPIRED` or `TOKEN_INVALID`.
- A `get_current_user` dependency: reads the bearer token, decodes it, loads the user from the DB on every request, and rejects a missing or inactive user.
- Permissions are defined in code in `app/modules/auth/constants.py`: a `Permission` string enum and a `ROLE_PERMISSIONS` map (role -> set of permissions). This is the single place to edit when permissions change; no DB tables. Initial set:
  - `users:read` (list all users): held by `admin` only.
  - `users:read_self` (read own profile): held by `admin` and `user`.
- A `require_permissions(*perms)` dependency factory built on `get_current_user`; it resolves the user's **DB role** to its permissions (the token's role claim is never used) and allows the request only if the user holds **all** listed permissions, otherwise `ForbiddenError`.
- A `require_roles(*roles)` dependency factory built on `get_current_user`; allows the request only if the user's **DB role** is one of the listed roles, otherwise `ForbiddenError`. Intended for coarse role gates (e.g. an admin area); it never trusts the token's role claim.
- Both guards are FastAPI dependencies attached per route (`Depends(...)`), not middleware: middleware cannot know a route's requirements, and dependencies appear in OpenAPI. Use `require_permissions` for feature access and `require_roles` for coarse role gates; a route may use either or both. Existing `RequestContextMiddleware` is unchanged.
- Role -> permissions resolution goes through one function, `permissions_for(role)`, which is the only code that reads `ROLE_PERMISSIONS`. `require_permissions` and `/auth/me` both call it, so moving permissions into DB tables later changes only that function.
- `GET /api/v1/auth/me` returns the current user (`id`, `email`, `role`, `permissions`); requires `users:read_self`.
- `GET /api/v1/users` requires `users:read` (so effectively admin-only), lives in its own `users` module, and is paginated: `limit` (default 20, max 100), `offset` (default 0), ordered by `id` ascending (UUIDv7, so creation order). The response is an envelope `{items, total, limit, offset}`; each item has `id`, `email`, `role`, `is_active`.
- `RegisterIn` does not accept a `role`; new users are always `user`.
- Existing `POST /auth/register` moves to `/api/v1/auth/register`; existing tests that call `/auth/register` are updated. `/health` stays at the root.
- A CLI script (run with `uv run python -m ...`) creates an admin by email or promotes an existing user to admin, reading the password securely if creating.
- New settings in `core/config.py` and `.env.example`: secret key, algorithm (HS256), token expiry minutes, issuer, audience.

### Non-Functional
- Security: the secret has no usable default (app fails to start if missing); responses never include `password_hash`; token and password values never appear in logs; login does not reveal whether an email exists (same response, comparable timing).
- Every protected route is default-deny: no token -> 401 before any business logic runs.
- Authorization data is always fresh: role or `is_active` changes in the DB take effect on the next request.

## UX Requirements
- Error responses use the existing structured shape (`error.code`, `message`, `request_id`).
- 401 responses include `WWW-Authenticate: Bearer` (already provided by `UnauthorizedError`).
- New routes are documented in OpenAPI with `responses=` for 401/403/422 as applicable.

## Constraints
- Single token only; no refresh token, no revocation list, no logout endpoint.
- Client is a Next.js app that stores the token in an httpOnly cookie it sets itself (Next.js server acts as a backend-for-frontend). FastAPI only returns the token in the login JSON body and reads it from the bearer header; it never sets or reads cookies. Logout is the client clearing its cookie.
- One role per user; permissions are code-defined per role, not stored in the database or editable at runtime.
- Adds one dependency: a JWT library (PyJWT), justified because the stdlib cannot sign/verify JWTs.
- Python >= 3.14, FastAPI, SQLAlchemy, Alembic, `uv` (per `pyproject.toml`).
- Password hashing stays on the existing Argon2 helpers in `core/security.py`.

## Blockers
- None. (Rate limiting and refresh tokens are deferred by decision, not blocked.)

## Edge Cases
Format: condition -> expected outcome.

- **EC1:** Request to a protected route with no `Authorization` header -> 401 `TOKEN_MISSING`.
- **EC2:** `Authorization` header present but not a `Bearer` scheme or with an empty token -> 401 `TOKEN_MISSING`.
- **EC3:** Token past its `exp` -> 401 `TOKEN_EXPIRED`.
- **EC4:** Token with a modified payload or wrong signature -> 401 `TOKEN_INVALID`.
- **EC5:** Token signed with a different algorithm (e.g. `alg: none`) -> 401 `TOKEN_INVALID`.
- **EC6:** Token with wrong `iss` or `aud` -> 401 `TOKEN_INVALID`.
- **EC7:** Valid token whose `sub` is not a UUID (including tokens issued with old integer ids) or refers to a deleted user -> 401 `TOKEN_INVALID`.
- **EC8:** Valid token for a user later set `is_active=false` -> 401 `TOKEN_INVALID`.
- **EC9:** Login with an unknown email -> 401 `INVALID_CREDENTIALS`, same message as a wrong password.
- **EC10:** Login with a correct password for an inactive user -> 401 `INVALID_CREDENTIALS`, same message as a wrong password.
- **EC11:** Regular `user` (lacks `users:read`) calls `GET /api/v1/users` -> 403 `FORBIDDEN`.
- **EC12:** User's DB role changes after the token was issued -> the DB role is used; the stale role claim is ignored (a demoted admin gets 403, a promoted user gets 200, both without re-login).
- **EC13:** Register request body includes `role: "admin"` -> 422 validation error (`extra="forbid"` on `RegisterIn`); the user is never created with a role from the request.
- **EC14:** `GET /api/v1/users?limit=101`, `limit=0`, or a negative `offset` -> 422 validation error.
- **EC15:** `GET /api/v1/users?offset` beyond the number of users -> 200 with an empty list.
- **EC16:** Login request with a malformed email or missing fields -> 422 validation error (existing shape).
- **EC17:** Admin script run for an email that does not exist -> creates the user as `admin`; run for an existing email -> promotes to `admin` without changing the password; running it twice is idempotent.
- **EC18:** App starts with the JWT secret unset -> startup fails with a clear configuration error (no insecure default).
- **EC19:** Migration applied to a database that already contains users -> all existing users become `role=user`, `is_active=true`.
- **EC20:** Route requires several permissions and the user holds only some -> 403 `FORBIDDEN` (all must be held).
- **EC21:** A role value in the DB has no entry in the role->permissions map -> the user holds no permissions: 403 `FORBIDDEN` on every guarded route (default-deny), and the problem is logged.

## Acceptance Criteria
Specific, testable criteria with an observable outcome:

- [ ] **AC1:** `users` has `role` and `is_active` columns via a new Alembic migration; existing rows default to `user` / `true` (EC19).
- [ ] **AC2:** `POST /api/v1/auth/login` with valid credentials returns 200 and a bearer token whose decoded claims include `sub`, `role`, `iat`, `exp`, `iss`, `aud`, with `exp - iat` equal to the configured lifetime.
- [ ] **AC3:** Login failures (unknown email, wrong password, inactive user) return 401 `INVALID_CREDENTIALS` with identical bodies apart from `request_id` (EC9, EC10).
- [ ] **AC4:** Protected routes return 401 with `TOKEN_MISSING`, `TOKEN_EXPIRED` or `TOKEN_INVALID` for EC1-EC8, each with `WWW-Authenticate: Bearer`.
- [ ] **AC5:** `GET /api/v1/auth/me` with a valid token returns 200 with `id`, `email`, `role` and no `password_hash`.
- [ ] **AC6:** `GET /api/v1/users` returns 200 with a paginated list for an admin and 403 `FORBIDDEN` for a `user` (EC11).
- [ ] **AC7:** Pagination honors `limit`/`offset` defaults (20/0), caps at 100, orders by id, returns `total` in the envelope, and rejects out-of-range values with 422 (EC14, EC15).
- [ ] **AC8:** Authorization uses the DB role: changing a user's role in the DB changes access on the next request with the same token (EC12).
- [ ] **AC9:** Registration always yields role `user`; a request body containing `role` is rejected with 422 (EC13).
- [ ] **AC10:** `/api/v1/auth/register` works as before; `/auth/register` no longer exists; `/health` unchanged; all existing tests pass after being updated to the new path.
- [ ] **AC11:** The admin CLI script creates or promotes an admin by email and is idempotent (EC17).
- [ ] **AC12:** The app refuses to start without a JWT secret; `.env.example` lists all new settings (EC18).
- [ ] **AC13:** OpenAPI for login, me, and users documents 401/403/422 responses using the shared `ErrorResponse` model.
- [ ] **AC14:** No log line produced by login or protected-route calls contains the password, the token, or a password hash.
- [ ] **AC15:** `uv run pytest` and `uv run ruff check .` both pass.
- [ ] **AC16:** The role->permissions map is a single code-defined source: `admin` holds `users:read` and `users:read_self`; `user` holds only `users:read_self`. A test asserts this mapping.
- [ ] **AC17:** `require_permissions` returns 403 `FORBIDDEN` when any required permission is missing, and `/auth/me` returns the caller's resolved `permissions` list (EC20, EC21).
- [ ] **AC18:** `require_roles` returns 403 `FORBIDDEN` when the user's DB role is not in the listed roles and lets the request through when it is; it uses the DB role, not the token claim (verified with a test-only route, since no production route needs it yet).
- [ ] **AC19:** Authorization is implemented only as route dependencies (`require_roles`, `require_permissions`); no auth middleware is added.

## Out of Scope
- Refresh tokens, token revocation, logout: decided to keep a single simple token for speed; revisit later.
- Rate limiting on `/auth/login` (CLAUDE.md requires it eventually): deferred to a separate follow-up to keep this feature to RBAC.
- Role-change and user-management endpoints (PATCH role, deactivate, delete): the DB/CLI covers this for now.
- Multiple roles per user, database-stored or runtime-editable permissions, per-resource ownership checks: no feature needs them yet; the code-defined map can move to tables later without changing route guards.
- Email verification, password reset, password-change flows.
- CORS and security-header changes.
- Cookie handling on the API side (Set-Cookie, SameSite, CSRF, CORS with credentials): the Next.js server owns the httpOnly cookie and calls FastAPI server-to-server, so none of that applies to the API. Revisit if the browser ever calls FastAPI directly.
