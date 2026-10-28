# Graph Report - cuewise-be  (2026-10-28)

## Corpus Check
- 62 files · ~22,787 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 500 nodes · 1069 edges · 26 communities (17 shown, 9 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 216 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b55cac2b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- require_permissions
- conftest.py
- decode_token
- exception_handlers.py
- AppError
- Implementation Plan: Start an Interview (backend)
- Role
- Implementation Steps
- config.py
- users_route.py
- test_guards.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_error_handling.py
- Implementation Plan: UUID primary keys
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- users_utils.py
- README.md
- cuewise-be

## God Nodes (most connected - your core abstractions)
1. `Role` - 36 edges
2. `User` - 36 edges
3. `AuthController` - 24 edges
4. `Implementation Steps` - 24 edges
5. `decode_token()` - 23 edges
6. `require_permissions()` - 21 edges
7. `AppError` - 20 edges
8. `TokenInvalidError` - 19 edges
9. `permissions_for()` - 18 edges
10. `Permission` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Affected Files & Patterns` --references--> `AppError`  [INFERRED]
  docs/features/rbac/plan.md → app/core/errors.py
- `UX Requirements` --references--> `UnauthorizedError`  [INFERRED]
  docs/features/rbac/spec.md → app/core/errors.py
- `Affected Files & Patterns` --references--> `Base`  [INFERRED]
  docs/features/uuid-primary-keys/plan.md → app/db/session.py
- `Architecture & Design` --references--> `User`  [INFERRED]
  docs/features/uuid-primary-keys/plan.md → app/modules/auth/auth_model.py
- `Known Issues` --references--> `main()`  [INFERRED]
  docs/features/error-handling/task.md → app/scripts/create_admin.py

## Import Cycles
- None detected.

## Communities (26 total, 9 thin omitted)

### Community 0 - "User"
Cohesion: 0.07
Nodes (41): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), ConflictError, hash_password(), verify_password(), Base (+33 more)

### Community 1 - "require_permissions"
Cohesion: 0.05
Nodes (49): ForbiddenError, get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), require_roles() (+41 more)

### Community 2 - "conftest.py"
Cohesion: 0.06
Nodes (38): RequestIdFilter, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions (+30 more)

### Community 3 - "decode_token"
Cohesion: 0.11
Nodes (33): BadRequestError, ErrorBody, InvalidCredentialsError, NotFoundError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError (+25 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.11
Nodes (32): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, _raise_location() (+24 more)

### Community 5 - "AppError"
Cohesion: 0.08
Nodes (25): AppError, ErrorResponse, Any, BaseModel, Exception, Base for expected errors. Controllers raise these instead of HTTPException., Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware (+17 more)

### Community 6 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.07
Nodes (28): Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions (+20 more)

### Community 7 - "Role"
Cohesion: 0.13
Nodes (17): Permission, permissions_for(), The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, StrEnum, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry() (+9 more)

### Community 8 - "Implementation Steps"
Cohesion: 0.14
Nodes (17): UUID, login(), me(), AuthControllerDep, get, register(), LoginIn, MeOut (+9 more)

### Community 9 - "config.py"
Cohesion: 0.10
Nodes (14): Settings, BaseSettings, pydantic, pydantic_settings, pytest, re, test_settings_refuse_missing_jwt_secret(), test_settings_refuse_short_jwt_secret() (+6 more)

### Community 10 - "users_route.py"
Cohesion: 0.13
Nodes (16): UsersController, Session, UsersRepository, get_controller(), list_users(), Depends, get, Session (+8 more)

### Community 11 - "test_guards.py"
Cohesion: 0.13
Nodes (21): CurrentUserDep, admin_role(), _assert_401(), authenticated(), get, parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid() (+13 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 15 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 16 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

## Knowledge Gaps
- **88 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+83 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 216 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `require_permissions`, `conftest.py`, `Implementation Plan: Start an Interview (backend)`, `Role`, `Implementation Steps`, `users_route.py`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Why does `Role` connect `Role` to `User`, `require_permissions`, `conftest.py`, `decode_token`, `Implementation Steps`, `config.py`, `test_guards.py`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Why does `UUIDPrimaryKeyMixin` connect `Implementation Plan: Start an Interview (backend)` to `User`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `Role` (e.g. with `AuthController` and `require_roles()`) actually correct?**
  _`Role` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 16 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `AuthController` (e.g. with `ConflictError` and `InvalidCredentialsError`) actually correct?**
  _`AuthController` has 12 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `Implementation Steps` (e.g. with `InvalidCredentialsError` and `TokenExpiredError`) actually correct?**
  _`Implementation Steps` has 23 INFERRED edges - model-reasoned connections that need verification._