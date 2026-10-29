# Graph Report - cuewise-be  (2026-10-29)

## Corpus Check
- 100 files · ~48,605 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 979 nodes · 2367 edges · 71 communities (59 shown, 12 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 452 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `65366d59`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- Feature: Start an Interview (backend)
- app_logs
- errors.py
- exception_handlers.py
- Implementation Plan: Error Handling
- Cuewise BE — Project Instructions
- test_select_questions.py
- auth_dependencies.py
- test_get_interview.py
- users_route.py
- test_guards.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- Settings
- test_create_interview.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- users_utils.py
- README.md
- cuewise-be
- Implementation: Start an Interview (backend)
- require_permissions
- tests/conftest.py
- Implementation: Error Handling
- RequestIdFilter
- provider.py
- interviews_controller.py
- OpenRouterProvider
- test_llm_messages.py
- The fundamentals
- InterviewMessage
- interviews_dependencies.py
- test_openrouter.py
- auth_controller.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_answer_guards.py
- Implementation Steps
- test_answer_llm.py
- interviews_utils.py
- test_transcript.py
- main.py
- test_llm_logging.py
- Role
- Implementation Plan: Role-Based Access Control (single JWT)
- interviews_route.py
- ErrorResponse
- Feature: Role-Based Access Control (single JWT)
- test_list_users.py
- RequestContextMiddleware
- test_question_bank.py
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: Start an Interview (backend)
- test_answer_interview.py
- Learnings: LLM Slice 1 (Interviewer Reaction)
- admin
- test_request_context.py
- auth_header
- pytest
- Clock
- test_user_ids.py
- _raise_location
- started

## God Nodes (most connected - your core abstractions)
1. `User` - 50 edges
2. `InterviewsController` - 40 edges
3. `Role` - 36 edges
4. `InterviewMessage` - 29 edges
5. `require_permissions()` - 28 edges
6. `InterviewSession` - 28 edges
7. `OpenRouterProvider` - 26 edges
8. `InterviewQuestion` - 26 edges
9. `ChatMessage` - 24 edges
10. `LLMResult` - 24 edges

## Surprising Connections (you probably didn't know these)
- `Slice 3: Structured follow-up decisions` --references--> `FakeProvider`  [INFERRED]
  docs/ai-engineering-learning-path.md → app/core/ai/fake.py
- `Affected Files & Patterns` --references--> `AppError`  [INFERRED]
  docs/features/rbac/plan.md → app/core/errors.py
- `Trade-offs & Rationale` --references--> `NotEnoughQuestionsError`  [INFERRED]
  docs/features/start-interview/plan.md → app/core/errors.py
- `UX Requirements` --references--> `UnauthorizedError`  [INFERRED]
  docs/features/rbac/spec.md → app/core/errors.py
- `Test Cases` --references--> `ErrorResponse`  [INFERRED]
  docs/features/error-handling/task.md → app/core/errors.py

## Import Cycles
- None detected.

## Communities (71 total, 12 thin omitted)

### Community 0 - "User"
Cohesion: 0.13
Nodes (13): AuthController, get_controller(), Depends, Session, User, AuthRepository, Session, UUID (+5 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 2 - "app_logs"
Cohesion: 0.19
Nodes (13): Completed Steps, Affected Files & Patterns, Testing Strategy, app_logs(), client(), db(), make_user(), _make() (+5 more)

### Community 3 - "errors.py"
Cohesion: 0.07
Nodes (48): AppError, BadRequestError, ConflictError, ErrorBody, InvalidCredentialsError, Any, Exception, Base for expected errors. Controllers raise these instead of HTTPException. (+40 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.20
Nodes (21): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+13 more)

### Community 5 - "Implementation Plan: Error Handling"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Testing Strategy, Trade-offs & Rationale

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_select_questions.py"
Cohesion: 0.21
Nodes (22): NotEnoughQuestionsError, InterviewType, Random, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), itertools, _bank(), parametrize (+14 more)

### Community 8 - "auth_dependencies.py"
Cohesion: 0.11
Nodes (12): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, get_db(), Session, DeclarativeBase (+4 more)

### Community 9 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 10 - "users_route.py"
Cohesion: 0.14
Nodes (15): UsersController, Session, UsersRepository, get_controller(), list_users(), Depends, Session, BaseModel (+7 more)

### Community 11 - "test_guards.py"
Cohesion: 0.18
Nodes (15): _assert_401(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access(), test_guards_allow_or_forbid_by_db_role(), test_missing_header_is_token_missing(), test_non_bearer_or_empty_token_is_token_missing() (+7 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "Settings"
Cohesion: 0.05
Nodes (40): Settings, BaseSettings, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Ready to Implement (+32 more)

### Community 15 - "test_create_interview.py"
Cohesion: 0.15
Nodes (19): parametrize, _question_count(), _questions(), _sessions(), test_database_rejects_two_in_progress_sessions_for_one_user(), session_for(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+11 more)

### Community 16 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "require_permissions"
Cohesion: 0.24
Nodes (14): ForbiddenError, get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), require_roles() (+6 more)

### Community 28 - "tests/conftest.py"
Cohesion: 0.17
Nodes (14): CurrentUserDep, fastapi_testclient, os, sqlalchemy_pool, raise_conflict(), raise_crash(), raise_db_down(), raise_expired() (+6 more)

### Community 29 - "Implementation: Error Handling"
Cohesion: 0.18
Nodes (10): Baseline Failures, Implementation: Error Handling, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit, Test Cases (+2 more)

### Community 30 - "RequestIdFilter"
Cohesion: 0.50
Nodes (3): RequestIdFilter, Deviations from Plan, LogRecord

### Community 31 - "provider.py"
Cohesion: 0.14
Nodes (21): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, FakeProvider, Test double for LLMProvider: scripted replies or errors, records every call.…, ChatMessage, LLMProvider, LLMResult, BaseModel (+13 more)

### Community 33 - "interviews_controller.py"
Cohesion: 0.20
Nodes (19): NotFoundError, QuestionNotCurrentError, SessionNotInProgressError, InterviewsController, _log_llm_call(), Random, UUID, Ask the LLM for a reaction; any failure is a missing reaction, never a failed… (+11 more)

### Community 34 - "OpenRouterProvider"
Cohesion: 0.13
Nodes (19): _int_or_none(), OpenRouterProvider, Any, Random, OpenRouter over plain httpx (OpenAI-compatible chat completions). The only…, LLMBadResponseError, LLMError, LLMRateLimitError (+11 more)

### Community 35 - "test_llm_messages.py"
Cohesion: 0.18
Nodes (23): JobRole, Level, build_llm_messages(), history_turns(), Already-answered questions with their answer and (if saved) reaction, in…, The full input for one call: the model has no memory, so the whole conversation…, One question of the conversation as the model sees it; `reaction` is None when…, Only trusted enum values go in here; candidate text never enters the system… (+15 more)

### Community 36 - "The fundamentals"
Cohesion: 0.08
Nodes (24): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+16 more)

### Community 37 - "InterviewMessage"
Cohesion: 0.19
Nodes (13): SessionStatus, InterviewMessage, InterviewQuestion, InterviewSession, A snapshot of a bank question, so later bank edits never change an existing…, A candidate answer or an interviewer reaction to one question. The questions…, InterviewsRepository, Session (+5 more)

### Community 38 - "interviews_dependencies.py"
Cohesion: 0.14
Nodes (22): get_bank(), get_controller(), get_llm_provider(), Depends, Request, Session, The question source; tests override it with a fixture bank., Built once at startup (app lifespan); None when no key is configured or the… (+14 more)

### Community 39 - "test_openrouter.py"
Cohesion: 0.17
Nodes (22): json, completion(), make_provider(), _make(), parametrize, A chat-completions body in the OpenAI-compatible shape OpenRouter returns., Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_client_errors_are_never_retried() (+14 more)

### Community 40 - "auth_controller.py"
Cohesion: 0.15
Nodes (16): hash_password(), verify_password(), main(), Session, Create the first admin, or promote an existing user to admin. Usage: uv run…, argparse, Implementation Notes (added during /implement), Known Issues (+8 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 1. Wiring and permission, Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_answer_guards.py"
Cohesion: 0.17
Nodes (10): message_count(), parametrize, test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing(), failing_commit(), test_database_rejects_a_second_answer_for_one_question(), test_invalid_input_is_422_and_saves_nothing(), test_missing_and_foreign_sessions_are_the_same_404() (+2 more)

### Community 43 - "Implementation Steps"
Cohesion: 0.31
Nodes (13): login(), me(), AuthControllerDep, post, register(), LoginIn, MeOut, BaseModel (+5 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.19
Nodes (10): fixture, parametrize, rows(), started(), test_database_failure_saving_the_reaction_keeps_the_answer(), test_full_interview_with_llm_stores_the_whole_conversation(), test_llm_failure_still_saves_the_answer_and_moves_on(), test_missing_usage_is_stored_as_null() (+2 more)

### Community 45 - "interviews_utils.py"
Cohesion: 0.32
Nodes (10): MessageKind, MessageRole, StrEnum, QuestionCategory, Transcript item kinds: a question comes from interview_questions, the other two…, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut, build_transcript() (+2 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question(), test_missing_and_foreign_sessions_are_the_same_404() (+3 more)

### Community 47 - "main.py"
Cohesion: 0.19
Nodes (10): setup_logging(), health_check(), lifespan(), FastAPI, contextlib, contextvars, logging_config, starlette_types (+2 more)

### Community 48 - "test_llm_logging.py"
Cohesion: 0.26
Nodes (11): LLMServerError, 5xx or a dropped connection: the provider's side failed., llm_records(), fixture, parametrize, started(), test_failure_line_reports_attempts(), test_failures_are_logged_once_at_the_right_level() (+3 more)

### Community 49 - "Role"
Cohesion: 0.38
Nodes (10): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry() (+2 more)

### Community 50 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (10): Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., Affected Files & Patterns, Blockers & Resolutions, Implementation Deviations (recorded during /implement), Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement (+2 more)

### Community 51 - "interviews_route.py"
Cohesion: 0.29
Nodes (11): answer_question(), get_interview(), get_transcript(), post, UUID, start_interview(), fastapi, interviews_answer (+3 more)

### Community 52 - "ErrorResponse"
Cohesion: 0.22
Nodes (11): ErrorResponse, BaseModel, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Affected Files & Patterns, Requirements (no spec.md: requirement and edge-case IDs are defined here), Project Rules Applied, Project Conventions (+3 more)

### Community 53 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem, Requirements (+2 more)

### Community 54 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 55 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 56 - "test_question_bank.py"
Cohesion: 0.33
Nodes (9): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, Path, _entry(), parametrize, test_invalid_bank_raises_clear_error(), test_shipped_bank_covers_every_type_role_and_level(), test_valid_bank_loads_typed_entries() (+1 more)

### Community 57 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.20
Nodes (9): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Goal, Out of Scope, Problem, User Flow (+1 more)

### Community 58 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Known Follow-ups (story 3: Chat with the interviewer), Overview, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 59 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 60 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.22
Nodes (7): Save the answer and advance the session in one commit, only if it is still at…, Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 61 - "admin"
Cohesion: 0.22
Nodes (9): Acceptance Criteria, Functional, Non-Functional, Requirements, Acceptance Criteria, Edge Cases, Acceptance Criteria, admin() (+1 more)

### Community 62 - "test_request_context.py"
Cohesion: 0.25
Nodes (4): re, parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 63 - "auth_header"
Cohesion: 0.22
Nodes (9): auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, answer(), _answer(), POST a setup for `user`; any field can be overridden, or dropped by passing…, POST an answer; `question_id` defaults to whatever the caller passes, body…, start_interview() (+1 more)

### Community 64 - "pytest"
Cohesion: 0.29
Nodes (4): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 65 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 66 - "test_user_ids.py"
Cohesion: 0.70
Nodes (4): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7()

### Community 67 - "_raise_location"
Cohesion: 0.67
Nodes (3): _raise_location(), (path/to/file.py:42 func)' of the innermost frame, i.e. where the error was…, BaseException

### Community 68 - "started"
Cohesion: 0.67
Nodes (3): fixture, An owner with a started 3-question interview: (owner, session_id, first…, started()

## Knowledge Gaps
- **150 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+145 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 387 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `interviews_controller.py`, `app_logs`, `errors.py`, `InterviewMessage`, `auth_controller.py`, `auth_dependencies.py`, `users_route.py`, `Implementation Steps`, `test_create_interview.py`, `Role`, `interviews_route.py`, `ErrorResponse`, `require_permissions`, `tests/conftest.py`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Why does `UUIDPrimaryKeyMixin` connect `ErrorResponse` to `User`, `interviews_controller.py`, `InterviewMessage`, `Cuewise BE — Project Instructions`, `auth_dependencies.py`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Why does `Implementation Steps` connect `interviews_controller.py` to `OpenRouterProvider`, `test_llm_messages.py`, `app_logs`, `InterviewMessage`, `interviews_dependencies.py`, `test_select_questions.py`, `interviews_utils.py`, `Settings`, `Role`, `provider.py`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Are the 22 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `InterviewsController` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`InterviewsController` has 26 INFERRED edges - model-reasoned connections that need verification._
- **Are the 19 inferred relationships involving `Role` (e.g. with `AuthController` and `require_roles()`) actually correct?**
  _`Role` has 19 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `InterviewMessage` (e.g. with `InterviewsController` and `InterviewsRepository`) actually correct?**
  _`InterviewMessage` has 9 INFERRED edges - model-reasoned connections that need verification._