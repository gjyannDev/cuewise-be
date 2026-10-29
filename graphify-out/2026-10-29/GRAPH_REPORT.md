# Graph Report - cuewise-be  (2026-10-28)

## Corpus Check
- 79 files · ~27,153 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 654 nodes · 1527 edges · 33 communities (22 shown, 11 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 302 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b55cac2b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- Implementation Plan: Role-Based Access Control (single JWT)
- Affected Files & Patterns
- decode_token
- exception_handlers.py
- ErrorResponse
- Cuewise BE — Project Instructions
- test_select_questions.py
- interviews_controller.py
- pytest
- users_route.py
- test_guards.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_error_handling.py
- test_create_interview.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- users_utils.py
- README.md
- cuewise-be
- Implementation: Start an Interview (backend)
- errors.py
- tests/conftest.py
- Implementation: Error Handling
- app_logs
- .__init__

## God Nodes (most connected - your core abstractions)
1. `User` - 45 edges
2. `Role` - 36 edges
3. `AuthController` - 24 edges
4. `require_permissions()` - 24 edges
5. `Implementation Steps` - 24 edges
6. `decode_token()` - 23 edges
7. `Permission` - 21 edges
8. `AppError` - 20 edges
9. `BankQuestion` - 20 edges
10. `select_questions()` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Affected Files & Patterns` --references--> `AppError`  [INFERRED]
  docs/features/rbac/plan.md → app/core/errors.py
- `UX Requirements` --references--> `UnauthorizedError`  [INFERRED]
  docs/features/rbac/spec.md → app/core/errors.py
- `Affected Files & Patterns` --references--> `Base`  [INFERRED]
  docs/features/uuid-primary-keys/plan.md → app/db/session.py
- `1. Constants and permissions` --references--> `Permission`  [INFERRED]
  docs/features/start-interview/task.md → app/modules/auth/auth_constants.py
- `Architecture & Design` --references--> `User`  [INFERRED]
  docs/features/uuid-primary-keys/plan.md → app/modules/auth/auth_model.py

## Import Cycles
- None detected.

## Communities (33 total, 11 thin omitted)

### Community 0 - "User"
Cohesion: 0.06
Nodes (67): hash_password(), verify_password(), Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, AuthController (+59 more)

### Community 1 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.05
Nodes (46): get_current_user(), AuthControllerDep, Depends, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, require_roles(), check(), bearer_scheme, Affected Files & Patterns (+38 more)

### Community 2 - "Affected Files & Patterns"
Cohesion: 0.19
Nodes (12): Completed Steps, Affected Files & Patterns, auth_header(), _header(), client(), db(), make_user(), _make() (+4 more)

### Community 3 - "decode_token"
Cohesion: 0.09
Nodes (35): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Testing Strategy, Affected Files & Patterns (+27 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.07
Nodes (43): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, _raise_location() (+35 more)

### Community 5 - "ErrorResponse"
Cohesion: 0.17
Nodes (12): ErrorResponse, BaseModel, Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+4 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.15
Nodes (12): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards, Git Rules (STRICT) (+4 more)

### Community 7 - "test_select_questions.py"
Cohesion: 0.08
Nodes (63): NotEnoughQuestionsError, InterviewType, JobRole, Level, StrEnum, QuestionCategory, SessionStatus, get_bank() (+55 more)

### Community 8 - "interviews_controller.py"
Cohesion: 0.07
Nodes (37): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), NotFoundError, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+29 more)

### Community 9 - "pytest"
Cohesion: 0.05
Nodes (21): Settings, BaseSettings, pydantic, pydantic_settings, pytest, test_settings_refuse_missing_jwt_secret(), test_settings_refuse_short_jwt_secret(), parametrize (+13 more)

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

### Community 15 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_invalid_setup_is_422_and_creates_nothing() (+9 more)

### Community 16 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.12
Nodes (16): 1. Constants and permissions, Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Start an Interview (backend), Known Issues (+8 more)

### Community 27 - "errors.py"
Cohesion: 0.32
Nodes (13): AppError, BadRequestError, ErrorBody, ForbiddenError, InvalidCredentialsError, Exception, Base for expected errors. Controllers raise these instead of HTTPException., TokenExpiredError (+5 more)

### Community 28 - "tests/conftest.py"
Cohesion: 0.24
Nodes (11): ConflictError, fastapi_testclient, os, sqlalchemy_exc, sqlalchemy_pool, get, raise_conflict(), raise_crash() (+3 more)

### Community 29 - "Implementation: Error Handling"
Cohesion: 0.18
Nodes (10): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+2 more)

### Community 30 - "app_logs"
Cohesion: 0.40
Nodes (5): RequestIdFilter, Deviations from Plan, LogRecord, app_logs(), Capture records from the non-propagating 'app' logger, with request_id like…

## Knowledge Gaps
- **98 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+93 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 261 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `Implementation Plan: Role-Based Access Control (single JWT)`, `Affected Files & Patterns`, `decode_token`, `interviews_controller.py`, `users_route.py`, `test_create_interview.py`, `tests/conftest.py`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Why does `Permission` connect `User` to `Implementation Plan: Role-Based Access Control (single JWT)`, `interviews_controller.py`, `users_route.py`, `test_guards.py`, `Implementation: Start an Interview (backend)`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **Why does `Role` connect `User` to `Implementation Plan: Role-Based Access Control (single JWT)`, `Affected Files & Patterns`, `decode_token`, `exception_handlers.py`, `pytest`, `test_guards.py`, `tests/conftest.py`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Are the 20 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 20 INFERRED edges - model-reasoned connections that need verification._
- **Are the 19 inferred relationships involving `Role` (e.g. with `AuthController` and `require_roles()`) actually correct?**
  _`Role` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `AuthController` (e.g. with `ConflictError` and `InvalidCredentialsError`) actually correct?**
  _`AuthController` has 12 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `require_permissions()` (e.g. with `Permission` and `check()`) actually correct?**
  _`require_permissions()` has 12 INFERRED edges - model-reasoned connections that need verification._