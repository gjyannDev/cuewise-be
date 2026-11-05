# Graph Report - cuewise-be  (2026-11-05)

## Corpus Check
- 210 files · ~179,178 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 2994 nodes · 7738 edges · 155 communities (141 shown, 14 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1364 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0d936164`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- LLMServerError
- test_tracing_routes.py
- config.py
- exception_handlers.py
- interviews_dependencies.py
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- JobRole
- Implementation Steps
- tests/conftest.py
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
- interviews_turn.py
- interviews_utils.py
- test_start_llm.py
- Implementation Steps
- test_answer_stream.py
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- InterviewMessage
- Feature: LLM as the Interviewer (it asks the questions)
- Bundle
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- test_list_interviews.py
- test_transcript.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- typing
- ContextManager
- .record_turn
- test_turn_budget.py
- test_evals.py
- InterviewerInputs
- test_interview_report.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- AppError
- LLMError
- InterviewQuestion
- Implementation Plan: Role-Based Access Control (single JWT)
- job_description_summary_v2.md
- test_create_interview.py
- test_stream_answer.py
- interviews_model.py
- pytest
- interviews_controller.py
- LLMResult
- build_usage_report
- test_context.py
- test_reply_contract.py
- interviews_context.py
- test_guards.py
- RecordingClient
- Feature: Start an Interview (backend)
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- uuid
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_transcribe.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- _safe
- test_context_controller.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- Tracer
- QuestionCategory
- Langfuse Observability
- interviewer_v3.md
- fixture
- no_llm_env
- Implementation: Langfuse Tracing
- json
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- main.py
- require_permissions
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- StreamedTurn
- interview_report.py
- Langfuse CLI Reference
- Feature: Langfuse Tracing
- Langfuse
- Learnings: SSE Streaming of the Interview Turn (Slice 4)
- context.py
- Role
- Implementation Plan: Start an Interview (backend)
- Langfuse Implementation Notes
- interviewer_v5.md
- Implementation Plan: Langfuse Tracing
- llm
- Implementation Plan: UUID primary keys
- test_follow_ups.py
- RateLimiter
- test_answer_interview.py
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- clock
- Langfuse Dataset Construction
- Langfuse v4 project migration
- Langfuse
- traces
- Judge Calibration
- Langfuse Prompt Migration
- Feature: Follow-up Questions (decide / write split)
- limit_transcriptions
- Langfuse CI/CD
- Prompt Engineering
- TranscriptionResult
- Langfuse Implementation Notes
- Learnings: LLM Slice 1 (Interviewer Reaction)
- Implementation: Interview History List (backend)
- 2. Langfuse Documentation
- Feature: Interview History List (backend)
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- started
- stream_answer
- build_tracer
- _reset_request_id

## God Nodes (most connected - your core abstractions)
1. `InterviewsController` - 90 edges
2. `FakeProvider` - 87 edges
3. `InterviewQuestion` - 73 edges
4. `LLMResult` - 64 edges
5. `InterviewSession` - 62 edges
6. `User` - 60 edges
7. `QuestionCategory` - 59 edges
8. `InterviewType` - 56 edges
9. `ChatMessage` - 54 edges
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

## Communities (155 total, 14 thin omitted)

### Community 0 - "User"
Cohesion: 0.09
Nodes (24): verify_password(), get_controller(), Depends, Session, User, AuthRepository, Session, UUID (+16 more)

### Community 1 - "LLMServerError"
Cohesion: 0.10
Nodes (25): _parse(), Response, The first channel's best transcript (blank for silence) and the reported audio…, _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, Random (+17 more)

### Community 3 - "config.py"
Cohesion: 0.13
Nodes (28): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Implementation Steps (+20 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "interviews_dependencies.py"
Cohesion: 0.11
Nodes (29): Protocol, The speech-to-text contract features code against, separate from the text-only…, Transcriber, get_bank(), get_clock(), get_controller(), get_llm_provider(), get_tracer() (+21 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.12
Nodes (36): NotEnoughQuestionsError, InterviewType, pick_fallback_question(), One unused bank question for `position`, used when the LLM is off or its reply…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Collection, Deviations from Plan (+28 more)

### Community 8 - "users_route.py"
Cohesion: 0.07
Nodes (36): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, get_db() (+28 more)

### Community 9 - "JobRole"
Cohesion: 0.09
Nodes (43): JobRole, Level, EvalSetup, job_description_block(), load_prompt(), Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the…, Per-interview constants only, so the text is identical on every call of an… (+35 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.17
Nodes (24): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect, The label for the decide call: the action it should pick, and the gap when only…, Decision, parse_decision_reply() (+16 more)

### Community 11 - "tests/conftest.py"
Cohesion: 0.07
Nodes (43): alias, health_check(), answer_question(), answer_question_stream(), get_interview(), get_transcript(), list_interviews(), interviews_answer (+35 more)

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
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - "QuestionTurn"
Cohesion: 0.14
Nodes (18): An earlier question as the model would have written it. A follow-up was written…, End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Answered questions with their answers (and the model's note on each), in… (+10 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.15
Nodes (33): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, StrEnum, The next chunk of the question being written (shown as it arrives)., What the turn ends with, after the limits: the model can only ask for the first…, TurnAction (+25 more)

### Community 28 - "interviews_turn.py"
Cohesion: 0.15
Nodes (16): ActionKnown, _decision_label(), Draft, log_stream_summary(), PhaseChanged, NamedTuple, One answer turn of the LLM interviewer: decide (follow up or move on), apply…, The turn's final action, sent only once nothing can change it (a follow-up only… (+8 more)

### Community 29 - "interviews_utils.py"
Cohesion: 0.08
Nodes (44): AudioContainer, HistorySortColumn, MessageKind, MessageRole, StrEnum, QuestionSource, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, The history columns GET /interviews sorts by; the values are the response's… (+36 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.05
Nodes (47): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, RequestIdFilter, setup_logging(), split_fields(), contextvars, Baseline Failures (+39 more)

### Community 31 - "Implementation Steps"
Cohesion: 0.14
Nodes (15): The question text streamed so far is taken back: that draft failed, another one…, The same turn as `answer_turn` (same decide, limits and fallbacks), telling the…, Reset, Implementation Steps, Phase A: plumbing and progress events, Phase B: streaming the question text, Step 13: The streamed write step in `stream_turn`, Step 14: The event loop stays free (+7 more)

### Community 32 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (18): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+10 more)

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
Cohesion: 0.07
Nodes (27): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+19 more)

### Community 37 - "InterviewMessage"
Cohesion: 0.11
Nodes (20): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, sqlalchemy_exc, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started() (+12 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.11
Nodes (19): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+11 more)

### Community 39 - "Bundle"
Cohesion: 0.11
Nodes (21): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+13 more)

### Community 40 - "test_context_strategies.py"
Cohesion: 0.16
Nodes (37): Checkpoint C: what a follow-up costs in context (concept 2), decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+29 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (32): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+24 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.11
Nodes (23): Learning Log (`learnings.md`), Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions(), Answer every question of a started interview; returns the list of answer… (+15 more)

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
Cohesion: 0.14
Nodes (18): client(), drain(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage() (+10 more)

### Community 49 - "typing"
Cohesion: 0.17
Nodes (19): ConflictError, InvalidCredentialsError, hash_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., login(), AuthControllerDep, post (+11 more)

### Community 50 - "ContextManager"
Cohesion: 0.22
Nodes (16): ContextManager, Task, build_context_manager(), `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WindowLedger, get_context_manager(), Decides what each LLM call sends; tests swap in one with a tiny limit., test_a_second_task_with_its_own_strategy_leaves_the_first_alone() (+8 more)

### Community 51 - ".record_turn"
Cohesion: 0.18
Nodes (11): Save one whole turn in one commit: advance the session, the answer, the…, Affected Files & Patterns, Deviations Found During Implementation, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.22
Nodes (14): Testing Strategy, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start() (+6 more)

### Community 53 - "test_evals.py"
Cohesion: 0.08
Nodes (74): FakeProvider, check_decision(), load_cases(), Path, The decide reply against the case's label; the injection check reads the raw…, run_case(), decision(), failed() (+66 more)

### Community 54 - "InterviewerInputs"
Cohesion: 0.15
Nodes (20): InterviewerInputs, NamedTuple, Plain values for one interviewer or decide call., Deadline, Interviewer, _log_error(), log_llm_call(), log_result() (+12 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.11
Nodes (62): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, analysis(), answer(), emit_answer_turn(), emit_call() (+54 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (26): LLMRateLimitError, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok() (+18 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.10
Nodes (45): analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), _call_table(), _cost(), _counts(), _dash() (+37 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "AppError"
Cohesion: 0.08
Nodes (30): AppError, BadRequestError, ErrorBody, ErrorResponse, Any, BaseModel, Exception, Base for expected errors. Controllers raise these instead of HTTPException. (+22 more)

### Community 60 - "LLMError"
Cohesion: 0.10
Nodes (21): anyio, DeepgramTranscriber, AsyncBaseTransport, Random, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Test doubles for LLMProvider and Transcriber: scripted replies or errors,…, LLMError, LLMRequestError (+13 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.11
Nodes (22): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter(), _history_order(), InterviewsRepository, Session, UUID (+14 more)

### Community 62 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.22
Nodes (8): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Trade-offs & Rationale

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
Nodes (11): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, Print stored LLM usage per interview: tokens per question position and per… (+3 more)

### Community 67 - "pytest"
Cohesion: 0.05
Nodes (29): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), fixture, parametrize (+21 more)

### Community 68 - "interviews_controller.py"
Cohesion: 0.06
Nodes (69): AudioTooLargeError, AudioTooLongError, NoSpeechError, NotFoundError, QuestionNotCurrentError, SessionNotInProgressError, TranscriptionUnavailableError, UnsupportedAudioError (+61 more)

### Community 71 - "LLMResult"
Cohesion: 0.09
Nodes (23): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, LLMProvider, LLMResult, BaseModel, Protocol, ReasoningEffort (+15 more)

### Community 72 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 73 - "test_context.py"
Cohesion: 0.18
Nodes (14): Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default(), test_a_strategy_without_a_limit_is_never_trimmed() (+6 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.16
Nodes (26): Checkpoint B: a small closed decision instead of free text (concept 4), Checkpoint D: labelled evals for a decision (concept 10), Checkpoint E: one deadline for two calls (concept 9), Learnings: Follow-up Questions (decide / write split), follow_up(), parse(), parametrize, reply() (+18 more)

### Community 75 - "interviews_context.py"
Cohesion: 0.15
Nodes (15): QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that…, _counts(), FullHistory, JobDescriptionSummary, What the interview LLM calls send: the tasks and strategies registered with the…, App data at the end of the last user message; untrusted parts (questions,…, _status_block() (+7 more)

### Community 76 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 77 - "RecordingClient"
Cohesion: 0.12
Nodes (7): case(), langfuse(), fixture, A Langfuse client stand-in. Entering a trace sets `current_trace`, like the SDK…, RecordingClient, test_a_failed_dataset_upsert_still_scores_the_cases(), test_a_langfuse_outage_does_not_change_the_run()

### Community 78 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Status, Test Cases (+2 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 82 - "uuid"
Cohesion: 0.18
Nodes (12): main(), Session, parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version() (+4 more)

### Community 83 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Decisions (grilled with the user), Implementation Plan: Eval runs in Langfuse (scores + datasets), Overview, Plan-defined criteria, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 84 - "test_transcribe.py"
Cohesion: 0.14
Nodes (12): code(), parametrize, test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long(), test_a_session_not_in_progress_is_409(), test_an_empty_file_is_no_speech(), test_every_vendor_failure_is_a_generic_503() (+4 more)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Acceptance Criteria, Blockers, Constraints, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 87 - "_safe"
Cohesion: 0.12
Nodes (17): AbstractContextManager, Any, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Run an SDK call; on any failure log what failed (not why: the message could…, _safe() (+9 more)

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

### Community 92 - "Tracer"
Cohesion: 0.09
Nodes (14): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, FakeObservation, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_disabled_tracer_is_a_pass_through(), test_score_failure_is_swallowed() (+6 more)

### Community 93 - "QuestionCategory"
Cohesion: 0.07
Nodes (57): QuestionCategory, check_streamed_reply(), check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, read(), _streamed_question(), _check_question(), HeaderSplit, InterviewerReply (+49 more)

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
Cohesion: 0.18
Nodes (10): Commit message suggestion, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+2 more)

### Community 99 - "json"
Cohesion: 0.29
Nodes (10): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, json, _entry(), parametrize, test_invalid_bank_raises_clear_error(), test_shipped_bank_covers_every_type_role_and_level() (+2 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.11
Nodes (18): Baseline Failures, Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+10 more)

### Community 103 - "main.py"
Cohesion: 0.10
Nodes (28): build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Settings, lifespan(), FastAPI, BaseSettings (+20 more)

### Community 104 - "require_permissions"
Cohesion: 0.05
Nodes (50): ForbiddenError, TokenMissingError, get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check() (+42 more)

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
Nodes (59): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_reply(), dataset_items() (+51 more)

### Community 109 - "StreamedTurn"
Cohesion: 0.25
Nodes (6): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

### Community 110 - "interview_report.py"
Cohesion: 0.15
Nodes (19): html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+11 more)

### Community 111 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional (+6 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "Learnings: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (9): Checkpoint A: what the candidate waits for, Checkpoint B: streaming vs structured output, Checkpoint C: what a dropped stream leaves behind, Learnings: SSE Streaming of the Interview Turn (Slice 4), Proof (concept 7), Still open, anyio, test_other_requests_are_served_while_a_stream_waits_on_the_llm() (+1 more)

### Community 115 - "context.py"
Cohesion: 0.14
Nodes (16): BuiltContext, ContextReport, ContextTooLargeError, estimate_tokens(), _log(), Any, Exception, NamedTuple (+8 more)

### Community 116 - "Role"
Cohesion: 0.13
Nodes (16): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry(), test_unknown_role_has_no_permissions_and_is_logged() (+8 more)

### Community 117 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 121 - "llm"
Cohesion: 0.24
Nodes (6): as_v5_text(), llm(), script(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY…

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): Checkpoint A: the model suggests, the code enforces (concept 5), answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 124 - "RateLimiter"
Cohesion: 0.20
Nodes (11): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, math, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window() (+3 more)

### Community 125 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 126 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 127 - "clock"
Cohesion: 0.20
Nodes (5): _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 131 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 134 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 135 - "limit_transcriptions"
Cohesion: 0.33
Nodes (6): RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., limit_transcriptions(), Depends, interviews_answer, Per-user cap on transcriptions, checked before the upload goes anywhere that…

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

### Community 140 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 142 - "Implementation: Interview History List (backend)"
Cohesion: 0.15
Nodes (12): Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 143 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 144 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

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

### Community 150 - "started"
Cohesion: 0.67
Nodes (3): fixture, An owner with a started backend interview: (owner, session_id)., started()

### Community 155 - "stream_answer"
Cohesion: 0.40
Nodes (5): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream()

### Community 156 - "build_tracer"
Cohesion: 0.47
Nodes (6): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

## Knowledge Gaps
- **489 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+484 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1156 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `Implementation: Eval runs in Langfuse (scores + datasets)`, `test_tracing_routes.py`, `interviews_controller.py`, `interviews_dependencies.py`, `traces`, `LLMResult`, `main.py`, `interviews_evals.py`, `RecordingClient`, `test_tracing.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `test_tracing_lifespan.py`, `test_evals.py`, `_safe`, `build_tracer`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `test_create_interview.py`, `interviews_model.py`, `config.py`, `interviews_controller.py`, `interviews_dependencies.py`, `limit_transcriptions`, `require_permissions`, `users_route.py`, `tests/conftest.py`, `typing`, `InterviewQuestion`, `Role`, `_safe`, `Implementation Plan: UUID primary keys`, `interviews_utils.py`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `JobRole`, `Implementation Steps`, `QuestionTurn`, `interviews_utils.py`, `test_start_llm.py`, `test_answer_stream.py`, `InterviewMessage`, `Bundle`, `test_answer_llm.py`, `test_list_interviews.py`, `test_transcript.py`, `.record_turn`, `test_turn_budget.py`, `test_interview_report.py`, `interviews_report.py`, `test_create_interview.py`, `interviews_model.py`, `interviews_controller.py`, `build_usage_report`, `interviews_context.py`, `uuid`, `test_context_controller.py`, `test_follow_ups.py`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Are the 63 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 63 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 23 INFERRED edges - model-reasoned connections that need verification._