# Graph Report - cuewise-be  (2026-11-06)

## Corpus Check
- 231 files · ~224,805 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 3542 nodes · 9641 edges · 187 communities (171 shown, 16 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1732 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4dfd8d26`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- auth_controller.py
- LLMError
- test_tracing_routes.py
- decode_token
- test_feedback_evals.py
- interviews_dependencies.py
- Cuewise BE — Project Instructions
- interviews_utils.py
- users_route.py
- test_context_prompts.py
- Implementation Steps
- Implementation Plan: Start an Interview (backend)
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- interviews_context.py
- users_utils.py
- README.md
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- test_feedback_endpoint.py
- audio_container
- ConsoleFormatter
- LLMProvider
- test_answer_stream.py
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Implementation: LLM as the Interviewer (it asks the questions)
- QuestionTurn
- InterviewMessage
- Feature: LLM as the Interviewer (it asks the questions)
- auth_header
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- test_list_interviews.py
- test_transcript.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- interviews_feedback_evals.py
- interviews_model.py
- LLMServerError
- json
- test_evals.py
- Permission
- report_for
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- Implementation: Error Handling
- Implementation Plan: Langfuse Tracing
- InterviewSession
- interviews_feedback_turn.py
- job_description_summary_v2.md
- test_create_interview.py
- test_stream_answer.py
- ChatMessage
- test_request_context.py
- .finish_answer
- hint_for
- Any
- build_usage_report
- exception_handlers.py
- interviews_controller.py
- test_feedback_contract.py
- Role
- RecordingClient
- test_start_llm.py
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- test_job_description_summary.py
- RateLimiter
- test_transcribe.py
- require_permissions
- Implementation Plan: Context Management for the Interview LLM Calls
- .trace
- InterviewQuestion
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- QuestionCategory
- ContextManager
- Langfuse Observability
- interviewer_v3.md
- Tracer
- no_llm_env
- Implementation: Langfuse Tracing
- interviews_feedback.py
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- main.py
- User
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- decision
- test_interview_report.py
- interviews_turn.py
- Feature: Langfuse Tracing
- Langfuse
- FakeProvider
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- test_list_users.py
- interviews_feedback_controller.py
- Langfuse Implementation Notes
- interviewer_v5.md
- LLMResult
- interviews/conftest.py
- Implementation Plan: UUID primary keys
- test_reply_contract.py
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_answer_interview.py
- .write
- Feature: Interview History List (backend)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- pytest
- Implementation: Interview History List (backend)
- Judge Calibration
- Langfuse Prompt Migration
- ErrorResponse
- AI Engineering Learning Path (Cuewise)
- Langfuse CI/CD
- Prompt Engineering
- TranscriptionResult
- Langfuse Implementation Notes
- Slices in detail
- test_create_admin.py
- test_reaction_pick.py
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Error Handling
- RubricCriterion
- test_feedback_context.py
- FeedbackCaseResult
- test_keyterms.py
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- ._run
- Implementation: Interview Feedback and Scoring (Slice 6)
- failed
- The fundamentals
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_get_interview.py
- Feature: Role-Based Access Control (single JWT)
- StoredResult
- Feature: Start an Interview (backend)
- RecordingClient
- time
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- StreamedTurn
- test_login.py
- Feature: Interview Feedback and Scoring (Slice 6)
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- .stream
- feedback_score_v1.md
- feedback_write_v1.md
- build_tracer
- FakeObservation
- check_feedback
- uuid
- page_params
- Checks
- ProviderConfig
- _LostClaim
- budget
- .expected_answers

## God Nodes (most connected - your core abstractions)
1. `FakeProvider` - 91 edges
2. `InterviewsController` - 90 edges
3. `LLMResult` - 80 edges
4. `InterviewQuestion` - 80 edges
5. `QuestionCategory` - 78 edges
6. `InterviewType` - 75 edges
7. `Tracer` - 69 edges
8. `User` - 68 edges
9. `InterviewSession` - 68 edges
10. `JobRole` - 67 edges

## Surprising Connections (you probably didn't know these)
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Constraints` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Project Conventions` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py

## Import Cycles
- None detected.

## Communities (187 total, 16 thin omitted)

### Community 0 - "auth_controller.py"
Cohesion: 0.13
Nodes (16): hash_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Session, AuthRepository, Session, UUID (+8 more)

### Community 1 - "LLMError"
Cohesion: 0.12
Nodes (21): anyio, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Test doubles for LLMProvider and Transcriber: scripted replies or errors,…, LLMError, Exception, The LLM contract every feature codes against: message/result types, typed…, Base for every provider failure. `retryable` marks faults that may pass on…, backoff_seconds() (+13 more)

### Community 2 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 3 - "decode_token"
Cohesion: 0.17
Nodes (27): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+19 more)

### Community 4 - "test_feedback_evals.py"
Cohesion: 0.11
Nodes (34): feedback_scores_for(), One case through the same pre-check, score call, write call and template…, (name, value, comment) per check, plus `valid_reply` and `case_passed`. An…, run_feedback_case(), _usage(), case(), Grader, parametrize (+26 more)

### Community 5 - "interviews_dependencies.py"
Cohesion: 0.11
Nodes (29): Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, get_clock(), get_context_manager(), get_controller(), get_feedback_controller(), get_llm_provider() (+21 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "interviews_utils.py"
Cohesion: 0.06
Nodes (84): NotEnoughQuestionsError, InterviewType, JobRole, Level, EvalSetup, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, interview_categories() (+76 more)

### Community 8 - "users_route.py"
Cohesion: 0.12
Nodes (20): Page, BaseModel, Offset pagination shared by every list endpoint, so clients see one query…, get_db(), Session, UsersController, Session, UsersRepository (+12 more)

### Community 9 - "test_context_prompts.py"
Cohesion: 0.13
Nodes (20): A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), load_prompt(), Testing Strategy, Deviations from Plan, parametrize (+12 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.15
Nodes (27): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect, The label for the decide call: the action it should pick, and the gap when only…, Decision, parse_decision_reply() (+19 more)

### Community 11 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_config.py"
Cohesion: 0.14
Nodes (26): os, _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored() (+18 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - "interviews_context.py"
Cohesion: 0.10
Nodes (26): StrategyOutput, build_context_manager(), _counts(), FeedbackScore, FeedbackWrite, FollowUpDecision, FullHistory, JobDescriptionSummary (+18 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.12
Nodes (15): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions (+7 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.14
Nodes (36): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, Delta, PhaseChanged, StrEnum (+28 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.07
Nodes (72): get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists, 2. What it is, 3. When to use it (+64 more)

### Community 29 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

### Community 30 - "ConsoleFormatter"
Cohesion: 0.22
Nodes (13): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), sys, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success() (+5 more)

### Community 31 - "LLMProvider"
Cohesion: 0.15
Nodes (7): LLMProvider, Protocol, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, datetime, FeedbackGenerator, One budget for the whole generation, started when the request holds its claim.

### Community 32 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (19): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+11 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.18
Nodes (10): Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+2 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "QuestionTurn"
Cohesion: 0.11
Nodes (30): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't…, Answered questions with their answers (and the model's note on each), in… (+22 more)

### Community 37 - "InterviewMessage"
Cohesion: 0.11
Nodes (20): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_a_future_question_is_not_current_either() (+12 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.12
Nodes (18): Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional, Goal (+10 more)

### Community 39 - "auth_header"
Cohesion: 0.11
Nodes (21): Affected Files & Patterns, auth_header(), _header(), client(), make_user(), _make(), fixture, Bearer header for a user; pass role to mint a token whose role claim differs… (+13 more)

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
Cohesion: 0.14
Nodes (29): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+21 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.11
Nodes (23): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages() (+15 more)

### Community 45 - "test_list_interviews.py"
Cohesion: 0.10
Nodes (36): answered(), history(), ids_of(), fixture, parametrize, GET /api/v1/interviews: the candidate's interview history, newest first,…, Start `n` interviews in a row; returns their ids newest first (each start…, Five sessions stored directly (oldest first), with values that sort differently… (+28 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.13
Nodes (18): drain(), Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage(), test_disabled_tracer_is_a_pass_through(), test_failed_call_is_marked_error_and_the_same_exception_is_raised(), test_missing_usage_is_omitted_never_guessed() (+10 more)

### Community 49 - "interviews_feedback_evals.py"
Cohesion: 0.15
Nodes (25): feedback_dataset_items(), feedback_hints_for(), feedback_trace_input(), feedback_trace_output(), FeedbackEvalCase, FeedbackEvalQuestion, FeedbackEvalSetup, FeedbackEvalTurn (+17 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.06
Nodes (18): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, Create the first admin, or promote an existing user to admin. Usage: uv run… (+10 more)

### Community 51 - "LLMServerError"
Cohesion: 0.09
Nodes (21): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, LLMServerError, LLMTimeoutError (+13 more)

### Community 52 - "json"
Cohesion: 0.25
Nodes (13): Testing Strategy, Baseline Failures, json, llm_lines(), One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time() (+5 more)

### Community 53 - "test_evals.py"
Cohesion: 0.15
Nodes (29): load_cases(), Path, contextvars, run_main(), test_a_case_without_an_answer_yet_shows_only_its_kind_and_job_description(), test_a_failed_check_is_scored_false_with_its_detail(), test_a_failed_decision_trace_shows_the_verdict_the_decision_and_the_expected_one(), test_a_passing_case_says_pass_and_a_label_with_a_gap_shows_it() (+21 more)

### Community 54 - "Permission"
Cohesion: 0.21
Nodes (19): Permission, permissions_for(), The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., login(), me(), AuthControllerDep, register(), LoginIn (+11 more)

### Community 55 - "report_for"
Cohesion: 0.11
Nodes (49): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start() (+41 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (27): LLMRateLimitError, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), _make() (+19 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.08
Nodes (60): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+52 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.10
Nodes (35): LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., Clock, completion(), make_provider(), _make(), fixture, parametrize (+27 more)

### Community 59 - "Implementation: Error Handling"
Cohesion: 0.17
Nodes (11): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+3 more)

### Community 60 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.09
Nodes (19): Generation, _model_parameters(), ReasoningEffort, What the call asked the model for, shown on the generation. A temperature only…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, The stream was closed before it finished (client left, or the turn's deadline…, _usage_details(), Affected Files & Patterns (+11 more)

### Community 61 - "InterviewSession"
Cohesion: 0.09
Nodes (23): InterviewSession, _history_filter(), _history_order(), InterviewsRepository, Any, datetime, Session, UUID (+15 more)

### Community 62 - "interviews_feedback_turn.py"
Cohesion: 0.16
Nodes (16): FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, _Attempts, CallUsage, log_feedback_summary() (+8 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 65 - "test_stream_answer.py"
Cohesion: 0.10
Nodes (26): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+18 more)

### Community 66 - "ChatMessage"
Cohesion: 0.13
Nodes (22): ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go… (+14 more)

### Community 67 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 68 - ".finish_answer"
Cohesion: 0.06
Nodes (42): ErrorBody, QuestionNotCurrentError, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, _elapsed_ms(), InterviewSetup, _llm_question(), NamedTuple (+34 more)

### Community 69 - "hint_for"
Cohesion: 0.18
Nodes (12): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, test_a_template_text_hint_tells_a_rate_limit_from_a_bad_text(), test_an_errored_case_hints_at_its_error(), parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes() (+4 more)

### Community 71 - "Any"
Cohesion: 0.13
Nodes (14): AbstractContextManager, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Set the output of the trace being built (call it inside `trace()`): what a…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, Run an SDK call; on any failure log what failed (not why: the message could…, _safe() (+6 more)

### Community 72 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "interviews_controller.py"
Cohesion: 0.07
Nodes (65): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, NoSpeechError, NotFoundError, Any (+57 more)

### Community 75 - "test_feedback_contract.py"
Cohesion: 0.12
Nodes (44): QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that…, assess_evidence(), build_threads(), compute_overall(), FeedbackThread, parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises… (+36 more)

### Community 76 - "Role"
Cohesion: 0.09
Nodes (29): health_check(), StrEnum, Role, CurrentUserDep, raise_conflict(), raise_crash(), raise_db_down(), raise_expired() (+21 more)

### Community 77 - "RecordingClient"
Cohesion: 0.12
Nodes (7): case(), langfuse(), fixture, A Langfuse client stand-in. Entering a trace sets `current_trace`, like the SDK…, RecordingClient, test_a_failed_dataset_upsert_still_scores_the_cases(), test_a_langfuse_outage_does_not_change_the_run()

### Community 78 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Status, Test Cases (+2 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 83 - "RateLimiter"
Cohesion: 0.11
Nodes (19): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, get_transcription_limiter(), limit_transcriptions(), interviews_answer, Tests swap in a fresh limiter so counts never leak between them., Per-user cap on transcriptions, checked before the upload goes anywhere that… (+11 more)

### Community 84 - "test_transcribe.py"
Cohesion: 0.07
Nodes (28): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope (+20 more)

### Community 85 - "require_permissions"
Cohesion: 0.09
Nodes (30): ForbiddenError, get_current_user(), AuthControllerDep, Depends, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check() (+22 more)

### Community 86 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 87 - ".trace"
Cohesion: 0.17
Nodes (11): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Deviations from the first version of this plan (found during /implement), Implementation Steps, Completed Steps, client() (+3 more)

### Community 88 - "InterviewQuestion"
Cohesion: 0.17
Nodes (17): InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, Every stored question, grouped by interview in creation order (UUIDv7), for the…, main(), Session, candidate_messages(), noted(), run() (+9 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "QuestionCategory"
Cohesion: 0.13
Nodes (35): QuestionCategory, read(), _streamed_question(), _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, load_object() (+27 more)

### Community 93 - "ContextManager"
Cohesion: 0.17
Nodes (17): BuiltContext, ContextManager, ContextReport, ContextTooLargeError, _log(), Exception, NamedTuple, Context management: the one place that decides what each LLM call sends. The… (+9 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "Tracer"
Cohesion: 0.12
Nodes (12): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_makes_no_call_without_a_trace_id_or_when_tracing_is_off(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises() (+4 more)

### Community 97 - "no_llm_env"
Cohesion: 0.33
Nodes (6): no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.18
Nodes (10): Commit message suggestion, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+2 more)

### Community 99 - "interviews_feedback.py"
Cohesion: 0.12
Nodes (32): Criterion, What the score call rates, 1 to 5. Which ones apply depends on the question's…, _check_lengths(), Evidence, _has_markup(), _normalized(), parse_write_reply(), BaseModel (+24 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "main.py"
Cohesion: 0.10
Nodes (27): build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, TracingProvider, model_validator, Self, Settings (+19 more)

### Community 104 - "User"
Cohesion: 0.10
Nodes (34): alias, User, UUID, Every check and read of an answer turn, before any LLM call. Raises the usual…, Only the owner of an interview in progress may transcribe for it; returns the…, answer_question(), answer_question_stream(), get_interview() (+26 more)

### Community 105 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.10
Nodes (19): RequestIdFilter, get_bank(), The question source; tests override it with a fixture bank., Deviations from Plan, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1) (+11 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.07
Nodes (63): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_reply() (+55 more)

### Community 109 - "decision"
Cohesion: 0.24
Nodes (15): decision(), hints_of(), labelled(), mentions(), test_a_cut_off_reply_hints_at_max_tokens_before_quality(), test_a_provider_error_hints_that_it_is_not_a_quality_problem(), down(), test_a_reply_that_does_not_parse_hints_at_the_format() (+7 more)

### Community 110 - "test_interview_report.py"
Cohesion: 0.12
Nodes (35): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+27 more)

### Community 111 - "interviews_turn.py"
Cohesion: 0.07
Nodes (57): InterviewerInputs, Plain values for one interviewer or decide call., UUID, At most two attempts; a retry only for a reply that came back but broke the…, Save one whole turn in one commit: advance the session, the answer, the…, End the read transaction before a slow call, so no connection sits idle in a…, ActionKnown, Deadline (+49 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "FakeProvider"
Cohesion: 0.18
Nodes (22): FakeProvider, run_case(), long_case(), noted(), reply(), test_a_passing_case_has_no_hints(), test_a_provider_error_fails_the_case_without_crashing(), test_a_streamed_provider_error_fails_the_case_without_crashing() (+14 more)

### Community 115 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 116 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 117 - "interviews_feedback_controller.py"
Cohesion: 0.19
Nodes (21): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`… (+13 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "LLMResult"
Cohesion: 0.11
Nodes (21): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, Random, ReasoningEffort, Response, OpenAI-compatible chat completions over plain httpx (Google AI Studio,… (+13 more)

### Community 121 - "interviews/conftest.py"
Cohesion: 0.09
Nodes (23): answer(), _answer(), anyio_backend(), as_v5_text(), clock(), _decision_json(), llm(), script() (+15 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "test_reply_contract.py"
Cohesion: 0.06
Nodes (61): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open (+53 more)

### Community 124 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional (+5 more)

### Community 125 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 126 - ".write"
Cohesion: 0.18
Nodes (14): At most two attempts of the write call only. Failing is fine: the template…, 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+6 more)

### Community 127 - "Feature: Interview History List (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "pytest"
Cohesion: 0.29
Nodes (4): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.15
Nodes (12): Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 134 - "ErrorResponse"
Cohesion: 0.21
Nodes (12): ErrorResponse, BaseModel, Testing Strategy, Completed Steps, Acceptance Criteria, Project Conventions, Project Conventions, Project Conventions (+4 more)

### Community 135 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.18
Nodes (10): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slices (+2 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "TranscriptionResult"
Cohesion: 0.32
Nodes (5): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, TranscriptionResult

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "Slices in detail"
Cohesion: 0.18
Nodes (11): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 7: Eval maturity (trust the judge, catch regressions), Slice 9: Tool use and agents (+3 more)

### Community 142 - "test_create_admin.py"
Cohesion: 0.40
Nodes (9): verify_password(), main(), Session, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting(), test_new_admin_password_follows_registration_rules(), test_running_twice_is_a_no_op() (+1 more)

### Community 143 - "test_reaction_pick.py"
Cohesion: 0.26
Nodes (13): LevelGroup, Reactions are warmer for people early in their career and briefer for…, test_the_rubric_anchors_five_levels_for_every_criterion_and_both_level_groups(), pick(), parametrize, test_a_one_entry_pool_still_works(), test_every_category_and_level_group_has_a_pool(), test_final_answer_uses_the_closing_pool() (+5 more)

### Community 144 - "PageParams"
Cohesion: 0.18
Nodes (12): PageParams, NamedTuple, Architecture & Design, Blockers & Resolutions, Implementation Plan: Interview History List (backend), Overview, Project Rules Applied, Ready to Implement (+4 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "Implementation Plan: Error Handling"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec.md: requirement and edge-case IDs are defined here) (+2 more)

### Community 151 - "RubricCriterion"
Cohesion: 0.40
Nodes (4): model_validator, Self, One criterion of the feedback rubric: what it asks, an anchor per score, and…, RubricCriterion

### Community 152 - "test_feedback_context.py"
Cohesion: 0.39
Nodes (13): estimate_tokens(), Step 4 of the feedback plan: what the score and write calls send, through the…, score_inputs(), test_an_answer_over_the_cap_is_shortened_and_counted_but_quotes_still_verify(), test_closing_tags_inside_untrusted_text_are_neutralised(), test_tags_inside_quoted_text_are_neutralised_in_the_write_call(), test_the_largest_allowed_interview_fits_the_score_limit(), test_the_score_call_fences_the_job_description_and_every_answer_as_data() (+5 more)

### Community 154 - "FeedbackCaseResult"
Cohesion: 0.31
Nodes (9): criterion_spread(), FeedbackCaseResult, level_gap_check(), The pair's check, or None when there is nothing to compare: no pair, or either…, Per case: the largest gap between the highest and lowest score any one…, test_nothing_to_compare_is_not_a_level_failure(), test_the_higher_level_must_score_at_least_half_a_point_lower(), check() (+1 more)

### Community 155 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 156 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 157 - "._run"
Cohesion: 0.29
Nodes (9): _Claim, _Interview, _Outcome, Any, NamedTuple, Too little to assess (the code's pre-check, or the model's flag): final, with…, The interview as plain values, read before the claim's commit expires the…, How a generation ended, for the trace (metadata only). (+1 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (14): 9. Review gate (user), Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions (+6 more)

### Community 159 - "failed"
Cohesion: 0.28
Nodes (9): Slice 6: Feedback and scoring, failed(), parametrize, test_a_good_reply_passes_every_check(), test_a_good_streamed_reply_passes_every_check(), test_bad_flags_exit_with_the_valid_choices(), test_check_decision_compares_against_the_label(), test_each_check_catches_its_problem() (+1 more)

### Community 160 - "The fundamentals"
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Decisions (grilled with the user), Implementation Plan: Eval runs in Langfuse (scores + datasets), Overview, Plan-defined criteria, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 162 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 163 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 165 - "Feature: Start an Interview (backend)"
Cohesion: 0.13
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 167 - "time"
Cohesion: 0.15
Nodes (9): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send, starlette_types (+1 more)

### Community 168 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview (+6 more)

### Community 169 - "StreamedTurn"
Cohesion: 0.33
Nodes (4): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, StreamedTurn

### Community 170 - "test_login.py"
Cohesion: 0.25
Nodes (4): _login_error(), test_registered_user_is_a_plain_active_user(), test_unknown_email_wrong_password_and_inactive_user_fail_identically(), test_valid_login_returns_bearer_token_for_the_user()

### Community 171 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.29
Nodes (8): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 174 - ".stream"
Cohesion: 0.36
Nodes (3): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Reply

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "build_tracer"
Cohesion: 0.47
Nodes (6): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 179 - "check_feedback"
Cohesion: 0.20
Nodes (7): Band, _band_check(), check_feedback(), model_validator, Self, The case's labels against what came out. Check names stay stable: Langfuse…, test_a_case_scored_when_it_should_not_have_been_points_at_the_pre_check()

### Community 180 - "uuid"
Cohesion: 0.53
Nodes (5): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7(), uuid

### Community 181 - "page_params"
Cohesion: 0.40
Nodes (5): page_params(), Query, ge, le, MAX_PAGE_SIZE

### Community 182 - "Checks"
Cohesion: 0.40
Nodes (5): Checks, bad_parent(), _consistency(), Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers…

### Community 183 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 184 - "_LostClaim"
Cohesion: 0.67
Nodes (3): _LostClaim, Exception, Another request took the row over while this one ran: this one's writes are…

## Knowledge Gaps
- **550 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+545 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1332 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `InterviewQuestion` connect `InterviewQuestion` to `interviews_utils.py`, `Implementation Steps`, `test_feedback_endpoint.py`, `test_answer_stream.py`, `QuestionTurn`, `InterviewMessage`, `test_answer_llm.py`, `test_list_interviews.py`, `test_transcript.py`, `interviews_model.py`, `json`, `Checks`, `report_for`, `interviews_report.py`, `InterviewSession`, `test_create_interview.py`, `.finish_answer`, `build_usage_report`, `interviews_controller.py`, `test_feedback_contract.py`, `test_start_llm.py`, `interviews_feedback.py`, `test_interview_report.py`, `interviews_turn.py`, `LLMResult`, `test_reply_contract.py`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `LLMError`, `test_tracing_routes.py`, `test_feedback_evals.py`, `interviews_dependencies.py`, `test_tracing_lifespan.py`, `test_feedback_endpoint.py`, `LLMProvider`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `test_tracing.py`, `build_tracer`, `interviews_feedback_evals.py`, `test_evals.py`, `Implementation Plan: Langfuse Tracing`, `interviews_feedback_turn.py`, `ChatMessage`, `Any`, `interviews_controller.py`, `RecordingClient`, `.trace`, `main.py`, `interviews_evals.py`, `interviews_feedback_controller.py`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `InterviewsController` connect `interviews_controller.py` to `LLMError`, `interviews_dependencies.py`, `interviews_utils.py`, `TranscriptionResult`, `PageParams`, `interviews_context.py`, `test_stream_turn.py`, `LLMProvider`, `QuestionTurn`, `InterviewMessage`, `InterviewSession`, `test_stream_answer.py`, `.finish_answer`, `test_feedback_contract.py`, `InterviewQuestion`, `QuestionCategory`, `ContextManager`, `Tracer`, `main.py`, `User`, `interviews_turn.py`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 63 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 63 INFERRED edges - model-reasoned connections that need verification._
- **Are the 32 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 32 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 29 INFERRED edges - model-reasoned connections that need verification._