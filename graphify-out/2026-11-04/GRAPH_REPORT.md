# Graph Report - cuewise-be  (2026-11-04)

## Corpus Check
- 196 files · ~167,699 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 2610 nodes · 6930 edges · 139 communities (128 shown, 11 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1255 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b60a2007`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- Feature: Start an Interview (backend)
- test_tracing_routes.py
- decode_token
- exception_handlers.py
- Implementation Plan: Start an Interview (backend)
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- JobRole
- Implementation Steps
- auth_controller.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- ContextTooLargeError
- test_interviewer_messages.py
- users_utils.py
- README.md
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- ContextManager
- interviews_controller.py
- test_start_llm.py
- Implementation Steps
- test_answer_stream.py
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- test_answer_guards.py
- Feature: LLM as the Interviewer (it asks the questions)
- interviews_log.py
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- test_transcript.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- tests/conftest.py
- QuestionTurn
- QuestionCategory
- test_turn_budget.py
- test_evals.py
- interviews_turn.py
- test_interview_report.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- _thread_endings
- OpenAICompatibleProvider
- InterviewQuestion
- Implementation Plan: Role-Based Access Control (single JWT)
- job_description_summary_v2.md
- test_create_interview.py
- InterviewSession
- interviews_model.py
- test_get_interview.py
- InterviewsController
- LLMResult
- build_usage_report
- ChatMessage
- test_reply_contract.py
- errors.py
- test_guards.py
- main
- interviews_utils.py
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- uuid
- ConsoleFormatter
- Generation
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_context_controller.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- Bundle
- InvalidReplyError
- Langfuse Observability
- interviewer_v3.md
- fixture
- no_llm_env
- Implementation: Langfuse Tracing
- check_decision
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- Settings
- require_permissions
- Implementation Plan: Context Management for the Interview LLM Calls
- Implementation Steps
- Langfuse Dataset Construction
- interviews_evals.py
- StreamedTurn
- get_controller
- test_me.py
- Feature: Langfuse Tracing
- test_llm_settings_default_to_off_with_documented_limits
- anyio
- RequestContextMiddleware
- Role
- pytest
- Langfuse Implementation Notes
- interviewer_v5.md
- Implementation Plan: Langfuse Tracing
- llm
- Implementation Plan: UUID primary keys
- WindowLedger
- bank
- test_answer_interview.py
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- LLMServerError
- clock
- Langfuse v4 project migration
- Clock
- stream_answer
- Judge Calibration
- Langfuse Prompt Migration
- Clock
- Tracer
- Langfuse CI/CD
- Prompt Engineering

## God Nodes (most connected - your core abstractions)
1. `FakeProvider` - 87 edges
2. `InterviewsController` - 72 edges
3. `InterviewQuestion` - 71 edges
4. `LLMResult` - 64 edges
5. `QuestionCategory` - 59 edges
6. `ChatMessage` - 54 edges
7. `InterviewType` - 54 edges
8. `InterviewSession` - 54 edges
9. `User` - 53 edges
10. `Tracer` - 52 edges

## Surprising Connections (you probably didn't know these)
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
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

## Communities (139 total, 11 thin omitted)

### Community 0 - "User"
Cohesion: 0.12
Nodes (20): get_controller(), Depends, Session, User, AuthRepository, Session, UUID, main() (+12 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 2 - "test_tracing_routes.py"
Cohesion: 0.12
Nodes (7): get_tracer(), Request, Built once at startup (app lifespan); a disabled tracer when the lifespan…, fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 3 - "decode_token"
Cohesion: 0.14
Nodes (25): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Testing Strategy, Implementation Steps (+17 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.06
Nodes (31): Checkpoint A: after Step 3 (provider package), Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction) (+23 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.16
Nodes (27): NotEnoughQuestionsError, InterviewType, Random, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), Pick `count` distinct questions for the setup, in interview order. The single…, select_questions() (+19 more)

### Community 8 - "users_route.py"
Cohesion: 0.12
Nodes (19): get_db(), Session, UsersController, Session, UsersRepository, get_controller(), list_users(), Depends (+11 more)

### Community 9 - "JobRole"
Cohesion: 0.12
Nodes (34): JobRole, Level, EvalSetup, load_bank(), load_prompt(), Path, Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never… (+26 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.17
Nodes (23): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, _load_object(), parse_decision_reply(), The reply as a JSON object: one optional fence around it, nothing else before…, The decide call suggests; the code still applies the follow-up cap and the time… (+15 more)

### Community 11 - "auth_controller.py"
Cohesion: 0.16
Nodes (19): hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., login(), me(), AuthControllerDep, post (+11 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_config.py"
Cohesion: 0.14
Nodes (24): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., _google(), parametrize, _settings(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored() (+16 more)

### Community 15 - "ContextTooLargeError"
Cohesion: 0.27
Nodes (7): BuiltContext, ContextReport, ContextTooLargeError, _log(), Exception, NamedTuple, Even with every droppable entry gone the input is over the strategy's limit.

### Community 16 - "test_interviewer_messages.py"
Cohesion: 0.12
Nodes (23): interviewer_history(), job_description_block(), Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't…, Answered questions with their answers (and the model's note on each), in…, render_interviewer_prompt(), render_template() (+15 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.15
Nodes (33): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, StrEnum, The next chunk of the question being written (shown as it arrives)., What the turn ends with, after the limits: the model can only ask for the first…, TurnAction (+25 more)

### Community 28 - "ContextManager"
Cohesion: 0.15
Nodes (21): ContextManager, LLMProvider, Protocol, _add_usage(), _case_inputs(), ReasoningEffort, One decide call on the case's latest answer, as the app makes it after every…, The streamed turn's write call (interviewer_stream, v5) on one case: the same… (+13 more)

### Community 29 - "interviews_controller.py"
Cohesion: 0.11
Nodes (35): MessageKind, MessageRole, StrEnum, QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, A main question opens a thread; a follow-up digs into the latest answer of that…, Transcript item kinds: a question comes from interview_questions, the other two… (+27 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 31 - "Implementation Steps"
Cohesion: 0.08
Nodes (30): ActionKnown, PhaseChanged, NamedTuple, The turn's final action, sent only once nothing can change it (a follow-up only…, The question text streamed so far is taken back: that draft failed, another one…, The same turn as `answer_turn` (same decide, limits and fallbacks), telling the…, Reset, Settled (+22 more)

### Community 32 - "test_answer_stream.py"
Cohesion: 0.07
Nodes (20): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+12 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.18
Nodes (10): Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+2 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+17 more)

### Community 37 - "test_answer_guards.py"
Cohesion: 0.14
Nodes (13): message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing(), failing_commit() (+5 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "interviews_log.py"
Cohesion: 0.13
Nodes (18): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+10 more)

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
Cohesion: 0.15
Nodes (27): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+19 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.14
Nodes (16): itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., questions(), Answer every question of a started interview; returns the list of answer…, run_interview(), test_a_mixed_bank_only_interview_alternates_behavioral_first(), test_a_new_interview_started_during_the_call_wins() (+8 more)

### Community 45 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.11
Nodes (26): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, client(), drain(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result() (+18 more)

### Community 49 - "tests/conftest.py"
Cohesion: 0.13
Nodes (21): health_check(), CurrentUserDep, Affected Files & Patterns, os, sqlalchemy_exc, sqlalchemy_pool, auth_header(), _header() (+13 more)

### Community 50 - "QuestionTurn"
Cohesion: 0.12
Nodes (22): _counts(), An earlier question as the model would have written it. A follow-up was written…, App data at the end of the last user message; untrusted parts (questions,…, _status_block(), End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), main_numbers(), neutralize_app_tags() (+14 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.11
Nodes (32): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, pick_fallback_question(), pick_reaction(), Random, One unused bank question for `position`, used when the LLM is off or its reply…, A predefined, neutral acknowledgement for the answer just given; never the same… (+24 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 53 - "test_evals.py"
Cohesion: 0.11
Nodes (58): FakeProvider, build_context_manager(), `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, load_cases(), Path, run_case(), decision(), hints_of() (+50 more)

### Community 54 - "interviews_turn.py"
Cohesion: 0.11
Nodes (33): InterviewerInputs, Plain values for one interviewer or decide call., Condense a long job description once, so later calls send less. One attempt…, Decision, NamedTuple, Deadline, _decision_label(), Draft (+25 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.07
Nodes (85): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, What needs attention comes first (watch, checks), then the sections, then the…, render_html(), render_text(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, html_target() (+77 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.18
Nodes (23): LLMTimeoutError, chunk(), drain(), Interrupted, make_provider(), ok(), Exception, parametrize (+15 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.17
Nodes (25): analyze_rollup(), _avg(), _cost(), _effectiveness(), _efficiency(), _latency_row(), _limit_tone(), _n() (+17 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.15
Nodes (29): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_cached_and_reasoning_tokens_are_none_when_not_reported() (+21 more)

### Community 59 - "_thread_endings"
Cohesion: 0.50
Nodes (4): _counts(), How each follow-up thread was closed, read from the turn that answered its last…, _thread_endings(), Counter

### Community 60 - "OpenAICompatibleProvider"
Cohesion: 0.16
Nodes (12): _int_or_none(), OpenAICompatibleProvider, Any, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final…, How long to wait before retrying, or None to give up., One streamed request: its text chunks, then an LLMResult (attempts and latency… (+4 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.13
Nodes (18): InterviewMessage, InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, A candidate answer or the interviewer's reaction to one question. The questions…, InterviewsRepository, Session, UUID, Save one whole turn in one commit: advance the session, the answer, the… (+10 more)

### Community 62 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.06
Nodes (34): get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, require_roles(), check(), bearer_scheme, Affected Files & Patterns, Architecture & Design (+26 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 65 - "InterviewSession"
Cohesion: 0.20
Nodes (15): InterviewSession, test_database_rejects_two_in_progress_sessions_for_one_user(), session_for(), fixture, InterviewsController.stream_answer driven directly, for what a test client…, A started interview and a controller wired like the app's: returns (controller,…, saved_answers(), summaries() (+7 more)

### Community 66 - "interviews_model.py"
Cohesion: 0.07
Nodes (16): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, Create the first admin, or promote an existing user to admin. Usage: uv run… (+8 more)

### Community 67 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 68 - "InterviewsController"
Cohesion: 0.10
Nodes (36): QuestionNotCurrentError, SessionNotInProgressError, InterviewsController, InterviewSetup, _llm_question(), NamedTuple, UUID, The main question the answered question belongs to (itself, or a follow-up's… (+28 more)

### Community 71 - "LLMResult"
Cohesion: 0.11
Nodes (17): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, LLMError, LLMResult, Exception, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Base for every provider failure. `retryable` marks faults that may pass on… (+9 more)

### Community 72 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 73 - "ChatMessage"
Cohesion: 0.08
Nodes (31): estimate_tokens(), StrategyOutput, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, FollowUpDecision, FullHistory, JobDescriptionSummary (+23 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.07
Nodes (55): Checkpoint A: the model suggests, the code enforces (concept 5), Checkpoint B: a small closed decision instead of free text (concept 4), Checkpoint D: labelled evals for a decision (concept 10), Checkpoint E: one deadline for two calls (concept 9), Learnings: Follow-up Questions (decide / write split), Blockers, Constraints, Edge Cases (+47 more)

### Community 75 - "errors.py"
Cohesion: 0.07
Nodes (43): AppError, BadRequestError, ConflictError, ErrorBody, ErrorResponse, ForbiddenError, InvalidCredentialsError, NotFoundError (+35 more)

### Community 76 - "test_guards.py"
Cohesion: 0.13
Nodes (19): fastapi, admin_role(), _assert_401(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access() (+11 more)

### Community 77 - "main"
Cohesion: 0.09
Nodes (15): dataset_items(), dataset_name(), main(), The stream task reads the same cases as write, so they share one dataset., The cases as Langfuse dataset items. The id is the case id behind the dataset's…, The tags that make runs comparable in Langfuse: what was run, and with which…, run_tags(), Namespace (+7 more)

### Community 78 - "interviews_utils.py"
Cohesion: 0.10
Nodes (31): Context management: the one place that decides what each LLM call sends. The…, Test double for LLMProvider: scripted replies or errors, records every call.…, The LLM contract every feature codes against: message/result types, typed…, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, setup_logging(), lifespan(), FastAPI, What the interview LLM calls send: the tasks and strategies registered with the… (+23 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Status, Test Cases (+2 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview (+6 more)

### Community 82 - "uuid"
Cohesion: 0.18
Nodes (12): main(), Session, parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version() (+4 more)

### Community 83 - "ConsoleFormatter"
Cohesion: 0.18
Nodes (14): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), LogRecord, sys, _record(), test_console_appends_the_traceback() (+6 more)

### Community 84 - "Generation"
Cohesion: 0.13
Nodes (13): AbstractContextManager, Generation, Any, Set the output of the trace being built (call it inside `trace()`): what a…, Run an SDK call; on any failure log what failed (not why: the message could…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, The stream was closed before it finished (client left, or the turn's deadline…, _safe() (+5 more)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 87 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.10
Nodes (20): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Architecture & Design, Decisions (grilled with the user), Deviations from the first version of this plan (found during /implement), Implementation Plan: Eval runs in Langfuse (scores + datasets) (+12 more)

### Community 88 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learnings: Context Management"
Cohesion: 0.29
Nodes (6): Checkpoint A: the baseline (before any context change), Checkpoint B: the six-part prompts (after step 3), Checkpoint C: the "before" snapshot (step 8), Checkpoint D: the comparison (step 12) - strategy comparison recorded, ablations open, Checkpoint E: where the cost went (live interview, 2026-10-30), Learnings: Context Management

### Community 92 - "Bundle"
Cohesion: 0.15
Nodes (21): analyze_interview(), Bundle, _call_table(), Checks, bad_parent(), _consistency(), _dash(), _facts() (+13 more)

### Community 93 - "InvalidReplyError"
Cohesion: 0.14
Nodes (27): read(), _streamed_question(), _check_question(), InterviewerReply, InvalidReplyError, _normalized(), parse_interviewer_reply(), parse_streamed_reply() (+19 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.18
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "fixture"
Cohesion: 0.18
Nodes (11): answer(), _answer(), anyio_backend(), _decision_json(), fixture, Builds a reply in the exact shape the decide call must produce., Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a setup for `user`; any field can be overridden, or dropped by passing… (+3 more)

### Community 97 - "no_llm_env"
Cohesion: 0.50
Nodes (4): no_langfuse_env(), no_llm_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.18
Nodes (10): Commit message suggestion, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+2 more)

### Community 99 - "check_decision"
Cohesion: 0.23
Nodes (12): check_decision(), The decide reply against the case's label; the injection check reads the raw…, failed(), labelled(), parametrize, test_a_good_reply_passes_every_check(), test_an_injected_marker_in_the_decision_fails_the_case(), test_bad_flags_exit_with_the_valid_choices() (+4 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "Settings"
Cohesion: 0.13
Nodes (18): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, TracingProvider, Settings, BaseSettings, Completed Steps, Step 0: Rename the provider to a vendor-neutral name, field_validator (+10 more)

### Community 104 - "require_permissions"
Cohesion: 0.09
Nodes (28): Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), answer_question(), answer_question_stream(), get_interview(), get_transcript(), post (+20 more)

### Community 105 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 106 - "Implementation Steps"
Cohesion: 0.15
Nodes (19): get_context_manager(), Decides what each LLM call sends; tests swap in one with a tiny limit., _print_summary(), The same one-off condensation the app makes at interview start; its tokens…, One run proves little (the same cases scored 5/6, then 6/6): look at the spread…, summarize(), summarize_runs(), Summary (+11 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.09
Nodes (37): anyio_from_thread, _action_and_gap(), CaseResult, Check, check_reply(), check_streamed_reply(), DecisionSummary, EvalCase (+29 more)

### Community 109 - "StreamedTurn"
Cohesion: 0.25
Nodes (6): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

### Community 110 - "get_controller"
Cohesion: 0.17
Nodes (16): get_bank(), get_clock(), get_controller(), get_llm_provider(), Depends, Session, The question source; tests override it with a fixture bank., Built once at startup (app lifespan); None when no key is configured or the… (+8 more)

### Community 111 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.33
Nodes (7): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 114 - "anyio"
Cohesion: 0.18
Nodes (9): anyio, Checkpoint A: what the candidate waits for, Checkpoint B: streaming vs structured output, Checkpoint C: what a dropped stream leaves behind, Learnings: SSE Streaming of the Interview Turn (Slice 4), Proof (concept 7), Still open, test_other_requests_are_served_while_a_stream_waits_on_the_llm() (+1 more)

### Community 115 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 116 - "Role"
Cohesion: 0.12
Nodes (18): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, fastapi_security, test_admin_holds_every_user_permission() (+10 more)

### Community 117 - "pytest"
Cohesion: 0.25
Nodes (4): pytest, parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 121 - "llm"
Cohesion: 0.24
Nodes (6): as_v5_text(), llm(), script(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY…

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "WindowLedger"
Cohesion: 0.39
Nodes (8): Task, WindowLedger, fixture, tiny_context(), test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), test_the_guard_never_drops_the_current_thread(), manager()

### Community 124 - "bank"
Cohesion: 0.22
Nodes (9): Acceptance Criteria, Acceptance Criteria, Edge Cases, Functional, Non-Functional, Requirements, Test Results, bank() (+1 more)

### Community 125 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 126 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 127 - "LLMServerError"
Cohesion: 0.15
Nodes (15): Random, _raise_for_status(), OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, LLMRateLimitError, LLMRequestError, LLMServerError, 5xx or a dropped connection: the provider's side failed., Other 4xx (bad key, bad request): retrying sends the same broken request again. (+7 more)

### Community 128 - "clock"
Cohesion: 0.25
Nodes (4): _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 131 - "stream_answer"
Cohesion: 0.29
Nodes (7): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream(), test_done_has_the_json_endpoints_shape_and_content(), run()

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 134 - "Clock"
Cohesion: 0.33
Nodes (3): anyio_backend(), Clock, fixture

### Community 135 - "Tracer"
Cohesion: 0.10
Nodes (11): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, FakeObservation, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_sdk_failure_does_not_mask_the_llm_error(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises() (+3 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

## Knowledge Gaps
- **406 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+401 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 975 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `test_tracing_routes.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `InterviewsController`, `Settings`, `InterviewType`, `ChatMessage`, `interviews_evals.py`, `main`, `interviews_utils.py`, `get_controller`, `test_tracing.py`, `Generation`, `test_evals.py`, `test_tracing_lifespan.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `interviews_controller.py`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Why does `InterviewSession` connect `InterviewSession` to `test_answer_stream.py`, `test_create_interview.py`, `interviews_model.py`, `InterviewsController`, `test_answer_guards.py`, `Implementation Steps`, `test_reply_contract.py`, `test_answer_llm.py`, `test_transcript.py`, `uuid`, `InterviewQuestion`, `test_answer_interview.py`, `test_interview_report.py`, `interviews_report.py`, `Bundle`, `interviews_controller.py`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `test_evals.py` to `Implementation Steps`, `ContextManager`, `Implementation Steps`, `Feature: Context Management for the Interview LLM Calls`, `The fundamentals`, `test_tracing.py`, `QuestionTurn`, `LLMResult`, `ChatMessage`, `main`, `interviews_utils.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `check_decision`, `Settings`, `require_permissions`, `Implementation Steps`, `interviews_evals.py`, `llm`, `LLMServerError`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Are the 21 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 49 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 49 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 23 INFERRED edges - model-reasoned connections that need verification._