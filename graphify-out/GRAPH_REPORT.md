# Graph Report - cuewise-be  (2026-11-26)

## Corpus Check
- 486 files · ~448,411 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 9 file(s) not represented in the graph (top: (none) 4, .example 1, .ini 1)

## Summary
- 6758 nodes · 18968 edges · 337 communities (291 shown, 46 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 3650 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3f3619f6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- FakeProvider
- test_retry.py
- interviews_profile_eval_metrics.py
- decode_token
- test_interview_report.py
- auth_service.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- interviews_rag_evals.py
- Implementation Plan: Start an Interview (backend)
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
- interviews/conftest.py
- AnswerService
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_rag_evals.py
- traced
- Feature: Context Management for the Interview LLM Calls
- check_prompts
- interviews_schema.py
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
- get_logger
- InterviewerInputs
- profile_service.py
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- InterviewQuestion
- test_openai_compatible.py
- test_profile_context.py
- test_tracing_routes.py
- test_context_controller.py
- Rules
- job_description_summary_v2.md
- errors.py
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- test_reference_note_context.py
- test_answer_llm.py
- run_generation
- Tracer
- exception_handlers.py
- interviews_feedback_evals.py
- test_gateway.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- InvalidReplyError
- Implementation: Start an Interview (backend)
- Langfuse
- Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)
- interviews_evals.py
- FakeTranscriber
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- FollowUpAction
- UsersService
- RetryPolicy
- LLMTimeoutError
- test_tracing.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- Project
- 4. How it works
- Langfuse Observability
- interviewer_v3.md
- interviews_constants.py
- InterviewType
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
- InterviewMessage
- interview_report.py
- test_retrieval_profile_cases.py
- Feature: Langfuse Tracing
- Langfuse
- JobRole
- Implementation: Prompt Registry
- app_logs
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- tests/conftest.py
- test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only
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
- test_generation_arms.py
- ChatMessage
- CandidateProfile
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- test_reply_contract.py
- ContextManager
- Implementation: Agentic Workflow v2
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- profile_evals.py
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- scrub_contacts
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- LLMServerError
- merge_note_rankings
- Learn: Résumé-aware interview (Slice 8d)
- test_answer_with_profile.py
- failed
- llm
- QuestionCategory
- hint_for
- FeedbackEvalCase
- ReplyAttempts
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Feature: Interview History List (backend)
- feedback_score_v1.md
- feedback_write_v1.md
- Implementation: Layered Modules (route -> controller -> service -> repository)
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- Slices in detail
- Feature: Langfuse experiments for the interviews evals
- Implementation: LLM as the Interviewer (it asks the questions)
- audio_container
- interviews_feedback_controller.py
- test_profile_eval_metrics.py
- FakeSynthesizer
- load_prompt
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Role-Based Access Control (single JWT)
- Implementation: Three New Interview Roles (designer, qa, devops)
- test_retrieval_eval.py
- Any
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
- Learn: Streaming and latency (Slice 4, SSE)
- Communication and priorities
- Engineering habits
- Senior judgement
- interviews_model.py
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- require_permissions
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- Implementation: Langfuse experiments for the interviews evals
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- interviews_job_url_utils.py
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- Slices in detail
- test_tracing_lifespan.py
- Feature: U1 structlog (structured JSON logs)
- Feature: Job URL (Slice 8b)
- test_generation_eval.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- test_answer_interview.py
- main
- Learn: Résumé upload and the candidate profile (Slice 8c)
- FakeLangfuse
- test_request_context.py
- Implementation Plan: Error Handling
- InterviewSession
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- test_transcript.py
- ._attempts
- InterviewsRepository
- Feature: Start an Interview (backend)
- test_job_description_summary.py
- setup_logging
- check_layers
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- Implementation Plan: Interview Room (backend)
- Implementation: Error Handling
- done
- Langfuse Observability
- QuestionTurn
- Learn: Splitting the interviews dependency wiring
- Affected Files & Patterns
- FakeClient
- Implementation: Eval runs in Langfuse (scores + datasets)
- Langfuse Prompt Migration
- profile_extract_v1.md
- .speech
- Langfuse Prompt Migration
- test_factory.py
- ErrorResponse
- pytest
- AI Engineering Learning Path (Cuewise)
- interviews_route.py
- Implementation Steps
- interview-room/README.md
- Implementation Plan: Follow-up Questions (decide / write split)
- test_context.py
- test_list_users.py
- test_log_context.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- Learn: one retry policy on tenacity, and why reply retries stay out of it (U2)
- interviews_feedback_service.py
- U0 baselines
- check_core
- test_eval_runs.py
- Learn: Layered architecture (route -> controller -> service -> repository)
- Implementation Steps
- test_create_admin.py
- Implementation Plan: Context Management for the Interview LLM Calls
- RubricCriterion
- bank
- Learn: Prompt registry (one place for prompt versions and routing)
- lf
- RecordingClient
- Web
- guard_verdict
- db
- ContextTooLargeError
- _profile_scores
- notes_overlap
- experiments
- _Usage
- started

## God Nodes (most connected - your core abstractions)
1. `User` - 131 edges
2. `Tracer` - 125 edges
3. `FakeProvider` - 121 edges
4. `JobRole` - 118 edges
5. `LLMResult` - 108 edges
6. `LLMServerError` - 106 edges
7. `Level` - 103 edges
8. `InterviewType` - 99 edges
9. `InterviewQuestion` - 97 edges
10. `LLMError` - 93 edges

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

## Communities (337 total, 46 thin omitted)

### Community 0 - "FakeProvider"
Cohesion: 0.12
Nodes (40): FakeProvider, 5. What can go wrong, Deviations from Plan, Reply, decision(), hints_of(), labelled_cases(), last_line() (+32 more)

### Community 1 - "test_retry.py"
Cohesion: 0.14
Nodes (42): anyio_lowlevel, LLMRateLimitError, 5. What can go wrong, anyio_backend(), Clock, fields(), make_policy(), anyio (+34 more)

### Community 2 - "interviews_profile_eval_metrics.py"
Cohesion: 0.21
Nodes (18): ArmProfileSummary, GuardVerdict, _injection_share(), _mention_share(), profile_summary(), ProfileRow, NamedTuple, Pure metrics of the résumé-aware generation eval (resume-aware-interview, arms… (+10 more)

### Community 3 - "decode_token"
Cohesion: 0.07
Nodes (45): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, Affected Files & Patterns, Blockers & Resolutions (+37 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.08
Nodes (80): bind_log_context(), Adds fields to every later log line of the current request (or, outside a…, log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, render_text(), main(), Session, add_session() (+72 more)

### Community 5 - "auth_service.py"
Cohesion: 0.08
Nodes (34): hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), get_service(), Depends, Session (+26 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "interviews_rag_evals.py"
Cohesion: 0.04
Nodes (82): Embedder, Protocol, ProfileRequiredError, An interview asked to use the candidate's profile, and there is none to use…, log_retrieval(), Which reference notes an interview got at start: mode, count, scores, how many…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as… (+74 more)

### Community 9 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.08
Nodes (30): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+22 more)

### Community 10 - "WithInterviewData"
Cohesion: 0.06
Nodes (41): build_context_manager(), FullHistory, A main-question write that carries the interview's own data: reference notes…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WithInterviewData, The labelled text the write call is asked for (the parser reads it back…, 1. Why it exists, 2. What it is (+33 more)

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
Nodes (43): ProviderConfig, One listed provider, resolved from its vendor block., _google(), no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture (+35 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.09
Nodes (43): Review, anyio_backend(), audio(), Clock, listen_body(), make_synthesizer(), _make(), make_transcriber() (+35 more)

### Community 16 - "test_feedback_contract.py"
Cohesion: 0.12
Nodes (42): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 1. Why it exists, 2. What it is (+34 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.12
Nodes (36): One case through the same pre-check, score call, write call and template…, run_feedback_case(), case(), Grader, Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The…, A fake provider: scores every criterion `value`, quoting the start of each…, _result(), run_main() (+28 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.12
Nodes (44): Refused before connecting, or the network side failed (DNS, timeout,…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError, UrlUnreachableError, Deviations found during implementation (2026-11-13), FakeResolver, fetcher(), public() (+36 more)

### Community 19 - "User"
Cohesion: 0.06
Nodes (52): attempt(), T, get_synthesizer(), Built once at startup (app lifespan); None when no Deepgram key is configured…, Attempted, What one call returned, plus how many attempts and how long it took (for the…, Protocol, SpeechSynthesizer (+44 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.14
Nodes (27): Data, PromptVersion, StrEnum, What an interviewer write carries beyond the job description; it picks the…, Status, 5. What can go wrong, archived_routes(), catalog_mismatches() (+19 more)

### Community 26 - "interviews/conftest.py"
Cohesion: 0.05
Nodes (44): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, Per-user caps on paid speech calls. One limiter instance per process: every…, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window() (+36 more)

### Community 27 - "AnswerService"
Cohesion: 0.06
Nodes (43): QuestionNotCurrentError, AnswerController, UUID, The checks and reads before the stream opens (sync DB work: the route runs it…, Reload rows a commit expired, so reading their fields later needs no database…, AnswerIn, AnswerOut, AnswerService (+35 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.11
Nodes (60): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, 5. What can go wrong, fresh_limiter(), happy(), interview() (+52 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.09
Nodes (16): assert_one_terminal(), follow_up_json(), message_count(), parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, test_a_completed_session_is_a_json_409(), test_a_follow_up_streams_no_reaction(), test_a_follow_up_that_falls_back_sends_its_reaction_only_in_done() (+8 more)

### Community 31 - "test_rag_evals.py"
Cohesion: 0.13
Nodes (28): build_sheet(), Exception, _ranking(), _rating(), The grading file can't be read; the message starts with the line and gives the…, One interview's keyword scores, for its Langfuse trace: the same rules the arm…, One block per setup with each arm's question set under a neutral label in a…, Every setup of the key must have one complete ranking; anything else, and any… (+20 more)

### Community 32 - "traced"
Cohesion: 0.15
Nodes (22): drain(), result(), test_a_redacted_call_records_a_placeholder_instead_of_the_messages(), test_a_redacted_failure_records_no_partial_text(), test_a_redacted_stream_closed_early_records_no_partial_text(), test_a_redacted_success_keeps_model_usage_and_labels_but_not_the_reply(), test_an_unlabelled_call_still_records_full_content(), test_call_without_labels_still_gets_a_name() (+14 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "check_prompts"
Cohesion: 0.21
Nodes (16): check_prompts(), PromptCheckError, Exception, One or more routed prompts cannot be sent; the message lists each one., Raises PromptCheckError naming every routed version whose file is missing or…, 4. How it works, loader(), load() (+8 more)

### Community 35 - "interviews_schema.py"
Cohesion: 0.10
Nodes (40): PhaseChanged, The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), _error_event(), _event(), _frame(), AnswerEvent (+32 more)

### Community 36 - "test_profile_read_resume.py"
Cohesion: 0.17
Nodes (30): make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), read_resume(), ResumeUnreadableRefusal, ResumeUnsupportedRefusal, Run, parametrize (+22 more)

### Community 37 - "4. How it works"
Cohesion: 0.07
Nodes (29): _decode(), FetchedPage, FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach… (+21 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 39 - "interviews_knowledge_utils.py"
Cohesion: 0.04
Nodes (83): log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, InterviewSessionChunk, KnowledgeChunkScope, One (role, level) a chunk applies to. Rows instead of array columns, so the…, A reference note one interview was given at start: the same notes for every… (+75 more)

### Community 40 - "test_layers.py"
Cohesion: 0.32
Nodes (11): ast, 5. What can go wrong, _one(), The layer rules of app/modules (CLAUDE.md, "Architecture"): route -> controller…, test_a_feature_importing_another_features_repository_is_reported(), test_a_layer_file_left_at_a_module_root_is_reported(), test_controller_importing_a_repository_the_llm_or_the_db_session_is_reported(), test_repository_importing_a_service_controller_or_route_is_reported() (+3 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues, Links (+7 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.15
Nodes (25): _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card(), _html_metric_row(), _html_table() (+17 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.13
Nodes (26): JobTextUnreadableError, A pasted page held no job description (too little text, or not recognisably a…, JobTextFormat, Which clipboard copy the client sent: the HTML one when the browser has it (its…, JobUrlController, Job posting links and pasted pages: request -> JobUrlService, job text ->…, get_job_url_controller(), get_job_url_service() (+18 more)

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
Cohesion: 0.12
Nodes (41): load_cases(), Path, run_case(), console_number(), long_case(), noted(), reply(), run_task() (+33 more)

### Community 49 - "interviews_feedback.py"
Cohesion: 0.08
Nodes (53): FeedbackScore, FeedbackScoreInputs, Plain values for the score call: the whole interview, read once the interview…, The score call: every thread whole, nothing droppable. Over its own limit it…, _check_lengths(), Evidence, FeedbackThread, _has_markup() (+45 more)

### Community 50 - "get_logger"
Cohesion: 0.11
Nodes (34): get_logger(), Logger, log_stream_summary(), How a streamed turn felt and ended: time to the first event and to the first…, 5. What can go wrong, structlog, parametrize, The logging pipeline (U1 structlog): what actually lands in the log file and on… (+26 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.09
Nodes (50): InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, Deadline, _decision_label(), plan_write(), UUID (+42 more)

### Community 52 - "profile_service.py"
Cohesion: 0.05
Nodes (53): ProfileExtractionFailedError, ProfileNotFoundError, ProfileUnavailableError, Over the byte, page or unzipped-size limit of a résumé upload., Encrypted, corrupt, scanned, too little text, or no usable profile in it., The model gave no valid profile after the retry, timed out, or the provider…, ResumeTooLargeError, ResumeUnreadableError (+45 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (21): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+13 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.12
Nodes (41): 5. What can go wrong, auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, fail(), error(), import_url(), _post() (+33 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.11
Nodes (34): Review, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok() (+26 more)

### Community 57 - "InterviewQuestion"
Cohesion: 0.06
Nodes (78): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, A main question opens a thread; a follow-up digs into the latest answer of that…, InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank… (+70 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (37): Deviations from Plan, busy(), Clock, completion(), make_provider(), fixture, parametrize, Response (+29 more)

### Community 59 - "test_profile_context.py"
Cohesion: 0.20
Nodes (23): estimate_tokens(), default_strategy(), everything(), fingerprint(), golden_inputs(), inputs(), manager_for(), max_profile() (+15 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

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
Cohesion: 0.12
Nodes (35): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody, InvalidCredentialsError, JobUrlUnreachableError (+27 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.07
Nodes (71): EmbedCall, FakeEmbedder, NamedTuple, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, active(), chunks() (+63 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.16
Nodes (34): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase (+26 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (36): 5. What can go wrong, profile_json(), resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,…, Swagger UI builds its request from the OpenAPI schema. Declared as a url-… (+28 more)

### Community 68 - "test_reference_note_context.py"
Cohesion: 0.13
Nodes (26): Task, An earlier question as the model would have written it. A follow-up was written…, WindowLedger, Affected Files & Patterns, 5. What can go wrong, test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), manager() (+18 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.14
Nodes (17): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview() (+9 more)

### Community 71 - "run_generation"
Cohesion: 0.11
Nodes (25): ArmInterview, generation_item(), generation_run_scores(), _generation_scores(), _print_profile_summary(), Any, Namespace, Score (+17 more)

### Community 72 - "Tracer"
Cohesion: 0.06
Nodes (32): LLMProvider, Protocol, Send what is still buffered, then stop the background exporter. Called once at…, Tracer, TracingProvider, FeedbackGenerator, Save one whole turn in one commit: advance the session, the answer, the…, Random (+24 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.16
Nodes (25): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, BaseException, Exception (+17 more)

### Community 74 - "interviews_feedback_evals.py"
Cohesion: 0.11
Nodes (37): criterion_spread(), feedback_hints_for(), feedback_run_scores(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult, FeedbackEvalQuestion, FeedbackEvalTurn (+29 more)

### Community 75 - "test_gateway.py"
Cohesion: 0.15
Nodes (26): anyio_backend(), _Broken, code_of(), fixture, parametrize, The speech gateway: the generic half of every speech call (checks, vendor…, A vendor adapter with a bug: it raises something that isn't an LLMError., stt_lines() (+18 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues (+8 more)

### Community 77 - "InvalidReplyError"
Cohesion: 0.13
Nodes (30): InvalidReplyError, load_object(), Exception, The reply as a JSON object: one optional fence around it, nothing else before…, fit(), parse_profile_reply(), BaseModel, The contract for the profile-extraction reply, and the check that enforces it.… (+22 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)

### Community 81 - "interviews_evals.py"
Cohesion: 0.07
Nodes (57): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, dataset_items(), dataset_name(), DecisionSummary (+49 more)

### Community 82 - "FakeTranscriber"
Cohesion: 0.14
Nodes (11): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, test_a_transcription_fills_every_result_field(), The speech-to-text seam of a test: a scripted transcriber and a fresh per-test… (+3 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+6 more)

### Community 84 - "FollowUpAction"
Cohesion: 0.15
Nodes (24): parse_decision_reply(), BaseModel, The decide call suggests; the code still applies the follow-up cap and the time…, A follow-up carries no category: it inherits its main question's, so the model…, _RawDecision, _RawFollowUp, _RawReply, FollowUpAction (+16 more)

### Community 85 - "UsersService"
Cohesion: 0.17
Nodes (11): UsersController, get_controller(), get_service(), Depends, Session, Session, UsersRepository, BaseModel (+3 more)

### Community 86 - "RetryPolicy"
Cohesion: 0.05
Nodes (53): BaseTransport, AsyncBaseTransport, BaseTransport, _Call, parse_retry_after(), Logger, T, The same rules for an async attempt; waits are awaited, so the event loop stays… (+45 more)

### Community 87 - "LLMTimeoutError"
Cohesion: 0.05
Nodes (62): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, GoogleEmbedder (+54 more)

### Community 88 - "test_tracing.py"
Cohesion: 0.10
Nodes (12): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, client(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, _settings(), test_both_keys_build_an_enabled_tracer() (+4 more)

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
Nodes (19): candidate_profile_block(), The profile fenced as data, like the job description. Summaries and…, Project, BaseModel, The multipart upload: exactly one part, `file`. Extra form fields are refused., ResumeUploadIn, _profile(), resume-aware-interview Step 2 (seam S1): the profile as prompt text and as… (+11 more)

### Community 93 - "4. How it works"
Cohesion: 0.09
Nodes (25): decide_run_scores(), interviewer_prompt_version(), The run-level numbers of a decide run, from the same summaries the console…, The interviewer prompt a write or stream run actually used: `--prompt` for the…, load_generation_profiles(), load_profile_eval_data(), _post_judgements(), ProfileEvalData (+17 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "interviews_constants.py"
Cohesion: 0.05
Nodes (94): anyio, BuiltContext, ContextReport, _log(), NamedTuple, Context management: the one place that decides what each LLM call sends. The…, Test doubles for LLMProvider, Transcriber, SpeechSynthesizer and Embedder:…, Reading a model's JSON reply: one optional ```json fence around one JSON… (+86 more)

### Community 97 - "InterviewType"
Cohesion: 0.13
Nodes (35): NotEnoughQuestionsError, InterviewType, pick_fallback_question(), Collection, One unused bank question for `position`, used when the LLM is off or its reply…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Architecture & Design (+27 more)

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

### Community 103 - "test_speech.py"
Cohesion: 0.10
Nodes (23): 5. What can go wrong, answered(), assert_hidden(), code(), fixture, parametrize, GET /interviews/{id}/questions/{qid}/speech and /messages/{mid}/speech: the…, An owner with a started backend interview: (owner, session_id, first question). (+15 more)

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "Role"
Cohesion: 0.18
Nodes (22): EmptyProfileError, Exception, No skills and no roles: not a résumé we can use (refused as unreadable, nothing…, Role, _appears(), ground_profile(), keep(), _normalized() (+14 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+1 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "parse_log"
Cohesion: 0.10
Nodes (29): _json_event(), LogEvent, parse_log(), Reading the app's own log back: what each request did for an interview, from…, Old text lines: `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]).…, Reads both log formats, so a log that rotated mid-change (`app.log.1` text,…, _split_fields(), _text() (+21 more)

### Community 109 - "InterviewMessage"
Cohesion: 0.12
Nodes (19): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_a_future_question_is_not_current_either() (+11 more)

### Community 110 - "interview_report.py"
Cohesion: 0.25
Nodes (8): html_target(), Path, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines(), test_the_script_reads_the_rotated_log_before_the_current_one()

### Community 111 - "test_retrieval_profile_cases.py"
Cohesion: 0.14
Nodes (24): case_set_problems(), ExtraSetup, _is_short_items(), _print_retrieval_row(), BaseModel, A generation-only setup, run with arm D or E: the injection and the mismatch…, One retrieval case's outcome: the ranking by meaning and its metrics, the…, The run's averages, as the console prints them: an errored case counts as a… (+16 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "JobRole"
Cohesion: 0.06
Nodes (69): JobRole, Level, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, EvalSetup, FeedbackEvalSetup, ExtraSetupFields, One interview's main questions through the streamed writer's text format (the… (+61 more)

### Community 115 - "Implementation: Prompt Registry"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Known Issues (+8 more)

### Community 116 - "app_logs"
Cohesion: 0.06
Nodes (30): current_request_id(), Completed Steps, Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: U1 structlog (structured JSON logs), Overview (+22 more)

### Community 117 - "The fundamentals"
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "tests/conftest.py"
Cohesion: 0.07
Nodes (36): health_check(), list_users(), PageDep, CurrentUserDep, Affected Files & Patterns, sqlalchemy_pool, tempfile, make_user() (+28 more)

### Community 121 - "test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only"
Cohesion: 0.11
Nodes (21): Baseline Failures, Known Issues, Baseline Failures, Testing Strategy, 15. Evals, fault check and graph, Baseline Failures, Changes Made, Completed Steps (+13 more)

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "profile_resume_files.py"
Cohesion: 0.11
Nodes (33): build_file(), The case as the file a candidate would upload. Hidden lines are white (PDF) or…, _content(), _escape(), _fill(), Image, make_pdf(), plain_zip() (+25 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

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
Cohesion: 0.10
Nodes (37): _clean(), _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _has_external_relationship() (+29 more)

### Community 134 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

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
Cohesion: 0.18
Nodes (10): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Goal, Out of Scope, Problem (+2 more)

### Community 142 - "test_generation_arms.py"
Cohesion: 0.13
Nodes (19): parse_arms(), `--arms`: comma-separated arm letters (any case), at least two (a ranking…, parametrize, The generation eval's arms D and E (resume-aware-interview Step 9a; seam S5).…, A fake LLM that keeps every prompt, answering each main question with a new…, RecordingWriter, run(), test_a_ranking_must_name_every_label_of_its_setup() (+11 more)

### Community 143 - "ChatMessage"
Cohesion: 0.05
Nodes (40): StrategyOutput, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, One turn of the conversation sent to the model. The model keeps no memory:… (+32 more)

### Community 144 - "CandidateProfile"
Cohesion: 0.22
Nodes (18): CandidateProfile, ExpectedProfile, _key(), ProfileScore, BaseModel, NamedTuple, Scoring an extracted profile against a hand-labelled synthetic résumé (resume-…, score_profile() (+10 more)

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

### Community 150 - "test_reply_contract.py"
Cohesion: 0.06
Nodes (64): apply_limits(), The code's say over the model's: returns the action and why it overrode the…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+56 more)

### Community 151 - "ContextManager"
Cohesion: 0.09
Nodes (58): ContextManager, get_llm_provider(), get_tracer(), get_transcriber(), Request, Request dependencies for the AI services every feature shares, built once at…, Built once at startup (app lifespan); None when no key is configured or the…, Built once at startup (app lifespan); a disabled tracer when the lifespan… (+50 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.11
Nodes (32): get_embedder(), Request, Built once at startup (app lifespan); None without the Google key or when the…, profile_query_text(), The candidate profile as interview input: a fenced prompt block and a short…, The profile's short items as one retrieval query. None: nothing to embed., embedder(), has_notes() (+24 more)

### Community 156 - "profile_evals.py"
Cohesion: 0.08
Nodes (34): pacer(), wait(), Local time, as the Langfuse list shows the run's start: the name and the…, `wait()` sleeps `pause` seconds on every call but the first. Called before each…, run_stamp(), extract_profile(), Extraction, ExtractionFailedError (+26 more)

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
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+2 more)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.06
Nodes (37): One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Run an SDK call; on any failure log what failed (not why: the message could…, _safe(), decorate(), Affected Files & Patterns (+29 more)

### Community 162 - "LLMServerError"
Cohesion: 0.06
Nodes (29): _DeepgramAdapter, _parse(), Any, AsyncBaseTransport, Response, The first channel's best transcript (blank for silence) and the reported audio…, What both Deepgram adapters share: one authenticated client, the retry policy…, One POST that never waits past the total budget; a non-2xx or failed request… (+21 more)

### Community 163 - "merge_note_rankings"
Cohesion: 0.07
Nodes (41): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, Architecture & Design, Blockers & Resolutions, Decisions (grill-me, 2026-11-14), Deviations during implementation (2026-11-14, see task.md), Implementation Plan: Résumé-aware interview (Slice 8d), Overview (+33 more)

### Community 164 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.14
Nodes (13): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+5 more)

### Community 165 - "test_answer_with_profile.py"
Cohesion: 0.25
Nodes (12): opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent(), test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile() (+4 more)

### Community 166 - "failed"
Cohesion: 0.15
Nodes (19): Check, check_decision(), check_reply(), check_streamed_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format., The decide reply against the case's label; the injection check reads the raw… (+11 more)

### Community 167 - "llm"
Cohesion: 0.15
Nodes (11): Functional, Non-Functional, Requirements, as_v5_text(), llm(), script(), script_score(), script_write() (+3 more)

### Community 168 - "QuestionCategory"
Cohesion: 0.09
Nodes (44): _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_interviewer_reply(), parse_streamed_reply(), NamedTuple, interviewer_v5's finished question text, checked like a v4 reply. It was… (+36 more)

### Community 169 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 170 - "FeedbackEvalCase"
Cohesion: 0.12
Nodes (15): Band, _band_check(), check_feedback(), feedback_dataset_items(), FeedbackEvalCase, load_feedback_cases(), model_validator, Path (+7 more)

### Community 171 - "ReplyAttempts"
Cohesion: 0.13
Nodes (18): Iterate to get `(attempt, seconds_left)` for each reply attempt that may start.…, ReplyAttempts, asyncio, An extra set of runs (not used for the verdict), Failures, Scores, Still to do, U2 (tenacity) vs. the U0 baseline (+10 more)

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
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 179 - "Slices in detail"
Cohesion: 0.14
Nodes (13): AI Engineering Upgrade Path (Cuewise), Build order, How to make it stick, Progress, Slices in detail, U0: Baselines, U1: structlog, U4: Prompt templates + Langfuse Prompt Management (+5 more)

### Community 180 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.13
Nodes (14): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional (+6 more)

### Community 181 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 182 - "audio_container"
Cohesion: 0.28
Nodes (13): audio_container(), AudioContainer, _has_signature(), StrEnum, Audio rules every speech feature shares: which recording containers are…, Recording containers an upload may arrive in (what browsers' MediaRecorder…, The container of an uploaded recording, or None when its declared type isn't…, parametrize (+5 more)

### Community 183 - "interviews_feedback_controller.py"
Cohesion: 0.10
Nodes (23): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, get_feedback_controller(), FeedbackEvidenceOut (+15 more)

### Community 184 - "test_profile_eval_metrics.py"
Cohesion: 0.18
Nodes (17): coverage_spread(), profile_mentions(), profile_only_items(), profile_only_mention_share(), `item` as a whole term, case-insensitive. Lookarounds instead of \\b, so items…, The profile's short items the job description does not name (all of them when…, _whole(), profile_items() (+9 more)

### Community 185 - "FakeSynthesizer"
Cohesion: 0.15
Nodes (10): FakeSynthesizer, Scripted clips (bytes, a full result, or an error), one per call; records each…, BaseModel, One spoken clip. `content_type` is what the vendor says the audio is: the…, `text` spoken in the configured voice, as one whole clip., SynthesisResult, test_a_synthesis_fills_every_result_field(), The text-to-speech seam of a test: a scripted synthesizer and a fresh per-test… (+2 more)

### Community 186 - "load_prompt"
Cohesion: 0.33
Nodes (8): load_prompt(), Path, `<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in…, The shared prompt loader (prompt-registry AC9, EC13): one cached read per…, test_a_second_call_does_not_read_the_file_again(), test_an_unknown_version_raises_file_not_found_naming_the_path(), test_returns_the_text_of_the_versioned_file(), test_the_same_version_in_two_directories_gives_two_texts()

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

### Community 193 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional (+5 more)

### Community 203 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (11): Blockers, Constraints, Edge Cases, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.15
Nodes (25): notes_fingerprint(), A short id for the ingested notes: changes when any note changes, not when the…, Rank the notes for every labelled query and score where the right note landed,…, run_retrieval(), embedder(), labelled(), lf(), fixture (+17 more)

### Community 220 - "Any"
Cohesion: 0.10
Nodes (14): AbstractContextManager, Generation, Any, The stream was closed before it finished (client left, or the turn's deadline…, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the… (+6 more)

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

### Community 234 - "Learn: Streaming and latency (Slice 4, SSE)"
Cohesion: 0.12
Nodes (16): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+8 more)

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "interviews_model.py"
Cohesion: 0.03
Nodes (55): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so… (+47 more)

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

### Community 244 - "require_permissions"
Cohesion: 0.07
Nodes (59): AnswerControllerDep, ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, get_current_user() (+51 more)

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

### Community 252 - "Slices in detail"
Cohesion: 0.12
Nodes (17): 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety (+9 more)

### Community 253 - "test_tracing_lifespan.py"
Cohesion: 0.20
Nodes (7): fastapi_testclient, The app lifespan runs the prompt check before anything else (prompt-registry…, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

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

### Community 260 - "main"
Cohesion: 0.15
Nodes (15): main(), _non_negative_seconds(), _parser(), pause_for(), _positive(), ArgumentParser, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, parametrize (+7 more)

### Community 261 - "Learn: Résumé upload and the candidate profile (Slice 8c)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Résumé upload and the candidate profile (Slice 8c)

### Community 262 - "FakeLangfuse"
Cohesion: 0.09
Nodes (16): User Flow, experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input() (+8 more)

### Community 263 - "test_request_context.py"
Cohesion: 0.07
Nodes (19): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, fastapi_responses, Receive, Scope, Send (+11 more)

### Community 264 - "Implementation Plan: Error Handling"
Cohesion: 0.14
Nodes (13): open_stream(), Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+5 more)

### Community 265 - "InterviewSession"
Cohesion: 0.29
Nodes (12): InterviewSession, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing(), test_the_first_event_is_sent_before_any_llm_call_returns() (+4 more)

### Community 266 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 267 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 268 - "._attempts"
Cohesion: 0.22
Nodes (10): attempt(), _Attempts, NamedTuple, T, UUID, At most two attempts; a retry only for a reply that came back but broke the…, At most two attempts of the write call only. Failing is fine: the template…, Scored (+2 more)

### Community 269 - "InterviewsRepository"
Cohesion: 0.11
Nodes (12): InterviewsRepository, Any, datetime, Session, UUID, An interviewer reaction of this session; None for a candidate answer or another…, Any user's session, by id: for the report script only (the API always goes…, The first claim of an interview's feedback. False when another request inserted… (+4 more)

### Community 270 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 271 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 272 - "setup_logging"
Cohesion: 0.06
Nodes (33): _default_request_id(), _formatter(), _json(), _json_renderer(), _merge_request_fields(), Any, Path, Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything… (+25 more)

### Community 273 - "check_layers"
Cohesion: 0.33
Nodes (6): Blockers & Resolutions, Known Issues, check_layers(), Every layer-rule violation in `files` (repo-relative path -> source), as…, test_clean_layer_imports_have_no_violations(), _violation()

### Community 274 - "Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 275 - "Implementation Plan: Agentic Workflow v2"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: Agentic Workflow v2, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 276 - "Implementation Plan: Interview Room (backend)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Blockers & Resolutions, Implementation Plan: Interview Room (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 277 - "Implementation: Error Handling"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 290 - "done"
Cohesion: 0.15
Nodes (15): done(), Deviations from Plan, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal (+7 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "QuestionTurn"
Cohesion: 0.07
Nodes (48): A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), MessageRole, Every stored question, grouped by interview in creation order (UUIDv7), for the…, build_interviewer_messages(), interviewer_history() (+40 more)

### Community 293 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+2 more)

### Community 294 - "Affected Files & Patterns"
Cohesion: 0.33
Nodes (5): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns

### Community 295 - "FakeClient"
Cohesion: 0.10
Nodes (10): FakeClient, FakeObservation, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_reports_whether_it_was_sent(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises(), test_steps_and_checks_are_no_ops_when_off_and_never_raise_when_langfuse_fails(), test_trace_with_a_broken_sdk_still_runs_the_body_and_keeps_its_exception() (+2 more)

### Community 296 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "profile_extract_v1.md"
Cohesion: 0.40
Nodes (4): Constraints, Input, Role, Task

### Community 299 - ".speech"
Cohesion: 0.22
Nodes (10): BaseModel, Every speech setting in one read-only group, so the speech factories depend on…, Speech-to-text (voice answers)., Text-to-speech (the interviewer's voice)., The speech vendor's settings, grouped (see `Settings.speech`). One key and base…, _SpeechPart, SpeechSettings, SttSettings (+2 more)

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 301 - "test_factory.py"
Cohesion: 0.04
Nodes (75): DeepgramSynthesizer, DeepgramTranscriber, Deepgram over plain httpx: pre-recorded speech-to-text (`POST /v1/listen`, Nova…, Aura text-to-speech: the text goes in a JSON body, the voice (`model`) and…, build_embedder(), build_provider(), build_synthesizer(), build_transcriber() (+67 more)

### Community 302 - "ErrorResponse"
Cohesion: 0.24
Nodes (11): ErrorResponse, BaseModel, Test Cases, Project Conventions, Project Conventions, Project Conventions, Acceptance Criteria, Acceptance Criteria (+3 more)

### Community 303 - "pytest"
Cohesion: 0.18
Nodes (9): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms() (+1 more)

### Community 304 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.18
Nodes (10): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slices (+2 more)

### Community 305 - "interviews_route.py"
Cohesion: 0.05
Nodes (77): alias, Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query… (+69 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 308 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 309 - "test_context.py"
Cohesion: 0.31
Nodes (10): manager(), parametrize, test_a_named_strategy_overrides_the_default(), test_a_strategy_without_a_limit_is_never_trimmed(), test_builds_the_task_with_its_default_strategy(), test_estimate_is_characters_divided_by_four(), test_over_the_limit_drops_oldest_entries_until_it_fits(), test_required_parts_alone_over_the_limit_raise_and_still_log() (+2 more)

### Community 310 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 311 - "test_log_context.py"
Cohesion: 0.29
Nodes (9): fixture, Log context on real interview requests (U1 structlog, AC4): `session` and…, Every line of the one request whose access line ends with `path_end`., _request_lines(), started(), test_a_request_for_someone_elses_interview_logs_the_id_it_asked_for(), test_a_start_request_logs_the_new_session_and_the_user_on_every_line(), test_a_streamed_turn_logs_its_session_and_user_from_inside_the_stream() (+1 more)

### Community 312 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 313 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 314 - "Learn: one retry policy on tenacity, and why reply retries stay out of it (U2)"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Eval log (+1 more)

### Community 315 - "interviews_feedback_service.py"
Cohesion: 0.11
Nodes (30): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackWrite, FeedbackWriteInputs (+22 more)

### Community 316 - "U0 baselines"
Cohesion: 0.25
Nodes (7): Before relying on this, Cost, Eval baselines, How to use this file, Live interviews (from `logs/app.log`, before U1), Prompts with no eval baseline (gaps), U0 baselines

### Community 317 - "check_core"
Cohesion: 0.25
Nodes (8): Skills Consulted During Implementation, check_core(), _imports(), Every `app/core` import of a feature module (`app.modules...`): core is shared…, (absolute module, imported names) per import statement; relative imports…, test_a_core_file_importing_a_feature_module_is_reported(), test_a_core_file_importing_only_core_and_libraries_is_clean(), test_the_real_core_imports_no_feature_module()

### Community 318 - "test_eval_runs.py"
Cohesion: 0.06
Nodes (49): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), Any, Score (+41 more)

### Community 319 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository)

### Community 320 - "Implementation Steps"
Cohesion: 0.31
Nodes (9): MessageKind, Transcript item kinds: a question comes from interview_questions, the other two…, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut, build_transcript(), The chat as the user saw it: each question, then its answer and reaction when…, Implementation Steps, Affected Files & Patterns (+1 more)

### Community 321 - "test_create_admin.py"
Cohesion: 0.44
Nodes (8): main(), Session, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting(), test_new_admin_password_follows_registration_rules(), test_running_twice_is_a_no_op(), test_unknown_email_creates_an_active_admin()

### Community 322 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 323 - "RubricCriterion"
Cohesion: 0.40
Nodes (4): model_validator, Self, One criterion of the feedback rubric: what it asks, an anchor per score, and…, RubricCriterion

### Community 324 - "bank"
Cohesion: 0.25
Nodes (9): Acceptance Criteria, Acceptance Criteria, Edge Cases, Test Results, Deviations from Plan, bank(), _bank_question(), make_bank_question() (+1 more)

### Community 325 - "Learn: Prompt registry (one place for prompt versions and routing)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Eval log (AI features only), Learn: Prompt registry (one place for prompt versions and routing)

### Community 326 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

### Community 327 - "RecordingClient"
Cohesion: 0.22
Nodes (3): Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, recording(), RecordingClient

### Community 328 - "Web"
Cohesion: 0.22
Nodes (4): Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 329 - "guard_verdict"
Cohesion: 0.32
Nodes (8): guard_verdict(), GuardStatus, StrEnum, D or E against C (spec AC13). `*_repeat_means`: skill_coverage averaged per…, parametrize, test_the_coverage_guard_uses_cs_spread_as_its_margin(), test_the_guard_fails_when_the_injection_was_obeyed_even_once(), test_the_guard_refuses_with_fewer_than_three_repeats()

### Community 330 - "db"
Cohesion: 0.47
Nodes (5): db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., test_a_turn_is_saved_all_or_nothing(), arm_once(), failing_commit()

### Community 331 - "ContextTooLargeError"
Cohesion: 0.40
Nodes (3): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit.

### Community 332 - "_profile_scores"
Cohesion: 0.40
Nodes (5): presumption_hits(), Indexes of the questions that contain a presumption phrase (case-insensitive…, _profile_scores(), One interview's résumé metrics, for its Langfuse result; the same for every…, test_presumption_phrases_match_case_insensitively_and_nothing_else()

### Community 333 - "notes_overlap"
Cohesion: 0.50
Nodes (4): notes_overlap(), Collection, Jaccard of two arms' note chunk ids: 1.0 = the same notes, 0.0 = none shared., test_notes_overlap_is_the_jaccard_of_chunk_ids()

### Community 334 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 335 - "_Usage"
Cohesion: 0.67
Nodes (3): The four usage fields of FeedbackCaseResult, so `**_usage(...)` is checked…, _Usage, TypedDict

### Community 336 - "started"
Cohesion: 0.67
Nodes (3): fixture, An owner with a started 3-question behavioral interview: (owner, session_id,…, started()

## Knowledge Gaps
- **1081 isolated node(s):** `cuewise-be`, `What it does`, `How to invoke`, `Example output`, `See also` (+1076 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2553 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **46 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LLMError` connect `interviews_constants.py` to `FakeProvider`, `test_retry.py`, `Cuewise BE — Project Instructions`, `interviews_rag_evals.py`, `test_deepgram.py`, `ChatMessage`, `User`, `profile_evals.py`, `LLMServerError`, `interviews_knowledge_utils.py`, `test_factory.py`, `test_evals.py`, `interviews_route.py`, `InterviewerInputs`, `FakeSynthesizer`, `InterviewQuestion`, `interviews_feedback_service.py`, `Learn: one retry policy on tenacity, and why reply retries stay out of it (U2)`, `errors.py`, `FakeEmbedder`, `test_stream_turn.py`, `Tracer`, `Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)`, `interviews_evals.py`, `FakeTranscriber`, `FollowUpAction`, `RetryPolicy`, `LLMTimeoutError`, `Any`, `Feature: Langfuse Tracing`, `JobRole`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `FakeProvider`, `test_generation_eval.py`, `main`, `FakeLangfuse`, `interviews_rag_evals.py`, `ChatMessage`, `test_feedback_evals.py`, `ContextManager`, `AnswerService`, `profile_evals.py`, `test_feedback_endpoint.py`, `traced`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `FakeClient`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `test_factory.py`, `test_evals.py`, `interviews_route.py`, `InterviewerInputs`, `Feature: Langfuse experiments for the interviews evals`, `test_openai_compatible_stream.py`, `interviews_feedback_service.py`, `test_tracing_routes.py`, `test_eval_runs.py`, `run_generation`, `RecordingClient`, `interviews_feedback_evals.py`, `experiments`, `interviews_evals.py`, `test_retrieval_eval.py`, `test_tracing.py`, `Any`, `4. How it works`, `interviews_constants.py`, `test_tracing_lifespan.py`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `decode_token`, `auth_service.py`, `interviews_rag_evals.py`, `InterviewSession`, `ContextManager`, `AnswerService`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `interviews_schema.py`, `interviews_job_url_service.py`, `interviews_route.py`, `profile_service.py`, `test_create_interview.py`, `interviews_feedback_controller.py`, `interviews_feedback_service.py`, `test_create_admin.py`, `UsersService`, `interviews_constants.py`, `interviews_model.py`, `require_permissions`, `tests/conftest.py`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Are the 51 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 41 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 41 INFERRED edges - model-reasoned connections that need verification._
- **Are the 31 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 31 INFERRED edges - model-reasoned connections that need verification._
- **Are the 71 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 71 INFERRED edges - model-reasoned connections that need verification._