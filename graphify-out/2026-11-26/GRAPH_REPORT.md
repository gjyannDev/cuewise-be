# Graph Report - cuewise-be  (2026-11-26)

## Corpus Check
- 484 files · ~445,951 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 9 file(s) not represented in the graph (top: (none) 4, .example 1, .ini 1)

## Summary
- 6740 nodes · 18879 edges · 327 communities (268 shown, 59 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 3631 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3f3619f6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- KnowledgeRepository
- test_retry.py
- test_profile_eval_metrics.py
- decode_token
- test_interview_report.py
- auth_service.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- interviews_retrieval_service.py
- tests/conftest.py
- WithInterviewData
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- test_feedback_contract.py
- test_feedback_evals.py
- test_safe_fetch.py
- User
- test_prompt_registry.py
- cuewise-be
- RateLimiter
- interviews_answer_service.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_rag_evals.py
- FakeStream
- Feature: Context Management for the Interview LLM Calls
- check_prompts
- test_retry_budget.py
- test_profile_read_resume.py
- 4. How it works
- Feature: LLM as the Interviewer (it asks the questions)
- Completed Steps
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- interviews_job_url_service.py
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_evals.py
- interviews_feedback.py
- test_profile_redaction.py
- LLMResult
- profile_service.py
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- Implementation Plan: Résumé-aware interview (Slice 8d)
- test_tracing_routes.py
- test_context_controller.py
- Rules
- job_description_summary_v2.md
- errors.py
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- ContextManager
- test_answer_llm.py
- interviews_rag_evals.py
- Implementation Steps
- exception_handlers.py
- interviews_feedback_evals.py
- test_gateway.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- profile_reply.py
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)
- interviews_evals.py
- FakeTranscriber
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- FollowUpAction
- Implementation Steps
- LLMError
- EmbeddingKind
- test_tracing.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- pytest
- test_speech_contracts.py
- Langfuse Observability
- interviewer_v3.md
- LLMServerError
- interviews/conftest.py
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_speech.py
- test_get_interview.py
- Role
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- parse_log
- fixture
- interview_report.py
- Implementation Plan: Langfuse Tracing
- Feature: Langfuse Tracing
- Langfuse
- JobRole
- Implementation: Prompt Registry
- bind_log_context
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- Role
- Implementation: U2 — One tenacity retry policy for the AI call layer
- Feature: Agentic Workflow v2 (debug, review-feature, gated loop)
- profile_resume_files.py
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Feature: Résumé upload and candidate profile (Slice 8c)
- How to evaluate an AI feature: from the command to the fix
- Feature: Résumé-aware interview (Slice 8d)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- test_start_with_profile.py
- Implementation: Interview History List (backend)
- Judge Calibration
- profile_resume_utils.py
- build_usage_report
- Setup complete-behavioral-junior
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- Feature: Interview Feedback and Scoring (Slice 6)
- test_knowledge_ingest.py
- ChatMessage
- test_feedback_context.py
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
- CandidateProfile
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- scrub_contacts
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Tracer
- 4. How it works
- merge_note_rankings
- Learn: Résumé-aware interview (Slice 8d)
- test_answer_with_profile.py
- test_reaction_pick.py
- llm
- QuestionCategory
- hint_for
- test_question_bank.py
- interviews_feedback_turn.py
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Feature: Interview History List (backend)
- feedback_score_v1.md
- feedback_write_v1.md
- Implementation: Layered Modules (route -> controller -> service -> repository)
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- LLMProvider
- Feature: Langfuse experiments for the interviews evals
- Implementation: LLM as the Interviewer (it asks the questions)
- audio_container
- interviews_feedback_controller.py
- types.py
- FakeSynthesizer
- profile_extract.py
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- ErrorResponse
- get_current_user
- Implementation: Three New Interview Roles (designer, qa, devops)
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
- TracingProvider
- Communication and priorities
- Engineering habits
- Senior judgement
- sqlalchemy
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
- Implementation Plan: Interview History List (backend)
- test_tracing_lifespan.py
- Feature: U1 structlog (structured JSON logs)
- Langfuse CLI Reference
- test_generation_eval.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- test_answer_interview.py
- test_profile_evals.py
- Learn: Résumé upload and the candidate profile (Slice 8c)
- experiment
- get_logger
- Learn: Adding interview roles (designer, qa, devops)
- interviews_prompt_registry.py
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- StreamedTurn
- build_tracer
- InterviewQuestion
- LogCapture
- test_job_description_summary.py
- 4. How it works
- check_layers
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- Langfuse
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- done
- Langfuse Observability
- QuestionTurn
- Learn: Splitting the interviews dependency wiring
- Affected Files & Patterns
- FakeObservation
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Langfuse Prompt Migration
- profile_extract_v1.md
- traces
- Langfuse Prompt Migration
- test_factory.py
- 2. Langfuse Documentation
- test_keyterms.py
- profile_route.py
- interviews_constants.py
- Implementation Steps
- interview-room/README.md
- stream_answer
- test_log_context.py
- interviews_feedback_service.py
- U0 baselines
- check_core
- FakeLangfuse
- Learn: Layered architecture (route -> controller -> service -> repository)
- ._covers_every_criterion
- lf

## God Nodes (most connected - your core abstractions)
1. `User` - 131 edges
2. `Tracer` - 123 edges
3. `FakeProvider` - 118 edges
4. `JobRole` - 116 edges
5. `LLMResult` - 108 edges
6. `LLMServerError` - 105 edges
7. `Level` - 101 edges
8. `InterviewType` - 97 edges
9. `InterviewQuestion` - 97 edges
10. `LLMError` - 93 edges

## Surprising Connections (you probably didn't know these)
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `1. Why it exists` --references--> `DeepgramTranscriber`  [INFERRED]
  docs/features/interview-room/learnings.md → app/core/ai/deepgram.py
- `6. Try it yourself` --references--> `get_tracer()`  [INFERRED]
  docs/features/split-interviews-dependencies/learnings.md → app/core/ai/dependencies.py
- `Acceptance Criteria` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py
- `Functional` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py

## Import Cycles
- None detected.

## Communities (327 total, 59 thin omitted)

### Community 0 - "KnowledgeRepository"
Cohesion: 0.09
Nodes (27): alembic_config, KnowledgeChunk, _eligible(), KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, Active chunks scoped to this role (or every role) and this level. Role and…, End the read transaction before a slow call (the embedding), so no connection… (+19 more)

### Community 1 - "test_retry.py"
Cohesion: 0.12
Nodes (43): anyio_lowlevel, parse_retry_after(), The Retry-After header as seconds. Only the delta-seconds form is read; an HTTP…, 5. What can go wrong, anyio_backend(), Clock, fields(), make_policy() (+35 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.09
Nodes (49): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, _injection_share(), _mention_share(), notes_overlap() (+41 more)

### Community 3 - "decode_token"
Cohesion: 0.09
Nodes (39): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, BaseModel, UserAdminOut (+31 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.10
Nodes (64): analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start(), html_for() (+56 more)

### Community 5 - "auth_service.py"
Cohesion: 0.11
Nodes (28): ConflictError, hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), post (+20 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.15
Nodes (12): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards, Git Rules (STRICT) (+4 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "interviews_retrieval_service.py"
Cohesion: 0.08
Nodes (33): Embedder, Protocol, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Step, log_retrieval(), Which reference notes an interview got at start: mode, count, scores, how many…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as… (+25 more)

### Community 9 - "tests/conftest.py"
Cohesion: 0.05
Nodes (45): health_check(), CurrentUserDep, Deviations from Plan, Affected Files & Patterns, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend) (+37 more)

### Community 10 - "WithInterviewData"
Cohesion: 0.08
Nodes (31): build_context_manager(), A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WithInterviewData, The labelled text the write call is asked for (the parser reads it back…, 6. Try it yourself, Affected Files & Patterns (+23 more)

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
Nodes (43): ProviderConfig, One listed provider, resolved from its vendor block., _google(), no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture (+35 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.09
Nodes (42): Review, anyio_backend(), audio(), Clock, listen_body(), make_synthesizer(), _make(), make_transcriber() (+34 more)

### Community 16 - "test_feedback_contract.py"
Cohesion: 0.16
Nodes (36): compute_overall(), parse_score_reply(), parse_write_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The write call's text, slot by slot: every section once and in order, list…, 6. Try it yourself, parametrize (+28 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.10
Nodes (42): feedback_trace_output(), One case through the same pre-check, score call, write call and template…, What came out next to what was wanted: the verdict, the overall against its…, run_feedback_case(), case(), Grader, parametrize, Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The… (+34 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (41): Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request, Response (+33 more)

### Community 19 - "User"
Cohesion: 0.07
Nodes (34): NotFoundError, User, AuthRepository, Session, UUID, Response, UUID, The interview voice adapter, HTTP side: request -> VoiceService, domain result… (+26 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.15
Nodes (21): Data, StrEnum, What an interviewer write carries beyond the job description; it picks the…, 5. What can go wrong, catalog_mismatches(), Collection, The prompt registry's guards (prompt-registry AC1, AC2, AC6, EC1-EC4). Each…, A string literal that is exactly a version name, outside the registry: a… (+13 more)

### Community 26 - "RateLimiter"
Cohesion: 0.07
Nodes (47): RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, Per-user caps on paid speech calls. One limiter instance per process: every…, get_db(), Session (+39 more)

### Community 27 - "interviews_answer_service.py"
Cohesion: 0.05
Nodes (75): QuestionNotCurrentError, SessionNotInProgressError, current_request_id(), log_stream_summary(), How a streamed turn felt and ended: time to the first event and to the first…, PhaseChanged, The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent (+67 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.05
Nodes (89): FeedbackWrite, The write call: scores, evidence and question texts only; small whatever the…, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists, 2. What it is, 3. When to use it (+81 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.14
Nodes (38): FollowUpDecision, The decide call: the current thread in full (it judges the latest answer within…, decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i. (+30 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.06
Nodes (35): Save one whole turn in one commit: advance the session, the answer, the…, AnswerOut, Deviations from Plan, Affected Files & Patterns, 5. What can go wrong, 6. Try it yourself, Step 2: Event contract, Functional (+27 more)

### Community 31 - "test_rag_evals.py"
Cohesion: 0.07
Nodes (53): build_sheet(), case_set_problems(), ExtraSetup, filter_baseline(), _is_short_items(), BaseModel, Collection, Exception (+45 more)

### Community 32 - "FakeStream"
Cohesion: 0.14
Nodes (24): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, drain(), result(), test_a_redacted_call_records_a_placeholder_instead_of_the_messages(), test_a_redacted_failure_records_no_partial_text(), test_a_redacted_stream_closed_early_records_no_partial_text() (+16 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "check_prompts"
Cohesion: 0.15
Nodes (21): check_prompts(), PromptCheckError, Exception, One or more routed prompts cannot be sent; the message lists each one., Raises PromptCheckError naming every routed version whose file is missing or…, 4. How it works, 7. What surprised me, Eval log (AI features only) (+13 more)

### Community 35 - "test_retry_budget.py"
Cohesion: 0.12
Nodes (16): anyio_backend(), Clock, counting(), handler(), malformed_reply(), anyio, fixture, parametrize (+8 more)

### Community 36 - "test_profile_read_resume.py"
Cohesion: 0.15
Nodes (33): make_docx(), make_pdf(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, A PDF with one page per list. `encrypt` adds a standard security handler whose…, rezip(), read_resume(), ResumeUnreadableRefusal, ResumeUnsupportedRefusal (+25 more)

### Community 37 - "4. How it works"
Cohesion: 0.05
Nodes (36): _decode(), FetchedPage, FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach… (+28 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.11
Nodes (19): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+11 more)

### Community 39 - "Completed Steps"
Cohesion: 0.06
Nodes (77): log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _embed(), ingest_corpus(), IngestCounts, NamedTuple (+69 more)

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
Nodes (28): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+20 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.10
Nodes (35): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, Any network-side failure of a job link. One message for every cause, so…, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, JobTextFormat, Which clipboard copy the client sent: the HTML one when the browser has it (its… (+27 more)

### Community 45 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.07
Nodes (101): FakeProvider, load_cases(), main(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, run_case(), console_number() (+93 more)

### Community 49 - "interviews_feedback.py"
Cohesion: 0.13
Nodes (29): _check_lengths(), Evidence, _has_markup(), _normalized(), BaseModel, NamedTuple, _question_score(), QuestionScore (+21 more)

### Community 50 - "test_profile_redaction.py"
Cohesion: 0.32
Nodes (14): assert_redacted(), assert_traced_in_full(), generations(), inputs(), anyio, resume-aware-interview Step 5: a write whose prompt carries the profile is…, run_stream_write(), run_write() (+6 more)

### Community 51 - "LLMResult"
Cohesion: 0.08
Nodes (71): LLMResult, InterviewerInputs, The labels of one write call. A write whose prompt carries the candidate…, Plain values for one interviewer or decide call., write_trace_labels(), decide(), UUID, The decide step of an answer turn: the model suggests following up or moving… (+63 more)

### Community 52 - "profile_service.py"
Cohesion: 0.08
Nodes (33): ProfileExtractionFailedError, ProfileNotFoundError, ProfileUnavailableError, Over the byte, page or unzipped-size limit of a résumé upload., Not a PDF or a Word document by its content (the file name is never trusted)., Encrypted, corrupt, scanned, too little text, or no usable profile in it., The model gave no valid profile after the retry, timed out, or the provider…, ResumeTooLargeError (+25 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (21): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+13 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.14
Nodes (37): 5. What can go wrong, Open Questions, fail(), error(), import_url(), long_posting(), page(), paste() (+29 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.11
Nodes (31): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+23 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (65): Call, group_requests(), _int(), NamedTuple, The events of each request, oldest request first (the id is on every line of…, The requests that logged this session, oldest first: the start, then one…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+57 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (37): Deviations from Plan, busy(), Clock, completion(), make_provider(), fixture, parametrize, Response (+29 more)

### Community 59 - "Implementation Plan: Résumé-aware interview (Slice 8d)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Blockers & Resolutions, Decisions (grill-me, 2026-11-14), Deviations during implementation (2026-11-14, see task.md), Implementation Plan: Résumé-aware interview (Slice 8d), Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 61 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 62 - "Rules"
Cohesion: 0.09
Nodes (20): caveman, Example output, How to invoke, See also, What it does, 1. Answer first, 2. Kill ceremony, 3. Short word (+12 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "errors.py"
Cohesion: 0.08
Nodes (44): open_stream(), AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ErrorBody, InvalidCredentialsError, NoSpeechError (+36 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.10
Nodes (48): EmbedCall, FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, test_a_slow_fake_embedder_waits_at_most_its_budget_then_times_out(), test_fake_embedder_honors_scripted_vectors_and_errors(), test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets() (+40 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.17
Nodes (30): Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, Step 13: The streamed write step in `stream_turn`, collect(), follow_up_json(), inputs() (+22 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (37): 5. What can go wrong, profile_json(), Synthetic résumé data and the scripted model shared by the profile tests (no…, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,… (+29 more)

### Community 68 - "ContextManager"
Cohesion: 0.07
Nodes (50): BuiltContext, ContextManager, ContextReport, ContextTooLargeError, _log(), Exception, NamedTuple, Even with every droppable entry gone the input is over the strategy's limit. (+42 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.05
Nodes (42): 2. What it is, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+34 more)

### Community 71 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (87): ExperimentRun, NamedTuple, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, What a recorded experiment run left behind: its name and link, and the trace of…, final_line(), notes_fingerprint(), What every eval task moved onto Langfuse experiments shares (langfuse-… (+79 more)

### Community 72 - "Implementation Steps"
Cohesion: 0.09
Nodes (21): Affected Files & Patterns, Blockers & Resolutions, Deviations Found During Implementation, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps, Overview, Phase A: plumbing and progress events, Phase B: streaming the question text (+13 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.17
Nodes (24): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, BaseException, Exception (+16 more)

### Community 74 - "interviews_feedback_evals.py"
Cohesion: 0.07
Nodes (49): ThreadTurn, Band, _band_check(), check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for(), feedback_run_scores() (+41 more)

### Community 75 - "test_gateway.py"
Cohesion: 0.18
Nodes (24): anyio_backend(), _Broken, code_of(), fixture, parametrize, The speech gateway: the generic half of every speech call (checks, vendor…, A vendor adapter with a bug: it raises something that isn't an LLMError., stt_lines() (+16 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues (+8 more)

### Community 77 - "profile_reply.py"
Cohesion: 0.17
Nodes (24): fit(), parse_profile_reply(), BaseModel, The contract for the profile-extraction reply, and the check that enforces it.…, Whitespace tidied, then cut to `max_length` on a word boundary (a single over-…, Tidied, blanks dropped, duplicates merged ignoring case (the first spelling…, _RawProfile, _RawProject (+16 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)

### Community 81 - "interviews_evals.py"
Cohesion: 0.06
Nodes (73): anyio_from_thread, SummaryInputs, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision() (+65 more)

### Community 82 - "FakeTranscriber"
Cohesion: 0.14
Nodes (11): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, test_a_transcription_fills_every_result_field(), The speech-to-text seam of a test: a scripted transcriber and a fresh per-test… (+3 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "FollowUpAction"
Cohesion: 0.12
Nodes (30): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Completed Steps (+22 more)

### Community 85 - "Implementation Steps"
Cohesion: 0.13
Nodes (17): Page, BaseModel, Offset pagination shared by every list endpoint, so clients see one query…, UsersController, get_controller(), get_service(), Depends, Session (+9 more)

### Community 86 - "LLMError"
Cohesion: 0.04
Nodes (57): AsyncBaseTransport, BaseTransport, LLMError, Exception, Base for every provider failure. `retryable` marks faults that may pass on…, _Call, BaseException, Logger (+49 more)

### Community 87 - "EmbeddingKind"
Cohesion: 0.08
Nodes (37): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, A vector of another length than configured. Vectors of different sizes can't be…, GoogleEmbedder, BaseTransport (+29 more)

### Community 88 - "test_tracing.py"
Cohesion: 0.07
Nodes (16): client(), FakeClient, propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_score_failure_is_swallowed() (+8 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "pytest"
Cohesion: 0.16
Nodes (25): candidate_profile_block(), profile_query_text(), The candidate profile as interview input: a fenced prompt block and a short…, The profile fenced as data, like the job description. Summaries and…, The profile's short items as one retrieval query. None: nothing to embed., Project, Testing Strategy, pytest (+17 more)

### Community 93 - "test_speech_contracts.py"
Cohesion: 0.14
Nodes (16): BaseModel, One spoken clip. `content_type` is what the vendor says the audio is: the…, `text` spoken in the configured voice, as one whole clip., SynthesisResult, anyio_backend(), _aura(), _deepgram(), _no_wait() (+8 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "LLMServerError"
Cohesion: 0.06
Nodes (55): anyio, Context management: the one place that decides what each LLM call sends. The…, Deepgram over plain httpx: pre-recorded speech-to-text (`POST /v1/listen`, Nova…, The embedding contract features code against, separate from the chat…, Test doubles for LLMProvider, Transcriber, SpeechSynthesizer and Embedder:…, Any, Gemini embeddings through Google's native `batchEmbedContents` endpoint, over…, _int_or_none() (+47 more)

### Community 97 - "interviews/conftest.py"
Cohesion: 0.09
Nodes (42): NotEnoughQuestionsError, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), pick_fallback_question(), Collection, Random, One unused bank question for `position`, used when the LLM is off or its reply… (+34 more)

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
Cohesion: 0.10
Nodes (24): 5. What can go wrong, answered(), assert_hidden(), code(), fixture, parametrize, GET /interviews/{id}/questions/{qid}/speech and /messages/{mid}/speech: the…, An owner with a started backend interview: (owner, session_id, first question). (+16 more)

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "Role"
Cohesion: 0.18
Nodes (22): EmptyProfileError, Exception, No skills and no roles: not a résumé we can use (refused as unreadable, nothing…, Role, _appears(), ground_profile(), keep(), _normalized() (+14 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "parse_log"
Cohesion: 0.10
Nodes (29): _json_event(), LogEvent, parse_log(), Reading the app's own log back: what each request did for an interview, from…, Old text lines: `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]).…, Reads both log formats, so a log that rotated mid-change (`app.log.1` text,…, _split_fields(), _text() (+21 more)

### Community 109 - "fixture"
Cohesion: 0.12
Nodes (17): answer(), _answer(), anyio_backend(), delete_profile(), _delete(), fixture, POST an answer; `question_id` defaults to whatever the caller passes, body…, Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio… (+9 more)

### Community 110 - "interview_report.py"
Cohesion: 0.15
Nodes (19): html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+11 more)

### Community 111 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "JobRole"
Cohesion: 0.07
Nodes (77): What the interview LLM calls send: the tasks and strategies registered with the…, InterviewType, JobRole, Level, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, EvalSetup, ExtraSetupFields (+69 more)

### Community 115 - "Implementation: Prompt Registry"
Cohesion: 0.13
Nodes (14): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Links (+6 more)

### Community 116 - "bind_log_context"
Cohesion: 0.06
Nodes (46): bind_log_context(), _formatter(), _json_renderer(), Path, Writes to whatever `sys.stderr` is at the time of the write (test runners and…, Routes every logger through the processor chain. Safe to call again (tests do):…, Adds fields to every later log line of the current request (or, outside a…, setup_logging() (+38 more)

### Community 117 - "The fundamentals"
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+17 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Role"
Cohesion: 0.06
Nodes (36): permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry(), test_unknown_role_has_no_permissions_and_is_logged(), test_user_can_only_read_self() (+28 more)

### Community 121 - "Implementation: U2 — One tenacity retry policy for the AI call layer"
Cohesion: 0.12
Nodes (15): 13. Pin the call budget, Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U2 — One tenacity retry policy for the AI call layer, Known Issues, Links (+7 more)

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "profile_resume_files.py"
Cohesion: 0.13
Nodes (26): _content(), _escape(), _fill(), Image, plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build…, Rect, Text (+18 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+6 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.11
Nodes (20): injection_ignored(), 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+12 more)

### Community 127 - "Feature: Résumé-aware interview (Slice 8d)"
Cohesion: 0.11
Nodes (17): _json(), Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé-aware interview (Slice 8d), Functional (+9 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "test_start_with_profile.py"
Cohesion: 0.25
Nodes (16): 5. What can go wrong, first_question(), profile_of(), Starting an interview with the candidate's profile (resume-aware-interview Step…, A synthetic profile whose every free-text field carries `marker`, so a leak…, sent(), sessions(), test_a_refused_start_leaves_the_interview_in_progress_alone() (+8 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "profile_resume_utils.py"
Cohesion: 0.10
Nodes (36): _clean(), _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _has_external_relationship() (+28 more)

### Community 134 - "build_usage_report"
Cohesion: 0.20
Nodes (16): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, main(), Session, Print stored LLM usage per interview: tokens per question position and per…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind() (+8 more)

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

### Community 140 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional (+5 more)

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.21
Nodes (23): IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, active(), chunks(), corpus(), FailingOn, interview() (+15 more)

### Community 143 - "ChatMessage"
Cohesion: 0.09
Nodes (27): estimate_tokens(), ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, Step 11: `FakeProvider.stream`, Reply (+19 more)

### Community 144 - "test_feedback_context.py"
Cohesion: 0.25
Nodes (16): FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, Step 4 of the feedback plan: what the score and write calls send, through the…, score_inputs(), scored(), test_an_answer_over_the_cap_is_shortened_and_counted_but_quotes_still_verify(), test_an_interview_over_the_limit_raises_instead_of_dropping_an_answer(), test_closing_tags_inside_untrusted_text_are_neutralised() (+8 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only"
Cohesion: 0.19
Nodes (17): Baseline Failures, Baseline Failures, Testing Strategy, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,… (+9 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_reply_contract.py"
Cohesion: 0.06
Nodes (59): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open (+51 more)

### Community 151 - "interviews_start_dependencies.py"
Cohesion: 0.08
Nodes (55): get_llm_provider(), get_synthesizer(), get_tracer(), get_transcriber(), Request, Request dependencies for the AI services every feature shares, built once at…, Built once at startup (app lifespan); None when no key is configured or the…, Built once at startup (app lifespan); a disabled tracer when the lifespan… (+47 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Skills Consulted During Implementation, Status (+4 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.15
Nodes (24): has_notes(), UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started(), stored(), test_a_follow_up_is_written_without_the_notes() (+16 more)

### Community 156 - "CandidateProfile"
Cohesion: 0.08
Nodes (46): pacer(), wait(), Local time, as the Langfuse list shows the run's start: the name and the…, `wait()` sleeps `pause` seconds on every call but the first. Called before each…, run_stamp(), Limits, thresholds and messages of the résumé upload (resume-upload spec)., Output, CandidateProfile (+38 more)

### Community 157 - "Implementation: Interview Room (backend)"
Cohesion: 0.12
Nodes (15): Changes Made, Current Step, Debug Log, Deviations from Plan, Done. Next: `/review-feature`, Implementation: Interview Room (backend), Known Issues, Links (+7 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 160 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 161 - "Tracer"
Cohesion: 0.04
Nodes (53): AbstractContextManager, Any, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Create the dataset if needed and upsert its items (each carries its own `id`,…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, Send what is still buffered, then stop the background exporter. Called once at… (+45 more)

### Community 162 - "4. How it works"
Cohesion: 0.13
Nodes (13): _DeepgramAdapter, attempt(), attempt(), _parse(), Any, AsyncBaseTransport, Response, T (+5 more)

### Community 163 - "merge_note_rankings"
Cohesion: 0.10
Nodes (30): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gate: Step 10, real-model runs (yours) (+22 more)

### Community 164 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.11
Nodes (16): UUID, The user's stored profile for an interview prompt, read live (never copied onto…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me (+8 more)

### Community 165 - "test_answer_with_profile.py"
Cohesion: 0.25
Nodes (12): opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent(), test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile() (+4 more)

### Community 166 - "test_reaction_pick.py"
Cohesion: 0.23
Nodes (15): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), A predefined, neutral acknowledgement for the answer just given; never the same…, test_the_rubric_anchors_five_levels_for_every_criterion_and_both_level_groups(), pick(), parametrize, test_a_one_entry_pool_still_works() (+7 more)

### Community 167 - "llm"
Cohesion: 0.16
Nodes (11): as_v5_text(), _decision_json(), llm(), script(), script_decide(), script_score(), script_write(), unique_question() (+3 more)

### Community 168 - "QuestionCategory"
Cohesion: 0.08
Nodes (51): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, _check_question(), HeaderSplit, InterviewerReply (+43 more)

### Community 169 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 170 - "test_question_bank.py"
Cohesion: 0.30
Nodes (11): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, Test Results, _entry(), parametrize, test_every_role_has_its_own_technical_question_at_every_level(), test_invalid_bank_raises_clear_error() (+3 more)

### Community 171 - "interviews_feedback_turn.py"
Cohesion: 0.10
Nodes (27): ScoreResult, _Attempts, FeedbackGenerator, NamedTuple, T, UUID, The two LLM calls of end-of-interview feedback: score (closed JSON), then write…, At most two attempts; a retry only for a reply that came back but broke the… (+19 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.15
Nodes (16): Baseline Failures, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL), Testing Strategy (+8 more)

### Community 174 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Changes Made, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 178 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 179 - "LLMProvider"
Cohesion: 0.06
Nodes (32): LLMProvider, Protocol, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions (+24 more)

### Community 180 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.17
Nodes (11): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Goal, Out of Scope, Problem (+3 more)

### Community 181 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 182 - "audio_container"
Cohesion: 0.25
Nodes (14): audio_container(), AudioContainer, _has_signature(), StrEnum, Audio rules every speech feature shares: which recording containers are…, Recording containers an upload may arrive in (what browsers' MediaRecorder…, The container of an uploaded recording, or None when its declared type isn't…, enum (+6 more)

### Community 183 - "interviews_feedback_controller.py"
Cohesion: 0.11
Nodes (21): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, get_feedback_controller(), FeedbackEvidenceOut (+13 more)

### Community 184 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 185 - "FakeSynthesizer"
Cohesion: 0.22
Nodes (6): FakeSynthesizer, Scripted clips (bytes, a full result, or an error), one per call; records each…, Affected Files & Patterns, The text-to-speech seam of a test: a scripted synthesizer and a fresh per-test…, No synthesizer configured (DEEPGRAM_API_KEY blank)., _Tts

### Community 186 - "profile_extract.py"
Cohesion: 0.16
Nodes (15): load_prompt(), Path, Prompt files: versioned Markdown read once per process. Feature modules pass…, `<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in…, build_messages(), Extraction, NamedTuple, The extraction call: scrubbed résumé text in, a validated profile out (resume-… (+7 more)

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
Nodes (53): ErrorResponse, Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+45 more)

### Community 203 - "get_current_user"
Cohesion: 0.11
Nodes (21): ForbiddenError, get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, check(), require_roles(), check(), bearer_scheme, Affected Files & Patterns (+13 more)

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.15
Nodes (12): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.18
Nodes (21): embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, 15 cases with the kinds the label rules require: most expect API design first;…, run() (+13 more)

### Community 220 - "Generation"
Cohesion: 0.25
Nodes (5): Generation, The stream was closed before it finished (client left, or the turn's deadline…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, _usage_details(), TraceLabels

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

### Community 234 - "TracingProvider"
Cohesion: 0.24
Nodes (5): _model_parameters(), ReasoningEffort, What the call asked the model for, shown on the generation. A temperature only…, TracingProvider, test_disabled_tracer_is_a_pass_through()

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "sqlalchemy"
Cohesion: 0.09
Nodes (29): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, InterviewSessionChunk (+21 more)

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
Cohesion: 0.09
Nodes (49): alias, AnswerControllerDep, Permission, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), me(), limit_feedback(), interviews_feedback (+41 more)

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
Cohesion: 0.14
Nodes (16): _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), _plain(), _posting_text(), Turn a fetched job page into plain job-description text (Slice 8b). Pure…, A JSON-LD description is usually HTML, sometimes entity-escaped HTML: unescape,… (+8 more)

### Community 251 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 252 - "Implementation Plan: Interview History List (backend)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview History List (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 253 - "test_tracing_lifespan.py"
Cohesion: 0.20
Nodes (7): fastapi_testclient, The app lifespan runs the prompt check before anything else (prompt-registry…, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 255 - "Feature: U1 structlog (structured JSON logs)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: U1 structlog (structured JSON logs), Functional, Goal, Non-Functional (+6 more)

### Community 256 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 257 - "test_generation_eval.py"
Cohesion: 0.08
Nodes (53): parse_arms(), Read your filled-in sheet, print how often each arm ranked first, then post…, `--arms`: comma-separated arm letters (any case), at least two (a ranking…, run_ranking(), argparse, 5. What can go wrong, parametrize, The generation eval's arms D and E (resume-aware-interview Step 9a; seam S5).… (+45 more)

### Community 258 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 259 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 260 - "test_profile_evals.py"
Cohesion: 0.23
Nodes (9): build_file(), The case as the file a candidate would upload. Hidden lines are white (PDF) or…, LabelledModel, The profile eval runner offline: every synthetic case builds into a readable…, Answers each case with its own label, so the scores test the pipeline and the…, test_a_model_that_answers_the_labels_scores_one_everywhere(), test_every_case_builds_into_a_file_whose_visible_text_holds_its_labels(), test_the_hidden_injection_is_dropped_before_the_model() (+1 more)

### Community 261 - "Learn: Résumé upload and the candidate profile (Slice 8c)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Résumé upload and the candidate profile (Slice 8c)

### Community 262 - "experiment"
Cohesion: 0.13
Nodes (19): 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Prompt registry (one place for prompt versions and routing), User Flow, experiment() (+11 more)

### Community 263 - "get_logger"
Cohesion: 0.08
Nodes (31): get_logger(), Logger, 5. What can go wrong, fastapi_responses, parametrize, The logging pipeline (U1 structlog): what actually lands in the log file and on…, test_a_key_that_only_contains_a_sensitive_word_is_kept(), test_a_logged_exception_is_one_line_with_the_traceback() (+23 more)

### Community 264 - "Learn: Adding interview roles (designer, qa, devops)"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

### Community 265 - "interviews_prompt_registry.py"
Cohesion: 0.39
Nodes (8): PromptVersion, Every interviews prompt version, and which one each LLM call sends. Data only:…, Status, archived_routes(), incomplete_entries(), test_a_route_to_an_archived_or_unknown_version_is_named(), test_an_entry_with_no_reason_or_a_wrong_name_is_named(), types

### Community 266 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 267 - "StreamedTurn"
Cohesion: 0.25
Nodes (6): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

### Community 268 - "build_tracer"
Cohesion: 0.32
Nodes (7): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, Completed Steps, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 269 - "InterviewQuestion"
Cohesion: 0.04
Nodes (78): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, MessageRole, QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, A main question opens a thread; a follow-up digs into the latest answer of that…, InterviewMessage (+70 more)

### Community 270 - "LogCapture"
Cohesion: 0.29
Nodes (4): StringIO, LogCapture, Path, What the real logging pipeline wrote during a test: the file's JSON lines and…

### Community 271 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 272 - "4. How it works"
Cohesion: 0.07
Nodes (27): _default_request_id(), _merge_request_fields(), Any, Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything…, Dev console: time, level, short request id, logger, event, then one aligned…, ReadableRenderer, redact_sensitive(), _redacted() (+19 more)

### Community 273 - "check_layers"
Cohesion: 0.33
Nodes (6): Blockers & Resolutions, Known Issues, check_layers(), Every layer-rule violation in `files` (repo-relative path -> source), as…, test_clean_layer_imports_have_no_violations(), _violation()

### Community 274 - "Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 275 - "Implementation Plan: Agentic Workflow v2"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: Agentic Workflow v2, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 276 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 277 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy, Trade-offs & Rationale

### Community 290 - "done"
Cohesion: 0.11
Nodes (20): done(), 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Streaming and latency (Slice 4, SSE) (+12 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "QuestionTurn"
Cohesion: 0.05
Nodes (58): StrategyOutput, _counts(), FullHistory, JobDescriptionSummary, An earlier question as the model would have written it. A follow-up was written…, App data at the end of the last user message; untrusted parts (questions,…, _status_block(), Every stored question, grouped by interview in creation order (UUIDv7), for the… (+50 more)

### Community 293 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+2 more)

### Community 294 - "Affected Files & Patterns"
Cohesion: 0.33
Nodes (5): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns

### Community 296 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "profile_extract_v1.md"
Cohesion: 0.40
Nodes (4): Constraints, Input, Role, Task

### Community 299 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 301 - "test_factory.py"
Cohesion: 0.04
Nodes (81): DeepgramSynthesizer, DeepgramTranscriber, Aura text-to-speech: the text goes in a JSON body, the voice (`model`) and…, build_embedder(), build_provider(), build_synthesizer(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a… (+73 more)

### Community 302 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 303 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 304 - "profile_route.py"
Cohesion: 0.16
Nodes (15): _out(), ProfileController, The signed-in user's résumé profile: request -> ProfileService, stored row ->…, delete_profile(), get_profile(), post, ProfileUser, A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes… (+7 more)

### Community 305 - "interviews_constants.py"
Cohesion: 0.06
Nodes (69): ProfileRequiredError, An interview asked to use the candidate's profile, and there is none to use…, page_params(), PageParams, NamedTuple, Query, HistorySortColumn, MessageKind (+61 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 308 - "stream_answer"
Cohesion: 0.40
Nodes (5): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream()

### Community 311 - "test_log_context.py"
Cohesion: 0.29
Nodes (9): fixture, Log context on real interview requests (U1 structlog, AC4): `session` and…, Every line of the one request whose access line ends with `path_end`., _request_lines(), started(), test_a_request_for_someone_elses_interview_logs_the_id_it_asked_for(), test_a_start_request_logs_the_new_session_and_the_user_on_every_line(), test_a_streamed_turn_logs_its_session_and_user_from_inside_the_stream() (+1 more)

### Community 315 - "interviews_feedback_service.py"
Cohesion: 0.09
Nodes (41): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackScoreInputs, FeedbackWriteInputs (+33 more)

### Community 316 - "U0 baselines"
Cohesion: 0.25
Nodes (7): Before relying on this, Cost, Eval baselines, How to use this file, Live interviews (from `logs/app.log`, before U1), Prompts with no eval baseline (gaps), U0 baselines

### Community 317 - "check_core"
Cohesion: 0.25
Nodes (8): Skills Consulted During Implementation, check_core(), _imports(), Every `app/core` import of a feature module (`app.modules...`): core is shared…, (absolute module, imported names) per import statement; relative imports…, test_a_core_file_importing_a_feature_module_is_reported(), test_a_core_file_importing_only_core_and_libraries_is_clean(), test_the_real_core_imports_no_feature_module()

### Community 318 - "FakeLangfuse"
Cohesion: 0.04
Nodes (47): _evaluation(), git_commit(), Any, Score, Run every case once, in order, as one Langfuse experiment run; whatever the run…, The short commit hash, `-dirty` when the working tree has changes, `unknown`…, run_cases(), item_scores() (+39 more)

### Community 319 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository)

### Community 326 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

## Knowledge Gaps
- **1079 isolated node(s):** `cuewise-be`, `What it does`, `How to invoke`, `Example output`, `See also` (+1074 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2547 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **59 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `KnowledgeRepository`, `decode_token`, `auth_service.py`, `tests/conftest.py`, `InterviewQuestion`, `interviews_start_dependencies.py`, `RateLimiter`, `interviews_answer_service.py`, `interviews_job_url_service.py`, `profile_route.py`, `interviews_constants.py`, `profile_service.py`, `test_create_interview.py`, `interviews_feedback_controller.py`, `interviews_feedback_service.py`, `get_current_user`, `Implementation Steps`, `Implementation: Langfuse Tracing`, `sqlalchemy`, `interviews_route.py`, `Role`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Why does `LLMError` connect `LLMError` to `Cuewise BE — Project Instructions`, `interviews_retrieval_service.py`, `InterviewQuestion`, `test_deepgram.py`, `ChatMessage`, `interviews_start_dependencies.py`, `test_rag_evals.py`, `FakeStream`, `4. How it works`, `Completed Steps`, `Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `interviews_feedback_turn.py`, `test_factory.py`, `test_evals.py`, `interviews_constants.py`, `LLMResult`, `profile_service.py`, `LLMProvider`, `FakeSynthesizer`, `profile_extract.py`, `interviews_feedback_service.py`, `errors.py`, `FakeEmbedder`, `test_stream_turn.py`, `test_answer_llm.py`, `interviews_rag_evals.py`, `Implementation Steps`, `Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)`, `interviews_evals.py`, `FakeTranscriber`, `EmbeddingKind`, `Generation`, `test_speech_contracts.py`, `LLMServerError`, `TracingProvider`, `Feature: Langfuse Tracing`, `JobRole`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Why does `LLMProvider` connect `LLMProvider` to `Cuewise BE — Project Instructions`, `InterviewQuestion`, `test_feedback_evals.py`, `interviews_start_dependencies.py`, `RateLimiter`, `interviews_answer_service.py`, `CandidateProfile`, `test_answer_stream.py`, `done`, `interviews_feedback_turn.py`, `test_factory.py`, `test_evals.py`, `interviews_constants.py`, `LLMResult`, `profile_service.py`, `profile_extract.py`, `interviews_feedback_service.py`, `interviews_rag_evals.py`, `Implementation Steps`, `interviews_feedback_evals.py`, `interviews_evals.py`, `LLMServerError`, `TracingProvider`, `sqlalchemy`, `JobRole`, `The fundamentals`, `Feature: Résumé upload and candidate profile (Slice 8c)`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Are the 51 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 41 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 41 INFERRED edges - model-reasoned connections that need verification._
- **Are the 30 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 30 INFERRED edges - model-reasoned connections that need verification._
- **Are the 70 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 70 INFERRED edges - model-reasoned connections that need verification._