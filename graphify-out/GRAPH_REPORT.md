# Graph Report - cuewise-be  (2026-11-26)

## Corpus Check
- 473 files · ~429,530 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 9 file(s) not represented in the graph (top: (none) 4, .example 1, .ini 1)

## Summary
- 6558 nodes · 18336 edges · 326 communities (276 shown, 50 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 3453 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e33f7e51`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- interviews_utils.py
- LLMRateLimitError
- test_profile_eval_metrics.py
- decode_token
- test_interview_report.py
- AuthController
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- Completed Steps
- tests/conftest.py
- WindowLedger
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
- interviews/conftest.py
- interviews_answer_service.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_rag_evals.py
- interviews_rag_evals.py
- Feature: Context Management for the Interview LLM Calls
- check_prompts
- pathlib
- test_profile_read_resume.py
- 4. How it works
- Feature: LLM as the Interviewer (it asks the questions)
- interviews_knowledge_utils.py
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
- QuestionCategory
- InterviewerInputs
- ProfileService
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- ReferenceNote
- test_tracing_routes.py
- test_context_controller.py
- interviews_session_utils.py
- job_description_summary_v2.md
- errors.py
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- test_reference_note_context.py
- test_answer_llm.py
- run_generation
- test_profile_context.py
- exception_handlers.py
- interviews_feedback_evals.py
- test_gateway.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- parse_profile_reply
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- retry.py
- interviews_evals.py
- profile_service.py
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- FollowUpAction
- pydantic
- OpenAICompatibleProvider
- fake.py
- Tracer
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- Project
- Implementation Steps
- Langfuse Observability
- interviewer_v3.md
- LLMResult
- InterviewType
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_speech.py
- test_get_interview.py
- Role
- Settings
- Langfuse Dataset Construction
- parse_log
- test_reply_contract.py
- interview_report.py
- LLMProvider
- Feature: Langfuse Tracing
- Langfuse
- load_prompt
- Implementation: Prompt Registry
- bind_log_context
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- test_guards.py
- summarize
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
- get_logger
- test_knowledge_ingest.py
- ContextManager
- test_feedback_context.py
- Langfuse v4 project migration
- Judge Calibration
- test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only
- Langfuse CI/CD
- Prompt Engineering
- test_follow_ups.py
- interviews_feedback_dependencies.py
- Implementation: Agentic Workflow v2
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- CandidateProfile
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- scrub_contacts
- follow_up
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- 4. How it works
- Implementation: Résumé-aware interview (Slice 8d)
- Learn: Résumé-aware interview (Slice 8d)
- test_answer_with_profile.py
- test_reaction_pick.py
- llm
- test_streamed_reply.py
- hint_for
- JobRole
- Implementation: U1 structlog (structured JSON logs)
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Feature: Interview History List (backend)
- feedback_score_v1.md
- feedback_write_v1.md
- Implementation: Layered Modules (route -> controller -> service -> repository)
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- failed
- Feature: Langfuse experiments for the interviews evals
- Implementation: LLM as the Interviewer (it asks the questions)
- audio_container
- interviews_feedback_controller.py
- Feature: Follow-up Questions (decide / write split)
- run_case
- load_prompt
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- ErrorResponse
- permissions_for
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
- setup_logging
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
- test_fallback_pick.py
- test_tracing_lifespan.py
- Feature: U1 structlog (structured JSON logs)
- Langfuse CLI Reference
- test_generation_eval.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- test_answer_interview.py
- profile_evals.py
- Learn: Résumé upload and the candidate profile (Slice 8c)
- FakeLangfuse
- test_request_context.py
- FeedbackThread
- run_task
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- Web
- experiments
- InterviewQuestion
- main
- test_job_description_summary.py
- ReadableRenderer
- check_layers
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- Langfuse
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation Steps
- Langfuse Observability
- QuestionTurn
- Learn: Splitting the interviews dependency wiring
- Implementation: Error Handling
- Feature: Layered Modules (route -> controller -> service -> repository)
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Langfuse Prompt Migration
- profile_extract_v1.md
- traces
- Langfuse Prompt Migration
- test_factory.py
- 2. Langfuse Documentation
- pytest
- profile_dependencies.py
- interviews_constants.py
- Implementation Steps
- interview-room/README.md
- _reset_request_id
- Implementation Plan: UUID primary keys
- RequestContextMiddleware
- test_log_context.py
- render_text
- Learn: Calling an LLM safely (Slice 1, interviewer reaction)
- Learn: Prompt registry (one place for prompt versions and routing)
- FeedbackService
- U0 baselines
- check_core
- Learn: Langfuse experiments for the interviews evals
- Learn: Layered architecture (route -> controller -> service -> repository)
- fixture
- test_me.py
- Clock
- ._covers_every_criterion
- ResumeRefusal
- .__init__

## God Nodes (most connected - your core abstractions)
1. `User` - 131 edges
2. `Tracer` - 123 edges
3. `FakeProvider` - 118 edges
4. `JobRole` - 114 edges
5. `LLMResult` - 107 edges
6. `Level` - 99 edges
7. `InterviewQuestion` - 97 edges
8. `InterviewType` - 95 edges
9. `QuestionCategory` - 89 edges
10. `LLMServerError` - 88 edges

## Surprising Connections (you probably didn't know these)
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `1. Why it exists` --references--> `DeepgramTranscriber`  [INFERRED]
  docs/features/interview-room/learnings.md → app/core/ai/deepgram.py
- `6. Try it yourself` --references--> `get_tracer()`  [INFERRED]
  docs/features/split-interviews-dependencies/learnings.md → app/core/ai/dependencies.py
- `Acceptance Criteria` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py

## Import Cycles
- None detected.

## Communities (326 total, 50 thin omitted)

### Community 0 - "interviews_utils.py"
Cohesion: 0.07
Nodes (43): interview_categories(), job_description_block(), load_rubric(), Path, Read and validate a feedback rubric file; a bad one fails loudly at startup,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the…, The question categories an interview of this type can hold (mixed: both). (+35 more)

### Community 1 - "LLMRateLimitError"
Cohesion: 0.12
Nodes (33): LLMRateLimitError, LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., parse_retry_after(), raise_for_status(), Map a vendor's HTTP status to the typed errors; 200 passes. `retry_after` is…, The Retry-After header as seconds. Only the delta-seconds form is read; an HTTP…, 7. What surprised me (+25 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.09
Nodes (50): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, _injection_share(), _mention_share(), notes_overlap() (+42 more)

### Community 3 - "decode_token"
Cohesion: 0.12
Nodes (31): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+23 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (54): analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start(), html_for() (+46 more)

### Community 5 - "AuthController"
Cohesion: 0.24
Nodes (14): AuthController, Request -> service call, domain result -> response schema., login(), me(), post, register(), LoginIn, MeOut (+6 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "Completed Steps"
Cohesion: 0.05
Nodes (66): Embedder, Protocol, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Step, log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as… (+58 more)

### Community 9 - "tests/conftest.py"
Cohesion: 0.04
Nodes (51): Deviations from Plan, Affected Files & Patterns, Testing Strategy, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: U1 structlog (structured JSON logs), Overview (+43 more)

### Community 10 - "WindowLedger"
Cohesion: 0.06
Nodes (44): StrategyOutput, build_context_manager(), FollowUpDecision, FullHistory, JobDescriptionSummary, A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, The decide call: the current thread in full (it judges the latest answer within… (+36 more)

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
Cohesion: 0.10
Nodes (34): ProviderConfig, One listed provider, resolved from its vendor block., _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url() (+26 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.10
Nodes (39): anyio_backend(), audio(), Clock, listen_body(), make_synthesizer(), _make(), make_transcriber(), _make() (+31 more)

### Community 16 - "test_feedback_contract.py"
Cohesion: 0.16
Nodes (36): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+28 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.10
Nodes (44): feedback_scores_for(), feedback_trace_output(), One case through the same pre-check, score call, write call and template…, What came out next to what was wanted: the verdict, the overall against its…, (name, value, comment) per check, plus `valid_reply` and `case_passed`. An…, run_feedback_case(), case(), Grader (+36 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (41): Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request, Response (+33 more)

### Community 19 - "User"
Cohesion: 0.09
Nodes (33): hash_password(), verify_password(), Role, get_controller(), get_service(), Session, User, AuthRepository (+25 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.14
Nodes (28): Data, PromptVersion, StrEnum, Every interviews prompt version, and which one each LLM call sends. Data only:…, What an interviewer write carries beyond the job description; it picks the…, Status, 5. What can go wrong, archived_routes() (+20 more)

### Community 26 - "interviews/conftest.py"
Cohesion: 0.05
Nodes (55): RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, Per-user caps on paid speech calls. One limiter instance per process: every…, get_speech_limiter(), get_transcription_limiter() (+47 more)

### Community 27 - "interviews_answer_service.py"
Cohesion: 0.05
Nodes (87): QuestionNotCurrentError, current_request_id(), log_stream_summary(), How a streamed turn felt and ended: time to the first event and to the first…, ActionKnown, Delta, PhaseChanged, NamedTuple (+79 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.05
Nodes (88): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists, 2. What it is, 3. When to use it (+80 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.07
Nodes (30): anyio, 5. What can go wrong, 6. Try it yourself, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing() (+22 more)

### Community 31 - "test_rag_evals.py"
Cohesion: 0.09
Nodes (44): build_sheet(), competencies_of(), filter_baseline(), Collection, Exception, _ranking(), _rating(), The grading file can't be read; the message starts with the line and gives the… (+36 more)

### Community 32 - "interviews_rag_evals.py"
Cohesion: 0.06
Nodes (55): _arm_notes(), ArmInterview, ArmSummary, case_set_problems(), ExtraSetup, generation_run_scores(), _generation_scores(), _is_short_items() (+47 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "check_prompts"
Cohesion: 0.19
Nodes (17): check_prompts(), PromptCheckError, Exception, One or more routed prompts cannot be sent; the message lists each one., Raises PromptCheckError naming every routed version whose file is missing or…, Known Issues, Skills Consulted During Implementation, loader() (+9 more)

### Community 35 - "pathlib"
Cohesion: 0.36
Nodes (10): pathlib, ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1(), test_an_invalid_note_names_the_file_writes_nothing_and_exits_1(), test_it_prints_the_counts_and_exits_0(), test_warnings_are_printed_without_note_text() (+2 more)

### Community 36 - "test_profile_read_resume.py"
Cohesion: 0.14
Nodes (38): make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), _clean(), NamedTuple, _read_docx(), _read_pdf(), read_resume() (+30 more)

### Community 37 - "4. How it works"
Cohesion: 0.07
Nodes (29): _decode(), FetchedPage, FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach… (+21 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "interviews_knowledge_utils.py"
Cohesion: 0.07
Nodes (53): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, cosine_similarity(), _hash(), _listed() (+45 more)

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
Cohesion: 0.15
Nodes (28): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+20 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.11
Nodes (33): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, Any network-side failure of a job link. One message for every cause, so…, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError (+25 more)

### Community 45 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Architecture & Design, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview (+6 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.12
Nodes (51): FakeProvider, LLMServerError, 5xx or a dropped connection: the provider's side failed., 5. What can go wrong, Deviations from Plan, decision(), hints_of(), labelled() (+43 more)

### Community 49 - "interviews_feedback.py"
Cohesion: 0.12
Nodes (31): _check_lengths(), Evidence, _has_markup(), _normalized(), parse_write_reply(), BaseModel, _question_score(), QuestionScore (+23 more)

### Community 50 - "QuestionCategory"
Cohesion: 0.11
Nodes (36): _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_interviewer_reply(), parse_streamed_reply(), BaseModel, NamedTuple (+28 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.10
Nodes (40): _counts(), InterviewerInputs, App data at the end of the last user message; untrusted parts (questions,…, Plain values for one interviewer or decide call., _status_block(), Decision, Interviewer, apply_limits() (+32 more)

### Community 52 - "ProfileService"
Cohesion: 0.08
Nodes (30): _out(), ProfileController, The signed-in user's résumé profile: request -> ProfileService, stored row ->…, CandidateProfileRow, A user's résumé profile: at most one per user (the unique user_id is the…, ProfileRepository, datetime, Session (+22 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (21): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+13 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.15
Nodes (36): 5. What can go wrong, fail(), error(), import_url(), _post(), long_posting(), page(), paste() (+28 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.09
Nodes (55): group_requests(), The events of each request, oldest request first (the id is on every line of…, analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table() (+47 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.15
Nodes (31): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_retry_after_longer_than_the_budget_fails_at_once_without_waiting(), test_a_smaller_budget_argument_caps_retries() (+23 more)

### Community 59 - "ReferenceNote"
Cohesion: 0.11
Nodes (29): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, A note an interview was given: what the question writer sees (competency and…, ReferenceNote, The interview's reference notes, fenced as data like the job description, most…, reference_notes_block(), Affected Files & Patterns, Architecture & Design (+21 more)

### Community 61 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 62 - "interviews_session_utils.py"
Cohesion: 0.08
Nodes (32): NotFoundError, SessionNotInProgressError, HistoryPage, InterviewsService, InterviewState, NamedTuple, UUID, Condense a long job description once, so later calls send less. One attempt… (+24 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "errors.py"
Cohesion: 0.08
Nodes (48): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody, FeedbackFailedError, FeedbackInProgressError (+40 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.10
Nodes (45): EmbedCall, FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, 1. Where 8a stands, competencies(), embedder_for() (+37 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.15
Nodes (33): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, test_a_redacted_stream_closed_early_records_no_partial_text(), test_stream_closed_early_is_warning_cancelled_with_partial_text(), collect() (+25 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (35): profile_json(), Synthetic résumé data and the scripted model shared by the profile tests (no…, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,…, Swagger UI builds its request from the OpenAPI schema. Declared as a url-… (+27 more)

### Community 68 - "test_reference_note_context.py"
Cohesion: 0.19
Nodes (19): 5. What can go wrong, first_user(), inputs(), _max_note(), anyio, parametrize, Reference notes in the question writer's input (knowledge-base-rag Step 9;…, test_a_follow_up_write_gets_no_notes_and_the_plain_prompt() (+11 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.08
Nodes (27): 2. What it is, Learning Log (`learnings.md`), 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+19 more)

### Community 71 - "run_generation"
Cohesion: 0.05
Nodes (78): ExperimentRun, NamedTuple, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit() (+70 more)

### Community 72 - "test_profile_context.py"
Cohesion: 0.17
Nodes (24): ContextReport, estimate_tokens(), _log(), NamedTuple, default_strategy(), everything(), fingerprint(), golden_inputs() (+16 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.19
Nodes (22): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+14 more)

### Community 74 - "interviews_feedback_evals.py"
Cohesion: 0.09
Nodes (33): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), check_feedback(), criterion_spread(), feedback_hints_for(), feedback_run_scores() (+25 more)

### Community 75 - "test_gateway.py"
Cohesion: 0.10
Nodes (34): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, 5. What can go wrong, anyio_backend() (+26 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues (+8 more)

### Community 77 - "parse_profile_reply"
Cohesion: 0.23
Nodes (19): fit(), parse_profile_reply(), Whitespace tidied, then cut to `max_length` on a word boundary (a single over-…, Tidied, blanks dropped, duplicates merged ignoring case (the first spelling…, _unique(), parametrize, parse_profile_reply: the model's JSON -> a capped, cleaned CandidateProfile, or…, reply() (+11 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "retry.py"
Cohesion: 0.08
Nodes (31): T, Attempted, backoff_seconds(), _elapsed_ms(), Random, T, Retry rules shared by every vendor client in `core/ai` (the LLM provider, the…, What one call returned, plus how many attempts and how long it took (for the… (+23 more)

### Community 81 - "interviews_evals.py"
Cohesion: 0.07
Nodes (57): anyio_from_thread, SummaryInputs, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, dataset_items(), dataset_name() (+49 more)

### Community 82 - "profile_service.py"
Cohesion: 0.09
Nodes (27): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, build_messages(), extract_profile(), Extraction (+19 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "FollowUpAction"
Cohesion: 0.22
Nodes (18): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect (+10 more)

### Community 85 - "pydantic"
Cohesion: 0.12
Nodes (20): Page, BaseModel, Offset pagination shared by every list endpoint, so clients see one query…, UsersController, get_controller(), get_service(), Depends, Session (+12 more)

### Community 86 - "OpenAICompatibleProvider"
Cohesion: 0.08
Nodes (20): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+12 more)

### Community 87 - "fake.py"
Cohesion: 0.08
Nodes (42): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, Test doubles for LLMProvider, Transcriber, SpeechSynthesizer and Embedder:… (+34 more)

### Community 88 - "Tracer"
Cohesion: 0.06
Nodes (43): build_tracer(), Send what is still buffered, then stop the background exporter. Called once at…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, Tracer, client(), drain(), FakeClient, FakeObservation (+35 more)

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
Cohesion: 0.22
Nodes (20): candidate_profile_block(), profile_query_text(), The candidate profile as interview input: a fenced prompt block and a short…, The profile fenced as data, like the job description. Summaries and…, The profile's short items as one retrieval query. None: nothing to embed., Project, Testing Strategy, _profile() (+12 more)

### Community 93 - "Implementation Steps"
Cohesion: 0.04
Nodes (65): _DeepgramAdapter, DeepgramSynthesizer, attempt(), DeepgramTranscriber, attempt(), _parse(), Any, AsyncBaseTransport (+57 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "LLMResult"
Cohesion: 0.05
Nodes (78): BuiltContext, Context management: the one place that decides what each LLM call sends. The…, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, ChatMessage, LLMError, LLMResult (+70 more)

### Community 97 - "InterviewType"
Cohesion: 0.13
Nodes (30): NotEnoughQuestionsError, InterviewType, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules (+22 more)

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
Cohesion: 0.09
Nodes (24): Review, test_any_other_speak_request_failure_is_a_server_error_not_a_crash(), test_every_configurable_encoding_has_a_media_type(), answered(), assert_hidden(), code(), fixture, GET /interviews/{id}/questions/{qid}/speech and /messages/{mid}/speech: the… (+16 more)

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "Role"
Cohesion: 0.16
Nodes (24): EmptyProfileError, Exception, No skills and no roles: not a résumé we can use (refused as unreadable, nothing…, Role, _appears(), ground_profile(), keep(), _normalized() (+16 more)

### Community 106 - "Settings"
Cohesion: 0.06
Nodes (26): model_validator, Self, Settings, BaseSettings, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview (+18 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "parse_log"
Cohesion: 0.11
Nodes (26): Call, _int(), _json_event(), LogEvent, parse_log(), NamedTuple, Reading the app's own log back: what each request did for an interview, from…, Old text lines: `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]).… (+18 more)

### Community 109 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 110 - "interview_report.py"
Cohesion: 0.15
Nodes (19): html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+11 more)

### Community 111 - "LLMProvider"
Cohesion: 0.08
Nodes (20): LLMProvider, Protocol, Random, Random, AI Engineering Upgrade Path (Cuewise), Build order, How to make it stick, Progress (+12 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "load_prompt"
Cohesion: 0.10
Nodes (34): _interviewer(), The startup prompt check: every routed prompt version loads and renders through…, _routed(), load_prompt(), An interviews prompt by version (cached; the startup check reads every routed…, Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt() (+26 more)

### Community 115 - "Implementation: Prompt Registry"
Cohesion: 0.13
Nodes (14): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Links (+6 more)

### Community 116 - "bind_log_context"
Cohesion: 0.13
Nodes (26): bind_log_context(), Any, Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything…, Makes `fields` (at least `request_id`) part of every log line inside the block., Adds fields to every later log line of the current request (or, outside a…, redact_sensitive(), _redacted(), request_log_context() (+18 more)

### Community 117 - "The fundamentals"
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+17 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 121 - "summarize"
Cohesion: 0.09
Nodes (26): A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), _print_summary(), The same one-off condensation the app makes at interview start; its tokens…, One run proves little (the same cases scored 5/6, then 6/6): look at the spread…, summarize() (+18 more)

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "profile_resume_files.py"
Cohesion: 0.12
Nodes (30): _content(), _escape(), _fill(), Image, make_pdf(), plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build…, A PDF with one page per list. `encrypt` adds a standard security handler whose… (+22 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+5 more)

### Community 125 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+7 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.14
Nodes (16): injection_ignored(), 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+8 more)

### Community 127 - "Feature: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Decisions, Edge Cases, Feature: Résumé-aware interview (Slice 8d), Functional, Goal, Known limits (+7 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "test_start_with_profile.py"
Cohesion: 0.21
Nodes (18): 5. What can go wrong, embedder(), first_question(), profile_of(), fixture, Starting an interview with the candidate's profile (resume-aware-interview Step…, A synthetic profile whose every free-text field carries `marker`, so a leak…, sent() (+10 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "profile_resume_utils.py"
Cohesion: 0.13
Nodes (27): _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _has_external_relationship(), _hex_lightness() (+19 more)

### Community 134 - "build_usage_report"
Cohesion: 0.19
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

### Community 140 - "get_logger"
Cohesion: 0.19
Nodes (18): get_logger(), Logger, parametrize, The logging pipeline (U1 structlog): what actually lands in the log file and on…, test_a_key_that_only_contains_a_sensitive_word_is_kept(), test_a_logged_exception_is_one_line_with_the_traceback(), test_a_nested_or_mixed_case_sensitive_key_is_masked(), test_a_sensitive_key_is_masked_in_the_file_and_on_the_console() (+10 more)

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.26
Nodes (20): active(), chunks(), corpus(), FailingOn, interview(), ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag…, Fails on the n-th embed call (1-based), then works again., rows() (+12 more)

### Community 143 - "ContextManager"
Cohesion: 0.11
Nodes (28): ContextManager, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., Task, Inputs, manager(), NamedTuple (+20 more)

### Community 144 - "test_feedback_context.py"
Cohesion: 0.25
Nodes (14): FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, Step 4 of the feedback plan: what the score and write calls send, through the…, score_inputs(), test_an_answer_over_the_cap_is_shortened_and_counted_but_quotes_still_verify(), test_an_interview_over_the_limit_raises_instead_of_dropping_an_answer(), test_closing_tags_inside_untrusted_text_are_neutralised(), test_tags_inside_quoted_text_are_neutralised_in_the_write_call() (+6 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): 5. What can go wrong, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 151 - "interviews_feedback_dependencies.py"
Cohesion: 0.08
Nodes (58): get_llm_provider(), get_tracer(), get_transcriber(), Request, Built once at startup (app lifespan); None when no key is configured or the…, Built once at startup (app lifespan); a disabled tracer when the lifespan…, Built once at startup (app lifespan); None when no Deepgram key is configured…, get_db() (+50 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "CandidateProfile"
Cohesion: 0.16
Nodes (23): CandidateProfile, BaseModel, The multipart upload: exactly one part, `file`. Extra form fields are refused., ResumeUploadIn, ExpectedProfile, _key(), ProfileScore, BaseModel (+15 more)

### Community 157 - "Implementation: Interview Room (backend)"
Cohesion: 0.12
Nodes (15): Changes Made, Current Step, Debug Log, Deviations from Plan, Done. Next: `/review-feature`, Implementation: Interview Room (backend), Known Issues, Links (+7 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (14): 9. Review gate (user), Baseline Failures, Changes Made, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions (+6 more)

### Community 159 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 160 - "follow_up"
Cohesion: 0.16
Nodes (13): Slice 3: Structured follow-up decisions, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+5 more)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.04
Nodes (56): AbstractContextManager, Generation, Any, The stream was closed before it finished (client left, or the turn's deadline…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Create the dataset if needed and upsert its items (each carries its own `id`,…, A named step inside the current trace (a Langfuse `chain`): the generations and… (+48 more)

### Community 162 - "4. How it works"
Cohesion: 0.15
Nodes (13): Response, UUID, The interview voice adapter, HTTP side: request -> VoiceService, domain result…, The clip with the media type the synthesizer reported, never a hardcoded one.…, VoiceController, POST /interviews/{id}/transcriptions: what the candidate said, for them to…, TranscriptionOut, NamedTuple (+5 more)

### Community 163 - "Implementation: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gate: Step 10, real-model runs (yours), Implementation: Résumé-aware interview (Slice 8d), Known Issues (+8 more)

### Community 164 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.11
Nodes (16): UUID, The user's stored profile for an interview prompt, read live (never copied onto…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me (+8 more)

### Community 165 - "test_answer_with_profile.py"
Cohesion: 0.25
Nodes (12): opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent(), test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile() (+4 more)

### Community 166 - "test_reaction_pick.py"
Cohesion: 0.23
Nodes (15): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), Random, A predefined, neutral acknowledgement for the answer just given; never the same…, pick(), parametrize, test_a_one_entry_pool_still_works() (+7 more)

### Community 167 - "llm"
Cohesion: 0.15
Nodes (12): Affected Files & Patterns, as_v5_text(), _decision_json(), llm(), script(), script_decide(), script_score(), script_write() (+4 more)

### Community 168 - "test_streamed_reply.py"
Cohesion: 0.18
Nodes (17): interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), read(), parse(), parametrize, interviewer_v5's streamed reply: a `CATEGORY:` header line (next-question mode…, test_a_header_split_across_chunks_is_read_once_its_line_ends(), test_a_long_first_line_is_no_header_without_waiting_for_its_end() (+9 more)

### Community 169 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 170 - "JobRole"
Cohesion: 0.12
Nodes (30): JobRole, Level, EvalSetup, FeedbackEvalSetup, ExtraSetupFields, One interview's main questions through the streamed writer's text format (the…, simulate_main_questions(), load_bank() (+22 more)

### Community 171 - "Implementation: U1 structlog (structured JSON logs)"
Cohesion: 0.12
Nodes (16): 7. Convert the remaining call sites (not started; waiting at the checkpoint), Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U1 structlog (structured JSON logs), Known Issues (+8 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.15
Nodes (16): Baseline Failures, Baseline Failures, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+8 more)

### Community 174 - "Feature: Interview History List (backend)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+6 more)

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
Cohesion: 0.07
Nodes (24): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Skills Consulted (+16 more)

### Community 179 - "failed"
Cohesion: 0.09
Nodes (29): Check, check_decision(), check_reply(), check_streamed_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format., The decide reply against the case's label; the injection check reads the raw… (+21 more)

### Community 180 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.14
Nodes (13): Assumptions to verify (external system behaviour), Blockers, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 181 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 182 - "audio_container"
Cohesion: 0.25
Nodes (14): audio_container(), AudioContainer, _has_signature(), StrEnum, Audio rules every speech feature shares: which recording containers are…, Recording containers an upload may arrive in (what browsers' MediaRecorder…, The container of an uploaded recording, or None when its declared type isn't…, enum (+6 more)

### Community 183 - "interviews_feedback_controller.py"
Cohesion: 0.18
Nodes (11): Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, FeedbackEvidenceOut (+3 more)

### Community 184 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 185 - "run_case"
Cohesion: 0.23
Nodes (16): run_case(), long_case(), noted(), reply(), test_a_passing_case_has_no_hints(), test_a_v3_window_reply_must_carry_a_note_when_there_is_an_answer(), test_an_unusable_summary_falls_back_to_the_original(), test_no_note_check_for_full_history_or_the_first_question() (+8 more)

### Community 186 - "load_prompt"
Cohesion: 0.24
Nodes (10): load_prompt(), Path, Prompt files: versioned Markdown read once per process. Feature modules pass…, `<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in…, functools, The shared prompt loader (prompt-registry AC9, EC13): one cached read per…, test_a_second_call_does_not_read_the_file_again(), test_an_unknown_version_raises_file_not_found_naming_the_path() (+2 more)

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
Nodes (52): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+44 more)

### Community 203 - "permissions_for"
Cohesion: 0.09
Nodes (29): ForbiddenError, permissions_for(), The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., get_current_user(), Depends, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, check(), require_roles() (+21 more)

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.15
Nodes (24): contextvars, A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and…, embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;… (+16 more)

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

### Community 234 - "setup_logging"
Cohesion: 0.15
Nodes (13): _formatter(), _json(), _json_renderer(), Path, Writes to whatever `sys.stderr` is at the time of the write (test runners and…, Routes every logger through the processor chain. Safe to call again (tests do):…, setup_logging(), _StderrHandler (+5 more)

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
Cohesion: 0.03
Nodes (49): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so… (+41 more)

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
Nodes (51): alias, AnswerControllerDep, Permission, StrEnum, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), get_job_url_limiter(), limit_job_imports() (+43 more)

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
Cohesion: 0.13
Nodes (17): _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), _plain(), _posting_text(), Turn a fetched job page into plain job-description text (Slice 8b). Pure…, A JSON-LD description is usually HTML, sometimes entity-escaped HTML: unescape,… (+9 more)

### Community 251 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 252 - "test_fallback_pick.py"
Cohesion: 0.21
Nodes (14): pick_fallback_question(), Collection, One unused bank question for `position`, used when the LLM is off or its reply…, fixture_bank(), pick(), fixture, parametrize, test_general_and_role_specific_questions_are_both_eligible() (+6 more)

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
Nodes (52): parse_arms(), Read your filled-in sheet, print how often each arm ranked first, then post…, `--arms`: comma-separated arm letters (any case), at least two (a ranking…, run_ranking(), argparse, parametrize, The generation eval's arms D and E (resume-aware-interview Step 9a; seam S5).…, A fake LLM that keeps every prompt, answering each main question with a new… (+44 more)

### Community 258 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 259 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 260 - "profile_evals.py"
Cohesion: 0.10
Nodes (31): pacer(), wait(), `wait()` sleeps `pause` seconds on every call but the first. Called before each…, build_file(), case_scores(), CaseResult, EvalCase, load_cases() (+23 more)

### Community 261 - "Learn: Résumé upload and the candidate profile (Slice 8c)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Résumé upload and the candidate profile (Slice 8c)

### Community 262 - "FakeLangfuse"
Cohesion: 0.09
Nodes (15): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+7 more)

### Community 263 - "test_request_context.py"
Cohesion: 0.09
Nodes (13): asyncio, fastapi_responses, anyio_backend(), _context_app(), stream(), anyio, fixture, parametrize (+5 more)

### Community 264 - "FeedbackThread"
Cohesion: 0.13
Nodes (17): FeedbackThread, NamedTuple, One main question with its follow-ups and every answer: what one set of scores…, ScoreResult, ThreadTurn, feedback_dataset_items(), FeedbackEvalCase, load_feedback_cases() (+9 more)

### Community 265 - "run_task"
Cohesion: 0.23
Nodes (14): console_number(), run_task(), test_a_failed_check_is_scored_false_with_its_detail(), test_a_write_result_shows_the_reply_and_the_notes_but_no_expected_action(), test_a_write_run_per_repeat_carries_what_produced_it(), test_each_case_shows_what_was_judged(), test_every_check_is_scored_on_each_write_case(), test_main_runs_the_streamed_task_and_prints_the_first_token() (+6 more)

### Community 266 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 267 - "Web"
Cohesion: 0.20
Nodes (5): fixture, Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 268 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 269 - "InterviewQuestion"
Cohesion: 0.04
Nodes (68): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, MessageRole, QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, A main question opens a thread; a follow-up digs into the latest answer of that…, InterviewMessage (+60 more)

### Community 270 - "main"
Cohesion: 0.15
Nodes (13): load_cases(), main(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, test_a_summarised_run_records_the_summary_prompt(), test_at_least_ten_shipped_cases_are_labelled_with_both_injections(), test_main_runs_every_case_n_times_and_prints_the_aggregate() (+5 more)

### Community 271 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 272 - "ReadableRenderer"
Cohesion: 0.26
Nodes (7): _default_request_id(), _merge_request_fields(), Dev console: time, level, short request id, logger, event, then one aligned…, ReadableRenderer, EventDict, test_the_readable_console_colours_outcome_by_success(), WrappedLogger

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
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 290 - "Implementation Steps"
Cohesion: 0.04
Nodes (50): done(), 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Streaming and latency (Slice 4, SSE) (+42 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "QuestionTurn"
Cohesion: 0.09
Nodes (31): An earlier question as the model would have written it. A follow-up was written…, build_interviewer_messages(), interviewer_history(), main_numbers(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, The main-question number of each turn: a follow-up shares the number of the… (+23 more)

### Community 293 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+2 more)

### Community 294 - "Implementation: Error Handling"
Cohesion: 0.18
Nodes (10): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+2 more)

### Community 295 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 296 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "profile_extract_v1.md"
Cohesion: 0.33
Nodes (5): Constraints, Input, Output, Role, Task

### Community 299 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 301 - "test_factory.py"
Cohesion: 0.07
Nodes (41): build_embedder(), build_provider(), build_synthesizer(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Text-to-speech for the interviewer's voice; None without a key (the interview…, Embeddings for reference-note retrieval; None without the Google key (notes are… (+33 more)

### Community 302 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 303 - "pytest"
Cohesion: 0.38
Nodes (6): pytest, parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 304 - "profile_dependencies.py"
Cohesion: 0.08
Nodes (31): Request dependencies for the AI services every feature shares, built once at…, BaseModel, Every speech setting in one read-only group, so the speech factories depend on…, Speech-to-text (voice answers)., Text-to-speech (the interviewer's voice)., The speech vendor's settings, grouped (see `Settings.speech`). One key and base…, _SpeechPart, SpeechSettings (+23 more)

### Community 305 - "interviews_constants.py"
Cohesion: 0.06
Nodes (59): page_params(), PageParams, NamedTuple, Query, HistorySortColumn, MessageKind, StrEnum, The history columns GET /interviews sorts by; the values are the response's… (+51 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 309 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 310 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 311 - "test_log_context.py"
Cohesion: 0.29
Nodes (9): fixture, Log context on real interview requests (U1 structlog, AC4): `session` and…, Every line of the one request whose access line ends with `path_end`., _request_lines(), started(), test_a_request_for_someone_elses_interview_logs_the_id_it_asked_for(), test_a_start_request_logs_the_new_session_and_the_user_on_every_line(), test_a_streamed_turn_logs_its_session_and_user_from_inside_the_stream() (+1 more)

### Community 312 - "render_text"
Cohesion: 0.28
Nodes (9): render_text(), lines_of(), The log file the real pipeline wrote: JSON lines, as `interview_report` reads…, Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis(), squash(), test_calls_logged_before_the_task_name_existed_fold_into_other_so_the_rows_add_up() (+1 more)

### Community 313 - "Learn: Calling an LLM safely (Slice 1, interviewer reaction)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 3. When to use it, 4. How it works, 5. What can go wrong, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Calling an LLM safely (Slice 1, interviewer reaction)

### Community 314 - "Learn: Prompt registry (one place for prompt versions and routing)"
Cohesion: 0.22
Nodes (8): 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Eval log (AI features only), Learn: Prompt registry (one place for prompt versions and routing)

### Community 315 - "FeedbackService"
Cohesion: 0.12
Nodes (19): FeedbackScoreInputs, FeedbackWrite, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, The write call: scores, evidence and question texts only; small whatever the…, _Claim (+11 more)

### Community 316 - "U0 baselines"
Cohesion: 0.25
Nodes (7): Before relying on this, Cost, Eval baselines, How to use this file, Live interviews (from `logs/app.log`, before U1), Prompts with no eval baseline (gaps), U0 baselines

### Community 317 - "check_core"
Cohesion: 0.25
Nodes (8): Skills Consulted During Implementation, check_core(), _imports(), Every `app/core` import of a feature module (`app.modules...`): core is shared…, (absolute module, imported names) per import statement; relative imports…, test_a_core_file_importing_a_feature_module_is_reported(), test_a_core_file_importing_only_core_and_libraries_is_clean(), test_the_real_core_imports_no_feature_module()

### Community 318 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 319 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository)

### Community 320 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 321 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 322 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 324 - "ResumeRefusal"
Cohesion: 0.50
Nodes (3): Exception, Why a file was refused; `reason` is short and machine-readable (logged, never…, ResumeRefusal

## Knowledge Gaps
- **1043 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+1038 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2481 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **50 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `decode_token`, `AuthController`, `tests/conftest.py`, `InterviewQuestion`, `interviews_feedback_dependencies.py`, `interviews/conftest.py`, `interviews_answer_service.py`, `4. How it works`, `interviews_job_url_service.py`, `profile_dependencies.py`, `interviews_constants.py`, `ProfileService`, `Implementation Plan: UUID primary keys`, `test_create_interview.py`, `interviews_feedback_controller.py`, `FeedbackService`, `interviews_session_utils.py`, `errors.py`, `permissions_for`, `profile_service.py`, `pydantic`, `LLMResult`, `Implementation: Langfuse Tracing`, `sqlalchemy`, `interviews_route.py`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Why does `LLMProvider` connect `LLMProvider` to `profile_evals.py`, `Cuewise BE — Project Instructions`, `InterviewQuestion`, `main`, `test_feedback_evals.py`, `interviews_feedback_dependencies.py`, `interviews_answer_service.py`, `interviews_rag_evals.py`, `Implementation Steps`, `JobRole`, `test_factory.py`, `profile_dependencies.py`, `QuestionCategory`, `InterviewerInputs`, `ProfileService`, `failed`, `run_case`, `FeedbackService`, `interviews_session_utils.py`, `errors.py`, `ErrorResponse`, `run_generation`, `interviews_feedback_evals.py`, `interviews_evals.py`, `profile_service.py`, `Implementation Steps`, `LLMResult`, `The fundamentals`, `Feature: Résumé upload and candidate profile (Slice 8c)`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `test_generation_eval.py`, `profile_evals.py`, `WindowLedger`, `test_job_description_summary.py`, `test_feedback_evals.py`, `test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`, `interviews_answer_service.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `test_factory.py`, `test_evals.py`, `QuestionCategory`, `InterviewerInputs`, `test_start_llm.py`, `test_openai_compatible_stream.py`, `run_case`, `FeedbackService`, `interviews_session_utils.py`, `test_answer_llm.py`, `interviews_feedback_evals.py`, `interviews_evals.py`, `profile_service.py`, `OpenAICompatibleProvider`, `fake.py`, `Tracer`, `LLMProvider`, `summarize`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Are the 51 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 41 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 41 INFERRED edges - model-reasoned connections that need verification._
- **Are the 30 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 30 INFERRED edges - model-reasoned connections that need verification._
- **Are the 69 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 69 INFERRED edges - model-reasoned connections that need verification._