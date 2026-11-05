# Graph Report - cuewise-be  (2026-11-04)

## Corpus Check
- 210 files · ~177,601 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 2978 nodes · 7670 edges · 161 communities (147 shown, 14 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1345 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0d936164`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- auth_controller.py
- LLMResult
- test_tracing_routes.py
- decode_token
- exception_handlers.py
- get_controller
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- JobRole
- Implementation Steps
- interviews_route.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- test_interviewer_messages.py
- users_utils.py
- README.md
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- .settle
- interviews_controller.py
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
- tests/conftest.py
- ContextManager
- QuestionCategory
- test_turn_budget.py
- test_evals.py
- InterviewerInputs
- test_interview_report.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- errors.py
- interviews_turn.py
- InterviewQuestion
- Implementation Plan: Role-Based Access Control (single JWT)
- job_description_summary_v2.md
- test_create_interview.py
- test_stream_answer.py
- sqlalchemy
- test_get_interview.py
- InterviewsController
- FakeProvider
- interviews_model.py
- test_context.py
- test_reply_contract.py
- interviews_context.py
- test_guards.py
- RecordingClient
- RequestContextMiddleware
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- test_job_description_summary.py
- ConsoleFormatter
- test_transcribe.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_context_controller.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- Tracer
- interviews_reply.py
- Langfuse Observability
- interviewer_v3.md
- fixture
- no_llm_env
- Implementation: Langfuse Tracing
- check_decision
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- main.py
- ErrorResponse
- run_stream_case
- run_case
- Langfuse Dataset Construction
- interviews_evals.py
- StreamedTurn
- interview_report.py
- pytest
- Feature: Langfuse Tracing
- Langfuse
- Learnings: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Steps
- Role
- test_request_context.py
- Langfuse Implementation Notes
- interviewer_v5.md
- Implementation Plan: Langfuse Tracing
- llm
- Implementation Plan: UUID primary keys
- test_follow_ups.py
- RateLimiter
- test_answer_interview.py
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- .__init__
- Langfuse Dataset Construction
- Langfuse v4 project migration
- test_fallback_pick.py
- Generation
- Judge Calibration
- Langfuse Prompt Migration
- follow_up
- FakeObservation
- Langfuse CI/CD
- Prompt Engineering
- DeepgramTranscriber
- Langfuse Implementation Notes
- Learnings: LLM Slice 1 (Interviewer Reaction)
- Implementation: Interview History List (backend)
- test_list_users.py
- Feature: Interview History List (backend)
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- audio_container
- InvalidReplyError
- bank
- test_llm_settings_default_to_off_with_documented_limits
- stream_answer
- build_tracer
- test_keyterms.py
- tracer
- ProviderConfig
- _reset_request_id

## God Nodes (most connected - your core abstractions)
1. `InterviewsController` - 88 edges
2. `FakeProvider` - 87 edges
3. `InterviewQuestion` - 73 edges
4. `LLMResult` - 64 edges
5. `User` - 60 edges
6. `InterviewSession` - 60 edges
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

## Communities (161 total, 14 thin omitted)

### Community 0 - "auth_controller.py"
Cohesion: 0.07
Nodes (28): hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session, AuthRepository (+20 more)

### Community 1 - "LLMResult"
Cohesion: 0.11
Nodes (22): _int_or_none(), OpenAICompatibleProvider, Any, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final…, How long to wait before retrying, or None to give up., One streamed request: its text chunks, then an LLMResult (attempts and latency… (+14 more)

### Community 2 - "test_tracing_routes.py"
Cohesion: 0.13
Nodes (6): get_tracer(), Built once at startup (app lifespan); a disabled tracer when the lifespan…, fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 3 - "decode_token"
Cohesion: 0.14
Nodes (25): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Testing Strategy, Implementation Steps (+17 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "get_controller"
Cohesion: 0.05
Nodes (44): Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, get_bank(), get_clock(), get_controller(), get_llm_provider(), get_transcriber() (+36 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.09
Nodes (41): NotEnoughQuestionsError, InterviewType, Random, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), load_bank(), Path (+33 more)

### Community 8 - "users_route.py"
Cohesion: 0.08
Nodes (34): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, UsersController (+26 more)

### Community 9 - "JobRole"
Cohesion: 0.11
Nodes (31): JobRole, Level, EvalSetup, load_prompt(), Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt(), render_interviewer_v2_prompt() (+23 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.19
Nodes (22): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect, The label for the decide call: the action it should pick, and the gap when only…, Decision, parse_decision_reply() (+14 more)

### Community 11 - "interviews_route.py"
Cohesion: 0.11
Nodes (35): alias, answer_question(), answer_question_stream(), get_interview(), get_transcript(), list_interviews(), interviews_answer, PageDep (+27 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_config.py"
Cohesion: 0.14
Nodes (25): _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored(), test_api_key_never_shows_in_repr_or_errors() (+17 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.09
Nodes (29): anyio_backend(), Clock, listen_body(), make_transcriber(), _make(), ok(), fixture, parametrize (+21 more)

### Community 16 - "test_interviewer_messages.py"
Cohesion: 0.10
Nodes (32): build_interviewer_messages(), interviewer_history(), job_description_block(), Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't…, Answered questions with their answers (and the model's note on each), in…, The full input for one call (the model has no memory, so the whole interview is… (+24 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.16
Nodes (31): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, StrEnum, What the turn ends with, after the limits: the model can only ask for the first…, TurnAction, collect(), follow_up_json() (+23 more)

### Community 28 - ".settle"
Cohesion: 0.12
Nodes (24): End the read transaction before a slow call, so no connection sits idle in a…, ActionKnown, _decision_label(), Delta, PhaseChanged, NamedTuple, The turn's final action, sent only once nothing can change it (a follow-up only…, The next chunk of the question being written (shown as it arrives). (+16 more)

### Community 29 - "interviews_controller.py"
Cohesion: 0.09
Nodes (47): MessageKind, MessageRole, StrEnum, QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, A main question opens a thread; a follow-up digs into the latest answer of that…, Transcript item kinds: a question comes from interview_questions, the other two… (+39 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 31 - "Implementation Steps"
Cohesion: 0.12
Nodes (16): Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps, Overview, Phase A: plumbing and progress events, Phase B: streaming the question text, Project Rules Applied, Ready to Implement, Skills Consulted (+8 more)

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

### Community 37 - "InterviewMessage"
Cohesion: 0.10
Nodes (23): Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, Project Conventions, Project Rules Applied, Project Rules Applied, message_count() (+15 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "Bundle"
Cohesion: 0.11
Nodes (21): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+13 more)

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
Cohesion: 0.14
Nodes (32): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+24 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.13
Nodes (19): Checkpoint A: after Step 3 (provider package), Learning Log (`learnings.md`), Known Follow-ups (story 3: Chat with the interviewer), messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview(), test_a_double_submit_stores_one_answer_and_makes_one_call() (+11 more)

### Community 45 - "test_list_interviews.py"
Cohesion: 0.13
Nodes (24): answered(), history(), fixture, parametrize, GET /api/v1/interviews: the candidate's interview history, newest first,…, Start `n` interviews in a row; returns their ids newest first (each start…, One interview of each status, started in this order: completed, then abandoned,…, started_ids() (+16 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.16
Nodes (15): drain(), Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage(), test_failed_call_is_marked_error_and_the_same_exception_is_raised(), test_missing_usage_is_omitted_never_guessed(), test_retried_call_is_one_generation_with_attempts() (+7 more)

### Community 49 - "tests/conftest.py"
Cohesion: 0.06
Nodes (44): RequestIdFilter, get_db(), Session, health_check(), Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling (+36 more)

### Community 50 - "ContextManager"
Cohesion: 0.16
Nodes (20): ContextManager, Task, build_context_manager(), JobDescriptionSummary, NamedTuple, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, SummaryInputs, WindowLedger (+12 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.15
Nodes (26): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), A predefined, neutral acknowledgement for the answer just given; never the same…, pick(), parametrize, test_a_one_entry_pool_still_works() (+18 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 53 - "test_evals.py"
Cohesion: 0.14
Nodes (38): load_cases(), Path, decision(), hints_of(), mentions(), noted(), run_main(), test_a_case_without_an_answer_yet_shows_only_its_kind_and_job_description() (+30 more)

### Community 54 - "InterviewerInputs"
Cohesion: 0.17
Nodes (17): InterviewerInputs, Plain values for one interviewer or decide call., Condense a long job description once, so later calls send less. One attempt…, Deadline, Interviewer, _log_error(), log_llm_call(), log_result() (+9 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.11
Nodes (62): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, analysis(), answer(), emit_answer_turn(), emit_call() (+54 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (26): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), _make(), ok() (+18 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.10
Nodes (45): analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), _call_table(), _cost(), _counts(), _dash() (+37 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "errors.py"
Cohesion: 0.15
Nodes (22): AppError, BadRequestError, ConflictError, ErrorBody, InvalidCredentialsError, NotFoundError, Any, BaseModel (+14 more)

### Community 60 - "interviews_turn.py"
Cohesion: 0.10
Nodes (34): anyio, Context management: the one place that decides what each LLM call sends. The…, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Test doubles for LLMProvider and Transcriber: scripted replies or errors,…, OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, LLMError, LLMRateLimitError, LLMRequestError (+26 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.11
Nodes (19): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter(), InterviewsRepository, Session, UUID, Any user's session, by id: for the report script only (the API always goes… (+11 more)

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

### Community 66 - "sqlalchemy"
Cohesion: 0.07
Nodes (9): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, DeclarativeBase, fastapi_security, sqlalchemy (+1 more)

### Community 67 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 68 - "InterviewsController"
Cohesion: 0.09
Nodes (33): AudioTooLargeError, AudioTooLongError, NoSpeechError, QuestionNotCurrentError, SessionNotInProgressError, TranscriptionUnavailableError, UnsupportedAudioError, User (+25 more)

### Community 71 - "FakeProvider"
Cohesion: 0.07
Nodes (28): estimate_tokens(), FakeProvider, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, LLMProvider, BaseModel, Protocol (+20 more)

### Community 72 - "interviews_model.py"
Cohesion: 0.18
Nodes (17): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, main(), Session, Print stored LLM usage per interview: tokens per question position and per…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind() (+9 more)

### Community 73 - "test_context.py"
Cohesion: 0.15
Nodes (17): StrategyOutput, FullHistory, Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub (+9 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 75 - "interviews_context.py"
Cohesion: 0.16
Nodes (16): _counts(), FollowUpDecision, What the interview LLM calls send: the tasks and strategies registered with the…, An earlier question as the model would have written it. A follow-up was written…, The decide call: the current thread in full (it judges the latest answer within…, App data at the end of the last user message; untrusted parts (questions,…, _status_block(), main_numbers() (+8 more)

### Community 76 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 77 - "RecordingClient"
Cohesion: 0.12
Nodes (7): case(), langfuse(), fixture, A Langfuse client stand-in. Entering a trace sets `current_trace`, like the SDK…, RecordingClient, test_a_failed_dataset_upsert_still_scores_the_cases(), test_a_langfuse_outage_does_not_change_the_run()

### Community 78 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Status, Test Cases (+2 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.12
Nodes (15): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split) (+7 more)

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 83 - "ConsoleFormatter"
Cohesion: 0.18
Nodes (14): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), LogRecord, sys, _record(), test_console_appends_the_traceback() (+6 more)

### Community 84 - "test_transcribe.py"
Cohesion: 0.11
Nodes (17): Acceptance Criteria, Functional, code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech() (+9 more)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 87 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.10
Nodes (21): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Run an SDK call; on any failure log what failed (not why: the message could…, _safe(), decorate(), Affected Files & Patterns, Architecture & Design (+13 more)

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
Cohesion: 0.12
Nodes (13): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_disabled_tracer_is_a_pass_through(), test_score_failure_is_swallowed(), test_score_makes_no_call_without_a_trace_id_or_when_tracing_is_off() (+5 more)

### Community 93 - "interviews_reply.py"
Cohesion: 0.14
Nodes (21): _check_question(), HeaderSplit, InterviewerReply, _load_object(), _normalized(), parse_interviewer_reply(), parse_streamed_reply(), BaseModel (+13 more)

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

### Community 99 - "check_decision"
Cohesion: 0.25
Nodes (11): check_decision(), The decide reply against the case's label; the injection check reads the raw…, failed(), labelled(), parametrize, test_an_injected_marker_in_the_decision_fails_the_case(), test_bad_flags_exit_with_the_valid_choices(), test_check_decision_compares_against_the_label() (+3 more)

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
Cohesion: 0.09
Nodes (31): build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Settings, setup_logging(), lifespan(), FastAPI (+23 more)

### Community 104 - "ErrorResponse"
Cohesion: 0.04
Nodes (55): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+47 more)

### Community 105 - "run_stream_case"
Cohesion: 0.15
Nodes (20): _add_usage(), _case_inputs(), CaseResult, ReasoningEffort, One decide call on the case's latest answer, as the app makes it after every…, The streamed turn's write call (interviewer_stream, v5) on one case: the same…, The write call's inputs for a case, with the job description condensed first…, One line a reader can scan in Langfuse: PASS, FAIL with each failed check and… (+12 more)

### Community 106 - "run_case"
Cohesion: 0.21
Nodes (12): run_case(), long_case(), reply(), test_a_failed_check_is_scored_false_with_its_detail(), test_a_good_reply_passes_every_check(), test_a_v3_window_reply_must_carry_a_note_when_there_is_an_answer(), test_an_unusable_summary_falls_back_to_the_original(), test_no_note_check_for_full_history_or_the_first_question() (+4 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.09
Nodes (42): anyio_from_thread, _action_and_gap(), Check, check_reply(), check_streamed_reply(), dataset_items(), dataset_name(), DecisionSummary (+34 more)

### Community 109 - "StreamedTurn"
Cohesion: 0.25
Nodes (6): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

### Community 110 - "interview_report.py"
Cohesion: 0.15
Nodes (19): html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+11 more)

### Community 111 - "pytest"
Cohesion: 0.29
Nodes (4): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "Learnings: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (9): Checkpoint A: what the candidate waits for, Checkpoint B: streaming vs structured output, Checkpoint C: what a dropped stream leaves behind, Learnings: SSE Streaming of the Interview Turn (Slice 4), Proof (concept 7), Still open, anyio, test_other_requests_are_served_while_a_stream_waits_on_the_llm() (+1 more)

### Community 115 - "Implementation Steps"
Cohesion: 0.16
Nodes (15): BuiltContext, ContextReport, ContextTooLargeError, _log(), Exception, NamedTuple, Even with every droppable entry gone the input is over the strategy's limit., The same one-off condensation the app makes at interview start; its tokens… (+7 more)

### Community 116 - "Role"
Cohesion: 0.11
Nodes (41): ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, get_current_user(), AuthControllerDep (+33 more)

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

### Community 123 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): Checkpoint A: the model suggests, the code enforces (concept 5), answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 124 - "RateLimiter"
Cohesion: 0.11
Nodes (18): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them., math (+10 more)

### Community 125 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 126 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 127 - ".__init__"
Cohesion: 0.50
Nodes (3): AsyncBaseTransport, Random, BaseTransport

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "test_fallback_pick.py"
Cohesion: 0.18
Nodes (16): pick_fallback_question(), Random, One unused bank question for `position`, used when the LLM is off or its reply…, Collection, random, fixture_bank(), pick(), fixture (+8 more)

### Community 131 - "Generation"
Cohesion: 0.17
Nodes (8): AbstractContextManager, Generation, Any, Set the output of the trace being built (call it inside `trace()`): what a…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, The stream was closed before it finished (client left, or the turn's deadline…, Changes Made, TraceLabels

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 134 - "follow_up"
Cohesion: 0.10
Nodes (20): Checkpoint B: a small closed decision instead of free text (concept 4), Checkpoint D: labelled evals for a decision (concept 10), Checkpoint E: one deadline for two calls (concept 9), Learnings: Follow-up Questions (decide / write split), Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split) (+12 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "DeepgramTranscriber"
Cohesion: 0.14
Nodes (10): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what… (+2 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 142 - "Implementation: Interview History List (backend)"
Cohesion: 0.12
Nodes (15): 1. Shared pagination module, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links (+7 more)

### Community 143 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

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

### Community 150 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

### Community 151 - "InvalidReplyError"
Cohesion: 0.28
Nodes (8): read(), InvalidReplyError, Exception, interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), test_a_long_first_line_is_no_header_without_waiting_for_its_end(), test_at_the_end_of_the_reply_a_header_needs_no_newline(), test_no_header_is_known_until_its_line_ends()

### Community 152 - "bank"
Cohesion: 0.22
Nodes (9): Acceptance Criteria, Acceptance Criteria, Edge Cases, Functional, Non-Functional, Requirements, Test Results, bank() (+1 more)

### Community 154 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.29
Nodes (8): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 155 - "stream_answer"
Cohesion: 0.29
Nodes (7): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream(), test_done_has_the_json_endpoints_shape_and_content(), run()

### Community 156 - "build_tracer"
Cohesion: 0.47
Nodes (6): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 157 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 158 - "tracer"
Cohesion: 0.40
Nodes (4): client(), propagated(), fixture, tracer()

### Community 159 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

## Knowledge Gaps
- **490 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+485 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1154 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `InterviewsController` to `auth_controller.py`, `test_create_interview.py`, `sqlalchemy`, `decode_token`, `InterviewMessage`, `interviews_model.py`, `users_route.py`, `interviews_route.py`, `tests/conftest.py`, `InterviewQuestion`, `Role`, `Implementation Plan: UUID primary keys`, `errors.py`, `interviews_turn.py`, `interviews_controller.py`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `test_tracing_routes.py`, `Generation`, `InterviewsController`, `get_controller`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `FakeProvider`, `main.py`, `InterviewType`, `interviews_evals.py`, `RecordingClient`, `interviews_turn.py`, `test_tracing.py`, `test_tracing_lifespan.py`, `test_evals.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `build_tracer`, `interviews_controller.py`, `tracer`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `FakeProvider` to `LLMResult`, `Implementation Steps`, `test_interviewer_messages.py`, `.settle`, `interviews_controller.py`, `Feature: Context Management for the Interview LLM Calls`, `The fundamentals`, `test_tracing.py`, `ContextManager`, `test_evals.py`, `errors.py`, `interviews_turn.py`, `RecordingClient`, `test_transcribe.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Tracer`, `check_decision`, `main.py`, `run_stream_case`, `run_case`, `interviews_evals.py`, `Implementation Steps`, `llm`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Are the 61 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 61 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 23 INFERRED edges - model-reasoned connections that need verification._