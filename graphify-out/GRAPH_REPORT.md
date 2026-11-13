# Graph Report - cuewise-be  (2026-11-13)

## Corpus Check
- 366 files · ~326,910 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 5090 nodes · 14368 edges · 259 communities (218 shown, 41 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2739 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d294e61e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- auth_service.py
- Generation
- Completed Steps
- decode_token
- test_interview_report.py
- require_permissions
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- test_knowledge_utils.py
- test_guards.py
- run_generation
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- interviews_job_url_utils.py
- test_feedback_evals.py
- test_safe_fetch.py
- Bundle
- test_tracing_lifespan.py
- cuewise-be
- LLMResult
- test_stream_turn.py
- interview
- test_context_strategies.py
- test_answer_stream.py
- test_transcript.py
- KnowledgeRepository
- Feature: Context Management for the Interview LLM Calls
- RateLimiter
- Completed Steps
- test_reference_note_context.py
- 4. How it works
- llm
- interviews_utils.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- interviews_job_url_service.py
- interviews_answer_service.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_evals.py
- test_feedback_contract.py
- interviews_model.py
- InterviewerInputs
- JobRole
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- Tracer
- test_tracing_routes.py
- InterviewsRepository
- ConsoleFormatter
- job_description_summary_v2.md
- test_reply_contract.py
- FakeEmbedder
- interviews_constants.py
- interviews_feedback_turn.py
- interviews_feedback_service.py
- test_answer_llm.py
- test_eval_runs.py
- Implementation Plan: Follow-up Questions (decide / write split)
- exception_handlers.py
- errors.py
- test_tracing.py
- test_feedback_endpoint.py
- failed
- interviews/conftest.py
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- test_stream_answer.py
- EmbeddingKind
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- InvalidReplyError
- provider.py
- LLMServerError
- read_rankings
- LLMError
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- RecordingClient
- clock
- Langfuse Observability
- interviewer_v3.md
- Implementation: LLM as the Interviewer (it asks the questions)
- QuestionCategory
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- interviews_rag_evals.py
- test_get_interview.py
- Implementation Plan: UUID primary keys
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- User
- interview_report.py
- Implementation: Eval runs in Langfuse (scores + datasets)
- Feature: Langfuse Tracing
- Langfuse
- interviews_reply.py
- Implementation: Langfuse experiments for the interviews evals
- audio_container
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Langfuse Implementation Notes
- interviewer_v5.md
- Feature: Langfuse experiments for the interviews evals
- Feature: Interview Feedback and Scoring (Slice 6)
- Implementation: Three New Interview Roles (designer, qa, devops)
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- parse_log
- How to evaluate an AI feature: from the command to the fix
- _retrieval_row
- Langfuse Dataset Construction
- Langfuse v4 project migration
- tests/conftest.py
- Implementation: Interview History List (backend)
- Judge Calibration
- text
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- test_request_context.py
- test_knowledge_ingest.py
- interviews_feedback_evals.py
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- Learn: Splitting the interviews dependency wiring
- interviews_feedback_dependencies.py
- test_generation_eval.py
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- safe_fetch.py
- interviews_knowledge_ingest.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- InterviewType
- Implementation Plan: Context Management for the Interview LLM Calls
- Implementation Steps
- test_answer_interview.py
- Implementation Plan: Start an Interview (backend)
- experiments
- ErrorResponse
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- RequestContextMiddleware
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_context_controller.py
- types.py
- test_feedback_context.py
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- .stream
- feedback_score_v1.md
- feedback_write_v1.md
- FeedbackStatus
- interviews_route.py
- .record_turn
- Implementation Plan: Langfuse Tracing
- Learn: Langfuse experiments for the interviews evals
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Layered Modules (route -> controller -> service -> repository)
- InterviewQuestion
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- test_list_users.py
- Web
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- users_utils.py
- _reset_request_id
- pytest
- test_retrieval_eval.py
- test_me.py
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
- InterviewFeedback
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
- _post_judgements
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)
- .__init__
- cuewise-be
- .__init__
- get_feedback_controller
- tiny_context
- FakeLangfuse

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 112 edges
2. `User` - 112 edges
3. `FakeProvider` - 106 edges
4. `JobRole` - 104 edges
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

## Communities (259 total, 41 thin omitted)

### Community 0 - "auth_service.py"
Cohesion: 0.10
Nodes (29): hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), post (+21 more)

### Community 1 - "Generation"
Cohesion: 0.29
Nodes (4): Generation, The stream was closed before it finished (client left, or the turn's deadline…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, TraceLabels

### Community 2 - "Completed Steps"
Cohesion: 0.15
Nodes (18): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, generate_feedback(), get_feedback() (+10 more)

### Community 3 - "decode_token"
Cohesion: 0.13
Nodes (28): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Implementation Steps (+20 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (52): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start() (+44 more)

### Community 5 - "require_permissions"
Cohesion: 0.07
Nodes (59): alias, AnswerControllerDep, ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role (+51 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "test_knowledge_utils.py"
Cohesion: 0.11
Nodes (34): _check_hidden(), CorpusError, load_corpus(), parse_note(), pick_filter_notes(), Exception, Path, T (+26 more)

### Community 9 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 10 - "run_generation"
Cohesion: 0.09
Nodes (36): Local time, as the Langfuse list shows the run's start: the name and the…, run_stamp(), ArmInterview, case_set_problems(), generation_item(), generation_run_scores(), _generation_scores(), _print_retrieval_row() (+28 more)

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
Cohesion: 0.08
Nodes (39): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., _google(), no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env() (+31 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (24): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+16 more)

### Community 16 - "interviews_job_url_utils.py"
Cohesion: 0.13
Nodes (17): _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), _plain(), _posting_text(), Turn a fetched job page into plain job-description text (Slice 8b). Pure…, A JSON-LD description is usually HTML, sometimes entity-escaped HTML: unescape,… (+9 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.08
Nodes (60): check_feedback(), criterion_spread(), feedback_hints_for(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult, FeedbackEvalCase, level_gap_check() (+52 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (42): FetchedPage, Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request (+34 more)

### Community 19 - "Bundle"
Cohesion: 0.08
Nodes (32): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+24 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "LLMResult"
Cohesion: 0.13
Nodes (30): LLMResult, setup_logging(), decide(), UUID, The decide step of an answer turn: the model suggests following up or moving…, At most two attempts within the decide cap; any failure means "next_question"…, log_embedding_call(), log_llm_call() (+22 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.17
Nodes (31): Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, collect(), follow_up_json() (+23 more)

### Community 28 - "interview"
Cohesion: 0.21
Nodes (24): 5. What can go wrong, interview(), post(), parametrize, Insert a stored interview: one main question per answer, optional follow-ups…, rows_of(), test_a_failed_score_step_is_an_error_in_the_trace(), test_a_failing_write_call_falls_back_to_the_template_and_keeps_the_scores() (+16 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.08
Nodes (56): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Task, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions (+48 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.09
Nodes (17): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+9 more)

### Community 31 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 32 - "KnowledgeRepository"
Cohesion: 0.09
Nodes (26): Embedder, Protocol, KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a…, _embed() (+18 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "RateLimiter"
Cohesion: 0.22
Nodes (10): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window(), test_refused_hits_do_not_extend_the_window() (+2 more)

### Community 35 - "Completed Steps"
Cohesion: 0.13
Nodes (23): Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, _eligible(), EligibleChunk, NamedTuple, Active chunks scoped to this role (or every role) and this level. Role and… (+15 more)

### Community 36 - "test_reference_note_context.py"
Cohesion: 0.12
Nodes (26): ContextReport, _log(), NamedTuple, A main-question write of an interview with reference notes: the notes-aware…, WithReferenceNotes, A note an interview was given: what the question writer sees (competency and…, ReferenceNote, 5. What can go wrong (+18 more)

### Community 37 - "4. How it works"
Cohesion: 0.10
Nodes (20): _decode(), is_public_address(), Response, Scheme, credentials, port and every resolved address. Returns the address to…, One hop: a page, or the redirect's Location to check next., Header charset, else a <meta> charset, else UTF-8; never raises (bad bytes…, True only for a globally routable unicast address., _job_url() (+12 more)

### Community 38 - "llm"
Cohesion: 0.07
Nodes (27): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+19 more)

### Community 39 - "interviews_utils.py"
Cohesion: 0.06
Nodes (65): StrategyOutput, build_context_manager(), _counts(), FeedbackWrite, FollowUpDecision, FullHistory, JobDescriptionSummary, What the interview LLM calls send: the tasks and strategies registered with the… (+57 more)

### Community 40 - "test_layers.py"
Cohesion: 0.05
Nodes (47): ast, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository) (+39 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.15
Nodes (28): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+20 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.10
Nodes (38): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, Any network-side failure of a job link. One message for every cause, so…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError (+30 more)

### Community 45 - "interviews_answer_service.py"
Cohesion: 0.05
Nodes (95): QuestionNotCurrentError, Page, BaseModel, Offset pagination shared by every list endpoint, so clients see one query…, PhaseChanged, MessageKind, MessageRole, StrEnum (+87 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.11
Nodes (16): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_125_s_or_an_unreported_duration_is_accepted(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415() (+8 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.07
Nodes (91): FakeProvider, load_cases(), main(), Path, run_case(), Deviations from Plan, console_number(), decision() (+83 more)

### Community 49 - "test_feedback_contract.py"
Cohesion: 0.18
Nodes (33): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+25 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.06
Nodes (42): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+34 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.13
Nodes (36): InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, apply_limits(), _decision_label(), plan_write(), UUID (+28 more)

### Community 52 - "JobRole"
Cohesion: 0.06
Nodes (63): JobRole, Level, NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, ArmSummary, competencies_of(), NamedTuple, The share of the job description's skills that at least one question mentions;… (+55 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.16
Nodes (19): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+11 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.14
Nodes (37): 5. What can go wrong, Open Questions, fail(), error(), import_url(), _post(), long_posting(), page() (+29 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.11
Nodes (28): LLMBadResponseError, A 200 whose body is unusable (not JSON, no choices, blank text). Not transient,…, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider() (+20 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.14
Nodes (37): analyze_interview(), analyze_rollup(), _avg(), _call_table(), _cost(), _counts(), _dash(), _effectiveness() (+29 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (33): Clock, completion(), make_provider(), _make(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant. (+25 more)

### Community 59 - "Tracer"
Cohesion: 0.08
Nodes (15): AbstractContextManager, Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, FakeObservation, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_score_failure_is_swallowed() (+7 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 61 - "InterviewsRepository"
Cohesion: 0.06
Nodes (35): HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SortDirection, InterviewSession, _history_filter(), _history_order(), InterviewsRepository, Any (+27 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.08
Nodes (29): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), Acceptance Criteria, Blockers, Constraints, Edge Cases (+21 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_reply_contract.py"
Cohesion: 0.06
Nodes (61): Slice 3: Structured follow-up decisions, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me (+53 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.14
Nodes (28): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), parametrize, RetrievalService.retrieve: the vector / filter / skip ladder (knowledge-base-…, A stand-in tracer that records each step's metadata and output. (+20 more)

### Community 66 - "interviews_constants.py"
Cohesion: 0.11
Nodes (26): JobTextFormat, QuestionSource, Which clipboard copy the client sent: the HTML one when the browser has it (its…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), InterviewState (+18 more)

### Community 67 - "interviews_feedback_turn.py"
Cohesion: 0.08
Nodes (34): BuiltContext, NamedTuple, The labelled text the write call is asked for (the parser reads it back…, ScoreResult, _Attempts, CallUsage, FeedbackGenerator, hint_for() (+26 more)

### Community 68 - "interviews_feedback_service.py"
Cohesion: 0.12
Nodes (30): FeedbackFailedError, FeedbackInProgressError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple (+22 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.11
Nodes (23): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), itertools, messages(), questions(), Answer every question of a started interview; returns the list of answer… (+15 more)

### Community 71 - "test_eval_runs.py"
Cohesion: 0.06
Nodes (49): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), notes_fingerprint(), Any (+41 more)

### Community 72 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "errors.py"
Cohesion: 0.07
Nodes (46): Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError (+38 more)

### Community 75 - "test_tracing.py"
Cohesion: 0.10
Nodes (25): client(), drain(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), _settings(), test_both_keys_build_an_enabled_tracer() (+17 more)

### Community 76 - "test_feedback_endpoint.py"
Cohesion: 0.21
Nodes (18): 8. Check your understanding, POST and GET /api/v1/interviews/{id}/feedback: the end-to-end seam for the…, rows(), score_json(), stored_scores_json(), test_a_mixed_interview_scores_each_question_on_its_own_categorys_criteria(), test_a_rejected_reply_and_the_template_fallback_stand_out_in_the_trace(), test_a_second_post_during_generation_gets_409_and_one_row_exists() (+10 more)

### Community 77 - "failed"
Cohesion: 0.29
Nodes (8): check_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, Slice 6: Feedback and scoring, failed(), test_a_good_reply_passes_every_check(), test_a_good_streamed_reply_passes_every_check(), test_each_check_catches_its_problem(), test_each_streamed_check_catches_its_problem()

### Community 78 - "interviews/conftest.py"
Cohesion: 0.05
Nodes (43): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them., Baseline Failures, Changes Made, Completed Steps, Deviations from Plan (+35 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "test_stream_answer.py"
Cohesion: 0.17
Nodes (18): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, 5. What can go wrong, 6. Try it yourself, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries() (+10 more)

### Community 82 - "EmbeddingKind"
Cohesion: 0.09
Nodes (34): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, A vector of another length than configured. Vectors of different sizes can't be…, EmbedCall, GoogleEmbedder (+26 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "InvalidReplyError"
Cohesion: 0.09
Nodes (42): build_threads(), _check_lengths(), Evidence, FeedbackThread, _has_markup(), _normalized(), parse_write_reply(), BaseModel (+34 more)

### Community 85 - "provider.py"
Cohesion: 0.08
Nodes (34): estimate_tokens(), Context management: the one place that decides what each LLM call sends. The…, The embedding contract features code against, separate from the chat…, ReasoningEffort, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or…, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel (+26 more)

### Community 86 - "LLMServerError"
Cohesion: 0.06
Nodes (45): anyio, DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The first channel's best transcript (blank for silence) and the reported audio… (+37 more)

### Community 87 - "read_rankings"
Cohesion: 0.16
Nodes (19): build_sheet(), Exception, _ranking(), _rating(), The grading file can't be read; the message starts with the line and gives the…, One block per setup with the three question sets under X/Y/Z in a seeded random…, Every setup of the key must have one complete ranking; anything else, and any…, `fit relevance variety specificity`, whole numbers 1 to 5; relevance may be `-`… (+11 more)

### Community 88 - "LLMError"
Cohesion: 0.09
Nodes (23): LLMError, LLMRateLimitError, Exception, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Base for every provider failure. `retryable` marks faults that may pass on…, _degrade_reason(), Retrieval at interview start: pick up to 6 reference notes for the interview's… (+15 more)

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
Cohesion: 0.12
Nodes (11): stream(), submit_the_same_answer_elsewhere(), fresh_limiter(), happy(), owner(), fixture, Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, Fake wall clock for the claim token and the stale takeover. (+3 more)

### Community 93 - "clock"
Cohesion: 0.12
Nodes (12): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open, Learn: Adding interview roles (designer, qa, devops) (+4 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 97 - "QuestionCategory"
Cohesion: 0.06
Nodes (55): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, model_validator, Self, One criterion of the feedback rubric: what it asks, an anchor per score, and…, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric (+47 more)

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

### Community 103 - "interviews_rag_evals.py"
Cohesion: 0.06
Nodes (49): build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, OpenAICompatibleProvider, LLMProvider (+41 more)

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.06
Nodes (69): anyio_from_thread, ContextManager, SummaryInputs, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check (+61 more)

### Community 109 - "User"
Cohesion: 0.12
Nodes (18): User, AuthRepository, Session, UUID, UUID, Transcript, main(), Session (+10 more)

### Community 110 - "interview_report.py"
Cohesion: 0.15
Nodes (19): html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+11 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional (+6 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "interviews_reply.py"
Cohesion: 0.06
Nodes (62): _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_decision_reply(), parse_interviewer_reply(), parse_streamed_reply(), BaseModel (+54 more)

### Community 115 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.14
Nodes (13): 13. Phase 2 real runs (yours), Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 116 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

### Community 117 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.14
Nodes (13): Assumptions to verify (external system behaviour), Blockers, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 121 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional (+5 more)

### Community 122 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 123 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.15
Nodes (12): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Functional, Goal, Non-Functional (+4 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "parse_log"
Cohesion: 0.22
Nodes (14): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), analysis(), lines_of(), Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis() (+6 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.13
Nodes (14): 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse, 7. Fix: the smallest change in the right place (+6 more)

### Community 127 - "_retrieval_row"
Cohesion: 0.23
Nodes (13): filter_baseline(), Collection, What filter mode alone would score: recall@k and reciprocal rank averaged over…, (threshold, mean recall@k, mean notes kept) per threshold: a higher threshold…, recall_at_k(), reciprocal_rank(), _retrieval_row(), threshold_sweep() (+5 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "tests/conftest.py"
Cohesion: 0.06
Nodes (44): RequestIdFilter, health_check(), list_users(), PageDep, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling (+36 more)

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
Cohesion: 0.05
Nodes (41): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+33 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "Implementation Plan: Job URL (Slice 8b)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Job URL (Slice 8b), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.21
Nodes (23): IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, active(), chunks(), corpus(), FailingOn, interview() (+15 more)

### Community 143 - "interviews_feedback_evals.py"
Cohesion: 0.08
Nodes (31): What produced a run, as the strings Langfuse stores: the run explains itself…, run_metadata(), Band, _band_check(), feedback_dataset_items(), feedback_run_scores(), FeedbackEvalQuestion, FeedbackEvalSetup (+23 more)

### Community 144 - "PageParams"
Cohesion: 0.06
Nodes (41): page_params(), PageParams, NamedTuple, Query, UsersController, get_controller(), get_service(), Depends (+33 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (11): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+3 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

### Community 151 - "interviews_feedback_dependencies.py"
Cohesion: 0.11
Nodes (47): get_db(), Session, get_answer_controller(), get_answer_service(), Depends, Session, get_feedback_limiter(), get_feedback_service() (+39 more)

### Community 152 - "test_generation_eval.py"
Cohesion: 0.17
Nodes (31): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), arm_of(), fill(), generated(), posted(), parametrize, quiet() (+23 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "safe_fetch.py"
Cohesion: 0.17
Nodes (8): FetchError, BaseTransport, Exception, Fetch a web page whose address a user chose, without letting that user reach…, codecs, ipaddress, Resolver, socket

### Community 157 - "interviews_knowledge_ingest.py"
Cohesion: 0.23
Nodes (15): main(), _parser(), ArgumentParser, Session, Ingest the reference notes into the database (knowledge-base RAG). uv run…, pathlib, ingest(), Path (+7 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "InterviewType"
Cohesion: 0.13
Nodes (34): NotEnoughQuestionsError, InterviewType, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 4. How it works, Implementation Steps, Testing Strategy, fixture_bank() (+26 more)

### Community 160 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 161 - "Implementation Steps"
Cohesion: 0.05
Nodes (49): Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, A named step inside the current trace (a Langfuse `chain`): the generations and… (+41 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules, Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 164 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 165 - "ErrorResponse"
Cohesion: 0.04
Nodes (57): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+49 more)

### Community 166 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.10
Nodes (16): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Ready to Implement (+8 more)

### Community 167 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.18
Nodes (10): Blockers & Resolutions, Deviations from Spec (to apply to spec.md), Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 169 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 170 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 171 - "test_feedback_context.py"
Cohesion: 0.19
Nodes (19): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, ThreadTurn, Step 4 of the feedback plan: what the score and write calls send, through the…, score_inputs() (+11 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.13
Nodes (21): Baseline Failures, Testing Strategy, Testing Strategy, Baseline Failures, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against (+13 more)

### Community 174 - ".stream"
Cohesion: 0.36
Nodes (3): ReasoningEffort, Same request with `stream: true`: chunks as they arrive, then the final…, How long to wait before retrying, or None to give up.

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "FeedbackStatus"
Cohesion: 0.24
Nodes (10): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, row(), test_a_completed_interview_gets_scored_written_and_stored(), test_a_provider_error_fails_at_once_with_no_partial_scores(), test_a_request_whose_row_was_taken_over_stores_nothing(), test_no_retry_when_the_budget_is_nearly_spent(), test_scores_are_stored_before_the_write_call_starts() (+2 more)

### Community 178 - "interviews_route.py"
Cohesion: 0.20
Nodes (9): limit_feedback(), Depends, interviews_feedback, Per-user cap on feedback requests, checked before anything that can cost an LLM…, limit_transcriptions(), interviews_answer, Per-user cap on transcriptions, checked before the upload goes anywhere that…, fastapi_concurrency (+1 more)

### Community 179 - ".record_turn"
Cohesion: 0.10
Nodes (20): Save one whole turn in one commit: advance the session, the answer, the…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+12 more)

### Community 180 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 181 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 182 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 183 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 184 - "InterviewQuestion"
Cohesion: 0.09
Nodes (28): InterviewMessage, InterviewQuestion, A candidate answer or the interviewer's reaction to one question. The questions…, A question as it was shown: written by the LLM, or snapshotted from the bank…, Every stored question, grouped by interview in creation order (UUIDv7), for the…, The saved turn. `session` and `current_question` are refreshed after the…, TurnResult, main() (+20 more)

### Community 185 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 186 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 187 - "Web"
Cohesion: 0.20
Nodes (5): fixture, Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 188 - "Platform and DevOps practice"
Cohesion: 0.25
Nodes (7): CI/CD pipelines with safe rollback, Cloud security, backup and recovery, Containers and Kubernetes troubleshooting, Infrastructure as code in practice, Monitoring, alerting and observability, Platform and DevOps practice, Production problems with no obvious cause

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 207 - "pytest"
Cohesion: 0.27
Nodes (8): pytest, parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.18
Nodes (21): embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, 15 cases with the kinds the label rules require: most expect API design first;…, run() (+13 more)

### Community 220 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

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

### Community 234 - "InterviewFeedback"
Cohesion: 0.33
Nodes (5): InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, test_a_stale_row_without_scores_runs_the_whole_generation(), test_losing_the_insert_race_answers_409()

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

### Community 246 - "_post_judgements"
Cohesion: 0.33
Nodes (6): _post_judgements(), Path, RankingReport, The sheet's third file: setup, then arm, then the Langfuse trace of that arm's…, Post every rank (and rating) to its arm's result; returns the line saying what…, _write_traces()

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "interviewer_v7.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 249 - "interviewer_v7_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 250 - "Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)"
Cohesion: 0.33
Nodes (5): 1. Why it exists, 2. What it is, 3. When to use it, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)

### Community 251 - ".__init__"
Cohesion: 0.50
Nodes (3): AsyncBaseTransport, BaseTransport, Random

### Community 268 - "FakeLangfuse"
Cohesion: 0.07
Nodes (25): contextvars, 5. What can go wrong, experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only() (+17 more)

## Knowledge Gaps
- **814 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+809 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1935 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **41 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `Generation`, `run_generation`, `FakeLangfuse`, `interviews_feedback_evals.py`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `interviews_feedback_dependencies.py`, `test_generation_eval.py`, `KnowledgeRepository`, `Implementation Steps`, `Completed Steps`, `experiments`, `interviews_answer_service.py`, `test_evals.py`, `test_tracing_routes.py`, `InterviewsRepository`, `interviews_constants.py`, `interviews_feedback_turn.py`, `interviews_feedback_service.py`, `test_eval_runs.py`, `test_tracing.py`, `test_feedback_endpoint.py`, `test_retrieval_eval.py`, `provider.py`, `LLMError`, `RecordingClient`, `interviews_rag_evals.py`, `interviews_evals.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `_post_judgements`, `Feature: Langfuse experiments for the interviews evals`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `auth_service.py`, `Completed Steps`, `decode_token`, `interviews_feedback_service.py`, `require_permissions`, `interviews_constants.py`, `Implementation: Langfuse Tracing`, `tests/conftest.py`, `Implementation Plan: UUID primary keys`, `errors.py`, `interviews_job_url_service.py`, `interviews_answer_service.py`, `PageParams`, `interviews_model.py`, `interviews_route.py`, `test_create_interview.py`, `interviews_feedback_dependencies.py`, `InterviewsRepository`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `Generation`, `interviews_feedback_evals.py`, `test_feedback_evals.py`, `test_turn_budget.py`, `test_generation_eval.py`, `interviews_utils.py`, `interviews_answer_service.py`, `.stream`, `test_evals.py`, `InterviewerInputs`, `test_start_llm.py`, `test_openai_compatible_stream.py`, `interviews_constants.py`, `interviews_feedback_turn.py`, `interviews_feedback_service.py`, `test_answer_llm.py`, `test_tracing.py`, `pytest`, `provider.py`, `LLMServerError`, `LLMError`, `interviews_rag_evals.py`, `interviews_evals.py`, `Feature: Langfuse Tracing`, `interviews_reply.py`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 47 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._