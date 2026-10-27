# Implementation: UUID primary keys

## Status
Ready for PR (all 5 steps complete; user commits manually)

## Completed Steps
- [x] 1. Mixin, model, schemas
- [x] 2. Tokens (`sub` is the UUID string)
- [x] 3. Migration 9d04cd22055a (drop and recreate users)
- [x] 4. Docs and memory
- [x] 5. Wrap-up

## Changes Made
Not committed (user commits manually). Suggested:

    git add app/db/mixins.py app/modules/auth app/modules/users app/core/tokens.py tests
    git commit -m "refactor(db): use UUIDv7 primary keys for users"

    git add alembic/versions/9d04cd22055a_use_uuid_primary_key_for_users.py
    git commit -m "feat(db): recreate users table with uuid primary key"

    git add CLAUDE.md docs
    git commit -m "docs: require UUID primary keys and update RBAC docs"

## Test Results
106 passed (baseline 100; 6 new: 3 UUID-id tests, 3 extra non-UUID `sub` cases). Ruff: clean except pre-existing RUF012 in app/core/errors.py.

## Test Cases
| Check | File | Cases | Status |
|-------|------|-------|--------|
| R1, R4 | tests/modules/auth/test_user_ids.py | register and /me return UUIDv7 ids | pass |
| R5, E3 | tests/modules/auth/test_user_ids.py | /users ids are UUIDv7 in creation order (6 back-to-back inserts) | pass |
| R3 | tests/core/test_tokens.py | round trip keeps the exact UUID string as `sub` | pass |
| E1, E2 | tests/modules/auth/test_guards.py | `sub` of "1", "42", "not-a-uuid", "" -> TOKEN_INVALID with a real user present | pass |
| R1, E4, E5 | manual, Postgres | upgrade: id is UUID, table emptied; downgrade: INTEGER/SERIAL restored, empty; re-upgrade; `alembic check` no drift | pass |
| R1 | manual, Postgres (rolled back) | inserts get UUIDv7, round-trip and order correctly, role/is_active defaults apply | pass |

Updated (assumption was wrong, not the code): 6 existing tests compared JSON `id` (string) to `user.id` (now `UUID`); they now compare to `str(user.id)`.

## Open Questions
- None.

## Baseline Failures
- None (100 passed before Step 1).

## Known Issues
- The migration deleted the 2 users in the local DB (user-approved drop and recreate). Re-create the admin: `uv run python -m app.scripts.create_admin <email>`.
- Every token issued before this change now returns 401 TOKEN_INVALID (intended).
- `create_admin` was not run against Postgres here because it prompts for a password; the rolled-back insert probe covers the same DB path.

## Deviations from Plan
- Steps 1 and 2 overlapped: `/me` resolves the user from the token, so Step 1's tests needed the controller's UUID `sub` parsing. Step 2's token tests were therefore green when written (no red phase); they still guard the behavior.
- Verified up front instead of assuming: `uuid.uuid7()` on Python 3.14.7 is version 7 and monotonic over 10,000 back-to-back calls, both as bytes and as strings.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 1-2 | tdd / test | red -> green at the HTTP and token seams |
| 3 | (manual) | Postgres migration review via `--sql`, round trip, insert probe |

## Links
- Plan: docs/features/uuid-primary-keys/plan.md
- Related: docs/features/rbac/

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite + build green (106 passed)
- [x] Every requirement met by code and covered by a passing test or a recorded manual check
- [x] Open Questions resolved or surfaced
- [x] No skipped, deleted, or loosened tests (6 updated to compare string ids; assertions unchanged in strength)
- [x] task.md fully updated
- [ ] Commits documented (user commits manually)
- [x] No open blockers
- [x] Code follows CLAUDE.md
- [x] No unresolved plan deviations
