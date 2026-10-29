# Graph Report - cuewise-be  (2026-10-29)

## Corpus Check
- 112 files · ~66,001 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 1171 nodes · 2873 edges · 71 communities (58 shown, 13 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 530 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1f364fbe`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- AuthRepository
- Feature: Start an Interview (backend)
- app_logs
- decode_token
- main.py
- Implementation Plan: Error Handling
- Cuewise BE — Project Instructions
- test_select_questions.py
- users_route.py
- test_get_interview.py
- interviews_evals.py
- test_guards.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- Settings
- test_create_interview.py
- test_interviewer_messages.py
- users_utils.py
- README.md
- cuewise-be
- Implementation: Start an Interview (backend)
- auth_dependencies.py
- tests/conftest.py
- Implementation: Error Handling
- test_start_llm.py
- provider.py
- interviews_controller.py
- OpenRouterProvider
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- InterviewQuestion
- Feature: LLM as the Interviewer (it asks the questions)
- test_openrouter.py
- test_create_admin.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_answer_guards.py
- typing
- test_answer_llm.py
- interviews_utils.py
- test_transcript.py
- test_fallback_pick.py
- errors.py
- Role
- Implementation Plan: Role-Based Access Control (single JWT)
- QuestionCategory
- auth_controller.py
- Feature: Role-Based Access Control (single JWT)
- test_list_users.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- pytest
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- UUIDPrimaryKeyMixin
- test_answer_interview.py
- Learnings: LLM Slice 1 (Interviewer Reaction)
- ErrorResponse
- Implementation Plan: UUID primary keys
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_me.py
- Clock
- uuid
- test_login.py
- .__init__

## God Nodes (most connected - your core abstractions)
1. `User` - 50 edges
2. `InterviewsController` - 42 edges
3. `InterviewQuestion` - 41 edges
4. `Role` - 36 edges
5. `QuestionCategory` - 34 edges
6. `InterviewType` - 34 edges
7. `Level` - 31 edges
8. `InterviewSession` - 31 edges
9. `InterviewMessage` - 31 edges
10. `JobRole` - 30 edges

## Surprising Connections (you probably didn't know these)
- `Slice 3: Structured follow-up decisions` --references--> `FakeProvider`  [INFERRED]
  docs/ai-engineering-learning-path.md → app/core/ai/fake.py
- `Trade-offs & Rationale` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/plan.md → app/core/ai/provider.py
- `Deviations from Plan` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/task.md → app/core/ai/provider.py
- `Implementation Notes (added during /implement)` --references--> `AppError`  [INFERRED]
  docs/features/error-handling/plan.md → app/core/errors.py
- `Affected Files & Patterns` --references--> `AppError`  [INFERRED]
  docs/features/rbac/plan.md → app/core/errors.py

## Import Cycles
- None detected.

## Communities (71 total, 13 thin omitted)

### Community 0 - "AuthRepository"
Cohesion: 0.12
Nodes (11): get_controller(), Depends, Session, AuthRepository, Session, UUID, existing_email(), fixture (+3 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 2 - "app_logs"
Cohesion: 0.17
Nodes (14): RequestIdFilter, Completed Steps, Deviations from Plan, Testing Strategy, Affected Files & Patterns, Testing Strategy, LogRecord, app_logs() (+6 more)

### Community 3 - "decode_token"
Cohesion: 0.23
Nodes (20): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Implementation Steps, Testing Strategy (+12 more)

### Community 4 - "main.py"
Cohesion: 0.06
Nodes (42): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+34 more)

### Community 5 - "Implementation Plan: Error Handling"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+1 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_select_questions.py"
Cohesion: 0.28
Nodes (17): NotEnoughQuestionsError, _bank(), parametrize, _q(), _select(), test_general_question_is_eligible_for_every_role(), test_mixed_even_count_is_an_exact_split(), test_mixed_short_on_one_type_is_rejected_without_rebalancing() (+9 more)

### Community 8 - "users_route.py"
Cohesion: 0.05
Nodes (30): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast… (+22 more)

### Community 9 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 10 - "interviews_evals.py"
Cohesion: 0.07
Nodes (54): CaseResult, Check, check_reply(), EvalCase, EvalTurn, load_cases(), main(), BaseModel (+46 more)

### Community 11 - "test_guards.py"
Cohesion: 0.15
Nodes (17): CurrentUserDep, _assert_401(), authenticated(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access(), test_guards_allow_or_forbid_by_db_role() (+9 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "Settings"
Cohesion: 0.07
Nodes (30): Settings, BaseSettings, field_validator, model_validator, pydantic, pydantic_settings, Self, _settings() (+22 more)

### Community 15 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 16 - "test_interviewer_messages.py"
Cohesion: 0.12
Nodes (27): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't… (+19 more)

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "auth_dependencies.py"
Cohesion: 0.16
Nodes (17): get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), require_roles(), check() (+9 more)

### Community 28 - "tests/conftest.py"
Cohesion: 0.17
Nodes (15): fastapi_testclient, os, sqlalchemy_pool, auth_header(), _header(), raise_conflict(), raise_crash(), raise_db_down() (+7 more)

### Community 29 - "Implementation: Error Handling"
Cohesion: 0.18
Nodes (10): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+2 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.20
Nodes (13): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_every_call_logs_one_line_without_any_content(), test_no_retry_when_too_little_time_is_left() (+5 more)

### Community 31 - "provider.py"
Cohesion: 0.13
Nodes (23): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, FakeProvider, Test double for LLMProvider: scripted replies or errors, records every call.…, ChatMessage, LLMProvider, LLMResult, BaseModel (+15 more)

### Community 33 - "interviews_controller.py"
Cohesion: 0.08
Nodes (59): NotFoundError, QuestionNotCurrentError, SessionNotInProgressError, User, MessageKind, MessageRole, Transcript item kinds: a question comes from interview_questions, the other two…, InterviewsController (+51 more)

### Community 34 - "OpenRouterProvider"
Cohesion: 0.11
Nodes (23): _int_or_none(), OpenRouterProvider, Any, Random, OpenRouter over plain httpx (OpenAI-compatible chat completions). The only…, LLMBadResponseError, LLMError, LLMRateLimitError (+15 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.12
Nodes (16): 1. Settings and provider additions, Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: LLM as the Interviewer (it asks the questions), Known Issues (+8 more)

### Community 36 - "The fundamentals"
Cohesion: 0.08
Nodes (24): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+16 more)

### Community 37 - "InterviewQuestion"
Cohesion: 0.13
Nodes (20): Base, SessionStatus, InterviewMessage, InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, A candidate answer or the interviewer's reaction to one question. The questions…, InterviewsRepository (+12 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.07
Nodes (32): Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional, Goal (+24 more)

### Community 39 - "test_openrouter.py"
Cohesion: 0.17
Nodes (25): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape OpenRouter returns., Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_client_errors_are_never_retried() (+17 more)

### Community 40 - "test_create_admin.py"
Cohesion: 0.22
Nodes (11): main(), Session, Create the first admin, or promote an existing user to admin. Usage: uv run…, argparse, getpass, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting() (+3 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_answer_guards.py"
Cohesion: 0.14
Nodes (13): sqlalchemy_exc, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing() (+5 more)

### Community 43 - "typing"
Cohesion: 0.30
Nodes (13): login(), me(), AuthControllerDep, post, register(), LoginIn, MeOut, BaseModel (+5 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.12
Nodes (21): Learning Log (`learnings.md`), Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions(), Answer every question of a started interview; returns the list of answer… (+13 more)

### Community 45 - "interviews_utils.py"
Cohesion: 0.20
Nodes (19): InterviewType, JobRole, Level, StrEnum, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, EvalSetup, pick_reaction() (+11 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "test_fallback_pick.py"
Cohesion: 0.19
Nodes (15): pick_fallback_question(), One unused bank question for `position`, used when the LLM is off or its reply…, Collection, random, fixture_bank(), pick(), fixture, parametrize (+7 more)

### Community 48 - "errors.py"
Cohesion: 0.32
Nodes (14): AppError, BadRequestError, ConflictError, ErrorBody, ForbiddenError, InvalidCredentialsError, Exception, Base for expected errors. Controllers raise these instead of HTTPException. (+6 more)

### Community 49 - "Role"
Cohesion: 0.38
Nodes (10): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry() (+2 more)

### Community 50 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.22
Nodes (8): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Trade-offs & Rationale

### Community 51 - "QuestionCategory"
Cohesion: 0.32
Nodes (13): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, pick(), parametrize, test_a_one_entry_pool_still_works(), test_every_category_and_level_group_has_a_pool(), test_final_answer_uses_the_closing_pool() (+5 more)

### Community 52 - "auth_controller.py"
Cohesion: 0.26
Nodes (6): hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., Implementation Deviations (recorded during /implement), pwdlib

### Community 53 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.22
Nodes (8): Blockers, Constraints, Feature: Role-Based Access Control (single JWT), Goal, Out of Scope, Problem, User Flow, UX Requirements

### Community 54 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 55 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 56 - "pytest"
Cohesion: 0.19
Nodes (14): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, Deviations from Plan, json, pytest, _bank_question(), make_bank_question() (+6 more)

### Community 57 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 58 - "UUIDPrimaryKeyMixin"
Cohesion: 0.15
Nodes (13): Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Project Rules Applied, Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules, Overview (+5 more)

### Community 59 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 60 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 61 - "ErrorResponse"
Cohesion: 0.18
Nodes (13): ErrorResponse, BaseModel, Requirements (no spec.md: requirement and edge-case IDs are defined here), Testing Strategy, Test Cases, Acceptance Criteria, Project Conventions, Acceptance Criteria (+5 more)

### Community 62 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 63 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.22
Nodes (8): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 64 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 65 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 66 - "uuid"
Cohesion: 0.53
Nodes (5): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7(), uuid

### Community 67 - "test_login.py"
Cohesion: 0.25
Nodes (4): _login_error(), test_registered_user_is_a_plain_active_user(), test_unknown_email_wrong_password_and_inactive_user_fail_identically(), test_valid_login_returns_bearer_token_for_the_user()

## Knowledge Gaps
- **188 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+183 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 462 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `interviews_controller.py` to `AuthRepository`, `app_logs`, `decode_token`, `InterviewQuestion`, `users_route.py`, `test_create_admin.py`, `typing`, `test_create_interview.py`, `errors.py`, `Role`, `auth_controller.py`, `UUIDPrimaryKeyMixin`, `auth_dependencies.py`, `tests/conftest.py`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Why does `AI Engineering Learning Path (Cuewise)` connect `The fundamentals` to `provider.py`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `Build order: "Chat with the interviewer"` connect `provider.py` to `The fundamentals`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Are the 22 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `InterviewsController` (e.g. with `LLMError` and `LLMProvider`) actually correct?**
  _`InterviewsController` has 29 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `QuestionSource`) actually correct?**
  _`InterviewQuestion` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 19 inferred relationships involving `Role` (e.g. with `AuthController` and `require_roles()`) actually correct?**
  _`Role` has 19 INFERRED edges - model-reasoned connections that need verification._