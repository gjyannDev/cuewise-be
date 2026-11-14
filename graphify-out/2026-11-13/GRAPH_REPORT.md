# Graph Report - cuewise-be  (2026-11-13)

## Corpus Check
- 368 files · ~335,066 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 5119 nodes · 14435 edges · 269 communities (230 shown, 39 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2778 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e45e503f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- AuthService
- Implementation Plan: Langfuse Tracing
- interviews_constants.py
- errors.py
- test_interview_report.py
- Role
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- interviews_knowledge_utils.py
- test_guards.py
- Tracer
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- interviews_job_url_utils.py
- test_feedback_evals.py
- test_safe_fetch.py
- User
- test_tracing_lifespan.py
- cuewise-be
- LLMProvider
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_transcript.py
- KnowledgeRepository
- Feature: Context Management for the Interview LLM Calls
- RateLimiter
- RetrievalService
- test_reference_note_context.py
- SafeFetcher
- Feature: LLM as the Interviewer (it asks the questions)
- QuestionTurn
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
- FollowUpAction
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- FakeClient
- test_tracing_routes.py
- InterviewsRepository
- ConsoleFormatter
- job_description_summary_v2.md
- test_reply_contract.py
- FakeEmbedder
- test_follow_ups.py
- hint_for
- interviews_feedback_service.py
- test_answer_llm.py
- test_eval_runs.py
- ContextManager
- exception_handlers.py
- AppError
- test_tracing.py
- interviews_feedback_evals.py
- Slices in detail
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- test_stream_answer.py
- EmbeddingKind
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- WriteText
- ChatMessage
- LLMError
- traced
- Completed Steps
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- AnswerService
- clock
- Langfuse Observability
- interviewer_v3.md
- Implementation: LLM as the Interviewer (it asks the questions)
- ._covers_every_criterion
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
- FeedbackGenerator
- main
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
- StreamedTurn
- Implementation: Three New Interview Roles (designer, qa, devops)
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Feature: Résumé upload and candidate profile (Slice 8c)
- How to evaluate an AI feature: from the command to the fix
- InterviewQuestion
- Langfuse Dataset Construction
- Langfuse v4 project migration
- Implementation: Error Handling
- Implementation: Interview History List (backend)
- Judge Calibration
- Feature: Interview History List (backend)
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- test_request_context.py
- test_knowledge_ingest.py
- test_context.py
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- Learn: Splitting the interviews dependency wiring
- get_llm_provider
- test_generation_eval.py
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- Implementation: Layered Modules (route -> controller -> service -> repository)
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- JobRole
- llm
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_answer_interview.py
- InterviewsService
- experiments
- ErrorResponse
- select_questions
- Implementation Plan: Role-Based Access Control (single JWT)
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_fallback_pick.py
- test_select_questions.py
- interviews_feedback.py
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- LLMResult
- feedback_score_v1.md
- feedback_write_v1.md
- Feature: Follow-up Questions (decide / write split)
- Learn: Follow-up questions (decide / write split)
- .record_turn
- test_question_bank.py
- AI Engineering Learning Path (Cuewise)
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Layered Modules (route -> controller -> service -> repository)
- InterviewMessage
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- Feature: Interview Feedback and Scoring (Slice 6)
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- users_utils.py
- _reset_request_id
- test_job_description_summary.py
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
- auth_header
- Communication and priorities
- Engineering habits
- Senior judgement
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- fixture
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- Langfuse CLI Reference
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- Learn: Layered architecture (route -> controller -> service -> repository)
- _Stt
- Learn: Job URL import and SSRF (Slice 8b)
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- Langfuse
- traces
- run
- 2. Langfuse Documentation
- Implementation Plan: Context Management for the Interview LLM Calls
- Steps
- get_feedback_service
- Learn: Langfuse experiments for the interviews evals
- lf
- Affected Files & Patterns
- Checks
- Completed Steps
- lf
- FakeLangfuse

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 112 edges
2. `User` - 112 edges
3. `FakeProvider` - 107 edges
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

## Communities (269 total, 39 thin omitted)

### Community 0 - "AuthService"
Cohesion: 0.11
Nodes (28): AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), post, register(), LoginIn (+20 more)

### Community 1 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.10
Nodes (16): Generation, _model_parameters(), ReasoningEffort, What the call asked the model for, shown on the generation. A temperature only…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Implementation Steps (+8 more)

### Community 2 - "interviews_constants.py"
Cohesion: 0.09
Nodes (46): MessageKind, MessageRole, StrEnum, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Why an interview has no reference notes at all (logged as…, Transcript item kinds: a question comes from interview_questions, the other two…, RetrievalSkip (+38 more)

### Community 3 - "errors.py"
Cohesion: 0.09
Nodes (42): BadRequestError, ConflictError, ErrorBody, InvalidCredentialsError, NotFoundError, BaseModel, TokenExpiredError, TokenInvalidError (+34 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (54): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http() (+46 more)

### Community 5 - "Role"
Cohesion: 0.08
Nodes (26): verify_password(), permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, AuthRepository, Session, main() (+18 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "interviews_knowledge_utils.py"
Cohesion: 0.08
Nodes (50): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, cosine_similarity(), _hash(), _listed() (+42 more)

### Community 9 - "test_guards.py"
Cohesion: 0.09
Nodes (28): health_check(), list_users(), PageDep, CurrentUserDep, raise_crash(), raise_db_down(), raise_integrity(), admin_role() (+20 more)

### Community 10 - "Tracer"
Cohesion: 0.06
Nodes (75): build_tracer(), Create the dataset if needed and upsert its items (each carries its own `id`,…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, Send what is still buffered, then stop the background exporter. Called once at…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, Tracer, final_line(), The console's last line: which Langfuse runs to open, or why nothing was… (+67 more)

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
Cohesion: 0.12
Nodes (26): anyio_backend(), Clock, listen_body(), make_transcriber(), _make(), ok(), fixture, parametrize (+18 more)

### Community 16 - "interviews_job_url_utils.py"
Cohesion: 0.13
Nodes (17): _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), _plain(), _posting_text(), Turn a fetched job page into plain job-description text (Slice 8b). Pure…, A JSON-LD description is usually HTML, sometimes entity-escaped HTML: unescape,… (+9 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.07
Nodes (66): check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult, FeedbackEvalCase (+58 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (42): FetchedPage, Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request (+34 more)

### Community 19 - "User"
Cohesion: 0.09
Nodes (54): alias, AnswerControllerDep, RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Permission, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions() (+46 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "LLMProvider"
Cohesion: 0.07
Nodes (44): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., LLMProvider, Protocol, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, decide() (+36 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.15
Nodes (35): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate… (+27 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.08
Nodes (66): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 8. Check your understanding, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback), fresh_limiter() (+58 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (37): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+29 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.09
Nodes (17): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+9 more)

### Community 31 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 32 - "KnowledgeRepository"
Cohesion: 0.10
Nodes (21): KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a…, _embed(), ingest_corpus(), IngestCounts (+13 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "RateLimiter"
Cohesion: 0.18
Nodes (13): RateLimiter, Count one request for `key`: None when allowed, else whole seconds until its…, get_transcription_limiter(), limit_transcriptions(), interviews_answer, Tests swap in a fresh limiter so counts never leak between them., Per-user cap on transcriptions, checked before the upload goes anywhere that…, Clock (+5 more)

### Community 35 - "RetrievalService"
Cohesion: 0.17
Nodes (15): Why vector mode fell back to filter mode (logged as…, RetrievalDegrade, _eligible(), EligibleChunk, NamedTuple, Active chunks scoped to this role (or every role) and this level. Role and…, The k eligible chunks embedded with `model` that are most similar to the query,…, _log_level() (+7 more)

### Community 36 - "test_reference_note_context.py"
Cohesion: 0.15
Nodes (22): A main-question write of an interview with reference notes: the notes-aware…, WindowLedger, WithReferenceNotes, 5. What can go wrong, first_user(), inputs(), _max_note(), anyio (+14 more)

### Community 37 - "SafeFetcher"
Cohesion: 0.06
Nodes (26): _decode(), FetchError, BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach…, Scheme, credentials, port and every resolved address. Returns the address to…, One hop: a page, or the redirect's Location to check next. (+18 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.11
Nodes (19): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+11 more)

### Community 39 - "QuestionTurn"
Cohesion: 0.07
Nodes (47): build_interviewer_messages(), interviewer_history(), job_description_block(), main_numbers(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, The main-question number of each turn: a follow-up shares the number of the… (+39 more)

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
Nodes (29): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+21 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.12
Nodes (31): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, Any network-side failure of a job link. One message for every cause, so…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError (+23 more)

### Community 45 - "interviews_answer_service.py"
Cohesion: 0.11
Nodes (36): PhaseChanged, The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), _error_event(), _event(), _frame(), AnswerEvent (+28 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.11
Nodes (16): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_125_s_or_an_unreported_duration_is_accepted(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415() (+8 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.07
Nodes (99): FakeProvider, build_context_manager(), `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, load_cases(), main(), Path, run_case(), 5. What can go wrong (+91 more)

### Community 49 - "test_feedback_contract.py"
Cohesion: 0.17
Nodes (35): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, load_object(), The reply as a JSON object: one optional fence around it, nothing else before… (+27 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.04
Nodes (59): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so… (+51 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.09
Nodes (43): InterviewerInputs, Plain values for one interviewer or decide call., One budget for the whole generation, started when the request holds its claim., Decision, Interviewer, apply_limits(), Deadline, _decision_label() (+35 more)

### Community 52 - "FollowUpAction"
Cohesion: 0.22
Nodes (18): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect (+10 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.16
Nodes (19): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+11 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.14
Nodes (37): 5. What can go wrong, fail(), error(), import_url(), _post(), long_posting(), page(), paste() (+29 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (26): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), _make(), ok() (+18 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (62): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+54 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "FakeClient"
Cohesion: 0.10
Nodes (10): FakeClient, FakeObservation, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_reports_whether_it_was_sent(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises(), test_steps_and_checks_are_no_ops_when_off_and_never_raise_when_langfuse_fails(), test_trace_with_a_broken_sdk_still_runs_the_body_and_keeps_its_exception() (+2 more)

### Community 61 - "InterviewsRepository"
Cohesion: 0.07
Nodes (33): HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, InterviewSession, _history_filter(), _history_order(), InterviewsRepository (+25 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.06
Nodes (40): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites, ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message… (+32 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_reply_contract.py"
Cohesion: 0.23
Nodes (22): follow_up(), parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_follow_up_in_a_behavioral_only_interview_keeps_the_behavioral_category(), test_a_follow_up_is_accepted_without_a_category_and_inherits_the_parents() (+14 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.18
Nodes (26): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), parametrize, RetrievalService.retrieve: the vector / filter / skip ladder (knowledge-base-…, retrieve() (+18 more)

### Community 66 - "test_follow_ups.py"
Cohesion: 0.23
Nodes (18): 5. What can go wrong, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+10 more)

### Community 67 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 68 - "interviews_feedback_service.py"
Cohesion: 0.08
Nodes (48): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackScoreInputs, FeedbackWriteInputs (+40 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.11
Nodes (23): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages() (+15 more)

### Community 71 - "test_eval_runs.py"
Cohesion: 0.06
Nodes (47): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), git_commit(), notes_fingerprint(), Any, Score (+39 more)

### Community 72 - "ContextManager"
Cohesion: 0.10
Nodes (33): anyio, ContextManager, Context management: the one place that decides what each LLM call sends. The…, Embedder, Protocol, The embedding contract features code against, separate from the chat…, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or…, The LLM contract every feature codes against: message/result types, typed… (+25 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "AppError"
Cohesion: 0.09
Nodes (30): Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, NoSpeechError, Any (+22 more)

### Community 75 - "test_tracing.py"
Cohesion: 0.10
Nodes (10): client(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, _settings(), test_both_keys_build_an_enabled_tracer(), test_close_on_a_disabled_tracer_does_nothing(), test_no_keys_builds_a_disabled_tracer_without_warning() (+2 more)

### Community 76 - "interviews_feedback_evals.py"
Cohesion: 0.12
Nodes (18): Band, _band_check(), feedback_run_scores(), FeedbackEvalQuestion, FeedbackEvalTurn, FeedbackSummary, _print_summary(), BaseModel (+10 more)

### Community 77 - "Slices in detail"
Cohesion: 0.11
Nodes (18): 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety (+10 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "test_stream_answer.py"
Cohesion: 0.11
Nodes (23): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+15 more)

### Community 82 - "EmbeddingKind"
Cohesion: 0.08
Nodes (39): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, A vector of another length than configured. Vectors of different sizes can't be…, EmbedCall, GoogleEmbedder (+31 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "WriteText"
Cohesion: 0.24
Nodes (9): _check_lengths(), parse_write_reply(), The labelled text the write call is asked for (the parser reads it back…, The write call's text, slot by slot: every section once and in order, list…, _slots(), WriteText, test_a_valid_write_reply_is_parsed_into_slots(), test_blank_lines_and_a_wrapped_summary_are_accepted() (+1 more)

### Community 85 - "ChatMessage"
Cohesion: 0.09
Nodes (22): StrategyOutput, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, _counts(), FeedbackWrite (+14 more)

### Community 86 - "LLMError"
Cohesion: 0.07
Nodes (35): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The first channel's best transcript (blank for silence) and the reported audio…, LLMError (+27 more)

### Community 87 - "traced"
Cohesion: 0.19
Nodes (17): drain(), result(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage(), test_disabled_tracer_is_a_pass_through(), test_failed_call_is_marked_error_and_the_same_exception_is_raised(), test_missing_usage_is_omitted_never_guessed(), test_retried_call_is_one_generation_with_attempts() (+9 more)

### Community 88 - "Completed Steps"
Cohesion: 0.10
Nodes (44): build_sheet(), competencies_of(), filter_baseline(), Collection, Exception, _ranking(), _rating(), The grading file can't be read; the message starts with the line and gives the… (+36 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "AnswerService"
Cohesion: 0.10
Nodes (26): AnswerController, UUID, The checks and reads before the stream opens (sync DB work: the route runs it…, AnswerIn, AnswerService, AnswerEvent, Random, UUID (+18 more)

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
Cohesion: 0.09
Nodes (32): build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, TracingProvider, model_validator (+24 more)

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
Nodes (70): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_reply() (+62 more)

### Community 109 - "FeedbackGenerator"
Cohesion: 0.11
Nodes (19): BuiltContext, ContextReport, _log(), NamedTuple, _Attempts, CallUsage, FeedbackGenerator, log_feedback_summary() (+11 more)

### Community 110 - "main"
Cohesion: 0.10
Nodes (30): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+22 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional (+6 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "QuestionCategory"
Cohesion: 0.09
Nodes (43): HeaderSplit, InterviewerReply, parse_interviewer_reply(), parse_streamed_reply(), NamedTuple, interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, interviewer_v5's finished question text, checked like a v4 reply. It was…, split_header() (+35 more)

### Community 115 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.14
Nodes (13): 13. Phase 2 real runs (yours), Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 116 - "pytest"
Cohesion: 0.13
Nodes (20): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, pytest, parametrize, test_each_role_list_includes_the_shared_terms_once() (+12 more)

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

### Community 121 - "StreamedTurn"
Cohesion: 0.15
Nodes (11): parse_sse(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json() (+3 more)

### Community 122 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 123 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope (+3 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.12
Nodes (14): The notes stored for this interview at start, rank order; none for interviews…, 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links (+6 more)

### Community 125 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal, Non-Functional (+6 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.13
Nodes (14): 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse, 7. Fix: the smallest change in the right place (+6 more)

### Community 127 - "InterviewQuestion"
Cohesion: 0.15
Nodes (19): InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, Every stored question, grouped by interview in creation order (UUIDv7), for the…, main(), Session, candidate_messages(), noted(), fixture (+11 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "Implementation: Error Handling"
Cohesion: 0.12
Nodes (15): RequestIdFilter, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions (+7 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

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

### Community 143 - "test_context.py"
Cohesion: 0.15
Nodes (17): estimate_tokens(), Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default() (+9 more)

### Community 144 - "PageParams"
Cohesion: 0.07
Nodes (35): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, get_db() (+27 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_turn_budget.py"
Cohesion: 0.20
Nodes (15): Testing Strategy, Testing Strategy, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result() (+7 more)

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
Nodes (40): get_answer_controller(), get_answer_service(), Depends, Session, get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., get_bank(), get_clock() (+32 more)

### Community 152 - "test_generation_eval.py"
Cohesion: 0.24
Nodes (21): arm_of(), fill(), generated(), posted(), parametrize, quiet(), `run_generation` as Langfuse experiment runs (langfuse-experiments Step 11;…, A recorded generation run: its sheet, key and traces file in tmp_path. (+13 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.15
Nodes (12): Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (26): corpus(), embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of() (+18 more)

### Community 156 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.27
Nodes (13): main(), _parser(), ArgumentParser, Session, ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1() (+5 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "JobRole"
Cohesion: 0.08
Nodes (58): FullHistory, What the interview LLM calls send: the tasks and strategies registered with the…, A running note is optional model output about the latest answer; it is sent…, validate_note(), InterviewType, JobRole, Level, EvalSetup (+50 more)

### Community 160 - "llm"
Cohesion: 0.16
Nodes (11): as_v5_text(), _decision_json(), llm(), script(), script_decide(), script_score(), script_write(), unique_question() (+3 more)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.05
Nodes (44): AbstractContextManager, Any, The stream was closed before it finished (client left, or the turn's deadline…, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, A named step inside the current trace (a Langfuse `chain`): the generations and… (+36 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "InterviewsService"
Cohesion: 0.16
Nodes (13): HistoryPage, InterviewsService, InterviewState, NamedTuple, Random, UUID, One page of the user's interviews, each with its answered main-question count,…, Transcript (+5 more)

### Community 164 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 165 - "ErrorResponse"
Cohesion: 0.04
Nodes (56): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+48 more)

### Community 166 - "select_questions"
Cohesion: 0.07
Nodes (25): Random, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 4. How it works, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec) (+17 more)

### Community 167 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.06
Nodes (32): ForbiddenError, Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, get_current_user(), get_service(), Depends, Session, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates… (+24 more)

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "test_fallback_pick.py"
Cohesion: 0.19
Nodes (16): NotEnoughQuestionsError, pick_fallback_question(), Collection, One unused bank question for `position`, used when the LLM is off or its reply…, Deviations from Plan, fixture_bank(), pick(), fixture (+8 more)

### Community 170 - "test_select_questions.py"
Cohesion: 0.29
Nodes (16): _bank(), parametrize, _q(), _select(), test_general_question_is_eligible_for_every_role(), test_mixed_even_count_is_an_exact_split(), test_mixed_short_on_one_type_is_rejected_without_rebalancing(), test_mixed_splits_evenly_extra_behavioral_and_interleaves() (+8 more)

### Community 171 - "interviews_feedback.py"
Cohesion: 0.08
Nodes (52): Task, FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, build_threads(), Evidence, FeedbackThread, _has_markup(), _normalized() (+44 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.13
Nodes (19): Baseline Failures, Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material (+11 more)

### Community 174 - "LLMResult"
Cohesion: 0.10
Nodes (23): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+15 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 178 - "Learn: Follow-up questions (decide / write split)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split)

### Community 179 - ".record_turn"
Cohesion: 0.08
Nodes (32): QuestionNotCurrentError, ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Save one whole turn in one commit: advance the session, the answer, the…, AnswerOut, Turn the outcome into rows and save the whole turn in one commit. `reaction` is…, 4. How it works, Affected Files & Patterns (+24 more)

### Community 180 - "test_question_bank.py"
Cohesion: 0.22
Nodes (14): load_bank(), load_rubric(), Path, Read and validate a feedback rubric file; a bad one fails loudly at startup,…, Read and validate a question bank file; a bad file fails loudly instead of at…, 5. What can go wrong, Test Results, _entry() (+6 more)

### Community 181 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.18
Nodes (10): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slices (+2 more)

### Community 182 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 183 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 184 - "InterviewMessage"
Cohesion: 0.11
Nodes (20): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_a_future_question_is_not_current_either() (+12 more)

### Community 185 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 186 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional (+5 more)

### Community 187 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 188 - "Platform and DevOps practice"
Cohesion: 0.25
Nodes (7): CI/CD pipelines with safe rollback, Cloud security, backup and recovery, Containers and Kubernetes troubleshooting, Infrastructure as code in practice, Monitoring, alerting and observability, Platform and DevOps practice, Production problems with no obvious cause

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 191 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 207 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.20
Nodes (19): embedder(), labelled(), quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, 15 cases with the kinds the label rules require: most expect API design first;…, run(), summary_numbers(), test_a_case_set_that_breaks_the_label_rules_is_still_refused() (+11 more)

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

### Community 234 - "auth_header"
Cohesion: 0.16
Nodes (14): Affected Files & Patterns, auth_header(), _header(), client(), make_user(), _make(), fixture, Bearer header for a user; pass role to mint a token whose role claim differs… (+6 more)

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

### Community 244 - "fixture"
Cohesion: 0.17
Nodes (12): answer(), _answer(), anyio_backend(), fixture, Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a recording to the transcription endpoint; `audio=None` sends no file part…, POST a setup for `user`; any field can be overridden, or dropped by passing…, POST an answer; `question_id` defaults to whatever the caller passes, body… (+4 more)

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

### Community 250 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (9): Reload rows a commit expired, so reading their fields later needs no database…, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 251 - "_Stt"
Cohesion: 0.24
Nodes (5): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank)., _Stt

### Community 252 - "Learn: Job URL import and SSRF (Slice 8b)"
Cohesion: 0.20
Nodes (9): is_public_address(), True only for a globally routable unicast address., 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 253 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Résumé upload and candidate profile (Slice 8c), Implementation Steps, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 255 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 256 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 257 - "run"
Cohesion: 0.24
Nodes (9): The console with each arm row's start_ms (wall-clock time) dropped, and without…, A fake LLM: a new, valid main question per call; it can fail every call that…, run(), table_without_timings(), test_an_arm_failing_for_a_setup_leaves_it_off_the_sheet_but_recorded(), test_generation_stops_before_any_call_when_no_notes_are_ingested(), test_the_console_sheet_and_key_are_the_same_with_and_without_langfuse(), test_without_keys_no_traces_file_is_written_and_a_stale_one_is_removed() (+1 more)

### Community 258 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 259 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 261 - "get_feedback_service"
Cohesion: 0.29
Nodes (8): get_feedback_service(), datetime, Depends, Session, get_now(), datetime, Wall-clock time for stored timestamps (the feedback claim and its stale…, _utc_now()

### Community 262 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 263 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

### Community 264 - "Affected Files & Patterns"
Cohesion: 0.33
Nodes (5): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns

### Community 265 - "Checks"
Cohesion: 0.40
Nodes (5): Checks, bad_parent(), _consistency(), Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers…

### Community 266 - "Completed Steps"
Cohesion: 0.50
Nodes (5): One streamed-turn event as the dict sse-starlette encodes: the event name, and…, The controller's events as SSE frames. Closing this (a client that left) closes…, sse_frame(), sse_frames(), Completed Steps

### Community 268 - "FakeLangfuse"
Cohesion: 0.09
Nodes (15): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+7 more)

## Knowledge Gaps
- **832 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+827 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1955 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **39 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `traces`, `Implementation Plan: Langfuse Tracing`, `run`, `get_feedback_service`, `FakeLangfuse`, `test_feedback_evals.py`, `User`, `test_tracing_lifespan.py`, `get_llm_provider`, `test_generation_eval.py`, `LLMProvider`, `test_feedback_endpoint.py`, `KnowledgeRepository`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `RetrievalService`, `InterviewsService`, `experiments`, `interviews_answer_service.py`, `test_evals.py`, `FakeClient`, `test_tracing_routes.py`, `interviews_feedback_service.py`, `test_eval_runs.py`, `ContextManager`, `test_tracing.py`, `interviews_feedback_evals.py`, `test_retrieval_eval.py`, `ChatMessage`, `traced`, `AnswerService`, `test_factory.py`, `interviews_evals.py`, `FeedbackGenerator`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `Feature: Langfuse experiments for the interviews evals`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `AuthService`, `interviews_constants.py`, `errors.py`, `Role`, `PageParams`, `get_llm_provider`, `RateLimiter`, `InterviewsService`, `Implementation Plan: Role-Based Access Control (single JWT)`, `interviews_job_url_service.py`, `interviews_answer_service.py`, `interviews_model.py`, `test_create_interview.py`, `InterviewsRepository`, `interviews_feedback_service.py`, `ContextManager`, `AppError`, `AnswerService`, `Implementation: Langfuse Tracing`, `Implementation Plan: UUID primary keys`, `auth_header`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `Implementation Plan: Langfuse Tracing`, `interviews_constants.py`, `run`, `test_feedback_evals.py`, `test_turn_budget.py`, `test_generation_eval.py`, `LLMProvider`, `JobRole`, `InterviewsService`, `test_evals.py`, `InterviewerInputs`, `test_start_llm.py`, `test_openai_compatible_stream.py`, `interviews_feedback_service.py`, `test_answer_llm.py`, `ContextManager`, `test_tracing.py`, `interviews_feedback_evals.py`, `test_job_description_summary.py`, `ChatMessage`, `LLMError`, `traced`, `test_factory.py`, `interviews_evals.py`, `FeedbackGenerator`, `Feature: Langfuse Tracing`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 47 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Are the 28 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 28 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._