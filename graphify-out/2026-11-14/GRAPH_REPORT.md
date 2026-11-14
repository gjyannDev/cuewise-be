# Graph Report - cuewise-be  (2026-11-13)

## Corpus Check
- 369 files · ~335,797 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 5146 nodes · 14519 edges · 269 communities (229 shown, 40 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2787 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e45e503f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- AuthController
- LLMServerError
- test_knowledge_postgres.py
- decode_token
- test_interview_report.py
- auth_dependencies.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- interviews_constants.py
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
- User
- test_tracing_lifespan.py
- cuewise-be
- LLMResult
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
- interviews_job_url_service.py
- AnswerService
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_evals.py
- test_feedback_contract.py
- interviews_model.py
- Interviewer
- FollowUpAction
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- FakeClient
- test_tracing_routes.py
- InterviewQuestion
- ConsoleFormatter
- job_description_summary_v2.md
- typing
- FakeEmbedder
- test_follow_ups.py
- hint_for
- interviews_feedback_service.py
- test_answer_llm.py
- interviews_feedback_evals.py
- interviews_transcription_dependencies.py
- exception_handlers.py
- errors.py
- test_tracing.py
- check_feedback
- Implementation Steps
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- run_feedback_case
- fake.py
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- interviews_log.py
- interviews_context.py
- LLMTimeoutError
- traced
- test_reaction_pick.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- FeedbackCaseResult
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
- InterviewType
- Implementation: Langfuse experiments for the interviews evals
- audio_container
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Langfuse Implementation Notes
- interviewer_v5.md
- Feature: Langfuse experiments for the interviews evals
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation: Three New Interview Roles (designer, qa, devops)
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Feature: Résumé upload and candidate profile (Slice 8c)
- How to evaluate an AI feature: from the command to the fix
- test_context_controller.py
- Langfuse Dataset Construction
- Langfuse v4 project migration
- tests/conftest.py
- Implementation: Interview History List (backend)
- Judge Calibration
- Feature: Interview History List (backend)
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- re
- test_knowledge_ingest.py
- test_context.py
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- Learn: Splitting the interviews dependency wiring
- interviews_feedback_dependencies.py
- run_ranking
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- Implementation: Layered Modules (route -> controller -> service -> repository)
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- test_context_prompts.py
- interviews/conftest.py
- Tracer
- test_answer_interview.py
- interviews_answer_service.py
- experiments
- ErrorResponse
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- require_permissions
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- interviews_utils.py
- test_select_questions.py
- interviews_feedback.py
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- OpenAICompatibleProvider
- feedback_score_v1.md
- feedback_write_v1.md
- Feature: Follow-up Questions (decide / write split)
- Feature: Start an Interview (backend)
- .record_turn
- JobRole
- middleware.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Layered Modules (route -> controller -> service -> repository)
- Implementation Plan: Role-Based Access Control (single JWT)
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
- pytest
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
- FeedbackEvalCase
- Communication and priorities
- Engineering habits
- Senior judgement
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- Implementation Plan: Follow-up Questions (decide / write split)
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- Langfuse CLI Reference
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- Learn: Layered architecture (route -> controller -> service -> repository)
- TranscriptionResult
- Feature: Role-Based Access Control (single JWT)
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- Langfuse
- traces
- test_generation_eval.py
- 2. Langfuse Documentation
- Web
- parse_log
- test_login.py
- Learn: Langfuse experiments for the interviews evals
- lf
- ContextManager
- compute_overall
- .stream
- FakeLangfuse

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 113 edges
2. `User` - 112 edges
3. `FakeProvider` - 110 edges
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

## Communities (269 total, 40 thin omitted)

### Community 0 - "AuthController"
Cohesion: 0.21
Nodes (16): AuthController, Request -> service call, domain result -> response schema., login(), me(), post, register(), LoginIn, MeOut (+8 more)

### Community 1 - "LLMServerError"
Cohesion: 0.10
Nodes (36): anyio, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Any, Gemini embeddings through Google's native `batchEmbedContents` endpoint, over…, OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, LLMError, LLMRateLimitError, LLMServerError (+28 more)

### Community 2 - "test_knowledge_postgres.py"
Cohesion: 0.11
Nodes (25): alembic_config, KnowledgeChunk, cuewise-be, Development database (Postgres 18 + pgvector), Reference notes (knowledge-base RAG), sqlalchemy_dialects, sqlalchemy_exc, chunk() (+17 more)

### Community 3 - "decode_token"
Cohesion: 0.17
Nodes (28): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+20 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.12
Nodes (58): log_retrieval(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, Which reference notes an interview got at start: mode, count, scores and the…, analysis(), answer(), emit_answer_turn(), emit_call() (+50 more)

### Community 5 - "auth_dependencies.py"
Cohesion: 0.09
Nodes (27): hash_password(), verify_password(), get_controller(), get_service(), Session, AuthRepository, Session, UUID (+19 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.13
Nodes (35): extract_job_text(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, At most `limit` characters, cut at the last whitespace so no word is split;…, truncate_on_word(), jsonld(), page() (+27 more)

### Community 8 - "interviews_constants.py"
Cohesion: 0.08
Nodes (50): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+42 more)

### Community 9 - "Role"
Cohesion: 0.11
Nodes (29): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry() (+21 more)

### Community 10 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (93): Local time, as the Langfuse list shows the run's start: the name and the…, run_stamp(), _arm_notes(), ArmInterview, ArmSummary, build_sheet(), case_set_problems(), competencies_of() (+85 more)

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

### Community 16 - "interviews_job_url_utils.py"
Cohesion: 0.11
Nodes (20): _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), job_term_hits(), _plain(), _posting_text(), Turn a fetched job page into plain job-description text (Slice 8b). Pure… (+12 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.16
Nodes (19): Grader, Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The…, A fake provider: scores every criterion `value`, quoting the start of each…, _result(), run_main(), scores_on(), test_a_langfuse_outage_does_not_change_the_run(), test_a_single_run_posts_no_spread() (+11 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (42): FetchedPage, Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request (+34 more)

### Community 19 - "User"
Cohesion: 0.06
Nodes (78): alias, AnswerControllerDep, User, HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, interview_out() (+70 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "LLMResult"
Cohesion: 0.09
Nodes (51): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., LLMResult, The LLM contract every feature codes against: message/result types, typed…, decide(), UUID, The decide step of an answer turn: the model suggests following up or moving… (+43 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.15
Nodes (35): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate… (+27 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.07
Nodes (75): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, Who wrote the feedback text: the write call, or the code's template when that…, TextSource, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists (+67 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (37): 5. What can go wrong, decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+29 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.06
Nodes (32): 5. What can go wrong, 6. Try it yourself, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing() (+24 more)

### Community 31 - "test_transcript.py"
Cohesion: 0.28
Nodes (10): fixture, shape(), started(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question(), test_missing_and_foreign_sessions_are_the_same_404() (+2 more)

### Community 32 - "KnowledgeRepository"
Cohesion: 0.08
Nodes (34): Embedder, Protocol, KnowledgeRepository, Session, Database access for the reference-note corpus. No business rules: which rows to…, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a… (+26 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "RateLimiter"
Cohesion: 0.22
Nodes (10): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window(), test_refused_hits_do_not_extend_the_window() (+2 more)

### Community 35 - "Completed Steps"
Cohesion: 0.11
Nodes (29): log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, _eligible(), EligibleChunk (+21 more)

### Community 36 - "test_reference_note_context.py"
Cohesion: 0.17
Nodes (21): A note an interview was given: what the question writer sees (competency and…, ReferenceNote, 5. What can go wrong, first_user(), inputs(), _max_note(), anyio, parametrize (+13 more)

### Community 37 - "safe_fetch.py"
Cohesion: 0.09
Nodes (17): FetchError, is_public_address(), BaseTransport, Exception, Fetch a web page whose address a user chose, without letting that user reach…, True only for a globally routable unicast address., codecs, 1. Why it exists (+9 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "QuestionTurn"
Cohesion: 0.08
Nodes (43): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the… (+35 more)

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
Nodes (33): Checks, bad_parent(), Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, Each check with the problems it found (none = passed)., _cell_class(), _heading(), _html_block() (+25 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.07
Nodes (52): JobTextUnreadableError, JobUrlUnreachableError, A pasted page held no job description (too little text, or not recognisably a…, Any network-side failure of a job link. One message for every cause, so…, _decode(), Response, Header charset, else a <meta> charset, else UTF-8; never raises (bad bytes…, The server answered, but not with an HTML page we are willing to read. (+44 more)

### Community 45 - "AnswerService"
Cohesion: 0.06
Nodes (61): QuestionNotCurrentError, log_stream_summary(), How a streamed turn felt and ended: time to the first event and to the first…, PhaseChanged, The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), AnswerController (+53 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.07
Nodes (100): FakeProvider, load_cases(), main(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, run_case(), 5. What can go wrong (+92 more)

### Community 49 - "test_feedback_contract.py"
Cohesion: 0.20
Nodes (30): assess_evidence(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The pre-check, before any LLM call: enough main questions have a real answer to…, parametrize, question_json(), The feedback contract (interviews_feedback.py): the code pre-check, the score…, reason_of() (+22 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.10
Nodes (28): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin (+20 more)

### Community 51 - "Interviewer"
Cohesion: 0.19
Nodes (16): Interviewer, Deadline, The turn's LLM time budget, set once and asked by every call (an injectable…, UUID, The same turn as `answer_turn` (same decide, limits and fallbacks), telling the…, What the turn does after the decision, before the write call: shared by the…, TurnOutcome, WritePlan (+8 more)

### Community 52 - "FollowUpAction"
Cohesion: 0.11
Nodes (32): Decision, parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, apply_limits(), plan_write(), The code's say over the model's: returns the action and why it overrode the…, After the decision: the code's limits pick the action, and whether a write call… (+24 more)

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
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.09
Nodes (50): analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table(), _consistency(), _cost() (+42 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (34): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+26 more)

### Community 59 - "FakeClient"
Cohesion: 0.10
Nodes (10): FakeClient, FakeObservation, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_reports_whether_it_was_sent(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises(), test_steps_and_checks_are_no_ops_when_off_and_never_raise_when_langfuse_fails(), test_trace_with_a_broken_sdk_still_runs_the_body_and_keeps_its_exception() (+2 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.05
Nodes (52): InterviewMessage, InterviewQuestion, InterviewSession, A candidate answer or the interviewer's reaction to one question. The questions…, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter(), _history_order(), InterviewsRepository (+44 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.05
Nodes (42): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites, ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message… (+34 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 65 - "FakeEmbedder"
Cohesion: 0.11
Nodes (34): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, test_fake_embedder_honors_scripted_vectors_and_errors(), test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets(), competencies(), corpus() (+26 more)

### Community 66 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): 8. Check your understanding, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 67 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 68 - "interviews_feedback_service.py"
Cohesion: 0.10
Nodes (30): FeedbackFailedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackWriteInputs, Plain values for the write call: the stored scores and evidence, never the…, build_threads(), FeedbackThread, The scores and evidence from the score call, then the text. Read back through…, The validated scores with their questions' text and category, ready to store… (+22 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.13
Nodes (19): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview() (+11 more)

### Community 71 - "interviews_feedback_evals.py"
Cohesion: 0.04
Nodes (76): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), notes_fingerprint(), pacer() (+68 more)

### Community 72 - "interviews_transcription_dependencies.py"
Cohesion: 0.11
Nodes (21): Protocol, The speech-to-text contract features code against, separate from the text-only…, Transcriber, RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., UUID, Voice answers: request -> TranscriptionService, text -> TranscriptionOut. The…, TranscriptionController (+13 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "errors.py"
Cohesion: 0.13
Nodes (29): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody, FeedbackInProgressError, FeedbackNotFoundError (+21 more)

### Community 75 - "test_tracing.py"
Cohesion: 0.10
Nodes (10): client(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, _settings(), test_both_keys_build_an_enabled_tracer(), test_close_on_a_disabled_tracer_does_nothing(), test_no_keys_builds_a_disabled_tracer_without_warning() (+2 more)

### Community 76 - "check_feedback"
Cohesion: 0.14
Nodes (11): Band, _band_check(), check_feedback(), FeedbackEvalQuestion, FeedbackEvalTurn, BaseModel, model_validator, Self (+3 more)

### Community 77 - "Implementation Steps"
Cohesion: 0.12
Nodes (14): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Implementation Steps, Phase A: plumbing and progress events, Phase B: streaming the question text, Step 11: `FakeProvider.stream`, Step 14: The event loop stays free, Step 15: Evals (+6 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "run_feedback_case"
Cohesion: 0.19
Nodes (19): feedback_trace_output(), One case through the same pre-check, score call, write call and template…, What came out next to what was wanted: the verdict, the overall against its…, run_feedback_case(), case(), test_a_case_in_its_band_passes_every_check(), test_a_passing_case_has_no_hints(), test_a_provider_error_is_the_cases_error() (+11 more)

### Community 82 - "fake.py"
Cohesion: 0.08
Nodes (39): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, EmbedCall (+31 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+6 more)

### Community 84 - "interviews_log.py"
Cohesion: 0.15
Nodes (14): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+6 more)

### Community 85 - "interviews_context.py"
Cohesion: 0.08
Nodes (38): StrategyOutput, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, build_context_manager(), _counts(), FeedbackScore, FeedbackWrite (+30 more)

### Community 86 - "LLMTimeoutError"
Cohesion: 0.11
Nodes (16): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, LLMTimeoutError, 1. Why it exists (+8 more)

### Community 87 - "traced"
Cohesion: 0.19
Nodes (17): drain(), result(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage(), test_disabled_tracer_is_a_pass_through(), test_failed_call_is_marked_error_and_the_same_exception_is_raised(), test_missing_usage_is_omitted_never_guessed(), test_retried_call_is_one_generation_with_attempts() (+9 more)

### Community 88 - "test_reaction_pick.py"
Cohesion: 0.29
Nodes (12): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick(), parametrize, test_a_one_entry_pool_still_works(), test_every_category_and_level_group_has_a_pool(), test_final_answer_uses_the_closing_pool(), test_never_repeats_the_previous_reaction() (+4 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "FeedbackCaseResult"
Cohesion: 0.23
Nodes (12): criterion_spread(), feedback_scores_for(), FeedbackCaseResult, level_gap_check(), The pair's check, or None when there is nothing to compare: no pair, or either…, Per case: the largest gap between the highest and lowest score any one…, (name, value, comment) per check, plus `valid_reply` and `case_passed`. An…, _verdict() (+4 more)

### Community 93 - "clock"
Cohesion: 0.17
Nodes (7): 9. Still open, Known Issues, _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

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
Cohesion: 0.05
Nodes (51): build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, _model_parameters(), ReasoningEffort (+43 more)

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
Nodes (74): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_reply() (+66 more)

### Community 109 - "FeedbackGenerator"
Cohesion: 0.13
Nodes (17): ScoreResult, _Attempts, CallUsage, FeedbackGenerator, log_feedback_summary(), tokens(), NamedTuple, T (+9 more)

### Community 110 - "main"
Cohesion: 0.16
Nodes (18): html_target(), main(), Path, Session, UUID, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines() (+10 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional (+6 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "InterviewType"
Cohesion: 0.08
Nodes (66): _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, load_object(), _normalized(), parse_interviewer_reply(), parse_streamed_reply() (+58 more)

### Community 115 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.15
Nodes (12): 13. Phase 2 real runs (yours), Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

### Community 116 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

### Community 117 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.13
Nodes (14): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional (+6 more)

### Community 121 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 122 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 123 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.11
Nodes (16): Scheme, credentials, port and every resolved address. Returns the address to…, One hop: a page, or the redirect's Location to check next., Client, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4) (+8 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal, Non-Functional (+6 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.13
Nodes (14): 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse, 7. Fix: the smallest change in the right place (+6 more)

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
Nodes (43): RequestIdFilter, health_check(), CurrentUserDep, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues (+35 more)

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
Cohesion: 0.05
Nodes (36): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+28 more)

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

### Community 140 - "re"
Cohesion: 0.25
Nodes (4): re, parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.22
Nodes (22): KnowledgeChunkScope, One (role, level) a chunk applies to. Rows instead of array columns, so the…, active(), chunks(), corpus(), FailingOn, interview(), ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag… (+14 more)

### Community 143 - "test_context.py"
Cohesion: 0.18
Nodes (14): Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default(), test_a_strategy_without_a_limit_is_never_trimmed() (+6 more)

### Community 144 - "PageParams"
Cohesion: 0.07
Nodes (39): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, answered_main_questions() (+31 more)

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
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

### Community 151 - "interviews_feedback_dependencies.py"
Cohesion: 0.10
Nodes (50): get_db(), Session, get_answer_controller(), get_answer_service(), Depends, Session, get_feedback_controller(), get_feedback_limiter() (+42 more)

### Community 152 - "run_ranking"
Cohesion: 0.19
Nodes (20): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), Acceptance Criteria, Edge Cases, Test Results, arm_of(), fill(), generated() (+12 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.15
Nodes (12): Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.42
Nodes (9): ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1(), test_an_invalid_note_names_the_file_writes_nothing_and_exits_1(), test_it_prints_the_counts_and_exits_0(), test_warnings_are_printed_without_note_text(), test_without_the_google_key_it_says_what_to_set_and_exits_1() (+1 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "test_context_prompts.py"
Cohesion: 0.10
Nodes (30): A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), load_prompt(), Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt() (+22 more)

### Community 160 - "interviews/conftest.py"
Cohesion: 0.06
Nodes (40): BankQuestion, One entry of the hand-written question bank file., Affected Files & Patterns, Step 2: Event contract, answer(), _answer(), anyio_backend(), as_v5_text() (+32 more)

### Community 161 - "Tracer"
Cohesion: 0.05
Nodes (55): AbstractContextManager, build_tracer(), Generation, Any, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, The stream was closed before it finished (client left, or the turn's deadline…, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests… (+47 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "interviews_answer_service.py"
Cohesion: 0.09
Nodes (31): LLMProvider, Protocol, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Random, One answer turn: the checks and reads, the LLM interviewer (or the bank), and…, HistoryPage, InterviewsService (+23 more)

### Community 164 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 165 - "ErrorResponse"
Cohesion: 0.11
Nodes (22): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+14 more)

### Community 166 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Implementation Steps, Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 167 - "require_permissions"
Cohesion: 0.10
Nodes (27): ForbiddenError, get_current_user(), Depends, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), require_roles() (+19 more)

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 169 - "interviews_utils.py"
Cohesion: 0.11
Nodes (30): NotEnoughQuestionsError, MessageKind, MessageRole, StrEnum, Transcript item kinds: a question comes from interview_questions, the other two…, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut, build_transcript() (+22 more)

### Community 170 - "test_select_questions.py"
Cohesion: 0.22
Nodes (19): Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 4. How it works, _bank(), parametrize, _q(), _select(), test_general_question_is_eligible_for_every_role() (+11 more)

### Community 171 - "interviews_feedback.py"
Cohesion: 0.11
Nodes (30): _check_lengths(), Evidence, _has_markup(), _normalized(), parse_write_reply(), BaseModel, NamedTuple, _question_score() (+22 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.15
Nodes (16): Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+8 more)

### Community 174 - "OpenAICompatibleProvider"
Cohesion: 0.13
Nodes (14): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+6 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 178 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 179 - ".record_turn"
Cohesion: 0.09
Nodes (23): ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Save one whole turn in one commit: advance the session, the answer, the…, Architecture & Design, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works (+15 more)

### Community 180 - "JobRole"
Cohesion: 0.07
Nodes (47): JobRole, Level, EvalSetup, FeedbackEvalSetup, One interview's main questions through the streamed writer's text format (the…, simulate_main_questions(), load_bank(), load_rubric() (+39 more)

### Community 181 - "middleware.py"
Cohesion: 0.17
Nodes (8): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send, starlette_types

### Community 182 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 183 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Requirements, User Flow (+1 more)

### Community 184 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (10): Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., Affected Files & Patterns, Blockers & Resolutions, Implementation Deviations (recorded during /implement), Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement (+2 more)

### Community 185 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 186 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 187 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

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
Cohesion: 0.19
Nodes (21): embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, 15 cases with the kinds the label rules require: most expect API design first;…, run() (+13 more)

### Community 220 - "pytest"
Cohesion: 0.09
Nodes (12): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms() (+4 more)

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

### Community 234 - "FeedbackEvalCase"
Cohesion: 0.22
Nodes (10): feedback_dataset_items(), FeedbackEvalCase, load_feedback_cases(), Any, Path, The cases as dataset items: the interview as input, the bands as the expected…, parametrize, test_a_badly_labelled_case_is_rejected() (+2 more)

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

### Community 244 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

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
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository)

### Community 251 - "TranscriptionResult"
Cohesion: 0.15
Nodes (10): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank). (+2 more)

### Community 252 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.20
Nodes (9): Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal, Out of Scope, Problem, User Flow (+1 more)

### Community 253 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Résumé upload and candidate profile (Slice 8c), Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 255 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 256 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 257 - "test_generation_eval.py"
Cohesion: 0.19
Nodes (17): lf(), fixture, quiet(), `run_generation` as Langfuse experiment runs (langfuse-experiments Step 11;…, The console with each arm row's start_ms (wall-clock time) dropped, and without…, A fake LLM: a new, valid main question per call; it can fail every call that…, run(), table_without_timings() (+9 more)

### Community 258 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 259 - "Web"
Cohesion: 0.20
Nodes (5): fixture, Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 260 - "parse_log"
Cohesion: 0.31
Nodes (9): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, lines_of(), Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis(), squash(), test_calls_logged_before_the_task_name_existed_fold_into_other_so_the_rows_add_up() (+1 more)

### Community 261 - "test_login.py"
Cohesion: 0.25
Nodes (4): _login_error(), test_registered_user_is_a_plain_active_user(), test_unknown_email_wrong_password_and_inactive_user_fail_identically(), test_valid_login_returns_bearer_token_for_the_user()

### Community 262 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 263 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

### Community 264 - "ContextManager"
Cohesion: 0.10
Nodes (36): BuiltContext, ContextManager, ContextReport, estimate_tokens(), _log(), Any, NamedTuple, Protocol (+28 more)

### Community 265 - "compute_overall"
Cohesion: 0.47
Nodes (6): compute_overall(), The mean of every criterion score of every main question, rounded half up to…, 6. Try it yourself, score(), test_the_overall_is_the_mean_of_every_criterion_score(), test_the_overall_rounds_half_up_to_one_decimal()

### Community 268 - "FakeLangfuse"
Cohesion: 0.09
Nodes (15): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+7 more)

## Knowledge Gaps
- **832 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+827 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1958 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **40 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `traces`, `LLMServerError`, `test_generation_eval.py`, `interviews_rag_evals.py`, `FakeLangfuse`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `interviews_feedback_dependencies.py`, `run_ranking`, `LLMResult`, `test_feedback_endpoint.py`, `KnowledgeRepository`, `interviews_answer_service.py`, `Completed Steps`, `experiments`, `AnswerService`, `test_evals.py`, `FakeClient`, `test_tracing_routes.py`, `interviews_feedback_service.py`, `interviews_feedback_evals.py`, `test_tracing.py`, `run_feedback_case`, `test_retrieval_eval.py`, `interviews_context.py`, `traced`, `test_factory.py`, `interviews_evals.py`, `FeedbackGenerator`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `Feature: Langfuse experiments for the interviews evals`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `AuthController`, `test_knowledge_postgres.py`, `decode_token`, `tests/conftest.py`, `auth_dependencies.py`, `Role`, `PageParams`, `interviews_feedback_dependencies.py`, `interviews_answer_service.py`, `require_permissions`, `interviews_job_url_service.py`, `AnswerService`, `interviews_model.py`, `test_create_interview.py`, `InterviewQuestion`, `interviews_feedback_service.py`, `interviews_transcription_dependencies.py`, `errors.py`, `Implementation: Langfuse Tracing`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `LLMServerError`, `test_generation_eval.py`, `.stream`, `test_feedback_evals.py`, `test_turn_budget.py`, `test_context_prompts.py`, `Tracer`, `interviews_answer_service.py`, `interviews_utils.py`, `OpenAICompatibleProvider`, `test_evals.py`, `Interviewer`, `test_start_llm.py`, `test_openai_compatible_stream.py`, `interviews_feedback_service.py`, `test_answer_llm.py`, `interviews_feedback_evals.py`, `test_tracing.py`, `Implementation Steps`, `test_job_description_summary.py`, `fake.py`, `interviews_context.py`, `traced`, `test_factory.py`, `interviews_evals.py`, `FeedbackGenerator`, `Feature: Langfuse Tracing`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 47 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Are the 28 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 28 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._