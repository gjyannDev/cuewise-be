# Graph Report - cuewise-be  (2026-11-12)

## Corpus Check
- 354 files · ~310,471 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 4795 nodes · 13545 edges · 260 communities (220 shown, 40 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2592 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `99762d63`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- auth_service.py
- Implementation Plan: Langfuse Tracing
- interviews_answer_service.py
- decode_token
- test_interview_report.py
- interviews_route.py
- Cuewise BE — Project Instructions
- test_rag_evals.py
- interviews_knowledge_utils.py
- test_guards.py
- interviews_evals.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- Feature: Interview Feedback and Scoring (Slice 6)
- test_feedback_evals.py
- Checks
- cuewise-be
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- interview
- test_context_strategies.py
- test_answer_stream.py
- test_feedback_contract.py
- Completed Steps
- Feature: Context Management for the Interview LLM Calls
- test_feedback_context.py
- interviews_retrieval_service.py
- ContextManager
- User
- interviews/conftest.py
- GoogleEmbedder
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- RateLimiter
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
- FeedbackStatus
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- tests/conftest.py
- test_tracing_routes.py
- InterviewsRepository
- ConsoleFormatter
- job_description_summary_v2.md
- test_follow_ups.py
- FakeEmbedder
- test_fallback_pick.py
- interviews_constants.py
- interviews_feedback_service.py
- interviews_utils.py
- run_cases
- FollowUpAction
- exception_handlers.py
- errors.py
- FakeLangfuse
- interviews_feedback_controller.py
- test_evals.py
- experiments
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- interviews_transcription_dependencies.py
- LLMBadResponseError
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- interviews_feedback.py
- ChatMessage
- _Stt
- Implementation: Langfuse experiments for the interviews evals
- FakeClient
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- RecordingClient
- hint_for
- Langfuse Observability
- interviewer_v3.md
- Implementation: LLM as the Interviewer (it asks the questions)
- test_question_bank.py
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_factory.py
- test_get_interview.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- InvalidReplyError
- run_ranking
- main
- Implementation: Eval runs in Langfuse (scores + datasets)
- Feature: Langfuse Tracing
- Langfuse
- test_streamed_reply.py
- json
- test_transcript.py
- Implementation: Three New Interview Roles (designer, qa, devops)
- Langfuse Implementation Notes
- interviewer_v5.md
- Feature: Langfuse experiments for the interviews evals
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Implementation Plan: UUID primary keys
- test_answer_guards.py
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_reply_contract.py
- LLMRateLimitError
- Feature: Interview History List (backend)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- Learn: Streaming and latency (Slice 4, SSE)
- Implementation: Interview History List (backend)
- Judge Calibration
- text
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- follow_up
- Langfuse Implementation Notes
- test_request_context.py
- test_knowledge_ingest.py
- interviews_feedback_evals.py
- Implementation Steps
- Langfuse v4 project migration
- Judge Calibration
- Feature: Follow-up Questions (decide / write split)
- Langfuse CI/CD
- Prompt Engineering
- test_feedback_endpoint.py
- interviews_start_dependencies.py
- test_generation_eval.py
- Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)
- test_start_reference_notes.py
- Learn: Adding interview roles (designer, qa, devops)
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- test_select_questions.py
- traced
- Tracer
- test_answer_interview.py
- LLMProvider
- InterviewQuestion
- ErrorResponse
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- RequestContextMiddleware
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_context_controller.py
- types.py
- row
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- LLMServerError
- feedback_score_v1.md
- feedback_write_v1.md
- pytest
- InterviewsService
- .record_turn
- Slices in detail
- AI Engineering Learning Path (Cuewise)
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Layered Modules (route -> controller -> service -> repository)
- test_job_description_summary.py
- Learn: Splitting the interviews dependency wiring
- test_list_users.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- tracing.py
- users_utils.py
- _reset_request_id
- parse_log
- test_retrieval_eval.py
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
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
- Implementation Plan: Interview History List (backend)
- Communication and priorities
- Engineering habits
- Senior judgement
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- Implementation Plan: Role-Based Access Control (single JWT)
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- StreamedTurn
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- fixture
- Slice 8: Embeddings and RAG (split into 8a to 8e)
- test_user_ids.py
- ProviderConfig
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

## Communities (260 total, 40 thin omitted)

### Community 0 - "auth_service.py"
Cohesion: 0.11
Nodes (27): hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), register() (+19 more)

### Community 1 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.09
Nodes (18): Generation, _model_parameters(), ReasoningEffort, The stream was closed before it finished (client left, or the turn's deadline…, What the call asked the model for, shown on the generation. A temperature only…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, _usage_details(), Blockers & Resolutions (+10 more)

### Community 2 - "interviews_answer_service.py"
Cohesion: 0.17
Nodes (19): QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, A main question opens a thread; a follow-up digs into the latest answer of that…, One answer turn: the checks and reads, the LLM interviewer (or the bank), and…, Condense a long job description once, so later calls send less. One attempt…, bank_question(), interviewer_inputs() (+11 more)

### Community 3 - "decode_token"
Cohesion: 0.12
Nodes (32): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+24 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (54): analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start(), html_for() (+46 more)

### Community 5 - "interviews_route.py"
Cohesion: 0.09
Nodes (49): AnswerControllerDep, ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, get_current_user() (+41 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_rag_evals.py"
Cohesion: 0.09
Nodes (44): ArmSummary, build_sheet(), case_set_problems(), competencies_of(), filter_baseline(), Collection, Exception, NamedTuple (+36 more)

### Community 8 - "interviews_knowledge_utils.py"
Cohesion: 0.09
Nodes (43): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+35 more)

### Community 9 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 10 - "interviews_evals.py"
Cohesion: 0.04
Nodes (106): anyio_from_thread, build_tracer(), ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, final_line(), git_commit() (+98 more)

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

### Community 16 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.08
Nodes (59): check_feedback(), criterion_spread(), feedback_hints_for(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult, level_gap_check(), _print_case() (+51 more)

### Community 18 - "Checks"
Cohesion: 0.40
Nodes (5): Checks, bad_parent(), _consistency(), Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers…

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.10
Nodes (44): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Delta, PhaseChanged, StrEnum, What one answer turn of the LLM interviewer hands around: its action, its… (+36 more)

### Community 28 - "interview"
Cohesion: 0.20
Nodes (23): interview(), post(), parametrize, Insert a stored interview: one main question per answer, optional follow-ups…, rows_of(), test_a_failed_score_step_is_an_error_in_the_trace(), test_a_failing_write_call_falls_back_to_the_template_and_keeps_the_scores(), test_a_fresh_generating_row_answers_409() (+15 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.06
Nodes (74): build_interviewer_messages(), job_description_block(), Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't…, The full input for one call (the model has no memory, so the whole interview is…, render_interviewer_prompt(), render_template() (+66 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (18): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+10 more)

### Community 31 - "test_feedback_contract.py"
Cohesion: 0.20
Nodes (30): assess_evidence(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The pre-check, before any LLM call: enough main questions have a real answer to…, parametrize, question_json(), The feedback contract (interviews_feedback.py): the code pre-check, the score…, reason_of() (+22 more)

### Community 32 - "Completed Steps"
Cohesion: 0.07
Nodes (38): Embedder, Protocol, log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, EligibleChunk, KnowledgeRepository, NamedTuple, Session (+30 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "test_feedback_context.py"
Cohesion: 0.18
Nodes (22): FeedbackScore, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, The score call: every thread whole, nothing droppable. Over its own limit it…, Evidence (+14 more)

### Community 35 - "interviews_retrieval_service.py"
Cohesion: 0.11
Nodes (29): EmbeddingSizeError, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, Gemini embeddings through Google's native `batchEmbedContents` endpoint, over…, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Step, log_retrieval(), Which reference notes an interview got at start: mode, count, scores and the… (+21 more)

### Community 36 - "ContextManager"
Cohesion: 0.04
Nodes (71): ContextManager, ContextReport, _log(), Any, NamedTuple, Protocol, How many oldest entries may be dropped; everything else is required., Strategy (+63 more)

### Community 37 - "User"
Cohesion: 0.14
Nodes (17): User, AuthRepository, Session, UUID, UUID, Voice answers: request -> TranscriptionService, text -> TranscriptionOut. The…, TranscriptionController, POST /interviews/{id}/transcriptions: what the candidate said, for them to… (+9 more)

### Community 38 - "interviews/conftest.py"
Cohesion: 0.05
Nodes (46): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+38 more)

### Community 39 - "GoogleEmbedder"
Cohesion: 0.15
Nodes (8): EmbeddingResult, BaseModel, GoogleEmbedder, Any, BaseTransport, Random, Response, _make()

### Community 40 - "test_layers.py"
Cohesion: 0.05
Nodes (47): ast, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open (+39 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (29): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+21 more)

### Community 44 - "RateLimiter"
Cohesion: 0.20
Nodes (11): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, math, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window() (+3 more)

### Community 45 - "interviews_schema.py"
Cohesion: 0.06
Nodes (67): QuestionNotCurrentError, The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), AnswerController, _error_event(), _event(), _frame() (+59 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.06
Nodes (32): BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, Acceptance Criteria, Blockers, Constraints, Edge Cases (+24 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.10
Nodes (10): client(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, _settings(), test_both_keys_build_an_enabled_tracer(), test_close_on_a_disabled_tracer_does_nothing(), test_no_keys_builds_a_disabled_tracer_without_warning() (+2 more)

### Community 49 - "JobRole"
Cohesion: 0.17
Nodes (26): InterviewType, JobRole, Level, EvalSetup, FeedbackEvalSetup, One interview's main questions through the streamed writer's text format (the…, simulate_main_questions(), Per-interview constants and the rubric only: no answer or job-description text… (+18 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.05
Nodes (52): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+44 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.12
Nodes (35): InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, apply_limits(), plan_write(), The code's say over the model's: returns the action and why it overrode the…, After the decision: the code's limits pick the action, and whether a write call… (+27 more)

### Community 52 - "test_context_prompts.py"
Cohesion: 0.13
Nodes (22): load_prompt(), Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt(), render_interviewer_v2_prompt(), parametrize, test_a_valid_note_is_returned_trimmed(), test_a_valid_summary_is_returned_trimmed() (+14 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.16
Nodes (19): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+11 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "FeedbackStatus"
Cohesion: 0.25
Nodes (14): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, 5. What can go wrong, happy(), score_json(), test_a_mixed_interview_scores_each_question_on_its_own_categorys_criteria(), test_a_request_whose_row_was_taken_over_stores_nothing(), test_a_second_post_during_generation_gets_409_and_one_row_exists() (+6 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (27): LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider() (+19 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (63): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+55 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "tests/conftest.py"
Cohesion: 0.05
Nodes (55): RequestIdFilter, health_check(), start_interview(), Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues (+47 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 61 - "InterviewsRepository"
Cohesion: 0.09
Nodes (20): InterviewSession, _history_filter(), InterviewsRepository, Any, datetime, Session, UUID, Any user's session, by id: for the report script only (the API always goes… (+12 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.18
Nodes (14): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), LogRecord, sys, _record(), test_console_appends_the_traceback() (+6 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): 5. What can go wrong, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.10
Nodes (38): EmbeddingKind, StrEnum, EmbedCall, FakeEmbedder, NamedTuple, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode (+30 more)

### Community 66 - "test_fallback_pick.py"
Cohesion: 0.27
Nodes (11): fixture_bank(), pick(), fixture, parametrize, test_general_and_role_specific_questions_are_both_eligible(), test_level_must_match(), test_mixed_alternates_starting_with_behavioral(), test_nothing_left_raises() (+3 more)

### Community 67 - "interviews_constants.py"
Cohesion: 0.06
Nodes (76): anyio, BuiltContext, ContextTooLargeError, Exception, Context management: the one place that decides what each LLM call sends. The…, Even with every droppable entry gone the input is over the strategy's limit., Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or… (+68 more)

### Community 68 - "interviews_feedback_service.py"
Cohesion: 0.12
Nodes (28): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, Who wrote the feedback text: the write call, or the code's template when that…, TextSource (+20 more)

### Community 69 - "interviews_utils.py"
Cohesion: 0.08
Nodes (42): HeaderSplit, InterviewerReply, NamedTuple, LevelGroup, MessageKind, MessageRole, QuestionCategory, Reactions are warmer for people early in their career and briefer for… (+34 more)

### Community 71 - "run_cases"
Cohesion: 0.10
Nodes (24): _evaluation(), Any, Score, Run every case once, in order, as one Langfuse experiment run; whatever the run…, run_cases(), item_scores(), C, 1. Why it exists (+16 more)

### Community 72 - "FollowUpAction"
Cohesion: 0.15
Nodes (25): parse_decision_reply(), BaseModel, The decide call suggests; the code still applies the follow-up cap and the time…, A follow-up carries no category: it inherits its main question's, so the model…, _RawDecision, _RawFollowUp, _RawReply, FollowUpAction (+17 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.11
Nodes (34): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+26 more)

### Community 74 - "errors.py"
Cohesion: 0.16
Nodes (22): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody, NoSpeechError, NotFoundError (+14 more)

### Community 75 - "FakeLangfuse"
Cohesion: 0.09
Nodes (15): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+7 more)

### Community 76 - "interviews_feedback_controller.py"
Cohesion: 0.25
Nodes (11): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, FeedbackEvidenceOut, FeedbackOut (+3 more)

### Community 77 - "test_evals.py"
Cohesion: 0.07
Nodes (93): FakeProvider, check_reply(), load_cases(), Path, Rule checks for one reply. Text checks look at the parsed question, or at the…, run_case(), 5. What can go wrong, Deviations from Plan (+85 more)

### Community 78 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "interviews_transcription_dependencies.py"
Cohesion: 0.13
Nodes (19): Protocol, Transcriber, RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., get_db(), Session, get_transcriber(), Built once at startup (app lifespan); None when no Deepgram key is configured… (+11 more)

### Community 82 - "LLMBadResponseError"
Cohesion: 0.16
Nodes (22): LLMBadResponseError, A 200 whose body is unusable (not JSON, no choices, blank text). Not transient,…, Clock, make_embedder(), ok(), fixture, parametrize, Response (+14 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "interviews_feedback.py"
Cohesion: 0.10
Nodes (36): _check_lengths(), compute_overall(), _has_markup(), _normalized(), parse_write_reply(), BaseModel, _question_score(), QuestionScore (+28 more)

### Community 85 - "ChatMessage"
Cohesion: 0.09
Nodes (28): estimate_tokens(), ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, Step 11: `FakeProvider.stream`, Reply (+20 more)

### Community 86 - "_Stt"
Cohesion: 0.28
Nodes (5): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank)., _Stt

### Community 87 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.15
Nodes (12): 13. Phase 2 real runs (yours), Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

### Community 88 - "FakeClient"
Cohesion: 0.10
Nodes (10): FakeClient, FakeObservation, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_reports_whether_it_was_sent(), test_sdk_failure_does_not_mask_the_llm_error(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises(), test_steps_and_checks_are_no_ops_when_off_and_never_raise_when_langfuse_fails() (+2 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "RecordingClient"
Cohesion: 0.15
Nodes (7): fresh_limiter(), fixture, Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, Fake wall clock for the claim token and the stale takeover., recording(), RecordingClient, wall()

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

### Community 97 - "test_question_bank.py"
Cohesion: 0.24
Nodes (13): load_bank(), load_rubric(), Path, Read and validate a feedback rubric file; a bad one fails loudly at startup,…, Read and validate a question bank file; a bad file fails loudly instead of at…, Test Results, _entry(), parametrize (+5 more)

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.15
Nodes (12): Baseline Failures, Commit message suggestion, Deviations from Plan, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

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
Cohesion: 0.07
Nodes (35): DeepgramTranscriber, AsyncBaseTransport, Random, build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and… (+27 more)

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "test_answer_llm.py"
Cohesion: 0.10
Nodes (25): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages() (+17 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "InvalidReplyError"
Cohesion: 0.05
Nodes (69): _check_question(), InvalidReplyError, load_object(), _normalized(), parse_interviewer_reply(), parse_streamed_reply(), Exception, interviewer_v5's finished question text, checked like a v4 reply. It was… (+61 more)

### Community 109 - "run_ranking"
Cohesion: 0.21
Nodes (19): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), Edge Cases, Test Results, arm_of(), fill(), generated(), posted() (+11 more)

### Community 110 - "main"
Cohesion: 0.16
Nodes (18): html_target(), main(), Path, Session, UUID, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines() (+10 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "test_streamed_reply.py"
Cohesion: 0.18
Nodes (17): interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), read(), parse(), parametrize, interviewer_v5's streamed reply: a `CATEGORY:` header line (next-question mode…, test_a_header_split_across_chunks_is_read_once_its_line_ends(), test_a_long_first_line_is_no_header_without_waiting_for_its_end() (+9 more)

### Community 115 - "json"
Cohesion: 0.18
Nodes (16): Testing Strategy, Baseline Failures, 7. What surprised me, json, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,… (+8 more)

### Community 116 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 117 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.08
Nodes (18): 9. Still open, Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Known Issues, Links, Open Questions (+10 more)

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
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "test_answer_guards.py"
Cohesion: 0.13
Nodes (14): message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_a_future_question_is_not_current_either(), test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing() (+6 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 126 - "LLMRateLimitError"
Cohesion: 0.11
Nodes (18): LLMRateLimitError, 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+10 more)

### Community 127 - "Feature: Interview History List (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "Learn: Streaming and latency (Slice 4, SSE)"
Cohesion: 0.10
Nodes (24): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+16 more)

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
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 135 - "The fundamentals"
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "follow_up"
Cohesion: 0.16
Nodes (13): Slice 3: Structured follow-up decisions, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+5 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.24
Nodes (20): active(), chunks(), corpus(), FailingOn, interview(), ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag…, Fails on the n-th embed call (1-based), then works again., rows() (+12 more)

### Community 143 - "interviews_feedback_evals.py"
Cohesion: 0.08
Nodes (31): build_threads(), FeedbackThread, NamedTuple, One main question with its follow-ups and every answer: what one set of scores…, Stored rows as plain values, one thread per main question in interview order (a…, ThreadTurn, Band, _band_check() (+23 more)

### Community 144 - "Implementation Steps"
Cohesion: 0.12
Nodes (19): Page, BaseModel, Offset pagination shared by every list endpoint, so clients see one query…, UsersController, get_controller(), get_service(), Depends, Session (+11 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_feedback_endpoint.py"
Cohesion: 0.23
Nodes (13): InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, POST and GET /api/v1/interviews/{id}/feedback: the end-to-end seam for the…, rows(), stored_scores_json(), test_a_second_post_returns_the_stored_feedback_with_no_llm_call(), test_a_stale_row_with_stored_scores_is_taken_over_and_only_the_write_call_runs() (+5 more)

### Community 151 - "interviews_start_dependencies.py"
Cohesion: 0.14
Nodes (35): get_answer_controller(), get_answer_service(), Depends, Session, get_bank(), get_clock(), get_context_manager(), get_embedder() (+27 more)

### Community 152 - "test_generation_eval.py"
Cohesion: 0.22
Nodes (17): lf(), fixture, quiet(), `run_generation` as Langfuse experiment runs (langfuse-experiments Step 11;…, The console with each arm row's start_ms (wall-clock time) dropped, and without…, A fake LLM: a new, valid main question per call; it can fail every call that…, run(), table_without_timings() (+9 more)

### Community 154 - "Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)"
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 8. Check your understanding, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "Learn: Adding interview roles (designer, qa, devops)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 8. Check your understanding, Learn: Adding interview roles (designer, qa, devops)

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.36
Nodes (10): pathlib, ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1(), test_an_invalid_note_names_the_file_writes_nothing_and_exits_1(), test_it_prints_the_counts_and_exits_0(), test_warnings_are_printed_without_note_text() (+2 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "test_select_questions.py"
Cohesion: 0.20
Nodes (21): NotEnoughQuestionsError, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 4. How it works, Implementation Steps, _bank(), parametrize, _q() (+13 more)

### Community 160 - "traced"
Cohesion: 0.25
Nodes (14): drain(), result(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage(), test_failed_call_is_marked_error_and_the_same_exception_is_raised(), test_missing_usage_is_omitted_never_guessed(), test_retried_call_is_one_generation_with_attempts(), test_sdk_failure_never_changes_the_llm_result() (+6 more)

### Community 161 - "Tracer"
Cohesion: 0.05
Nodes (56): AbstractContextManager, Any, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, A named step inside the current trace (a Langfuse `chain`): the generations and… (+48 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "LLMProvider"
Cohesion: 0.17
Nodes (7): LLMProvider, Protocol, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), Random, Random

### Community 164 - "InterviewQuestion"
Cohesion: 0.13
Nodes (18): InterviewMessage, InterviewQuestion, A candidate answer or the interviewer's reaction to one question. The questions…, A question as it was shown: written by the LLM, or snapshotted from the bank…, Every stored question, grouped by interview in creation order (UUIDv7), for the…, InterviewState, NamedTuple, UUID (+10 more)

### Community 165 - "ErrorResponse"
Cohesion: 0.04
Nodes (56): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+48 more)

### Community 166 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.15
Nodes (11): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 167 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 170 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 171 - "row"
Cohesion: 0.18
Nodes (9): FeedbackWrite, The write call: scores, evidence and question texts only; small whatever the…, row(), test_a_completed_interview_gets_scored_written_and_stored(), test_a_provider_error_fails_at_once_with_no_partial_scores(), test_an_interview_too_large_for_the_score_call_fails_without_a_call(), test_no_retry_when_the_budget_is_nearly_spent(), look() (+1 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.15
Nodes (16): Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+8 more)

### Community 174 - "LLMServerError"
Cohesion: 0.06
Nodes (38): _parse(), Response, The first channel's best transcript (blank for silence) and the reported audio…, _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport (+30 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "pytest"
Cohesion: 0.18
Nodes (9): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms() (+1 more)

### Community 178 - "InterviewsService"
Cohesion: 0.08
Nodes (44): alias, page_params(), PageParams, NamedTuple, Query, HistorySortColumn, StrEnum, The history columns GET /interviews sorts by; the values are the response's… (+36 more)

### Community 179 - ".record_turn"
Cohesion: 0.08
Nodes (26): Save one whole turn in one commit: advance the session, the answer, the…, Architecture & Design, 6. Try it yourself, Deviations from Plan, Affected Files & Patterns, Deviations Found During Implementation, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps (+18 more)

### Community 180 - "Slices in detail"
Cohesion: 0.18
Nodes (11): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 6: Feedback and scoring, Slice 7: Eval maturity (trust the judge, catch regressions), Slice 9: Tool use and agents (+3 more)

### Community 181 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.18
Nodes (10): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slices (+2 more)

### Community 182 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 183 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 184 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 185 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

### Community 186 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

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

### Community 191 - "tracing.py"
Cohesion: 0.16
Nodes (17): Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, get_feedback_controller(), get_feedback_limiter(), get_feedback_service(), limit_feedback(), datetime, Depends, interviews_feedback (+9 more)

### Community 207 - "parse_log"
Cohesion: 0.29
Nodes (10): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), lines_of(), Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis(), squash() (+2 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.18
Nodes (21): embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, 15 cases with the kinds the label rules require: most expect API design first;…, run() (+13 more)

### Community 220 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

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

### Community 234 - "Implementation Plan: Interview History List (backend)"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Interview History List (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Testing Strategy, Trade-offs & Rationale

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

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

### Community 244 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.22
Nodes (8): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Trade-offs & Rationale

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "StreamedTurn"
Cohesion: 0.33
Nodes (4): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, StreamedTurn

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "interviewer_v7.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 249 - "interviewer_v7_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 250 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 251 - "Slice 8: Embeddings and RAG (split into 8a to 8e)"
Cohesion: 0.33
Nodes (6): 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e)

### Community 252 - "test_user_ids.py"
Cohesion: 0.70
Nodes (4): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7()

### Community 260 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 268 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

## Knowledge Gaps
- **790 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+785 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1846 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **40 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `Implementation Plan: Langfuse Tracing`, `interviews_answer_service.py`, `interviews_evals.py`, `interviews_feedback_evals.py`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `test_feedback_endpoint.py`, `interviews_start_dependencies.py`, `test_generation_eval.py`, `Completed Steps`, `traced`, `LLMProvider`, `interviews_retrieval_service.py`, `interviews_schema.py`, `test_tracing.py`, `InterviewsService`, `test_tracing_routes.py`, `tracing.py`, `interviews_constants.py`, `interviews_feedback_service.py`, `run_cases`, `FakeLangfuse`, `test_evals.py`, `experiments`, `test_retrieval_eval.py`, `ChatMessage`, `FakeClient`, `RecordingClient`, `test_factory.py`, `InvalidReplyError`, `run_ranking`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `Feature: Langfuse experiments for the interviews evals`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `interviews_answer_service.py`, `test_interview_report.py`, `build_usage_report`, `test_list_interviews.py`, `interviews_feedback_evals.py`, `Checks`, `test_feedback_endpoint.py`, `test_stream_turn.py`, `interview`, `test_context_strategies.py`, `test_answer_stream.py`, `test_feedback_contract.py`, `ContextManager`, `test_context_controller.py`, `interviews_schema.py`, `InterviewsService`, `interviews_model.py`, `.record_turn`, `test_create_interview.py`, `test_start_llm.py`, `interviews_report.py`, `InterviewsRepository`, `test_follow_ups.py`, `interviews_constants.py`, `interviews_utils.py`, `FollowUpAction`, `interviews_feedback.py`, `test_answer_llm.py`, `json`, `test_transcript.py`, `test_answer_guards.py`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `auth_service.py`, `interviews_answer_service.py`, `decode_token`, `interviews_route.py`, `Implementation Steps`, `interviews_start_dependencies.py`, `InterviewQuestion`, `interviews_schema.py`, `interviews_model.py`, `InterviewsService`, `test_create_interview.py`, `tests/conftest.py`, `InterviewsRepository`, `tracing.py`, `interviews_constants.py`, `interviews_feedback_service.py`, `errors.py`, `interviews_feedback_controller.py`, `interviews_transcription_dependencies.py`, `Implementation: Langfuse Tracing`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.026) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 42 INFERRED edges - model-reasoned connections that need verification._