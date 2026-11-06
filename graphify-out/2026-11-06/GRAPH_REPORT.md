# Graph Report - cuewise-be  (2026-11-06)

## Corpus Check
- 231 files · ~223,825 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 3534 nodes · 9612 edges · 188 communities (165 shown, 23 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1732 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4dfd8d26`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- AuthRepository
- Learn: Calling an LLM safely (Slice 1, interviewer reaction)
- test_tracing_routes.py
- decode_token
- test_feedback_evals.py
- interviews_dependencies.py
- Cuewise BE — Project Instructions
- interviews_utils.py
- users_route.py
- test_context_prompts.py
- Implementation Steps
- test_select_questions.py
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
- logging.py
- LLMProvider
- test_answer_stream.py
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Implementation: LLM as the Interviewer (it asks the questions)
- QuestionTurn
- test_answer_guards.py
- Feature: LLM as the Interviewer (it asks the questions)
- tests/conftest.py
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- test_list_interviews.py
- test_transcript.py
- Implementation: Follow-up Questions (decide / write split)
- Tracer
- interviews_feedback_evals.py
- interviews_model.py
- LLMServerError
- test_turn_budget.py
- test_evals.py
- auth_controller.py
- test_interview_report.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- Implementation: Error Handling
- TracingProvider
- InterviewQuestion
- LLMResult
- job_description_summary_v2.md
- test_create_interview.py
- test_stream_answer.py
- ChatMessage
- test_request_context.py
- interviews_controller.py
- hint_for
- Any
- build_usage_report
- exception_handlers.py
- test_reply_contract.py
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
- Implementation Steps
- .trace
- ContextManager
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- test_streamed_reply.py
- InvalidReplyError
- Langfuse Observability
- interviewer_v3.md
- fixture
- no_llm_env
- Implementation: Langfuse Tracing
- interviews_feedback.py
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- main.py
- interviews_route.py
- RecordingClient
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- follow_up
- interview_report.py
- interviews_turn.py
- Feature: Langfuse Tracing
- Langfuse
- run_case
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- test_list_users.py
- interviews_feedback_controller.py
- Langfuse Implementation Notes
- interviewer_v5.md
- OpenAICompatibleProvider
- llm
- Implementation Plan: UUID primary keys
- test_follow_ups.py
- Implementation Plan: Role-Based Access Control (single JWT)
- test_answer_interview.py
- .write
- clock
- Langfuse Dataset Construction
- Langfuse v4 project migration
- pytest
- Implementation: Interview History List (backend)
- Judge Calibration
- Langfuse Prompt Migration
- Feature: Follow-up Questions (decide / write split)
- Clock
- Langfuse CI/CD
- Prompt Engineering
- fake.py
- Langfuse Implementation Notes
- Clock
- test_create_admin.py
- QuestionCategory
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- Implementation Steps
- ._covers_every_criterion
- test_feedback_context.py
- FeedbackCaseResult
- test_keyterms.py
- _reset_request_id
- ._run
- Implementation: Interview Feedback and Scoring (Slice 6)
- run_feedback
- The fundamentals
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_get_interview.py
- Feature: Role-Based Access Control (single JWT)
- WriteText
- ErrorResponse
- RecordingClient
- RequestContextMiddleware
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- StreamedTurn
- Affected Files & Patterns
- failed
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- usage_report.py
- feedback_score_v1.md
- feedback_write_v1.md
- FeedbackThread
- stream_answer
- ._ordered
- Clock
- .insert_feedback

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

## Communities (188 total, 23 thin omitted)

### Community 0 - "AuthRepository"
Cohesion: 0.12
Nodes (11): get_controller(), Depends, Session, AuthRepository, Session, UUID, existing_email(), fixture (+3 more)

### Community 1 - "Learn: Calling an LLM safely (Slice 1, interviewer reaction)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Calling an LLM safely (Slice 1, interviewer reaction)

### Community 2 - "test_tracing_routes.py"
Cohesion: 0.11
Nodes (9): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient (+1 more)

### Community 3 - "decode_token"
Cohesion: 0.13
Nodes (24): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Implementation Steps, Testing Strategy (+16 more)

### Community 4 - "test_feedback_evals.py"
Cohesion: 0.14
Nodes (25): feedback_scores_for(), One case through the same pre-check, score call, write call and template…, (name, value, comment) per check, plus `valid_reply` and `case_passed`. An…, run_feedback_case(), case(), Grader, Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The…, A fake provider: scores every criterion `value`, quoting the start of each… (+17 more)

### Community 5 - "interviews_dependencies.py"
Cohesion: 0.11
Nodes (31): get_db(), Session, get_bank(), get_clock(), get_context_manager(), get_controller(), get_feedback_controller(), get_feedback_limiter() (+23 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "interviews_utils.py"
Cohesion: 0.07
Nodes (69): InterviewType, JobRole, Level, MessageKind, MessageRole, StrEnum, Transcript item kinds: a question comes from interview_questions, the other two…, BankQuestion (+61 more)

### Community 8 - "users_route.py"
Cohesion: 0.16
Nodes (14): Page, BaseModel, UsersController, Session, UsersRepository, get_controller(), list_users(), Depends (+6 more)

### Community 9 - "test_context_prompts.py"
Cohesion: 0.12
Nodes (22): load_prompt(), Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt(), render_interviewer_v2_prompt(), parametrize, test_a_valid_note_is_returned_trimmed(), test_a_valid_summary_is_returned_trimmed() (+14 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.20
Nodes (20): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect, The label for the decide call: the action it should pick, and the gap when only…, parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time… (+12 more)

### Community 11 - "test_select_questions.py"
Cohesion: 0.09
Nodes (38): NotEnoughQuestionsError, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, QuestionOut, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions() (+30 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_config.py"
Cohesion: 0.12
Nodes (28): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows() (+20 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.17
Nodes (24): anyio_backend(), listen_body(), make_transcriber(), ok(), fixture, parametrize, Response, A pre-recorded /v1/listen response, trimmed to the fields the transcriber reads. (+16 more)

### Community 16 - "interviews_context.py"
Cohesion: 0.10
Nodes (29): StrategyOutput, QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that…, build_context_manager(), _counts(), FeedbackScore, FeedbackWrite, FollowUpDecision (+21 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.13
Nodes (40): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, Delta, PhaseChanged, NamedTuple (+32 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.12
Nodes (56): InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, 5. What can go wrong, 8. Check your understanding, happy(), interview(), post(), parametrize (+48 more)

### Community 29 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

### Community 30 - "logging.py"
Cohesion: 0.15
Nodes (17): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), LogRecord, pathlib, re, starlette_types (+9 more)

### Community 31 - "LLMProvider"
Cohesion: 0.06
Nodes (27): LLMProvider, Protocol, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Blockers & Resolutions, Deviations Found During Implementation (+19 more)

### Community 32 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (21): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+13 more)

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
Cohesion: 0.10
Nodes (37): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the… (+29 more)

### Community 37 - "test_answer_guards.py"
Cohesion: 0.14
Nodes (13): sqlalchemy_exc, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing() (+5 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.11
Nodes (19): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+11 more)

### Community 39 - "tests/conftest.py"
Cohesion: 0.09
Nodes (27): health_check(), CurrentUserDep, Affected Files & Patterns, fastapi, os, sqlalchemy_pool, auth_header(), _header() (+19 more)

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
Nodes (27): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+19 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.06
Nodes (39): 2. What it is, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+31 more)

### Community 45 - "test_list_interviews.py"
Cohesion: 0.10
Nodes (36): answered(), history(), ids_of(), fixture, parametrize, GET /api/v1/interviews: the candidate's interview history, newest first,…, Start `n` interviews in a row; returns their ids newest first (each start…, Five sessions stored directly (oldest first), with values that sort differently… (+28 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "Tracer"
Cohesion: 0.06
Nodes (39): build_tracer(), Send what is still buffered, then stop the background exporter. Called once at…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, Tracer, client(), drain(), FakeClient, FakeObservation (+31 more)

### Community 49 - "interviews_feedback_evals.py"
Cohesion: 0.13
Nodes (19): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), check_feedback(), FeedbackEvalQuestion, FeedbackEvalSetup, FeedbackEvalTurn (+11 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.13
Nodes (10): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, DeclarativeBase, logging_config, sqlalchemy (+2 more)

### Community 51 - "LLMServerError"
Cohesion: 0.08
Nodes (34): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The first channel's best transcript (blank for silence) and the reported audio…, _int_or_none() (+26 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.22
Nodes (14): Testing Strategy, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start() (+6 more)

### Community 53 - "test_evals.py"
Cohesion: 0.11
Nodes (48): FakeProvider, load_cases(), Path, contextvars, Reply, decision(), hints_of(), labelled() (+40 more)

### Community 54 - "auth_controller.py"
Cohesion: 0.18
Nodes (17): hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., login(), me(), AuthControllerDep, register() (+9 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.13
Nodes (54): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http() (+46 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.17
Nodes (24): LLMBadResponseError, A 200 whose body is unusable (not JSON, no choices, blank text). Not transient,…, chunk(), drain(), Interrupted, make_provider(), ok(), Exception (+16 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (69): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+61 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.14
Nodes (31): LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget() (+23 more)

### Community 59 - "Implementation: Error Handling"
Cohesion: 0.13
Nodes (16): RequestIdFilter, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions (+8 more)

### Community 60 - "TracingProvider"
Cohesion: 0.22
Nodes (6): _model_parameters(), ReasoningEffort, What the call asked the model for, shown on the generation. A temperature only…, TracingProvider, Implementation Steps, test_disabled_tracer_is_a_pass_through()

### Community 61 - "InterviewQuestion"
Cohesion: 0.07
Nodes (45): HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, The user's own interviews in the requested order: the history table. Under the…, InterviewMessage, InterviewQuestion, InterviewSession (+37 more)

### Community 62 - "LLMResult"
Cohesion: 0.11
Nodes (25): BuiltContext, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, LLMResult, ScoreResult, _Attempts, CallUsage, FeedbackGenerator (+17 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 65 - "test_stream_answer.py"
Cohesion: 0.13
Nodes (22): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+14 more)

### Community 66 - "ChatMessage"
Cohesion: 0.09
Nodes (30): ContextReport, ContextTooLargeError, _log(), Exception, NamedTuple, Context management: the one place that decides what each LLM call sends. The…, Even with every droppable entry gone the input is over the strategy's limit., ChatMessage (+22 more)

### Community 67 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 68 - "interviews_controller.py"
Cohesion: 0.05
Nodes (73): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ErrorBody, NoSpeechError, Any, Exception (+65 more)

### Community 69 - "hint_for"
Cohesion: 0.18
Nodes (12): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, test_a_template_text_hint_tells_a_rate_limit_from_a_bad_text(), test_an_errored_case_hints_at_its_error(), parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes() (+4 more)

### Community 71 - "Any"
Cohesion: 0.09
Nodes (19): AbstractContextManager, Generation, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Set the output of the trace being built (call it inside `trace()`): what a…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, Run an SDK call; on any failure log what failed (not why: the message could… (+11 more)

### Community 72 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 75 - "test_feedback_contract.py"
Cohesion: 0.24
Nodes (27): assess_evidence(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The pre-check, before any LLM call: enough main questions have a real answer to…, parametrize, question_json(), The feedback contract (interviews_feedback.py): the code pre-check, the score…, reason_of() (+19 more)

### Community 76 - "Role"
Cohesion: 0.13
Nodes (22): StrEnum, Role, enum, _assert_401(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access() (+14 more)

### Community 77 - "RecordingClient"
Cohesion: 0.12
Nodes (7): case(), langfuse(), fixture, A Langfuse client stand-in. Entering a trace sets `current_trace`, like the SDK…, RecordingClient, test_a_failed_dataset_upsert_still_scores_the_cases(), test_a_langfuse_outage_does_not_change_the_run()

### Community 78 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 79 - "Langfuse"
Cohesion: 0.12
Nodes (14): Skill Feedback, Submission options, 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles (+6 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

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
Cohesion: 0.15
Nodes (29): ForbiddenError, InvalidCredentialsError, TokenExpiredError, TokenMissingError, UnauthorizedError, Permission, permissions_for(), The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later. (+21 more)

### Community 86 - "Implementation Steps"
Cohesion: 0.13
Nodes (19): The same one-off condensation the app makes at interview start; its tokens…, summarize(), Summary, A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), Blockers & Resolutions (+11 more)

### Community 87 - ".trace"
Cohesion: 0.23
Nodes (8): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Deviations from the first version of this plan (found during /implement), Implementation Steps, Completed Steps, tracer()

### Community 88 - "ContextManager"
Cohesion: 0.17
Nodes (21): ContextManager, Task, An earlier question as the model would have written it. A follow-up was written…, WindowLedger, candidate_messages(), noted(), fixture, run() (+13 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "test_streamed_reply.py"
Cohesion: 0.17
Nodes (17): read(), interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), One streamed attempt: the question's text chunks (never the CATEGORY line),…, parse(), parametrize, interviewer_v5's streamed reply: a `CATEGORY:` header line (next-question mode…, test_a_header_split_across_chunks_is_read_once_its_line_ends() (+9 more)

### Community 93 - "InvalidReplyError"
Cohesion: 0.16
Nodes (19): _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, load_object(), _normalized(), parse_interviewer_reply(), parse_streamed_reply() (+11 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "fixture"
Cohesion: 0.14
Nodes (14): answer(), _answer(), anyio_backend(), _decision_json(), fixture, Builds a reply in the exact shape the decide call must produce., Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a recording to the transcription endpoint; `audio=None` sends no file part… (+6 more)

### Community 97 - "no_llm_env"
Cohesion: 0.33
Nodes (6): no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.15
Nodes (11): Commit message suggestion, Completed Steps, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 99 - "interviews_feedback.py"
Cohesion: 0.15
Nodes (25): Criterion, What the score call rates, 1 to 5. Which ones apply depends on the question's…, Evidence, _has_markup(), _normalized(), BaseModel, _question_score(), QuestionScore (+17 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 103 - "main.py"
Cohesion: 0.10
Nodes (27): build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, model_validator, Self, Settings (+19 more)

### Community 104 - "interviews_route.py"
Cohesion: 0.09
Nodes (34): alias, answer_question(), answer_question_stream(), generate_feedback(), get_feedback(), get_interview(), get_transcript(), list_interviews() (+26 more)

### Community 105 - "RecordingClient"
Cohesion: 0.11
Nodes (12): anyio, test_other_requests_are_served_while_a_stream_waits_on_the_llm(), stream(), submit_the_same_answer_elsewhere(), fresh_limiter(), owner(), fixture, Records the trace, its steps (chains) and the code's checks (guardrails) apart,… (+4 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.08
Nodes (51): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, dataset_items(), dataset_name(), DecisionSummary (+43 more)

### Community 109 - "follow_up"
Cohesion: 0.18
Nodes (13): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+5 more)

### Community 110 - "interview_report.py"
Cohesion: 0.11
Nodes (29): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+21 more)

### Community 111 - "interviews_turn.py"
Cohesion: 0.12
Nodes (32): Condense a long job description once, so later calls send less. One attempt…, Decision, apply_limits(), Deadline, _decision_label(), Interviewer, log_llm_call(), log_llm_error() (+24 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "run_case"
Cohesion: 0.23
Nodes (16): run_case(), long_case(), noted(), reply(), test_a_v3_window_reply_must_carry_a_note_when_there_is_an_answer(), test_an_unusable_summary_falls_back_to_the_original(), test_finish_length_is_recorded_and_counted(), test_main_runs_every_case_n_times_and_prints_the_aggregate() (+8 more)

### Community 115 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 116 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 117 - "interviews_feedback_controller.py"
Cohesion: 0.12
Nodes (29): ConflictError, FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, NotFoundError, RateLimitedError (+21 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "OpenAICompatibleProvider"
Cohesion: 0.09
Nodes (19): OpenAICompatibleProvider, AsyncBaseTransport, Random, ReasoningEffort, Same request with `stream: true`: chunks as they arrive, then the final…, How long to wait before retrying, or None to give up., BaseTransport, Affected Files & Patterns (+11 more)

### Community 121 - "llm"
Cohesion: 0.20
Nodes (8): as_v5_text(), llm(), script(), script_score(), script_write(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY…

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): 5. What can go wrong, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 124 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Testing Strategy (+1 more)

### Community 125 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 126 - ".write"
Cohesion: 0.18
Nodes (14): At most two attempts of the write call only. Failing is fine: the template…, 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+6 more)

### Community 127 - "clock"
Cohesion: 0.20
Nodes (5): _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

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

### Community 134 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 135 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "fake.py"
Cohesion: 0.12
Nodes (13): anyio, FakeTranscriber, Test doubles for LLMProvider and Transcriber: scripted replies or errors,…, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, Protocol, The speech-to-text contract features code against, separate from the text-only…, What the vendor heard. `text` may be blank (silence); the caller decides what… (+5 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "Clock"
Cohesion: 0.33
Nodes (3): anyio_backend(), Clock, fixture

### Community 142 - "test_create_admin.py"
Cohesion: 0.22
Nodes (11): main(), Session, Create the first admin, or promote an existing user to admin. Usage: uv run…, argparse, getpass, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting() (+3 more)

### Community 143 - "QuestionCategory"
Cohesion: 0.29
Nodes (14): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, test_the_rubric_anchors_five_levels_for_every_criterion_and_both_level_groups(), pick(), parametrize, test_a_one_entry_pool_still_works(), test_every_category_and_level_group_has_a_pool() (+6 more)

### Community 144 - "PageParams"
Cohesion: 0.07
Nodes (29): page_params(), PageParams, NamedTuple, Query, Architecture & Design, Blockers & Resolutions, Implementation Plan: Interview History List (backend), Overview (+21 more)

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

### Community 150 - "Implementation Steps"
Cohesion: 0.16
Nodes (13): compute_overall(), The mean of every criterion score of every main question, rounded half up to…, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open (+5 more)

### Community 152 - "test_feedback_context.py"
Cohesion: 0.22
Nodes (20): estimate_tokens(), FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, Step 4 of the feedback plan: what the score and write calls send, through the…, score_inputs() (+12 more)

### Community 154 - "FeedbackCaseResult"
Cohesion: 0.22
Nodes (12): criterion_spread(), feedback_hints_for(), feedback_trace_output(), FeedbackCaseResult, _print_case(), Per case: the largest gap between the highest and lowest score any one…, Where to look first for each failed check (or the error), in the order the…, What came out next to what was wanted: the verdict, the overall against its… (+4 more)

### Community 155 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 157 - "._run"
Cohesion: 0.29
Nodes (9): _Claim, _Interview, _Outcome, Any, NamedTuple, Too little to assess (the code's pre-check, or the model's flag): final, with…, The interview as plain values, read before the claim's commit expires the…, How a generation ended, for the trace (metadata only). (+1 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (14): 9. Review gate (user), Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions (+6 more)

### Community 159 - "run_feedback"
Cohesion: 0.23
Nodes (12): feedback_dataset_items(), feedback_trace_input(), FeedbackEvalCase, load_feedback_cases(), Any, Namespace, Path, The cases as dataset items: the interview as input, the bands as the expected… (+4 more)

### Community 160 - "The fundamentals"
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+17 more)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Decisions (grilled with the user), Implementation Plan: Eval runs in Langfuse (scores + datasets), Overview, Plan-defined criteria, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 162 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 163 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 164 - "WriteText"
Cohesion: 0.24
Nodes (9): _check_lengths(), parse_write_reply(), The labelled text the write call is asked for (the parser reads it back…, The write call's text, slot by slot: every section once and in order, list…, _slots(), WriteText, test_a_valid_write_reply_is_parsed_into_slots(), test_blank_lines_and_a_wrapped_summary_are_accepted() (+1 more)

### Community 165 - "ErrorResponse"
Cohesion: 0.05
Nodes (46): ErrorResponse, BaseModel, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied (+38 more)

### Community 167 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 168 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "StreamedTurn"
Cohesion: 0.25
Nodes (6): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

### Community 170 - "Affected Files & Patterns"
Cohesion: 0.33
Nodes (5): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns

### Community 171 - "failed"
Cohesion: 0.06
Nodes (42): Check, check_decision(), check_reply(), check_streamed_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format., The decide reply against the case's label; the injection check reads the raw… (+34 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.33
Nodes (7): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 174 - "usage_report.py"
Cohesion: 0.43
Nodes (5): main(), Session, Print stored LLM usage per interview: tokens per question position and per…, test_an_empty_database(), test_reports_stored_questions_grouped_by_interview()

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "FeedbackThread"
Cohesion: 0.50
Nodes (4): FeedbackThread, NamedTuple, One main question with its follow-ups and every answer: what one set of scores…, ThreadTurn

### Community 178 - "stream_answer"
Cohesion: 0.40
Nodes (5): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream()

## Knowledge Gaps
- **550 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+545 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1332 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **23 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `InterviewQuestion` connect `InterviewQuestion` to `interviews_utils.py`, `Implementation Steps`, `test_select_questions.py`, `interviews_context.py`, `test_feedback_endpoint.py`, `test_answer_stream.py`, `QuestionTurn`, `test_answer_guards.py`, `test_answer_llm.py`, `test_list_interviews.py`, `test_transcript.py`, `usage_report.py`, `interviews_model.py`, `test_turn_budget.py`, `test_interview_report.py`, `interviews_report.py`, `LLMResult`, `test_create_interview.py`, `interviews_controller.py`, `build_usage_report`, `test_feedback_contract.py`, `test_start_llm.py`, `ContextManager`, `interviews_feedback.py`, `interviews_feedback_controller.py`, `test_follow_ups.py`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `test_tracing_routes.py`, `test_feedback_evals.py`, `interviews_dependencies.py`, `fake.py`, `test_tracing_lifespan.py`, `test_feedback_endpoint.py`, `LLMProvider`, `run_feedback`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `interviews_feedback_evals.py`, `test_evals.py`, `TracingProvider`, `LLMResult`, `ChatMessage`, `interviews_controller.py`, `Any`, `RecordingClient`, `.trace`, `Implementation: Langfuse Tracing`, `main.py`, `RecordingClient`, `interviews_evals.py`, `interviews_feedback_controller.py`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `test_feedback_evals.py`, `fake.py`, `interviews_context.py`, `._run`, `LLMProvider`, `test_answer_llm.py`, `Tracer`, `interviews_feedback_evals.py`, `LLMServerError`, `test_turn_budget.py`, `test_evals.py`, `test_openai_compatible_stream.py`, `TracingProvider`, `ChatMessage`, `interviews_controller.py`, `Any`, `test_start_llm.py`, `test_job_description_summary.py`, `Implementation Steps`, `main.py`, `interviews_evals.py`, `interviews_turn.py`, `run_case`, `interviews_feedback_controller.py`, `OpenAICompatibleProvider`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 63 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 63 INFERRED edges - model-reasoned connections that need verification._
- **Are the 32 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 32 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 29 INFERRED edges - model-reasoned connections that need verification._