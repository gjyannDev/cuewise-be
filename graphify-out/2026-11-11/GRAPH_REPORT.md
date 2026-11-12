# Graph Report - cuewise-be  (2026-11-11)

## Corpus Check
- 343 files · ~285,488 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 4505 nodes · 12588 edges · 261 communities (220 shown, 41 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2368 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3bd96fbe`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- LLMServerError
- TurnContext
- decode_token
- test_interview_report.py
- interviews_route.py
- Cuewise BE — Project Instructions
- interviews_rag_evals.py
- test_knowledge_utils.py
- Role
- test_reference_note_context.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- .build
- run_feedback_case
- Checks
- test_knowledge_postgres.py
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_feedback_contract.py
- test_reaction_pick.py
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Completed Steps
- QuestionTurn
- QuestionCategory
- Feature: LLM as the Interviewer (it asks the questions)
- interviews_constants.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- interviews_schema.py
- interviews_answer_controller.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- interviews_feedback.py
- interviews_model.py
- ContextManager
- JobRole
- test_create_interview.py
- test_start_llm.py
- StreamEventOut
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- test_select_questions.py
- test_tracing_routes.py
- InterviewsRepository
- ConsoleFormatter
- job_description_summary_v2.md
- test_follow_ups.py
- FakeEmbedder
- StrategyOutput
- pytest
- interviews_feedback_service.py
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Any
- run_feedback
- exception_handlers.py
- errors.py
- Slices in detail
- interviews_feedback_controller.py
- test_evals.py
- main
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- EmbeddingKind
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_feedback_context.py
- Implementation: Three New Interview Roles (designer, qa, devops)
- Implementation Plan: Context Management for the Interview LLM Calls
- Feature: Follow-up Questions (decide / write split)
- Clock
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- Tracer
- hint_for
- Langfuse Observability
- interviewer_v3.md
- Implementation: LLM as the Interviewer (it asks the questions)
- fixture
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_factory.py
- tests/conftest.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- CaseResult
- llm
- interview_report.py
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Feature: Langfuse Tracing
- Langfuse
- FakeProvider
- .finish_answer
- test_transcript.py
- LLMResult
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
- FeedbackCaseResult
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- InterviewQuestion
- interviews_start_dependencies.py
- failed
- KnowledgeRepository
- test_start_reference_notes.py
- FeedbackThread
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- clock
- Learn: Layered architecture (route -> controller -> service -> repository)
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_answer_interview.py
- parse_log
- test_list_users.py
- require_permissions
- filter_baseline
- RequestContextMiddleware
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- QuestionScore
- audio_container
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- ChatMessage
- feedback_score_v1.md
- feedback_write_v1.md
- test_me.py
- test_feedback_evals.py
- WindowLedger
- test_keyterms.py
- test_create_admin.py
- Langfuse CLI Reference
- Feature: Start an Interview (backend)
- Learn: Splitting the interviews dependency wiring
- StreamedTurn
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- Langfuse
- users_utils.py
- _reset_request_id
- Generation
- Backend design and operations
- UX design and engineering collaboration
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
- limit_transcriptions
- Communication and priorities
- Engineering habits
- Senior judgement
- Affected Files & Patterns
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- ._covers_every_criterion
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- fixture
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- get_feedback_service
- logging.py
- build_tracer
- Implementation Steps
- stored_scores
- FakeObservation
- tracer
- test_shipped_corpus.py
- ._ordered
- langfuse
- _raise_location
- _LostClaim
- check_feedback

## God Nodes (most connected - your core abstractions)
1. `JobRole` - 102 edges
2. `User` - 100 edges
3. `FakeProvider` - 95 edges
4. `LLMResult` - 91 edges
5. `InterviewQuestion` - 88 edges
6. `Level` - 87 edges
7. `InterviewType` - 87 edges
8. `QuestionCategory` - 86 edges
9. `InterviewsRepository` - 81 edges
10. `Tracer` - 80 edges

## Surprising Connections (you probably didn't know these)
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `Acceptance Criteria` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py
- `Functional` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py

## Import Cycles
- None detected.

## Communities (261 total, 41 thin omitted)

### Community 0 - "User"
Cohesion: 0.07
Nodes (38): get_db(), Session, AuthController, Request -> service call, domain result -> response schema., get_controller(), get_service(), Depends, Session (+30 more)

### Community 1 - "LLMServerError"
Cohesion: 0.08
Nodes (28): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, LLMServerError, LLMTimeoutError (+20 more)

### Community 2 - "TurnContext"
Cohesion: 0.13
Nodes (14): AnswerController, UUID, The checks and reads before the stream opens (sync DB work: the route runs it…, AnswerIn, _elapsed_ms(), AnswerEvent, UUID, Every check and read of an answer turn, before any LLM call. Raises the usual… (+6 more)

### Community 3 - "decode_token"
Cohesion: 0.18
Nodes (26): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Implementation Steps (+18 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (52): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start() (+44 more)

### Community 5 - "interviews_route.py"
Cohesion: 0.10
Nodes (30): alias, AnswerControllerDep, answer_question(), answer_question_stream(), generate_feedback(), get_feedback(), get_interview(), get_transcript() (+22 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "interviews_rag_evals.py"
Cohesion: 0.12
Nodes (34): ArmSummary, build_sheet(), case_set_problems(), competencies_of(), BaseModel, Exception, NamedTuple, Path (+26 more)

### Community 8 - "test_knowledge_utils.py"
Cohesion: 0.06
Nodes (51): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, cosine_similarity(), _hash(), _listed() (+43 more)

### Community 9 - "Role"
Cohesion: 0.10
Nodes (31): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry(), test_unknown_role_has_no_permissions_and_is_logged() (+23 more)

### Community 10 - "test_reference_note_context.py"
Cohesion: 0.11
Nodes (35): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect (+27 more)

### Community 11 - "test_list_interviews.py"
Cohesion: 0.10
Nodes (37): answered(), history(), ids_of(), fixture, parametrize, GET /api/v1/interviews: the candidate's interview history, newest first,…, Five sessions stored directly (oldest first), with values that sort differently…, Start `n` interviews in a row; returns their ids newest first (each start… (+29 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_config.py"
Cohesion: 0.12
Nodes (30): os, _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored() (+22 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - ".build"
Cohesion: 0.16
Nodes (9): _counts(), FollowUpDecision, An earlier question as the model would have written it. A follow-up was written…, The decide call: the current thread in full (it judges the latest answer within…, App data at the end of the last user message; untrusted parts (questions,…, _status_block(), main_numbers(), The main-question number of each turn: a follow-up shares the number of the… (+1 more)

### Community 17 - "run_feedback_case"
Cohesion: 0.13
Nodes (25): feedback_scores_for(), feedback_trace_output(), One case through the same pre-check, score call, write call and template…, What came out next to what was wanted: the verdict, the overall against its…, (name, value, comment) per check, plus `valid_reply` and `case_passed`. An…, run_feedback_case(), case(), Grader (+17 more)

### Community 18 - "Checks"
Cohesion: 0.40
Nodes (5): Checks, bad_parent(), _consistency(), Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers…

### Community 19 - "test_knowledge_postgres.py"
Cohesion: 0.11
Nodes (27): alembic_config, InterviewSessionChunk, KnowledgeChunk, A reference note one interview was given at start: the same notes for every…, cuewise-be, Development database (Postgres 18 + pgvector), Reference notes (knowledge-base RAG), sqlalchemy_dialects (+19 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.19
Nodes (27): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, collect(), follow_up_json(), inputs(), kinds(), make_interviewer(), parametrize (+19 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.05
Nodes (86): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, Who wrote the feedback text: the write call, or the code's template when that…, TextSource, InterviewFeedback (+78 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.07
Nodes (21): assert_one_terminal(), follow_up_json(), message_count(), anyio, fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,… (+13 more)

### Community 31 - "test_feedback_contract.py"
Cohesion: 0.24
Nodes (27): assess_evidence(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The pre-check, before any LLM call: enough main questions have a real answer to…, parametrize, question_json(), The feedback contract (interviews_feedback.py): the code pre-check, the score…, reason_of() (+19 more)

### Community 32 - "test_reaction_pick.py"
Cohesion: 0.18
Nodes (17): LevelGroup, Reactions are warmer for people early in their career and briefer for…, The predefined acknowledgement for moving on (or completing). The id is set…, pick_reaction(), Random, A predefined, neutral acknowledgement for the answer just given; never the same…, Project Conventions, pick() (+9 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 35 - "Completed Steps"
Cohesion: 0.10
Nodes (35): log_embedding_call(), log_retrieval(), One line per embedding call (ingest or retrieval): metadata only, never the…, Which reference notes an interview got at start: mode, count, scores and the…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip (+27 more)

### Community 36 - "QuestionTurn"
Cohesion: 0.11
Nodes (30): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't…, Answered questions with their answers (and the model's note on each), in… (+22 more)

### Community 37 - "QuestionCategory"
Cohesion: 0.07
Nodes (68): _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, load_object(), _normalized(), parse_interviewer_reply(), parse_streamed_reply() (+60 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "interviews_constants.py"
Cohesion: 0.06
Nodes (69): anyio, anyio_from_thread, Context management: the one place that decides what each LLM call sends. The…, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The embedding contract features code against, separate from the chat…, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or…, OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, The LLM contract every feature codes against: message/result types, typed… (+61 more)

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
Nodes (29): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+21 more)

### Community 44 - "interviews_schema.py"
Cohesion: 0.10
Nodes (38): HistorySortColumn, MessageKind, MessageRole, StrEnum, The history columns GET /interviews sorts by; the values are the response's…, Transcript item kinds: a question comes from interview_questions, the other two…, SessionStatus, SortDirection (+30 more)

### Community 45 - "interviews_answer_controller.py"
Cohesion: 0.15
Nodes (25): answer_out(), _frame(), AnswerEvent, Answer turns: request -> AnswerService, domain result -> AnswerOut, and the…, _reaction_out(), question_out(), QuestionDeltaOut, The next chunk of the question being written; the client appends it to the text… (+17 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.07
Nodes (25): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank). (+17 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.13
Nodes (16): drain(), Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage(), test_failed_call_is_marked_error_and_the_same_exception_is_raised(), test_missing_usage_is_omitted_never_guessed(), test_retried_call_is_one_generation_with_attempts() (+8 more)

### Community 49 - "interviews_feedback.py"
Cohesion: 0.27
Nodes (11): BaseModel, End-of-interview feedback: what the score and write calls must return, and the…, _RawEvidence, _RawQuestion, _RawScoreReply, StoredEvidence, StoredQuestion, Criterion (+3 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.04
Nodes (26): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin (+18 more)

### Community 51 - "ContextManager"
Cohesion: 0.08
Nodes (67): ContextManager, InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, apply_limits(), Deadline, _decision_label() (+59 more)

### Community 52 - "JobRole"
Cohesion: 0.05
Nodes (95): FullHistory, A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), InterviewType, JobRole, Level (+87 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (20): 5. What can go wrong, parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session() (+12 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "StreamEventOut"
Cohesion: 0.13
Nodes (19): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, _error_event(), _event(), BaseModel, NamedTuple, One event of a streamed turn as the controller yields it; the route encodes it…, StreamEventOut (+11 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (63): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+55 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "test_select_questions.py"
Cohesion: 0.12
Nodes (31): NotEnoughQuestionsError, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Implementation Steps, Module Structure & Layer Rules (+23 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 61 - "InterviewsRepository"
Cohesion: 0.08
Nodes (24): InterviewSession, _history_filter(), _history_order(), InterviewsRepository, Any, datetime, Session, UUID (+16 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.27
Nodes (12): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success(), test_console_keeps_free_text_on_one_line() (+4 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_follow_ups.py"
Cohesion: 0.15
Nodes (24): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+16 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.13
Nodes (32): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), corpus(), note_text(), fixture (+24 more)

### Community 66 - "StrategyOutput"
Cohesion: 0.11
Nodes (20): StrategyOutput, FeedbackWrite, JobDescriptionSummary, The write call: scores, evidence and question texts only; small whatever the…, Inputs, manager(), NamedTuple, parametrize (+12 more)

### Community 67 - "pytest"
Cohesion: 0.25
Nodes (4): pytest, parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 68 - "interviews_feedback_service.py"
Cohesion: 0.12
Nodes (26): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, NotFoundError, The LLM could not produce valid scores in time: nothing partial is returned;…, _Claim (+18 more)

### Community 69 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Functional, Goal, Non-Functional (+5 more)

### Community 71 - "Any"
Cohesion: 0.13
Nodes (14): AbstractContextManager, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Set the output of the trace being built (call it inside `trace()`): what a…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, Run an SDK call; on any failure log what failed (not why: the message could…, _safe() (+6 more)

### Community 72 - "run_feedback"
Cohesion: 0.22
Nodes (13): feedback_dataset_items(), feedback_trace_input(), FeedbackEvalCase, load_feedback_cases(), Any, Namespace, Path, The cases as dataset items: the interview as input, the bands as the expected… (+5 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.21
Nodes (20): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+12 more)

### Community 74 - "errors.py"
Cohesion: 0.07
Nodes (47): Protocol, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody (+39 more)

### Community 75 - "Slices in detail"
Cohesion: 0.18
Nodes (11): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 7: Eval maturity (trust the judge, catch regressions), Slice 9: Tool use and agents (+3 more)

### Community 76 - "interviews_feedback_controller.py"
Cohesion: 0.10
Nodes (21): Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, get_feedback_controller() (+13 more)

### Community 77 - "test_evals.py"
Cohesion: 0.13
Nodes (34): build_context_manager(), `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, check_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, The same one-off condensation the app makes at interview start; its tokens…, One run proves little (the same cases scored 5/6, then 6/6): look at the spread…, run_case(), summarize() (+26 more)

### Community 78 - "main"
Cohesion: 0.07
Nodes (20): dataset_items(), dataset_name(), DecisionSummary, main(), _parser(), _positive(), _print_decisions(), ArgumentParser (+12 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 82 - "EmbeddingKind"
Cohesion: 0.08
Nodes (40): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, A vector of another length than configured. Vectors of different sizes can't be…, EmbedCall, NamedTuple (+32 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "test_feedback_context.py"
Cohesion: 0.16
Nodes (21): ContextReport, estimate_tokens(), _log(), NamedTuple, FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, Evidence, Step 4 of the feedback plan: what the score and write calls send, through the… (+13 more)

### Community 85 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 86 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 87 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Goal, Non-Functional, Out of Scope, Problem (+4 more)

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
Cohesion: 0.11
Nodes (14): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_disabled_tracer_is_a_pass_through(), test_score_failure_is_swallowed(), test_score_makes_no_call_without_a_trace_id_or_when_tracing_is_off() (+6 more)

### Community 93 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 97 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 98 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 99 - "Implementation: Split interviews_dependencies.py by responsibility"
Cohesion: 0.14
Nodes (13): Changes Made, Completed Steps, Deviations from Plan, Implementation: Split interviews_dependencies.py by responsibility, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 103 - "test_factory.py"
Cohesion: 0.06
Nodes (45): build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, TracingProvider, ProviderConfig (+37 more)

### Community 104 - "tests/conftest.py"
Cohesion: 0.06
Nodes (45): RequestIdFilter, hash_password(), health_check(), start_interview(), CurrentUserDep, Baseline Failures, Completed Steps, Deviations from Plan (+37 more)

### Community 105 - "test_answer_llm.py"
Cohesion: 0.11
Nodes (22): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview() (+14 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "CaseResult"
Cohesion: 0.11
Nodes (26): _action_and_gap(), _add_usage(), CaseResult, check_decision(), EvalCase, hints_for(), _print_case(), The decide reply against the case's label; the injection check reads the raw… (+18 more)

### Community 109 - "llm"
Cohesion: 0.14
Nodes (13): as_v5_text(), _decision_json(), llm(), script(), script_decide(), script_score(), script_write(), unique_question() (+5 more)

### Community 110 - "interview_report.py"
Cohesion: 0.15
Nodes (19): html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+11 more)

### Community 111 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "FakeProvider"
Cohesion: 0.12
Nodes (35): FakeProvider, load_cases(), Path, decision(), hints_of(), mentions(), run_main(), test_a_case_without_an_answer_yet_shows_only_its_kind_and_job_description() (+27 more)

### Community 115 - ".finish_answer"
Cohesion: 0.14
Nodes (17): QuestionNotCurrentError, AnswerOut, Turn the outcome into rows and save the whole turn in one commit. `reaction` is…, Implementation Steps, Affected Files & Patterns, Implementation Steps, Phase A: plumbing and progress events, Phase B: streaming the question text (+9 more)

### Community 116 - "test_transcript.py"
Cohesion: 0.25
Nodes (12): fixture, shape(), started(), test_a_follow_up_is_shown_with_its_kind_and_its_main_questions_number(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question() (+4 more)

### Community 117 - "LLMResult"
Cohesion: 0.06
Nodes (58): BuiltContext, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., LLMError, LLMProvider, LLMResult, Exception (+50 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "OpenAICompatibleProvider"
Cohesion: 0.13
Nodes (13): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+5 more)

### Community 121 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "InterviewMessage"
Cohesion: 0.11
Nodes (20): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, test_threads_group_follow_ups_under_their_main_question_in_order(), message_count(), fixture, parametrize (+12 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+5 more)

### Community 125 - "test_turn_budget.py"
Cohesion: 0.20
Nodes (15): Testing Strategy, 7. What surprised me, Known Issues, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result() (+7 more)

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
Cohesion: 0.07
Nodes (35): Save one whole turn in one commit: advance the session, the answer, the…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me (+27 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

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
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.22
Nodes (22): KnowledgeChunkScope, One (role, level) a chunk applies to. Rows instead of array columns, so the…, active(), chunks(), corpus(), FailingOn, interview(), ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag… (+14 more)

### Community 143 - "FeedbackCaseResult"
Cohesion: 0.22
Nodes (13): criterion_spread(), feedback_hints_for(), FeedbackCaseResult, level_gap_check(), _print_case(), The pair's check, or None when there is nothing to compare: no pair, or either…, Per case: the largest gap between the highest and lowest score any one…, Where to look first for each failed check (or the error), in the order the… (+5 more)

### Community 144 - "PageParams"
Cohesion: 0.08
Nodes (38): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewListOut (+30 more)

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

### Community 150 - "InterviewQuestion"
Cohesion: 0.16
Nodes (18): InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, Every stored question, grouped by interview in creation order (UUIDv7), for the…, Transcript, main(), Session, candidate_messages(), noted() (+10 more)

### Community 151 - "interviews_start_dependencies.py"
Cohesion: 0.13
Nodes (37): get_answer_controller(), get_answer_service(), Depends, Session, get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., get_bank(), get_clock() (+29 more)

### Community 152 - "failed"
Cohesion: 0.11
Nodes (19): Slice 6: Feedback and scoring, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal (+11 more)

### Community 154 - "KnowledgeRepository"
Cohesion: 0.07
Nodes (38): Embedder, Protocol, KnowledgeRepository, Session, Database access for the reference-note corpus. No business rules: which rows to…, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a… (+30 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "FeedbackThread"
Cohesion: 0.13
Nodes (17): _check_lengths(), FeedbackThread, _has_markup(), _normalized(), parse_write_reply(), NamedTuple, _question_score(), Case and whitespace don't make a quote different; anything else (words,… (+9 more)

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.42
Nodes (9): ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1(), test_an_invalid_note_names_the_file_writes_nothing_and_exits_1(), test_it_prints_the_counts_and_exits_0(), test_warnings_are_printed_without_note_text(), test_without_the_google_key_it_says_what_to_set_and_exits_1() (+1 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "clock"
Cohesion: 0.11
Nodes (13): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 8. Check your understanding, 9. Still open, Learn: Adding interview roles (designer, qa, devops) (+5 more)

### Community 160 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (8): Reload rows a commit expired, so reading their fields later needs no database…, 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.10
Nodes (18): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Architecture & Design, Decisions (grilled with the user), Deviations from the first version of this plan (found during /implement), Implementation Plan: Eval runs in Langfuse (scores + datasets) (+10 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "parse_log"
Cohesion: 0.22
Nodes (14): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), analysis(), lines_of(), Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis() (+6 more)

### Community 164 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 165 - "require_permissions"
Cohesion: 0.06
Nodes (50): ErrorResponse, ForbiddenError, BaseModel, get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check() (+42 more)

### Community 166 - "filter_baseline"
Cohesion: 0.22
Nodes (14): filter_baseline(), Collection, UUID, What filter mode alone would score: recall@k and reciprocal rank averaged over…, (threshold, mean recall@k, mean notes kept) per threshold: a higher threshold…, recall_at_k(), reciprocal_rank(), _run_retrieval() (+6 more)

### Community 167 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 170 - "QuestionScore"
Cohesion: 0.24
Nodes (12): compute_overall(), QuestionScore, The mean of every criterion score of every main question, rounded half up to…, Plain, stiff, always valid: built from the stored scores and the score call's…, _template_note(), template_text(), 6. Try it yourself, score() (+4 more)

### Community 171 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.15
Nodes (16): Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+8 more)

### Community 174 - "ChatMessage"
Cohesion: 0.07
Nodes (26): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, _model_parameters(), ReasoningEffort, What the call asked the model for, shown on the generation. A temperature only… (+18 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 178 - "test_feedback_evals.py"
Cohesion: 0.13
Nodes (12): summarize_feedback(), Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The…, Records traces (spans), steps (chains) and checks (guardrails) apart, like the…, RecordingClient, run_main(), test_a_langfuse_outage_does_not_change_the_run(), test_a_run_scores_the_level_gap_on_the_higher_levels_trace(), test_main_runs_every_case_traces_it_and_mirrors_the_dataset() (+4 more)

### Community 179 - "WindowLedger"
Cohesion: 0.20
Nodes (12): Task, A main-question write of an interview with reference notes: the notes-aware…, WindowLedger, WithReferenceNotes, test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), test_the_guard_never_drops_the_current_thread(), manager() (+4 more)

### Community 180 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 181 - "test_create_admin.py"
Cohesion: 0.35
Nodes (9): verify_password(), main(), Session, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting(), test_new_admin_password_follows_registration_rules(), test_running_twice_is_a_no_op() (+1 more)

### Community 182 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 183 - "Feature: Start an Interview (backend)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 184 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 8. Check your understanding, 9. Still open, Learn: Splitting the interviews dependency wiring

### Community 185 - "StreamedTurn"
Cohesion: 0.18
Nodes (9): parse_sse(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream() (+1 more)

### Community 186 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 187 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 188 - "Platform and DevOps practice"
Cohesion: 0.25
Nodes (7): CI/CD pipelines with safe rollback, Cloud security, backup and recovery, Containers and Kubernetes troubleshooting, Infrastructure as code in practice, Monitoring, alerting and observability, Platform and DevOps practice, Production problems with no obvious cause

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 191 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 220 - "Generation"
Cohesion: 0.29
Nodes (4): Generation, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, The stream was closed before it finished (client left, or the turn's deadline…, TraceLabels

### Community 221 - "Backend design and operations"
Cohesion: 0.33
Nodes (5): API design and versioning, Backend design and operations, Caching and scaling reads, Data consistency and transactions, Observability and incidents

### Community 222 - "UX design and engineering collaboration"
Cohesion: 0.25
Nodes (7): Checking feasibility with engineers, Clear wording in forms and instructions, From requirements to user flows, Measuring whether a design worked, Usability testing and reporting findings, User research that changes a design, UX design and engineering collaboration

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

### Community 234 - "limit_transcriptions"
Cohesion: 0.20
Nodes (10): RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., limit_feedback(), interviews_feedback, Per-user cap on feedback requests, checked before anything that can cost an LLM…, get_transcription_limiter(), limit_transcriptions(), interviews_answer (+2 more)

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "Affected Files & Patterns"
Cohesion: 0.33
Nodes (5): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns

### Community 239 - "Design fundamentals"
Cohesion: 0.29
Nodes (6): Accessibility basics, Design fundamentals, Handing a design to developers, Taking critique, User flows and wireframes, Visual hierarchy and layout

### Community 240 - "DevOps fundamentals"
Cohesion: 0.29
Nodes (6): Cloud basics, Containers with Docker, DevOps fundamentals, Git and a first CI pipeline, Linux and shell basics, Reading logs and basic monitoring

### Community 241 - "Test strategy and quality leadership"
Cohesion: 0.29
Nodes (6): Leading a release sign-off, Quality gates in CI and releases, Quality metrics that matter, Risk-based test planning, Test strategy and quality leadership, What to automate and the test pyramid

### Community 242 - "Quality assurance basics"
Cohesion: 0.29
Nodes (6): Quality assurance basics, Raising edge cases before code exists, Regression and cross-platform testing, Test case design techniques, Verifying an API and the data behind a screen, Writing a reproducible bug report

### Community 243 - "Writing a knowledge-base note (guide)"
Cohesion: 0.33
Nodes (5): Check a note before ingesting (reads the file only; no database, no API call), Rules the ingest CLI enforces (a broken rule refuses the whole file), What makes a section good, Where real material comes from, Writing a knowledge-base note (guide)

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "fixture"
Cohesion: 0.17
Nodes (12): answer(), _answer(), anyio_backend(), fixture, Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a recording to the transcription endpoint; `audio=None` sends no file part…, POST a setup for `user`; any field can be overridden, or dropped by passing…, POST an answer; `question_id` defaults to whatever the caller passes, body… (+4 more)

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "get_feedback_service"
Cohesion: 0.29
Nodes (8): get_feedback_service(), datetime, Depends, Session, get_now(), datetime, Wall-clock time for stored timestamps (the feedback claim and its stale…, _utc_now()

### Community 249 - "logging.py"
Cohesion: 0.29
Nodes (5): setup_logging(), contextvars, logging_config, starlette_types, sys

### Community 250 - "build_tracer"
Cohesion: 0.47
Nodes (6): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 252 - "stored_scores"
Cohesion: 0.33
Nodes (4): The scores and evidence from the score call, then the text. Read back through…, The validated scores with their questions' text and category, ready to store…, stored_scores(), StoredResult

### Community 254 - "tracer"
Cohesion: 0.40
Nodes (4): client(), propagated(), fixture, tracer()

### Community 255 - "test_shipped_corpus.py"
Cohesion: 0.40
Nodes (3): parametrize, The shipped reference-note corpus (data/knowledge/): valid, broad enough, and…, test_every_role_and_level_has_enough_notes_for_filter_mode()

### Community 257 - "langfuse"
Cohesion: 0.50
Nodes (3): case(), langfuse(), fixture

### Community 258 - "_raise_location"
Cohesion: 0.67
Nodes (3): _raise_location(), (path/to/file.py:42 func)' of the innermost frame, i.e. where the error was…, BaseException

### Community 259 - "_LostClaim"
Cohesion: 0.67
Nodes (3): _LostClaim, Exception, Another request took the row over while this one ran: this one's writes are…

### Community 260 - "check_feedback"
Cohesion: 0.67
Nodes (3): check_feedback(), The case's labels against what came out. Check names stay stable: Langfuse…, test_a_case_scored_when_it_should_not_have_been_points_at_the_pre_check()

## Knowledge Gaps
- **755 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+750 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1750 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **41 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `TurnContext`, `decode_token`, `interviews_route.py`, `Role`, `PageParams`, `test_knowledge_postgres.py`, `interviews_start_dependencies.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `require_permissions`, `interviews_constants.py`, `interviews_schema.py`, `interviews_answer_controller.py`, `interviews_model.py`, `ContextManager`, `test_create_interview.py`, `test_create_admin.py`, `InterviewsRepository`, `interviews_feedback_service.py`, `errors.py`, `interviews_feedback_controller.py`, `tests/conftest.py`, `limit_transcriptions`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `User`, `langfuse`, `run_feedback_case`, `test_tracing_lifespan.py`, `interviews_start_dependencies.py`, `KnowledgeRepository`, `test_feedback_endpoint.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `Completed Steps`, `interviews_constants.py`, `interviews_schema.py`, `ChatMessage`, `test_tracing.py`, `test_feedback_evals.py`, `ContextManager`, `test_tracing_routes.py`, `interviews_feedback_service.py`, `Any`, `run_feedback`, `test_evals.py`, `main`, `Generation`, `test_factory.py`, `CaseResult`, `LLMResult`, `get_feedback_service`, `build_tracer`, `tracer`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `User`, `test_stream_answer.py`, `TurnContext`, `test_interview_report.py`, `build_usage_report`, `test_reference_note_context.py`, `test_list_interviews.py`, `Checks`, `test_feedback_endpoint.py`, `test_answer_stream.py`, `test_feedback_contract.py`, `QuestionTurn`, `interviews_constants.py`, `interviews_schema.py`, `interviews_answer_controller.py`, `interviews_feedback.py`, `interviews_model.py`, `ContextManager`, `JobRole`, `test_create_interview.py`, `test_start_llm.py`, `interviews_report.py`, `test_select_questions.py`, `InterviewsRepository`, `test_follow_ups.py`, `test_answer_llm.py`, `InterviewMessage`, `test_transcript.py`, `Implementation Steps`, `test_turn_budget.py`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Are the 63 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 63 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 37 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 37 INFERRED edges - model-reasoned connections that need verification._