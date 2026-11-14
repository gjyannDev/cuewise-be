# Graph Report - cuewise-be  (2026-11-14)

## Corpus Check
- 418 files · ~361,430 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 5632 nodes · 15796 edges · 295 communities (232 shown, 63 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2978 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1650faf8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- QuestionTurn
- LLMRateLimitError
- Completed Steps
- decode_token
- test_interview_report.py
- auth_service.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- interviews_knowledge_utils.py
- tests/conftest.py
- Tracer
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- done
- test_feedback_evals.py
- test_safe_fetch.py
- User
- test_tracing_lifespan.py
- cuewise-be
- interviews_feedback_turn.py
- LLMServerError
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- select_questions
- interviews_rag_evals.py
- Feature: Context Management for the Interview LLM Calls
- Feature: Layered Modules (route -> controller -> service -> repository)
- Embedder
- ContextManager
- 4. How it works
- Implementation: LLM as the Interviewer (it asks the questions)
- interviews_context.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- interviews_job_url_service.py
- interviews_log.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_evals.py
- test_feedback_contract.py
- test_knowledge_postgres.py
- InterviewerInputs
- profile_route.py
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- Implementation: Résumé-aware interview (Slice 8d)
- test_tracing_routes.py
- test_context_controller.py
- interviews_model.py
- job_description_summary_v2.md
- errors.py
- FakeEmbedder
- interviews_transcription_controller.py
- test_profile_routes.py
- Implementation Plan: Error Handling
- test_answer_llm.py
- interviews_feedback_evals.py
- Feature: Role-Based Access Control (single JWT)
- exception_handlers.py
- RateLimiter
- Langfuse CLI Reference
- Implementation: Résumé upload and candidate profile (Slice 8c)
- parse_profile_reply
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- interviews_evals.py
- provider.py
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_question_bank.py
- get_db
- LLMResult
- EmbeddingKind
- _Stt
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- build_tracer
- clock
- Langfuse Observability
- interviewer_v3.md
- usage_report.py
- Implementation Plan: Context Management for the Interview LLM Calls
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- Settings
- test_get_interview.py
- profile_reply.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- Langfuse
- test_me.py
- main
- Implementation: Eval runs in Langfuse (scores + datasets)
- Feature: Langfuse Tracing
- Langfuse
- QuestionCategory
- Implementation: Langfuse experiments for the interviews evals
- interviews_utils.py
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- Feature: Langfuse experiments for the interviews evals
- types.py
- traces
- test_profile_read_resume.py
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Feature: Résumé upload and candidate profile (Slice 8c)
- How to evaluate an AI feature: from the command to the fix
- Feature: Résumé-aware interview (Slice 8d)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- Implementation: Error Handling
- Implementation: Interview History List (backend)
- Judge Calibration
- profile_resume_utils.py
- build_usage_report
- Slices in detail
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- text
- KnowledgeRepository
- Clock
- follow_up
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- test_follow_ups.py
- get_llm_provider
- ConsoleFormatter
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- profile_evals.py
- interviews_knowledge_ingest.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- scrub_contacts
- interviews_reply.py
- hint_for
- Learn: Streaming and latency (Slice 4, SSE)
- Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)
- Feature: Follow-up Questions (decide / write split)
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- LLMProvider
- interviews/conftest.py
- ProfileLLM
- Feature: Start an Interview (backend)
- test_select_questions.py
- ErrorResponse
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Feature: Interview History List (backend)
- feedback_score_v1.md
- feedback_write_v1.md
- test_reply_contract.py
- 2. Langfuse Documentation
- test_stream_answer.py
- interviews_constants.py
- RequestContextMiddleware
- test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only
- interviews_schema.py
- test_user_ids.py
- Learn: Splitting the interviews dependency wiring
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- users_utils.py
- Implementation: Three New Interview Roles (designer, qa, devops)
- test_retrieval_eval.py
- test_list_users.py
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
- Communication and priorities
- Engineering habits
- Senior judgement
- profile_dependencies.py
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- interviews_service.py
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- AI Engineering Learning Path (Cuewise)
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- interviews_job_url_utils.py
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- Implementation Plan: UUID primary keys
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_generation_eval.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- test_answer_interview.py
- Learn: Résumé upload and the candidate profile (Slice 8c)
- test_tracing.py
- pytest
- BaseModel
- Langfuse Prompt Migration
- Langfuse Prompt Migration
- Web
- FakeLangfuse
- InterviewQuestion
- test_job_description_summary.py
- experiments
- _reset_request_id
- SummaryInputs
- .__init__
- fixture
- get_now
- .insert_feedback
- Clock

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

## Communities (295 total, 63 thin omitted)

### Community 0 - "QuestionTurn"
Cohesion: 0.09
Nodes (40): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the… (+32 more)

### Community 1 - "LLMRateLimitError"
Cohesion: 0.10
Nodes (34): LLMRateLimitError, LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., backoff_seconds(), parse_retry_after(), Random, raise_for_status(), Retry rules shared by every vendor client in `core/ai` (the LLM provider and… (+26 more)

### Community 2 - "Completed Steps"
Cohesion: 0.14
Nodes (26): log_embedding_call(), log_retrieval(), One line per embedding call (ingest or retrieval): metadata only, never the…, Which reference notes an interview got at start: mode, count, scores and the…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip (+18 more)

### Community 3 - "decode_token"
Cohesion: 0.10
Nodes (35): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, Affected Files & Patterns, Blockers & Resolutions (+27 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (52): analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start(), html_for() (+44 more)

### Community 5 - "auth_service.py"
Cohesion: 0.09
Nodes (36): hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), post (+28 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "interviews_knowledge_utils.py"
Cohesion: 0.09
Nodes (44): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, cosine_similarity(), _hash(), _listed() (+36 more)

### Community 9 - "tests/conftest.py"
Cohesion: 0.05
Nodes (55): RequestIdFilter, list_users(), PageDep, CurrentUserDep, Deviations from Plan, Testing Strategy, Affected Files & Patterns, os (+47 more)

### Community 10 - "Tracer"
Cohesion: 0.08
Nodes (17): AbstractContextManager, Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, FakeObservation, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_disabled_tracer_is_a_pass_through() (+9 more)

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
Cohesion: 0.13
Nodes (28): _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored(), test_api_key_never_shows_in_repr_or_errors() (+20 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.19
Nodes (22): listen_body(), make_transcriber(), ok(), parametrize, Response, A pre-recorded /v1/listen response, trimmed to the fields the transcriber reads., Transcriber whose HTTP layer is a scripted list of responses (or exceptions),…, test_a_429_is_retried() (+14 more)

### Community 16 - "done"
Cohesion: 0.13
Nodes (16): done(), Affected Files & Patterns, Step 2: Event contract, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4) (+8 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.07
Nodes (65): compute_overall(), The mean of every criterion score of every main question, rounded half up to…, Who wrote the feedback text: the write call, or the code's template when that…, TextSource, check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_trace_output() (+57 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (41): Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request, Response (+33 more)

### Community 19 - "User"
Cohesion: 0.06
Nodes (82): alias, AnswerControllerDep, ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role (+74 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "interviews_feedback_turn.py"
Cohesion: 0.07
Nodes (49): BuiltContext, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., decide(), UUID, The decide step of an answer turn: the model suggests following up or moving…, At most two attempts within the decide cap; any failure means "next_question"… (+41 more)

### Community 27 - "LLMServerError"
Cohesion: 0.06
Nodes (83): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, LLMServerError, 5xx or a dropped connection: the provider's side failed., One answer turn of the LLM interviewer: decide (follow up or move on), apply…, ActionKnown, Delta (+75 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.13
Nodes (54): InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, 5. What can go wrong, happy(), interview(), post(), parametrize, POST and GET /api/v1/interviews/{id}/feedback: the end-to-end seam for the… (+46 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.19
Nodes (35): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+27 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (18): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+10 more)

### Community 31 - "select_questions"
Cohesion: 0.08
Nodes (24): Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Implementation Steps, Overview (+16 more)

### Community 32 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (88): _arm_notes(), ArmInterview, ArmSummary, build_sheet(), case_set_problems(), competencies_of(), filter_baseline(), generation_item() (+80 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 35 - "Embedder"
Cohesion: 0.11
Nodes (15): Embedder, Protocol, 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e) (+7 more)

### Community 36 - "ContextManager"
Cohesion: 0.05
Nodes (63): ContextManager, ContextReport, estimate_tokens(), _log(), Any, NamedTuple, Protocol, How many oldest entries may be dropped; everything else is required. (+55 more)

### Community 37 - "4. How it works"
Cohesion: 0.07
Nodes (29): _decode(), FetchedPage, FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach… (+21 more)

### Community 38 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.06
Nodes (33): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+25 more)

### Community 39 - "interviews_context.py"
Cohesion: 0.08
Nodes (27): StrategyOutput, build_context_manager(), _counts(), FeedbackScore, FeedbackScoreInputs, FeedbackWrite, FeedbackWriteInputs, FollowUpDecision (+19 more)

### Community 40 - "test_layers.py"
Cohesion: 0.05
Nodes (46): ast, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository) (+38 more)

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
Nodes (33): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, Any network-side failure of a job link. One message for every cause, so…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError (+25 more)

### Community 45 - "interviews_log.py"
Cohesion: 0.15
Nodes (14): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+6 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.11
Nodes (16): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_125_s_or_an_unreported_duration_is_accepted(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415() (+8 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.07
Nodes (102): FakeProvider, load_cases(), main(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, run_case(), 5. What can go wrong (+94 more)

### Community 49 - "test_feedback_contract.py"
Cohesion: 0.06
Nodes (91): assess_evidence(), _check_lengths(), Evidence, FeedbackThread, _has_markup(), _normalized(), parse_score_reply(), parse_write_reply() (+83 more)

### Community 50 - "test_knowledge_postgres.py"
Cohesion: 0.12
Nodes (28): alembic_config, InterviewSessionChunk, KnowledgeChunk, A reference note one interview was given at start: the same notes for every…, pathlib, cuewise-be, Development database (Postgres 18 + pgvector), Reference notes (knowledge-base RAG) (+20 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.12
Nodes (38): InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, apply_limits(), Deadline, _decision_label(), plan_write() (+30 more)

### Community 52 - "profile_route.py"
Cohesion: 0.14
Nodes (16): Limits, thresholds and messages of the résumé upload (resume-upload spec)., delete_profile(), get_profile(), post, ProfileUser, A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes…, The signed-in user's profile; 404 `PROFILE_NOT_FOUND` before the first upload., Remove the signed-in user's profile for good; 204 also when there was none. (+8 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.09
Nodes (32): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+24 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.15
Nodes (36): 5. What can go wrong, fail(), error(), import_url(), _post(), long_posting(), page(), paste() (+28 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.21
Nodes (21): chunk(), drain(), Interrupted, make_provider(), ok(), parametrize, Response, OpenAICompatibleProvider.stream: chat completions with `stream: true`, read as… (+13 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.09
Nodes (55): QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that…, analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table() (+47 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (34): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+26 more)

### Community 59 - "Implementation: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Changes Made, Completed Steps, Current Step, Deviations from Plan, Gate after Step 1: apply the migration, Implementation: Résumé-aware interview (Slice 8d), Known Issues, Links (+7 more)

### Community 61 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 62 - "interviews_model.py"
Cohesion: 0.12
Nodes (25): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, KnowledgeChunkScope (+17 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "errors.py"
Cohesion: 0.06
Nodes (61): Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError (+53 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.12
Nodes (33): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets(), competencies(), corpus(), note_text() (+25 more)

### Community 66 - "interviews_transcription_controller.py"
Cohesion: 0.22
Nodes (9): UUID, Voice answers: request -> TranscriptionService, text -> TranscriptionOut. The…, TranscriptionController, get_transcription_controller(), get_transcription_service(), Depends, Session, POST /interviews/{id}/transcriptions: what the candidate said, for them to… (+1 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (37): 5. What can go wrong, profile_json(), Synthetic résumé data and the scripted model shared by the profile tests (no…, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,… (+29 more)

### Community 68 - "Implementation Plan: Error Handling"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.06
Nodes (38): 2. What it is, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+30 more)

### Community 71 - "interviews_feedback_evals.py"
Cohesion: 0.04
Nodes (92): ExperimentRun, NamedTuple, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), Any (+84 more)

### Community 72 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.19
Nodes (22): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+14 more)

### Community 74 - "RateLimiter"
Cohesion: 0.14
Nodes (18): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, get_resume_limiter(), Tests swap in a fresh limiter so counts never leak between them., math, Clock, test_a_new_window_allows_again() (+10 more)

### Community 75 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues, Links (+7 more)

### Community 77 - "parse_profile_reply"
Cohesion: 0.23
Nodes (19): fit(), parse_profile_reply(), Whitespace tidied, then cut to `max_length` on a word boundary (a single over-…, Tidied, blanks dropped, duplicates merged ignoring case (the first spelling…, _unique(), parametrize, parse_profile_reply: the model's JSON -> a capped, cleaned CandidateProfile, or…, reply() (+11 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+2 more)

### Community 81 - "interviews_evals.py"
Cohesion: 0.06
Nodes (71): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_reply() (+63 more)

### Community 82 - "provider.py"
Cohesion: 0.06
Nodes (45): anyio, Context management: the one place that decides what each LLM call sends. The…, DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over… (+37 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "test_question_bank.py"
Cohesion: 0.13
Nodes (20): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+12 more)

### Community 85 - "get_db"
Cohesion: 0.10
Nodes (23): Page, page_params(), BaseModel, Query, Offset pagination shared by every list endpoint, so clients see one query…, get_db(), Session, UsersController (+15 more)

### Community 86 - "LLMResult"
Cohesion: 0.06
Nodes (46): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport (+38 more)

### Community 87 - "EmbeddingKind"
Cohesion: 0.08
Nodes (37): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, EmbedCall (+29 more)

### Community 88 - "_Stt"
Cohesion: 0.24
Nodes (5): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank)., _Stt

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "build_tracer"
Cohesion: 0.32
Nodes (7): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, Completed Steps, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 93 - "clock"
Cohesion: 0.18
Nodes (6): Known Issues, _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "usage_report.py"
Cohesion: 0.36
Nodes (5): main(), Session, Print stored LLM usage per interview: tokens per question position and per…, test_an_empty_database(), test_reports_stored_questions_grouped_by_interview()

### Community 97 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.18
Nodes (10): Baseline Failures, Commit message suggestion, Implementation: Langfuse Tracing, Known Issues, Links, Skills Consulted During Implementation, Status, Test Cases (+2 more)

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

### Community 103 - "Settings"
Cohesion: 0.12
Nodes (12): ProviderConfig, BaseModel, model_validator, Self, One listed provider, resolved from its vendor block., Settings, BaseSettings, Open Questions (+4 more)

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "profile_reply.py"
Cohesion: 0.09
Nodes (48): EmptyProfileError, BaseModel, Exception, The contract for the profile-extraction reply, and the check that enforces it.…, No skills and no roles: not a résumé we can use (refused as unreadable, nothing…, _RawProfile, _RawProject, _RawRole (+40 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 109 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 110 - "main"
Cohesion: 0.10
Nodes (30): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+22 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.10
Nodes (16): Generation, The stream was closed before it finished (client left, or the turn's deadline…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, Baseline Failures, Changes Made, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues (+8 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "QuestionCategory"
Cohesion: 0.14
Nodes (30): interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), A predefined, neutral acknowledgement for the answer just given; never the same…, parse() (+22 more)

### Community 115 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.14
Nodes (13): 13. Phase 2 real runs (yours), Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 116 - "interviews_utils.py"
Cohesion: 0.09
Nodes (34): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, model_validator, Self, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, audio_container(), _has_signature() (+26 more)

### Community 117 - "The fundamentals"
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

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

### Community 122 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 123 - "test_profile_read_resume.py"
Cohesion: 0.09
Nodes (61): _content(), _escape(), _fill(), Image, make_docx(), make_pdf(), plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build… (+53 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+7 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.13
Nodes (14): 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse, 7. Fix: the smallest change in the right place (+6 more)

### Community 127 - "Feature: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé-aware interview (Slice 8d), Functional, Goal (+8 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "Implementation: Error Handling"
Cohesion: 0.18
Nodes (10): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+2 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "profile_resume_utils.py"
Cohesion: 0.11
Nodes (33): _clean(), _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _has_external_relationship() (+25 more)

### Community 134 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 135 - "Slices in detail"
Cohesion: 0.18
Nodes (11): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 6: Feedback and scoring, Slice 7: Eval maturity (trust the judge, catch regressions) (+3 more)

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

### Community 140 - "text"
Cohesion: 0.13
Nodes (16): text(), Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Job URL (Slice 8b), Functional, Goal (+8 more)

### Community 142 - "KnowledgeRepository"
Cohesion: 0.09
Nodes (40): KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a…, _embed(), ingest_corpus(), IngestCounts (+32 more)

### Community 143 - "Clock"
Cohesion: 0.33
Nodes (3): anyio_backend(), Clock, fixture

### Community 144 - "follow_up"
Cohesion: 0.15
Nodes (14): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+6 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_turn_budget.py"
Cohesion: 0.29
Nodes (10): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds(), test_a_write_retry_is_skipped_below_the_retry_minimum() (+2 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): 5. What can go wrong, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 151 - "get_llm_provider"
Cohesion: 0.12
Nodes (35): get_llm_provider(), get_tracer(), Request, Built once at startup (app lifespan); None when no key is configured or the…, Built once at startup (app lifespan); a disabled tracer when the lifespan…, get_feedback_service(), datetime, Depends (+27 more)

### Community 152 - "ConsoleFormatter"
Cohesion: 0.18
Nodes (14): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), LogRecord, sys, _record(), test_console_appends_the_traceback() (+6 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "profile_evals.py"
Cohesion: 0.06
Nodes (43): pacer(), wait(), Local time, as the Langfuse list shows the run's start: the name and the…, `wait()` sleeps `pause` seconds on every call but the first. Called before each…, run_stamp(), extract_profile(), ExtractionFailedError, Exception (+35 more)

### Community 157 - "interviews_knowledge_ingest.py"
Cohesion: 0.15
Nodes (21): build_embedder(), Embeddings for reference-note retrieval; None without the Google key (notes are…, main(), _parser(), ArgumentParser, Session, Ingest the reference notes into the database (knowledge-base RAG). uv run…, Why the corpus leans too much on drafted notes, or None. A model grounded on a… (+13 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 160 - "interviews_reply.py"
Cohesion: 0.07
Nodes (49): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, _check_question(), HeaderSplit, InterviewerReply (+41 more)

### Community 161 - "hint_for"
Cohesion: 0.04
Nodes (54): Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the… (+46 more)

### Community 162 - "Learn: Streaming and latency (Slice 4, SSE)"
Cohesion: 0.13
Nodes (14): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Streaming and latency (Slice 4, SSE) (+6 more)

### Community 163 - "Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)"
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 8. Check your understanding, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)

### Community 164 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 165 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 166 - "LLMProvider"
Cohesion: 0.04
Nodes (60): LLMProvider, Protocol, QuestionNotCurrentError, get_answer_controller(), get_answer_service(), Depends, Session, Save one whole turn in one commit: advance the session, the answer, the… (+52 more)

### Community 167 - "interviews/conftest.py"
Cohesion: 0.05
Nodes (49): BankQuestion, One entry of the hand-written question bank file., _unique_ids(), Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement (+41 more)

### Community 169 - "Feature: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 170 - "test_select_questions.py"
Cohesion: 0.12
Nodes (33): NotEnoughQuestionsError, pick_fallback_question(), Collection, Random, One unused bank question for `position`, used when the LLM is off or its reply…, random, fixture_bank(), pick() (+25 more)

### Community 171 - "ErrorResponse"
Cohesion: 0.11
Nodes (22): ErrorResponse, Requirements (no spec.md: requirement and edge-case IDs are defined here), Completed Steps, Test Cases, Acceptance Criteria, Blockers, Constraints, Edge Cases (+14 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.33
Nodes (9): Baseline Failures, Testing Strategy, Baseline Failures, Testing Strategy, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits() (+1 more)

### Community 174 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 178 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 179 - "test_stream_answer.py"
Cohesion: 0.25
Nodes (13): 5. What can go wrong, fixture, AnswerController.stream_answer driven directly, for what a test client can't…, A started interview and a controller wired like the app's: returns (controller,…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing() (+5 more)

### Community 180 - "interviews_constants.py"
Cohesion: 0.12
Nodes (39): FollowUpGap, InterviewType, JobRole, Level, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, _Interview, The interview as plain values, read before the claim's commit expires the…, EvalSetup (+31 more)

### Community 181 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 182 - "test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only"
Cohesion: 0.40
Nodes (5): Baseline Failures, Baseline Failures, Baseline Failures, result(), test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only()

### Community 183 - "interviews_schema.py"
Cohesion: 0.08
Nodes (46): FeedbackStatus, MessageKind, MessageRole, StrEnum, QuestionSource, A feedback row's life: `generating` while a request holds it, then `generated`…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Transcript item kinds: a question comes from interview_questions, the other two… (+38 more)

### Community 184 - "test_user_ids.py"
Cohesion: 0.70
Nodes (4): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7()

### Community 186 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 8. Check your understanding, 9. Still open, Learn: Splitting the interviews dependency wiring

### Community 188 - "Platform and DevOps practice"
Cohesion: 0.25
Nodes (7): CI/CD pipelines with safe rollback, Cloud security, backup and recovery, Containers and Kubernetes troubleshooting, Infrastructure as code in practice, Monitoring, alerting and observability, Platform and DevOps practice, Production problems with no obvious cause

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.17
Nodes (23): notes_fingerprint(), A short id for the ingested notes: changes when any note changes, not when the…, embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;… (+15 more)

### Community 220 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

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

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "profile_dependencies.py"
Cohesion: 0.07
Nodes (38): _out(), ProfileController, The signed-in user's résumé profile: request -> ProfileService, stored row ->…, get_profile_clock(), get_profile_controller(), get_profile_now(), get_profile_service(), limit_resume_uploads() (+30 more)

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

### Community 244 - "interviews_service.py"
Cohesion: 0.06
Nodes (56): PageParams, NamedTuple, HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, interview_out(), InterviewsController (+48 more)

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.18
Nodes (10): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slices (+2 more)

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "interviewer_v7.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 249 - "interviewer_v7_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 250 - "interviews_job_url_utils.py"
Cohesion: 0.14
Nodes (16): _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), _plain(), _posting_text(), Turn a fetched job page into plain job-description text (Slice 8b). Pure…, A JSON-LD description is usually HTML, sometimes entity-escaped HTML: unescape,… (+8 more)

### Community 252 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

### Community 253 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 255 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 256 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 257 - "test_generation_eval.py"
Cohesion: 0.15
Nodes (32): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), arm_of(), fill(), generated(), posted(), parametrize, quiet() (+24 more)

### Community 258 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 259 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 261 - "Learn: Résumé upload and the candidate profile (Slice 8c)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Résumé upload and the candidate profile (Slice 8c)

### Community 262 - "test_tracing.py"
Cohesion: 0.11
Nodes (24): client(), drain(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), test_a_redacted_call_records_a_placeholder_instead_of_the_messages(), test_a_redacted_failure_records_no_partial_text() (+16 more)

### Community 263 - "pytest"
Cohesion: 0.11
Nodes (13): pytest, re, parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text(), parametrize (+5 more)

### Community 264 - "BaseModel"
Cohesion: 0.18
Nodes (8): Band, _band_check(), FeedbackEvalQuestion, FeedbackEvalTurn, BaseModel, model_validator, Self, One main question with its follow-ups, as the score call sees a thread.

### Community 265 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 266 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 267 - "Web"
Cohesion: 0.20
Nodes (5): fixture, Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 268 - "FakeLangfuse"
Cohesion: 0.08
Nodes (20): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+12 more)

### Community 269 - "InterviewQuestion"
Cohesion: 0.05
Nodes (55): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, InterviewMessage, InterviewQuestion, InterviewSession, A candidate answer or the interviewer's reaction to one question. The questions…, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository (+47 more)

### Community 271 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 275 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 293 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 295 - "get_now"
Cohesion: 0.11
Nodes (13): get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., get_now(), datetime, Wall-clock time for stored timestamps (the feedback claim and its stale…, _utc_now(), fresh_limiter(), fixture (+5 more)

### Community 299 - "Clock"
Cohesion: 0.33
Nodes (3): anyio_backend(), Clock, fixture

## Knowledge Gaps
- **891 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+886 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2135 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **63 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `test_generation_eval.py`, `Completed Steps`, `test_tracing.py`, `FakeLangfuse`, `test_feedback_evals.py`, `User`, `experiments`, `test_tracing_lifespan.py`, `get_llm_provider`, `interviews_feedback_turn.py`, `LLMServerError`, `profile_evals.py`, `test_feedback_endpoint.py`, `interviews_rag_evals.py`, `hint_for`, `Embedder`, `LLMProvider`, `get_now`, `ProfileLLM`, `test_evals.py`, `test_tracing_routes.py`, `errors.py`, `test_profile_routes.py`, `interviews_feedback_evals.py`, `interviews_evals.py`, `provider.py`, `test_retrieval_eval.py`, `LLMResult`, `build_tracer`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `interviews_service.py`, `Feature: Langfuse experiments for the interviews evals`, `traces`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `decode_token`, `auth_service.py`, `tests/conftest.py`, `InterviewQuestion`, `get_llm_provider`, `LLMServerError`, `hint_for`, `LLMProvider`, `interviews_job_url_service.py`, `test_knowledge_postgres.py`, `test_create_interview.py`, `interviews_schema.py`, `interviews_model.py`, `errors.py`, `interviews_transcription_controller.py`, `get_db`, `profile_dependencies.py`, `interviews_service.py`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `QuestionTurn`, `test_interview_report.py`, `build_usage_report`, `test_list_interviews.py`, `test_turn_budget.py`, `test_follow_ups.py`, `LLMServerError`, `test_feedback_endpoint.py`, `test_answer_stream.py`, `LLMProvider`, `test_feedback_contract.py`, `test_create_interview.py`, `test_start_llm.py`, `interviews_schema.py`, `test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`, `interviews_report.py`, `test_context_controller.py`, `interviews_model.py`, `errors.py`, `test_answer_llm.py`, `LLMResult`, `usage_report.py`, `interviews_service.py`, `interviews_utils.py`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Are the 49 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 49 INFERRED edges - model-reasoned connections that need verification._
- **Are the 40 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 29 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._