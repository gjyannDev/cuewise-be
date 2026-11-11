# Graph Report - cuewise-be  (2026-11-09)

## Corpus Check
- 283 files · ~248,463 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 3823 nodes · 10561 edges · 210 communities (171 shown, 39 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2008 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ef0c183e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- AuthService
- LLMTimeoutError
- AnswerService
- decode_token
- test_interview_report.py
- require_permissions
- Cuewise BE — Project Instructions
- test_select_questions.py
- get_db
- test_guards.py
- Implementation Steps
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- interviews_context.py
- test_feedback_evals.py
- README.md
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- LLMServerError
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_feedback_contract.py
- test_feedback_prompts.py
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Implementation: LLM as the Interviewer (it asks the questions)
- pytest
- InvalidReplyError
- Feature: LLM as the Interviewer (it asks the questions)
- LLMResult
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- User
- interviews_answer_controller.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- JobRole
- interviews_model.py
- interviews_turn.py
- select_questions
- test_create_interview.py
- test_start_llm.py
- interviews_utils.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- Implementation: Error Handling
- test_tracing_routes.py
- InterviewQuestion
- ConsoleFormatter
- job_description_summary_v2.md
- test_follow_ups.py
- test_stream_answer.py
- ContextManager
- test_request_context.py
- LLMProvider
- interviews_reply.py
- Any
- interviews_feedback_evals.py
- exception_handlers.py
- errors.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- ._run
- test_fallback_pick.py
- RecordingClient
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- interviews_dependencies.py
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- AnswerOut
- Implementation Plan: Role-Based Access Control (single JWT)
- Implementation Plan: Context Management for the Interview LLM Calls
- .trace
- follow_up
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- QuestionCategory
- interviews_feedback_turn.py
- Langfuse Observability
- interviewer_v3.md
- Tracer
- no_llm_env
- Implementation: Langfuse Tracing
- interviews_feedback.py
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_factory.py
- interviews_route.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- interviews/conftest.py
- main
- InterviewerInputs
- LLMError
- Langfuse
- test_evals.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- test_transcript.py
- interviews_feedback_service.py
- Langfuse Implementation Notes
- interviewer_v5.md
- OpenAICompatibleProvider
- llm
- Implementation Plan: UUID primary keys
- Feature: Follow-up Questions (decide / write split)
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_turn_budget.py
- LLMRateLimitError
- Feature: Interview History List (backend)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- Learn: Streaming and latency (Slice 4, SSE)
- Implementation: Interview History List (backend)
- Judge Calibration
- Langfuse Prompt Migration
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- Implementation: Layered Modules (route -> controller -> service -> repository)
- Langfuse Implementation Notes
- test_get_interview.py
- auth_service.py
- Feature: Role-Based Access Control (single JWT)
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- test_context_controller.py
- get_llm_provider
- test_feedback_context.py
- Feature: Layered Modules (route -> controller -> service -> repository)
- RecordingClient
- AnswerController
- Implementation Plan: Langfuse Tracing
- Implementation: Interview Feedback and Scoring (Slice 6)
- clock
- Learn: Layered architecture (route -> controller -> service -> repository)
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_answer_interview.py
- test_job_description_summary.py
- test_list_users.py
- ErrorResponse
- parse_log
- RequestContextMiddleware
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- db
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- .stream
- feedback_score_v1.md
- feedback_write_v1.md
- test_me.py
- Clock
- Langfuse CLI Reference
- ProviderConfig
- Rubric
- users_utils.py
- _reset_request_id

## God Nodes (most connected - your core abstractions)
1. `User` - 97 edges
2. `FakeProvider` - 91 edges
3. `LLMResult` - 91 edges
4. `InterviewQuestion` - 88 edges
5. `QuestionCategory` - 85 edges
6. `JobRole` - 79 edges
7. `InterviewType` - 78 edges
8. `Tracer` - 73 edges
9. `InterviewsRepository` - 71 edges
10. `InterviewSession` - 70 edges

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

## Communities (210 total, 39 thin omitted)

### Community 0 - "AuthService"
Cohesion: 0.11
Nodes (28): AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), register(), LoginIn, MeOut (+20 more)

### Community 1 - "LLMTimeoutError"
Cohesion: 0.08
Nodes (26): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, LLMRequestError, LLMTimeoutError (+18 more)

### Community 2 - "AnswerService"
Cohesion: 0.13
Nodes (20): QuestionNotCurrentError, The checks and reads before the stream opens (sync DB work: the route runs it…, AnswerIn, AnswerService, _elapsed_ms(), AnswerEvent, UUID, Every check and read of an answer turn, before any LLM call. Raises the usual… (+12 more)

### Community 3 - "decode_token"
Cohesion: 0.14
Nodes (25): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Testing Strategy (+17 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (53): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start() (+45 more)

### Community 5 - "require_permissions"
Cohesion: 0.10
Nodes (34): ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, get_current_user(), get_service() (+26 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_select_questions.py"
Cohesion: 0.33
Nodes (15): NotEnoughQuestionsError, _bank(), _q(), _select(), test_general_question_is_eligible_for_every_role(), test_mixed_even_count_is_an_exact_split(), test_mixed_short_on_one_type_is_rejected_without_rebalancing(), test_mixed_splits_evenly_extra_behavioral_and_interleaves() (+7 more)

### Community 8 - "get_db"
Cohesion: 0.20
Nodes (18): get_db(), Session, get_answer_controller(), get_answer_service(), get_context_manager(), get_feedback_service(), get_interviews_controller(), get_interviews_service() (+10 more)

### Community 9 - "test_guards.py"
Cohesion: 0.10
Nodes (27): health_check(), CurrentUserDep, raise_conflict(), raise_crash(), raise_db_down(), raise_expired(), raise_integrity(), admin_role() (+19 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.20
Nodes (20): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect (+12 more)

### Community 11 - "test_list_interviews.py"
Cohesion: 0.10
Nodes (36): answered(), history(), ids_of(), fixture, parametrize, GET /api/v1/interviews: the candidate's interview history, newest first,…, Five sessions stored directly (oldest first), with values that sort differently…, Start `n` interviews in a row; returns their ids newest first (each start… (+28 more)

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
Cohesion: 0.06
Nodes (54): StrategyOutput, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, build_context_manager(), _counts(), FeedbackScore, FeedbackWrite (+46 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.09
Nodes (49): check_feedback(), criterion_spread(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult, level_gap_check(), The pair's check, or None when there is nothing to compare: no pair, or either…, The case's labels against what came out. Check names stay stable: Langfuse… (+41 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "LLMServerError"
Cohesion: 0.13
Nodes (38): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, LLMServerError, 5xx or a dropped connection: the provider's side failed., Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one… (+30 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.06
Nodes (82): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., 1. Why it exists, 2. What it is, 3. When to use it (+74 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.18
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (19): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+11 more)

### Community 31 - "test_feedback_contract.py"
Cohesion: 0.16
Nodes (36): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+28 more)

### Community 32 - "test_feedback_prompts.py"
Cohesion: 0.21
Nodes (11): load_rubric(), Path, Read and validate a feedback rubric file; a bad one fails loudly at startup,…, Counts and limits come from the constants the write parser checks; a test…, render_feedback_write_prompt(), parametrize, Step 3 of the feedback plan: the rubric (data) and the two prompts. Structure…, test_a_broken_rubric_file_fails_loudly_at_load() (+3 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "pytest"
Cohesion: 0.14
Nodes (18): Fill {{name}} placeholders in one pass: inserted values are never scanned…, render_template(), pytest, parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text() (+10 more)

### Community 37 - "InvalidReplyError"
Cohesion: 0.24
Nodes (21): InvalidReplyError, Exception, parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_follow_up_still_asks_one_question_only() (+13 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "LLMResult"
Cohesion: 0.14
Nodes (29): LLMResult, decide(), UUID, The decide step of an answer turn: the model suggests following up or moving…, At most two attempts within the decide cap; any failure means "next_question"…, log_llm_call(), log_llm_error(), log_result() (+21 more)

### Community 40 - "test_layers.py"
Cohesion: 0.17
Nodes (20): ast, 5. What can go wrong, Blockers & Resolutions, Known Issues, check_layers(), _imports(), _one(), The layer rules of app/modules (CLAUDE.md, "Architecture"): route -> controller… (+12 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (32): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+24 more)

### Community 44 - "User"
Cohesion: 0.06
Nodes (58): SessionNotInProgressError, User, FeedbackStatus, HistorySortColumn, MessageKind, MessageRole, StrEnum, A feedback row's life: `generating` while a request holds it, then `generated`… (+50 more)

### Community 45 - "interviews_answer_controller.py"
Cohesion: 0.12
Nodes (31): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), _error_event(), _event(), _frame(), AnswerEvent, BaseModel (+23 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.06
Nodes (27): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them. (+19 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.10
Nodes (27): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, client(), drain(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result() (+19 more)

### Community 49 - "JobRole"
Cohesion: 0.09
Nodes (46): InterviewType, JobRole, Level, InterviewCreateIn, BaseModel, QuestionOut, SessionOut, _Interview (+38 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.05
Nodes (26): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, InterviewFeedback (+18 more)

### Community 51 - "interviews_turn.py"
Cohesion: 0.14
Nodes (24): Decision, apply_limits(), Deadline, _decision_label(), plan_write(), UUID, The code's say over an answer turn: the shared deadline, the follow-up cap and…, The turn's LLM time budget, set once and asked by every call (an injectable… (+16 more)

### Community 52 - "select_questions"
Cohesion: 0.10
Nodes (24): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Implementation Steps, Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend) (+16 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "interviews_utils.py"
Cohesion: 0.24
Nodes (15): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), pick_reaction(), Random, A predefined, neutral acknowledgement for the answer just given; never the same…, The container of an uploaded recording, or None when its declared type isn't… (+7 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (27): LLMBadResponseError, A 200 whose body is unusable (not JSON, no choices, blank text). Not transient,…, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider() (+19 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (63): Call, group_requests(), _int(), LogEvent, NamedTuple, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer., The events of each request, oldest request first (the id is on every line of… (+55 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.15
Nodes (29): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_cached_and_reasoning_tokens_are_none_when_not_reported() (+21 more)

### Community 59 - "Implementation: Error Handling"
Cohesion: 0.17
Nodes (11): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+3 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.11
Nodes (9): get_tracer(), get_transcriber(), Request, Built once at startup (app lifespan); None when no Deepgram key is configured…, Built once at startup (app lifespan); a disabled tracer when the lifespan…, fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient (+1 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.05
Nodes (52): Protocol, Transcriber, InterviewMessage, InterviewQuestion, InterviewSession, A candidate answer or the interviewer's reaction to one question. The questions…, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter() (+44 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.22
Nodes (13): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), sys, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success() (+5 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): 5. What can go wrong, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 65 - "test_stream_answer.py"
Cohesion: 0.32
Nodes (11): 5. What can go wrong, random, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing() (+3 more)

### Community 66 - "ContextManager"
Cohesion: 0.10
Nodes (28): ContextManager, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., Task, WindowLedger, Deviations Found During Implementation, Inputs (+20 more)

### Community 67 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 68 - "LLMProvider"
Cohesion: 0.09
Nodes (17): LLMProvider, Protocol, ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Random, Random, Slice 9: Tool use and agents, 4. How it works (+9 more)

### Community 69 - "interviews_reply.py"
Cohesion: 0.17
Nodes (15): _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_streamed_reply(), BaseModel, NamedTuple, The contract for what the interviewer LLM must reply, and the check that… (+7 more)

### Community 71 - "Any"
Cohesion: 0.09
Nodes (18): AbstractContextManager, Generation, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Set the output of the trace being built (call it inside `trace()`): what a…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, Run an SDK call; on any failure log what failed (not why: the message could… (+10 more)

### Community 72 - "interviews_feedback_evals.py"
Cohesion: 0.10
Nodes (28): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), feedback_dataset_items(), feedback_hints_for(), feedback_trace_input(), FeedbackEvalCase (+20 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "errors.py"
Cohesion: 0.13
Nodes (26): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody, FeedbackNotFoundError, InvalidCredentialsError (+18 more)

### Community 75 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): 2. What it is, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+7 more)

### Community 76 - "._run"
Cohesion: 0.24
Nodes (11): log_feedback_summary(), tokens(), How one generation ended (generated, insufficient, failed) and what it cost.…, sum_known(), _Claim, _Outcome, Any, NamedTuple (+3 more)

### Community 77 - "test_fallback_pick.py"
Cohesion: 0.21
Nodes (14): pick_fallback_question(), One unused bank question for `position`, used when the LLM is off or its reply…, Collection, fixture_bank(), pick(), fixture, parametrize, test_general_and_role_specific_questions_are_both_eligible() (+6 more)

### Community 78 - "RecordingClient"
Cohesion: 0.12
Nodes (7): case(), langfuse(), fixture, A Langfuse client stand-in. Entering a trace sets `current_trace`, like the SDK…, RecordingClient, test_a_failed_dataset_upsert_still_scores_the_cases(), test_a_langfuse_outage_does_not_change_the_run()

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 82 - "interviews_dependencies.py"
Cohesion: 0.10
Nodes (35): anyio, Context management: the one place that decides what each LLM call sends. The…, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Test doubles for LLMProvider and Transcriber: scripted replies or errors,…, OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, The LLM contract every feature codes against: message/result types, typed…, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, The speech-to-text contract features code against, separate from the text-only… (+27 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "AnswerOut"
Cohesion: 0.15
Nodes (13): AnswerOut, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional (+5 more)

### Community 85 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Deviations (recorded during /implement), Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+1 more)

### Community 86 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 87 - ".trace"
Cohesion: 0.21
Nodes (9): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Deviations from the first version of this plan (found during /implement), Implementation Steps, Completed Steps, Deviations from Plan (+1 more)

### Community 88 - "follow_up"
Cohesion: 0.18
Nodes (12): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+4 more)

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
Cohesion: 0.12
Nodes (32): interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, One criterion of the feedback rubric: what it asks, an anchor per score, and…, RubricCriterion, read() (+24 more)

### Community 93 - "interviews_feedback_turn.py"
Cohesion: 0.09
Nodes (31): BuiltContext, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, ScoreResult, _Attempts (+23 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "Tracer"
Cohesion: 0.09
Nodes (13): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, FakeObservation, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_makes_no_call_without_a_trace_id_or_when_tracing_is_off() (+5 more)

### Community 97 - "no_llm_env"
Cohesion: 0.33
Nodes (6): no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.17
Nodes (11): Baseline Failures, Commit message suggestion, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 99 - "interviews_feedback.py"
Cohesion: 0.12
Nodes (26): _check_lengths(), FeedbackThread, _has_markup(), _normalized(), parse_write_reply(), BaseModel, _question_score(), End-of-interview feedback: what the score and write calls must return, and the… (+18 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "test_factory.py"
Cohesion: 0.10
Nodes (26): build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, TracingProvider, model_validator, Self, Settings (+18 more)

### Community 104 - "interviews_route.py"
Cohesion: 0.06
Nodes (48): alias, AnswerControllerDep, limit_feedback(), limit_transcriptions(), interviews_answer, interviews_feedback, Per-user cap on feedback requests, checked before anything that can cost an LLM…, Per-user cap on transcriptions, checked before the upload goes anywhere that… (+40 more)

### Community 105 - "test_answer_llm.py"
Cohesion: 0.18
Nodes (12): 5. What can go wrong, questions(), Answer every question of a started interview; returns the list of answer…, run_interview(), test_a_legacy_session_uses_its_stored_questions_and_no_llm(), test_a_mixed_bank_only_interview_alternates_behavioral_first(), test_a_new_interview_started_during_the_call_wins(), test_a_non_final_answer_gets_a_reaction_and_the_llms_next_question() (+4 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.06
Nodes (73): anyio_from_thread, parse_interviewer_reply(), A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), _action_and_gap(), _add_usage() (+65 more)

### Community 109 - "interviews/conftest.py"
Cohesion: 0.08
Nodes (34): BankQuestion, One entry of the hand-written question bank file., _unique_ids(), json, auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, answer() (+26 more)

### Community 110 - "main"
Cohesion: 0.16
Nodes (18): html_target(), main(), Path, Session, UUID, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines() (+10 more)

### Community 111 - "InterviewerInputs"
Cohesion: 0.14
Nodes (26): InterviewerInputs, Plain values for one interviewer or decide call., Interviewer, UUID, The same turn as `answer_turn` (same decide, limits and fallbacks), telling the…, TurnOutcome, Written, 1. Why it exists (+18 more)

### Community 112 - "LLMError"
Cohesion: 0.06
Nodes (31): LLMError, Exception, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Base for every provider failure. `retryable` marks faults that may pass on…, Acceptance Criteria, Blockers, Constraints (+23 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "test_evals.py"
Cohesion: 0.09
Nodes (71): FakeProvider, load_cases(), Path, run_case(), Slice 6: Feedback and scoring, decision(), failed(), hints_of() (+63 more)

### Community 115 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 116 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 117 - "interviews_feedback_service.py"
Cohesion: 0.15
Nodes (17): FeedbackFailedError, FeedbackInProgressError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, FeedbackService (+9 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "OpenAICompatibleProvider"
Cohesion: 0.12
Nodes (16): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, Random, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final… (+8 more)

### Community 121 - "llm"
Cohesion: 0.06
Nodes (31): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Save one whole turn in one commit: advance the session, the answer, the…, End the read transaction before a slow call, so no connection sits idle in a…, Affected Files & Patterns, Architecture & Design (+23 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 1. Split `interviews_turn.py` (done, awaiting review), Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

### Community 125 - "test_turn_budget.py"
Cohesion: 0.12
Nodes (21): Blockers & Resolutions, Implementation Plan: Interview History List (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+13 more)

### Community 126 - "LLMRateLimitError"
Cohesion: 0.13
Nodes (15): LLMRateLimitError, 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+7 more)

### Community 127 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "Learn: Streaming and latency (Slice 4, SSE)"
Cohesion: 0.15
Nodes (11): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Streaming and latency (Slice 4, SSE) (+3 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.15
Nodes (12): Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 134 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 135 - "The fundamentals"
Cohesion: 0.05
Nodes (41): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+33 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 142 - "auth_service.py"
Cohesion: 0.27
Nodes (11): hash_password(), verify_password(), main(), Session, pwdlib, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting() (+3 more)

### Community 143 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 144 - "PageParams"
Cohesion: 0.10
Nodes (25): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, UsersController (+17 more)

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

### Community 150 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 151 - "get_llm_provider"
Cohesion: 0.16
Nodes (17): RequestIdFilter, get_bank(), get_clock(), get_llm_provider(), The question source; tests override it with a fixture bank., Built once at startup (app lifespan); None when no key is configured or the…, Monotonic clock for the per-turn LLM time budget; tests swap in a fake one., Affected Files & Patterns (+9 more)

### Community 152 - "test_feedback_context.py"
Cohesion: 0.16
Nodes (28): ContextReport, estimate_tokens(), _log(), NamedTuple, Evidence, NamedTuple, QuestionScore, Plain, stiff, always valid: built from the stored scores and the score call's… (+20 more)

### Community 154 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 156 - "AnswerController"
Cohesion: 0.20
Nodes (8): AnswerController, UUID, NamedTuple, One event of a streamed turn as the controller yields it; the route encodes it…, StreamEventOut, fixture, A started interview and a controller wired like the app's: returns (controller,…, turn()

### Community 157 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.12
Nodes (14): _model_parameters(), ReasoningEffort, What the call asked the model for, shown on the generation. A temperature only…, Architecture & Design, Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Implementation Steps, Overview (+6 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (14): 9. Review gate (user), Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions (+6 more)

### Community 159 - "clock"
Cohesion: 0.20
Nodes (5): _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 160 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (9): Reload rows a commit expired, so reading their fields later needs no database…, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Decisions (grilled with the user), Implementation Plan: Eval runs in Langfuse (scores + datasets), Overview, Plan-defined criteria, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "test_job_description_summary.py"
Cohesion: 0.36
Nodes (6): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_without_an_llm_no_summary_is_made()

### Community 164 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 165 - "ErrorResponse"
Cohesion: 0.04
Nodes (55): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+47 more)

### Community 166 - "parse_log"
Cohesion: 0.31
Nodes (10): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, analysis(), lines_of(), rollup_analysis(), session(), test_calls_logged_before_the_task_name_existed_fold_into_other_so_the_rows_add_up(), test_parse_log_reads_the_apps_own_lines_and_skips_traceback_lines() (+2 more)

### Community 167 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 170 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 171 - "db"
Cohesion: 0.28
Nodes (8): client(), db(), fixture, Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., failing_commit(), test_a_turn_is_saved_all_or_nothing(), arm_once(), failing_commit()

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.25
Nodes (9): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting() (+1 more)

### Community 174 - ".stream"
Cohesion: 0.36
Nodes (3): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Reply

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 178 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 182 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 183 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 188 - "Rubric"
Cohesion: 0.29
Nodes (6): model_validator, Self, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, The anchors of the criteria this interview can be scored on, with this level…, render_rubric()

## Knowledge Gaps
- **617 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+612 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1465 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **39 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `AnswerService`, `get_db`, `interviews_context.py`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `test_feedback_endpoint.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `User`, `test_tracing.py`, `test_tracing_routes.py`, `LLMProvider`, `Any`, `interviews_feedback_evals.py`, `RecordingClient`, `interviews_dependencies.py`, `.trace`, `interviews_feedback_turn.py`, `test_factory.py`, `interviews_evals.py`, `test_evals.py`, `interviews_feedback_service.py`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Why does `LLMError` connect `LLMError` to `LLMTimeoutError`, `Implementation Steps`, `LLMServerError`, `Implementation Plan: Langfuse Tracing`, `LLMResult`, `Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `User`, `test_transcribe.py`, `select_questions`, `test_openai_compatible_stream.py`, `Any`, `errors.py`, `Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `interviews_dependencies.py`, `interviews_feedback_turn.py`, `test_factory.py`, `interviews_evals.py`, `InterviewerInputs`, `test_evals.py`, `OpenAICompatibleProvider`, `LLMRateLimitError`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `LLMTimeoutError`, `interviews_context.py`, `test_feedback_evals.py`, `Implementation Plan: Langfuse Tracing`, `test_job_description_summary.py`, `User`, `.stream`, `test_tracing.py`, `interviews_turn.py`, `test_start_llm.py`, `test_openai_compatible_stream.py`, `Any`, `interviews_feedback_evals.py`, `._run`, `interviews_dependencies.py`, `interviews_feedback_turn.py`, `test_factory.py`, `test_answer_llm.py`, `interviews_evals.py`, `InterviewerInputs`, `LLMError`, `test_evals.py`, `interviews_feedback_service.py`, `OpenAICompatibleProvider`, `test_turn_budget.py`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Are the 42 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 37 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 37 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `InterviewQuestion` (e.g. with `build_threads()` and `question_out()`) actually correct?**
  _`InterviewQuestion` has 34 INFERRED edges - model-reasoned connections that need verification._