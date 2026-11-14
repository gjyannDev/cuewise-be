# Graph Report - cuewise-be  (2026-11-14)

## Corpus Check
- 434 files · ~376,652 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 5902 nodes · 16787 edges · 285 communities (237 shown, 48 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 3101 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1650faf8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- interviews_context.py
- LLMRateLimitError
- test_profile_eval_metrics.py
- decode_token
- test_interview_report.py
- auth_dependencies.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- Completed Steps
- tests/conftest.py
- test_profile_read_resume.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- LLMResult
- test_feedback_evals.py
- test_safe_fetch.py
- require_permissions
- test_tracing_lifespan.py
- cuewise-be
- interviews_write.py
- interviews_answer_service.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- Implementation Steps
- interviews_rag_evals.py
- Feature: Context Management for the Interview LLM Calls
- Feature: Layered Modules (route -> controller -> service -> repository)
- Transcriber
- ChatMessage
- 4. How it works
- Implementation: LLM as the Interviewer (it asks the questions)
- test_reference_note_context.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- interviews_job_url_service.py
- Implementation Plan: Follow-up Questions (decide / write split)
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_evals.py
- test_feedback_contract.py
- interviews_model.py
- interviews_turn.py
- profile_route.py
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- merge_note_rankings
- test_tracing_routes.py
- test_context_controller.py
- test_create_admin.py
- job_description_summary_v2.md
- errors.py
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- Implementation Plan: Error Handling
- test_answer_llm.py
- test_eval_runs.py
- test_profile_context.py
- exception_handlers.py
- interviews_feedback_evals.py
- Langfuse CLI Reference
- Implementation: Résumé upload and candidate profile (Slice 8c)
- InvalidReplyError
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- interviews_evals.py
- provider.py
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- interviews_feedback_turn.py
- PageParams
- OpenAICompatibleProvider
- test_google_embedder.py
- run_feedback_case
- interviewer_v2.md
- job_description_summary_v1.md
- ContextManager
- Project
- DeepgramTranscriber
- Langfuse Observability
- interviewer_v3.md
- main
- Implementation Plan: Context Management for the Interview LLM Calls
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- ProviderConfig
- test_get_interview.py
- Role
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- Langfuse
- LLMServerError
- interview_report.py
- Implementation: Eval runs in Langfuse (scores + datasets)
- Feature: Langfuse Tracing
- Langfuse
- interviews_constants.py
- InterviewerInputs
- audio_container
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- test_guards.py
- types.py
- traces
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
- Slices in detail
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- ConsoleFormatter
- test_knowledge_ingest.py
- test_answer_guards.py
- Generation
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- test_reply_contract.py
- interviews/conftest.py
- test_profile_redaction.py
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- CandidateProfile
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- scrub_contacts
- FollowUpAction
- Implementation Steps
- FeedbackCaseResult
- parse_log
- Learn: Résumé-aware interview (Slice 8d)
- test_answer_with_profile.py
- .record_turn
- llm
- test_transcript.py
- hint_for
- JobRole
- ErrorResponse
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Feature: Interview History List (backend)
- feedback_score_v1.md
- feedback_write_v1.md
- Implementation: Layered Modules (route -> controller -> service -> repository)
- 2. Langfuse Documentation
- test_stream_answer.py
- load_prompt
- fixture
- bank
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: LLM as the Interviewer (it asks the questions)
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- StreamedTurn
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- stream_answer
- Implementation: Three New Interview Roles (designer, qa, devops)
- test_retrieval_eval.py
- Permission
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
- import_job_text_paste
- Communication and priorities
- Engineering habits
- Senior judgement
- LLMProvider
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- User
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- Clock
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- interviews_job_url_utils.py
- Checks
- profile_extract_v1.md
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- Implementation Plan: UUID primary keys
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_generation_eval.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- test_answer_interview.py
- ResumeRefusal
- Learn: Résumé upload and the candidate profile (Slice 8c)
- Tracer
- pytest
- check_feedback
- lf
- test_a_badly_labelled_case_is_rejected
- Web
- FakeLangfuse
- InterviewQuestion
- test_job_description_summary.py
- _reset_request_id
- fixture

## God Nodes (most connected - your core abstractions)
1. `User` - 123 edges
2. `Tracer` - 122 edges
3. `FakeProvider` - 117 edges
4. `JobRole` - 113 edges
5. `LLMResult` - 106 edges
6. `Level` - 98 edges
7. `InterviewType` - 94 edges
8. `InterviewQuestion` - 92 edges
9. `QuestionCategory` - 89 edges
10. `LLMProvider` - 84 edges

## Surprising Connections (you probably didn't know these)
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `6. Try it yourself` --references--> `get_tracer()`  [INFERRED]
  docs/features/split-interviews-dependencies/learnings.md → app/core/ai/dependencies.py
- `Acceptance Criteria` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py
- `Functional` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py

## Import Cycles
- None detected.

## Communities (285 total, 48 thin omitted)

### Community 0 - "interviews_context.py"
Cohesion: 0.05
Nodes (70): NamedTuple, StrategyOutput, build_context_manager(), _counts(), FeedbackScoreInputs, FeedbackWrite, FeedbackWriteInputs, FollowUpDecision (+62 more)

### Community 1 - "LLMRateLimitError"
Cohesion: 0.18
Nodes (23): LLMRateLimitError, LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., backoff_seconds(), parse_retry_after(), Random, raise_for_status(), Retry rules shared by every vendor client in `core/ai` (the LLM provider and… (+15 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.08
Nodes (51): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, _injection_share(), _mention_share(), notes_overlap() (+43 more)

### Community 3 - "decode_token"
Cohesion: 0.11
Nodes (33): BadRequestError, InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token() (+25 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (52): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start() (+44 more)

### Community 5 - "auth_dependencies.py"
Cohesion: 0.10
Nodes (31): AuthController, Request -> service call, domain result -> response schema., get_controller(), get_service(), Depends, Session, AuthRepository, Session (+23 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "Completed Steps"
Cohesion: 0.04
Nodes (99): Embedder, Protocol, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Step, NoteSource, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, Where a note's content came from. A model grounding a model on its own drafts… (+91 more)

### Community 9 - "tests/conftest.py"
Cohesion: 0.05
Nodes (49): RequestIdFilter, hash_password(), CurrentUserDep, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues (+41 more)

### Community 10 - "test_profile_read_resume.py"
Cohesion: 0.17
Nodes (31): make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), read_resume(), ResumeUnreadableRefusal, ResumeUnsupportedRefusal, Run, parametrize (+23 more)

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
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - "LLMResult"
Cohesion: 0.12
Nodes (26): LLMResult, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Delta, Draft, NamedTuple, What one answer turn of the LLM interviewer hands around: its action, its…, The next chunk of the question being written (shown as it arrives). (+18 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.16
Nodes (18): Grader, Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The…, A fake provider: scores every criterion `value`, quoting the start of each…, _result(), run_main(), scores_on(), test_a_langfuse_outage_does_not_change_the_run(), test_a_single_run_posts_no_spread() (+10 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (41): Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request, Response (+33 more)

### Community 19 - "require_permissions"
Cohesion: 0.08
Nodes (32): ForbiddenError, get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), require_roles(), check() (+24 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "interviews_write.py"
Cohesion: 0.09
Nodes (32): The labels of one write call. A write whose prompt carries the candidate…, write_trace_labels(), The decide step of an answer turn: the model suggests following up or moving…, log_embedding_call(), log_llm_call(), log_llm_error(), log_result(), log_retrieval() (+24 more)

### Community 27 - "interviews_answer_service.py"
Cohesion: 0.06
Nodes (73): QuestionNotCurrentError, MessageKind, The SSE event names of a streamed turn: the contract with the client. `done`…, Transcript item kinds: a question comes from interview_questions, the other two…, StreamEvent, answer_out(), AnswerController, _error_event() (+65 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.05
Nodes (88): RateLimiter, Count one request for `key`: None when allowed, else whole seconds until its…, get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, get_resume_limiter() (+80 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (37): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+29 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.09
Nodes (17): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+9 more)

### Community 31 - "Implementation Steps"
Cohesion: 0.09
Nodes (21): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Skills Consulted (+13 more)

### Community 32 - "interviews_rag_evals.py"
Cohesion: 0.04
Nodes (120): notes_fingerprint(), What every eval task moved onto Langfuse experiments shares (langfuse-…, What produced a run, as the strings Langfuse stores: the run explains itself…, Local time, as the Langfuse list shows the run's start: the name and the…, A short id for the ingested notes: changes when any note changes, not when the…, run_metadata(), run_stamp(), _arm_notes() (+112 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 35 - "Transcriber"
Cohesion: 0.18
Nodes (9): Protocol, Transcriber, 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e) (+1 more)

### Community 36 - "ChatMessage"
Cohesion: 0.09
Nodes (29): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:… (+21 more)

### Community 37 - "4. How it works"
Cohesion: 0.07
Nodes (30): _decode(), FetchedPage, FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach… (+22 more)

### Community 38 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 39 - "test_reference_note_context.py"
Cohesion: 0.12
Nodes (23): A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, WindowLedger, WithInterviewData, 5. What can go wrong, first_user(), inputs(), _max_note() (+15 more)

### Community 40 - "test_layers.py"
Cohesion: 0.06
Nodes (44): ast, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository) (+36 more)

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
Cohesion: 0.10
Nodes (38): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, Any network-side failure of a job link. One message for every cause, so…, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError (+30 more)

### Community 45 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.07
Nodes (25): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview (+17 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.07
Nodes (25): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank). (+17 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.07
Nodes (99): FakeProvider, load_cases(), main(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, run_case(), Deviations from Plan (+91 more)

### Community 49 - "test_feedback_contract.py"
Cohesion: 0.06
Nodes (90): FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, assess_evidence(), build_threads(), _check_lengths(), compute_overall(), Evidence, FeedbackThread (+82 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.06
Nodes (71): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., In-memory fixed-window rate limiting for sensitive endpoints. Per process only:… (+63 more)

### Community 51 - "interviews_turn.py"
Cohesion: 0.12
Nodes (25): decide(), UUID, At most two attempts within the decide cap; any failure means "next_question"…, One budget for the whole generation, started when the request holds its claim., Decision, apply_limits(), Deadline, _decision_label() (+17 more)

### Community 52 - "profile_route.py"
Cohesion: 0.15
Nodes (16): delete_profile(), get_profile(), post, ProfileUser, A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes…, The signed-in user's profile; 404 `PROFILE_NOT_FOUND` before the first upload., Remove the signed-in user's profile for good; 204 also when there was none., upload_resume() (+8 more)

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
Cohesion: 0.07
Nodes (63): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+55 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.15
Nodes (31): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_retry_after_longer_than_the_budget_fails_at_once_without_waiting(), test_a_smaller_budget_argument_caps_retries() (+23 more)

### Community 59 - "merge_note_rankings"
Cohesion: 0.07
Nodes (39): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, Architecture & Design, Blockers & Resolutions, Decisions (grill-me, 2026-11-14), Deviations during implementation (2026-11-14, see task.md), Implementation Plan: Résumé-aware interview (Slice 8d), Overview (+31 more)

### Community 61 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 62 - "test_create_admin.py"
Cohesion: 0.21
Nodes (12): verify_password(), main(), Session, Create the first admin, or promote an existing user to admin. Usage: uv run…, argparse, getpass, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password() (+4 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "errors.py"
Cohesion: 0.07
Nodes (55): AppError, AudioTooLargeError, AudioTooLongError, ConflictError, FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError (+47 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.11
Nodes (45): EmbedCall, FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), embedder_for(), RetrievalService.retrieve with the candidate profile's query (resume-aware-… (+37 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.19
Nodes (28): PhaseChanged, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, collect(), follow_up_json(), inputs(), kinds(), make_interviewer() (+20 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (37): 5. What can go wrong, profile_json(), Synthetic résumé data and the scripted model shared by the profile tests (no…, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,… (+29 more)

### Community 68 - "Implementation Plan: Error Handling"
Cohesion: 0.09
Nodes (19): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling (+11 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.13
Nodes (19): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview() (+11 more)

### Community 71 - "test_eval_runs.py"
Cohesion: 0.04
Nodes (65): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), Any, Score (+57 more)

### Community 72 - "test_profile_context.py"
Cohesion: 0.18
Nodes (25): ContextReport, estimate_tokens(), _log(), default_strategy(), everything(), fingerprint(), golden_inputs(), inputs() (+17 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.19
Nodes (22): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+14 more)

### Community 74 - "interviews_feedback_evals.py"
Cohesion: 0.12
Nodes (26): feedback_dataset_items(), feedback_run_scores(), FeedbackEvalCase, FeedbackEvalQuestion, FeedbackEvalSetup, FeedbackEvalTurn, FeedbackSummary, load_feedback_cases() (+18 more)

### Community 75 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues, Links (+7 more)

### Community 77 - "InvalidReplyError"
Cohesion: 0.12
Nodes (31): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, fit(), parse_profile_reply(), BaseModel (+23 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "interviews_evals.py"
Cohesion: 0.06
Nodes (73): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_reply() (+65 more)

### Community 82 - "provider.py"
Cohesion: 0.03
Nodes (74): anyio, Context management: the one place that decides what each LLM call sends. The…, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Request dependencies for the AI services every feature shares, built once at…, EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel (+66 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "interviews_feedback_turn.py"
Cohesion: 0.17
Nodes (18): BuiltContext, ScoreResult, _Attempts, CallUsage, FeedbackGenerator, log_feedback_summary(), tokens(), NamedTuple (+10 more)

### Community 85 - "PageParams"
Cohesion: 0.07
Nodes (34): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, UsersController (+26 more)

### Community 86 - "OpenAICompatibleProvider"
Cohesion: 0.13
Nodes (13): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+5 more)

### Community 87 - "test_google_embedder.py"
Cohesion: 0.17
Nodes (20): Clock, make_embedder(), ok(), fixture, parametrize, Response, GoogleEmbedder: Gemini's native batchEmbedContents over httpx (knowledge-base-…, Embedder whose HTTP layer is a scripted list of responses (or exceptions), one… (+12 more)

### Community 88 - "run_feedback_case"
Cohesion: 0.16
Nodes (22): feedback_scores_for(), feedback_trace_output(), One case through the same pre-check, score call, write call and template…, What came out next to what was wanted: the verdict, the overall against its…, (name, value, comment) per check, plus `valid_reply` and `case_passed`. An…, run_feedback_case(), case(), test_a_case_in_its_band_passes_every_check() (+14 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "ContextManager"
Cohesion: 0.12
Nodes (18): ContextManager, Task, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+10 more)

### Community 92 - "Project"
Cohesion: 0.22
Nodes (20): candidate_profile_block(), profile_query_text(), The candidate profile as interview input: a fenced prompt block and a short…, The profile fenced as data, like the job description. Summaries and…, The profile's short items as one retrieval query. None: nothing to embed., Project, Testing Strategy, _profile() (+12 more)

### Community 93 - "DeepgramTranscriber"
Cohesion: 0.16
Nodes (7): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, _make()

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "main"
Cohesion: 0.60
Nodes (4): main(), Session, test_an_empty_database(), test_reports_stored_questions_grouped_by_interview()

### Community 97 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

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

### Community 103 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

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

### Community 108 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 109 - "LLMServerError"
Cohesion: 0.10
Nodes (17): LLMServerError, 5xx or a dropped connection: the provider's side failed., 7. What surprised me, Eval log, 1. Why it exists, 3. When to use it, 4. How it works, 5. What can go wrong (+9 more)

### Community 110 - "interview_report.py"
Cohesion: 0.15
Nodes (19): html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+11 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "interviews_constants.py"
Cohesion: 0.07
Nodes (52): _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_interviewer_reply(), parse_streamed_reply(), BaseModel, NamedTuple (+44 more)

### Community 115 - "InterviewerInputs"
Cohesion: 0.23
Nodes (12): InterviewerInputs, Plain values for one interviewer or decide call., Interviewer, UUID, The same turn as `answer_turn` (same decide, limits and fallbacks), telling the…, TurnOutcome, Deviations from Spec (to apply to spec.md), Deviations from Plan (+4 more)

### Community 116 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

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
Cohesion: 0.18
Nodes (15): _assert_401(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access(), test_guards_allow_or_forbid_by_db_role(), test_missing_header_is_token_missing(), test_non_bearer_or_empty_token_is_token_missing() (+7 more)

### Community 121 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 122 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 123 - "profile_resume_files.py"
Cohesion: 0.10
Nodes (34): build_file(), The case as the file a candidate would upload. Hidden lines are white (PDF) or…, _content(), _escape(), _fill(), Image, make_pdf(), plain_zip() (+26 more)

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
Nodes (16): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé-aware interview (Slice 8d), Functional, Goal (+8 more)

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
Cohesion: 0.11
Nodes (34): _clean(), _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _has_external_relationship() (+26 more)

### Community 134 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 135 - "Slices in detail"
Cohesion: 0.18
Nodes (11): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 6: Feedback and scoring, Slice 7: Eval maturity (trust the judge, catch regressions), Slice 9: Tool use and agents (+3 more)

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
Cohesion: 0.05
Nodes (43): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites, ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message… (+35 more)

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.27
Nodes (21): IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, active(), chunks(), corpus(), interview(), ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag… (+13 more)

### Community 143 - "test_answer_guards.py"
Cohesion: 0.15
Nodes (11): message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409(), test_database_rejects_a_second_answer_for_one_question(), test_invalid_input_is_422_and_saves_nothing() (+3 more)

### Community 144 - "Generation"
Cohesion: 0.17
Nodes (8): Generation, _model_parameters(), ReasoningEffort, The stream was closed before it finished (client left, or the turn's deadline…, What the call asked the model for, shown on the generation. A temperature only…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, _usage_details(), TraceLabels

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
Nodes (59): Slice 3: Structured follow-up decisions, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open (+51 more)

### Community 151 - "interviews/conftest.py"
Cohesion: 0.06
Nodes (63): get_llm_provider(), get_tracer(), Request, Built once at startup (app lifespan); None when no key is configured or the…, Built once at startup (app lifespan); a disabled tracer when the lifespan…, get_answer_controller(), get_answer_service(), Depends (+55 more)

### Community 152 - "test_profile_redaction.py"
Cohesion: 0.29
Nodes (15): contextlib, assert_redacted(), assert_traced_in_full(), generations(), inputs(), anyio, resume-aware-interview Step 5: a write whose prompt carries the profile is…, run_stream_write() (+7 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): has_notes(), UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started(), stored(), test_a_failing_embedder_still_starts_with_filter_notes() (+17 more)

### Community 156 - "CandidateProfile"
Cohesion: 0.08
Nodes (45): pacer(), wait(), `wait()` sleeps `pause` seconds on every call but the first. Called before each…, Limits, thresholds and messages of the résumé upload (resume-upload spec)., Output, CandidateProfile, The candidate profile: what a résumé becomes, what is stored, and what the API…, ExpectedProfile (+37 more)

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.42
Nodes (9): ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1(), test_an_invalid_note_names_the_file_writes_nothing_and_exits_1(), test_it_prints_the_counts_and_exits_0(), test_warnings_are_printed_without_note_text(), test_without_the_google_key_it_says_what_to_set_and_exits_1() (+1 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 160 - "FollowUpAction"
Cohesion: 0.25
Nodes (16): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Completed Steps (+8 more)

### Community 161 - "Implementation Steps"
Cohesion: 0.05
Nodes (48): AbstractContextManager, Any, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, A named step inside the current trace (a Langfuse `chain`): the generations and… (+40 more)

### Community 162 - "FeedbackCaseResult"
Cohesion: 0.21
Nodes (14): criterion_spread(), feedback_hints_for(), FeedbackCaseResult, level_gap_check(), _print_case(), The pair's check, or None when there is nothing to compare: no pair, or either…, Per case: the largest gap between the highest and lowest score any one…, Where to look first for each failed check (or the error), in the order the… (+6 more)

### Community 163 - "parse_log"
Cohesion: 0.22
Nodes (14): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), analysis(), lines_of(), Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis() (+6 more)

### Community 164 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.14
Nodes (13): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+5 more)

### Community 165 - "test_answer_with_profile.py"
Cohesion: 0.25
Nodes (12): opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent(), test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile() (+4 more)

### Community 166 - ".record_turn"
Cohesion: 0.06
Nodes (41): ErrorBody, BaseModel, ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Save one whole turn in one commit: advance the session, the answer, the…, done(), Deviations from Plan, 1. Why it exists (+33 more)

### Community 167 - "llm"
Cohesion: 0.13
Nodes (13): Functional, Non-Functional, Requirements, as_v5_text(), _decision_json(), llm(), script(), script_decide() (+5 more)

### Community 168 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 169 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 170 - "JobRole"
Cohesion: 0.05
Nodes (89): NotEnoughQuestionsError, InterviewType, JobRole, Level, BankQuestion, One entry of the hand-written question bank file., The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric (+81 more)

### Community 171 - "ErrorResponse"
Cohesion: 0.04
Nodes (55): ErrorResponse, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Goal, Out of Scope (+47 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.08
Nodes (29): Baseline Failures, Testing Strategy, Testing Strategy, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material (+21 more)

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

### Community 178 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 179 - "test_stream_answer.py"
Cohesion: 0.15
Nodes (19): 5. What can go wrong, 6. Try it yourself, fixture, AnswerController.stream_answer driven directly, for what a test client can't…, A started interview and a controller wired like the app's: returns (controller,…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing() (+11 more)

### Community 180 - "load_prompt"
Cohesion: 0.09
Nodes (35): A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), load_prompt(), Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt() (+27 more)

### Community 181 - "fixture"
Cohesion: 0.17
Nodes (12): answer(), _answer(), anyio_backend(), fixture, POST an answer; `question_id` defaults to whatever the caller passes, body…, Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a recording to the transcription endpoint; `audio=None` sends no file part…, POST a setup for `user`; any field can be overridden, or dropped by passing… (+4 more)

### Community 182 - "bank"
Cohesion: 0.18
Nodes (11): Acceptance Criteria, Acceptance Criteria, Edge Cases, Functional, Non-Functional, Requirements, Test Results, Deviations from Plan (+3 more)

### Community 183 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 184 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 185 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 186 - "StreamedTurn"
Cohesion: 0.22
Nodes (7): unique_question(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

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

### Community 193 - "stream_answer"
Cohesion: 0.29
Nodes (7): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream(), test_done_has_the_json_endpoints_shape_and_content(), run()

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.06
Nodes (26): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+18 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.14
Nodes (24): contextvars, A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and…, embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;… (+16 more)

### Community 220 - "Permission"
Cohesion: 0.10
Nodes (20): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry() (+12 more)

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

### Community 234 - "import_job_text_paste"
Cohesion: 0.40
Nodes (6): import_job_text_paste(), import_job_url(), interviews_create, Read the job description from a posting link, for the candidate to review…, Clean a whole posting page the candidate copied from their own browser: the…, JobUrlControllerDep

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "LLMProvider"
Cohesion: 0.05
Nodes (50): LLMProvider, Protocol, ProfileExtractionFailedError, ProfileNotFoundError, ProfileRequiredError, ProfileUnavailableError, Over the byte, page or unzipped-size limit of a résumé upload., Not a PDF or a Word document by its content (the file name is never trusted). (+42 more)

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

### Community 244 - "User"
Cohesion: 0.05
Nodes (85): alias, AnswerControllerDep, User, HistorySortColumn, StrEnum, QuestionSource, The history columns GET /interviews sorts by; the values are the response's…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and… (+77 more)

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

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

### Community 251 - "Checks"
Cohesion: 0.40
Nodes (5): Checks, bad_parent(), _consistency(), Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers…

### Community 252 - "profile_extract_v1.md"
Cohesion: 0.40
Nodes (4): Constraints, Input, Role, Task

### Community 253 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 255 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 256 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 257 - "test_generation_eval.py"
Cohesion: 0.06
Nodes (63): parse_arms(), Read your filled-in sheet, print how often each arm ranked first, then post…, `--arms`: comma-separated arm letters (any case), at least two (a ranking…, run_ranking(), 13. Phase 2 real runs (yours), Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals (+55 more)

### Community 258 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 259 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 260 - "ResumeRefusal"
Cohesion: 0.50
Nodes (3): Exception, Why a file was refused; `reason` is short and machine-readable (logged, never…, ResumeRefusal

### Community 261 - "Learn: Résumé upload and the candidate profile (Slice 8c)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Résumé upload and the candidate profile (Slice 8c)

### Community 262 - "Tracer"
Cohesion: 0.05
Nodes (52): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, build_tracer(), Send what is still buffered, then stop the background exporter. Called once at…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, Tracer, TracingProvider (+44 more)

### Community 263 - "pytest"
Cohesion: 0.16
Nodes (9): pytest, parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text(), parametrize, test_request_id_header_sent_exactly_once() (+1 more)

### Community 264 - "check_feedback"
Cohesion: 0.20
Nodes (7): Band, _band_check(), check_feedback(), model_validator, Self, The case's labels against what came out. Check names stay stable: Langfuse…, test_a_case_scored_when_it_should_not_have_been_points_at_the_pre_check()

### Community 265 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

### Community 266 - "test_a_badly_labelled_case_is_rejected"
Cohesion: 0.67
Nodes (3): parametrize, test_a_badly_labelled_case_is_rejected(), test_a_pair_must_name_an_earlier_case()

### Community 267 - "Web"
Cohesion: 0.20
Nodes (5): fixture, Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 268 - "FakeLangfuse"
Cohesion: 0.07
Nodes (22): 5. What can go wrong, experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input() (+14 more)

### Community 269 - "InterviewQuestion"
Cohesion: 0.07
Nodes (34): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter(), _history_order(), InterviewsRepository, Any, datetime (+26 more)

### Community 271 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 293 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

## Knowledge Gaps
- **897 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+892 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2197 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **48 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `test_generation_eval.py`, `Completed Steps`, `FakeLangfuse`, `Generation`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `interviews/conftest.py`, `test_profile_redaction.py`, `interviews_answer_service.py`, `CandidateProfile`, `test_feedback_endpoint.py`, `interviews_rag_evals.py`, `Implementation Steps`, `ChatMessage`, `test_evals.py`, `interviews_model.py`, `test_tracing_routes.py`, `errors.py`, `test_profile_routes.py`, `test_eval_runs.py`, `interviews_feedback_evals.py`, `interviews_evals.py`, `provider.py`, `test_retrieval_eval.py`, `interviews_feedback_turn.py`, `run_feedback_case`, `LLMProvider`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `User`, `traces`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `UUIDPrimaryKeyMixin` connect `interviews_model.py` to `Transcriber`, `Cuewise BE — Project Instructions`, `ErrorResponse`, `InterviewQuestion`, `LLMProvider`, `require_permissions`, `User`, `test_reply_contract.py`, `Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `interviews_answer_service.py`, `test_feedback_endpoint.py`, `Feature: Résumé upload and candidate profile (Slice 8c)`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `errors.py`, `decode_token`, `auth_dependencies.py`, `Completed Steps`, `tests/conftest.py`, `import_job_text_paste`, `interviews_job_url_service.py`, `InterviewQuestion`, `LLMProvider`, `interviews_model.py`, `require_permissions`, `PageParams`, `test_create_interview.py`, `interviews/conftest.py`, `interviews_answer_service.py`, `Permission`, `test_create_admin.py`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Are the 49 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 49 INFERRED edges - model-reasoned connections that need verification._
- **Are the 40 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 29 INFERRED edges - model-reasoned connections that need verification._
- **Are the 69 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 69 INFERRED edges - model-reasoned connections that need verification._