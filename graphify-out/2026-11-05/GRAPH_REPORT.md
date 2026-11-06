# Graph Report - cuewise-be  (2026-11-05)

## Corpus Check
- 228 files · ~218,557 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 3494 nodes · 9501 edges · 175 communities (162 shown, 13 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1714 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4dfd8d26`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Role
- LLMTimeoutError
- test_tracing_routes.py
- decode_token
- interviews_feedback_evals.py
- interviews_dependencies.py
- Cuewise BE — Project Instructions
- interviews_utils.py
- users_route.py
- JobRole
- interviews_constants.py
- Implementation Plan: Start an Interview (backend)
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- QuestionTurn
- users_utils.py
- README.md
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- test_feedback_endpoint.py
- audio_container
- test_start_llm.py
- Implementation Steps
- test_answer_stream.py
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Implementation: LLM as the Interviewer (it asks the questions)
- LLMProvider
- InterviewMessage
- Feature: LLM as the Interviewer (it asks the questions)
- interviews_schema.py
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- test_list_interviews.py
- test_transcript.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- test_create_admin.py
- interviews_model.py
- LLMServerError
- test_turn_budget.py
- test_evals.py
- Implementation Steps
- test_interview_report.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- interviews_controller.py
- LLMResult
- InterviewQuestion
- interviews_feedback_turn.py
- job_description_summary_v2.md
- test_create_interview.py
- InterviewSession
- typing
- test_request_context.py
- InterviewsController
- tracing.py
- build_usage_report
- ContextManager
- test_reply_contract.py
- test_feedback_contract.py
- test_guards.py
- RecordingClient
- Feature: Start an Interview (backend)
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- test_job_description_summary.py
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_transcribe.py
- auth_controller.py
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- .trace
- test_context_controller.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- Tracer
- InvalidReplyError
- Langfuse Observability
- interviewer_v3.md
- fixture
- no_llm_env
- TracingProvider
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
- StreamedTurn
- main
- interviews_turn.py
- Feature: Langfuse Tracing
- Langfuse
- exception_handlers.py
- Strategy
- pytest
- interviews_feedback_controller.py
- Langfuse Implementation Notes
- interviewer_v5.md
- Implementation Plan: Langfuse Tracing
- llm
- Implementation Plan: UUID primary keys
- test_follow_ups.py
- Implementation Plan: Role-Based Access Control (single JWT)
- test_answer_interview.py
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- clock
- Langfuse Dataset Construction
- Langfuse v4 project migration
- .stream_answer
- Implementation: Interview History List (backend)
- Judge Calibration
- Langfuse Prompt Migration
- Feature: Follow-up Questions (decide / write split)
- Implementation Plan: Context Management for the Interview LLM Calls
- Langfuse CI/CD
- Prompt Engineering
- TranscriptionResult
- Langfuse Implementation Notes
- .stream_turn
- test_question_bank.py
- InterviewerInputs
- Feature: Interview History List (backend)
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- Learn: Streaming and latency (Slice 4, SSE)
- full
- QuestionKind
- failed
- test_keyterms.py
- _reset_request_id
- InterviewType
- interviews_log.py
- The fundamentals
- compute_overall
- test_get_interview.py
- admin
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- OpenAICompatibleProvider
- interviews_context.py
- parse_log
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Feature: Interview Feedback and Scoring (Slice 6)
- test_llm_settings_default_to_off_with_documented_limits
- feedback_score_v1.md
- feedback_write_v1.md
- ProviderConfig
- uuid
- _LostClaim

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

## Communities (175 total, 13 thin omitted)

### Community 0 - "Role"
Cohesion: 0.09
Nodes (25): get_db(), Session, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, get_controller(), Depends (+17 more)

### Community 1 - "LLMTimeoutError"
Cohesion: 0.11
Nodes (15): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, LLMTimeoutError, 1. Why it exists (+7 more)

### Community 2 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 3 - "decode_token"
Cohesion: 0.13
Nodes (27): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Testing Strategy (+19 more)

### Community 4 - "interviews_feedback_evals.py"
Cohesion: 0.05
Nodes (65): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_scores_for() (+57 more)

### Community 5 - "interviews_dependencies.py"
Cohesion: 0.10
Nodes (35): Protocol, Transcriber, Random, get_bank(), get_clock(), get_context_manager(), get_controller(), get_feedback_controller() (+27 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "interviews_utils.py"
Cohesion: 0.08
Nodes (45): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, model_validator, Self, One criterion of the feedback rubric: what it asks, an anchor per score, and…, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric (+37 more)

### Community 8 - "users_route.py"
Cohesion: 0.07
Nodes (34): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, UsersController (+26 more)

### Community 9 - "JobRole"
Cohesion: 0.12
Nodes (36): JobRole, Level, EvalSetup, FeedbackEvalSetup, A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary() (+28 more)

### Community 10 - "interviews_constants.py"
Cohesion: 0.22
Nodes (17): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect, The label for the decide call: the action it should pick, and the gap when only…, parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time… (+9 more)

### Community 11 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.06
Nodes (36): RequestIdFilter, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions (+28 more)

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

### Community 16 - "QuestionTurn"
Cohesion: 0.10
Nodes (30): An earlier question as the model would have written it. A follow-up was written…, End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,… (+22 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.15
Nodes (35): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, Delta, StrEnum, The next chunk of the question being written (shown as it arrives). (+27 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.05
Nodes (84): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted… (+76 more)

### Community 29 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.06
Nodes (39): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, setup_logging(), split_fields(), Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp (+31 more)

### Community 31 - "Implementation Steps"
Cohesion: 0.11
Nodes (17): Blockers & Resolutions, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps, Overview, Phase A: plumbing and progress events, Phase B: streaming the question text, Project Rules Applied, Ready to Implement (+9 more)

### Community 32 - "test_answer_stream.py"
Cohesion: 0.06
Nodes (31): 6. Try it yourself, auth_header(), _header(), client(), fixture, Bearer header for a user; pass role to mint a token whose role claim differs…, assert_one_terminal(), follow_up_json() (+23 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.18
Nodes (10): Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+2 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "LLMProvider"
Cohesion: 0.11
Nodes (18): LLMProvider, Protocol, Build order: "Chat with the interviewer", Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming (+10 more)

### Community 37 - "InterviewMessage"
Cohesion: 0.12
Nodes (18): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409() (+10 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (22): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+14 more)

### Community 39 - "interviews_schema.py"
Cohesion: 0.09
Nodes (39): HistorySortColumn, MessageKind, MessageRole, StrEnum, QuestionSource, The history columns GET /interviews sorts by; the values are the response's…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Transcript item kinds: a question comes from interview_questions, the other two… (+31 more)

### Community 40 - "test_context_strategies.py"
Cohesion: 0.18
Nodes (35): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., decide(), fu(), inputs(), Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+27 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.13
Nodes (31): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+23 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.11
Nodes (23): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages() (+15 more)

### Community 45 - "test_list_interviews.py"
Cohesion: 0.10
Nodes (36): answered(), history(), ids_of(), fixture, parametrize, GET /api/v1/interviews: the candidate's interview history, newest first,…, Start `n` interviews in a row; returns their ids newest first (each start…, Five sessions stored directly (oldest first), with values that sort differently… (+28 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.25
Nodes (12): fixture, shape(), started(), test_a_follow_up_is_shown_with_its_kind_and_its_main_questions_number(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question() (+4 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.10
Nodes (25): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, client(), drain(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result() (+17 more)

### Community 49 - "test_create_admin.py"
Cohesion: 0.24
Nodes (11): main(), Session, Create the first admin, or promote an existing user to admin. Usage: uv run…, argparse, getpass, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting() (+3 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.12
Nodes (24): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, health_check() (+16 more)

### Community 51 - "LLMServerError"
Cohesion: 0.11
Nodes (27): anyio, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Test doubles for LLMProvider and Transcriber: scripted replies or errors,…, AsyncBaseTransport, Random, OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, LLMError, LLMRateLimitError (+19 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.22
Nodes (14): Testing Strategy, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start() (+6 more)

### Community 53 - "test_evals.py"
Cohesion: 0.09
Nodes (67): FakeProvider, load_cases(), Path, run_case(), contextvars, decision(), hints_of(), labelled() (+59 more)

### Community 54 - "Implementation Steps"
Cohesion: 0.13
Nodes (24): Decision, Save one whole turn in one commit: advance the session, the answer, the…, apply_limits(), Deadline, The code's say over the model's: returns the action and why it overrode the…, After the decision: the code's limits pick the action, and whether a write call…, The write's result decides the outcome: a failed follow-up moves on, and the…, The turn's LLM time budget, set once and asked by every call (an injectable… (+16 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.14
Nodes (50): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start() (+42 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (27): LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider() (+19 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.09
Nodes (55): group_requests(), LogEvent, The events of each request, oldest request first (the id is on every line of…, analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle (+47 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "interviews_controller.py"
Cohesion: 0.09
Nodes (38): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody, ErrorResponse, NoSpeechError (+30 more)

### Community 60 - "LLMResult"
Cohesion: 0.10
Nodes (23): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, LLMResult, BaseModel, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, One turn of the conversation sent to the model. The model keeps no memory:… (+15 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.08
Nodes (25): InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter(), InterviewsRepository, Any, datetime, Session, UUID (+17 more)

### Community 62 - "interviews_feedback_turn.py"
Cohesion: 0.11
Nodes (22): BuiltContext, ContextReport, _log(), NamedTuple, Context management: the one place that decides what each LLM call sends. The…, _Attempts, CallUsage, FeedbackGenerator (+14 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 65 - "InterviewSession"
Cohesion: 0.14
Nodes (20): InterviewSession, _history_order(), The requested column (its stored value, not the label), then `id desc` so ties…, 5. What can go wrong, test_database_rejects_two_in_progress_sessions_for_one_user(), session_for(), test_answered_count_of_a_session_with_every_question_stored_up_front(), fixture (+12 more)

### Community 66 - "typing"
Cohesion: 0.06
Nodes (8): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column, typing

### Community 67 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 68 - "InterviewsController"
Cohesion: 0.10
Nodes (26): QuestionNotCurrentError, InterviewsController, InterviewSetup, _llm_question(), NamedTuple, UUID, The session fields the interviewer needs, as plain values that survive the end…, The main question the answered question belongs to (itself, or a follow-up's… (+18 more)

### Community 71 - "tracing.py"
Cohesion: 0.10
Nodes (17): AbstractContextManager, Generation, Any, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Set the output of the trace being built (call it inside `trace()`): what a…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the… (+9 more)

### Community 72 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 73 - "ContextManager"
Cohesion: 0.12
Nodes (24): ContextManager, Task, build_context_manager(), `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WindowLedger, Deviations Found During Implementation, Inputs, manager() (+16 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.14
Nodes (29): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split), follow_up() (+21 more)

### Community 75 - "test_feedback_contract.py"
Cohesion: 0.20
Nodes (30): assess_evidence(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The pre-check, before any LLM call: enough main questions have a real answer to…, parametrize, question_json(), The feedback contract (interviews_feedback.py): the code pre-check, the score…, reason_of() (+22 more)

### Community 76 - "test_guards.py"
Cohesion: 0.15
Nodes (17): CurrentUserDep, _assert_401(), authenticated(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access(), test_guards_allow_or_forbid_by_db_role() (+9 more)

### Community 77 - "RecordingClient"
Cohesion: 0.13
Nodes (5): case(), langfuse(), fixture, A Langfuse client stand-in. Entering a trace sets `current_trace`, like the SDK…, RecordingClient

### Community 78 - "Feature: Start an Interview (backend)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Status, Test Cases (+2 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.18
Nodes (10): Blockers & Resolutions, Deviations Found During Implementation, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 83 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.15
Nodes (12): Architecture & Design, Blockers & Resolutions, Decisions (grilled with the user), Implementation Plan: Eval runs in Langfuse (scores + datasets), Overview, Plan-defined criteria, Project Rules Applied, Ready to Implement (+4 more)

### Community 84 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 85 - "auth_controller.py"
Cohesion: 0.17
Nodes (19): InvalidCredentialsError, hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., login(), me(), AuthControllerDep (+11 more)

### Community 86 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 87 - ".trace"
Cohesion: 0.23
Nodes (8): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Deviations from the first version of this plan (found during /implement), Implementation Steps, Completed Steps, tracer()

### Community 88 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "Tracer"
Cohesion: 0.09
Nodes (14): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, FakeObservation, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_makes_no_call_without_a_trace_id_or_when_tracing_is_off() (+6 more)

### Community 93 - "InvalidReplyError"
Cohesion: 0.09
Nodes (40): read(), _streamed_question(), _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, load_object(), _normalized() (+32 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "fixture"
Cohesion: 0.17
Nodes (12): answer(), _answer(), anyio_backend(), fixture, Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a recording to the transcription endpoint; `audio=None` sends no file part…, POST a setup for `user`; any field can be overridden, or dropped by passing…, POST an answer; `question_id` defaults to whatever the caller passes, body… (+4 more)

### Community 97 - "no_llm_env"
Cohesion: 0.33
Nodes (6): no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 98 - "TracingProvider"
Cohesion: 0.11
Nodes (13): TracingProvider, Commit message suggestion, Completed Steps, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 99 - "interviews_feedback.py"
Cohesion: 0.11
Nodes (35): Criterion, What the score call rates, 1 to 5. Which ones apply depends on the question's…, _check_lengths(), Evidence, FeedbackThread, _has_markup(), _normalized(), parse_write_reply() (+27 more)

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
Cohesion: 0.11
Nodes (27): build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, model_validator, Self, Settings, lifespan() (+19 more)

### Community 104 - "User"
Cohesion: 0.12
Nodes (39): alias, ForbiddenError, Permission, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), check(), User (+31 more)

### Community 105 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.07
Nodes (61): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_streamed_reply() (+53 more)

### Community 109 - "StreamedTurn"
Cohesion: 0.17
Nodes (9): Functional, Non-Functional, Requirements, NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json() (+1 more)

### Community 110 - "main"
Cohesion: 0.16
Nodes (18): html_target(), main(), Path, Session, UUID, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines() (+10 more)

### Community 111 - "interviews_turn.py"
Cohesion: 0.17
Nodes (18): _decision_label(), Draft, Interviewer, log_llm_call(), log_llm_error(), log_result(), log_stream_summary(), UUID (+10 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional (+6 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 115 - "Strategy"
Cohesion: 0.40
Nodes (4): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy

### Community 116 - "pytest"
Cohesion: 0.11
Nodes (7): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 117 - "interviews_feedback_controller.py"
Cohesion: 0.13
Nodes (29): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`… (+21 more)

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
Cohesion: 0.16
Nodes (11): as_v5_text(), _decision_json(), llm(), script(), script_decide(), script_score(), script_write(), unique_question() (+3 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "test_follow_ups.py"
Cohesion: 0.27
Nodes (16): answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries(), test_a_failed_follow_up_write_falls_back_to_the_next_main_bank_question() (+8 more)

### Community 124 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.12
Nodes (17): get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, require_roles(), bearer_scheme, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions (+9 more)

### Community 125 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 126 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 127 - "clock"
Cohesion: 0.20
Nodes (5): _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - ".stream_answer"
Cohesion: 0.18
Nodes (16): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, _elapsed_ms(), _error_event(), _event(), BaseModel, The predefined acknowledgement for moving on (or completing). The id is set…, The same turn as `answer`, as events: progress first, then the saved turn in… (+8 more)

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

### Community 135 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "TranscriptionResult"
Cohesion: 0.15
Nodes (10): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank). (+2 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - ".stream_turn"
Cohesion: 0.23
Nodes (11): ActionKnown, PhaseChanged, NamedTuple, The turn's final action, sent only once nothing can change it (a follow-up only…, The question text streamed so far is taken back: that draft failed, another one…, The same turn as `answer_turn` (same decide, limits and fallbacks), telling the…, Reset, Settled (+3 more)

### Community 142 - "test_question_bank.py"
Cohesion: 0.39
Nodes (8): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, _entry(), parametrize, test_invalid_bank_raises_clear_error(), test_shipped_bank_covers_every_type_role_and_level(), test_valid_bank_loads_typed_entries(), _write()

### Community 143 - "InterviewerInputs"
Cohesion: 0.32
Nodes (4): InterviewerInputs, Plain values for one interviewer or decide call., Index of the main question whose thread holds turn `index` (default: the latest…, thread_start()

### Community 144 - "Feature: Interview History List (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

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

### Community 150 - "Learn: Streaming and latency (Slice 4, SSE)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Streaming and latency (Slice 4, SSE)

### Community 151 - "full"
Cohesion: 0.33
Nodes (6): full(), parametrize, test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window(), max_inputs(), test_full_history_equals_todays_payload(), test_full_history_is_never_trimmed_however_large()

### Community 152 - "QuestionKind"
Cohesion: 0.17
Nodes (23): estimate_tokens(), QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that…, FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, ThreadTurn (+15 more)

### Community 154 - "failed"
Cohesion: 0.28
Nodes (9): check_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, Slice 6: Feedback and scoring, failed(), parametrize, test_a_good_reply_passes_every_check(), test_bad_flags_exit_with_the_valid_choices(), test_each_check_catches_its_problem() (+1 more)

### Community 155 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 157 - "InterviewType"
Cohesion: 0.13
Nodes (35): NotEnoughQuestionsError, InterviewType, pick_fallback_question(), One unused bank question for `position`, used when the LLM is off or its reply…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Collection, random (+27 more)

### Community 158 - "interviews_log.py"
Cohesion: 0.07
Nodes (26): Call, _int(), NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer., The requests that logged this session, oldest first: the start, then one…, Turn (+18 more)

### Community 160 - "The fundamentals"
Cohesion: 0.08
Nodes (24): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+16 more)

### Community 161 - "compute_overall"
Cohesion: 0.47
Nodes (6): compute_overall(), The mean of every criterion score of every main question, rounded half up to…, 6. Try it yourself, score(), test_the_overall_is_the_mean_of_every_criterion_score(), test_the_overall_rounds_half_up_to_one_decimal()

### Community 162 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 163 - "admin"
Cohesion: 0.11
Nodes (17): Acceptance Criteria, Project Conventions, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal (+9 more)

### Community 165 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 166 - "OpenAICompatibleProvider"
Cohesion: 0.15
Nodes (13): _int_or_none(), OpenAICompatibleProvider, Any, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final…, How long to wait before retrying, or None to give up., One streamed request: its text chunks, then an LLMResult (attempts and latency… (+5 more)

### Community 167 - "interviews_context.py"
Cohesion: 0.11
Nodes (20): StrategyOutput, _counts(), FeedbackScoreInputs, FeedbackWrite, FeedbackWriteInputs, FollowUpDecision, FullHistory, JobDescriptionSummary (+12 more)

### Community 169 - "parse_log"
Cohesion: 0.26
Nodes (12): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, analysis(), lines_of(), Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis(), session() (+4 more)

### Community 170 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 171 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.29
Nodes (8): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 178 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 181 - "uuid"
Cohesion: 0.53
Nodes (5): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7(), uuid

### Community 184 - "_LostClaim"
Cohesion: 0.67
Nodes (3): _LostClaim, Exception, Another request took the row over while this one ran: this one's writes are…

## Knowledge Gaps
- **541 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+536 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1318 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FakeProvider` connect `test_evals.py` to `Feature: Context Management for the Interview LLM Calls`, `TracingProvider`, `LLMProvider`, `InterviewsController`, `interviews_dependencies.py`, `main.py`, `ContextManager`, `QuestionTurn`, `test_tracing.py`, `LLMServerError`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Implementation Steps`, `.trace`, `llm`, `failed`, `LLMResult`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `test_tracing_routes.py`, `interviews_feedback_evals.py`, `interviews_dependencies.py`, `test_tracing_lifespan.py`, `test_feedback_endpoint.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `test_tracing.py`, `test_evals.py`, `interviews_controller.py`, `LLMResult`, `interviews_feedback_turn.py`, `InterviewsController`, `tracing.py`, `RecordingClient`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `.trace`, `TracingProvider`, `main.py`, `interviews_evals.py`, `interviews_feedback_controller.py`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `interviews_feedback_evals.py`, `JobRole`, `QuestionTurn`, `test_start_llm.py`, `OpenAICompatibleProvider`, `interviews_schema.py`, `test_answer_llm.py`, `test_tracing.py`, `LLMServerError`, `test_turn_budget.py`, `test_evals.py`, `Implementation Steps`, `test_openai_compatible_stream.py`, `interviews_controller.py`, `interviews_feedback_turn.py`, `InterviewsController`, `tracing.py`, `test_job_description_summary.py`, `TracingProvider`, `main.py`, `interviews_evals.py`, `interviews_turn.py`, `Feature: Langfuse Tracing`, `interviews_feedback_controller.py`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Are the 23 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 63 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 63 INFERRED edges - model-reasoned connections that need verification._
- **Are the 32 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 32 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 29 INFERRED edges - model-reasoned connections that need verification._