# Graph Report - cuewise-be  (2026-11-26)

## Corpus Check
- 507 files · ~470,440 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 9 file(s) not represented in the graph (top: (none) 4, .example 1, .ini 1)

## Summary
- 7182 nodes · 20305 edges · 323 communities (273 shown, 50 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 3870 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dc0ee662`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_langchain_behaviour.py
- LLMServerError
- test_profile_eval_metrics.py
- decode_token
- test_interview_report.py
- auth_service.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- ReferenceNote
- test_summary_evals.py
- WithInterviewData
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- test_feedback_contract.py
- test_feedback_evals.py
- test_safe_fetch.py
- test_knowledge_ingest.py
- test_prompt_registry.py
- cuewise-be
- interviews/conftest.py
- interviews_answer_service.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- setup_logging
- test_tracing.py
- Feature: Context Management for the Interview LLM Calls
- FakeChatModel
- interviews_rag_evals.py
- errors.py
- interviews_session_utils.py
- Feature: LLM as the Interviewer (it asks the questions)
- interviews_knowledge_utils.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- tracing.py
- interviews_job_url_service.py
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_evals.py
- interviews_feedback.py
- get_logger
- test_retry_budget.py
- CandidateProfileRow
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- test_profile_context.py
- test_tracing_routes.py
- uuid
- Rules
- job_description_summary_v2.md
- interviews_summary_evals.py
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- interviews_profile_eval_metrics.py
- test_answer_llm.py
- test_stream_answer.py
- KnowledgeRepository
- exception_handlers.py
- 4. How it works
- test_gateway.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- json
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- interviews_report_render.py
- interviews_evals.py
- profile_resume_files.py
- Embedder
- test_profile_redaction.py
- interviews_controller.py
- RetryPolicy
- LLMError
- RateLimiter
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- Project
- make_synthesizer
- Langfuse Observability
- interviewer_v3.md
- interviews_context.py
- test_select_questions.py
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_speech.py
- QuestionCategory
- audio_container
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- parse_log
- LLMResult
- Implementation: U3a LangChain foundation + first chains
- test_follow_ups.py
- Feature: Langfuse Tracing
- Langfuse
- interviews_constants.py
- Feature: Interview Feedback and Scoring (Slice 6)
- tests/conftest.py
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- Role
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Agentic Workflow v2 (debug, review-feature, gated loop)
- test_profile_read_resume.py
- Completed Steps
- Feature: Résumé upload and candidate profile (Slice 8c)
- How to evaluate an AI feature: from the command to the fix
- Feature: Résumé-aware interview (Slice 8d)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- sqlalchemy
- Implementation: Interview History List (backend)
- Judge Calibration
- profile_resume_utils.py
- interviews_model.py
- Setup complete-behavioral-junior
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- llm
- Implementation Plan: Résumé-aware interview (Slice 8d)
- QuestionTurn
- CandidateProfile
- Langfuse v4 project migration
- Judge Calibration
- test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only
- Langfuse CI/CD
- Prompt Engineering
- test_reply_contract.py
- interviews_start_dependencies.py
- Implementation: Agentic Workflow v2
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- Implementation Steps
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- RequestContextMiddleware
- Implementation Plan: Langfuse Tracing
- Tracer
- test_transcript.py
- Implementation: Résumé-aware interview (Slice 8d)
- Learn: Résumé-aware interview (Slice 8d)
- test_context.py
- TranscriptionResult
- Implementation Steps
- interviews_schema.py
- hint_for
- MessageRole
- test_interviews_reply_attempts.py
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Feature: Interview History List (backend)
- feedback_score_v1.md
- feedback_write_v1.md
- Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- AI Engineering Upgrade Path (Cuewise)
- Feature: Langfuse experiments for the interviews evals
- Implementation: LLM as the Interviewer (it asks the questions)
- test_start_with_profile.py
- StreamEventOut
- Learn: Langfuse experiments for the interviews evals
- FakeSynthesizer
- Learn: Résumé upload and the candidate profile (Slice 8c)
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- ErrorResponse
- main
- Implementation: Three New Interview Roles (designer, qa, devops)
- test_retrieval_eval.py
- LLMRequestError
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
- Deviations from Plan
- Communication and priorities
- Engineering habits
- Senior judgement
- Implementation: U2 — One tenacity retry policy for the AI call layer
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- interviews_route.py
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- Implementation: Langfuse experiments for the interviews evals
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- interviews_job_url_utils.py
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- Data
- test_tracing_lifespan.py
- Feature: U1 structlog (structured JSON logs)
- Feature: Job URL (Slice 8b)
- test_generation_eval.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- test_answer_interview.py
- Implementation: Prompt Registry
- interviews_feedback_controller.py
- FakeLangfuse
- bind_log_context
- Clock
- Clock
- SafeFetcher
- Implementation: Layered Modules (route -> controller -> service -> repository)
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- ResumeRefusal
- ._fits_the_task
- started
- tiny_context
- _reset_request_id
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- Slices in detail
- Learn: Splitting the interviews dependency wiring
- .record_turn
- Langfuse Observability
- interviews_knowledge_ingest.py
- get_current_user
- FakeClient
- Feature: Layered Modules (route -> controller -> service -> repository)
- Langfuse Prompt Migration
- profile_extract_v1.md
- Langfuse Prompt Migration
- test_factory.py
- test_get_interview.py
- InterviewQuestion
- Implementation Steps
- interview-room/README.md
- test_log_context.py
- Implementation Plan: Context Management for the Interview LLM Calls
- experiments
- interviews_feedback_service.py
- U0 baselines
- clock
- run_generation
- test_profile_evals.py
- _Stt
- traces
- RecordingClient
- safe_fetch.py
- Langfuse
- Learn: Layered architecture (route -> controller -> service -> repository)
- test_me.py
- User
- U2 (tenacity) vs. the U0 baseline
- Langfuse CLI Reference
- 2. Langfuse Documentation

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 152 edges
2. `User` - 131 edges
3. `LLMResult` - 123 edges
4. `FakeProvider` - 122 edges
5. `LLMServerError` - 119 edges
6. `JobRole` - 118 edges
7. `LLMError` - 114 edges
8. `Level` - 103 edges
9. `InterviewType` - 99 edges
10. `InterviewQuestion` - 97 edges

## Surprising Connections (you probably didn't know these)
- `Completed Steps` --references--> `to_llm_error()`  [INFERRED]
  docs/features/u3a-langchain-foundation/task.md → app/core/ai/chat_errors.py
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `1. Why it exists` --references--> `DeepgramTranscriber`  [INFERRED]
  docs/features/interview-room/learnings.md → app/core/ai/deepgram.py
- `6. Try it yourself` --references--> `get_tracer()`  [INFERRED]
  docs/features/split-interviews-dependencies/learnings.md → app/core/ai/dependencies.py

## Import Cycles
- None detected.

## Communities (323 total, 50 thin omitted)

### Community 0 - "test_langchain_behaviour.py"
Cohesion: 0.09
Nodes (41): ChatGenerationChunk, ChatGoogleGenerativeAI, Spike results (step 1, `tests/core/ai/test_langchain_behaviour.py`), GenerateContentResponse, google_ai_generativelanguage_v1beta_types, MonkeyPatch, _Flaky, _gemini() (+33 more)

### Community 1 - "LLMServerError"
Cohesion: 0.08
Nodes (64): anyio_lowlevel, _int_or_none(), Any, Response, One streamed request, ending by `end` on the clock: its text chunks, then an…, The token counts an OpenAI-compatible usage object reports; None for any it…, _usage(), LLMRateLimitError (+56 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.10
Nodes (30): coverage_spread(), guard_verdict(), GuardStatus, notes_overlap(), presumption_hits(), profile_mentions(), profile_only_items(), Collection (+22 more)

### Community 3 - "decode_token"
Cohesion: 0.09
Nodes (38): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Implementation Steps (+30 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.12
Nodes (56): analysis(), answer(), emit_answer_turn(), emit_follow_up_turn(), emit_start(), html_for(), lines_of(), parametrize (+48 more)

### Community 5 - "auth_service.py"
Cohesion: 0.11
Nodes (30): InvalidCredentialsError, hash_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), post (+22 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.12
Nodes (39): extract_job_text(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, At most `limit` characters, cut at the last whitespace so no word is split;…, truncate_on_word(), jsonld() (+31 more)

### Community 8 - "ReferenceNote"
Cohesion: 0.11
Nodes (31): Why an interview has no reference notes at all (logged as…, RetrievalSkip, The notes stored for this interview at start, rank order; none for interviews…, _log_level(), NamedTuple, UUID, `profile_query` is the candidate profile's short items (only for an interview…, The top-k eligible notes for one query vector that clear the threshold, most… (+23 more)

### Community 9 - "test_summary_evals.py"
Cohesion: 0.14
Nodes (26): check_summary(), _has_fact(), ChatModel, The app's own summary call (`summarize_job_description`, as `InterviewsService`…, run_summary_case(), case(), checks_by_name(), good_summary_for_every_case() (+18 more)

### Community 10 - "WithInterviewData"
Cohesion: 0.05
Nodes (46): build_context_manager(), FullHistory, JobDescriptionSummary, A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, SummaryInputs, WithInterviewData (+38 more)

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
Nodes (41): _google(), no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, parametrize, Settings built from a clean environment, so a developer's real key never leaks… (+33 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.19
Nodes (22): listen_body(), make_transcriber(), ok(), A pre-recorded /v1/listen response, trimmed to the fields the transcriber reads., Transcriber whose HTTP layer is a scripted list of responses (or exceptions),…, test_a_429_is_retried(), test_a_503_is_retried_after_backoff_then_succeeds(), test_a_dropped_connection_is_a_server_error() (+14 more)

### Community 16 - "test_feedback_contract.py"
Cohesion: 0.13
Nodes (39): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 1. Why it exists, 2. What it is (+31 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.05
Nodes (88): Band, _band_check(), check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for(), feedback_run_scores(), feedback_scores_for() (+80 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (42): FetchedPage, Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request (+34 more)

### Community 19 - "test_knowledge_ingest.py"
Cohesion: 0.20
Nodes (25): ingest_corpus(), IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, NoteChunk, active(), chunks(), corpus() (+17 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.14
Nodes (25): PromptVersion, Every interviews prompt version, and which one each LLM call sends. Data only:…, Status, 5. What can go wrong, archived_routes(), catalog_mismatches(), incomplete_entries(), Collection (+17 more)

### Community 26 - "interviews/conftest.py"
Cohesion: 0.08
Nodes (30): get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them., answer(), _answer(), anyio_backend(), _bank_question(), make_bank_question(), parse_sse() (+22 more)

### Community 27 - "interviews_answer_service.py"
Cohesion: 0.08
Nodes (45): log_stream_summary(), How a streamed turn felt and ended: time to the first event and to the first…, Delta, PhaseChanged, The next chunk of the question being written (shown as it arrives)., answer_out(), AnswerController, _frame() (+37 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.11
Nodes (60): InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 5. What can go wrong, fresh_limiter(), happy(), interview(), owner() (+52 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.16
Nodes (38): 5. What can go wrong, decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+30 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (18): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+10 more)

### Community 31 - "setup_logging"
Cohesion: 0.09
Nodes (21): _formatter(), _json(), _json_renderer(), Path, Writes to whatever `sys.stderr` is at the time of the write (test runners and…, Routes every logger through the processor chain. Safe to call again (tests do):…, setup_logging(), _StderrHandler (+13 more)

### Community 32 - "test_tracing.py"
Cohesion: 0.08
Nodes (33): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, client(), drain(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result() (+25 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "FakeChatModel"
Cohesion: 0.04
Nodes (93): fake_reply(), FakeChatModel, AIMessage, Any, BaseChatModel, BaseMessage, BaseModel, ChatResult (+85 more)

### Community 35 - "interviews_rag_evals.py"
Cohesion: 0.04
Nodes (83): Local time, as the Langfuse list shows the run's start: the name and the…, run_stamp(), _arm_notes(), ArmSummary, build_sheet(), case_set_problems(), ExtraSetup, filter_baseline() (+75 more)

### Community 36 - "errors.py"
Cohesion: 0.07
Nodes (54): Protocol, `text` spoken in the configured voice, as one whole clip., SpeechSynthesizer, Protocol, Transcriber, AppError, AudioTooLargeError, AudioTooLongError (+46 more)

### Community 37 - "interviews_session_utils.py"
Cohesion: 0.11
Nodes (26): ProfileRequiredError, An interview asked to use the candidate's profile, and there is none to use…, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, InterviewCreateIn, SessionOut, HistoryPage, InterviewState (+18 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "interviews_knowledge_utils.py"
Cohesion: 0.08
Nodes (49): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+41 more)

### Community 40 - "test_layers.py"
Cohesion: 0.12
Nodes (30): ast, Skills Consulted During Implementation, 5. What can go wrong, Known Issues, check_core(), check_layers(), _imports(), _is_llm_library() (+22 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "tracing.py"
Cohesion: 0.07
Nodes (46): complete_chat(), complete_structured(), A LangChain chat model for tests (spec FR6): scripted replies or errors, every…, _finish_reason(), AIMessage, Any, ChatModel, NamedTuple (+38 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.20
Nodes (20): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, Any network-side failure of a job link. One message for every cause, so…, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError (+12 more)

### Community 45 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview (+6 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.07
Nodes (101): FakeProvider, load_cases(), main(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, run_case(), Deviations from Plan (+93 more)

### Community 49 - "interviews_feedback.py"
Cohesion: 0.07
Nodes (56): Task, FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, _check_lengths(), Evidence, FeedbackThread, _has_markup(), _normalized() (+48 more)

### Community 50 - "get_logger"
Cohesion: 0.08
Nodes (31): get_logger(), Logger, 5. What can go wrong, fastapi_responses, parametrize, The logging pipeline (U1 structlog): what actually lands in the log file and on…, test_a_key_that_only_contains_a_sensitive_word_is_kept(), test_a_logged_exception_is_one_line_with_the_traceback() (+23 more)

### Community 51 - "test_retry_budget.py"
Cohesion: 0.13
Nodes (17): anyio_backend(), Clock, counting(), handler(), malformed_reply(), anyio, fixture, parametrize (+9 more)

### Community 52 - "CandidateProfileRow"
Cohesion: 0.17
Nodes (12): CandidateProfileRow, A user's résumé profile: at most one per user (the unique user_id is the…, ProfileRepository, datetime, Session, UUID, End the read transaction before the slow model call, so no connection sits idle…, The user's one profile, inserted or replaced in one commit. Select-then-write… (+4 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.14
Nodes (23): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_database_rejects_two_in_progress_sessions_for_one_user(), session_for() (+15 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.14
Nodes (38): 5. What can go wrong, fail(), error(), import_url(), _post(), long_posting(), page(), paste() (+30 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.11
Nodes (34): Review, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok() (+26 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.06
Nodes (74): QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that…, Call, group_requests(), _int(), _json_event(), LogEvent, NamedTuple (+66 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.16
Nodes (28): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_retry_after_longer_than_the_budget_fails_at_once_without_waiting(), test_cached_and_reasoning_tokens_are_none_when_not_reported(), test_cached_and_reasoning_tokens_are_read_when_reported() (+20 more)

### Community 59 - "test_profile_context.py"
Cohesion: 0.08
Nodes (62): estimate_tokens(), WindowLedger, parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid… (+54 more)

### Community 61 - "uuid"
Cohesion: 0.28
Nodes (11): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+3 more)

### Community 62 - "Rules"
Cohesion: 0.09
Nodes (20): caveman, Example output, How to invoke, See also, What it does, 1. Answer first, 2. Kill ceremony, 3. Short word (+12 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "interviews_summary_evals.py"
Cohesion: 0.18
Nodes (21): Check, _dataset_items(), load_summary_cases(), _print_case(), _print_summary(), Any, BaseModel, Namespace (+13 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.10
Nodes (47): EmbedCall, FakeEmbedder, NamedTuple, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, test_fake_embedder_honors_scripted_vectors_and_errors(), test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets() (+39 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.18
Nodes (29): The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, collect(), follow_up_json(), inputs(), kinds() (+21 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (35): 5. What can go wrong, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,…, Swagger UI builds its request from the OpenAPI schema. Declared as a url-…, stored() (+27 more)

### Community 68 - "interviews_profile_eval_metrics.py"
Cohesion: 0.21
Nodes (18): ArmProfileSummary, GuardVerdict, _injection_share(), _mention_share(), profile_summary(), ProfileRow, NamedTuple, Pure metrics of the résumé-aware generation eval (resume-aware-interview, arms… (+10 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.10
Nodes (24): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., failing_commit(), messages() (+16 more)

### Community 71 - "test_stream_answer.py"
Cohesion: 0.17
Nodes (17): 5. What can go wrong, 6. Try it yourself, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing() (+9 more)

### Community 72 - "KnowledgeRepository"
Cohesion: 0.06
Nodes (34): KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a…, parse_arms(), `--arms`: comma-separated arm letters (any case), at least two (a ranking…, Slices in detail (+26 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.17
Nodes (24): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, BaseException, Exception (+16 more)

### Community 74 - "4. How it works"
Cohesion: 0.18
Nodes (12): _default_request_id(), _merge_request_fields(), Any, Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything…, Dev console: time, level, short request id, logger, event, then one aligned…, ReadableRenderer, redact_sensitive(), _redacted() (+4 more)

### Community 75 - "test_gateway.py"
Cohesion: 0.16
Nodes (26): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, anyio_backend(), _Broken, code_of(), fixture, parametrize, The speech gateway: the generic half of every speech call (checks, vendor… (+18 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues (+8 more)

### Community 77 - "json"
Cohesion: 0.12
Nodes (31): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, parse_profile_reply(), A JSON-text reply, checked against `RawProfile`, then `clean_profile`. The live…, 5. What can go wrong, Test Results, Module Structure & Layer Rules (+23 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "interviews_report_render.py"
Cohesion: 0.15
Nodes (25): _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card(), _html_metric_row(), _html_table() (+17 more)

### Community 81 - "interviews_evals.py"
Cohesion: 0.06
Nodes (72): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_reply() (+64 more)

### Community 82 - "profile_resume_files.py"
Cohesion: 0.12
Nodes (29): _content(), _escape(), _fill(), Image, make_pdf(), plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build…, A PDF with one page per list. `encrypt` adds a standard security handler whose… (+21 more)

### Community 83 - "Embedder"
Cohesion: 0.08
Nodes (22): Embedder, Protocol, 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e) (+14 more)

### Community 84 - "test_profile_redaction.py"
Cohesion: 0.32
Nodes (14): assert_redacted(), assert_traced_in_full(), generations(), inputs(), anyio, resume-aware-interview Step 5: a write whose prompt carries the profile is…, run_stream_write(), run_write() (+6 more)

### Community 85 - "interviews_controller.py"
Cohesion: 0.09
Nodes (30): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewsController (+22 more)

### Community 86 - "RetryPolicy"
Cohesion: 0.03
Nodes (73): AsyncBaseTransport, BaseTransport, AsyncBaseTransport, BaseTransport, _Call, _OutOfTime, Logger, T (+65 more)

### Community 87 - "LLMError"
Cohesion: 0.04
Nodes (89): anyio, Deepgram over plain httpx: pre-recorded speech-to-text (`POST /v1/listen`, Nova…, EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat… (+81 more)

### Community 88 - "RateLimiter"
Cohesion: 0.06
Nodes (44): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, Per-user caps on paid speech calls. One limiter instance per process: every…, get_speech_limiter(), Tests swap in a fresh limiter so counts never leak between them., _out(), ProfileController (+36 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "Project"
Cohesion: 0.24
Nodes (19): candidate_profile_block(), profile_query_text(), The profile fenced as data, like the job description. Summaries and…, The profile's short items as one retrieval query. None: nothing to embed., Project, Testing Strategy, _profile(), resume-aware-interview Step 2 (seam S1): the profile as prompt text and as… (+11 more)

### Community 93 - "make_synthesizer"
Cohesion: 0.17
Nodes (16): audio(), make_synthesizer(), _make(), _make(), handler(), parametrize, Response, Synthesizer whose HTTP layer is a scripted list of responses (or exceptions),… (+8 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "interviews_context.py"
Cohesion: 0.05
Nodes (99): BuiltContext, ContextManager, ContextReport, ContextTooLargeError, _log(), Exception, NamedTuple, Context management: the one place that decides what each LLM call sends. The… (+91 more)

### Community 97 - "test_select_questions.py"
Cohesion: 0.11
Nodes (29): Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Slice 10: Provider fallback chain, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself (+21 more)

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

### Community 103 - "test_speech.py"
Cohesion: 0.11
Nodes (22): 5. What can go wrong, answered(), assert_hidden(), code(), fixture, GET /interviews/{id}/questions/{qid}/speech and /messages/{mid}/speech: the…, An owner with a started backend interview: (owner, session_id, first question)., The first question answered: (owner, session_id, q1, the reaction, q2). (+14 more)

### Community 104 - "QuestionCategory"
Cohesion: 0.07
Nodes (58): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, _check_question(), HeaderSplit, InterviewerReply (+50 more)

### Community 105 - "audio_container"
Cohesion: 0.25
Nodes (14): audio_container(), AudioContainer, _has_signature(), StrEnum, Audio rules every speech feature shares: which recording containers are…, Recording containers an upload may arrive in (what browsers' MediaRecorder…, The container of an uploaded recording, or None when its declared type isn't…, enum (+6 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "parse_log"
Cohesion: 0.06
Nodes (35): parse_log(), Old text lines: `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]).…, Reads both log formats, so a log that rotated mid-change (`app.log.1` text,…, _split_fields(), Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: U1 structlog (structured JSON logs) (+27 more)

### Community 109 - "LLMResult"
Cohesion: 0.04
Nodes (53): _chat_messages(), ChatTrace, Any, BaseMessage, One traced call: started by the first model run it sees, finished by the call…, LangChain messages in our own shape, so the trace reads like the old layer's…, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError… (+45 more)

### Community 110 - "Implementation: U3a LangChain foundation + first chains"
Cohesion: 0.13
Nodes (14): 9 -> 10. Stop: user-run comparison evals, Completed Steps, Current Step, Debug Log, Implementation: U3a LangChain foundation + first chains, Known Issues, Links, Open Questions (+6 more)

### Community 111 - "test_follow_ups.py"
Cohesion: 0.27
Nodes (16): answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries(), test_a_failed_follow_up_write_falls_back_to_the_next_main_bank_question() (+8 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "interviews_constants.py"
Cohesion: 0.04
Nodes (116): InterviewType, JobRole, Level, MessageKind, StrEnum, Transcript item kinds: a question comes from interview_questions, the other two…, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric (+108 more)

### Community 115 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional (+5 more)

### Community 116 - "tests/conftest.py"
Cohesion: 0.04
Nodes (58): health_check(), list_users(), PageDep, CurrentUserDep, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling (+50 more)

### Community 117 - "The fundamentals"
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Role"
Cohesion: 0.08
Nodes (30): permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry(), test_unknown_role_has_no_permissions_and_is_logged(), test_user_can_only_read_self() (+22 more)

### Community 121 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "test_profile_read_resume.py"
Cohesion: 0.15
Nodes (36): make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), _clean(), NamedTuple, _read_docx(), _read_pdf(), read_resume() (+28 more)

### Community 124 - "Completed Steps"
Cohesion: 0.10
Nodes (18): EligibleChunk, NamedTuple, The k eligible chunks embedded with `model` that are most similar to the query,…, IngestCounts, NamedTuple, 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made (+10 more)

### Community 125 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+7 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.10
Nodes (24): injection_ignored(), profile_only_mention_share(), _profile_scores(), One interview's résumé metrics, for its Langfuse result; the same for every…, 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run (+16 more)

### Community 127 - "Feature: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Decisions, Edge Cases, Feature: Résumé-aware interview (Slice 8d), Functional, Goal, Known limits (+7 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "sqlalchemy"
Cohesion: 0.04
Nodes (47): alembic_config, downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list… (+39 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "profile_resume_utils.py"
Cohesion: 0.13
Nodes (28): _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _has_external_relationship(), _hex_lightness() (+20 more)

### Community 134 - "interviews_model.py"
Cohesion: 0.11
Nodes (24): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, Print the cost, effectiveness and efficiency of the interviewer. Numbers and… (+16 more)

### Community 135 - "Setup complete-behavioral-junior"
Cohesion: 0.08
Nodes (25): Blind ranking, Setup complete-behavioral-junior, Setup long-job-description-frontend-junior, Setup near-empty-data-intern, Setup profile-injection-backend-mid, V, V, V (+17 more)

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

### Community 140 - "llm"
Cohesion: 0.15
Nodes (12): as_v5_text(), _decision_json(), llm(), script(), script_decide(), script_score(), script_summary(), script_write() (+4 more)

### Community 142 - "Implementation Plan: Résumé-aware interview (Slice 8d)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Blockers & Resolutions, Decisions (grill-me, 2026-11-14), Deviations during implementation (2026-11-14, see task.md), Implementation Plan: Résumé-aware interview (Slice 8d), Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 143 - "QuestionTurn"
Cohesion: 0.04
Nodes (66): StrategyOutput, _counts(), FeedbackWrite, FollowUpDecision, An earlier question as the model would have written it. A follow-up was written…, The decide call: the current thread in full (it judges the latest answer within…, App data at the end of the last user message; untrusted parts (questions,…, The write call: scores, evidence and question texts only; small whatever the… (+58 more)

### Community 144 - "CandidateProfile"
Cohesion: 0.04
Nodes (114): ProfileExtractionFailedError, ProfileNotFoundError, ProfileUnavailableError, Over the byte, page or unzipped-size limit of a résumé upload., Not a PDF or a Word document by its content (the file name is never trusted)., Encrypted, corrupt, scanned, too little text, or no usable profile in it., The model gave no valid profile after the retry, timed out, or the provider…, ResumeTooLargeError (+106 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only"
Cohesion: 0.17
Nodes (19): Baseline Failures, Baseline Failures, Testing Strategy, Baseline Failures, Testing Strategy, Baseline Failures, budget(), llm_lines() (+11 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_reply_contract.py"
Cohesion: 0.08
Nodes (42): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split), Blockers (+34 more)

### Community 151 - "interviews_start_dependencies.py"
Cohesion: 0.07
Nodes (61): get_chat_model(), get_llm_provider(), get_synthesizer(), get_tracer(), get_transcriber(), ChatModel, Request, Request dependencies for the AI services every feature shares, built once at… (+53 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.12
Nodes (30): embedding_text(), What a chunk is embedded as: its heading, then its text. The heading names the…, corpus(), embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,… (+22 more)

### Community 156 - "Implementation Steps"
Cohesion: 0.13
Nodes (16): NotEnoughQuestionsError, interview_out(), UUID, InterviewOut, TranscriptOut, Implementation Steps, Architecture & Design, Blockers & Resolutions (+8 more)

### Community 157 - "Implementation: Interview Room (backend)"
Cohesion: 0.07
Nodes (27): ProviderConfig, BaseModel, Every speech setting in one read-only group, so the speech factories depend on…, One listed provider, resolved from its vendor block., Speech-to-text (voice answers)., Text-to-speech (the interviewer's voice)., The speech vendor's settings, grouped (see `Settings.speech`). One key and base…, _SpeechPart (+19 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 160 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 161 - "Tracer"
Cohesion: 0.04
Nodes (67): AbstractContextManager, TraceLabels, build_tracer(), Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable… (+59 more)

### Community 162 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 163 - "Implementation: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gate: Step 10, real-model runs (yours), Implementation: Résumé-aware interview (Slice 8d), Known Issues (+8 more)

### Community 164 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.13
Nodes (14): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+6 more)

### Community 165 - "test_context.py"
Cohesion: 0.16
Nodes (16): Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default(), test_a_second_task_with_its_own_strategy_leaves_the_first_alone() (+8 more)

### Community 166 - "TranscriptionResult"
Cohesion: 0.22
Nodes (6): BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, test_a_transcription_fills_every_result_field(), test_125_s_or_an_unreported_duration_is_accepted()

### Community 167 - "Implementation Steps"
Cohesion: 0.14
Nodes (13): Affected Files & Patterns, Implementation Steps, Phase A: plumbing and progress events, Phase B: streaming the question text, Step 11: `FakeProvider.stream`, Step 13: The streamed write step in `stream_turn`, Step 14: The event loop stays free, Step 15: Evals (+5 more)

### Community 168 - "interviews_schema.py"
Cohesion: 0.11
Nodes (23): JobUrlController, Job posting links and pasted pages: request -> JobUrlService, job text ->…, JobTextIn, JobUrlIn, JobUrlOut, BaseModel, model_validator, Self (+15 more)

### Community 169 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 170 - "MessageRole"
Cohesion: 0.31
Nodes (9): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, MessageRole, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut, build_transcript(), The chat as the user saw it: each question, then its answer and reaction when…, Affected Files & Patterns (+1 more)

### Community 171 - "test_interviews_reply_attempts.py"
Cohesion: 0.21
Nodes (11): asyncio, clock_of(), parametrize, The attempt header the four reply loops share (decide, write, write stream,…, `time_left` returning each value in turn., test_a_cancellation_in_the_loop_body_is_not_swallowed(), test_a_retry_with_less_than_the_minimum_time_left_does_not_start(), test_each_attempt_receives_the_time_left_when_it_starts() (+3 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.14
Nodes (17): Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+9 more)

### Community 174 - "Feature: Interview History List (backend)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+6 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)

### Community 178 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 179 - "AI Engineering Upgrade Path (Cuewise)"
Cohesion: 0.33
Nodes (5): AI Engineering Upgrade Path (Cuewise), Build order, How to make it stick, Progress, The rules for this path

### Community 180 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.17
Nodes (11): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Goal, Out of Scope, Problem (+3 more)

### Community 181 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 182 - "test_start_with_profile.py"
Cohesion: 0.12
Nodes (30): 5. What can go wrong, opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent() (+22 more)

### Community 183 - "StreamEventOut"
Cohesion: 0.10
Nodes (25): current_request_id(), The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, _error_event(), _event(), BaseModel, NamedTuple, One event of a streamed turn as the controller yields it; the route encodes it… (+17 more)

### Community 184 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 185 - "FakeSynthesizer"
Cohesion: 0.22
Nodes (6): FakeSynthesizer, Scripted clips (bytes, a full result, or an error), one per call; records each…, Affected Files & Patterns, The text-to-speech seam of a test: a scripted synthesizer and a fresh per-test…, No synthesizer configured (DEEPGRAM_API_KEY blank)., _Tts

### Community 186 - "Learn: Résumé upload and the candidate profile (Slice 8c)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Résumé upload and the candidate profile (Slice 8c)

### Community 187 - "interviewer_v8.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 188 - "Platform and DevOps practice"
Cohesion: 0.25
Nodes (7): CI/CD pipelines with safe rollback, Cloud security, backup and recovery, Containers and Kubernetes troubleshooting, Infrastructure as code in practice, Monitoring, alerting and observability, Platform and DevOps practice, Production problems with no obvious cause

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 191 - "interviewer_v8_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 193 - "ErrorResponse"
Cohesion: 0.04
Nodes (56): open_stream(), ErrorResponse, BaseModel, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview (+48 more)

### Community 203 - "main"
Cohesion: 0.16
Nodes (18): html_target(), main(), Path, Session, UUID, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines() (+10 more)

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.17
Nodes (23): corpus(), embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, Ingests the three notes; returns the vector each note text gets (the embedder… (+15 more)

### Community 220 - "LLMRequestError"
Cohesion: 0.06
Nodes (49): _from_status(), _google_error(), _mapped(), BaseException, Map what the LangChain/Gemini call layer raises to our LLMError types (spec…, The LLMError for `exc`, with `exc` as its cause. Messages are fixed text: a…, Seconds from the error's `google.rpc.RetryInfo` detail (Google's Retry-After);…, _retry_after() (+41 more)

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

### Community 234 - "Deviations from Plan"
Cohesion: 0.53
Nodes (6): Deviations from Plan, busy(), Response, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_retries_stop_when_the_total_budget_would_be_exceeded()

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "Implementation: U2 — One tenacity retry policy for the AI call layer"
Cohesion: 0.13
Nodes (14): 15. Evals, fault check and graph, Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U2 — One tenacity retry policy for the AI call layer, Known Issues, Links (+6 more)

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

### Community 244 - "interviews_route.py"
Cohesion: 0.08
Nodes (57): alias, AnswerControllerDep, RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., Permission, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), limit_feedback() (+49 more)

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.13
Nodes (14): 13. Phase 2 real runs (yours), Baseline Failures, Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions (+6 more)

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
Cohesion: 0.08
Nodes (31): is_public_address(), True only for a globally routable unicast address., _job_url(), Shape only: http(s), a host, a valid port, no credentials. Whether the address…, _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text() (+23 more)

### Community 251 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 252 - "Data"
Cohesion: 0.13
Nodes (22): Data, StrEnum, What an interviewer write carries beyond the job description; it picks the…, check_prompts(), PromptCheckError, Exception, One or more routed prompts cannot be sent; the message lists each one., Raises PromptCheckError naming every routed version whose file is missing or… (+14 more)

### Community 253 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 255 - "Feature: U1 structlog (structured JSON logs)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: U1 structlog (structured JSON logs), Functional, Goal, Non-Functional (+6 more)

### Community 256 - "Feature: Job URL (Slice 8b)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Job URL (Slice 8b), Functional, Goal, Non-Functional (+7 more)

### Community 257 - "test_generation_eval.py"
Cohesion: 0.15
Nodes (32): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), arm_of(), fill(), generated(), posted(), parametrize, quiet() (+24 more)

### Community 258 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 259 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 260 - "Implementation: Prompt Registry"
Cohesion: 0.13
Nodes (14): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Links (+6 more)

### Community 261 - "interviews_feedback_controller.py"
Cohesion: 0.19
Nodes (14): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or… (+6 more)

### Community 262 - "FakeLangfuse"
Cohesion: 0.07
Nodes (25): 5. What can go wrong, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Eval log (AI features only) (+17 more)

### Community 263 - "bind_log_context"
Cohesion: 0.14
Nodes (28): bind_log_context(), Adds fields to every later log line of the current request (or, outside a…, log_retrieval(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, Which reference notes an interview got at start: mode, count, scores, how many…, render_text(), Implementation Steps (+20 more)

### Community 264 - "Clock"
Cohesion: 0.33
Nodes (3): anyio_backend(), Clock, fixture

### Community 265 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 266 - "SafeFetcher"
Cohesion: 0.09
Nodes (18): Response, Scheme, credentials, port and every resolved address. Returns the address to…, One hop: a page, or the redirect's Location to check next., SafeFetcher, get_job_url_controller(), get_job_url_service(), get_page_fetcher(), Depends (+10 more)

### Community 267 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.08
Nodes (21): Blockers & Resolutions, Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+13 more)

### Community 268 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 269 - "ResumeRefusal"
Cohesion: 0.50
Nodes (3): Exception, Why a file was refused; `reason` is short and machine-readable (logged, never…, ResumeRefusal

### Community 271 - "started"
Cohesion: 0.67
Nodes (3): fixture, An owner with a started 3-question interview: (owner, session_id, first…, started()

### Community 274 - "Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 275 - "Implementation Plan: Agentic Workflow v2"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: Agentic Workflow v2, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 276 - "Slices in detail"
Cohesion: 0.08
Nodes (23): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety (+15 more)

### Community 277 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

### Community 290 - ".record_turn"
Cohesion: 0.06
Nodes (44): QuestionNotCurrentError, ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Save one whole turn in one commit: advance the session, the answer, the…, AnswerOut, Turn the outcome into rows and save the whole turn in one commit. `reaction` is…, done(), Progress (+36 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 293 - "interviews_knowledge_ingest.py"
Cohesion: 0.11
Nodes (26): load_prompt(), Path, Prompt files: versioned Markdown read once per process. Feature modules pass…, `<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in…, main(), _parser(), ArgumentParser, Session (+18 more)

### Community 294 - "get_current_user"
Cohesion: 0.09
Nodes (25): ForbiddenError, get_current_user(), get_service(), Depends, Session, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, check(), require_roles() (+17 more)

### Community 295 - "FakeClient"
Cohesion: 0.09
Nodes (19): The LangChain tracing callback (spec FR5, AC8, EC14, EC15): one Langfuse…, result(), test_a_call_records_one_generation_with_its_messages_labels_and_usage(), test_a_disabled_tracer_records_nothing(), test_a_failed_call_records_an_error_with_the_error_class(), test_a_langfuse_failure_never_fails_the_call(), test_a_redacted_call_records_the_placeholder_for_input_and_output(), test_retried_attempts_are_still_one_generation_with_the_attempt_count() (+11 more)

### Community 296 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions (+3 more)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "profile_extract_v1.md"
Cohesion: 0.40
Nodes (4): Constraints, Input, Role, Task

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 301 - "test_factory.py"
Cohesion: 0.03
Nodes (88): _DeepgramAdapter, DeepgramSynthesizer, attempt(), DeepgramTranscriber, attempt(), _parse(), Any, Response (+80 more)

### Community 303 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 305 - "InterviewQuestion"
Cohesion: 0.05
Nodes (59): HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, InterviewMessage, InterviewQuestion, InterviewSession, A candidate answer or the interviewer's reaction to one question. The questions… (+51 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 311 - "test_log_context.py"
Cohesion: 0.29
Nodes (9): fixture, Log context on real interview requests (U1 structlog, AC4): `session` and…, Every line of the one request whose access line ends with `path_end`., _request_lines(), started(), test_a_request_for_someone_elses_interview_logs_the_id_it_asked_for(), test_a_start_request_logs_the_new_session_and_the_user_on_every_line(), test_a_streamed_turn_logs_its_session_and_user_from_inside_the_stream() (+1 more)

### Community 312 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 314 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 315 - "interviews_feedback_service.py"
Cohesion: 0.10
Nodes (34): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackScoreInputs, FeedbackWriteInputs (+26 more)

### Community 316 - "U0 baselines"
Cohesion: 0.25
Nodes (7): Before relying on this, Cost, Eval baselines, How to use this file, Live interviews (from `logs/app.log`, before U1), Prompts with no eval baseline (gaps), U0 baselines

### Community 317 - "clock"
Cohesion: 0.20
Nodes (6): Known Issues, Project Conventions, _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 318 - "run_generation"
Cohesion: 0.04
Nodes (82): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), notes_fingerprint(), pacer() (+74 more)

### Community 324 - "test_profile_evals.py"
Cohesion: 0.17
Nodes (12): build_file(), load_cases(), Path, The case as the file a candidate would upload. Hidden lines are white (PDF) or…, LabelledModel, Any, The profile eval runner offline: every synthetic case builds into a readable…, Answers each case with its own label, so the scores test the pipeline and the… (+4 more)

### Community 325 - "_Stt"
Cohesion: 0.33
Nodes (3): The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank)., _Stt

### Community 326 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 327 - "RecordingClient"
Cohesion: 0.22
Nodes (3): Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, recording(), RecordingClient

### Community 328 - "safe_fetch.py"
Cohesion: 0.14
Nodes (10): _decode(), FetchError, BaseTransport, Exception, Fetch a web page whose address a user chose, without letting that user reach…, Header charset, else a <meta> charset, else UTF-8; never raises (bad bytes…, codecs, ipaddress (+2 more)

### Community 329 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 330 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (9): Reload rows a commit expired, so reading their fields later needs no database…, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 331 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 332 - "User"
Cohesion: 0.07
Nodes (34): verify_password(), User, AuthRepository, Session, UUID, Response, UUID, The interview voice adapter, HTTP side: request -> VoiceService, domain result… (+26 more)

### Community 333 - "U2 (tenacity) vs. the U0 baseline"
Cohesion: 0.33
Nodes (5): An extra set of runs (not used for the verdict), Failures, Scores, Still to do, U2 (tenacity) vs. the U0 baseline

### Community 334 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 337 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

## Knowledge Gaps
- **1102 isolated node(s):** `cuewise-be`, `What it does`, `How to invoke`, `Example output`, `See also` (+1097 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2679 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **50 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LLMError` connect `LLMError` to `LLMServerError`, `Cuewise BE — Project Instructions`, `ReferenceNote`, `CandidateProfile`, `test_tracing.py`, `FakeChatModel`, `interviews_rag_evals.py`, `errors.py`, `interviews_session_utils.py`, `TranscriptionResult`, `Implementation Steps`, `Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `tracing.py`, `test_factory.py`, `test_evals.py`, `Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)`, `FakeSynthesizer`, `test_profile_context.py`, `interviews_feedback_service.py`, `clock`, `FakeEmbedder`, `test_gateway.py`, `interviews_evals.py`, `RetryPolicy`, `LLMRequestError`, `interviews_context.py`, `LLMResult`, `Feature: Langfuse Tracing`, `interviews_constants.py`, `Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Why does `ContextManager` connect `interviews_context.py` to `WithInterviewData`, `QuestionTurn`, `tiny_context`, `test_feedback_evals.py`, `Slices in detail`, `test_reply_contract.py`, `interviews_start_dependencies.py`, `interviews_answer_service.py`, `test_feedback_endpoint.py`, `test_context_strategies.py`, `FakeChatModel`, `.record_turn`, `test_context.py`, `test_evals.py`, `InterviewQuestion`, `interviews_feedback.py`, `interviews_feedback_service.py`, `test_profile_context.py`, `uuid`, `ErrorResponse`, `interviews_evals.py`, `Learn: Context management (what to send, and what it costs)`, `interviews_route.py`, `Completed Steps`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `test_generation_eval.py`, `FakeLangfuse`, `ReferenceNote`, `test_summary_evals.py`, `CandidateProfile`, `test_feedback_evals.py`, `interviews_start_dependencies.py`, `interviews_answer_service.py`, `test_feedback_endpoint.py`, `test_tracing.py`, `FakeChatModel`, `interviews_rag_evals.py`, `FakeClient`, `tracing.py`, `test_factory.py`, `test_evals.py`, `InterviewQuestion`, `Feature: Langfuse experiments for the interviews evals`, `test_openai_compatible_stream.py`, `experiments`, `interviews_feedback_service.py`, `test_tracing_routes.py`, `run_generation`, `interviews_summary_evals.py`, `test_profile_evals.py`, `traces`, `RecordingClient`, `KnowledgeRepository`, `interviews_evals.py`, `test_retrieval_eval.py`, `test_profile_redaction.py`, `RetryPolicy`, `LLMError`, `interviews_context.py`, `LLMResult`, `interviews_route.py`, `test_tracing_lifespan.py`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Tracer` (e.g. with `ChatTrace` and `TracerHandle`) actually correct?**
  _`Tracer` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 51 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 56 inferred relationships involving `LLMResult` (e.g. with `complete_chat()` and `_run()`) actually correct?**
  _`LLMResult` has 56 INFERRED edges - model-reasoned connections that need verification._
- **Are the 33 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 33 INFERRED edges - model-reasoned connections that need verification._