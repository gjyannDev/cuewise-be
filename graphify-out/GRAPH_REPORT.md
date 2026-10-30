# Graph Report - cuewise-be  (2026-10-29)

## Corpus Check
- 130 files · ~89,814 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 1442 nodes · 3668 edges · 94 communities (78 shown, 16 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 662 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b8da7d25`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- auth_controller.py
- Feature: Start an Interview (backend)
- app_logs
- decode_token
- exception_handlers.py
- ErrorResponse
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- test_get_interview.py
- test_evals.py
- tests/conftest.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- Settings
- test_create_interview.py
- test_interviewer_messages.py
- users_utils.py
- README.md
- cuewise-be
- Implementation: Start an Interview (backend)
- Implementation Plan: Role-Based Access Control (single JWT)
- errors.py
- Implementation: Error Handling
- test_start_llm.py
- ChatMessage
- test_create_admin.py
- OpenRouterProvider
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- InterviewQuestion
- Feature: LLM as the Interviewer (it asks the questions)
- test_openrouter.py
- LLMResult
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_answer_guards.py
- User
- test_answer_llm.py
- interviews_dependencies.py
- test_transcript.py
- JobRole
- db
- Role
- Level
- interviews_utils.py
- test_context_strategies.py
- interviews_evals.py
- check_reply
- admin
- test_question_bank.py
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- AI Engineering Learning Path (Cuewise)
- test_answer_interview.py
- Learnings: LLM Slice 1 (Interviewer Reaction)
- Feature: Role-Based Access Control (single JWT)
- Implementation Plan: UUID primary keys
- job_description_summary_v2.md
- pytest
- Clock
- interviews_model.py
- Strategy
- interviews_controller.py
- load_cases
- uuid
- test_reply_contract.py
- Feature: Context Management for the Interview LLM Calls
- test_error_handling.py
- Slices in detail
- main.py
- Implementation Steps
- RequestContextMiddleware
- InterviewSession
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- llm
- bank
- test_request_context.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- clock
- _raise_location

## God Nodes (most connected - your core abstractions)
1. `User` - 50 edges
2. `InterviewQuestion` - 50 edges
3. `InterviewsController` - 47 edges
4. `InterviewType` - 41 edges
5. `Level` - 39 edges
6. `FakeProvider` - 38 edges
7. `JobRole` - 38 edges
8. `Role` - 36 edges
9. `ChatMessage` - 35 edges
10. `QuestionCategory` - 35 edges

## Surprising Connections (you probably didn't know these)
- `Slice 3: Structured follow-up decisions` --references--> `FakeProvider`  [INFERRED]
  docs/ai-engineering-learning-path.md → app/core/ai/fake.py
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Constraints` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Project Conventions` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Trade-offs & Rationale` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/plan.md → app/core/ai/provider.py

## Import Cycles
- None detected.

## Communities (94 total, 16 thin omitted)

### Community 0 - "auth_controller.py"
Cohesion: 0.13
Nodes (14): hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session, Implementation Deviations (recorded during /implement) (+6 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 2 - "app_logs"
Cohesion: 0.21
Nodes (12): get_bank(), get_clock(), get_llm_provider(), Request, The question source; tests override it with a fixture bank., Built once at startup (app lifespan); None when no key is configured or the…, Monotonic clock for the per-turn LLM time budget; tests swap in a fake one., Affected Files & Patterns (+4 more)

### Community 3 - "decode_token"
Cohesion: 0.14
Nodes (25): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Testing Strategy, Implementation Steps (+17 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.21
Nodes (20): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+12 more)

### Community 5 - "ErrorResponse"
Cohesion: 0.13
Nodes (16): ErrorResponse, BaseModel, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied (+8 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.25
Nodes (20): NotEnoughQuestionsError, InterviewType, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), _bank(), parametrize, _q(), _select() (+12 more)

### Community 8 - "users_route.py"
Cohesion: 0.14
Nodes (15): UsersController, Session, UsersRepository, get_controller(), list_users(), Depends, Session, BaseModel (+7 more)

### Community 9 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 10 - "test_evals.py"
Cohesion: 0.32
Nodes (18): FakeProvider, run_case(), long_case(), noted(), reply(), test_a_provider_error_fails_the_case_without_crashing(), test_a_window_reply_must_carry_a_note_when_there_is_an_answer(), test_an_unusable_summary_falls_back_to_the_original() (+10 more)

### Community 11 - "tests/conftest.py"
Cohesion: 0.08
Nodes (34): CurrentUserDep, fastapi, fastapi_testclient, os, sqlalchemy_pool, auth_header(), _header(), raise_conflict() (+26 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "Settings"
Cohesion: 0.05
Nodes (40): Settings, BaseSettings, Baseline Failures, Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions (+32 more)

### Community 15 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 16 - "test_interviewer_messages.py"
Cohesion: 0.10
Nodes (34): End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned… (+26 more)

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.12
Nodes (17): get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, require_roles(), check(), bearer_scheme, Affected Files & Patterns, Architecture & Design (+9 more)

### Community 28 - "errors.py"
Cohesion: 0.18
Nodes (19): AppError, BadRequestError, ConflictError, ErrorBody, ForbiddenError, InvalidCredentialsError, NotFoundError, Any (+11 more)

### Community 29 - "Implementation: Error Handling"
Cohesion: 0.18
Nodes (10): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+2 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.20
Nodes (13): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_every_call_logs_one_line_without_any_content(), test_no_retry_when_too_little_time_is_left() (+5 more)

### Community 31 - "ChatMessage"
Cohesion: 0.13
Nodes (24): BuiltContext, ContextReport, estimate_tokens(), _log(), NamedTuple, Context management: the one place that decides what each LLM call sends. The…, build_provider(), The one place that picks the implementation; swapping vendor or model is a… (+16 more)

### Community 33 - "test_create_admin.py"
Cohesion: 0.22
Nodes (11): main(), Session, Create the first admin, or promote an existing user to admin. Usage: uv run…, argparse, getpass, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting() (+3 more)

### Community 34 - "OpenRouterProvider"
Cohesion: 0.10
Nodes (22): _int_or_none(), OpenRouterProvider, Any, Random, ReasoningEffort, OpenRouter over plain httpx (OpenAI-compatible chat completions). The only…, LLMBadResponseError, LLMError (+14 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.17
Nodes (12): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+4 more)

### Community 37 - "InterviewQuestion"
Cohesion: 0.16
Nodes (14): InterviewMessage, InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, A candidate answer or the interviewer's reaction to one question. The questions…, InterviewsRepository, Session, UUID, Abandon the user's active session and save the new one with its questions, all… (+6 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "test_openrouter.py"
Cohesion: 0.15
Nodes (29): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape OpenRouter returns., Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_cached_and_reasoning_tokens_are_none_when_not_reported() (+21 more)

### Community 40 - "LLMResult"
Cohesion: 0.29
Nodes (6): ReasoningEffort, LLMResult, BaseModel, ReasoningEffort, test_usage_is_stored_with_the_question_it_produced(), result()

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_answer_guards.py"
Cohesion: 0.14
Nodes (13): sqlalchemy_exc, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing() (+5 more)

### Community 43 - "User"
Cohesion: 0.18
Nodes (29): Permission, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), User, login(), me(), AuthControllerDep, post (+21 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.06
Nodes (37): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+29 more)

### Community 45 - "interviews_dependencies.py"
Cohesion: 0.22
Nodes (9): LLMProvider, Protocol, get_db(), Session, get_controller(), Depends, Session, Build order: "Chat with the interviewer" (+1 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "JobRole"
Cohesion: 0.18
Nodes (17): JobRole, pick_fallback_question(), Random, One unused bank question for `position`, used when the LLM is off or its reply…, Collection, random, fixture_bank(), pick() (+9 more)

### Community 48 - "db"
Cohesion: 0.22
Nodes (10): Completed Steps, Affected Files & Patterns, client(), db(), make_user(), _make(), fixture, Fresh in-memory SQLite DB per test, wired into the app's get_db dependency. (+2 more)

### Community 49 - "Role"
Cohesion: 0.13
Nodes (17): permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, AuthRepository, Session, UUID, enum (+9 more)

### Community 50 - "Level"
Cohesion: 0.12
Nodes (24): Level, _counts(), InterviewerInputs, What the interview LLM calls send: the tasks and strategies registered with the…, Plain values for one interviewer call; the next question is number len(turns) +…, BankQuestion, One entry of the hand-written question bank file., _unique_ids() (+16 more)

### Community 51 - "interviews_utils.py"
Cohesion: 0.14
Nodes (27): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, InterviewerReply, _normalized(), parse_interviewer_reply(), BaseModel, NamedTuple (+19 more)

### Community 52 - "test_context_strategies.py"
Cohesion: 0.05
Nodes (68): ContextManager, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., StrategyOutput, Task, build_context_manager(), FullHistory (+60 more)

### Community 53 - "interviews_evals.py"
Cohesion: 0.14
Nodes (24): _add_usage(), CaseResult, Check, EvalSetup, EvalTurn, main(), _parser(), _positive() (+16 more)

### Community 54 - "check_reply"
Cohesion: 0.22
Nodes (10): check_reply(), EvalCase, Rule checks for one reply. Text checks look at the parsed question, or at the…, case(), failed(), fixture, parametrize, test_a_good_reply_passes_every_check() (+2 more)

### Community 55 - "admin"
Cohesion: 0.22
Nodes (9): Acceptance Criteria, Functional, Non-Functional, Requirements, Acceptance Criteria, Edge Cases, Acceptance Criteria, admin() (+1 more)

### Community 56 - "test_question_bank.py"
Cohesion: 0.26
Nodes (11): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, Module Structure & Layer Rules, Testing Strategy, _entry(), parametrize, test_invalid_bank_raises_clear_error() (+3 more)

### Community 57 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.20
Nodes (9): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Goal, Out of Scope, Problem, User Flow (+1 more)

### Community 58 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.25
Nodes (7): AI Engineering Learning Path (Cuewise), How to make it stick, Later stages (after the core is solid), Progress, Slices, The core mindset, The foundation this leaves behind

### Community 59 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 60 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 61 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem, Requirements (+2 more)

### Community 62 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "pytest"
Cohesion: 0.11
Nodes (7): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 65 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 66 - "interviews_model.py"
Cohesion: 0.11
Nodes (13): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, QuestionSource (+5 more)

### Community 67 - "Strategy"
Cohesion: 0.40
Nodes (4): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy

### Community 68 - "interviews_controller.py"
Cohesion: 0.13
Nodes (34): QuestionNotCurrentError, SessionNotInProgressError, MessageKind, MessageRole, StrEnum, Transcript item kinds: a question comes from interview_questions, the other two…, SessionStatus, InterviewsController (+26 more)

### Community 71 - "load_cases"
Cohesion: 0.50
Nodes (4): load_cases(), Path, test_shipped_cases_include_long_histories_and_a_long_job_description(), test_shipped_cases_load_and_cover_every_kind()

### Community 72 - "uuid"
Cohesion: 0.23
Nodes (13): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, main(), Session, q(), test_an_empty_database_prints_an_empty_report(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums() (+5 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.28
Nodes (18): InvalidReplyError, Exception, parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing() (+10 more)

### Community 75 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 77 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 78 - "Slices in detail"
Cohesion: 0.33
Nodes (6): Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice: Context management (added after Slice 2), Slices in detail

### Community 79 - "main.py"
Cohesion: 0.18
Nodes (10): setup_logging(), health_check(), lifespan(), FastAPI, contextlib, contextvars, logging_config, pydantic_settings (+2 more)

### Community 80 - "Implementation Steps"
Cohesion: 0.13
Nodes (17): The job-description summary replaces the original on every later call, so it…, A running note is optional model output about the latest answer; it is sent…, validate_note(), validate_summary(), Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Implementation Steps, Overview (+9 more)

### Community 81 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 82 - "InterviewSession"
Cohesion: 0.24
Nodes (10): InterviewSession, test_database_rejects_two_in_progress_sessions_for_one_user(), session_for(), parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts() (+2 more)

### Community 83 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "llm"
Cohesion: 0.18
Nodes (13): Acceptance Criteria, answer(), llm(), script(), unique_question(), fixture, POST a setup for `user`; any field can be overridden, or dropped by passing…, POST an answer; `question_id` defaults to whatever the caller passes, body… (+5 more)

### Community 87 - "bank"
Cohesion: 0.25
Nodes (8): Edge Cases, Functional, Non-Functional, Requirements, Test Results, Deviations from Plan, bank(), Small fixture bank wired into the app instead of the shipped mock file; mutable…

### Community 88 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learnings: Context Management"
Cohesion: 0.33
Nodes (5): Checkpoint A: the baseline (before any context change), Checkpoint B: the six-part prompts (after step 3), Checkpoint C: the "before" snapshot (step 8) - NOT RECORDED YET, Checkpoint D: the comparison (step 12) - NOT RECORDED YET, Learnings: Context Management

### Community 96 - "_raise_location"
Cohesion: 0.67
Nodes (3): _raise_location(), (path/to/file.py:42 func)' of the innermost frame, i.e. where the error was…, BaseException

## Knowledge Gaps
- **235 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+230 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 548 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `auth_controller.py`, `test_create_admin.py`, `interviews_model.py`, `decode_token`, `interviews_controller.py`, `users_route.py`, `tests/conftest.py`, `test_create_interview.py`, `db`, `Role`, `InterviewSession`, `Implementation Plan: Role-Based Access Control (single JWT)`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `test_evals.py` to `OpenRouterProvider`, `LLMResult`, `Feature: Context Management for the Interview LLM Calls`, `interviews_dependencies.py`, `Slices in detail`, `test_interviewer_messages.py`, `Level`, `test_context_strategies.py`, `llm`, `check_reply`, `ChatMessage`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `LLMError` connect `OpenRouterProvider` to `interviews_controller.py`, `Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `test_evals.py`, `test_answer_llm.py`, `interviews_evals.py`, `ChatMessage`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Are the 22 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 16 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `QuestionSource`) actually correct?**
  _`InterviewQuestion` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Are the 33 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `ContextTooLargeError`) actually correct?**
  _`InterviewsController` has 33 INFERRED edges - model-reasoned connections that need verification._
- **Are the 25 inferred relationships involving `InterviewType` (e.g. with `InterviewerInputs` and `InterviewsController`) actually correct?**
  _`InterviewType` has 25 INFERRED edges - model-reasoned connections that need verification._