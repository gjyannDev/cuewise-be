# Graph Report - cuewise-be  (2026-10-31)

## Corpus Check
- 148 files · ~118,528 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 1884 nodes · 5081 edges · 123 communities (107 shown, 16 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 879 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5cff0168`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- Feature: Start an Interview (backend)
- get_controller
- errors.py
- exception_handlers.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- JobRole
- Implementation Steps
- Role
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- Settings
- ConsoleFormatter
- QuestionTurn
- users_utils.py
- README.md
- cuewise-be
- Implementation: Start an Interview (backend)
- Feature: Role-Based Access Control (single JWT)
- interviews_evals.py
- test_follow_ups.py
- test_start_llm.py
- interviews_utils.py
- Requirements
- provider.py
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- test_answer_guards.py
- Feature: LLM as the Interviewer (it asks the questions)
- test_openrouter.py
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- test_transcript.py
- Implementation: Follow-up Questions (decide / write split)
- Implementation: Error Handling
- tests/conftest.py
- interviews_model.py
- QuestionCategory
- test_turn_budget.py
- FakeProvider
- interviews_turn.py
- test_interview_report.py
- Bundle
- interviews_report.py
- select_questions
- test_answer_interview.py
- Learnings: LLM Slice 1 (Interviewer Reaction)
- InterviewQuestion
- LLMProvider
- job_description_summary_v2.md
- test_create_interview.py
- Clock
- typing
- test_get_interview.py
- interviews_controller.py
- context.py
- build_usage_report
- interviews_context.py
- InvalidReplyError
- ErrorResponse
- test_list_users.py
- Table
- test_context_controller.py
- InterviewMessage
- ChatMessage
- Implementation Plan: Follow-up Questions (decide / write split)
- test_job_description_summary.py
- parse_interviewer_reply
- Implementation Plan: Role-Based Access Control (single JWT)
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- llm
- Feature: Follow-up Questions (decide / write split)
- Implementation Steps
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- WindowLedger
- analyze_interview
- Stats
- interviewer_v3.md
- LLMResult
- no_llm_env
- auth_header
- test_evals.py
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_fallback_pick.py
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_question_bank.py
- clock
- uuid
- Implementation Plan: Context Management for the Interview LLM Calls
- ._blank_is_unset
- interviews_route.py
- RequestContextMiddleware
- logging.py
- test_llm_settings_default_to_off_with_documented_limits
- ._key_and_model_together
- test_factory.py
- pytest
- test_request_context.py
- main
- Learnings: Follow-up Questions (decide / write split)
- _raise_location
- TurnAction
- _make

## God Nodes (most connected - your core abstractions)
1. `InterviewQuestion` - 67 edges
2. `User` - 50 edges
3. `InterviewsController` - 48 edges
4. `InterviewType` - 45 edges
5. `QuestionCategory` - 44 edges
6. `InterviewSession` - 43 edges
7. `FakeProvider` - 42 edges
8. `InterviewMessage` - 42 edges
9. `JobRole` - 41 edges
10. `Level` - 41 edges

## Surprising Connections (you probably didn't know these)
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `Deviations from Plan` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/task.md → app/core/ai/provider.py
- `Implementation Notes (added during /implement)` --references--> `AppError`  [INFERRED]
  docs/features/error-handling/plan.md → app/core/errors.py
- `Affected Files & Patterns` --references--> `AppError`  [INFERRED]
  docs/features/rbac/plan.md → app/core/errors.py
- `Trade-offs & Rationale` --references--> `NotEnoughQuestionsError`  [INFERRED]
  docs/features/start-interview/plan.md → app/core/errors.py

## Import Cycles
- None detected.

## Communities (123 total, 16 thin omitted)

### Community 0 - "User"
Cohesion: 0.08
Nodes (32): hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session, User (+24 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 2 - "get_controller"
Cohesion: 0.15
Nodes (18): get_bank(), get_clock(), get_controller(), get_llm_provider(), Depends, Request, Session, The question source; tests override it with a fixture bank. (+10 more)

### Community 3 - "errors.py"
Cohesion: 0.14
Nodes (31): AppError, BadRequestError, ConflictError, ErrorBody, InvalidCredentialsError, Any, Exception, Base for expected errors. Controllers raise these instead of HTTPException. (+23 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.21
Nodes (20): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+12 more)

### Community 5 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.22
Nodes (8): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.15
Nodes (12): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards, Git Rules (STRICT) (+4 more)

### Community 7 - "InterviewType"
Cohesion: 0.31
Nodes (17): InterviewType, _bank(), parametrize, _q(), _select(), test_general_question_is_eligible_for_every_role(), test_mixed_even_count_is_an_exact_split(), test_mixed_short_on_one_type_is_rejected_without_rebalancing() (+9 more)

### Community 8 - "users_route.py"
Cohesion: 0.14
Nodes (15): UsersController, Session, UsersRepository, get_controller(), list_users(), Depends, Session, BaseModel (+7 more)

### Community 9 - "JobRole"
Cohesion: 0.16
Nodes (22): JobRole, Level, EvalSetup, load_prompt(), Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt(), render_interviewer_v2_prompt() (+14 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.21
Nodes (19): FollowUpAction, What the decide call may answer (a closed list: anything else is an invalid…, Decision, _load_object(), parse_decision_reply(), The reply as a JSON object: one optional fence around it, nothing else before…, The decide call suggests; the code still applies the follow-up cap and the time…, apply_limits() (+11 more)

### Community 11 - "Role"
Cohesion: 0.12
Nodes (38): ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, get_current_user(), AuthControllerDep (+30 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "Settings"
Cohesion: 0.23
Nodes (10): Settings, BaseSettings, parametrize, test_api_key_never_shows_in_repr(), test_blank_llm_settings_count_as_unset(), test_llm_limits_must_be_positive(), test_llm_settings_refuse_key_without_model_and_model_without_key(), test_llm_settings_with_key_and_model_are_configured() (+2 more)

### Community 15 - "ConsoleFormatter"
Cohesion: 0.24
Nodes (12): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success(), test_console_keeps_free_text_on_one_line() (+4 more)

### Community 16 - "QuestionTurn"
Cohesion: 0.09
Nodes (35): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,… (+27 more)

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional (+8 more)

### Community 28 - "interviews_evals.py"
Cohesion: 0.12
Nodes (31): ContextManager, _add_usage(), CaseResult, Check, check_decision(), DecisionSummary, EvalCase, EvalTurn (+23 more)

### Community 29 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): Checkpoint A: the model suggests, the code enforces (concept 5), answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 31 - "interviews_utils.py"
Cohesion: 0.10
Nodes (30): FollowUpGap, MessageKind, MessageRole, StrEnum, QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, A main question opens a thread; a follow-up digs into the latest answer of that… (+22 more)

### Community 33 - "Requirements"
Cohesion: 0.67
Nodes (3): Functional, Non-Functional, Requirements

### Community 34 - "provider.py"
Cohesion: 0.11
Nodes (24): _int_or_none(), OpenRouterProvider, Any, Random, ReasoningEffort, OpenRouter over plain httpx (OpenAI-compatible chat completions). The only…, LLMBadResponseError, LLMError (+16 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+17 more)

### Community 37 - "test_answer_guards.py"
Cohesion: 0.15
Nodes (12): sqlalchemy_exc, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing() (+4 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.12
Nodes (18): Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional, Goal (+10 more)

### Community 39 - "test_openrouter.py"
Cohesion: 0.15
Nodes (29): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape OpenRouter returns., Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_cached_and_reasoning_tokens_are_none_when_not_reported() (+21 more)

### Community 40 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): Checkpoint C: what a follow-up costs in context (concept 2), decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+28 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.16
Nodes (24): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_item(), _html_list_card(), _html_metric_row() (+16 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.11
Nodes (22): Learning Log (`learnings.md`), Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., failing_commit(), messages(), questions() (+14 more)

### Community 45 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+1 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "Implementation: Error Handling"
Cohesion: 0.17
Nodes (11): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+3 more)

### Community 49 - "tests/conftest.py"
Cohesion: 0.08
Nodes (34): health_check(), lifespan(), FastAPI, contextlib, CurrentUserDep, datetime, fastapi_testclient, jwt (+26 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.12
Nodes (22): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, get_db() (+14 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.32
Nodes (13): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, pick(), parametrize, test_a_one_entry_pool_still_works(), test_every_category_and_level_group_has_a_pool(), test_final_answer_uses_the_closing_pool() (+5 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 53 - "FakeProvider"
Cohesion: 0.12
Nodes (29): FakeProvider, run_case(), Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Goal (+21 more)

### Community 54 - "interviews_turn.py"
Cohesion: 0.15
Nodes (19): Condense a long job description once, so later calls send less. One attempt…, Deadline, _decision_label(), Interviewer, _log_error(), log_llm_call(), log_result(), log_turn_summary() (+11 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.08
Nodes (77): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), main(), Path, Session, UUID, The rotated log first, so the lines stay in time order. (+69 more)

### Community 56 - "Bundle"
Cohesion: 0.13
Nodes (18): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+10 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.18
Nodes (24): analyze_rollup(), _avg(), _cost(), _counts(), _effectiveness(), _efficiency(), _latency_row(), _limit_tone() (+16 more)

### Community 58 - "select_questions"
Cohesion: 0.15
Nodes (13): Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules, Overview, Project Rules Applied (+5 more)

### Community 59 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 60 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 61 - "InterviewQuestion"
Cohesion: 0.15
Nodes (15): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Session, UUID, Abandon the user's active session and save the new one with its questions, all…, Any user's session, by id: for the report script only (the API always goes… (+7 more)

### Community 62 - "LLMProvider"
Cohesion: 0.29
Nodes (5): LLMProvider, Protocol, ReasoningEffort, Build order: "Chat with the interviewer", Slice 1: Answer → reply (no streaming)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 65 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 66 - "typing"
Cohesion: 0.06
Nodes (6): pydantic_settings, _login_error(), test_registered_user_is_a_plain_active_user(), test_unknown_email_wrong_password_and_inactive_user_fail_identically(), test_valid_login_returns_bearer_token_for_the_user(), typing

### Community 67 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 68 - "interviews_controller.py"
Cohesion: 0.15
Nodes (29): NotFoundError, QuestionNotCurrentError, SessionNotInProgressError, SessionStatus, InterviewsController, InterviewSetup, NamedTuple, Random (+21 more)

### Community 71 - "context.py"
Cohesion: 0.22
Nodes (10): BuiltContext, ContextReport, estimate_tokens(), _log(), Any, NamedTuple, Protocol, Context management: the one place that decides what each LLM call sends. The… (+2 more)

### Community 72 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 73 - "interviews_context.py"
Cohesion: 0.12
Nodes (24): StrategyOutput, build_context_manager(), _counts(), FollowUpDecision, FullHistory, InterviewerInputs, JobDescriptionSummary, NamedTuple (+16 more)

### Community 74 - "InvalidReplyError"
Cohesion: 0.21
Nodes (24): InvalidReplyError, Exception, follow_up(), parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected() (+16 more)

### Community 75 - "ErrorResponse"
Cohesion: 0.15
Nodes (14): ErrorResponse, BaseModel, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied (+6 more)

### Community 76 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 77 - "Table"
Cohesion: 0.39
Nodes (9): _call_table(), _dash(), _question_table(), Turn N answers the question at position N and asks position N+1: positions are…, _rollup_table(), _strings(), Table, _tag() (+1 more)

### Community 78 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 79 - "InterviewMessage"
Cohesion: 0.22
Nodes (10): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, Save one whole turn in one commit: advance the session, the answer, the…, interviewer_history(), Answered questions with their answers (and the model's note on each), in…, Affected Files & Patterns, test_database_rejects_a_second_answer_for_one_question(), _question() (+2 more)

### Community 80 - "ChatMessage"
Cohesion: 0.15
Nodes (19): ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go… (+11 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 83 - "parse_interviewer_reply"
Cohesion: 0.15
Nodes (12): InterviewerReply, _normalized(), parse_interviewer_reply(), NamedTuple, Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine) (+4 more)

### Community 84 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.09
Nodes (18): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Trade-offs & Rationale (+10 more)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "llm"
Cohesion: 0.21
Nodes (11): Acceptance Criteria, _decision_json(), llm(), script(), script_decide(), unique_question(), fixture, Builds a reply in the exact shape the decide call must produce. (+3 more)

### Community 87 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 88 - "Implementation Steps"
Cohesion: 0.19
Nodes (14): get_context_manager(), Decides what each LLM call sends; tests swap in one with a tiny limit., The same one-off condensation the app makes at interview start; its tokens…, summarize(), A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary() (+6 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learnings: Context Management"
Cohesion: 0.29
Nodes (6): Checkpoint A: the baseline (before any context change), Checkpoint B: the six-part prompts (after step 3), Checkpoint C: the "before" snapshot (step 8), Checkpoint D: the comparison (step 12) - strategy comparison recorded, ablations open, Checkpoint E: where the cost went (live interview, 2026-10-30), Learnings: Context Management

### Community 92 - "WindowLedger"
Cohesion: 0.31
Nodes (9): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., Task, WindowLedger, test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), test_the_guard_never_drops_the_current_thread() (+1 more)

### Community 93 - "analyze_interview"
Cohesion: 0.18
Nodes (14): analyze_interview(), Checks, bad_parent(), _consistency(), _facts(), Time limits nearly used up, failed or odd calls, overrides, fallbacks, missing…, Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers… (+6 more)

### Community 94 - "Stats"
Cohesion: 0.22
Nodes (8): _answer_growth(), The numbers the sections and tiles share, worked out once over a list of…, How each follow-up thread was closed, read from the turn that answered its last…, Each follow-up answer's length relative to the answer before it (characters…, Stats, decide(), _thread_endings(), Counter

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "LLMResult"
Cohesion: 0.25
Nodes (6): ReasoningEffort, Test double for LLMProvider: scripted replies or errors, records every call.…, LLMResult, collections, test_usage_is_stored_with_the_question_it_produced(), result()

### Community 97 - "no_llm_env"
Cohesion: 0.67
Nodes (3): no_llm_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…

### Community 98 - "auth_header"
Cohesion: 0.22
Nodes (9): auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, answer(), _answer(), POST a setup for `user`; any field can be overridden, or dropped by passing…, POST an answer; `question_id` defaults to whatever the caller passes, body…, start_interview() (+1 more)

### Community 99 - "test_evals.py"
Cohesion: 0.15
Nodes (25): check_reply(), load_cases(), main(), Path, Rule checks for one reply. Text checks look at the parsed question, or at the…, summarize_decisions(), case(), decision() (+17 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "test_fallback_pick.py"
Cohesion: 0.18
Nodes (17): NotEnoughQuestionsError, pick_fallback_question(), One unused bank question for `position`, used when the LLM is off or its reply…, Collection, Deviations from Plan, random, fixture_bank(), pick() (+9 more)

### Community 104 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 105 - "test_question_bank.py"
Cohesion: 0.33
Nodes (9): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, _entry(), parametrize, test_invalid_bank_raises_clear_error(), test_shipped_bank_covers_every_type_role_and_level(), test_valid_bank_loads_typed_entries() (+1 more)

### Community 107 - "uuid"
Cohesion: 0.31
Nodes (7): starlette_types, test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7(), time, uuid

### Community 108 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 110 - "interviews_route.py"
Cohesion: 0.33
Nodes (10): answer_question(), get_interview(), get_transcript(), post, UUID, start_interview(), interviews_answer, interviews_create (+2 more)

### Community 111 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 112 - "logging.py"
Cohesion: 0.22
Nodes (7): RequestIdFilter, setup_logging(), contextvars, Deviations from Plan, logging_config, LogRecord, sys

### Community 113 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.50
Nodes (4): Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 115 - "test_factory.py"
Cohesion: 0.28
Nodes (8): fixture, settings_with(), _settings(), test_fake_records_the_budget_it_was_given(), test_fake_records_the_reasoning_effort(), test_fake_runs_the_on_call_hook_at_call_time(), test_key_and_model_build_the_openrouter_provider(), test_no_key_and_model_means_no_provider_and_one_warning()

### Community 116 - "pytest"
Cohesion: 0.29
Nodes (4): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 117 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 118 - "main"
Cohesion: 0.60
Nodes (4): main(), Session, test_an_empty_database(), test_reports_stored_questions_grouped_by_interview()

### Community 119 - "Learnings: Follow-up Questions (decide / write split)"
Cohesion: 0.40
Nodes (4): Checkpoint B: a small closed decision instead of free text (concept 4), Checkpoint D: labelled evals for a decision (concept 10), Checkpoint E: one deadline for two calls (concept 9), Learnings: Follow-up Questions (decide / write split)

### Community 120 - "_raise_location"
Cohesion: 0.67
Nodes (3): _raise_location(), (path/to/file.py:42 func)' of the innermost frame, i.e. where the error was…, BaseException

### Community 121 - "TurnAction"
Cohesion: 0.67
Nodes (3): StrEnum, What the turn ends with, after the limits: the model can only ask for the first…, TurnAction

## Knowledge Gaps
- **280 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+275 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 673 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `InterviewQuestion` connect `InterviewQuestion` to `Implementation Steps`, `QuestionTurn`, `test_follow_ups.py`, `test_start_llm.py`, `interviews_utils.py`, `test_answer_guards.py`, `test_answer_llm.py`, `test_transcript.py`, `interviews_model.py`, `test_turn_budget.py`, `test_interview_report.py`, `Bundle`, `interviews_report.py`, `test_create_interview.py`, `interviews_controller.py`, `build_usage_report`, `Table`, `test_context_controller.py`, `InterviewMessage`, `analyze_interview`, `Stats`, `LLMResult`, `main`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `test_create_interview.py`, `interviews_controller.py`, `users_route.py`, `Role`, `interviews_route.py`, `tests/conftest.py`, `interviews_model.py`, `Implementation Plan: Role-Based Access Control (single JWT)`, `InterviewQuestion`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `select_questions()` connect `select_questions` to `interviews_controller.py`, `Feature: LLM as the Interviewer (it asks the questions)`, `InterviewType`, `test_fallback_pick.py`, `JobRole`, `Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `test_answer_llm.py`, `QuestionTurn`, `QuestionCategory`, `interviews_utils.py`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `QuestionKind`) actually correct?**
  _`InterviewQuestion` has 25 INFERRED edges - model-reasoned connections that need verification._
- **Are the 22 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `InterviewType` (e.g. with `InterviewerInputs` and `InterviewsController`) actually correct?**
  _`InterviewType` has 29 INFERRED edges - model-reasoned connections that need verification._