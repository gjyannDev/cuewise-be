# Graph Report - cuewise-be  (2026-11-12)

## Corpus Check
- 353 files · ~309,531 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 4786 nodes · 13537 edges · 269 communities (223 shown, 46 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2592 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8302c751`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- LLMServerError
- AnswerService
- decode_token
- test_interview_report.py
- interviews_route.py
- Cuewise BE — Project Instructions
- interviews_rag_evals.py
- interviews_knowledge_utils.py
- Role
- interviews_reply.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- FollowUpDecision
- test_feedback_evals.py
- interviews_log.py
- test_knowledge_postgres.py
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_feedback_contract.py
- KnowledgeRepository
- Feature: Context Management for the Interview LLM Calls
- test_feedback_context.py
- Completed Steps
- QuestionTurn
- test_reply_contract.py
- Feature: LLM as the Interviewer (it asks the questions)
- interviews_answer_service.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- SessionStatus
- interviews_schema.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- JobRole
- interviews_model.py
- InterviewerInputs
- test_context_prompts.py
- test_create_interview.py
- test_start_llm.py
- Completed Steps
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
- interviews_write_stream.py
- ._run
- AnswerOut
- test_eval_runs.py
- QuestionCategory
- exception_handlers.py
- interviews_feedback_service.py
- FakeLangfuse
- interviews_feedback_controller.py
- FakeProvider
- experiments
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- EmbeddingKind
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- interviews_feedback.py
- test_reference_note_context.py
- ContextManager
- Feature: Follow-up Questions (decide / write split)
- decision
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- FakeClient
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
- Implementation Plan: Start an Interview (backend)
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- llm
- main
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- LLMError
- Langfuse
- test_evals.py
- test_turn_budget.py
- test_transcript.py
- LLMResult
- Langfuse Implementation Notes
- interviewer_v5.md
- Feature: Langfuse experiments for the interviews evals
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Implementation Plan: UUID primary keys
- InterviewMessage
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation: Three New Interview Roles (designer, qa, devops)
- LLMRateLimitError
- Feature: Interview History List (backend)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- test_stream_answer.py
- Implementation: Interview History List (backend)
- Judge Calibration
- text
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- run_task
- Langfuse Implementation Notes
- pytest
- test_knowledge_ingest.py
- ._ordered
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- Implementation: Layered Modules (route -> controller -> service -> repository)
- Langfuse CI/CD
- Prompt Engineering
- test_context_controller.py
- interviews_start_dependencies.py
- test_generation_eval.py
- experiment
- test_start_reference_notes.py
- WriteText
- interviews_knowledge_ingest.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- test_select_questions.py
- TranscriptionOut
- Tracer
- test_answer_interview.py
- Feature: Role-Based Access Control (single JWT)
- test_list_users.py
- ErrorResponse
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- RequestContextMiddleware
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- StrEnum
- 9b4e2d7c1a35_add_knowledge_chunks.py
- audio_container
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- ChatMessage
- feedback_score_v1.md
- feedback_write_v1.md
- test_me.py
- interviews_controller.py
- .record_turn
- Slices in detail
- interviews_constants.py
- Langfuse CLI Reference
- Feature: Layered Modules (route -> controller -> service -> repository)
- test_job_description_summary.py
- Learn: Splitting the interviews dependency wiring
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- Langfuse
- users_utils.py
- _reset_request_id
- test_retrieval_eval.py
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
- hints_of
- Communication and priorities
- Engineering habits
- Senior judgement
- FeedbackThread
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- RubricCriterion
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- interviews/conftest.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- Implementation Plan: Role-Based Access Control (single JWT)
- WithReferenceNotes
- _settings
- follow_up_decision_v2.md
- bank
- traces
- client
- Transcriber
- 2. Langfuse Documentation
- compute_overall
- Clock
- Clock
- ProviderConfig
- Functional
- lf

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 112 edges
2. `FakeProvider` - 106 edges
3. `JobRole` - 104 edges
4. `User` - 100 edges
5. `LLMResult` - 94 edges
6. `Level` - 89 edges
7. `InterviewQuestion` - 88 edges
8. `InterviewType` - 87 edges
9. `QuestionCategory` - 86 edges
10. `InterviewsRepository` - 81 edges

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

## Communities (269 total, 46 thin omitted)

### Community 0 - "User"
Cohesion: 0.08
Nodes (42): hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), get_service(), Depends, Session (+34 more)

### Community 1 - "LLMServerError"
Cohesion: 0.09
Nodes (19): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, _int_or_none(), Any (+11 more)

### Community 2 - "AnswerService"
Cohesion: 0.12
Nodes (22): QuestionNotCurrentError, AnswerController, UUID, The checks and reads before the stream opens (sync DB work: the route runs it…, AnswerIn, AnswerService, _elapsed_ms(), AnswerEvent (+14 more)

### Community 3 - "decode_token"
Cohesion: 0.12
Nodes (32): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+24 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.12
Nodes (54): log_retrieval(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, Which reference notes an interview got at start: mode, count, scores and the…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn() (+46 more)

### Community 5 - "interviews_route.py"
Cohesion: 0.07
Nodes (57): alias, AnswerControllerDep, ForbiddenError, Permission, permissions_for(), The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates… (+49 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (98): notes_fingerprint(), A short id for the ingested notes: changes when any note changes, not when the…, _arm_notes(), ArmInterview, ArmSummary, build_sheet(), case_set_problems(), competencies_of() (+90 more)

### Community 8 - "interviews_knowledge_utils.py"
Cohesion: 0.08
Nodes (49): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+41 more)

### Community 9 - "Role"
Cohesion: 0.08
Nodes (36): health_check(), StrEnum, Role, list_users(), PageDep, CurrentUserDep, raise_conflict(), raise_crash() (+28 more)

### Community 10 - "interviews_reply.py"
Cohesion: 0.14
Nodes (28): load_object(), parse_decision_reply(), BaseModel, The contract for what the interviewer LLM must reply, and the check that…, The reply as a JSON object: one optional fence around it, nothing else before…, The decide call suggests; the code still applies the follow-up cap and the time…, A follow-up carries no category: it inherits its main question's, so the model…, _RawDecision (+20 more)

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
Nodes (29): _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored(), test_api_key_never_shows_in_repr_or_errors() (+21 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.06
Nodes (81): Band, _band_check(), check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for(), feedback_run_scores(), feedback_scores_for() (+73 more)

### Community 18 - "interviews_log.py"
Cohesion: 0.16
Nodes (11): Call, _int(), NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer., The requests that logged this session, oldest first: the start, then one…, Turn (+3 more)

### Community 19 - "test_knowledge_postgres.py"
Cohesion: 0.16
Nodes (18): alembic_config, cosine_similarity(), 1 = same direction (same meaning), 0 = unrelated, -1 = opposite. Length is…, os, cuewise-be, Development database (Postgres 18 + pgvector), Reference notes (knowledge-base RAG), alembic_config() (+10 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.16
Nodes (34): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase (+26 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.05
Nodes (86): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, Who wrote the feedback text: the write call, or the code's template when that…, TextSource, get_feedback_limiter() (+78 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.07
Nodes (23): 6. Try it yourself, assert_one_terminal(), follow_up_json(), message_count(), anyio, fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events… (+15 more)

### Community 31 - "test_feedback_contract.py"
Cohesion: 0.24
Nodes (27): assess_evidence(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The pre-check, before any LLM call: enough main questions have a real answer to…, parametrize, question_json(), The feedback contract (interviews_feedback.py): the code pre-check, the score…, reason_of() (+19 more)

### Community 32 - "KnowledgeRepository"
Cohesion: 0.08
Nodes (29): Embedder, Protocol, KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a…, _embed() (+21 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "test_feedback_context.py"
Cohesion: 0.18
Nodes (22): FeedbackScore, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, The score call: every thread whole, nothing droppable. Over its own limit it…, Evidence (+14 more)

### Community 35 - "Completed Steps"
Cohesion: 0.14
Nodes (22): Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, EligibleChunk, NamedTuple, The k eligible chunks embedded with `model` that are most similar to the query,…, The notes stored for this interview at start, rank order; none for interviews… (+14 more)

### Community 36 - "QuestionTurn"
Cohesion: 0.05
Nodes (60): StrategyOutput, _counts(), FeedbackWrite, FullHistory, JobDescriptionSummary, An earlier question as the model would have written it. A follow-up was written…, App data at the end of the last user message; untrusted parts (questions,…, The write call: scores, evidence and question texts only; small whatever the… (+52 more)

### Community 37 - "test_reply_contract.py"
Cohesion: 0.21
Nodes (23): Slice 3: Structured follow-up decisions, follow_up(), parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_follow_up_in_a_behavioral_only_interview_keeps_the_behavioral_category() (+15 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "interviews_answer_service.py"
Cohesion: 0.10
Nodes (33): anyio, ContextReport, _log(), NamedTuple, Context management: the one place that decides what each LLM call sends. The…, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or…, OpenAI-compatible chat completions over plain httpx (Google AI Studio,… (+25 more)

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
Cohesion: 0.13
Nodes (30): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+22 more)

### Community 44 - "SessionStatus"
Cohesion: 0.16
Nodes (17): HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, _history_filter(), _history_order(), A page of the user's sessions in the requested order, each with the main-…, The rows one user's history lists and counts: always only their own, optionally… (+9 more)

### Community 45 - "interviews_schema.py"
Cohesion: 0.12
Nodes (35): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), _error_event(), _event(), _frame(), AnswerEvent, BaseModel (+27 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.07
Nodes (25): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank). (+17 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.11
Nodes (20): drain(), Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), test_call_without_labels_still_gets_a_name(), test_close_on_a_disabled_tracer_does_nothing(), test_complete_records_one_generation_with_full_content_and_usage(), test_disabled_tracer_is_a_pass_through(), test_failed_call_is_marked_error_and_the_same_exception_is_raised() (+12 more)

### Community 49 - "JobRole"
Cohesion: 0.09
Nodes (54): InterviewType, JobRole, Level, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, FeedbackEvalSetup, One interview's main questions through the streamed writer's text format (the…, simulate_main_questions() (+46 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.07
Nodes (34): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, portable_vector() (+26 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.11
Nodes (43): InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, apply_limits(), _decision_label(), plan_write(), UUID (+35 more)

### Community 52 - "test_context_prompts.py"
Cohesion: 0.15
Nodes (23): A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), load_prompt(), Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt(), Testing Strategy (+15 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.17
Nodes (18): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back() (+10 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "Completed Steps"
Cohesion: 0.50
Nodes (5): One streamed-turn event as the dict sse-starlette encodes: the event name, and…, The controller's events as SSE frames. Closing this (a client that left) closes…, sse_frame(), sse_frames(), Completed Steps

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (64): QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, A main question opens a thread; a follow-up digs into the latest answer of that…, _Interview, The interview as plain values, read before the claim's commit expires the…, group_requests(), LogEvent (+56 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.14
Nodes (31): LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget() (+23 more)

### Community 59 - "Implementation: Error Handling"
Cohesion: 0.11
Nodes (18): RequestIdFilter, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions (+10 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.08
Nodes (29): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Any, datetime, Session, UUID (+21 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.22
Nodes (13): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), sys, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success() (+5 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_follow_ups.py"
Cohesion: 0.15
Nodes (24): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+16 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.15
Nodes (28): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), parametrize, RetrievalService.retrieve: the vector / filter / skip ladder (knowledge-base-…, A stand-in tracer that records each step's metadata and output. (+20 more)

### Community 66 - "test_context.py"
Cohesion: 0.17
Nodes (15): estimate_tokens(), Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default() (+7 more)

### Community 67 - "interviews_write_stream.py"
Cohesion: 0.09
Nodes (39): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., decide(), UUID, The decide step of an answer turn: the model suggests following up or moving…, At most two attempts within the decide cap; any failure means "next_question"…, log_embedding_call() (+31 more)

### Community 68 - "._run"
Cohesion: 0.39
Nodes (6): _Claim, _Outcome, Any, NamedTuple, Too little to assess (the code's pre-check, or the model's flag): final, with…, How a generation ended, for the trace (metadata only).

### Community 69 - "AnswerOut"
Cohesion: 0.15
Nodes (14): AnswerOut, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Functional, Goal (+6 more)

### Community 71 - "test_eval_runs.py"
Cohesion: 0.05
Nodes (62): ExperimentRun, NamedTuple, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), Any (+54 more)

### Community 72 - "QuestionCategory"
Cohesion: 0.09
Nodes (46): _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, _normalized(), parse_interviewer_reply(), parse_streamed_reply(), Exception (+38 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "interviews_feedback_service.py"
Cohesion: 0.08
Nodes (43): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody, FeedbackFailedError, FeedbackInProgressError (+35 more)

### Community 75 - "FakeLangfuse"
Cohesion: 0.10
Nodes (6): contextvars, FakeLangfuse, A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and…, A step (chain) or span opened inside a task: recorded with the item it belongs…, A check (guardrail) or generation started inside a task., types

### Community 76 - "interviews_feedback_controller.py"
Cohesion: 0.20
Nodes (13): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, get_feedback_controller(), FeedbackEvidenceOut (+5 more)

### Community 77 - "FakeProvider"
Cohesion: 0.16
Nodes (25): FakeProvider, run_case(), Deviations from Plan, long_case(), noted(), reply(), test_a_passing_case_has_no_hints(), test_a_provider_error_fails_the_case_without_crashing() (+17 more)

### Community 78 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

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
Cohesion: 0.09
Nodes (37): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, EmbedCall (+29 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Assumptions to verify, Blockers, Constraints, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal (+6 more)

### Community 84 - "interviews_feedback.py"
Cohesion: 0.13
Nodes (25): _has_markup(), _normalized(), BaseModel, _question_score(), QuestionScore, End-of-interview feedback: what the score and write calls must return, and the…, Case and whitespace don't make a quote different; anything else (words,…, Plain, stiff, always valid: built from the stored scores and the score call's… (+17 more)

### Community 85 - "test_reference_note_context.py"
Cohesion: 0.23
Nodes (17): 5. What can go wrong, first_user(), inputs(), _max_note(), anyio, parametrize, Reference notes in the question writer's input (knowledge-base-rag Step 9;…, test_a_follow_up_write_gets_no_notes_and_the_plain_prompt() (+9 more)

### Community 86 - "ContextManager"
Cohesion: 0.28
Nodes (14): ContextManager, Task, build_context_manager(), `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WindowLedger, test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), test_the_guard_never_drops_the_current_thread() (+6 more)

### Community 87 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 88 - "decision"
Cohesion: 0.26
Nodes (19): 5. What can go wrong, decision(), labelled_cases(), last_line(), run_decide(), scores_on(), test_a_failed_decision_shows_the_verdict_the_decision_and_the_expected_one(), test_a_langfuse_failure_still_runs_every_case_once_and_exits_0() (+11 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "FakeClient"
Cohesion: 0.10
Nodes (10): FakeClient, FakeObservation, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_reports_whether_it_was_sent(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises(), test_steps_and_checks_are_no_ops_when_off_and_never_raise_when_langfuse_fails(), test_trace_with_a_broken_sdk_still_runs_the_body_and_keeps_its_exception() (+2 more)

### Community 93 - "hint_for"
Cohesion: 0.14
Nodes (14): A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, 4. How it works, Deviations from Plan, inspect, parametrize (+6 more)

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
Nodes (44): build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, TracingProvider, model_validator (+36 more)

### Community 104 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.09
Nodes (22): Affected Files & Patterns, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules, Overview, Project Rules Applied (+14 more)

### Community 105 - "test_answer_llm.py"
Cohesion: 0.12
Nodes (21): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), itertools, messages(), questions(), Answer every question of a started interview; returns the list of answer… (+13 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.06
Nodes (76): anyio_from_thread, LLMProvider, Protocol, build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, Local time, as the Langfuse list shows the run's start: the name and the…, run_stamp(), _action_and_gap() (+68 more)

### Community 109 - "llm"
Cohesion: 0.20
Nodes (8): as_v5_text(), llm(), script(), script_score(), script_write(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY…

### Community 110 - "main"
Cohesion: 0.10
Nodes (31): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+23 more)

### Community 111 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

### Community 112 - "LLMError"
Cohesion: 0.05
Nodes (45): LLMError, LLMTimeoutError, Exception, Base for every provider failure. `retryable` marks faults that may pass on…, backoff_seconds(), Random, Retry rules shared by every vendor client in `core/ai` (the LLM provider and…, How long to wait before retrying `exc` after `attempt` attempts, or None to… (+37 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "test_evals.py"
Cohesion: 0.13
Nodes (28): check_decision(), load_cases(), Path, The decide reply against the case's label; the injection check reads the raw…, Slice 6: Feedback and scoring, failed(), labelled(), parametrize (+20 more)

### Community 115 - "test_turn_budget.py"
Cohesion: 0.20
Nodes (15): Testing Strategy, Testing Strategy, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result() (+7 more)

### Community 116 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 117 - "LLMResult"
Cohesion: 0.12
Nodes (26): BuiltContext, LLMResult, BaseModel, ScoreResult, _Attempts, CallUsage, FeedbackGenerator, log_feedback_summary() (+18 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.13
Nodes (14): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional (+6 more)

### Community 121 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Architecture & Design, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview (+6 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "InterviewMessage"
Cohesion: 0.11
Nodes (20): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_a_future_question_is_not_current_either() (+12 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+5 more)

### Community 125 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.08
Nodes (18): 9. Still open, Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Known Issues, Links, Open Questions (+10 more)

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
Cohesion: 0.36
Nodes (10): 5. What can go wrong, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing(), test_the_first_event_is_sent_before_any_llm_call_returns() (+2 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "text"
Cohesion: 0.13
Nodes (13): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites, text(), 1. Inventory every prompt (before writing any code) (+5 more)

### Community 134 - "build_usage_report"
Cohesion: 0.20
Nodes (16): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, main(), Session, Print stored LLM usage per interview: tokens per question position and per…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind() (+8 more)

### Community 135 - "The fundamentals"
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+17 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "run_task"
Cohesion: 0.23
Nodes (14): console_number(), The trace id the fake gives a case in the given repeat's run (write and stream…, run_task(), test_a_failed_check_is_scored_false_with_its_detail(), test_a_provider_error_scores_the_case_failed_and_errored_with_the_class(), down(), test_a_write_result_shows_the_reply_and_the_notes_but_no_expected_action(), test_a_write_run_per_repeat_carries_what_produced_it() (+6 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "pytest"
Cohesion: 0.08
Nodes (14): pytest, parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text(), fixture, parametrize (+6 more)

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.22
Nodes (23): IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, active(), chunks(), corpus(), FailingOn, interview() (+15 more)

### Community 144 - "PageParams"
Cohesion: 0.08
Nodes (35): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewListOut (+27 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 151 - "interviews_start_dependencies.py"
Cohesion: 0.11
Nodes (45): get_answer_controller(), get_answer_service(), Depends, Session, get_feedback_service(), datetime, Depends, Session (+37 more)

### Community 152 - "test_generation_eval.py"
Cohesion: 0.06
Nodes (58): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional (+50 more)

### Community 154 - "experiment"
Cohesion: 0.22
Nodes (12): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+4 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "WriteText"
Cohesion: 0.27
Nodes (9): _check_lengths(), parse_write_reply(), The labelled text the write call is asked for (the parser reads it back…, The write call's text, slot by slot: every section once and in order, list…, _slots(), WriteText, test_a_valid_write_reply_is_parsed_into_slots(), test_blank_lines_and_a_wrapped_summary_are_accepted() (+1 more)

### Community 157 - "interviews_knowledge_ingest.py"
Cohesion: 0.24
Nodes (14): main(), _parser(), ArgumentParser, Session, Ingest the reference notes into the database (knowledge-base RAG). uv run…, ingest(), Path, The ingest command: python -m… (+6 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "test_select_questions.py"
Cohesion: 0.09
Nodes (41): NotEnoughQuestionsError, BankQuestion, One entry of the hand-written question bank file., load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 1. Why it exists (+33 more)

### Community 160 - "TranscriptionOut"
Cohesion: 0.15
Nodes (11): Reload rows a commit expired, so reading their fields later needs no database…, POST /interviews/{id}/transcriptions: what the candidate said, for them to…, TranscriptionOut, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me (+3 more)

### Community 161 - "Tracer"
Cohesion: 0.04
Nodes (54): AbstractContextManager, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Send what is still buffered, then stop the background exporter. Called once at… (+46 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 164 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 165 - "ErrorResponse"
Cohesion: 0.05
Nodes (45): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+37 more)

### Community 166 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Implementation Steps, Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 167 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "StrEnum"
Cohesion: 0.13
Nodes (19): MessageKind, MessageRole, StrEnum, Transcript item kinds: a question comes from interview_questions, the other two…, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut, build_transcript(), The chat as the user saw it: each question, then its answer and reaction when… (+11 more)

### Community 170 - "9b4e2d7c1a35_add_knowledge_chunks.py"
Cohesion: 0.40
Nodes (3): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, pgvector_sqlalchemy

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
Cohesion: 0.09
Nodes (20): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, OpenAICompatibleProvider, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Same request with `stream: true`: chunks as they arrive, then the final… (+12 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 178 - "interviews_controller.py"
Cohesion: 0.28
Nodes (12): interview_out(), InterviewsController, UUID, question_out(), Interview lifecycle: request -> InterviewsService, domain result -> response…, InterviewCreateIn, InterviewOut, BaseModel (+4 more)

### Community 179 - ".record_turn"
Cohesion: 0.10
Nodes (19): Save one whole turn in one commit: advance the session, the answer, the…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+11 more)

### Community 180 - "Slices in detail"
Cohesion: 0.20
Nodes (10): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 7: Eval maturity (trust the judge, catch regressions), Slice 9: Tool use and agents, Slice: Context management (added after Slice 2) (+2 more)

### Community 181 - "interviews_constants.py"
Cohesion: 0.11
Nodes (21): get_db(), Session, Voice answers: request -> TranscriptionService, text -> TranscriptionOut. The…, get_transcription_controller(), get_transcription_service(), Depends, Session, Create the first admin, or promote an existing user to admin. Usage: uv run… (+13 more)

### Community 182 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 183 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Requirements, User Flow (+1 more)

### Community 184 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 185 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

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
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.18
Nodes (21): embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, 15 cases with the kinds the label rules require: most expect API design first;…, run() (+13 more)

### Community 220 - "Generation"
Cohesion: 0.16
Nodes (9): Generation, _model_parameters(), ReasoningEffort, The stream was closed before it finished (client left, or the turn's deadline…, What the call asked the model for, shown on the generation. A temperature only…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, _usage_details(), Implementation Steps (+1 more)

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

### Community 234 - "hints_of"
Cohesion: 0.33
Nodes (10): hints_of(), mentions(), The hints on one case's result in Langfuse., test_a_cut_off_reply_hints_at_max_tokens_before_quality(), test_a_provider_error_hints_that_it_is_not_a_quality_problem(), test_a_reply_that_does_not_parse_hints_at_the_format(), test_a_right_action_with_a_different_gap_hints_at_an_ambiguous_label(), test_over_probing_a_normal_case_does_not_blame_an_injection() (+2 more)

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "FeedbackThread"
Cohesion: 0.32
Nodes (7): build_threads(), FeedbackThread, NamedTuple, One main question with its follow-ups and every answer: what one set of scores…, Stored rows as plain values, one thread per main question in interview order (a…, ThreadTurn, test_threads_group_follow_ups_under_their_main_question_in_order()

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

### Community 244 - "RubricCriterion"
Cohesion: 0.40
Nodes (4): model_validator, Self, One criterion of the feedback rubric: what it asks, an anchor per score, and…, RubricCriterion

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "interviews/conftest.py"
Cohesion: 0.08
Nodes (29): Affected Files & Patterns, Step 2: Event contract, answer(), _answer(), anyio_backend(), _bank_question(), _decision_json(), make_bank_question() (+21 more)

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.22
Nodes (8): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Trade-offs & Rationale

### Community 250 - "_settings"
Cohesion: 0.50
Nodes (4): _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 251 - "follow_up_decision_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 252 - "bank"
Cohesion: 0.29
Nodes (7): Acceptance Criteria, Acceptance Criteria, Edge Cases, Test Results, Deviations from Plan, bank(), Small fixture bank wired into the app instead of the shipped mock file; mutable…

### Community 253 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 254 - "client"
Cohesion: 0.67
Nodes (3): client(), propagated(), fixture

### Community 255 - "Transcriber"
Cohesion: 0.33
Nodes (4): Protocol, Transcriber, Affected Files & Patterns, Project Conventions

### Community 256 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 257 - "compute_overall"
Cohesion: 0.47
Nodes (6): compute_overall(), The mean of every criterion score of every main question, rounded half up to…, 6. Try it yourself, score(), test_the_overall_is_the_mean_of_every_criterion_score(), test_the_overall_rounds_half_up_to_one_decimal()

### Community 258 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 260 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 267 - "Functional"
Cohesion: 0.67
Nodes (3): Functional, Non-Functional, Requirements

### Community 268 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

## Knowledge Gaps
- **784 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+779 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1838 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **46 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `AnswerService`, `interviews_rag_evals.py`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `interviews_start_dependencies.py`, `test_generation_eval.py`, `experiment`, `test_feedback_endpoint.py`, `KnowledgeRepository`, `Completed Steps`, `interviews_answer_service.py`, `ChatMessage`, `test_tracing.py`, `interviews_constants.py`, `test_tracing_routes.py`, `InterviewQuestion`, `test_eval_runs.py`, `interviews_feedback_service.py`, `experiments`, `test_retrieval_eval.py`, `decision`, `Generation`, `hint_for`, `FakeClient`, `test_factory.py`, `interviews_evals.py`, `test_evals.py`, `LLMResult`, `Feature: Langfuse experiments for the interviews evals`, `traces`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `AnswerService`, `test_interview_report.py`, `build_usage_report`, `interviews_reply.py`, `test_list_interviews.py`, `test_context_controller.py`, `test_feedback_endpoint.py`, `test_answer_stream.py`, `test_feedback_contract.py`, `QuestionTurn`, `interviews_answer_service.py`, `StrEnum`, `interviews_schema.py`, `JobRole`, `interviews_controller.py`, `interviews_model.py`, `.record_turn`, `interviews_constants.py`, `test_create_interview.py`, `test_start_llm.py`, `interviews_report.py`, `test_follow_ups.py`, `interviews_feedback.py`, `test_answer_llm.py`, `FeedbackThread`, `test_turn_budget.py`, `test_transcript.py`, `LLMResult`, `InterviewMessage`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Why does `JobRole` connect `JobRole` to `AnswerService`, `interviews_rag_evals.py`, `interviews_knowledge_utils.py`, `pytest`, `test_feedback_evals.py`, `test_stream_turn.py`, `test_context_strategies.py`, `test_select_questions.py`, `test_feedback_context.py`, `QuestionTurn`, `Implementation Plan: Three New Interview Roles (designer, qa, devops)`, `interviews_answer_service.py`, `StrEnum`, `SessionStatus`, `interviews_schema.py`, `test_llm_settings_default_to_off_with_documented_limits`, `test_transcribe.py`, `interviews_controller.py`, `InterviewerInputs`, `test_context_prompts.py`, `interviews_constants.py`, `interviews_report.py`, `QuestionCategory`, `interviews_feedback_service.py`, `Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)`, `test_retrieval_eval.py`, `test_reference_note_context.py`, `interviews_evals.py`, `interviews/conftest.py`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 42 INFERRED edges - model-reasoned connections that need verification._