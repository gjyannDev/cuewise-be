# Graph Report - cuewise-be  (2026-11-11)

## Corpus Check
- 327 files · ~273,731 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 4372 nodes · 12396 edges · 238 communities (200 shown, 38 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2318 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c2d315f7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- LLMServerError
- AnswerService
- decode_token
- test_interview_report.py
- typing
- Cuewise BE — Project Instructions
- interviews_rag_evals.py
- interviews_knowledge_utils.py
- test_guards.py
- interviews_constants.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- interviews_context.py
- test_feedback_evals.py
- cuewise-be
- KnowledgeRepository
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_feedback_contract.py
- re
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Completed Steps
- QuestionTurn
- test_reply_contract.py
- Implementation: LLM as the Interviewer (it asks the questions)
- logging.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- interviews_schema.py
- interviews_answer_service.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- JobRole
- collections_abc
- InterviewerInputs
- test_select_questions.py
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
- FakeEmbedder
- test_context.py
- test_request_context.py
- LLMProvider
- .record_turn
- Any
- interviews_feedback_evals.py
- exception_handlers.py
- errors.py
- failed
- ._run
- interviews_session_utils.py
- main
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- ContextManager
- fake.py
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_reference_note_context.py
- Implementation Plan: Role-Based Access Control (single JWT)
- Implementation Plan: Context Management for the Interview LLM Calls
- .trace
- EmbeddingKind
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- QuestionCategory
- FeedbackGenerator
- Langfuse Observability
- interviewer_v3.md
- Tracer
- fixture
- Implementation: Langfuse Tracing
- interviews_feedback.py
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- ChatMessage
- tests/conftest.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- interviews/conftest.py
- main
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Feature: Langfuse Tracing
- Langfuse
- test_evals.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- test_transcript.py
- interviews_feedback_service.py
- Langfuse Implementation Notes
- interviewer_v5.md
- OpenAICompatibleProvider
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Implementation Plan: UUID primary keys
- InterviewMessage
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_turn_budget.py
- LLMRateLimitError
- Feature: Interview History List (backend)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- test_stream_answer.py
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
- test_knowledge_ingest.py
- Feature: Role-Based Access Control (single JWT)
- Implementation Steps
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- test_context_controller.py
- interviews_feedback_dependencies.py
- test_feedback_context.py
- Embedder
- test_start_reference_notes.py
- LLMResult
- interviews_knowledge_ingest.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- clock
- Learn: Layered architecture (route -> controller -> service -> repository)
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_answer_interview.py
- test_job_description_summary.py
- test_list_users.py
- Feature: Start an Interview (backend)
- llm
- RequestContextMiddleware
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- Settings
- run_case
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- .stream
- feedback_score_v1.md
- feedback_write_v1.md
- test_me.py
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- WindowLedger
- pytest
- ErrorResponse
- Langfuse CLI Reference
- ProviderConfig
- Feature: Interview Feedback and Scoring (Slice 6)
- Implementation Plan: Error Handling
- Implementation Plan: Interview History List (backend)
- Implementation Plan: Split interviews_dependencies.py by responsibility
- build_tracer
- interviewer_v6.md
- interviewer_v6_json.md
- Langfuse
- users_utils.py
- _reset_request_id
- traces
- Backend design and operations
- FakeObservation
- Backend fundamentals
- Data engineering
- Data fundamentals
- Frontend architecture
- Frontend fundamentals
- Full-stack delivery
- Full-stack fundamentals
- Behavioral notes for early-career candidates
- Behavioral notes for experienced candidates
- Mobile architecture and releases
- Mobile fundamentals
- 2. Langfuse Documentation
- Communication and priorities
- Engineering habits
- Senior judgement

## God Nodes (most connected - your core abstractions)
1. `User` - 100 edges
2. `FakeProvider` - 95 edges
3. `JobRole` - 94 edges
4. `LLMResult` - 91 edges
5. `InterviewQuestion` - 88 edges
6. `Level` - 87 edges
7. `InterviewType` - 87 edges
8. `QuestionCategory` - 85 edges
9. `InterviewsRepository` - 81 edges
10. `Tracer` - 80 edges

## Surprising Connections (you probably didn't know these)
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `Acceptance Criteria` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py
- `Functional` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Constraints` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py

## Import Cycles
- None detected.

## Communities (238 total, 38 thin omitted)

### Community 0 - "User"
Cohesion: 0.09
Nodes (30): verify_password(), StrEnum, Role, get_controller(), get_service(), Depends, Session, User (+22 more)

### Community 1 - "LLMServerError"
Cohesion: 0.08
Nodes (28): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The first channel's best transcript (blank for silence) and the reported audio…, Gemini embeddings through Google's native `batchEmbedContents` endpoint, over… (+20 more)

### Community 2 - "AnswerService"
Cohesion: 0.08
Nodes (38): QuestionNotCurrentError, SessionNotInProgressError, AnswerController, UUID, The checks and reads before the stream opens (sync DB work: the route runs it…, AnswerIn, NamedTuple, One event of a streamed turn as the controller yields it; the route encodes it… (+30 more)

### Community 3 - "decode_token"
Cohesion: 0.12
Nodes (32): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+24 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (54): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http() (+46 more)

### Community 5 - "typing"
Cohesion: 0.07
Nodes (61): AnswerControllerDep, The speech-to-text contract features code against, separate from the text-only…, ForbiddenError, Offset pagination shared by every list endpoint, so clients see one query…, Permission, permissions_for(), The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., AuthController (+53 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "interviews_rag_evals.py"
Cohesion: 0.09
Nodes (50): _arm_notes(), ArmSummary, build_sheet(), case_set_problems(), competencies_of(), filter_baseline(), Collection, Exception (+42 more)

### Community 8 - "interviews_knowledge_utils.py"
Cohesion: 0.09
Nodes (47): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, cosine_similarity(), _hash(), _listed() (+39 more)

### Community 9 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 10 - "interviews_constants.py"
Cohesion: 0.14
Nodes (27): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, FollowUpAction, FollowUpGap, MessageKind, StrEnum, QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that… (+19 more)

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
Cohesion: 0.12
Nodes (29): os, _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored() (+21 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - "interviews_context.py"
Cohesion: 0.08
Nodes (30): ContextReport, _log(), NamedTuple, Context management: the one place that decides what each LLM call sends. The…, StrategyOutput, The LLM contract every feature codes against: message/result types, typed…, build_context_manager(), _counts() (+22 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.08
Nodes (39): feedback_scores_for(), feedback_trace_output(), One case through the same pre-check, score call, write call and template…, What came out next to what was wanted: the verdict, the overall against its…, (name, value, comment) per check, plus `valid_reply` and `case_passed`. An…, run_feedback_case(), _usage(), case() (+31 more)

### Community 18 - "cuewise-be"
Cohesion: 0.50
Nodes (3): cuewise-be, Development database (Postgres 18 + pgvector), Reference notes (knowledge-base RAG)

### Community 19 - "KnowledgeRepository"
Cohesion: 0.09
Nodes (26): alembic_config, KnowledgeChunk, KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a…, sqlalchemy_dialects (+18 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.15
Nodes (35): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate… (+27 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.06
Nodes (80): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 8. Check your understanding (+72 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.06
Nodes (31): AnswerOut, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Functional, Goal (+23 more)

### Community 31 - "test_feedback_contract.py"
Cohesion: 0.15
Nodes (38): assess_evidence(), compute_overall(), FeedbackThread, parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, One main question with its follow-ups and every answer: what one set of scores…, The pre-check, before any LLM call: enough main questions have a real answer to… (+30 more)

### Community 32 - "re"
Cohesion: 0.15
Nodes (19): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), Random, A predefined, neutral acknowledgement for the answer just given; never the same…, random, re, starlette_types (+11 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.18
Nodes (10): Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+2 more)

### Community 35 - "Completed Steps"
Cohesion: 0.12
Nodes (29): log_retrieval(), Which reference notes an interview got at start: mode, count, scores and the…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, _eligible(), EligibleChunk (+21 more)

### Community 36 - "QuestionTurn"
Cohesion: 0.12
Nodes (29): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't…, Answered questions with their answers (and the model's note on each), in… (+21 more)

### Community 37 - "test_reply_contract.py"
Cohesion: 0.13
Nodes (31): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open (+23 more)

### Community 38 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.04
Nodes (45): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional (+37 more)

### Community 39 - "logging.py"
Cohesion: 0.09
Nodes (40): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., decide(), UUID, The decide step of an answer turn: the model suggests following up or moving…, At most two attempts within the decide cap; any failure means "next_question"…, log_embedding_call() (+32 more)

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
Cohesion: 0.15
Nodes (30): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+22 more)

### Community 44 - "interviews_schema.py"
Cohesion: 0.09
Nodes (42): page_params(), PageParams, NamedTuple, Query, Criterion, HistorySortColumn, What the score call rates, 1 to 5. Which ones apply depends on the question's…, The history columns GET /interviews sorts by; the values are the response's… (+34 more)

### Community 45 - "interviews_answer_service.py"
Cohesion: 0.09
Nodes (40): log_stream_summary(), How a streamed turn felt and ended: time to the first event and to the first…, PhaseChanged, The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), _error_event(), _event() (+32 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.07
Nodes (25): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank). (+17 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.13
Nodes (18): drain(), Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage(), test_disabled_tracer_is_a_pass_through(), test_failed_call_is_marked_error_and_the_same_exception_is_raised(), test_missing_usage_is_omitted_never_guessed() (+10 more)

### Community 49 - "JobRole"
Cohesion: 0.08
Nodes (59): InterviewType, JobRole, Level, _Interview, The interview as plain values, read before the claim's commit expires the…, EvalSetup, FeedbackEvalSetup, BaseModel (+51 more)

### Community 50 - "collections_abc"
Cohesion: 0.05
Nodes (30): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin (+22 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.12
Nodes (38): InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, apply_limits(), Deadline, _decision_label(), plan_write() (+30 more)

### Community 52 - "test_select_questions.py"
Cohesion: 0.09
Nodes (40): NotEnoughQuestionsError, load_bank(), load_rubric(), Path, Read and validate a feedback rubric file; a bad one fails loudly at startup,…, Read and validate a question bank file; a bad file fails loudly instead of at…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions() (+32 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "interviews_utils.py"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (66): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+58 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "Implementation: Error Handling"
Cohesion: 0.18
Nodes (10): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+2 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.05
Nodes (44): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter(), _history_order(), InterviewsRepository, Any, datetime (+36 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.18
Nodes (14): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), LogRecord, sys, _record(), test_console_appends_the_traceback() (+6 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_follow_ups.py"
Cohesion: 0.27
Nodes (16): answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries(), test_a_failed_follow_up_write_falls_back_to_the_next_main_bank_question() (+8 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.14
Nodes (27): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), parametrize, RetrievalService.retrieve: the vector / filter / skip ladder (knowledge-base-…, A stand-in tracer that records each step's metadata and output. (+19 more)

### Community 66 - "test_context.py"
Cohesion: 0.15
Nodes (17): estimate_tokens(), Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default() (+9 more)

### Community 67 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 68 - "LLMProvider"
Cohesion: 0.06
Nodes (29): LLMError, LLMProvider, Exception, Protocol, Base for every provider failure. `retryable` marks faults that may pass on…, Generation, _model_parameters(), ReasoningEffort (+21 more)

### Community 69 - ".record_turn"
Cohesion: 0.08
Nodes (24): Save one whole turn in one commit: advance the session, the answer, the…, Deviations from Plan, Affected Files & Patterns, Architecture & Design, Deviations Found During Implementation, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps, Overview (+16 more)

### Community 71 - "Any"
Cohesion: 0.15
Nodes (11): AbstractContextManager, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Set the output of the trace being built (call it inside `trace()`): what a…, A named step inside the current trace (a Langfuse `chain`): the generations and…, Run an SDK call; on any failure log what failed (not why: the message could…, _safe(), decorate() (+3 more)

### Community 72 - "interviews_feedback_evals.py"
Cohesion: 0.09
Nodes (40): ThreadTurn, Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Check, Band, _band_check(), check_feedback(), criterion_spread() (+32 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "errors.py"
Cohesion: 0.10
Nodes (29): Protocol, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ErrorBody, NoSpeechError (+21 more)

### Community 75 - "failed"
Cohesion: 0.08
Nodes (31): check_decision(), check_reply(), check_streamed_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format., The decide reply against the case's label; the injection check reads the raw…, summarize_decisions() (+23 more)

### Community 76 - "._run"
Cohesion: 0.39
Nodes (6): _Claim, _Outcome, Any, NamedTuple, Too little to assess (the code's pre-check, or the model's flag): final, with…, How a generation ended, for the trace (metadata only).

### Community 77 - "interviews_session_utils.py"
Cohesion: 0.11
Nodes (25): NotFoundError, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), bank_question(), Random (+17 more)

### Community 78 - "main"
Cohesion: 0.08
Nodes (17): dataset_items(), dataset_name(), main(), Namespace, The stream task reads the same cases as write, so they share one dataset., The cases as Langfuse dataset items. The id is the case id behind the dataset's…, The tags that make runs comparable in Langfuse: what was run, and with which…, run_tags() (+9 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "ContextManager"
Cohesion: 0.11
Nodes (24): ContextManager, _add_usage(), _case_inputs(), ReasoningEffort, One decide call on the case's latest answer, as the app makes it after every…, The streamed turn's write call (interviewer_stream, v5) on one case: the same…, The write call's inputs for a case, with the job description condensed first…, run_decide_case() (+16 more)

### Community 82 - "fake.py"
Cohesion: 0.09
Nodes (16): anyio, EmbeddingResult, EmbeddingSizeError, BaseModel, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, EmbedCall, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or… (+8 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "test_reference_note_context.py"
Cohesion: 0.16
Nodes (20): A main-question write of an interview with reference notes: the notes-aware…, WithReferenceNotes, 5. What can go wrong, first_user(), inputs(), _max_note(), anyio, parametrize (+12 more)

### Community 85 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (10): Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., Affected Files & Patterns, Blockers & Resolutions, Implementation Deviations (recorded during /implement), Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement (+2 more)

### Community 86 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 87 - ".trace"
Cohesion: 0.16
Nodes (12): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Deviations from the first version of this plan (found during /implement), Implementation Steps, Completed Steps, Deviations from Plan (+4 more)

### Community 88 - "EmbeddingKind"
Cohesion: 0.17
Nodes (24): EmbeddingKind, StrEnum, LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., Clock, make_embedder(), ok(), fixture (+16 more)

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
Cohesion: 0.09
Nodes (47): _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, load_object(), _normalized(), parse_interviewer_reply(), parse_streamed_reply() (+39 more)

### Community 93 - "FeedbackGenerator"
Cohesion: 0.09
Nodes (27): BuiltContext, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, FeedbackGenerator (+19 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "Tracer"
Cohesion: 0.12
Nodes (12): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_makes_no_call_without_a_trace_id_or_when_tracing_is_off(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises() (+4 more)

### Community 97 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.17
Nodes (11): Baseline Failures, Commit message suggestion, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 99 - "interviews_feedback.py"
Cohesion: 0.11
Nodes (30): _check_lengths(), Evidence, _has_markup(), _normalized(), parse_write_reply(), BaseModel, NamedTuple, _question_score() (+22 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "ChatMessage"
Cohesion: 0.11
Nodes (31): build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, ChatMessage, BaseModel (+23 more)

### Community 104 - "tests/conftest.py"
Cohesion: 0.07
Nodes (44): alias, ConflictError, RequestIdFilter, hash_password(), health_check(), get_interview(), get_transcript(), list_interviews() (+36 more)

### Community 105 - "test_answer_llm.py"
Cohesion: 0.06
Nodes (39): 2. What it is, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+31 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.09
Nodes (37): anyio_from_thread, _action_and_gap(), CaseResult, DecisionSummary, EvalCase, EvalTurn, hints_for(), _parser() (+29 more)

### Community 109 - "interviews/conftest.py"
Cohesion: 0.09
Nodes (28): Deviations from Plan, answer(), _answer(), anyio_backend(), _bank_question(), _decision_json(), make_bank_question(), parse_sse() (+20 more)

### Community 110 - "main"
Cohesion: 0.10
Nodes (30): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+22 more)

### Community 111 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.17
Nodes (11): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a) (+3 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.15
Nodes (12): Acceptance Criteria, Blockers, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "test_evals.py"
Cohesion: 0.13
Nodes (43): FakeProvider, load_cases(), Path, decision(), hints_of(), mentions(), run_main(), test_a_case_without_an_answer_yet_shows_only_its_kind_and_job_description() (+35 more)

### Community 115 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 116 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 117 - "interviews_feedback_service.py"
Cohesion: 0.07
Nodes (40): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`… (+32 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "OpenAICompatibleProvider"
Cohesion: 0.11
Nodes (18): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+10 more)

### Community 121 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview (+6 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "InterviewMessage"
Cohesion: 0.11
Nodes (22): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, MessageRole, InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, build_transcript(), The chat as the user saw it: each question, then its answer and reaction when…, test_threads_group_follow_ups_under_their_main_question_in_order() (+14 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.17
Nodes (11): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+3 more)

### Community 125 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 126 - "LLMRateLimitError"
Cohesion: 0.11
Nodes (18): LLMRateLimitError, 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+10 more)

### Community 127 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "test_stream_answer.py"
Cohesion: 0.12
Nodes (22): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+14 more)

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
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+17 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Changes Made, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases, Test Results (+2 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.19
Nodes (25): InterviewSessionChunk, A reference note one interview was given at start: the same notes for every…, IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, active(), chunks(), corpus() (+17 more)

### Community 143 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 144 - "Implementation Steps"
Cohesion: 0.15
Nodes (15): Page, BaseModel, UsersController, get_controller(), get_service(), Depends, Session, Session (+7 more)

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

### Community 151 - "interviews_feedback_dependencies.py"
Cohesion: 0.09
Nodes (54): RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., get_db(), Session, get_answer_controller(), get_answer_service(), Depends, Session (+46 more)

### Community 152 - "test_feedback_context.py"
Cohesion: 0.35
Nodes (14): Step 4 of the feedback plan: what the score and write calls send, through the…, score_inputs(), scored(), test_an_answer_over_the_cap_is_shortened_and_counted_but_quotes_still_verify(), test_an_interview_over_the_limit_raises_instead_of_dropping_an_answer(), test_closing_tags_inside_untrusted_text_are_neutralised(), test_tags_inside_quoted_text_are_neutralised_in_the_write_call(), test_the_largest_allowed_interview_fits_the_score_limit() (+6 more)

### Community 154 - "Embedder"
Cohesion: 0.11
Nodes (21): Embedder, Protocol, _embed(), ingest_corpus(), IngestCounts, NamedTuple, Ingestion: turn the validated note chunks into stored rows with their…, embedding_text() (+13 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "LLMResult"
Cohesion: 0.17
Nodes (18): LLMResult, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, ScoreResult, _Attempts, CallUsage, log_feedback_summary(), tokens() (+10 more)

### Community 157 - "interviews_knowledge_ingest.py"
Cohesion: 0.23
Nodes (15): main(), _parser(), ArgumentParser, Session, Ingest the reference notes into the database (knowledge-base RAG). uv run…, pathlib, ingest(), Path (+7 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (14): 9. Review gate (user), Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions (+6 more)

### Community 159 - "clock"
Cohesion: 0.17
Nodes (6): _make(), _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

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
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 164 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 165 - "Feature: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 166 - "llm"
Cohesion: 0.15
Nodes (11): Functional, Non-Functional, Requirements, as_v5_text(), llm(), script(), script_score(), script_write() (+3 more)

### Community 167 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 170 - "Settings"
Cohesion: 0.16
Nodes (8): model_validator, Self, Settings, BaseSettings, Constraints, Step 0: Rename the provider to a vendor-neutral name, field_validator, _settings()

### Community 171 - "run_case"
Cohesion: 0.27
Nodes (14): run_case(), long_case(), noted(), reply(), test_a_v3_window_reply_must_carry_a_note_when_there_is_an_answer(), test_an_unusable_summary_falls_back_to_the_original(), test_finish_length_is_recorded_and_counted(), test_no_note_check_for_full_history_or_the_first_question() (+6 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.25
Nodes (9): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting() (+1 more)

### Community 174 - ".stream"
Cohesion: 0.31
Nodes (4): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Step 11: `FakeProvider.stream`, Reply

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 178 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 179 - "WindowLedger"
Cohesion: 0.29
Nodes (11): Task, An earlier question as the model would have written it. A follow-up was written…, WindowLedger, Affected Files & Patterns, test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), test_the_guard_never_drops_the_current_thread(), manager() (+3 more)

### Community 180 - "pytest"
Cohesion: 0.20
Nodes (9): pytest, parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text(), parametrize, The shipped reference-note corpus (data/knowledge/): valid, broad enough, and… (+1 more)

### Community 181 - "ErrorResponse"
Cohesion: 0.25
Nodes (11): ErrorResponse, Affected Files & Patterns, Requirements (no spec.md: requirement and edge-case IDs are defined here), Test Cases, Project Conventions, Project Conventions, Acceptance Criteria, Acceptance Criteria (+3 more)

### Community 182 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 183 - "ProviderConfig"
Cohesion: 0.40
Nodes (4): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., test_listed_provider_with_its_block_is_configured()

### Community 184 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.18
Nodes (10): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Goal, Out of Scope, Problem (+2 more)

### Community 185 - "Implementation Plan: Error Handling"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Testing Strategy (+1 more)

### Community 186 - "Implementation Plan: Interview History List (backend)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview History List (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 187 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 188 - "build_tracer"
Cohesion: 0.32
Nodes (7): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, Completed Steps, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 191 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 220 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 221 - "Backend design and operations"
Cohesion: 0.33
Nodes (5): API design and versioning, Backend design and operations, Caching and scaling reads, Data consistency and transactions, Observability and incidents

### Community 223 - "Backend fundamentals"
Cohesion: 0.40
Nodes (4): Backend fundamentals, Debugging a failing request, HTTP and REST basics, SQL and data modelling

### Community 224 - "Data engineering"
Cohesion: 0.40
Nodes (4): Data engineering, Data quality and contracts, Modelling for analytics, Pipelines and orchestration

### Community 225 - "Data fundamentals"
Cohesion: 0.40
Nodes (4): Cleaning messy data, Communicating a result, Data fundamentals, SQL for analysis

### Community 226 - "Frontend architecture"
Cohesion: 0.40
Nodes (4): Frontend architecture, Performance and Core Web Vitals, State management at scale, Testing user interfaces

### Community 227 - "Frontend fundamentals"
Cohesion: 0.40
Nodes (4): Component state, Frontend fundamentals, HTML, CSS and accessibility, JavaScript and the DOM

### Community 228 - "Full-stack delivery"
Cohesion: 0.40
Nodes (4): API contracts between client and server, End-to-end feature ownership, Full-stack delivery, Security across the stack

### Community 229 - "Full-stack fundamentals"
Cohesion: 0.40
Nodes (4): A feature from form to database, Full-stack fundamentals, Reading a stack trace, Sessions and authentication basics

### Community 230 - "Behavioral notes for early-career candidates"
Cohesion: 0.40
Nodes (4): Behavioral notes for early-career candidates, Learning and asking for help, Taking feedback, Working on a team project

### Community 231 - "Behavioral notes for experienced candidates"
Cohesion: 0.40
Nodes (4): Behavioral notes for experienced candidates, Disagreement and influence, Ownership and delivery, Raising others

### Community 232 - "Mobile architecture and releases"
Cohesion: 0.40
Nodes (4): Mobile architecture and releases, Offline-first and sync, Performance and battery, Releases and crash management

### Community 233 - "Mobile fundamentals"
Cohesion: 0.40
Nodes (4): App lifecycle, Layouts across screen sizes, Mobile fundamentals, Networking on unreliable connections

### Community 234 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

## Knowledge Gaps
- **677 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+672 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1660 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `AnswerService`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `interviews_feedback_dependencies.py`, `Embedder`, `LLMResult`, `test_feedback_endpoint.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `Completed Steps`, `interviews_answer_service.py`, `test_tracing.py`, `build_tracer`, `test_tracing_routes.py`, `LLMProvider`, `Any`, `interviews_feedback_evals.py`, `main`, `.trace`, `traces`, `FeedbackGenerator`, `ChatMessage`, `interviews_evals.py`, `test_evals.py`, `interviews_feedback_service.py`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `AnswerService`, `decode_token`, `LLMProvider`, `typing`, `tests/conftest.py`, `errors.py`, `interviews_schema.py`, `interviews_answer_service.py`, `interviews_session_utils.py`, `Implementation Steps`, `collections_abc`, `KnowledgeRepository`, `interviews_feedback_service.py`, `.trace`, `interviews_feedback_dependencies.py`, `test_create_interview.py`, `Implementation Plan: UUID primary keys`, `InterviewQuestion`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **Why does `ContextManager` connect `ContextManager` to `AnswerService`, `interviews_context.py`, `test_feedback_evals.py`, `test_context_controller.py`, `interviews_feedback_dependencies.py`, `test_feedback_context.py`, `LLMResult`, `test_context_strategies.py`, `test_feedback_endpoint.py`, `Completed Steps`, `Implementation: LLM as the Interviewer (it asks the questions)`, `logging.py`, `run_case`, `interviews_answer_service.py`, `InterviewerInputs`, `WindowLedger`, `ErrorResponse`, `test_context.py`, `LLMProvider`, `interviews_feedback_evals.py`, `failed`, `test_reference_note_context.py`, `Learn: Context management (what to send, and what it costs)`, `FeedbackGenerator`, `interviews_evals.py`, `test_evals.py`, `interviews_feedback_service.py`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Are the 42 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 55 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 55 INFERRED edges - model-reasoned connections that need verification._
- **Are the 37 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 37 INFERRED edges - model-reasoned connections that need verification._