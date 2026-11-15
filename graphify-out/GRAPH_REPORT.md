# Graph Report - cuewise-be  (2026-11-15)

## Corpus Check
- 459 files · ~402,269 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 6198 nodes · 17439 edges · 310 communities (260 shown, 50 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 3279 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e79fab41`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- QuestionTurn
- LLMServerError
- test_profile_eval_metrics.py
- decode_token
- test_interview_report.py
- auth_service.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- Completed Steps
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
- InterviewSession
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- interviews_rag_evals.py
- Feature: Context Management for the Interview LLM Calls
- pytest
- ingest_corpus
- profile_service.py
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
- KnowledgeRepository
- QuestionCategory
- upload_resume
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- ReferenceNote
- test_tracing_routes.py
- test_context_controller.py
- interviews_service.py
- job_description_summary_v2.md
- Implementation Steps
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- test_reference_note_context.py
- test_answer_llm.py
- profile_evals.py
- test_profile_context.py
- exception_handlers.py
- BaseModel
- test_gateway.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- json
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- interviews_evals.py
- LLMError
- Embedder
- interviews_constants.py
- pydantic
- OpenAICompatibleProvider
- EmbeddingKind
- test_tracing.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- Project
- provider.py
- Langfuse Observability
- interviewer_v3.md
- LLMResult
- FakeClient
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- InterviewMessage
- test_get_interview.py
- Role
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_log.py
- test_reply_contract.py
- interview_report.py
- Implementation: Eval runs in Langfuse (scores + datasets)
- Settings
- Langfuse
- load_prompt
- Implementation: Prompt Registry
- test_profile_read_resume.py
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- test_guards.py
- types.py
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
- Feature: Interview Feedback and Scoring (Slice 6)
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- ConsoleFormatter
- test_knowledge_ingest.py
- ContextManager
- test_feedback_context.py
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- test_follow_ups.py
- interviews_start_dependencies.py
- Implementation: Agentic Workflow v2
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- CandidateProfile
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- scrub_contacts
- follow_up
- Tracer
- VoiceService
- Implementation: Résumé-aware interview (Slice 8d)
- Learn: Résumé-aware interview (Slice 8d)
- test_answer_with_profile.py
- test_reaction_pick.py
- llm
- test_transcript.py
- hint_for
- JobRole
- traced
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Feature: Interview History List (backend)
- feedback_score_v1.md
- feedback_write_v1.md
- Implementation: Layered Modules (route -> controller -> service -> repository)
- Feature: Start an Interview (backend)
- Slices in detail
- Feature: Langfuse experiments for the interviews evals
- Implementation: LLM as the Interviewer (it asks the questions)
- StreamedTurn
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Follow-up Questions (decide / write split)
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- load_prompt
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- errors.py
- Implementation Plan: Role-Based Access Control (single JWT)
- Implementation: Three New Interview Roles (designer, qa, devops)
- test_retrieval_eval.py
- main.py
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
- Implementation Plan: Résumé-aware interview (Slice 8d)
- Communication and priorities
- Engineering habits
- Senior judgement
- interviews_model.py
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
- fixture
- test_tracing_lifespan.py
- AI Engineering Learning Path (Cuewise)
- Langfuse CLI Reference
- test_generation_eval.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- test_answer_interview.py
- test_profile_evals.py
- Learn: Résumé upload and the candidate profile (Slice 8c)
- FakeLangfuse
- re
- ._ordered
- lf
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- Web
- experiments
- InterviewQuestion
- bank
- test_job_description_summary.py
- Feature: Job URL (Slice 8b)
- check_layers
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- Langfuse
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- .record_turn
- Langfuse Observability
- Implementation Plan: Follow-up Questions (decide / write split)
- Learn: Splitting the interviews dependency wiring
- text
- .format
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Langfuse Prompt Migration
- profile_extract_v1.md
- traces
- Langfuse Prompt Migration
- ProfileLLM
- 2. Langfuse Documentation
- test_keyterms.py
- typing
- interviews_schema.py
- Implementation Steps
- interview-room/README.md
- _reset_request_id
- interviews_feedback_service.py

## God Nodes (most connected - your core abstractions)
1. `User` - 123 edges
2. `Tracer` - 122 edges
3. `FakeProvider` - 117 edges
4. `JobRole` - 114 edges
5. `LLMResult` - 106 edges
6. `Level` - 99 edges
7. `InterviewType` - 95 edges
8. `InterviewQuestion` - 92 edges
9. `QuestionCategory` - 89 edges
10. `LLMProvider` - 84 edges

## Surprising Connections (you probably didn't know these)
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `1. Why it exists` --references--> `DeepgramTranscriber`  [INFERRED]
  docs/features/interview-room/learnings.md → app/core/ai/deepgram.py
- `6. Try it yourself` --references--> `get_tracer()`  [INFERRED]
  docs/features/split-interviews-dependencies/learnings.md → app/core/ai/dependencies.py
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py

## Import Cycles
- None detected.

## Communities (310 total, 50 thin omitted)

### Community 0 - "QuestionTurn"
Cohesion: 0.05
Nodes (56): _counts(), An earlier question as the model would have written it. A follow-up was written…, App data at the end of the last user message; untrusted parts (questions,…, _status_block(), build_interviewer_messages(), interviewer_history(), job_description_block(), main_numbers() (+48 more)

### Community 1 - "LLMServerError"
Cohesion: 0.05
Nodes (64): LLMRateLimitError, LLMRequestError, LLMServerError, 5xx or a dropped connection: the provider's side failed., Other 4xx (bad key, bad request): retrying sends the same broken request again., Attempted, backoff_seconds(), _elapsed_ms() (+56 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.09
Nodes (50): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, _injection_share(), _mention_share(), notes_overlap() (+42 more)

### Community 3 - "decode_token"
Cohesion: 0.09
Nodes (38): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, BaseModel, UserAdminOut (+30 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.10
Nodes (65): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, analysis(), answer(), emit_answer_turn(), emit_call() (+57 more)

### Community 5 - "auth_service.py"
Cohesion: 0.10
Nodes (29): ConflictError, hash_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), post (+21 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.13
Nodes (35): extract_job_text(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, At most `limit` characters, cut at the last whitespace so no word is split;…, truncate_on_word(), jsonld(), page() (+27 more)

### Community 8 - "Completed Steps"
Cohesion: 0.16
Nodes (18): Why vector mode fell back to filter mode (logged as…, RetrievalDegrade, EligibleChunk, NamedTuple, The k eligible chunks embedded with `model` that are most similar to the query,…, The notes stored for this interview at start, rank order; none for interviews…, _log_level(), NamedTuple (+10 more)

### Community 9 - "tests/conftest.py"
Cohesion: 0.04
Nodes (57): RequestIdFilter, list_users(), PageDep, Baseline Failures, Deviations from Plan, Implementation: Error Handling, Known Issues, Links (+49 more)

### Community 10 - "WithInterviewData"
Cohesion: 0.07
Nodes (33): StrategyOutput, build_context_manager(), FullHistory, JobDescriptionSummary, A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WithInterviewData (+25 more)

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
Cohesion: 0.09
Nodes (39): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., _google(), no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env() (+31 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - "test_feedback_contract.py"
Cohesion: 0.18
Nodes (33): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+25 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.07
Nodes (67): check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult, FeedbackEvalCase (+59 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (41): Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request, Response (+33 more)

### Community 19 - "User"
Cohesion: 0.07
Nodes (30): verify_password(), get_service(), Depends, Session, User, AuthRepository, Session, UUID (+22 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.14
Nodes (27): Data, PromptVersion, StrEnum, What an interviewer write carries beyond the job description; it picks the…, Status, 5. What can go wrong, archived_routes(), catalog_mismatches() (+19 more)

### Community 26 - "RateLimiter"
Cohesion: 0.11
Nodes (21): RateLimiter, Count one request for `key`: None when allowed, else whole seconds until its…, get_resume_limiter(), limit_resume_uploads(), ProfileUser, Tests swap in a fresh limiter so counts never leak between them., Checked before the body is read: every upload is a parse and a model call., 4. How it works (+13 more)

### Community 27 - "interviews_answer_service.py"
Cohesion: 0.06
Nodes (57): QuestionNotCurrentError, log_stream_summary(), How a streamed turn felt and ended: time to the first event and to the first…, PhaseChanged, answer_out(), AnswerController, _frame(), AnswerEvent (+49 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.07
Nodes (75): FeedbackWrite, The write call: scores, evidence and question texts only; small whatever the…, FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists (+67 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.15
Nodes (38): FollowUpDecision, The decide call: the current thread in full (it judges the latest answer within…, decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i. (+30 more)

### Community 30 - "InterviewSession"
Cohesion: 0.06
Nodes (36): InterviewSession, 5. What can go wrong, 6. Try it yourself, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing() (+28 more)

### Community 31 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Implementation Steps, Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 32 - "interviews_rag_evals.py"
Cohesion: 0.04
Nodes (110): Local time, as the Langfuse list shows the run's start: the name and the…, run_stamp(), _arm_notes(), ArmInterview, ArmSummary, build_sheet(), case_set_problems(), competencies_of() (+102 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "pytest"
Cohesion: 0.08
Nodes (34): lifespan(), FastAPI, check_prompts(), _interviewer(), PromptCheckError, Exception, The startup prompt check: every routed prompt version loads and renders through…, One or more routed prompts cannot be sent; the message lists each one. (+26 more)

### Community 35 - "ingest_corpus"
Cohesion: 0.09
Nodes (35): build_embedder(), Embeddings for reference-note retrieval; None without the Google key (notes are…, _embed(), ingest_corpus(), IngestCounts, IngestError, Exception, NamedTuple (+27 more)

### Community 36 - "profile_service.py"
Cohesion: 0.13
Nodes (30): The résumé upload, in separate steps: read -> scrub -> extract (LLM) -> parse…, make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), _clean(), Exception, NamedTuple, Why a file was refused; `reason` is short and machine-readable (logged, never… (+22 more)

### Community 37 - "4. How it works"
Cohesion: 0.07
Nodes (29): _decode(), FetchedPage, FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach… (+21 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "interviews_knowledge_utils.py"
Cohesion: 0.07
Nodes (53): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, cosine_similarity(), _hash(), _listed() (+45 more)

### Community 40 - "test_layers.py"
Cohesion: 0.19
Nodes (18): ast, 5. What can go wrong, check_core(), _imports(), _one(), The layer rules of app/modules (CLAUDE.md, "Architecture"): route -> controller…, Every `app/core` import of a feature module (`app.modules...`): core is shared…, (absolute module, imported names) per import statement; relative imports… (+10 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.16
Nodes (26): _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card(), _html_metric_row(), _html_table() (+18 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.11
Nodes (34): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, Any network-side failure of a job link. One message for every cause, so…, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError (+26 more)

### Community 45 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6) (+7 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.08
Nodes (30): audio_container(), AudioContainer, _has_signature(), StrEnum, Audio rules every speech feature shares: which recording containers are…, Recording containers an upload may arrive in (what browsers' MediaRecorder…, The container of an uploaded recording, or None when its declared type isn't…, enum (+22 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.06
Nodes (103): FakeProvider, check_reply(), load_cases(), main(), pause_for(), Path, Rule checks for one reply. Text checks look at the parsed question, or at the…, Seconds to wait between cases: what `--pause-seconds` asked for, else the… (+95 more)

### Community 49 - "interviews_feedback.py"
Cohesion: 0.11
Nodes (30): _check_lengths(), _has_markup(), _normalized(), parse_write_reply(), BaseModel, _question_score(), QuestionScore, End-of-interview feedback: what the score and write calls must return, and the… (+22 more)

### Community 50 - "KnowledgeRepository"
Cohesion: 0.08
Nodes (34): alembic_config, KnowledgeChunk, KnowledgeChunkScope, One (role, level) a chunk applies to. Rows instead of array columns, so the…, _eligible(), KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how… (+26 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.06
Nodes (79): InterviewerInputs, Plain values for one interviewer or decide call., One budget for the whole generation, started when the request holds its claim., _check_question(), Decision, HeaderSplit, InterviewerReply, _normalized() (+71 more)

### Community 52 - "upload_resume"
Cohesion: 0.20
Nodes (12): delete_profile(), get_profile(), post, ProfileUser, A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes…, The signed-in user's profile; 404 `PROFILE_NOT_FOUND` before the first upload., Remove the signed-in user's profile for good; 204 also when there was none., upload_resume() (+4 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (21): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+13 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.15
Nodes (36): 5. What can go wrong, fail(), error(), import_url(), long_posting(), page(), paste(), fixture (+28 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.09
Nodes (55): analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table(), Checks, bad_parent() (+47 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (34): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+26 more)

### Community 59 - "ReferenceNote"
Cohesion: 0.27
Nodes (16): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, A note an interview was given: what the question writer sees (competency and…, ReferenceNote, names(), ranked(), merge_note_rankings: the quota merge of the job-description and profile…, Notes named by single letters, ranked in the given order with falling scores. (+8 more)

### Community 61 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 62 - "interviews_service.py"
Cohesion: 0.07
Nodes (50): NotFoundError, ProfileRequiredError, An interview asked to use the candidate's profile, and there is none to use…, SummaryInputs, HistorySortColumn, QuestionSource, The history columns GET /interviews sorts by; the values are the response's…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and… (+42 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "Implementation Steps"
Cohesion: 0.08
Nodes (32): Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, AudioTooLargeError, AudioTooLongError, NoSpeechError, TranscriptionUnavailableError, UnsupportedAudioError (+24 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.11
Nodes (42): EmbedCall, FakeEmbedder, NamedTuple, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets(), competencies() (+34 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.13
Nodes (39): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase (+31 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (37): 5. What can go wrong, profile_json(), Synthetic résumé data and the scripted model shared by the profile tests (no…, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,… (+29 more)

### Community 68 - "test_reference_note_context.py"
Cohesion: 0.20
Nodes (18): 5. What can go wrong, first_user(), inputs(), _max_note(), anyio, parametrize, Reference notes in the question writer's input (knowledge-base-rag Step 9;…, test_a_follow_up_write_gets_no_notes_and_the_plain_prompt() (+10 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.11
Nodes (22): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions() (+14 more)

### Community 71 - "profile_evals.py"
Cohesion: 0.04
Nodes (73): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), pacer(), wait() (+65 more)

### Community 72 - "test_profile_context.py"
Cohesion: 0.15
Nodes (27): ContextReport, estimate_tokens(), _log(), NamedTuple, hashlib, default_strategy(), everything(), fingerprint() (+19 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "BaseModel"
Cohesion: 0.50
Nodes (4): FeedbackEvalQuestion, FeedbackEvalTurn, BaseModel, One main question with its follow-ups, as the score call sees a thread.

### Community 75 - "test_gateway.py"
Cohesion: 0.18
Nodes (19): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, 5. What can go wrong, test_a_vendor_failure_is_an_llm_error_with_its_attempts(), anyio_backend(), code_of(), fixture, parametrize (+11 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues, Links (+7 more)

### Community 77 - "json"
Cohesion: 0.12
Nodes (32): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, fit(), parse_profile_reply(), BaseModel (+24 more)

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
Cohesion: 0.07
Nodes (60): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_streamed_reply() (+52 more)

### Community 82 - "LLMError"
Cohesion: 0.05
Nodes (46): EmbeddingSizeError, A vector of another length than configured. Vectors of different sizes can't be…, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, LLMError, BaseModel, Exception (+38 more)

### Community 83 - "Embedder"
Cohesion: 0.08
Nodes (21): Embedder, Protocol, 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e) (+13 more)

### Community 84 - "interviews_constants.py"
Cohesion: 0.11
Nodes (40): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, StrEnum, QuestionKind, Why an interview has no reference notes at all (logged as… (+32 more)

### Community 85 - "pydantic"
Cohesion: 0.08
Nodes (32): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, UsersController (+24 more)

### Community 86 - "OpenAICompatibleProvider"
Cohesion: 0.10
Nodes (16): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+8 more)

### Community 87 - "EmbeddingKind"
Cohesion: 0.10
Nodes (28): EmbeddingKind, StrEnum, GoogleEmbedder, Any, BaseTransport, Random, Response, Clock (+20 more)

### Community 88 - "test_tracing.py"
Cohesion: 0.10
Nodes (10): client(), propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, _settings(), test_both_keys_build_an_enabled_tracer(), test_close_on_a_disabled_tracer_does_nothing(), test_no_keys_builds_a_disabled_tracer_without_warning() (+2 more)

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

### Community 93 - "provider.py"
Cohesion: 0.06
Nodes (54): anyio, DeepgramTranscriber, attempt(), _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over… (+46 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "LLMResult"
Cohesion: 0.07
Nodes (59): BuiltContext, ContextTooLargeError, Exception, Context management: the one place that decides what each LLM call sends. The…, Even with every droppable entry gone the input is over the strategy's limit., LLMProvider, LLMResult, Protocol (+51 more)

### Community 97 - "FakeClient"
Cohesion: 0.09
Nodes (11): FakeClient, FakeObservation, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_reports_whether_it_was_sent(), test_sdk_failure_does_not_mask_the_llm_error(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises(), test_steps_and_checks_are_no_ops_when_off_and_never_raise_when_langfuse_fails() (+3 more)

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

### Community 103 - "InterviewMessage"
Cohesion: 0.12
Nodes (18): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_a_future_question_is_not_current_either() (+10 more)

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

### Community 108 - "interviews_log.py"
Cohesion: 0.15
Nodes (14): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+6 more)

### Community 109 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 110 - "interview_report.py"
Cohesion: 0.15
Nodes (20): render_text(), html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is… (+12 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 112 - "Settings"
Cohesion: 0.07
Nodes (21): model_validator, Self, Settings, BaseSettings, Acceptance Criteria, Blockers, Constraints, Edge Cases (+13 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "load_prompt"
Cohesion: 0.08
Nodes (40): A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), load_prompt(), An interviews prompt by version (cached; the startup check reads every routed…, Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never… (+32 more)

### Community 115 - "Implementation: Prompt Registry"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Known Issues (+8 more)

### Community 116 - "test_profile_read_resume.py"
Cohesion: 0.22
Nodes (19): one_column(), pdf_text(), parametrize, read_resume: untrusted résumé bytes -> visible text in reading order, or a…, test_a_full_width_header_is_read_before_the_two_columns(), test_a_one_column_page_with_one_wide_gap_is_not_split(), test_a_pdf_over_five_pages_is_too_large(), test_a_real_pdf_is_read_whatever_its_name_would_have_been() (+11 more)

### Community 117 - "The fundamentals"
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 121 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "profile_resume_files.py"
Cohesion: 0.14
Nodes (22): _content(), _escape(), _fill(), Image, make_pdf(), plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build…, A PDF with one page per list. `encrypt` adds a standard security handler whose… (+14 more)

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
Cohesion: 0.21
Nodes (18): 5. What can go wrong, embedder(), first_question(), profile_of(), fixture, Starting an interview with the candidate's profile (resume-aware-interview Step…, A synthetic profile whose every free-text field carries `marker`, so a leak…, sent() (+10 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "profile_resume_utils.py"
Cohesion: 0.11
Nodes (28): Limits, thresholds and messages of the résumé upload (resume-upload spec)., _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _has_external_relationship() (+20 more)

### Community 134 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 135 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional, Out of Scope (+5 more)

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

### Community 140 - "ConsoleFormatter"
Cohesion: 0.36
Nodes (9): ConsoleFormatter, Dev console only: colours, and one field per line for `event key=value ...`…, sys, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success(), test_console_keeps_free_text_on_one_line(), test_console_puts_one_aligned_field_per_line() (+1 more)

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.24
Nodes (20): active(), chunks(), corpus(), FailingOn, interview(), ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag…, Fails on the n-th embed call (1-based), then works again., rows() (+12 more)

### Community 143 - "ContextManager"
Cohesion: 0.12
Nodes (28): ContextManager, Task, WindowLedger, Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go… (+20 more)

### Community 144 - "test_feedback_context.py"
Cohesion: 0.13
Nodes (29): FeedbackScore, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, The score call: every thread whole, nothing droppable. Over its own limit it…, build_threads() (+21 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_turn_budget.py"
Cohesion: 0.18
Nodes (16): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,… (+8 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_follow_ups.py"
Cohesion: 0.27
Nodes (16): answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries(), test_a_failed_follow_up_write_falls_back_to_the_next_main_bank_question() (+8 more)

### Community 151 - "interviews_start_dependencies.py"
Cohesion: 0.07
Nodes (67): get_llm_provider(), get_tracer(), get_transcriber(), Request, Built once at startup (app lifespan); None when no key is configured or the…, Built once at startup (app lifespan); a disabled tracer when the lifespan…, Built once at startup (app lifespan); None when no Deepgram key is configured…, get_db() (+59 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.13
Nodes (27): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+19 more)

### Community 156 - "CandidateProfile"
Cohesion: 0.18
Nodes (20): CandidateProfile, BaseModel, The candidate profile: what a résumé becomes, what is stored, and what the API…, The multipart upload: exactly one part, `file`. Extra form fields are refused., ResumeUploadIn, ExpectedProfile, _key(), BaseModel (+12 more)

### Community 157 - "Implementation: Interview Room (backend)"
Cohesion: 0.12
Nodes (16): Changes Made, Checkpoint after Step 5 (waiting for the user's review), Current Step, Debug Log, Deviations from Plan, Implementation: Interview Room (backend), Known Issues, Links (+8 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 160 - "follow_up"
Cohesion: 0.19
Nodes (12): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+4 more)

### Community 161 - "Tracer"
Cohesion: 0.03
Nodes (93): AbstractContextManager, build_tracer(), Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,… (+85 more)

### Community 162 - "VoiceService"
Cohesion: 0.19
Nodes (10): SessionNotInProgressError, UUID, The interview voice adapter, HTTP side: request -> VoiceService, domain result…, VoiceController, POST /interviews/{id}/transcriptions: what the candidate said, for them to…, TranscriptionOut, UUID, Only the owner of an interview in progress may transcribe for it; returns the… (+2 more)

### Community 163 - "Implementation: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Changes Made, Completed Steps, Current Step, Deviations from Plan, Gate: Step 10, real-model runs (yours), Implementation: Résumé-aware interview (Slice 8d), Known Issues, Links (+7 more)

### Community 164 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.11
Nodes (16): UUID, The user's stored profile for an interview prompt, read live (never copied onto…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me (+8 more)

### Community 165 - "test_answer_with_profile.py"
Cohesion: 0.25
Nodes (12): opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent(), test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile() (+4 more)

### Community 166 - "test_reaction_pick.py"
Cohesion: 0.23
Nodes (15): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), A predefined, neutral acknowledgement for the answer just given; never the same…, Project Conventions, pick(), parametrize, test_a_one_entry_pool_still_works() (+7 more)

### Community 167 - "llm"
Cohesion: 0.20
Nodes (8): as_v5_text(), llm(), script(), script_score(), script_write(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY…

### Community 168 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 169 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 170 - "JobRole"
Cohesion: 0.05
Nodes (91): NotEnoughQuestionsError, InterviewType, JobRole, Level, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), EvalSetup (+83 more)

### Community 171 - "traced"
Cohesion: 0.16
Nodes (21): drain(), result(), test_a_redacted_call_records_a_placeholder_instead_of_the_messages(), test_a_redacted_failure_records_no_partial_text(), test_a_redacted_stream_closed_early_records_no_partial_text(), test_a_redacted_success_keeps_model_usage_and_labels_but_not_the_reply(), test_an_unlabelled_call_still_records_full_content(), test_call_without_labels_still_gets_a_name() (+13 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.14
Nodes (17): Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+9 more)

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

### Community 178 - "Feature: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 179 - "Slices in detail"
Cohesion: 0.17
Nodes (12): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 6: Feedback and scoring, Slice 7: Eval maturity (trust the judge, catch regressions) (+4 more)

### Community 180 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.13
Nodes (14): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional (+6 more)

### Community 181 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 182 - "StreamedTurn"
Cohesion: 0.25
Nodes (6): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

### Community 183 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 184 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 185 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection

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

### Community 193 - "errors.py"
Cohesion: 0.03
Nodes (76): AppError, BadRequestError, ErrorBody, ErrorResponse, InvalidCredentialsError, ProfileExtractionFailedError, ProfileNotFoundError, ProfileUnavailableError (+68 more)

### Community 203 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Deviations (recorded during /implement), Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+1 more)

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.10
Nodes (16): 9. Still open, Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Known Issues, Links, Open Questions (+8 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.13
Nodes (25): Every interviews prompt version, and which one each LLM call sends. Data only:…, notes_fingerprint(), A short id for the ingested notes: changes when any note changes, not when the…, contextvars, A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and…, embedder(), labelled(), quiet() (+17 more)

### Community 220 - "main.py"
Cohesion: 0.06
Nodes (16): setup_logging(), Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, health_check(), ASGIApp, Architecture & Design, Receive, Scope (+8 more)

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

### Community 234 - "Implementation Plan: Résumé-aware interview (Slice 8d)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Decisions (grill-me, 2026-11-14), Deviations during implementation (2026-11-14, see task.md), Implementation Plan: Résumé-aware interview (Slice 8d), Overview, Ready to Implement, Skills Consulted (+2 more)

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
Cohesion: 0.04
Nodes (28): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, InterviewSessionChunk (+20 more)

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
Nodes (50): alias, AnswerControllerDep, ForbiddenError, get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check() (+42 more)

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.14
Nodes (13): 13. Phase 2 real runs (yours), Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

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
Cohesion: 0.11
Nodes (20): _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), job_term_hits(), _plain(), _posting_text(), Turn a fetched job page into plain job-description text (Slice 8b). Pure… (+12 more)

### Community 251 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 252 - "fixture"
Cohesion: 0.14
Nodes (14): answer(), _answer(), anyio_backend(), _decision_json(), fixture, POST an answer; `question_id` defaults to whatever the caller passes, body…, Builds a reply in the exact shape the decide call must produce., Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio… (+6 more)

### Community 253 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 255 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.18
Nodes (10): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slices (+2 more)

### Community 256 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 257 - "test_generation_eval.py"
Cohesion: 0.08
Nodes (51): parse_arms(), Read your filled-in sheet, print how often each arm ranked first, then post…, `--arms`: comma-separated arm letters (any case), at least two (a ranking…, run_ranking(), 5. What can go wrong, parametrize, The generation eval's arms D and E (resume-aware-interview Step 9a; seam S5).…, A fake LLM that keeps every prompt, answering each main question with a new… (+43 more)

### Community 258 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 259 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 260 - "test_profile_evals.py"
Cohesion: 0.21
Nodes (11): build_file(), EvalCase, BaseModel, The case as the file a candidate would upload. Hidden lines are white (PDF) or…, run_case(), LabelledModel, The profile eval runner offline: every synthetic case builds into a readable…, Answers each case with its own label, so the scores test the pipeline and the… (+3 more)

### Community 261 - "Learn: Résumé upload and the candidate profile (Slice 8c)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Résumé upload and the candidate profile (Slice 8c)

### Community 262 - "FakeLangfuse"
Cohesion: 0.09
Nodes (15): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+7 more)

### Community 263 - "re"
Cohesion: 0.25
Nodes (4): re, parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 265 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

### Community 266 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 267 - "Web"
Cohesion: 0.18
Nodes (6): get_page_fetcher(), Tests swap in a fetcher with a fake resolver and transport: no network., Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 268 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 269 - "InterviewQuestion"
Cohesion: 0.08
Nodes (23): InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Any, datetime, Session, UUID, Any user's session, by id: for the report script only (the API always goes… (+15 more)

### Community 270 - "bank"
Cohesion: 0.20
Nodes (10): Acceptance Criteria, Acceptance Criteria, Edge Cases, Functional, Non-Functional, Requirements, Test Results, Deviations from Plan (+2 more)

### Community 271 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 272 - "Feature: Job URL (Slice 8b)"
Cohesion: 0.20
Nodes (9): Blockers, Constraints, Feature: Job URL (Slice 8b), Goal, Out of Scope, Problem, Project Conventions, User Flow (+1 more)

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
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 290 - ".record_turn"
Cohesion: 0.05
Nodes (46): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, Save one whole turn in one commit: advance the session, the answer, the…, done(), Deviations from Plan, Affected Files & Patterns, 1. Why it exists, 2. What it is (+38 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 293 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+2 more)

### Community 294 - "text"
Cohesion: 0.25
Nodes (8): 1. Inventory every prompt (before writing any code), text(), 1. Inventory every prompt (before writing any code), Acceptance Criteria, Functional, Non-Functional, Paste fallback (added 2026-11-13), Requirements

### Community 295 - ".format"
Cohesion: 0.29
Nodes (5): `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, split_fields(), Edge Cases, test_split_fields_leaves_free_text_whole(), test_split_fields_reads_event_and_key_values()

### Community 296 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.33
Nodes (5): 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "profile_extract_v1.md"
Cohesion: 0.33
Nodes (5): Constraints, Input, Output, Role, Task

### Community 299 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.33
Nodes (5): 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 302 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 303 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 304 - "typing"
Cohesion: 0.11
Nodes (30): RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Per-user caps on paid speech calls. One limiter instance per process: every…, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later. (+22 more)

### Community 305 - "interviews_schema.py"
Cohesion: 0.06
Nodes (60): Criterion, MessageKind, MessageRole, What the score call rates, 1 to 5. Which ones apply depends on the question's…, Transcript item kinds: a question comes from interview_questions, the other two…, _error_event(), _event(), BaseModel (+52 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 315 - "interviews_feedback_service.py"
Cohesion: 0.13
Nodes (26): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, Who wrote the feedback text: the write call, or the code's template when that…, TextSource (+18 more)

## Knowledge Gaps
- **982 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+977 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2331 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **50 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LLMError` connect `LLMError` to `LLMServerError`, `Completed Steps`, `interviews_start_dependencies.py`, `interviews_rag_evals.py`, `ingest_corpus`, `Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `JobRole`, `test_evals.py`, `QuestionCategory`, `Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `interviews_feedback_service.py`, `interviews_service.py`, `Implementation Steps`, `FakeEmbedder`, `test_stream_turn.py`, `test_gateway.py`, `interviews_evals.py`, `interviews_constants.py`, `OpenAICompatibleProvider`, `EmbeddingKind`, `provider.py`, `LLMResult`, `Settings`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `test_generation_eval.py`, `test_profile_evals.py`, `FakeLangfuse`, `Completed Steps`, `experiments`, `test_feedback_evals.py`, `interviews_start_dependencies.py`, `interviews_answer_service.py`, `test_feedback_endpoint.py`, `interviews_rag_evals.py`, `traced`, `traces`, `ProfileLLM`, `typing`, `test_evals.py`, `Feature: Langfuse experiments for the interviews evals`, `interviews_feedback_service.py`, `test_tracing_routes.py`, `interviews_service.py`, `errors.py`, `test_profile_routes.py`, `profile_evals.py`, `interviews_evals.py`, `LLMError`, `Embedder`, `interviews_constants.py`, `test_retrieval_eval.py`, `test_tracing.py`, `provider.py`, `LLMResult`, `FakeClient`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `test_tracing_lifespan.py`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `test_evals.py` to `QuestionTurn`, `test_profile_evals.py`, `Feature: Interview Feedback and Scoring (Slice 6)`, `ContextManager`, `interviews_answer_service.py`, `interviews_rag_evals.py`, `Feature: Context Management for the Interview LLM Calls`, `Tracer`, `.record_turn`, `test_reaction_pick.py`, `llm`, `JobRole`, `traced`, `ProfileLLM`, `Slices in detail`, `test_profile_routes.py`, `LLMError`, `interviews_constants.py`, `test_tracing.py`, `provider.py`, `LLMResult`, `Implementation Plan: Résumé upload and candidate profile (Slice 8c)`, `AI Engineering Learning Path (Cuewise)`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Are the 49 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 49 INFERRED edges - model-reasoned connections that need verification._
- **Are the 40 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 29 INFERRED edges - model-reasoned connections that need verification._
- **Are the 69 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 69 INFERRED edges - model-reasoned connections that need verification._