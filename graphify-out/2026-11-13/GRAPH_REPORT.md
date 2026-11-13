# Graph Report - cuewise-be  (2026-11-13)

## Corpus Check
- 366 files · ~324,586 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 5055 nodes · 14252 edges · 252 communities (214 shown, 38 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2718 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d294e61e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- auth_service.py
- LLMResult
- interviews_constants.py
- decode_token
- test_interview_report.py
- User
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- interviews_knowledge_utils.py
- Role
- interviews_rag_evals.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- interviews_job_url_utils.py
- test_feedback_evals.py
- test_safe_fetch.py
- test_reply_contract.py
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_transcript.py
- KnowledgeRepository
- Feature: Context Management for the Interview LLM Calls
- RateLimiter
- Completed Steps
- test_reference_note_context.py
- safe_fetch.py
- Feature: LLM as the Interviewer (it asks the questions)
- QuestionTurn
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- SafeFetcher
- InterviewQuestion
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- FakeProvider
- summarize
- collections_abc
- LLMProvider
- JobRole
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- Implementation: Error Handling
- test_tracing_routes.py
- InterviewsRepository
- ConsoleFormatter
- job_description_summary_v2.md
- test_follow_ups.py
- FakeEmbedder
- decision
- FeedbackGenerator
- FeedbackService
- follow_up
- test_eval_runs.py
- FollowUpAction
- exception_handlers.py
- errors.py
- Tracer
- Feature: Follow-up Questions (decide / write split)
- test_evals.py
- interviews/conftest.py
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- FakeStream
- EmbeddingKind
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_feedback_contract.py
- test_context.py
- provider.py
- .stream_turn
- Implementation Steps
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- llm
- AI Engineering Learning Path (Cuewise)
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
- Implementation Plan: UUID primary keys
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- pydantic
- main
- Implementation: Eval runs in Langfuse (scores + datasets)
- Feature: Langfuse Tracing
- Langfuse
- QuestionCategory
- test_turn_budget.py
- audio_container
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Langfuse Implementation Notes
- interviewer_v5.md
- Feature: Langfuse experiments for the interviews evals
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Implementation: Three New Interview Roles (designer, qa, devops)
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- parse_log
- LLMRateLimitError
- Feature: Interview History List (backend)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- tests/conftest.py
- Implementation: Interview History List (backend)
- Judge Calibration
- Langfuse Prompt Migration
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- test_request_context.py
- test_knowledge_ingest.py
- ._ordered
- interviews_service.py
- Langfuse v4 project migration
- Judge Calibration
- Langfuse CLI Reference
- Langfuse CI/CD
- Prompt Engineering
- Learn: Splitting the interviews dependency wiring
- get_llm_provider
- test_generation_eval.py
- fixture
- test_start_reference_notes.py
- FetchError
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- test_select_questions.py
- Implementation Steps
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_answer_interview.py
- inputs
- experiments
- ErrorResponse
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- Implementation Plan: Error Handling
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_context_controller.py
- types.py
- interviews_context.py
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- OpenAICompatibleProvider
- feedback_score_v1.md
- feedback_write_v1.md
- _parser
- ._covers_every_criterion
- .record_turn
- Slices in detail
- Learn: Langfuse experiments for the interviews evals
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Layered Modules (route -> controller -> service -> repository)
- started
- started
- test_list_users.py
- Langfuse
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- traces
- users_utils.py
- _reset_request_id
- pytest
- test_retrieval_eval.py
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
- 2. Langfuse Documentation
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
- ProviderConfig
- FakeLangfuse

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 112 edges
2. `User` - 109 edges
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

## Communities (252 total, 38 thin omitted)

### Community 0 - "auth_service.py"
Cohesion: 0.11
Nodes (29): hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), post (+21 more)

### Community 1 - "LLMResult"
Cohesion: 0.07
Nodes (31): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, LLMResult, BaseModel, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, One turn of the conversation sent to the model. The model keeps no memory:… (+23 more)

### Community 2 - "interviews_constants.py"
Cohesion: 0.11
Nodes (22): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or… (+14 more)

### Community 3 - "decode_token"
Cohesion: 0.12
Nodes (30): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, UUID, BaseModel (+22 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.12
Nodes (58): log_retrieval(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, Which reference notes an interview got at start: mode, count, scores and the…, analysis(), answer(), emit_answer_turn(), emit_call() (+50 more)

### Community 5 - "User"
Cohesion: 0.05
Nodes (79): alias, AnswerControllerDep, The speech-to-text contract features code against, separate from the text-only…, RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, get_db(), Session (+71 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.14
Nodes (33): extract_job_text(), job_term_hits(), looks_like_job_posting(), The posting as plain text, or None when the page has too little text to be one…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;…, truncate_on_word(), jsonld() (+25 more)

### Community 8 - "interviews_knowledge_utils.py"
Cohesion: 0.08
Nodes (49): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, cosine_similarity(), _hash(), _listed() (+41 more)

### Community 9 - "Role"
Cohesion: 0.08
Nodes (30): permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, check(), AuthRepository, Session, test_admin_holds_every_user_permission() (+22 more)

### Community 10 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (104): Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, final_line(), The console's last line: which Langfuse runs to open, or why nothing was…, Local time, as the Langfuse list shows the run's start: the name and the…, run_stamp(), _arm_notes(), ArmInterview (+96 more)

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
Cohesion: 0.13
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), _make(), ok(), fixture, parametrize (+17 more)

### Community 16 - "interviews_job_url_utils.py"
Cohesion: 0.14
Nodes (15): _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), _plain(), _posting_text(), Turn a fetched job page into plain job-description text (Slice 8b). Pure…, A JSON-LD description is usually HTML, sometimes entity-escaped HTML: unescape,… (+7 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.05
Nodes (85): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for() (+77 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.12
Nodes (43): Refused before connecting, or the network side failed (DNS, timeout,…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize (+35 more)

### Community 19 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.26
Nodes (21): What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, collect(), kinds(), make_interviewer(), Interviewer.stream_turn: the streamed answer turn yields what it is doing,…, Event kinds in order, a run of deltas shown once as "Delta"., The question text of each draft (a Reset starts a new one). (+13 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.06
Nodes (83): InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 8. Check your understanding (+75 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (37): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+29 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.07
Nodes (29): 5. What can go wrong, 6. Try it yourself, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing() (+21 more)

### Community 31 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 32 - "KnowledgeRepository"
Cohesion: 0.07
Nodes (37): Embedder, Protocol, KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a…, _embed() (+29 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "RateLimiter"
Cohesion: 0.28
Nodes (8): RateLimiter, Count one request for `key`: None when allowed, else whole seconds until its…, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window(), test_refused_hits_do_not_extend_the_window(), test_retry_after_is_at_least_one_second()

### Community 35 - "Completed Steps"
Cohesion: 0.13
Nodes (25): One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Step, log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip (+17 more)

### Community 36 - "test_reference_note_context.py"
Cohesion: 0.10
Nodes (42): ContextReport, estimate_tokens(), _log(), NamedTuple, Task, FeedbackScoreInputs, Plain values for the score call: the whole interview, read once the interview…, A note an interview was given: what the question writer sees (competency and… (+34 more)

### Community 37 - "safe_fetch.py"
Cohesion: 0.08
Nodes (25): _decode(), FetchedPage, is_public_address(), Response, Fetch a web page whose address a user chose, without letting that user reach…, Scheme, credentials, port and every resolved address. Returns the address to…, One hop: a page, or the redirect's Location to check next., Header charset, else a <meta> charset, else UTF-8; never raises (bad bytes… (+17 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.11
Nodes (19): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+11 more)

### Community 39 - "QuestionTurn"
Cohesion: 0.09
Nodes (39): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the… (+31 more)

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
Cohesion: 0.13
Nodes (34): Checks, bad_parent(), Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, Each check with the problems it found (none = passed)., _cell_class(), _heading(), _html_block() (+26 more)

### Community 44 - "SafeFetcher"
Cohesion: 0.06
Nodes (36): JobUrlUnreachableError, JobUrlUnreadableError, The job link answered, but no job description could be read from it (not HTML,…, Any network-side failure of a job link. One message for every cause, so…, SafeFetcher, get_job_url_controller(), get_job_url_limiter(), get_job_url_service() (+28 more)

### Community 45 - "InterviewQuestion"
Cohesion: 0.05
Nodes (91): QuestionNotCurrentError, MessageKind, MessageRole, QuestionSource, The SSE event names of a streamed turn: the contract with the client. `done`…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Transcript item kinds: a question comes from interview_questions, the other two…, StreamEvent (+83 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.11
Nodes (16): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_125_s_or_an_unreported_duration_is_accepted(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415() (+8 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "FakeProvider"
Cohesion: 0.10
Nodes (43): FakeProvider, run_case(), Reply, console_number(), hints_of(), long_case(), mentions(), noted() (+35 more)

### Community 49 - "summarize"
Cohesion: 0.17
Nodes (13): The job-description summary replaces the original on every later call, so it…, validate_summary(), _print_summary(), The same one-off condensation the app makes at interview start; its tokens…, One run proves little (the same cases scored 5/6, then 6/6): look at the spread…, summarize(), summarize_runs(), Summary (+5 more)

### Community 50 - "collections_abc"
Cohesion: 0.04
Nodes (55): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+47 more)

### Community 51 - "LLMProvider"
Cohesion: 0.06
Nodes (72): ContextManager, Context management: the one place that decides what each LLM call sends. The…, LLMProvider, Protocol, decide(), UUID, The decide step of an answer turn: the model suggests following up or moving…, At most two attempts within the decide cap; any failure means "next_question"… (+64 more)

### Community 52 - "JobRole"
Cohesion: 0.06
Nodes (72): InterviewType, JobRole, Level, StrEnum, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, _Interview, The interview as plain values, read before the claim's commit expires the… (+64 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.16
Nodes (19): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+11 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.22
Nodes (24): 5. What can go wrong, fail(), error(), import_url(), long_posting(), page(), parametrize, POST /interviews/job-url (Slice 8b): the whole route with a fake resolver and a… (+16 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (26): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), _make(), ok() (+18 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (64): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+56 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "Implementation: Error Handling"
Cohesion: 0.12
Nodes (14): RequestIdFilter, Baseline Failures, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+6 more)

### Community 61 - "InterviewsRepository"
Cohesion: 0.04
Nodes (56): InterviewMessage, InterviewSession, A candidate answer or the interviewer's reaction to one question. The questions…, _history_filter(), InterviewsRepository, Any, datetime, Session (+48 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.22
Nodes (13): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), sys, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success() (+5 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_follow_ups.py"
Cohesion: 0.24
Nodes (18): 5. What can go wrong, 8. Check your understanding, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end() (+10 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.14
Nodes (29): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets(), competencies(), parametrize, RetrievalService.retrieve: the vector / filter / skip ladder (knowledge-base-… (+21 more)

### Community 66 - "decision"
Cohesion: 0.23
Nodes (20): Deviations from Plan, decision(), labelled_cases(), The trace id the fake gives a case in the given repeat's run (write and stream…, run_decide(), scores_on(), test_a_failed_decision_shows_the_verdict_the_decision_and_the_expected_one(), test_a_passing_case_says_pass_and_a_label_with_a_gap_shows_it() (+12 more)

### Community 67 - "FeedbackGenerator"
Cohesion: 0.08
Nodes (28): BuiltContext, _Attempts, FeedbackGenerator, hint_for(), NamedTuple, T, UUID, One budget for the whole generation, started when the request holds its claim. (+20 more)

### Community 68 - "FeedbackService"
Cohesion: 0.22
Nodes (11): FeedbackInProgressError, _Claim, FeedbackService, _Outcome, Any, NamedTuple, UUID, The feedback, generated now (True) or already stored (False). Checks run in… (+3 more)

### Community 69 - "follow_up"
Cohesion: 0.18
Nodes (12): Slice 3: Structured follow-up decisions, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+4 more)

### Community 71 - "test_eval_runs.py"
Cohesion: 0.06
Nodes (49): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), git_commit(), notes_fingerprint(), Any, Score (+41 more)

### Community 72 - "FollowUpAction"
Cohesion: 0.12
Nodes (27): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Blockers & Resolutions (+19 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "errors.py"
Cohesion: 0.09
Nodes (42): Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError (+34 more)

### Community 75 - "Tracer"
Cohesion: 0.06
Nodes (41): build_tracer(), Send what is still buffered, then stop the background exporter. Called once at…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, Tracer, client(), drain(), FakeClient, FakeObservation (+33 more)

### Community 76 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 77 - "test_evals.py"
Cohesion: 0.12
Nodes (35): check_decision(), load_cases(), main(), Path, The decide reply against the case's label; the injection check reads the raw…, 5. What can go wrong, failed(), labelled() (+27 more)

### Community 78 - "interviews/conftest.py"
Cohesion: 0.07
Nodes (30): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, get_transcriber(), Built once at startup (app lifespan); None when no Deepgram key is configured…, get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them., Known Issues, answer() (+22 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "FakeStream"
Cohesion: 0.22
Nodes (10): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, One streamed-turn event as the dict sse-starlette encodes: the event name, and…, The controller's events as SSE frames. Closing this (a client that left) closes…, sse_frame(), sse_frames(), Completed Steps (+2 more)

### Community 82 - "EmbeddingKind"
Cohesion: 0.09
Nodes (34): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, EmbedCall (+26 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "test_feedback_contract.py"
Cohesion: 0.07
Nodes (75): assess_evidence(), build_threads(), _check_lengths(), compute_overall(), Evidence, FeedbackThread, _has_markup(), _normalized() (+67 more)

### Community 85 - "test_context.py"
Cohesion: 0.16
Nodes (16): Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default(), test_a_second_task_with_its_own_strategy_leaves_the_first_alone() (+8 more)

### Community 86 - "provider.py"
Cohesion: 0.07
Nodes (44): anyio, DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The first channel's best transcript (blank for silence) and the reported audio… (+36 more)

### Community 87 - ".stream_turn"
Cohesion: 0.24
Nodes (11): The same turn as `answer_turn` (same decide, limits and fallbacks), telling the…, Delta, PhaseChanged, NamedTuple, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, Settled (+3 more)

### Community 88 - "Implementation Steps"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Implementation Steps, Phase A: plumbing and progress events, Phase B: streaming the question text, Step 14: The event loop stays free, Step 15: Evals, Step 16: Measure, document, finish, Step 1: Add the dependency (+3 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "llm"
Cohesion: 0.20
Nodes (8): as_v5_text(), llm(), script(), script_score(), script_write(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY…

### Community 93 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.18
Nodes (10): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slices (+2 more)

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
Cohesion: 0.27
Nodes (12): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, 5. What can go wrong, Test Results, _entry(), parametrize, test_every_role_has_its_own_technical_question_at_every_level() (+4 more)

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.17
Nodes (11): Baseline Failures, Commit message suggestion, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

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
Nodes (68): anyio_from_thread, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., InvalidReplyError, Exception, _action_and_gap(), _add_usage() (+60 more)

### Community 109 - "pydantic"
Cohesion: 0.38
Nodes (9): main(), Session, pydantic, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting(), test_new_admin_password_follows_registration_rules(), test_running_twice_is_a_no_op() (+1 more)

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
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "QuestionCategory"
Cohesion: 0.08
Nodes (51): _check_question(), HeaderSplit, InterviewerReply, load_object(), _normalized(), parse_interviewer_reply(), parse_streamed_reply(), BaseModel (+43 more)

### Community 115 - "test_turn_budget.py"
Cohesion: 0.05
Nodes (43): Blockers & Resolutions, Implementation Plan: Interview History List (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+35 more)

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
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Assumptions to verify (external system behaviour), Blockers, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional (+6 more)

### Community 121 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview (+6 more)

### Community 122 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 123 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Acceptance Criteria, Blockers, Constraints, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope, Problem (+2 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "parse_log"
Cohesion: 0.31
Nodes (9): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, lines_of(), Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis(), squash(), test_calls_logged_before_the_task_name_existed_fold_into_other_so_the_rows_add_up() (+1 more)

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

### Community 130 - "tests/conftest.py"
Cohesion: 0.06
Nodes (38): health_check(), list_users(), PageDep, CurrentUserDep, Affected Files & Patterns, os, sqlalchemy_pool, auth_header() (+30 more)

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
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "Implementation Plan: Job URL (Slice 8b)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Job URL (Slice 8b), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.24
Nodes (20): active(), chunks(), corpus(), FailingOn, interview(), ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag…, Fails on the n-th embed call (1-based), then works again., rows() (+12 more)

### Community 144 - "interviews_service.py"
Cohesion: 0.06
Nodes (63): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, HistorySortColumn (+55 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 8. Check your understanding, 9. Still open, Learn: Splitting the interviews dependency wiring

### Community 151 - "get_llm_provider"
Cohesion: 0.11
Nodes (37): get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., get_bank(), get_clock(), get_embedder(), get_llm_provider(), get_now(), get_tracer() (+29 more)

### Community 152 - "test_generation_eval.py"
Cohesion: 0.15
Nodes (34): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), arm_of(), fill(), generated(), lf(), posted(), fixture (+26 more)

### Community 154 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "FetchError"
Cohesion: 0.33
Nodes (4): FetchError, BaseTransport, Exception, Resolver

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.42
Nodes (9): ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1(), test_an_invalid_note_names_the_file_writes_nothing_and_exits_1(), test_it_prints_the_counts_and_exits_0(), test_warnings_are_printed_without_note_text(), test_without_the_google_key_it_says_what_to_set_and_exits_1() (+1 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "test_select_questions.py"
Cohesion: 0.10
Nodes (35): NotEnoughQuestionsError, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 4. How it works, Implementation Steps, Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend) (+27 more)

### Community 160 - "Implementation Steps"
Cohesion: 0.14
Nodes (14): A running note is optional model output about the latest answer; it is sent…, validate_note(), EvalTurn, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Implementation Steps, Overview, Project Rules Applied (+6 more)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.05
Nodes (39): AbstractContextManager, Any, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Create the dataset if needed and upsert its items (each carries its own `id`,…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, Run an SDK call; on any failure log what failed (not why: the message could… (+31 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "inputs"
Cohesion: 0.33
Nodes (6): follow_up_json(), inputs(), parametrize, test_leaving_mid_question_cancels_the_provider_call(), test_the_streamed_outcome_equals_the_json_turns(), script()

### Community 164 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 165 - "ErrorResponse"
Cohesion: 0.05
Nodes (47): ErrorResponse, Affected Files & Patterns, Completed Steps, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6) (+39 more)

### Community 166 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 167 - "Implementation Plan: Error Handling"
Cohesion: 0.09
Nodes (18): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview (+10 more)

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "test_context_controller.py"
Cohesion: 0.25
Nodes (12): candidate_messages(), noted(), fixture, run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer() (+4 more)

### Community 170 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 171 - "interviews_context.py"
Cohesion: 0.08
Nodes (36): StrategyOutput, build_context_manager(), _counts(), FeedbackScore, FeedbackWrite, FeedbackWriteInputs, FollowUpDecision, FullHistory (+28 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.17
Nodes (15): Baseline Failures, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL), Testing Strategy (+7 more)

### Community 174 - "OpenAICompatibleProvider"
Cohesion: 0.12
Nodes (16): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+8 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "_parser"
Cohesion: 0.67
Nodes (3): _parser(), _positive(), ArgumentParser

### Community 179 - ".record_turn"
Cohesion: 0.09
Nodes (23): ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Save one whole turn in one commit: advance the session, the answer, the…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 7. What surprised me (+15 more)

### Community 180 - "Slices in detail"
Cohesion: 0.20
Nodes (10): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 6: Feedback and scoring, Slice 7: Eval maturity (trust the judge, catch regressions), Slice: Context management (added after Slice 2) (+2 more)

### Community 181 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 182 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.06
Nodes (29): 2. What it is, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+21 more)

### Community 183 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 184 - "started"
Cohesion: 0.67
Nodes (3): fixture, An owner with a started 3-question interview: (owner, session_id, first…, started()

### Community 185 - "started"
Cohesion: 0.67
Nodes (3): fixture, An owner with a started 3-question behavioral interview: (owner, session_id,…, started()

### Community 186 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 187 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 188 - "Platform and DevOps practice"
Cohesion: 0.25
Nodes (7): CI/CD pipelines with safe rollback, Cloud security, backup and recovery, Containers and Kubernetes troubleshooting, Infrastructure as code in practice, Monitoring, alerting and observability, Platform and DevOps practice, Production problems with no obvious cause

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 191 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 207 - "pytest"
Cohesion: 0.20
Nodes (9): pytest, parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text(), parametrize, The shipped reference-note corpus (data/knowledge/): valid, broad enough, and… (+1 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.18
Nodes (21): embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, 15 cases with the kinds the label rules require: most expect API design first;…, run() (+13 more)

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
Cohesion: 0.07
Nodes (32): get_current_user(), get_service(), Depends, Session, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, require_roles(), check(), bearer_scheme (+24 more)

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "StreamedTurn"
Cohesion: 0.22
Nodes (7): parse_sse(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Split a text/event-stream body into (event, data) pairs; returns them and the…, _stream(), StreamedTurn

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "interviewer_v7.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 249 - "interviewer_v7_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 260 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 268 - "FakeLangfuse"
Cohesion: 0.08
Nodes (18): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+10 more)

## Knowledge Gaps
- **814 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+809 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1930 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `LLMResult`, `interviews_constants.py`, `User`, `interviews_rag_evals.py`, `FakeLangfuse`, `interviews_service.py`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `get_llm_provider`, `test_generation_eval.py`, `test_feedback_endpoint.py`, `KnowledgeRepository`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Completed Steps`, `experiments`, `InterviewQuestion`, `LLMProvider`, `test_tracing_routes.py`, `traces`, `FeedbackGenerator`, `FeedbackService`, `test_eval_runs.py`, `test_evals.py`, `test_retrieval_eval.py`, `test_factory.py`, `interviews_evals.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `Feature: Langfuse experiments for the interviews evals`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `auth_service.py`, `interviews_constants.py`, `decode_token`, `FeedbackService`, `tests/conftest.py`, `Role`, `errors.py`, `Implementation Plan: UUID primary keys`, `SafeFetcher`, `InterviewQuestion`, `pydantic`, `interviews_service.py`, `collections_abc`, `Implementation Plan: Role-Based Access Control (single JWT)`, `test_create_interview.py`, `get_llm_provider`, `InterviewsRepository`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `FakeProvider` to `LLMResult`, `interviews_rag_evals.py`, `Feature: Context Management for the Interview LLM Calls`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `test_reference_note_context.py`, `ErrorResponse`, `QuestionTurn`, `InterviewQuestion`, `summarize`, `LLMProvider`, `Slices in detail`, `.record_turn`, `JobRole`, `decision`, `follow_up`, `FollowUpAction`, `errors.py`, `Tracer`, `test_evals.py`, `interviews/conftest.py`, `provider.py`, `llm`, `AI Engineering Learning Path (Cuewise)`, `test_factory.py`, `interviews_evals.py`, `Feature: SSE Streaming of the Interview Turn (Slice 4)`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 46 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 46 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._