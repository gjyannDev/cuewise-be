# Graph Report - cuewise-be  (2026-10-29)

## Corpus Check
- 129 files · ~89,549 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 1435 nodes · 3662 edges · 99 communities (84 shown, 15 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 662 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b8da7d25`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- Feature: Start an Interview (backend)
- Level
- decode_token
- exception_handlers.py
- AppError
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- test_get_interview.py
- test_evals.py
- test_guards.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- Settings
- test_create_interview.py
- test_context_strategies.py
- users_utils.py
- README.md
- cuewise-be
- Implementation: Start an Interview (backend)
- require_permissions
- tests/conftest.py
- Implementation: Error Handling
- test_start_llm.py
- test_factory.py
- interviews_route.py
- provider.py
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- InterviewQuestion
- Feature: LLM as the Interviewer (it asks the questions)
- test_openrouter.py
- LLMResult
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_answer_guards.py
- Implementation Steps
- test_answer_llm.py
- interviews_reply.py
- test_transcript.py
- test_fallback_pick.py
- Affected Files & Patterns
- Role
- interviews_context.py
- QuestionCategory
- ChatMessage
- interviews_evals.py
- interviews_utils.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- test_question_bank.py
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: Start an Interview (backend)
- test_answer_interview.py
- Learnings: LLM Slice 1 (Interviewer Reaction)
- Feature: Role-Based Access Control (single JWT)
- Implementation Plan: UUID primary keys
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_me.py
- Clock
- typing
- InterviewSession
- interviews_controller.py
- OpenRouterProvider
- build_usage_report
- run_case
- test_reply_contract.py
- Feature: Context Management for the Interview LLM Calls
- Implementation: Context Management for the Interview LLM Calls
- test_error_handling.py
- LLMProvider
- main.py
- Implementation Plan: Context Management for the Interview LLM Calls
- RequestContextMiddleware
- test_job_description_summary.py
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- answer
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- llm
- bank
- test_request_context.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- clock
- usage_report.py
- start_interview
- ._key_and_model_together
- _raise_location
- no_llm_env
- .__init__

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
- `Deviations from Plan` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/task.md → app/core/ai/provider.py

## Import Cycles
- None detected.

## Communities (99 total, 15 thin omitted)

### Community 0 - "User"
Cohesion: 0.08
Nodes (29): hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session, User (+21 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.20
Nodes (9): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Goal, Out of Scope, Problem, User Flow (+1 more)

### Community 2 - "Level"
Cohesion: 0.11
Nodes (26): Level, Random, get_bank(), get_clock(), get_controller(), get_llm_provider(), Depends, Request (+18 more)

### Community 3 - "decode_token"
Cohesion: 0.14
Nodes (25): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Testing Strategy, Implementation Steps (+17 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.21
Nodes (20): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+12 more)

### Community 5 - "AppError"
Cohesion: 0.12
Nodes (19): AppError, ErrorResponse, BaseModel, Exception, Base for expected errors. Controllers raise these instead of HTTPException., Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement) (+11 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.15
Nodes (12): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards, Git Rules (STRICT) (+4 more)

### Community 7 - "InterviewType"
Cohesion: 0.25
Nodes (19): InterviewType, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), _bank(), parametrize, _q(), _select(), test_general_question_is_eligible_for_every_role() (+11 more)

### Community 8 - "users_route.py"
Cohesion: 0.13
Nodes (17): get_db(), Session, UsersController, Session, UsersRepository, get_controller(), list_users(), Depends (+9 more)

### Community 9 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 10 - "test_evals.py"
Cohesion: 0.18
Nodes (25): FakeProvider, check_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, test_fake_records_messages_and_returns_scripted_replies(), failed(), long_case(), noted(), parametrize (+17 more)

### Community 11 - "test_guards.py"
Cohesion: 0.12
Nodes (21): CurrentUserDep, fastapi, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid() (+13 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "Settings"
Cohesion: 0.15
Nodes (13): Settings, BaseSettings, field_validator, pydantic, pydantic_settings, parametrize, test_api_key_never_shows_in_repr(), test_blank_llm_settings_count_as_unset() (+5 more)

### Community 15 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 16 - "test_context_strategies.py"
Cohesion: 0.06
Nodes (64): _counts(), InterviewerInputs, NamedTuple, Plain values for one interviewer call; the next question is number len(turns) +…, End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), job_description_block() (+56 more)

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "require_permissions"
Cohesion: 0.08
Nodes (34): ForbiddenError, get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), require_roles() (+26 more)

### Community 28 - "tests/conftest.py"
Cohesion: 0.19
Nodes (19): BadRequestError, ConflictError, ErrorBody, InvalidCredentialsError, TokenExpiredError, TokenMissingError, UnauthorizedError, Implementation Steps (+11 more)

### Community 29 - "Implementation: Error Handling"
Cohesion: 0.13
Nodes (13): RequestIdFilter, Baseline Failures, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.20
Nodes (13): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_every_call_logs_one_line_without_any_content(), test_no_retry_when_too_little_time_is_left() (+5 more)

### Community 31 - "test_factory.py"
Cohesion: 0.24
Nodes (10): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, fixture, settings_with(), _settings(), test_fake_records_the_budget_it_was_given(), test_fake_records_the_reasoning_effort(), test_fake_runs_the_on_call_hook_at_call_time() (+2 more)

### Community 33 - "interviews_route.py"
Cohesion: 0.33
Nodes (10): answer_question(), get_interview(), get_transcript(), post, UUID, start_interview(), interviews_answer, interviews_create (+2 more)

### Community 34 - "provider.py"
Cohesion: 0.14
Nodes (19): _int_or_none(), Any, OpenRouter over plain httpx (OpenAI-compatible chat completions). The only…, LLMBadResponseError, LLMError, LLMRateLimitError, LLMRequestError, LLMServerError (+11 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.10
Nodes (20): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+12 more)

### Community 37 - "InterviewQuestion"
Cohesion: 0.16
Nodes (13): InterviewMessage, InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, A candidate answer or the interviewer's reaction to one question. The questions…, InterviewsRepository, Session, UUID, Abandon the user's active session and save the new one with its questions, all… (+5 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "test_openrouter.py"
Cohesion: 0.15
Nodes (29): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape OpenRouter returns., Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_cached_and_reasoning_tokens_are_none_when_not_reported() (+21 more)

### Community 40 - "LLMResult"
Cohesion: 0.20
Nodes (8): ReasoningEffort, Test double for LLMProvider: scripted replies or errors, records every call.…, LLMResult, BaseModel, collections, collections_abc, test_usage_is_stored_with_the_question_it_produced(), result()

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_answer_guards.py"
Cohesion: 0.14
Nodes (13): message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_a_future_question_is_not_current_either(), test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing() (+5 more)

### Community 43 - "Implementation Steps"
Cohesion: 0.31
Nodes (13): login(), me(), AuthControllerDep, post, register(), LoginIn, MeOut, BaseModel (+5 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.12
Nodes (21): Learning Log (`learnings.md`), Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions(), Answer every question of a started interview; returns the list of answer… (+13 more)

### Community 45 - "interviews_reply.py"
Cohesion: 0.15
Nodes (18): InterviewerReply, InvalidReplyError, _normalized(), parse_interviewer_reply(), BaseModel, Exception, NamedTuple, The contract for what the interviewer LLM must reply, and the check that… (+10 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "test_fallback_pick.py"
Cohesion: 0.15
Nodes (19): NotEnoughQuestionsError, pick_fallback_question(), Random, One unused bank question for `position`, used when the LLM is off or its reply…, Collection, Trade-offs & Rationale, Deviations from Plan, random (+11 more)

### Community 48 - "Affected Files & Patterns"
Cohesion: 0.24
Nodes (10): Completed Steps, Affected Files & Patterns, auth_header(), _header(), client(), make_user(), _make(), fixture (+2 more)

### Community 49 - "Role"
Cohesion: 0.13
Nodes (17): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry() (+9 more)

### Community 50 - "interviews_context.py"
Cohesion: 0.15
Nodes (18): build_context_manager(), FullHistory, JobDescriptionSummary, What the interview LLM calls send: the tasks and strategies registered with the…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, SummaryInputs, load_prompt(), Per-interview constants only, so the text is identical on every call of an… (+10 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.28
Nodes (15): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), A predefined, neutral acknowledgement for the answer just given; never the same…, pick(), parametrize, test_a_one_entry_pool_still_works() (+7 more)

### Community 52 - "ChatMessage"
Cohesion: 0.07
Nodes (52): BuiltContext, ContextManager, ContextReport, ContextTooLargeError, estimate_tokens(), _log(), Any, Exception (+44 more)

### Community 53 - "interviews_evals.py"
Cohesion: 0.15
Nodes (22): Check, EvalCase, EvalTurn, load_cases(), main(), _parser(), _positive(), _print_case() (+14 more)

### Community 54 - "interviews_utils.py"
Cohesion: 0.25
Nodes (15): JobRole, MessageKind, MessageRole, StrEnum, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Transcript item kinds: a question comes from interview_questions, the other two…, SessionStatus (+7 more)

### Community 55 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 56 - "test_question_bank.py"
Cohesion: 0.26
Nodes (11): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, Module Structure & Layer Rules, json, _entry(), parametrize, test_invalid_bank_raises_clear_error() (+3 more)

### Community 57 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.20
Nodes (9): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Goal, Out of Scope, Problem, User Flow (+1 more)

### Community 58 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.25
Nodes (7): Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Overview, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation

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

### Community 63 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.22
Nodes (8): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy

### Community 64 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 65 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 66 - "typing"
Cohesion: 0.09
Nodes (8): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), fastapi_security, sqlalchemy, sqlalchemy_orm, typing

### Community 67 - "InterviewSession"
Cohesion: 0.21
Nodes (10): Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, InterviewSession, Code Principles, DeclarativeBase, Project Rules Applied, Project Rules Applied (+2 more)

### Community 68 - "interviews_controller.py"
Cohesion: 0.19
Nodes (22): NotFoundError, QuestionNotCurrentError, SessionNotInProgressError, InterviewsController, InterviewSetup, _log_llm_call(), _log_result(), NamedTuple (+14 more)

### Community 71 - "OpenRouterProvider"
Cohesion: 0.22
Nodes (5): OpenRouterProvider, Random, ReasoningEffort, BaseTransport, _make()

### Community 72 - "build_usage_report"
Cohesion: 0.40
Nodes (8): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_prints_tokens_per_position_and_interview_totals(), test_the_report_never_contains_question_text()

### Community 73 - "run_case"
Cohesion: 0.33
Nodes (10): _add_usage(), CaseResult, ReasoningEffort, The same one-off condensation the app makes at interview start; its tokens…, run_case(), summarize(), _summarize(), Implementation Steps (+2 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.33
Nodes (16): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+8 more)

### Community 75 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 76 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+5 more)

### Community 77 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 78 - "LLMProvider"
Cohesion: 0.13
Nodes (12): LLMProvider, Protocol, ReasoningEffort, At most two attempts sharing one time budget. Only a reply that came back but…, _sum_known(), Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions (+4 more)

### Community 79 - "main.py"
Cohesion: 0.21
Nodes (9): setup_logging(), health_check(), lifespan(), FastAPI, contextlib, contextvars, logging_config, starlette_types (+1 more)

### Community 80 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 81 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 83 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 84 - "answer"
Cohesion: 0.67
Nodes (3): answer(), _answer(), POST an answer; `question_id` defaults to whatever the caller passes, body…

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "llm"
Cohesion: 0.32
Nodes (8): Acceptance Criteria, llm(), script(), unique_question(), fixture, Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json()

### Community 87 - "bank"
Cohesion: 0.29
Nodes (7): Edge Cases, Functional, Non-Functional, Requirements, Test Results, bank(), Small fixture bank wired into the app instead of the shipped mock file; mutable…

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

### Community 93 - "usage_report.py"
Cohesion: 0.36
Nodes (5): main(), Session, Print stored LLM usage per interview: tokens per question position and per…, test_an_empty_database(), test_reports_stored_questions_grouped_by_interview()

### Community 94 - "start_interview"
Cohesion: 0.67
Nodes (3): POST a setup for `user`; any field can be overridden, or dropped by passing…, start_interview(), _start()

### Community 96 - "_raise_location"
Cohesion: 0.67
Nodes (3): _raise_location(), (path/to/file.py:42 func)' of the innermost frame, i.e. where the error was…, BaseException

### Community 97 - "no_llm_env"
Cohesion: 0.67
Nodes (3): no_llm_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…

## Knowledge Gaps
- **229 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+224 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 542 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `interviews_route.py`, `typing`, `InterviewSession`, `decode_token`, `interviews_controller.py`, `users_route.py`, `Implementation Steps`, `test_create_interview.py`, `Affected Files & Patterns`, `Role`, `require_permissions`, `tests/conftest.py`, `usage_report.py`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `test_evals.py` to `provider.py`, `Level`, `The fundamentals`, `LLMResult`, `run_case`, `Feature: Context Management for the Interview LLM Calls`, `LLMProvider`, `test_context_strategies.py`, `ChatMessage`, `llm`, `test_factory.py`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `InterviewSession`, `interviews_controller.py`, `build_usage_report`, `LLMResult`, `test_answer_guards.py`, `test_answer_llm.py`, `LLMProvider`, `test_create_interview.py`, `test_context_strategies.py`, `test_transcript.py`, `ChatMessage`, `interviews_utils.py`, `usage_report.py`, `test_start_llm.py`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 22 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 16 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `QuestionSource`) actually correct?**
  _`InterviewQuestion` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Are the 33 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `ContextTooLargeError`) actually correct?**
  _`InterviewsController` has 33 INFERRED edges - model-reasoned connections that need verification._
- **Are the 25 inferred relationships involving `InterviewType` (e.g. with `InterviewerInputs` and `InterviewsController`) actually correct?**
  _`InterviewType` has 25 INFERRED edges - model-reasoned connections that need verification._