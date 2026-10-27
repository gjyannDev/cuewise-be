# Implementation: Role-Based Access Control (single JWT)

## Status
Ready for PR (all 11 steps complete; user commits manually)

## Completed Steps
- [x] 1. Config, PyJWT, test fixtures
- [x] 2. (folded into Step 1)
- [x] 3. Constants: Role, Permission, ROLE_PERMISSIONS, permissions_for
- [x] 4. Token helpers (create_token / decode_token)
- [x] 5. Model columns + Alembic migration
- [x] 6. Login, register hardening, token-to-user resolution
- [x] 7. Dependencies: get_current_user, require_roles, require_permissions
- [x] 8. Auth routes (/me) + /api/v1 prefix
- [x] 9. Users module (GET /users)
- [x] 10. Admin bootstrap script
- [x] 11. Wrap-up: lint, full suite, migration check

## Changes Made
Not committed (user commits manually). Suggested message:

    feat(auth): add JWT login and role/permission-based access control

    - POST /api/v1/auth/login issues a signed JWT (sub, role, iat, exp, iss, aud)
    - get_current_user re-loads the user from the DB on every request
    - require_roles / require_permissions route guards; permissions defined in auth/constants.py
    - GET /api/v1/auth/me and admin-only, paginated GET /api/v1/users
    - users.role and users.is_active via Alembic migration 965af3737bf4
    - app.scripts.create_admin bootstraps or promotes an admin
    - routes moved under /api/v1; /health unchanged

## Test Results
100 passed (baseline 25; 75 new). Full suite: `uv run pytest`.
Lint (`uv tool run ruff check app tests`): clean except pre-existing RUF012 in app/core/errors.py.

## Test Cases
| Area | File | Cases | Spec IDs |
|------|------|-------|----------|
| Settings | tests/core/test_config.py | missing secret, short secret, .env.example keys | AC12, EC18 |
| Tokens | tests/core/test_tokens.py | round trip + TTL, expired, tampered, wrong key, alg none, HS512, wrong iss/aud, 5 missing claims, garbage | AC2, EC3-EC7 |
| Permissions | tests/modules/auth/test_permissions.py | admin set, user set, map covers all roles, unknown role empty + logged | AC16, EC21 |
| Login/register | tests/modules/auth/test_login.py | valid login claims, identical failures, dummy-hash verify on miss, 422s, role field rejected, new user is plain user, no secrets in logs | AC2, AC3, AC9, AC14, EC9, EC10, EC13, EC16 |
| Guards | tests/modules/auth/test_guards.py | missing/non-bearer/empty, expired, invalid x4, non-int sub, deleted, deactivated, roles/permissions allow+deny, all-perms rule, demote/promote with old token, forged claim, unmapped role, no token in logs | AC4, AC8, AC14, AC17, AC18, EC1-EC8, EC12, EC20, EC21 |
| /me + versioning | tests/modules/auth/test_me.py | profile + permissions per role, 401, unmapped role 403, old paths 404, OpenAPI errors | AC5, AC10, AC13, AC17 |
| /users | tests/modules/users/test_list_users.py | envelope, 403 for user, 401 anon, defaults/order/total, window, 422 bounds, limit 100, offset past end, OpenAPI | AC6, AC7, AC13, EC11, EC14, EC15 |
| Admin script | tests/scripts/test_create_admin.py | create, promote (hash kept), idempotent, weak password, bad email | AC11, EC17 |

Verified outside pytest:
- AC1, EC19: `alembic upgrade head` on local Postgres with 1 existing user -> role='user', is_active=true, both NOT NULL with server defaults; downgrade/upgrade round trip clean. DB left at 965af3737bf4.
- AC19: app/main.py only adds RequestContextMiddleware; guards are route dependencies.
- AC15: pytest green; ruff check clean for feature files.

## Open Questions
- None blocking. For the user:
  - Local `.env` lacks JWT_SECRET_KEY; the app (and alembic) will refuse to start until it is added.
  - Ruff is not a project dev dependency; add with `uv add --dev ruff` and a `[tool.ruff]` line-length if you want `ruff format` enforced.

## Baseline Failures
- None (25 passed before Step 1)

## Known Issues
- Pre-existing lint: app/core/errors.py RUF012; alembic/env.py and migrations use autogenerate import style (not touched; applied migrations are immutable).
- Inferred cases added beyond the spec (all passing): weak/short JWT secret, every role mapped, missing required claims, HS512 token, forged admin claim, admin script email/password validation.

## Deviations from Plan
- Post-implementation (user request): token helpers split into `core/tokens.py`; every feature-module file renamed with its folder prefix (`auth_*.py`, `users_*.py`). 100 tests still pass; `alembic check` reports no drift.
- See plan.md "Implementation Deviations": /api/v1 + login pulled into Step 6; pagination constants in users module; ensure_admin on AuthController; users get_controller in route.py; ruff format not applied.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| all | fastapi (installed via find-skills: fastapi/fastapi@fastapi) | Annotated dependency aliases, router-level prefix, sync def for blocking DB code |
| 3-10 | tdd / test (loop rules) | red -> green per step at the confirmed seams |
| 6-7 | security review (inline) | alg pinning, required claims, timing parity, default-deny, no secrets in logs |

## Links
- Spec: docs/features/rbac/spec.md
- Plan: docs/features/rbac/plan.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite + build green (100 passed)
- [x] Every spec.md acceptance criterion met by actual code and covered by a passing spec test (or verification noted)
- [x] Open Questions resolved or explicitly surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately
- [x] task.md fully updated
- [ ] Commits documented (user commits manually)
- [x] No open blockers
- [x] Code follows project rules (CLAUDE.md)
- [x] No unresolved plan deviations
