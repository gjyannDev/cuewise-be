# Graph Report - cuewise-be  (2026-11-04)

## Corpus Check
- 196 files · ~166,998 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 2597 nodes · 6877 edges · 143 communities (131 shown, 12 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1250 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b60a2007`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- Feature: Start an Interview (backend)
- test_tracing_routes.py
- errors.py
- exception_handlers.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- interviews_utils.py
- Implementation Steps
- auth_route.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- ContextManager
- QuestionTurn
- users_utils.py
- README.md
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- LLMProvider
- test_follow_ups.py
- test_start_llm.py
- Implementation Steps
- test_answer_stream.py
- Feature: Context Management for the Interview LLM Calls
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- test_answer_guards.py
- Feature: LLM as the Interviewer (it asks the questions)
- Bundle
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- InterviewMessage
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- tests/conftest.py
- select_questions
- test_reaction_pick.py
- test_turn_budget.py
- test_evals.py
- interviews_turn.py
- test_interview_report.py
- test_fallback_pick.py
- interviews_report.py
- test_openai_compatible.py
- Stats
- .stream
- InterviewQuestion
- require_permissions
- job_description_summary_v2.md
- test_create_interview.py
- test_stream_answer.py
- interviews_model.py
- test_get_interview.py
- interviews_controller.py
- .stream
- uuid
- ChatMessage
- test_reply_contract.py
- AppError
- test_guards.py
- main
- LLMResult
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- test_job_description_summary.py
- test_context.py
- Generation
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- .trace
- test_context_controller.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- analyze_interview
- QuestionCategory
- Langfuse Observability
- interviewer_v3.md
- fixture
- no_llm_env
- TracingProvider
- check_streamed_reply
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- OpenAICompatibleProvider
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: Context Management for the Interview LLM Calls
- Feature: Role-Based Access Control (single JWT)
- Langfuse Dataset Construction
- interviews_evals.py
- StreamedTurn
- get_controller
- test_me.py
- Feature: Langfuse Tracing
- test_llm_settings_default_to_off_with_documented_limits
- Learnings: SSE Streaming of the Interview Turn (Slice 4)
- Langfuse CLI Reference
- Role
- test_request_context.py
- Langfuse Implementation Notes
- interviewer_v5.md
- Implementation Plan: Langfuse Tracing
- llm
- Implementation Plan: UUID primary keys
- Checks
- Feature: Follow-up Questions (decide / write split)
- test_answer_interview.py
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- LLMServerError
- main.py
- Langfuse v4 project migration
- Learnings: LLM Slice 1 (Interviewer Reaction)
- stream_answer
- Judge Calibration
- Langfuse Prompt Migration
- Strategy
- FakeObservation
- Langfuse CI/CD
- Prompt Engineering
- InterviewSetup
- Learnings: Follow-up Questions (decide / write split)
- .__init__
- SummaryInputs

## God Nodes (most connected - your core abstractions)
1. `FakeProvider` - 79 edges
2. `InterviewsController` - 72 edges
3. `InterviewQuestion` - 71 edges
4. `LLMResult` - 63 edges
5. `QuestionCategory` - 59 edges
6. `ChatMessage` - 54 edges
7. `InterviewType` - 54 edges
8. `InterviewSession` - 54 edges
9. `User` - 53 edges
10. `Tracer` - 52 edges

## Surprising Connections (you probably didn't know these)
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Constraints` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Project Conventions` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Trade-offs & Rationale` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/plan.md → app/core/ai/provider.py
- `Deviations from Plan` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/task.md → app/core/ai/provider.py

## Import Cycles
- None detected.

## Communities (143 total, 12 thin omitted)

### Community 0 - "User"
Cohesion: 0.09
Nodes (31): ConflictError, hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Session, User (+23 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 2 - "test_tracing_routes.py"
Cohesion: 0.12
Nodes (7): get_tracer(), Request, Built once at startup (app lifespan); a disabled tracer when the lifespan…, fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 3 - "errors.py"
Cohesion: 0.17
Nodes (29): BadRequestError, InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token() (+21 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.33
Nodes (16): InterviewType, itertools, _bank(), _q(), _select(), test_general_question_is_eligible_for_every_role(), test_mixed_even_count_is_an_exact_split(), test_mixed_short_on_one_type_is_rejected_without_rebalancing() (+8 more)

### Community 8 - "users_route.py"
Cohesion: 0.11
Nodes (19): get_db(), Session, UsersController, Session, UsersRepository, get_controller(), list_users(), Depends (+11 more)

### Community 9 - "interviews_utils.py"
Cohesion: 0.10
Nodes (42): JobRole, Level, What the interview LLM calls send: the tasks and strategies registered with the…, EvalSetup, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), load_prompt() (+34 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.15
Nodes (26): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, A running note is optional model output about the latest answer; it is sent…, _RawDecision (+18 more)

### Community 11 - "auth_route.py"
Cohesion: 0.32
Nodes (12): login(), me(), AuthControllerDep, post, register(), LoginIn, MeOut, BaseModel (+4 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_config.py"
Cohesion: 0.17
Nodes (22): os, _google(), parametrize, _settings(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored(), test_api_key_never_shows_in_repr_or_errors(), test_blank_provider_list_means_llm_off() (+14 more)

### Community 15 - "ContextManager"
Cohesion: 0.16
Nodes (19): BuiltContext, ContextManager, ContextReport, ContextTooLargeError, _log(), Exception, NamedTuple, Even with every droppable entry gone the input is over the strategy's limit. (+11 more)

### Community 16 - "QuestionTurn"
Cohesion: 0.12
Nodes (28): End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't… (+20 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.13
Nodes (40): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, Delta, PhaseChanged, NamedTuple (+32 more)

### Community 28 - "LLMProvider"
Cohesion: 0.13
Nodes (10): LLMProvider, Protocol, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Random, ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Blockers & Resolutions (+2 more)

### Community 29 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): Checkpoint A: the model suggests, the code enforces (concept 5), answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.06
Nodes (38): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, setup_logging(), split_fields(), Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp (+30 more)

### Community 31 - "Implementation Steps"
Cohesion: 0.11
Nodes (18): Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps, Overview, Phase A: plumbing and progress events, Phase B: streaming the question text, Project Rules Applied, Ready to Implement, Skills Consulted (+10 more)

### Community 32 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (18): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+10 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.08
Nodes (21): Architecture & Design, Decisions (grilled with the user), Implementation Plan: Eval runs in Langfuse (scores + datasets), Overview, Plan-defined criteria, Project Rules Applied, Ready to Implement, Skills Consulted (+13 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.07
Nodes (27): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+19 more)

### Community 37 - "test_answer_guards.py"
Cohesion: 0.12
Nodes (15): sqlalchemy_exc, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_a_future_question_is_not_current_either(), test_any_question_but_the_current_one_is_the_same_409() (+7 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "Bundle"
Cohesion: 0.15
Nodes (16): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+8 more)

### Community 40 - "test_context_strategies.py"
Cohesion: 0.18
Nodes (35): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+27 more)

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
Nodes (20): db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview(), test_a_double_submit_stores_one_answer_and_makes_one_call(), test_a_legacy_session_uses_its_stored_questions_and_no_llm() (+12 more)

### Community 45 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 46 - "InterviewMessage"
Cohesion: 0.22
Nodes (14): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, fixture, shape(), started(), test_a_follow_up_is_shown_with_its_kind_and_its_main_questions_number(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left() (+6 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.08
Nodes (30): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, client(), drain(), FakeClient, propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider… (+22 more)

### Community 49 - "tests/conftest.py"
Cohesion: 0.07
Nodes (37): RequestIdFilter, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions (+29 more)

### Community 50 - "select_questions"
Cohesion: 0.10
Nodes (25): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend) (+17 more)

### Community 51 - "test_reaction_pick.py"
Cohesion: 0.21
Nodes (16): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), Random, A predefined, neutral acknowledgement for the answer just given; never the same…, random, pick(), parametrize (+8 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 53 - "test_evals.py"
Cohesion: 0.12
Nodes (47): FakeProvider, load_cases(), Path, decision(), labelled(), long_case(), noted(), reply() (+39 more)

### Community 54 - "interviews_turn.py"
Cohesion: 0.11
Nodes (36): InterviewerInputs, Plain values for one interviewer or decide call., Condense a long job description once, so later calls send less. One attempt…, Decision, Deadline, _decision_label(), Draft, Interviewer (+28 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.07
Nodes (83): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, html_target(), main(), Path (+75 more)

### Community 56 - "test_fallback_pick.py"
Cohesion: 0.21
Nodes (15): NotEnoughQuestionsError, pick_fallback_question(), One unused bank question for `position`, used when the LLM is off or its reply…, Collection, fixture_bank(), pick(), fixture, parametrize (+7 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.17
Nodes (25): analyze_rollup(), _avg(), _cost(), _effectiveness(), _efficiency(), _latency_row(), _limit_tone(), _n() (+17 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.05
Nodes (64): LLMBadResponseError, A 200 whose body is unusable (not JSON, no choices, blank text). Not transient,…, httpx, Clock, completion(), make_provider(), _make(), fixture (+56 more)

### Community 59 - "Stats"
Cohesion: 0.22
Nodes (9): _answer_growth(), _counts(), The numbers the sections and tiles share, worked out once over a list of…, How each follow-up thread was closed, read from the turn that answered its last…, Each follow-up answer's length relative to the answer before it (characters…, Stats, decide(), _thread_endings() (+1 more)

### Community 60 - ".stream"
Cohesion: 0.16
Nodes (9): _int_or_none(), Any, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final…, How long to wait before retrying, or None to give up., One streamed request: its text chunks, then an LLMResult (attempts and latency…, The token counts an OpenAI-compatible usage object reports; None for any it… (+1 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.13
Nodes (16): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Session, UUID, Save one whole turn in one commit: advance the session, the answer, the…, Abandon the user's active session and save the new one with its questions, all… (+8 more)

### Community 62 - "require_permissions"
Cohesion: 0.08
Nodes (38): ForbiddenError, get_current_user(), AuthControllerDep, Depends, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check() (+30 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 65 - "test_stream_answer.py"
Cohesion: 0.27
Nodes (12): fixture, InterviewsController.stream_answer driven directly, for what a test client…, A started interview and a controller wired like the app's: returns (controller,…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing() (+4 more)

### Community 66 - "interviews_model.py"
Cohesion: 0.07
Nodes (12): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, Print the cost, effectiveness and efficiency of the interviewer. Numbers and… (+4 more)

### Community 67 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 68 - "interviews_controller.py"
Cohesion: 0.08
Nodes (63): NotFoundError, QuestionNotCurrentError, SessionNotInProgressError, MessageKind, MessageRole, StrEnum, QuestionKind, QuestionSource (+55 more)

### Community 71 - ".stream"
Cohesion: 0.31
Nodes (4): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Step 11: `FakeProvider.stream`, Reply

### Community 72 - "uuid"
Cohesion: 0.21
Nodes (16): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, main(), Session, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately() (+8 more)

### Community 73 - "ChatMessage"
Cohesion: 0.09
Nodes (29): StrategyOutput, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, build_context_manager(), _counts(), FollowUpDecision, FullHistory (+21 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.23
Nodes (22): follow_up(), parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_follow_up_in_a_behavioral_only_interview_keeps_the_behavioral_category(), test_a_follow_up_is_accepted_without_a_category_and_inherits_the_parents() (+14 more)

### Community 75 - "AppError"
Cohesion: 0.11
Nodes (21): AppError, ErrorBody, ErrorResponse, Any, BaseModel, Exception, Base for expected errors. Controllers raise these instead of HTTPException., Affected Files & Patterns (+13 more)

### Community 76 - "test_guards.py"
Cohesion: 0.15
Nodes (17): CurrentUserDep, _assert_401(), authenticated(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access(), test_guards_allow_or_forbid_by_db_role() (+9 more)

### Community 77 - "main"
Cohesion: 0.08
Nodes (17): dataset_items(), dataset_name(), main(), What the case judged, for the trace list: its kind, the last question and the…, The stream task reads the same cases as write, so they share one dataset., The cases as Langfuse dataset items. The id is the case id behind the dataset's…, The tags that make runs comparable in Langfuse: what was run, and with which…, run_tags() (+9 more)

### Community 78 - "LLMResult"
Cohesion: 0.09
Nodes (34): anyio, Context management: the one place that decides what each LLM call sends. The…, Test double for LLMProvider: scripted replies or errors, records every call.…, _raise_for_status(), OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, LLMError, LLMRateLimitError, LLMRequestError (+26 more)

### Community 79 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Status, Test Cases (+2 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 83 - "test_context.py"
Cohesion: 0.21
Nodes (13): estimate_tokens(), Inputs, manager(), NamedTuple, parametrize, test_a_named_strategy_overrides_the_default(), test_a_strategy_without_a_limit_is_never_trimmed(), test_builds_the_task_with_its_default_strategy() (+5 more)

### Community 84 - "Generation"
Cohesion: 0.13
Nodes (12): AbstractContextManager, Generation, Any, Set the output of the trace being built (call it inside `trace()`): what a…, Run an SDK call; on any failure log what failed (not why: the message could…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, The stream was closed before it finished (client left, or the turn's deadline…, _safe() (+4 more)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 87 - ".trace"
Cohesion: 0.22
Nodes (9): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Deviations from the first version of this plan (found during /implement), Implementation Steps, Completed Steps, Deviations from Plan (+1 more)

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

### Community 92 - "analyze_interview"
Cohesion: 0.23
Nodes (13): analyze_interview(), _call_table(), _dash(), _facts(), _question_table(), Turn N answers the question at position N and asks position N+1: positions are…, Time limits nearly used up, failed or odd calls, overrides, fallbacks, missing…, _rollup_table() (+5 more)

### Community 93 - "QuestionCategory"
Cohesion: 0.12
Nodes (36): QuestionCategory, read(), _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, _load_object(), _normalized() (+28 more)

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

### Community 98 - "TracingProvider"
Cohesion: 0.10
Nodes (14): ReasoningEffort, TracingProvider, Commit message suggestion, Completed Steps, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions (+6 more)

### Community 99 - "check_streamed_reply"
Cohesion: 0.18
Nodes (17): Check, check_decision(), check_reply(), check_streamed_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format., The decide reply against the case's label; the injection check reads the raw… (+9 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "OpenAICompatibleProvider"
Cohesion: 0.12
Nodes (22): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, OpenAICompatibleProvider, ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., Settings, BaseSettings (+14 more)

### Community 104 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional (+7 more)

### Community 105 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 106 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem, Requirements (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.08
Nodes (50): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, DecisionSummary, EvalCase, EvalTurn (+42 more)

### Community 109 - "StreamedTurn"
Cohesion: 0.25
Nodes (6): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

### Community 110 - "get_controller"
Cohesion: 0.21
Nodes (12): get_bank(), get_clock(), get_controller(), get_llm_provider(), Depends, Session, The question source; tests override it with a fixture bank., Built once at startup (app lifespan); None when no key is configured or the… (+4 more)

### Community 111 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.33
Nodes (7): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 114 - "Learnings: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.20
Nodes (8): Checkpoint A: what the candidate waits for, Checkpoint B: streaming vs structured output, Checkpoint C: what a dropped stream leaves behind, Learnings: SSE Streaming of the Interview Turn (Slice 4), Proof (concept 7), Still open, test_other_requests_are_served_while_a_stream_waits_on_the_llm(), stream()

### Community 115 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 116 - "Role"
Cohesion: 0.09
Nodes (21): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, _login_error(), test_registered_user_is_a_plain_active_user() (+13 more)

### Community 117 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

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

### Community 123 - "Checks"
Cohesion: 0.40
Nodes (5): Checks, bad_parent(), _consistency(), Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers…

### Community 124 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 125 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 126 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 127 - "LLMServerError"
Cohesion: 0.36
Nodes (8): LLMServerError, 5xx or a dropped connection: the provider's side failed., test_a_provider_error_fails_the_case_without_crashing(), test_a_provider_error_scores_the_case_failed_with_the_error_class(), down(), test_a_streamed_provider_error_fails_the_case_without_crashing(), test_an_errored_case_trace_says_error_with_the_class(), down()

### Community 128 - "main.py"
Cohesion: 0.29
Nodes (9): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, health_check(), lifespan(), FastAPI, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning() (+1 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 131 - "stream_answer"
Cohesion: 0.29
Nodes (7): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream(), test_done_has_the_json_endpoints_shape_and_content(), run()

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 134 - "Strategy"
Cohesion: 0.40
Nodes (4): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "InterviewSetup"
Cohesion: 0.47
Nodes (3): InterviewSetup, The fallback when the LLM is off, fails, runs out of time or keeps breaking the…, The session fields the interviewer needs, as plain values that survive the end…

### Community 139 - "Learnings: Follow-up Questions (decide / write split)"
Cohesion: 0.33
Nodes (5): Checkpoint B: a small closed decision instead of free text (concept 4), Checkpoint C: what a follow-up costs in context (concept 2), Checkpoint D: labelled evals for a decision (concept 10), Checkpoint E: one deadline for two calls (concept 9), Learnings: Follow-up Questions (decide / write split)

### Community 140 - ".__init__"
Cohesion: 0.50
Nodes (3): Random, AsyncBaseTransport, BaseTransport

### Community 142 - "SummaryInputs"
Cohesion: 0.50
Nodes (3): NamedTuple, SummaryInputs, test_the_summary_task_sends_the_job_description_as_data()

## Knowledge Gaps
- **406 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+401 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 974 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `test_tracing.py` to `main.py`, `TracingProvider`, `test_tracing_routes.py`, `interviews_controller.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `OpenAICompatibleProvider`, `ChatMessage`, `interviews_evals.py`, `main`, `LLMResult`, `get_controller`, `Generation`, `test_evals.py`, `test_tracing_lifespan.py`, `.trace`, `LLMProvider`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `interviews_utils.py`, `InterviewSetup`, `Implementation Steps`, `QuestionTurn`, `test_follow_ups.py`, `test_start_llm.py`, `test_answer_stream.py`, `test_answer_guards.py`, `Bundle`, `test_answer_llm.py`, `InterviewMessage`, `test_turn_budget.py`, `test_interview_report.py`, `interviews_report.py`, `Stats`, `test_create_interview.py`, `interviews_model.py`, `interviews_controller.py`, `uuid`, `test_context_controller.py`, `analyze_interview`, `Checks`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Why does `InterviewsController` connect `interviews_controller.py` to `User`, `test_stream_answer.py`, `TracingProvider`, `InterviewType`, `interviews_utils.py`, `InterviewSetup`, `LLMResult`, `ContextManager`, `test_tracing.py`, `SummaryInputs`, `InterviewMessage`, `InterviewQuestion`, `QuestionTurn`, `get_controller`, `interviews_turn.py`, `test_stream_turn.py`, `LLMProvider`, `QuestionCategory`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 21 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 49 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 49 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 23 INFERRED edges - model-reasoned connections that need verification._