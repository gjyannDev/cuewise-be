# Graph Report - cuewise-be  (2026-10-31)

## Corpus Check
- 148 files · ~118,411 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 1883 nodes · 5072 edges · 112 communities (98 shown, 14 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 879 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5cff0168`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- ErrorResponse
- get_controller
- errors.py
- exception_handlers.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- interviews_utils.py
- interviews_reply.py
- Role
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- Settings
- logging.py
- test_interviewer_messages.py
- users_utils.py
- README.md
- cuewise-be
- Implementation: Start an Interview (backend)
- Feature: Role-Based Access Control (single JWT)
- interviews_evals.py
- test_follow_ups.py
- test_start_llm.py
- build_context_manager
- Feature: Context Management for the Interview LLM Calls
- OpenRouterProvider
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- InterviewMessage
- Feature: LLM as the Interviewer (it asks the questions)
- test_openrouter.py
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- main.py
- Implementation: Follow-up Questions (decide / write split)
- tests/conftest.py
- test_guards.py
- interviews_model.py
- QuestionCategory
- test_turn_budget.py
- test_evals.py
- interviews_turn.py
- test_interview_report.py
- Bundle
- interviews_report.py
- select_questions
- test_answer_interview.py
- Learnings: LLM Slice 1 (Interviewer Reaction)
- InterviewSession
- ContextManager
- job_description_summary_v2.md
- test_create_interview.py
- Clock
- typing
- pytest
- interviews_controller.py
- context.py
- build_usage_report
- InterviewerInputs
- InvalidReplyError
- AppError
- test_list_users.py
- analyze_interview
- InterviewQuestion
- QuestionTurn
- test_context.py
- Implementation Plan: Follow-up Questions (decide / write split)
- test_job_description_summary.py
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- Implementation Plan: UUID primary keys
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- llm
- Feature: Follow-up Questions (decide / write split)
- main
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- WindowLedger
- interviews/conftest.py
- Stats
- interviewer_v3.md
- LLMResult
- no_llm_env
- auth_header
- check_decision
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_fallback_pick.py
- test_login.py
- json
- clock
- test_user_ids.py
- Implementation Plan: Context Management for the Interview LLM Calls
- ._blank_is_unset
- test_llm_settings_default_to_off_with_documented_limits
- ._key_and_model_together

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

## Communities (112 total, 14 thin omitted)

### Community 0 - "User"
Cohesion: 0.09
Nodes (28): ConflictError, hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session (+20 more)

### Community 1 - "ErrorResponse"
Cohesion: 0.06
Nodes (34): ErrorResponse, BaseModel, Affected Files & Patterns, Test Cases, Acceptance Criteria, Blockers, Constraints, Edge Cases (+26 more)

### Community 2 - "get_controller"
Cohesion: 0.24
Nodes (10): get_bank(), get_controller(), get_llm_provider(), Depends, Request, Session, The question source; tests override it with a fixture bank., Built once at startup (app lifespan); None when no key is configured or the… (+2 more)

### Community 3 - "errors.py"
Cohesion: 0.16
Nodes (30): BadRequestError, ErrorBody, InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token() (+22 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.31
Nodes (17): InterviewType, _bank(), parametrize, _q(), _select(), test_general_question_is_eligible_for_every_role(), test_mixed_even_count_is_an_exact_split(), test_mixed_short_on_one_type_is_rejected_without_rebalancing() (+9 more)

### Community 8 - "users_route.py"
Cohesion: 0.15
Nodes (15): UsersController, Session, UsersRepository, get_controller(), list_users(), Depends, Session, BaseModel (+7 more)

### Community 9 - "interviews_utils.py"
Cohesion: 0.12
Nodes (31): JobRole, Level, What the interview LLM calls send: the tasks and strategies registered with the…, EvalSetup, load_prompt(), Random, Only trusted values go in here; the job description and answers never enter the…, Per-interview constants only, so the text is identical on every call of an… (+23 more)

### Community 10 - "interviews_reply.py"
Cohesion: 0.12
Nodes (34): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Decision, InterviewerReply, _load_object(), _normalized() (+26 more)

### Community 11 - "Role"
Cohesion: 0.12
Nodes (37): ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, get_current_user(), AuthControllerDep (+29 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "Settings"
Cohesion: 0.23
Nodes (10): Settings, BaseSettings, parametrize, test_api_key_never_shows_in_repr(), test_blank_llm_settings_count_as_unset(), test_llm_limits_must_be_positive(), test_llm_settings_refuse_key_without_model_and_model_without_key(), test_llm_settings_with_key_and_model_are_configured() (+2 more)

### Community 15 - "logging.py"
Cohesion: 0.14
Nodes (19): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, setup_logging(), split_fields(), contextvars, logging_config, re (+11 more)

### Community 16 - "test_interviewer_messages.py"
Cohesion: 0.18
Nodes (15): job_description_block(), Fill {{name}} placeholders in one pass: inserted values are never scanned…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't…, render_template(), prompt(), parametrize, test_a_closing_tag_inside_the_job_description_is_neutralised(), test_job_description_goes_inside_a_delimited_block() (+7 more)

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem, Requirements (+2 more)

### Community 28 - "interviews_evals.py"
Cohesion: 0.14
Nodes (23): DecisionSummary, EvalTurn, Expect, _parser(), _positive(), _print_decisions(), _print_summary(), BaseModel (+15 more)

### Community 29 - "test_follow_ups.py"
Cohesion: 0.17
Nodes (21): Checkpoint A: the model suggests, the code enforces (concept 5), Checkpoint B: a small closed decision instead of free text (concept 4), Checkpoint D: labelled evals for a decision (concept 10), Checkpoint E: one deadline for two calls (concept 9), Learnings: Follow-up Questions (decide / write split), answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the… (+13 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 31 - "build_context_manager"
Cohesion: 0.29
Nodes (5): build_context_manager(), JobDescriptionSummary, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, SummaryInputs, Condense a long job description once, so later calls send less. One attempt…

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "OpenRouterProvider"
Cohesion: 0.13
Nodes (12): _int_or_none(), OpenRouterProvider, Any, Random, ReasoningEffort, LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., BaseTransport (+4 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+17 more)

### Community 37 - "InterviewMessage"
Cohesion: 0.11
Nodes (20): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, Save one whole turn in one commit: advance the session, the answer, the…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started() (+12 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "test_openrouter.py"
Cohesion: 0.15
Nodes (31): LLMServerError, 5xx or a dropped connection: the provider's side failed., completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape OpenRouter returns., Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget() (+23 more)

### Community 40 - "test_context_strategies.py"
Cohesion: 0.20
Nodes (33): decide(), fu(), full(), inputs(), Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window(), max_inputs() (+25 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.15
Nodes (29): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+21 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.12
Nodes (20): Learning Log (`learnings.md`), Known Follow-ups (story 3: Chat with the interviewer), db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview() (+12 more)

### Community 45 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+1 more)

### Community 46 - "main.py"
Cohesion: 0.20
Nodes (14): lifespan(), FastAPI, contextlib, fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left() (+6 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "tests/conftest.py"
Cohesion: 0.07
Nodes (33): RequestIdFilter, health_check(), Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links (+25 more)

### Community 49 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.13
Nodes (19): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, get_db() (+11 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.28
Nodes (15): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), A predefined, neutral acknowledgement for the answer just given; never the same…, pick(), parametrize, test_a_one_entry_pool_still_works() (+7 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 53 - "test_evals.py"
Cohesion: 0.30
Nodes (19): FakeProvider, run_case(), long_case(), noted(), reply(), test_a_provider_error_fails_the_case_without_crashing(), test_a_v3_window_reply_must_carry_a_note_when_there_is_an_answer(), test_an_unusable_summary_falls_back_to_the_original() (+11 more)

### Community 54 - "interviews_turn.py"
Cohesion: 0.18
Nodes (17): Deadline, _decision_label(), Interviewer, _log_error(), log_llm_call(), log_result(), log_turn_summary(), NamedTuple (+9 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.08
Nodes (76): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), main(), Path, Session, UUID, The rotated log first, so the lines stay in time order. (+68 more)

### Community 56 - "Bundle"
Cohesion: 0.14
Nodes (17): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+9 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.21
Nodes (22): analyze_rollup(), _avg(), _cost(), _counts(), _effectiveness(), _efficiency(), _latency_row(), _limit_tone() (+14 more)

### Community 58 - "select_questions"
Cohesion: 0.14
Nodes (14): Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Implementation Steps, Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules, Overview (+6 more)

### Community 59 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 60 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 61 - "InterviewSession"
Cohesion: 0.15
Nodes (10): InterviewSession, InterviewsRepository, Session, UUID, Abandon the user's active session and save the new one with its questions, all…, Any user's session, by id: for the report script only (the API always goes…, Every stored question, grouped by interview in creation order (UUIDv7), for the…, test_database_rejects_two_in_progress_sessions_for_one_user() (+2 more)

### Community 62 - "ContextManager"
Cohesion: 0.16
Nodes (17): ContextManager, LLMProvider, Protocol, _add_usage(), CaseResult, EvalCase, _print_case(), ReasoningEffort (+9 more)

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
Cohesion: 0.08
Nodes (13): login(), me(), AuthControllerDep, post, register(), LoginIn, MeOut, BaseModel (+5 more)

### Community 67 - "pytest"
Cohesion: 0.07
Nodes (12): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started() (+4 more)

### Community 68 - "interviews_controller.py"
Cohesion: 0.13
Nodes (38): NotFoundError, QuestionNotCurrentError, SessionNotInProgressError, MessageKind, MessageRole, StrEnum, QuestionKind, QuestionSource (+30 more)

### Community 71 - "context.py"
Cohesion: 0.15
Nodes (14): BuiltContext, ContextReport, ContextTooLargeError, estimate_tokens(), _log(), Any, Exception, NamedTuple (+6 more)

### Community 72 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 73 - "InterviewerInputs"
Cohesion: 0.14
Nodes (17): StrategyOutput, _counts(), FollowUpDecision, FullHistory, InterviewerInputs, NamedTuple, The decide call: the current thread in full (it judges the latest answer within…, App data at the end of the last user message; untrusted parts (questions,… (+9 more)

### Community 74 - "InvalidReplyError"
Cohesion: 0.21
Nodes (24): InvalidReplyError, Exception, follow_up(), parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected() (+16 more)

### Community 75 - "AppError"
Cohesion: 0.06
Nodes (29): AppError, Any, Exception, Base for expected errors. Controllers raise these instead of HTTPException., Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design (+21 more)

### Community 76 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 77 - "analyze_interview"
Cohesion: 0.13
Nodes (20): analyze_interview(), _call_table(), Checks, bad_parent(), _consistency(), _dash(), _facts(), _question_table() (+12 more)

### Community 78 - "InterviewQuestion"
Cohesion: 0.14
Nodes (21): get_context_manager(), Decides what each LLM call sends; tests swap in one with a tiny limit., InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, main(), Session, candidate_messages(), noted() (+13 more)

### Community 79 - "QuestionTurn"
Cohesion: 0.16
Nodes (18): End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Answered questions with their answers (and the model's note on each), in…, The full input for one call (the model has no memory, so the whole interview is… (+10 more)

### Community 80 - "test_context.py"
Cohesion: 0.17
Nodes (15): Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default(), test_a_second_task_with_its_own_strategy_leaves_the_first_alone() (+7 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.12
Nodes (15): apply_limits(), StrEnum, What the turn ends with, after the limits: the model can only ask for the first…, The code's say over the model's: returns the action and why it overrode the…, TurnAction, Architecture & Design, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split) (+7 more)

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

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
Cohesion: 0.16
Nodes (13): Acceptance Criteria, Acceptance Criteria, Edge Cases, Functional, Non-Functional, Requirements, Test Results, bank() (+5 more)

### Community 87 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 88 - "main"
Cohesion: 0.18
Nodes (11): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, load_cases(), main(), Path, summarize_decisions(), test_at_least_ten_shipped_cases_are_labelled_with_both_injections(), test_main_with_task_decide_runs_only_labelled_cases() (+3 more)

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
Cohesion: 0.33
Nodes (9): Task, WindowLedger, Checkpoint C: what a follow-up costs in context (concept 2), Affected Files & Patterns, test_a_maximum_interview_with_maximum_follow_ups_fits_in_both_tasks(), test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), test_the_guard_never_drops_the_current_thread() (+1 more)

### Community 93 - "interviews/conftest.py"
Cohesion: 0.28
Nodes (7): Random, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), Deviations from Plan, _bank_question(), make_bank_question()

### Community 94 - "Stats"
Cohesion: 0.22
Nodes (8): _answer_growth(), The numbers the sections and tiles share, worked out once over a list of…, How each follow-up thread was closed, read from the turn that answered its last…, Each follow-up answer's length relative to the answer before it (characters…, Stats, decide(), _thread_endings(), Counter

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "LLMResult"
Cohesion: 0.10
Nodes (29): ReasoningEffort, Test double for LLMProvider: scripted replies or errors, records every call.…, OpenRouter over plain httpx (OpenAI-compatible chat completions). The only…, ChatMessage, LLMBadResponseError, LLMError, LLMRateLimitError, LLMResult (+21 more)

### Community 97 - "no_llm_env"
Cohesion: 0.67
Nodes (3): no_llm_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…

### Community 98 - "auth_header"
Cohesion: 0.22
Nodes (9): auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, answer(), _answer(), POST a setup for `user`; any field can be overridden, or dropped by passing…, POST an answer; `question_id` defaults to whatever the caller passes, body…, start_interview() (+1 more)

### Community 99 - "check_decision"
Cohesion: 0.18
Nodes (16): Check, check_decision(), check_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, The decide reply against the case's label; the injection check reads the raw…, decision(), failed(), labelled() (+8 more)

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
Cohesion: 0.19
Nodes (16): NotEnoughQuestionsError, pick_fallback_question(), One unused bank question for `position`, used when the LLM is off or its reply…, Collection, random, fixture_bank(), pick(), fixture (+8 more)

### Community 104 - "test_login.py"
Cohesion: 0.25
Nodes (4): _login_error(), test_registered_user_is_a_plain_active_user(), test_unknown_email_wrong_password_and_inactive_user_fail_identically(), test_valid_login_returns_bearer_token_for_the_user()

### Community 105 - "json"
Cohesion: 0.29
Nodes (10): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, json, _entry(), parametrize, test_invalid_bank_raises_clear_error(), test_shipped_bank_covers_every_type_role_and_level() (+2 more)

### Community 106 - "clock"
Cohesion: 0.22
Nodes (7): clock(), _decision_json(), fixture, Builds a reply in the exact shape the decide call must produce., Builds a reply in the exact shape the interviewer LLM must produce., Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…, _reply_json()

### Community 107 - "test_user_ids.py"
Cohesion: 0.70
Nodes (4): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7()

### Community 108 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (12): get_clock(), Monotonic clock for the per-turn LLM time budget; tests swap in a fake one., Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied (+4 more)

### Community 113 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.50
Nodes (4): Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

## Knowledge Gaps
- **280 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+275 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 673 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `InterviewQuestion` connect `InterviewQuestion` to `interviews_utils.py`, `interviews_reply.py`, `test_interviewer_messages.py`, `test_follow_ups.py`, `test_start_llm.py`, `InterviewMessage`, `test_answer_llm.py`, `main.py`, `interviews_model.py`, `test_turn_budget.py`, `test_interview_report.py`, `Bundle`, `interviews_report.py`, `select_questions`, `InterviewSession`, `test_create_interview.py`, `interviews_controller.py`, `build_usage_report`, `analyze_interview`, `QuestionTurn`, `Stats`, `LLMResult`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `test_create_interview.py`, `typing`, `errors.py`, `interviews_controller.py`, `users_route.py`, `Role`, `tests/conftest.py`, `interviews_model.py`, `Implementation Plan: UUID primary keys`, `InterviewSession`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `test_evals.py` to `LLMResult`, `Feature: Context Management for the Interview LLM Calls`, `check_decision`, `The fundamentals`, `interviews_reply.py`, `QuestionTurn`, `llm`, `main`, `interviews/conftest.py`, `ContextManager`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `QuestionKind`) actually correct?**
  _`InterviewQuestion` has 25 INFERRED edges - model-reasoned connections that need verification._
- **Are the 22 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `InterviewType` (e.g. with `InterviewerInputs` and `InterviewsController`) actually correct?**
  _`InterviewType` has 29 INFERRED edges - model-reasoned connections that need verification._