# Graph Report - cuewise-be  (2026-10-30)

## Corpus Check
- 132 files · ~91,532 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 1470 nodes · 3728 edges · 98 communities (84 shown, 14 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 664 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `052a948e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- Feature: Start an Interview (backend)
- interviews_dependencies.py
- decode_token
- exception_handlers.py
- UUIDPrimaryKeyMixin
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- JobRole
- ConsoleFormatter
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
- Role
- app_logs
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
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_answer_guards.py
- Implementation Steps
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- test_transcript.py
- test_fallback_pick.py
- tests/conftest.py
- test_user_ids.py
- Level
- QuestionCategory
- context.py
- interviews_evals.py
- ._ask_llm
- ErrorResponse
- Implementation Plan: Role-Based Access Control (single JWT)
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: Start an Interview (backend)
- test_answer_interview.py
- Learnings: LLM Slice 1 (Interviewer Reaction)
- Feature: Role-Based Access Control (single JWT)
- test_context.py
- job_description_summary_v2.md
- typing
- Clock
- interviews_model.py
- ContextManager
- interviews_controller.py
- fixture
- build_usage_report
- interviews_utils.py
- pytest
- AppError
- Implementation: Context Management for the Interview LLM Calls
- test_error_handling.py
- test_context_controller.py
- main.py
- Implementation Plan: Context Management for the Interview LLM Calls
- RequestContextMiddleware
- interviews_route.py
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- Implementation Plan: UUID primary keys
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- llm
- bank
- errors.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- clock
- InterviewerInputs
- test_login.py
- interviewer_v3.md
- settings_with
- no_llm_env

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
- `Trade-offs & Rationale` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/plan.md → app/core/ai/provider.py
- `Deviations from Plan` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/task.md → app/core/ai/provider.py
- `Affected Files & Patterns` --references--> `AppError`  [INFERRED]
  docs/features/rbac/plan.md → app/core/errors.py
- `Trade-offs & Rationale` --references--> `NotEnoughQuestionsError`  [INFERRED]
  docs/features/start-interview/plan.md → app/core/errors.py

## Import Cycles
- None detected.

## Communities (98 total, 14 thin omitted)

### Community 0 - "User"
Cohesion: 0.12
Nodes (15): AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session, User, AuthRepository, Session (+7 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 2 - "interviews_dependencies.py"
Cohesion: 0.13
Nodes (22): LLMProvider, Protocol, Random, get_bank(), get_clock(), get_controller(), get_llm_provider(), Depends (+14 more)

### Community 3 - "decode_token"
Cohesion: 0.21
Nodes (21): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Testing Strategy, Implementation Steps (+13 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "UUIDPrimaryKeyMixin"
Cohesion: 0.29
Nodes (7): Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Code Principles, Project Rules Applied, Project Conventions, Project Rules Applied, Project Conventions

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.15
Nodes (12): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards, Git Rules (STRICT) (+4 more)

### Community 7 - "InterviewType"
Cohesion: 0.35
Nodes (16): NotEnoughQuestionsError, InterviewType, _bank(), _q(), _select(), test_general_question_is_eligible_for_every_role(), test_mixed_even_count_is_an_exact_split(), test_mixed_short_on_one_type_is_rejected_without_rebalancing() (+8 more)

### Community 8 - "users_route.py"
Cohesion: 0.19
Nodes (11): get_db(), Session, UsersController, Session, UsersRepository, get_controller(), Depends, Session (+3 more)

### Community 9 - "JobRole"
Cohesion: 0.18
Nodes (19): JobRole, What the interview LLM calls send: the tasks and strategies registered with the…, A running note is optional model output about the latest answer; it is sent…, validate_note(), load_prompt(), Per-interview constants only, so the text is identical on every call of an…, render_interviewer_v2_prompt(), render_summary_prompt() (+11 more)

### Community 10 - "ConsoleFormatter"
Cohesion: 0.20
Nodes (13): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), LogRecord, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success() (+5 more)

### Community 11 - "test_guards.py"
Cohesion: 0.08
Nodes (32): health_check(), list_users(), CurrentUserDep, ge, le, MAX_PAGE_SIZE, Query, raise_crash() (+24 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "Settings"
Cohesion: 0.12
Nodes (16): Settings, BaseSettings, field_validator, model_validator, pydantic, pydantic_settings, Self, parametrize (+8 more)

### Community 15 - "test_create_interview.py"
Cohesion: 0.16
Nodes (18): sqlalchemy_exc, parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back() (+10 more)

### Community 16 - "test_interviewer_messages.py"
Cohesion: 0.09
Nodes (37): _counts(), End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), job_description_block(), neutralize_app_tags(), NamedTuple, QuestionTurn (+29 more)

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "Role"
Cohesion: 0.17
Nodes (25): ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, get_current_user(), AuthControllerDep (+17 more)

### Community 28 - "app_logs"
Cohesion: 0.23
Nodes (12): RequestIdFilter, Affected Files & Patterns, Completed Steps, Deviations from Plan, Affected Files & Patterns, app_logs(), auth_header(), _header() (+4 more)

### Community 29 - "Implementation: Error Handling"
Cohesion: 0.18
Nodes (10): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+2 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 31 - "ChatMessage"
Cohesion: 0.12
Nodes (23): ReasoningEffort, Test double for LLMProvider: scripted replies or errors, records every call.…, ChatMessage, LLMResult, LLMTimeoutError, BaseModel, ReasoningEffort, The LLM contract every feature codes against: message/result types, typed… (+15 more)

### Community 33 - "test_create_admin.py"
Cohesion: 0.44
Nodes (8): main(), Session, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting(), test_new_admin_password_follows_registration_rules(), test_running_twice_is_a_no_op(), test_unknown_email_creates_an_active_admin()

### Community 34 - "OpenRouterProvider"
Cohesion: 0.10
Nodes (22): _int_or_none(), OpenRouterProvider, Any, Random, ReasoningEffort, OpenRouter over plain httpx (OpenAI-compatible chat completions). The only…, LLMBadResponseError, LLMError (+14 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.07
Nodes (27): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+19 more)

### Community 37 - "InterviewQuestion"
Cohesion: 0.15
Nodes (18): SessionStatus, InterviewMessage, InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, A candidate answer or the interviewer's reaction to one question. The questions…, InterviewsRepository, Session (+10 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "test_openrouter.py"
Cohesion: 0.15
Nodes (29): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape OpenRouter returns., Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_cached_and_reasoning_tokens_are_none_when_not_reported() (+21 more)

### Community 40 - "test_context_strategies.py"
Cohesion: 0.26
Nodes (21): full(), inputs(), parametrize, test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window(), max_inputs(), test_fewer_turns_than_the_window_are_all_sent_with_no_ledger(), test_full_history_equals_todays_payload(), test_full_history_is_never_trimmed_however_large() (+13 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_answer_guards.py"
Cohesion: 0.15
Nodes (12): message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing(), test_database_rejects_a_second_answer_for_one_question() (+4 more)

### Community 43 - "Implementation Steps"
Cohesion: 0.31
Nodes (13): login(), me(), AuthControllerDep, post, register(), LoginIn, MeOut, BaseModel (+5 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.08
Nodes (29): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+21 more)

### Community 45 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "test_fallback_pick.py"
Cohesion: 0.18
Nodes (16): pick_fallback_question(), Random, One unused bank question for `position`, used when the LLM is off or its reply…, Collection, random, fixture_bank(), pick(), fixture (+8 more)

### Community 48 - "tests/conftest.py"
Cohesion: 0.18
Nodes (12): ConflictError, hash_password(), verify_password(), fastapi, fastapi_testclient, os, pwdlib, sqlalchemy_pool (+4 more)

### Community 49 - "test_user_ids.py"
Cohesion: 0.70
Nodes (4): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7()

### Community 50 - "Level"
Cohesion: 0.17
Nodes (17): Level, EvalSetup, load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Module Structure & Layer Rules (+9 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.21
Nodes (19): LevelGroup, StrEnum, QuestionCategory, QuestionSource, Reactions are warmer for people early in their career and briefer for…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, pick_reaction(), A predefined, neutral acknowledgement for the answer just given; never the same… (+11 more)

### Community 52 - "context.py"
Cohesion: 0.15
Nodes (15): BuiltContext, ContextReport, ContextTooLargeError, estimate_tokens(), _log(), Any, Exception, NamedTuple (+7 more)

### Community 53 - "interviews_evals.py"
Cohesion: 0.06
Nodes (73): FakeProvider, _add_usage(), CaseResult, Check, check_reply(), EvalCase, EvalTurn, load_cases() (+65 more)

### Community 54 - "._ask_llm"
Cohesion: 0.23
Nodes (9): InterviewSetup, _log_llm_call(), _log_result(), NamedTuple, The session fields the interviewer needs, as plain values that survive the end…, Condense a long job description once, so later calls send less. One attempt…, The next question, and the model's note about the latest answer (None from the…, At most two attempts sharing one time budget. Only a reply that came back but… (+1 more)

### Community 55 - "ErrorResponse"
Cohesion: 0.28
Nodes (9): ErrorResponse, BaseModel, Test Cases, Acceptance Criteria, Acceptance Criteria, Edge Cases, Acceptance Criteria, admin() (+1 more)

### Community 56 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.22
Nodes (8): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Trade-offs & Rationale

### Community 57 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 58 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.22
Nodes (8): Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Overview, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 59 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 60 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 61 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem, Requirements (+2 more)

### Community 62 - "test_context.py"
Cohesion: 0.17
Nodes (16): StrategyOutput, Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default() (+8 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 65 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 66 - "interviews_model.py"
Cohesion: 0.14
Nodes (17): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, Create the first admin, or promote an existing user to admin. Usage: uv run…, main(), Session (+9 more)

### Community 67 - "ContextManager"
Cohesion: 0.20
Nodes (14): ContextManager, Task, build_context_manager(), FullHistory, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WindowLedger, get_context_manager(), Decides what each LLM call sends; tests swap in one with a tiny limit. (+6 more)

### Community 68 - "interviews_controller.py"
Cohesion: 0.25
Nodes (19): NotFoundError, QuestionNotCurrentError, SessionNotInProgressError, MessageRole, InterviewsController, UUID, AnswerIn, AnswerOut (+11 more)

### Community 71 - "fixture"
Cohesion: 0.22
Nodes (9): answer(), _answer(), fixture, POST a setup for `user`; any field can be overridden, or dropped by passing…, POST an answer; `question_id` defaults to whatever the caller passes, body…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), start_interview() (+1 more)

### Community 72 - "build_usage_report"
Cohesion: 0.40
Nodes (8): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_prints_tokens_per_position_and_interview_totals(), test_the_report_never_contains_question_text()

### Community 73 - "interviews_utils.py"
Cohesion: 0.18
Nodes (14): MessageKind, Transcript item kinds: a question comes from interview_questions, the other two…, InterviewerReply, _normalized(), parse_interviewer_reply(), BaseModel, NamedTuple, The contract for what the interviewer LLM must reply, and the check that… (+6 more)

### Community 74 - "pytest"
Cohesion: 0.05
Nodes (33): InvalidReplyError, Exception, pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), fixture, parametrize (+25 more)

### Community 75 - "AppError"
Cohesion: 0.13
Nodes (15): AppError, Any, Exception, Base for expected errors. Controllers raise these instead of HTTPException., Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling (+7 more)

### Community 76 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 77 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 78 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 79 - "main.py"
Cohesion: 0.19
Nodes (11): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, setup_logging(), lifespan(), FastAPI, contextlib, contextvars, logging_config (+3 more)

### Community 80 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 81 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 82 - "interviews_route.py"
Cohesion: 0.33
Nodes (10): answer_question(), get_interview(), get_transcript(), post, UUID, start_interview(), interviews_answer, interviews_create (+2 more)

### Community 83 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 84 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "llm"
Cohesion: 0.50
Nodes (5): Acceptance Criteria, llm(), script(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…

### Community 87 - "bank"
Cohesion: 0.25
Nodes (8): Edge Cases, Functional, Non-Functional, Requirements, Test Results, Deviations from Plan, bank(), Small fixture bank wired into the app instead of the shipped mock file; mutable…

### Community 88 - "errors.py"
Cohesion: 0.50
Nodes (8): BadRequestError, ErrorBody, InvalidCredentialsError, TokenExpiredError, TokenMissingError, UnauthorizedError, Implementation Steps, Project Conventions

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learnings: Context Management"
Cohesion: 0.29
Nodes (6): Checkpoint A: the baseline (before any context change), Checkpoint B: the six-part prompts (after step 3), Checkpoint C: the "before" snapshot (step 8) - NOT RECORDED YET, Checkpoint D: the comparison (step 12) - NOT RECORDED YET, Checkpoint E: where the cost went (live interview, 2026-10-30), Learnings: Context Management

### Community 93 - "InterviewerInputs"
Cohesion: 0.25
Nodes (6): InterviewerInputs, JobDescriptionSummary, NamedTuple, Plain values for one interviewer call; the next question is number len(turns) +…, SummaryInputs, test_the_summary_task_sends_the_job_description_as_data()

### Community 94 - "test_login.py"
Cohesion: 0.25
Nodes (4): _login_error(), test_registered_user_is_a_plain_active_user(), test_unknown_email_wrong_password_and_inactive_user_fail_identically(), test_valid_login_returns_bearer_token_for_the_user()

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "settings_with"
Cohesion: 0.50
Nodes (4): fixture, settings_with(), _settings(), test_no_key_and_model_means_no_provider_and_one_warning()

### Community 97 - "no_llm_env"
Cohesion: 0.67
Nodes (3): no_llm_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…

## Knowledge Gaps
- **242 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+237 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 555 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `test_create_admin.py`, `interviews_model.py`, `decode_token`, `interviews_controller.py`, `UUIDPrimaryKeyMixin`, `InterviewQuestion`, `users_route.py`, `Implementation Steps`, `test_create_interview.py`, `tests/conftest.py`, `interviews_route.py`, `Implementation Plan: UUID primary keys`, `._ask_llm`, `Role`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Why does `select_questions()` connect `Level` to `interviews_dependencies.py`, `interviews_controller.py`, `Feature: LLM as the Interviewer (it asks the questions)`, `InterviewType`, `interviews_utils.py`, `JobRole`, `test_answer_llm.py`, `test_fallback_pick.py`, `test_interviewer_messages.py`, `QuestionCategory`, `._ask_llm`, `Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `Implementation Plan: Start an Interview (backend)`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `interviews_evals.py` to `OpenRouterProvider`, `interviews_dependencies.py`, `The fundamentals`, `ContextManager`, `test_interviewer_messages.py`, `llm`, `ChatMessage`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Are the 22 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 16 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `QuestionSource`) actually correct?**
  _`InterviewQuestion` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Are the 33 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `ContextTooLargeError`) actually correct?**
  _`InterviewsController` has 33 INFERRED edges - model-reasoned connections that need verification._
- **Are the 25 inferred relationships involving `InterviewType` (e.g. with `InterviewerInputs` and `InterviewsController`) actually correct?**
  _`InterviewType` has 25 INFERRED edges - model-reasoned connections that need verification._