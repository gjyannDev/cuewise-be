# Graph Report - cuewise-be  (2026-10-30)

## Corpus Check
- 131 files · ~90,400 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 1459 nodes · 3710 edges · 91 communities (77 shown, 14 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 664 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `18c770e8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- AuthController
- Feature: Start an Interview (backend)
- get_controller
- errors.py
- exception_handlers.py
- ErrorResponse
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- test_get_interview.py
- ConsoleFormatter
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
- auth_dependencies.py
- app_logs
- Implementation: Error Handling
- test_start_llm.py
- FakeProvider
- User
- provider.py
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- InterviewQuestion
- Feature: LLM as the Interviewer (it asks the questions)
- test_openrouter.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- InterviewMessage
- Implementation Steps
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- test_transcript.py
- test_fallback_pick.py
- tests/conftest.py
- Role
- Level
- interviews_utils.py
- test_context_controller.py
- interviews_evals.py
- ._ask_llm
- admin
- Implementation Plan: Role-Based Access Control (single JWT)
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: Start an Interview (backend)
- test_answer_interview.py
- Learnings: LLM Slice 1 (Interviewer Reaction)
- Feature: Role-Based Access Control (single JWT)
- test_me.py
- job_description_summary_v2.md
- test_list_users.py
- Clock
- interviews_model.py
- main
- interviews_controller.py
- answer
- build_usage_report
- start_interview
- test_reply_contract.py
- Feature: Context Management for the Interview LLM Calls
- .filter
- Slices in detail
- main.py
- Implementation Plan: Context Management for the Interview LLM Calls
- RequestContextMiddleware
- test_job_description_summary.py
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- llm
- bank
- test_request_context.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- clock

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

## Communities (91 total, 14 thin omitted)

### Community 0 - "AuthController"
Cohesion: 0.15
Nodes (11): AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session, Implementation Deviations (recorded during /implement), existing_email(), fixture (+3 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 2 - "get_controller"
Cohesion: 0.19
Nodes (13): get_bank(), get_clock(), get_controller(), get_llm_provider(), Depends, Request, Session, The question source; tests override it with a fixture bank. (+5 more)

### Community 3 - "errors.py"
Cohesion: 0.06
Nodes (56): AppError, BadRequestError, ErrorBody, InvalidCredentialsError, NotFoundError, Any, Exception, Base for expected errors. Controllers raise these instead of HTTPException. (+48 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "ErrorResponse"
Cohesion: 0.24
Nodes (10): ErrorResponse, BaseModel, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Code Principles, Acceptance Criteria, Project Conventions, Module Structure & Layer Rules (+2 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.15
Nodes (12): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards, Git Rules (STRICT) (+4 more)

### Community 7 - "InterviewType"
Cohesion: 0.25
Nodes (19): InterviewType, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), _bank(), parametrize, _q(), _select(), test_general_question_is_eligible_for_every_role() (+11 more)

### Community 8 - "users_route.py"
Cohesion: 0.20
Nodes (9): get_db(), Session, UsersController, Session, UsersRepository, get_controller(), Depends, Session (+1 more)

### Community 9 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 10 - "ConsoleFormatter"
Cohesion: 0.24
Nodes (12): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success(), test_console_keeps_free_text_on_one_line() (+4 more)

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
Cohesion: 0.05
Nodes (41): Settings, BaseSettings, Baseline Failures, Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions (+33 more)

### Community 15 - "test_create_interview.py"
Cohesion: 0.16
Nodes (18): sqlalchemy_exc, parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back() (+10 more)

### Community 16 - "test_context_strategies.py"
Cohesion: 0.06
Nodes (66): _counts(), InterviewerInputs, JobDescriptionSummary, NamedTuple, Plain values for one interviewer call; the next question is number len(turns) +…, SummaryInputs, End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages() (+58 more)

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "auth_dependencies.py"
Cohesion: 0.14
Nodes (25): ForbiddenError, get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), require_roles() (+17 more)

### Community 28 - "app_logs"
Cohesion: 0.50
Nodes (5): RequestIdFilter, Deviations from Plan, Testing Strategy, app_logs(), Capture records from the non-propagating 'app' logger, with request_id like…

### Community 29 - "Implementation: Error Handling"
Cohesion: 0.17
Nodes (11): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+3 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.20
Nodes (13): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_every_call_logs_one_line_without_any_content(), test_no_retry_when_too_little_time_is_left() (+5 more)

### Community 31 - "FakeProvider"
Cohesion: 0.14
Nodes (21): FakeProvider, ReasoningEffort, Test double for LLMProvider: scripted replies or errors, records every call.…, ChatMessage, LLMResult, BaseModel, ReasoningEffort, One turn of the conversation sent to the model. The model keeps no memory:… (+13 more)

### Community 33 - "User"
Cohesion: 0.23
Nodes (11): User, AuthRepository, Session, main(), Session, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting() (+3 more)

### Community 34 - "provider.py"
Cohesion: 0.11
Nodes (24): _int_or_none(), OpenRouterProvider, Any, Random, ReasoningEffort, OpenRouter over plain httpx (OpenAI-compatible chat completions). The only…, LLMBadResponseError, LLMError (+16 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.10
Nodes (20): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+12 more)

### Community 37 - "InterviewQuestion"
Cohesion: 0.16
Nodes (12): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Session, UUID, Abandon the user's active session and save the new one with its questions, all…, Every stored question, grouped by interview in creation order (UUIDv7), for the… (+4 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "test_openrouter.py"
Cohesion: 0.14
Nodes (30): completion(), make_provider(), _make(), parametrize, A chat-completions body in the OpenAI-compatible shape OpenRouter returns., Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries() (+22 more)

### Community 40 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "InterviewMessage"
Cohesion: 0.13
Nodes (17): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409() (+9 more)

### Community 43 - "Implementation Steps"
Cohesion: 0.19
Nodes (18): create_token(), UUID, login(), me(), AuthControllerDep, post, register(), LoginIn (+10 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.16
Nodes (16): messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview(), test_a_double_submit_stores_one_answer_and_makes_one_call(), test_a_legacy_session_uses_its_stored_questions_and_no_llm(), test_a_mixed_bank_only_interview_alternates_behavioral_first(), test_a_new_interview_started_during_the_call_wins() (+8 more)

### Community 45 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "test_fallback_pick.py"
Cohesion: 0.19
Nodes (16): NotEnoughQuestionsError, pick_fallback_question(), One unused bank question for `position`, used when the LLM is off or its reply…, Collection, random, fixture_bank(), pick(), fixture (+8 more)

### Community 48 - "tests/conftest.py"
Cohesion: 0.13
Nodes (20): ConflictError, hash_password(), verify_password(), Completed Steps, Affected Files & Patterns, fastapi, fastapi_testclient, pwdlib (+12 more)

### Community 49 - "Role"
Cohesion: 0.26
Nodes (14): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry() (+6 more)

### Community 50 - "Level"
Cohesion: 0.16
Nodes (22): JobRole, Level, EvalSetup, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), load_bank(), Path (+14 more)

### Community 51 - "interviews_utils.py"
Cohesion: 0.13
Nodes (28): LevelGroup, MessageKind, StrEnum, QuestionCategory, QuestionSource, Reactions are warmer for people early in their career and briefer for…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Transcript item kinds: a question comes from interview_questions, the other two… (+20 more)

### Community 52 - "test_context_controller.py"
Cohesion: 0.07
Nodes (49): BuiltContext, ContextManager, ContextReport, ContextTooLargeError, estimate_tokens(), _log(), Any, Exception (+41 more)

### Community 53 - "interviews_evals.py"
Cohesion: 0.05
Nodes (84): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, LLMProvider, Protocol, build_context_manager(), FullHistory, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, get_context_manager() (+76 more)

### Community 54 - "._ask_llm"
Cohesion: 0.27
Nodes (8): InterviewSetup, _log_llm_call(), _log_result(), NamedTuple, The session fields the interviewer needs, as plain values that survive the end…, Condense a long job description once, so later calls send less. One attempt…, At most two attempts sharing one time budget. Only a reply that came back but…, _sum_known()

### Community 55 - "admin"
Cohesion: 0.25
Nodes (8): Functional, Non-Functional, Requirements, Acceptance Criteria, Edge Cases, Acceptance Criteria, admin(), fixture

### Community 56 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Testing Strategy (+1 more)

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
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 61 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem, Requirements (+2 more)

### Community 62 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 65 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 66 - "interviews_model.py"
Cohesion: 0.08
Nodes (12): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, Create the first admin, or promote an existing user to admin. Usage: uv run…, Print stored LLM usage per interview: tokens per question position and per…, DeclarativeBase (+4 more)

### Community 67 - "main"
Cohesion: 0.60
Nodes (4): main(), Session, test_an_empty_database(), test_reports_stored_questions_grouped_by_interview()

### Community 68 - "interviews_controller.py"
Cohesion: 0.16
Nodes (27): QuestionNotCurrentError, SessionNotInProgressError, MessageRole, SessionStatus, What the interview LLM calls send: the tasks and strategies registered with the…, InterviewsController, Random, UUID (+19 more)

### Community 71 - "answer"
Cohesion: 0.67
Nodes (3): answer(), _answer(), POST an answer; `question_id` defaults to whatever the caller passes, body…

### Community 72 - "build_usage_report"
Cohesion: 0.40
Nodes (8): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_prints_tokens_per_position_and_interview_totals(), test_the_report_never_contains_question_text()

### Community 73 - "start_interview"
Cohesion: 0.67
Nodes (3): POST a setup for `user`; any field can be overridden, or dropped by passing…, start_interview(), _start()

### Community 74 - "test_reply_contract.py"
Cohesion: 0.28
Nodes (18): InvalidReplyError, Exception, parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing() (+10 more)

### Community 75 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 78 - "Slices in detail"
Cohesion: 0.29
Nodes (7): Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice: Context management (added after Slice 2), Slices in detail

### Community 79 - "main.py"
Cohesion: 0.23
Nodes (9): setup_logging(), lifespan(), FastAPI, contextlib, contextvars, logging_config, re, starlette_types (+1 more)

### Community 80 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 81 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.36
Nodes (6): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_without_an_llm_no_summary_is_made()

### Community 83 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "llm"
Cohesion: 0.38
Nodes (7): llm(), script(), unique_question(), fixture, Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json()

### Community 87 - "bank"
Cohesion: 0.25
Nodes (8): Acceptance Criteria, Edge Cases, Functional, Non-Functional, Requirements, Test Results, bank(), Small fixture bank wired into the app instead of the shipped mock file; mutable…

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

## Knowledge Gaps
- **235 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+230 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 548 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `AuthController`, `interviews_model.py`, `errors.py`, `interviews_controller.py`, `ErrorResponse`, `InterviewQuestion`, `users_route.py`, `Implementation Steps`, `test_create_interview.py`, `tests/conftest.py`, `Role`, `auth_dependencies.py`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `FakeProvider` to `provider.py`, `The fundamentals`, `Feature: Context Management for the Interview LLM Calls`, `Slices in detail`, `test_context_strategies.py`, `Level`, `test_context_controller.py`, `interviews_evals.py`, `llm`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Why does `LLMError` connect `provider.py` to `interviews_controller.py`, `Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `interviews_utils.py`, `interviews_evals.py`, `FakeProvider`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 22 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 16 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `QuestionSource`) actually correct?**
  _`InterviewQuestion` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Are the 33 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `ContextTooLargeError`) actually correct?**
  _`InterviewsController` has 33 INFERRED edges - model-reasoned connections that need verification._
- **Are the 25 inferred relationships involving `InterviewType` (e.g. with `InterviewerInputs` and `InterviewsController`) actually correct?**
  _`InterviewType` has 25 INFERRED edges - model-reasoned connections that need verification._