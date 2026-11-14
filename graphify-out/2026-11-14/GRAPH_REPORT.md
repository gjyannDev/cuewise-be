# Graph Report - cuewise-be  (2026-11-14)

## Corpus Check
- 412 files · ~350,098 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 5554 nodes · 15653 edges · 287 communities (227 shown, 60 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2917 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `27122bf7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- interviews_schema.py
- LLMRateLimitError
- Completed Steps
- config.py
- test_interview_report.py
- auth_service.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- interviews_knowledge_utils.py
- test_guards.py
- interviews_rag_evals.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- .record_turn
- test_feedback_evals.py
- test_safe_fetch.py
- interviews_route.py
- test_tracing_lifespan.py
- cuewise-be
- interviews_constants.py
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_transcript.py
- Slices in detail
- Feature: Context Management for the Interview LLM Calls
- RateLimiter
- test_profile_read_resume.py
- test_reference_note_context.py
- SafeFetcher
- Feature: LLM as the Interviewer (it asks the questions)
- interviews_context.py
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
- LLMResult
- CandidateProfile
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- FakeClient
- test_tracing_routes.py
- InterviewsRepository
- profile_service.py
- job_description_summary_v2.md
- FakeProvider
- FakeEmbedder
- PageParams
- test_profile_routes.py
- InterviewQuestion
- test_answer_llm.py
- interviews_feedback_evals.py
- hints_of
- exception_handlers.py
- errors.py
- traced
- Implementation: Résumé upload and candidate profile (Slice 8c)
- profile_reply.py
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- profile_dependencies.py
- provider.py
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- parse_log
- User
- LLMTimeoutError
- EmbeddingKind
- interviews_service.py
- interviewer_v2.md
- job_description_summary_v1.md
- ContextManager
- EvalCase
- Implementation: Three New Interview Roles (designer, qa, devops)
- Langfuse Observability
- interviewer_v3.md
- Implementation: LLM as the Interviewer (it asks the questions)
- test_interviewer_messages.py
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_factory.py
- test_get_interview.py
- StreamedTurn
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- interviews_feedback_service.py
- interview_report.py
- Implementation: Eval runs in Langfuse (scores + datasets)
- Feature: Langfuse Tracing
- Langfuse
- QuestionCategory
- Implementation: Langfuse experiments for the interviews evals
- pytest
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Langfuse Implementation Notes
- interviewer_v5.md
- Feature: Langfuse experiments for the interviews evals
- types.py
- LLMProvider
- profile_resume_files.py
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Feature: Résumé upload and candidate profile (Slice 8c)
- How to evaluate an AI feature: from the command to the fix
- test_context_controller.py
- Langfuse Dataset Construction
- Langfuse v4 project migration
- tests/conftest.py
- Implementation: Interview History List (backend)
- Judge Calibration
- Any
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- ConsoleFormatter
- test_knowledge_ingest.py
- ChatMessage
- follow_up
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- test_follow_ups.py
- get_llm_provider
- LLMBadResponseError
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- test_profile_evals.py
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- scrub_contacts
- interviews/conftest.py
- Tracer
- test_answer_interview.py
- Checks
- Feature: Follow-up Questions (decide / write split)
- ErrorResponse
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- Implementation Plan: Role-Based Access Control (single JWT)
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_stream_answer.py
- test_select_questions.py
- LLMServerError
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- .stream
- feedback_score_v1.md
- feedback_write_v1.md
- test_reply_contract.py
- clock
- Implementation Steps
- JobRole
- main.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- StreamEventOut
- Implementation Plan: UUID primary keys
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- Learn: Splitting the interviews dependency wiring
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- Implementation: Layered Modules (route -> controller -> service -> repository)
- users_utils.py
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- test_job_description_summary.py
- test_retrieval_eval.py
- Role
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
- summary
- Communication and priorities
- Engineering habits
- Senior judgement
- .stream
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- check_layers
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- Langfuse CLI Reference
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- _TextCollector
- ProfileLLM
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- Langfuse
- traces
- test_generation_eval.py
- 2. Langfuse Documentation
- Learn: Langfuse experiments for the interviews evals
- Learn: Layered architecture (route -> controller -> service -> repository)
- Steps
- test_tracing.py
- _Usage
- FakeLangfuse
- cuewise-be

## God Nodes (most connected - your core abstractions)
1. `User` - 123 edges
2. `Tracer` - 120 edges
3. `FakeProvider` - 115 edges
4. `JobRole` - 104 edges
5. `LLMResult` - 103 edges
6. `Level` - 89 edges
7. `InterviewQuestion` - 88 edges
8. `InterviewType` - 87 edges
9. `QuestionCategory` - 86 edges
10. `LLMProvider` - 84 edges

## Surprising Connections (you probably didn't know these)
- `6. Try it yourself` --references--> `get_tracer()`  [INFERRED]
  docs/features/split-interviews-dependencies/learnings.md → app/core/ai/dependencies.py
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

## Communities (287 total, 60 thin omitted)

### Community 0 - "interviews_schema.py"
Cohesion: 0.07
Nodes (41): LevelGroup, MessageKind, MessageRole, StrEnum, QuestionSource, Reactions are warmer for people early in their career and briefer for…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Transcript item kinds: a question comes from interview_questions, the other two… (+33 more)

### Community 1 - "LLMRateLimitError"
Cohesion: 0.20
Nodes (20): LLMRateLimitError, LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., parse_retry_after(), raise_for_status(), The Retry-After header as seconds. Only the delta-seconds form is read; an HTTP…, Map a vendor's HTTP status to the typed errors; 200 passes. `retry_after` is…, 4. How it works (+12 more)

### Community 2 - "Completed Steps"
Cohesion: 0.07
Nodes (44): Embedder, EmbeddingSizeError, Protocol, A vector of another length than configured. Vectors of different sizes can't be…, log_embedding_call(), log_retrieval(), One line per embedding call (ingest or retrieval): metadata only, never the…, Which reference notes an interview got at start: mode, count, scores and the… (+36 more)

### Community 3 - "config.py"
Cohesion: 0.12
Nodes (28): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, UUID, Implementation Steps (+20 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.12
Nodes (58): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http() (+50 more)

### Community 5 - "auth_service.py"
Cohesion: 0.11
Nodes (29): hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), post (+21 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.08
Nodes (58): extract_job_text(), _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text() (+50 more)

### Community 8 - "interviews_knowledge_utils.py"
Cohesion: 0.09
Nodes (45): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+37 more)

### Community 9 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 10 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (90): _arm_notes(), ArmInterview, ArmSummary, build_sheet(), case_set_problems(), competencies_of(), filter_baseline(), generation_item() (+82 more)

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
Cohesion: 0.08
Nodes (39): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., _google(), no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env() (+31 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - ".record_turn"
Cohesion: 0.06
Nodes (37): Save one whole turn in one commit: advance the session, the answer, the…, done(), Deviations from Plan, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me (+29 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.06
Nodes (70): Band, _band_check(), check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_trace_output(), FeedbackCaseResult, FeedbackEvalCase (+62 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (42): FetchedPage, Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request (+34 more)

### Community 19 - "interviews_route.py"
Cohesion: 0.11
Nodes (40): alias, AnswerControllerDep, Permission, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), interview_out(), answer_question(), answer_question_stream() (+32 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "interviews_constants.py"
Cohesion: 0.05
Nodes (50): The decide step of an answer turn: the model suggests following up or moving…, _Attempts, CallUsage, FeedbackGenerator, hint_for(), log_feedback_summary(), tokens(), NamedTuple (+42 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.16
Nodes (32): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, StrEnum, What the turn ends with, after the limits: the model can only ask for the first…, TurnAction, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, collect() (+24 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.08
Nodes (69): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Eval log (+61 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (37): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+29 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (19): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+11 more)

### Community 31 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 32 - "Slices in detail"
Cohesion: 0.12
Nodes (16): 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety (+8 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "RateLimiter"
Cohesion: 0.14
Nodes (17): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, get_resume_limiter(), Tests swap in a fresh limiter so counts never leak between them., math, Clock, test_a_new_window_allows_again() (+9 more)

### Community 35 - "test_profile_read_resume.py"
Cohesion: 0.10
Nodes (53): make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), _clean(), _has_external_relationship(), Exception, NamedTuple, Reading an uploaded résumé: untrusted bytes in, visible text in reading order… (+45 more)

### Community 36 - "test_reference_note_context.py"
Cohesion: 0.15
Nodes (21): A main-question write of an interview with reference notes: the notes-aware…, WithReferenceNotes, 5. What can go wrong, first_user(), inputs(), _max_note(), anyio, parametrize (+13 more)

### Community 37 - "SafeFetcher"
Cohesion: 0.05
Nodes (33): _decode(), FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach…, Scheme, credentials, port and every resolved address. Returns the address to… (+25 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "interviews_context.py"
Cohesion: 0.08
Nodes (33): StrategyOutput, build_context_manager(), _counts(), FeedbackScore, FeedbackWrite, FollowUpDecision, FullHistory, JobDescriptionSummary (+25 more)

### Community 40 - "test_layers.py"
Cohesion: 0.32
Nodes (11): ast, 5. What can go wrong, _one(), The layer rules of app/modules (CLAUDE.md, "Architecture"): route -> controller…, test_a_feature_importing_another_features_repository_is_reported(), test_a_layer_file_left_at_a_module_root_is_reported(), test_controller_importing_a_repository_the_llm_or_the_db_session_is_reported(), test_repository_importing_a_service_controller_or_route_is_reported() (+3 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (29): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+21 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.11
Nodes (36): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, Any network-side failure of a job link. One message for every cause, so…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError (+28 more)

### Community 45 - "interviews_answer_service.py"
Cohesion: 0.06
Nodes (65): QuestionNotCurrentError, log_stream_summary(), How a streamed turn felt and ended: time to the first event and to the first…, Delta, PhaseChanged, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset (+57 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.07
Nodes (25): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank). (+17 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.11
Nodes (47): load_cases(), main(), pause_for(), _print_summary(), Path, One run proves little (the same cases scored 5/6, then 6/6): look at the spread…, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, RunsSummary (+39 more)

### Community 49 - "test_feedback_contract.py"
Cohesion: 0.06
Nodes (84): assess_evidence(), _check_lengths(), compute_overall(), Evidence, FeedbackThread, _has_markup(), _normalized(), parse_score_reply() (+76 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.08
Nodes (42): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+34 more)

### Community 51 - "LLMResult"
Cohesion: 0.09
Nodes (50): LLMResult, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, InterviewerInputs, Plain values for one interviewer or decide call., decide(), UUID, At most two attempts within the decide cap; any failure means "next_question"… (+42 more)

### Community 52 - "CandidateProfile"
Cohesion: 0.10
Nodes (43): CandidateProfile, Project, BaseModel, The candidate profile: what a résumé becomes, what is stored, and what the API…, The multipart upload: exactly one part, `file`. Extra form fields are refused., ResumeUploadIn, Role, ExpectedProfile (+35 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.16
Nodes (19): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+11 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.15
Nodes (34): Open Questions, fail(), error(), import_url(), long_posting(), page(), paste(), parametrize (+26 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (62): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+54 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (34): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+26 more)

### Community 59 - "FakeClient"
Cohesion: 0.09
Nodes (11): FakeClient, FakeObservation, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_reports_whether_it_was_sent(), test_sdk_failure_does_not_mask_the_llm_error(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises(), test_steps_and_checks_are_no_ops_when_off_and_never_raise_when_langfuse_fails() (+3 more)

### Community 61 - "InterviewsRepository"
Cohesion: 0.08
Nodes (24): InterviewSession, _history_filter(), _history_order(), InterviewsRepository, Any, datetime, Session, UUID (+16 more)

### Community 62 - "profile_service.py"
Cohesion: 0.08
Nodes (28): build_messages(), extract_profile(), Extraction, ExtractionFailedError, load_prompt(), Exception, NamedTuple, The extraction call: scrubbed résumé text in, a validated profile out (resume-… (+20 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "FakeProvider"
Cohesion: 0.14
Nodes (32): FakeProvider, run_case(), console_number(), long_case(), noted(), reply(), run_task(), test_a_failed_check_is_scored_false_with_its_detail() (+24 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.13
Nodes (33): EmbedCall, FakeEmbedder, NamedTuple, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets(), competencies() (+25 more)

### Community 66 - "PageParams"
Cohesion: 0.06
Nodes (43): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewListOut (+35 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.12
Nodes (33): profile_json(), Synthetic résumé data and the scripted model shared by the profile tests (no…, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,…, stored() (+25 more)

### Community 68 - "InterviewQuestion"
Cohesion: 0.07
Nodes (35): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, InterviewMessage, InterviewQuestion, A candidate answer or the interviewer's reaction to one question. The questions…, A question as it was shown: written by the LLM, or snapshotted from the bank…, Every stored question, grouped by interview in creation order (UUIDv7), for the…, HistoryPage (+27 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.10
Nodes (25): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., failing_commit(), messages() (+17 more)

### Community 71 - "interviews_feedback_evals.py"
Cohesion: 0.04
Nodes (87): build_tracer(), ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, _evaluation(), final_line(), git_commit() (+79 more)

### Community 72 - "hints_of"
Cohesion: 0.36
Nodes (9): hints_of(), mentions(), The hints on one case's result in Langfuse., test_a_cut_off_reply_hints_at_max_tokens_before_quality(), test_a_reply_that_does_not_parse_hints_at_the_format(), test_a_right_action_with_a_different_gap_hints_at_an_ambiguous_label(), test_over_probing_a_normal_case_does_not_blame_an_injection(), test_over_probing_an_injection_case_hints_at_injected_text_and_an_invented_answer() (+1 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.19
Nodes (22): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+14 more)

### Community 74 - "errors.py"
Cohesion: 0.08
Nodes (45): Protocol, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody (+37 more)

### Community 75 - "traced"
Cohesion: 0.17
Nodes (20): drain(), result(), test_a_redacted_call_records_a_placeholder_instead_of_the_messages(), test_a_redacted_failure_records_no_partial_text(), test_a_redacted_stream_closed_early_records_no_partial_text(), test_a_redacted_success_keeps_model_usage_and_labels_but_not_the_reply(), test_an_unlabelled_call_still_records_full_content(), test_call_without_labels_still_gets_a_name() (+12 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (16): 6. Read the résumé, Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues (+8 more)

### Community 77 - "profile_reply.py"
Cohesion: 0.15
Nodes (27): EmptyProfileError, fit(), parse_profile_reply(), BaseModel, Exception, The contract for the profile-extraction reply, and the check that enforces it.…, No skills and no roles: not a résumé we can use (refused as unreadable, nothing…, Whitespace tidied, then cut to `max_length` on a word boundary (a single over-… (+19 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+2 more)

### Community 81 - "profile_dependencies.py"
Cohesion: 0.11
Nodes (25): get_profile_clock(), get_profile_controller(), get_profile_now(), get_profile_service(), limit_resume_uploads(), datetime, Depends, ProfileUser (+17 more)

### Community 82 - "provider.py"
Cohesion: 0.09
Nodes (37): anyio, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Request dependencies for the AI services every feature shares, built once at…, EmbeddingResult, BaseModel, The embedding contract features code against, separate from the chat…, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or…, Gemini embeddings through Google's native `batchEmbedContents` endpoint, over… (+29 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "parse_log"
Cohesion: 0.29
Nodes (10): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), lines_of(), Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis(), squash() (+2 more)

### Community 85 - "User"
Cohesion: 0.08
Nodes (28): get_db(), Session, get_service(), Depends, Session, User, AuthRepository, Session (+20 more)

### Community 86 - "LLMTimeoutError"
Cohesion: 0.10
Nodes (17): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, LLMTimeoutError, 5. Triage: what kind of failure is it? (+9 more)

### Community 87 - "EmbeddingKind"
Cohesion: 0.19
Nodes (22): EmbeddingKind, StrEnum, Clock, make_embedder(), ok(), fixture, parametrize, Response (+14 more)

### Community 88 - "interviews_service.py"
Cohesion: 0.19
Nodes (17): SummaryInputs, HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, InterviewsController, UUID, Interview lifecycle: request -> InterviewsService, domain result -> response… (+9 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "ContextManager"
Cohesion: 0.08
Nodes (28): ContextManager, Task, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+20 more)

### Community 92 - "EvalCase"
Cohesion: 0.07
Nodes (40): Check, check_decision(), check_reply(), check_streamed_reply(), EvalCase, Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format. (+32 more)

### Community 93 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 97 - "test_interviewer_messages.py"
Cohesion: 0.11
Nodes (26): build_interviewer_messages(), interviewer_history(), job_description_block(), Untrusted text, fenced as data. Tags inside it are neutralised so it can't…, Answered questions with their answers (and the model's note on each), in…, The full input for one call (the model has no memory, so the whole interview is…, Architecture & Design, Trade-offs & Rationale (+18 more)

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
Nodes (32): build_embedder(), build_transcriber(), Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, OpenAICompatibleProvider, AsyncBaseTransport, BaseTransport, Random (+24 more)

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "StreamedTurn"
Cohesion: 0.15
Nodes (11): parse_sse(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream() (+3 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.07
Nodes (62): anyio_from_thread, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, dataset_items(), dataset_name() (+54 more)

### Community 109 - "interviews_feedback_service.py"
Cohesion: 0.08
Nodes (48): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackScoreInputs, FeedbackWriteInputs (+40 more)

### Community 110 - "interview_report.py"
Cohesion: 0.15
Nodes (19): html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+11 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "QuestionCategory"
Cohesion: 0.06
Nodes (62): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, _check_question(), HeaderSplit, InterviewerReply (+54 more)

### Community 115 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.14
Nodes (13): 13. Phase 2 real runs (yours), Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 116 - "pytest"
Cohesion: 0.09
Nodes (23): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, pytest, parametrize, test_each_role_list_includes_the_shared_terms_once() (+15 more)

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
Nodes (14): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional (+6 more)

### Community 121 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 122 - "LLMProvider"
Cohesion: 0.08
Nodes (20): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, LLMProvider, Protocol, Generation, _model_parameters(), ReasoningEffort, The stream was closed before it finished (client left, or the turn's deadline… (+12 more)

### Community 123 - "profile_resume_files.py"
Cohesion: 0.14
Nodes (21): _content(), _escape(), _fill(), Image, make_pdf(), plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build…, A PDF with one page per list. `encrypt` adds a standard security handler whose… (+13 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.12
Nodes (14): The notes stored for this interview at start, rank order; none for interviews…, 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links (+6 more)

### Community 125 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+7 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.14
Nodes (13): 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 6. Diagnose in Langfuse, 7. Fix: the smallest change in the right place, 8. Re-run to prove it, then document it (+5 more)

### Community 127 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "tests/conftest.py"
Cohesion: 0.06
Nodes (39): RequestIdFilter, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions (+31 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Any"
Cohesion: 0.13
Nodes (23): _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _hex_lightness(), _in_reading_order() (+15 more)

### Community 134 - "build_usage_report"
Cohesion: 0.19
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

### Community 138 - "Implementation Plan: Job URL (Slice 8b)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Job URL (Slice 8b), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "ConsoleFormatter"
Cohesion: 0.06
Nodes (40): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites, ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message… (+32 more)

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.21
Nodes (23): IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, active(), chunks(), corpus(), FailingOn, interview() (+15 more)

### Community 143 - "ChatMessage"
Cohesion: 0.11
Nodes (28): BuiltContext, ContextReport, ContextTooLargeError, estimate_tokens(), _log(), Exception, NamedTuple, Context management: the one place that decides what each LLM call sends. The… (+20 more)

### Community 144 - "follow_up"
Cohesion: 0.16
Nodes (16): Slice 3: Structured follow-up decisions, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me (+8 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_turn_budget.py"
Cohesion: 0.18
Nodes (16): Testing Strategy, Baseline Failures, Testing Strategy, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,… (+8 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_follow_ups.py"
Cohesion: 0.28
Nodes (15): answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries(), test_a_failed_follow_up_write_falls_back_to_the_next_main_bank_question() (+7 more)

### Community 151 - "get_llm_provider"
Cohesion: 0.08
Nodes (47): get_llm_provider(), get_tracer(), Request, Built once at startup (app lifespan); None when no key is configured or the…, Built once at startup (app lifespan); a disabled tracer when the lifespan…, get_answer_controller(), get_answer_service(), Depends (+39 more)

### Community 152 - "LLMBadResponseError"
Cohesion: 0.16
Nodes (8): GoogleEmbedder, Any, BaseTransport, Random, Response, LLMBadResponseError, A 200 whose body is unusable (not JSON, no choices, blank text). Not transient,…, 1. Where 8a stands

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.13
Nodes (28): embedding_text(), What a chunk is embedded as: its heading, then its text. The heading names the…, corpus(), embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,… (+20 more)

### Community 156 - "test_profile_evals.py"
Cohesion: 0.18
Nodes (13): build_file(), EvalCase, load_cases(), BaseModel, Path, The case as the file a candidate would upload. Hidden lines are white (PDF) or…, run_case(), LabelledModel (+5 more)

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.27
Nodes (13): main(), _parser(), ArgumentParser, Session, ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1() (+5 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 160 - "interviews/conftest.py"
Cohesion: 0.06
Nodes (54): Decision, parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, apply_limits(), plan_write(), The code's say over the model's: returns the action and why it overrode the…, After the decision: the code's limits pick the action, and whether a write call… (+46 more)

### Community 161 - "Tracer"
Cohesion: 0.05
Nodes (47): AbstractContextManager, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, A named step inside the current trace (a Langfuse `chain`): the generations and… (+39 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "Checks"
Cohesion: 0.40
Nodes (5): Checks, bad_parent(), _consistency(), Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers…

### Community 164 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 165 - "ErrorResponse"
Cohesion: 0.04
Nodes (57): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+49 more)

### Community 166 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 167 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.13
Nodes (19): ForbiddenError, get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, check(), require_roles(), check(), bearer_scheme, Affected Files & Patterns (+11 more)

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "test_stream_answer.py"
Cohesion: 0.25
Nodes (13): 5. What can go wrong, fixture, AnswerController.stream_answer driven directly, for what a test client can't…, A started interview and a controller wired like the app's: returns (controller,…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing() (+5 more)

### Community 170 - "test_select_questions.py"
Cohesion: 0.06
Nodes (51): NotEnoughQuestionsError, load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 1. Why it exists, 2. What it is, 3. When to use it (+43 more)

### Community 171 - "LLMServerError"
Cohesion: 0.23
Nodes (11): LLMServerError, 5xx or a dropped connection: the provider's side failed., test_a_provider_error_hints_that_it_is_not_a_quality_problem(), down(), test_a_provider_error_is_a_failed_errored_case_and_the_run_goes_on(), down(), test_a_provider_error_scores_the_case_failed_and_errored_with_the_class(), down() (+3 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.17
Nodes (15): Baseline Failures, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL), Testing Strategy (+7 more)

### Community 174 - ".stream"
Cohesion: 0.18
Nodes (9): _int_or_none(), Any, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final…, One streamed request: its text chunks, then an LLMResult (attempts and latency…, The token counts an OpenAI-compatible usage object reports; None for any it…, _usage() (+1 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 178 - "clock"
Cohesion: 0.15
Nodes (7): Known Issues, _make(), _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 179 - "Implementation Steps"
Cohesion: 0.15
Nodes (12): Affected Files & Patterns, Implementation Steps, Phase A: plumbing and progress events, Phase B: streaming the question text, Step 11: `FakeProvider.stream`, Step 14: The event loop stays free, Step 15: Evals, Step 16: Measure, document, finish (+4 more)

### Community 180 - "JobRole"
Cohesion: 0.06
Nodes (77): InterviewType, JobRole, Level, BankQuestion, One entry of the hand-written question bank file., The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, SessionOut (+69 more)

### Community 181 - "main.py"
Cohesion: 0.14
Nodes (11): setup_logging(), Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, health_check(), lifespan(), FastAPI, ASGIApp, Architecture & Design (+3 more)

### Community 182 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 183 - "StreamEventOut"
Cohesion: 0.10
Nodes (25): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, _error_event(), _event(), BaseModel, NamedTuple, One event of a streamed turn as the controller yields it; the route encodes it…, StreamEventOut (+17 more)

### Community 184 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 185 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 186 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+2 more)

### Community 187 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6) (+7 more)

### Community 188 - "Platform and DevOps practice"
Cohesion: 0.25
Nodes (7): CI/CD pipelines with safe rollback, Cloud security, backup and recovery, Containers and Kubernetes troubleshooting, Infrastructure as code in practice, Monitoring, alerting and observability, Platform and DevOps practice, Production problems with no obvious cause

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 191 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Changes Made, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 193 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 207 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.13
Nodes (26): contextvars, A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and…, corpus(), embedder(), labelled(), lf(), fixture, quiet() (+18 more)

### Community 220 - "Role"
Cohesion: 0.08
Nodes (26): permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, main(), Session, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry() (+18 more)

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

### Community 234 - "summary"
Cohesion: 0.25
Nodes (6): Constraints, Input, Output, Role, Task, summary()

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - ".stream"
Cohesion: 0.36
Nodes (3): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Reply

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

### Community 244 - "check_layers"
Cohesion: 0.25
Nodes (8): Blockers & Resolutions, Known Issues, check_layers(), _imports(), Every layer-rule violation in `files` (repo-relative path -> source), as…, (absolute module, imported names) per import statement; relative imports…, test_clean_layer_imports_have_no_violations(), _violation()

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "interviewer_v7.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 249 - "interviewer_v7_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 252 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

### Community 253 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 255 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 256 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 257 - "test_generation_eval.py"
Cohesion: 0.17
Nodes (31): 5. What can go wrong, arm_of(), fill(), generated(), lf(), posted(), fixture, parametrize (+23 more)

### Community 258 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 259 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 260 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository)

### Community 262 - "test_tracing.py"
Cohesion: 0.10
Nodes (10): client(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, _settings(), test_both_keys_build_an_enabled_tracer(), test_close_on_a_disabled_tracer_does_nothing(), test_no_keys_builds_a_disabled_tracer_without_warning() (+2 more)

### Community 264 - "_Usage"
Cohesion: 0.67
Nodes (3): The four usage fields of FeedbackCaseResult, so `**_usage(...)` is checked…, _Usage, TypedDict

### Community 268 - "FakeLangfuse"
Cohesion: 0.09
Nodes (15): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+7 more)

## Knowledge Gaps
- **846 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+841 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2082 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **60 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `traces`, `test_generation_eval.py`, `Completed Steps`, `test_tracing.py`, `interviews_rag_evals.py`, `FakeLangfuse`, `ChatMessage`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `get_llm_provider`, `interviews_constants.py`, `test_feedback_endpoint.py`, `test_profile_evals.py`, `interviews_answer_service.py`, `test_evals.py`, `FakeClient`, `test_tracing_routes.py`, `test_profile_routes.py`, `interviews_feedback_evals.py`, `traced`, `provider.py`, `test_retrieval_eval.py`, `interviews_service.py`, `EvalCase`, `test_factory.py`, `interviews_evals.py`, `interviews_feedback_service.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `Feature: Langfuse experiments for the interviews evals`, `LLMProvider`, `ProfileLLM`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `Completed Steps`, `config.py`, `tests/conftest.py`, `auth_service.py`, `interviews_route.py`, `get_llm_provider`, `Implementation Plan: Role-Based Access Control (single JWT)`, `interviews_job_url_service.py`, `interviews_answer_service.py`, `interviews_model.py`, `JobRole`, `test_create_interview.py`, `Implementation Plan: UUID primary keys`, `InterviewsRepository`, `profile_service.py`, `PageParams`, `InterviewQuestion`, `errors.py`, `profile_dependencies.py`, `provider.py`, `interviews_service.py`, `Role`, `Implementation: Langfuse Tracing`, `interviews_feedback_service.py`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `interviews_schema.py`, `test_interview_report.py`, `build_usage_report`, `test_list_interviews.py`, `.record_turn`, `test_turn_budget.py`, `test_follow_ups.py`, `test_feedback_endpoint.py`, `test_answer_stream.py`, `test_transcript.py`, `interviews/conftest.py`, `Checks`, `interviews_context.py`, `interviews_answer_service.py`, `test_feedback_contract.py`, `interviews_model.py`, `LLMResult`, `JobRole`, `test_create_interview.py`, `test_start_llm.py`, `interviews_report.py`, `InterviewsRepository`, `test_answer_llm.py`, `provider.py`, `interviews_service.py`, `test_interviewer_messages.py`, `test_context_controller.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Are the 49 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 49 INFERRED edges - model-reasoned connections that need verification._
- **Are the 40 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 29 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._