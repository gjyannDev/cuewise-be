# Graph Report - cuewise-be  (2026-11-15)

## Corpus Check
- 448 files · ~393,482 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 6073 nodes · 17112 edges · 320 communities (259 shown, 61 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 3167 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c4d500a4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- QuestionTurn
- provider.py
- test_profile_eval_metrics.py
- config.py
- test_interview_report.py
- typing
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
- test_select_questions.py
- test_prompt_registry.py
- cuewise-be
- profile_dependencies.py
- interviews_answer_service.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- interviews_rag_evals.py
- Feature: Context Management for the Interview LLM Calls
- Feature: Layered Modules (route -> controller -> service -> repository)
- KnowledgeRepository
- LLMResult
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
- interviews_model.py
- InterviewerInputs
- profile_controller.py
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- ReferenceNote
- test_tracing_routes.py
- test_context_controller.py
- SessionStatus
- job_description_summary_v2.md
- errors.py
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- test_reference_note_context.py
- test_answer_llm.py
- interviews_feedback_evals.py
- test_profile_context.py
- exception_handlers.py
- FeedbackEvalQuestion
- test_generation_arms.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- re
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- interviews_evals.py
- ChatMessage
- Embedder
- FollowUpAction
- User
- LLMBadResponseError
- EmbeddingKind
- test_tracing.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- profile_schema.py
- fake.py
- Langfuse Observability
- interviewer_v3.md
- interviews_context.py
- FakeClient
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- ProviderConfig
- test_get_interview.py
- ground_profile
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_log.py
- test_reply_contract.py
- main
- Implementation: Eval runs in Langfuse (scores + datasets)
- Feature: Langfuse Tracing
- Langfuse
- test_streamed_reply.py
- Implementation: Prompt Registry
- audio_container
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- test_guards.py
- types.py
- Feature: Agentic Workflow v2 (debug, review-feature, gated loop)
- test_profile_read_resume.py
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
- LLMProvider
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- ConsoleFormatter
- test_knowledge_ingest.py
- test_context.py
- test_feedback_context.py
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- test_follow_ups.py
- interviews/conftest.py
- Implementation: Agentic Workflow v2
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- CandidateProfile
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- scrub_contacts
- follow_up
- Tracer
- read_rankings
- Implementation: Résumé-aware interview (Slice 8d)
- Learn: Résumé-aware interview (Slice 8d)
- json
- done
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
- test_profile_redaction.py
- test_stream_answer.py
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
- require_permissions
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
- profile_service.py
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
- test_fallback_pick.py
- Implementation Plan: UUID primary keys
- Langfuse CLI Reference
- test_generation_eval.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- test_answer_interview.py
- test_profile_evals.py
- Learn: Résumé upload and the candidate profile (Slice 8c)
- FakeLangfuse
- pytest
- ._ordered
- lf
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- limit_job_imports
- experiments
- InterviewQuestion
- FakeStream
- test_job_description_summary.py
- Affected Files & Patterns
- check_layers
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- Langfuse
- clock
- interviews_reply.py
- Langfuse Observability
- Implementation Plan: Follow-up Questions (decide / write split)
- Learn: Splitting the interviews dependency wiring
- Learn: Layered architecture (route -> controller -> service -> repository)
- fixture
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Learn: Adding interview roles (designer, qa, devops)
- Learn: Langfuse experiments for the interviews evals
- traces
- interviews_prompt_registry.py
- ProfileLLM
- 2. Langfuse Documentation
- test_keyterms.py
- test_user_ids.py
- interviews_constants.py
- Implementation Steps
- interviews_feedback_service.py
- cuewise-be

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
- `6. Try it yourself` --references--> `get_tracer()`  [INFERRED]
  docs/features/split-interviews-dependencies/learnings.md → app/core/ai/dependencies.py
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Constraints` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py

## Import Cycles
- None detected.

## Communities (320 total, 61 thin omitted)

### Community 0 - "QuestionTurn"
Cohesion: 0.06
Nodes (56): StrategyOutput, _counts(), FeedbackWrite, FeedbackWriteInputs, JobDescriptionSummary, NamedTuple, An earlier question as the model would have written it. A follow-up was written…, App data at the end of the last user message; untrusted parts (questions,… (+48 more)

### Community 1 - "provider.py"
Cohesion: 0.11
Nodes (34): Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, Gemini embeddings through Google's native `batchEmbedContents` endpoint, over…, LLMRateLimitError, LLMRequestError, LLMServerError, The LLM contract every feature codes against: message/result types, typed…, 5xx or a dropped connection: the provider's side failed., Other 4xx (bad key, bad request): retrying sends the same broken request again. (+26 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.08
Nodes (51): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, _injection_share(), _mention_share(), notes_overlap() (+43 more)

### Community 3 - "config.py"
Cohesion: 0.10
Nodes (35): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+27 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.11
Nodes (57): log_retrieval(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, Which reference notes an interview got at start: mode, count, scores, how many…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn() (+49 more)

### Community 5 - "typing"
Cohesion: 0.07
Nodes (54): The speech-to-text contract features code against, separate from the text-only…, RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., hash_password(), verify_password(), Permission, permissions_for(), StrEnum (+46 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.13
Nodes (35): extract_job_text(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, At most `limit` characters, cut at the last whitespace so no word is split;…, truncate_on_word(), jsonld(), page() (+27 more)

### Community 8 - "Completed Steps"
Cohesion: 0.12
Nodes (27): Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, EligibleChunk, NamedTuple, The k eligible chunks embedded with `model` that are most similar to the query,…, _degrade_reason() (+19 more)

### Community 9 - "tests/conftest.py"
Cohesion: 0.08
Nodes (27): health_check(), list_users(), PageDep, CurrentUserDep, sqlalchemy_pool, client(), db(), make_user() (+19 more)

### Community 10 - "WithInterviewData"
Cohesion: 0.07
Nodes (36): lifespan(), FastAPI, build_context_manager(), FullHistory, A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WithInterviewData (+28 more)

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

### Community 16 - "test_feedback_contract.py"
Cohesion: 0.16
Nodes (36): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+28 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.06
Nodes (69): check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult, FeedbackEvalCase (+61 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (41): Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request, Response (+33 more)

### Community 19 - "test_select_questions.py"
Cohesion: 0.19
Nodes (22): NotEnoughQuestionsError, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 4. How it works, Implementation Steps, Testing Strategy, _bank(), parametrize (+14 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.06
Nodes (48): Data, PromptVersion, StrEnum, What an interviewer write carries beyond the job description; it picks the…, Status, check_prompts(), PromptCheckError, Exception (+40 more)

### Community 26 - "profile_dependencies.py"
Cohesion: 0.08
Nodes (30): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, get_profile_clock(), get_profile_controller(), get_profile_now(), get_resume_limiter(), limit_resume_uploads() (+22 more)

### Community 27 - "interviews_answer_service.py"
Cohesion: 0.06
Nodes (66): QuestionNotCurrentError, PhaseChanged, The question text streamed so far is taken back: that draft failed, another one…, Reset, The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), AnswerController (+58 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.07
Nodes (74): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists, 2. What it is, 3. When to use it (+66 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.09
Nodes (16): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+8 more)

### Community 31 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.15
Nodes (11): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 32 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (83): _arm_notes(), ArmInterview, ArmSummary, case_set_problems(), competencies_of(), ExtraSetup, filter_baseline(), generation_item() (+75 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 35 - "KnowledgeRepository"
Cohesion: 0.12
Nodes (20): KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, _embed(), ingest_corpus(), IngestCounts, NamedTuple (+12 more)

### Community 36 - "LLMResult"
Cohesion: 0.08
Nodes (32): BuiltContext, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, LLMResult, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, ScoreResult, _Attempts (+24 more)

### Community 37 - "4. How it works"
Cohesion: 0.07
Nodes (29): _decode(), FetchedPage, FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach… (+21 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.11
Nodes (19): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+11 more)

### Community 39 - "interviews_knowledge_utils.py"
Cohesion: 0.08
Nodes (48): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, main(), _parser(), ArgumentParser, Session, Ingest the reference notes into the database (knowledge-base RAG). uv run…, _check_hidden() (+40 more)

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
Cohesion: 0.13
Nodes (30): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, Any network-side failure of a job link. One message for every cause, so…, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError (+22 more)

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
Nodes (95): FakeProvider, load_cases(), main(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, run_case(), 5. What can go wrong (+87 more)

### Community 49 - "interviews_feedback.py"
Cohesion: 0.11
Nodes (34): _check_lengths(), Evidence, FeedbackThread, _has_markup(), _normalized(), parse_write_reply(), BaseModel, NamedTuple (+26 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.07
Nodes (52): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+44 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.09
Nodes (49): InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, apply_limits(), Deadline, _decision_label(), plan_write() (+41 more)

### Community 52 - "profile_controller.py"
Cohesion: 0.15
Nodes (16): _out(), ProfileController, The signed-in user's résumé profile: request -> ProfileService, stored row ->…, delete_profile(), get_profile(), post, ProfileUser, A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes… (+8 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (21): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+13 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.11
Nodes (43): 5. What can go wrong, Open Questions, auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, fail(), error(), import_url() (+35 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (26): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), _make(), ok() (+18 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.09
Nodes (53): analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table(), Checks, bad_parent() (+45 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.10
Nodes (35): Clock, completion(), make_provider(), _make(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant. (+27 more)

### Community 59 - "ReferenceNote"
Cohesion: 0.27
Nodes (16): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, A note an interview was given: what the question writer sees (competency and…, ReferenceNote, names(), ranked(), merge_note_rankings: the quota merge of the job-description and profile…, Notes named by single letters, ranked in the given order with falling scores. (+8 more)

### Community 61 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 62 - "SessionStatus"
Cohesion: 0.11
Nodes (31): HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, interview_out(), InterviewsController, UUID, question_out() (+23 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "errors.py"
Cohesion: 0.07
Nodes (40): Protocol, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody (+32 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.12
Nodes (40): EmbedCall, FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), embedder_for(), RetrievalService.retrieve with the candidate profile's query (resume-aware-… (+32 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.18
Nodes (29): Delta, The next chunk of the question being written (shown as it arrives)., What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, collect(), follow_up_json(), inputs(), kinds() (+21 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (37): 5. What can go wrong, profile_json(), Synthetic résumé data and the scripted model shared by the profile tests (no…, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,… (+29 more)

### Community 68 - "test_reference_note_context.py"
Cohesion: 0.14
Nodes (26): Task, WindowLedger, 5. What can go wrong, test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), manager(), first_user(), inputs() (+18 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.13
Nodes (19): 2. What it is, Learning Log (`learnings.md`), Known Follow-ups (story 3: Chat with the interviewer), messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview(), test_a_double_submit_stores_one_answer_and_makes_one_call() (+11 more)

### Community 71 - "interviews_feedback_evals.py"
Cohesion: 0.04
Nodes (101): build_tracer(), ExperimentRun, NamedTuple, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, What a recorded experiment run left behind: its name and link, and the trace of…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, _evaluation() (+93 more)

### Community 72 - "test_profile_context.py"
Cohesion: 0.20
Nodes (23): estimate_tokens(), default_strategy(), everything(), fingerprint(), golden_inputs(), inputs(), manager_for(), max_profile() (+15 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 75 - "test_generation_arms.py"
Cohesion: 0.13
Nodes (19): parse_arms(), `--arms`: comma-separated arm letters (any case), at least two (a ranking…, parametrize, The generation eval's arms D and E (resume-aware-interview Step 9a; seam S5).…, A fake LLM that keeps every prompt, answering each main question with a new…, RecordingWriter, run(), test_arms_are_parsed_case_insensitively_in_a_fixed_order() (+11 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues, Links (+7 more)

### Community 77 - "re"
Cohesion: 0.10
Nodes (39): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, build_messages(), extract_profile(), Extraction (+31 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.12
Nodes (15): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions (+7 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "interviews_evals.py"
Cohesion: 0.05
Nodes (90): anyio_from_thread, The job-description summary replaces the original on every later call, so it…, validate_summary(), _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check (+82 more)

### Community 82 - "ChatMessage"
Cohesion: 0.05
Nodes (60): build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, OpenAICompatibleProvider, ReasoningEffort (+52 more)

### Community 83 - "Embedder"
Cohesion: 0.06
Nodes (32): Embedder, Protocol, 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e) (+24 more)

### Community 84 - "FollowUpAction"
Cohesion: 0.16
Nodes (20): FollowUpDecision, The decide call: the current thread in full (it judges the latest answer within…, parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid… (+12 more)

### Community 85 - "User"
Cohesion: 0.05
Nodes (69): NotFoundError, ProfileRequiredError, An interview asked to use the candidate's profile, and there is none to use…, Page, page_params(), PageParams, BaseModel, NamedTuple (+61 more)

### Community 86 - "LLMBadResponseError"
Cohesion: 0.13
Nodes (15): _parse(), Response, The first channel's best transcript (blank for silence) and the reported audio…, _int_or_none(), Any, AsyncBaseTransport, BaseTransport, Random (+7 more)

### Community 87 - "EmbeddingKind"
Cohesion: 0.09
Nodes (33): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, GoogleEmbedder (+25 more)

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

### Community 92 - "profile_schema.py"
Cohesion: 0.16
Nodes (25): candidate_profile_block(), profile_query_text(), The candidate profile as interview input: a fenced prompt block and a short…, The profile fenced as data, like the job description. Summaries and…, The profile's short items as one retrieval query. None: nothing to embed., Project, BaseModel, The candidate profile: what a résumé becomes, what is stored, and what the API… (+17 more)

### Community 93 - "fake.py"
Cohesion: 0.07
Nodes (23): anyio, DeepgramTranscriber, AsyncBaseTransport, Random, FakeTranscriber, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or…, Scripted transcripts (text, a full result, or an error), one per call; records…, LLMTimeoutError (+15 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "interviews_context.py"
Cohesion: 0.10
Nodes (39): ContextManager, ContextReport, ContextTooLargeError, _log(), Exception, NamedTuple, Context management: the one place that decides what each LLM call sends. The…, Even with every droppable entry gone the input is over the strategy's limit. (+31 more)

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

### Community 103 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "ground_profile"
Cohesion: 0.16
Nodes (23): EmptyProfileError, Exception, No skills and no roles: not a résumé we can use (refused as unreadable, nothing…, _appears(), ground_profile(), keep(), _normalized(), _phone_or_keep() (+15 more)

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

### Community 110 - "main"
Cohesion: 0.10
Nodes (31): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+23 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional (+6 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "test_streamed_reply.py"
Cohesion: 0.18
Nodes (17): interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), read(), parse(), parametrize, interviewer_v5's streamed reply: a `CATEGORY:` header line (next-question mode…, test_a_header_split_across_chunks_is_read_once_its_line_ends(), test_a_long_first_line_is_no_header_without_waiting_for_its_end() (+9 more)

### Community 115 - "Implementation: Prompt Registry"
Cohesion: 0.11
Nodes (17): 10. Profile module uses the shared loader (next), Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry (+9 more)

### Community 116 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

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
Cohesion: 0.18
Nodes (15): _assert_401(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access(), test_guards_allow_or_forbid_by_db_role(), test_missing_header_is_token_missing(), test_non_bearer_or_empty_token_is_token_missing() (+7 more)

### Community 121 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "test_profile_read_resume.py"
Cohesion: 0.08
Nodes (60): _content(), _escape(), _fill(), Image, make_docx(), make_pdf(), plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build… (+52 more)

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

### Community 135 - "LLMProvider"
Cohesion: 0.05
Nodes (37): LLMProvider, Protocol, datetime, AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid) (+29 more)

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
Cohesion: 0.05
Nodes (42): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites, ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message… (+34 more)

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.21
Nodes (23): IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, active(), chunks(), corpus(), FailingOn, interview() (+15 more)

### Community 143 - "test_context.py"
Cohesion: 0.18
Nodes (14): Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default(), test_a_strategy_without_a_limit_is_never_trimmed() (+6 more)

### Community 144 - "test_feedback_context.py"
Cohesion: 0.30
Nodes (16): FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, Step 4 of the feedback plan: what the score and write calls send, through the…, score_inputs(), scored(), test_an_answer_over_the_cap_is_shortened_and_counted_but_quotes_still_verify(), test_an_interview_over_the_limit_raises_instead_of_dropping_an_answer(), test_closing_tags_inside_untrusted_text_are_neutralised() (+8 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_turn_budget.py"
Cohesion: 0.20
Nodes (15): Baseline Failures, Baseline Failures, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result() (+7 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): 5. What can go wrong, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 151 - "interviews/conftest.py"
Cohesion: 0.08
Nodes (61): get_llm_provider(), get_tracer(), Request, Request dependencies for the AI services every feature shares, built once at…, Built once at startup (app lifespan); None when no key is configured or the…, Built once at startup (app lifespan); a disabled tracer when the lifespan…, get_db(), Session (+53 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Skills Consulted During Implementation, Status (+4 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.13
Nodes (27): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+19 more)

### Community 156 - "CandidateProfile"
Cohesion: 0.16
Nodes (22): Constraints, Input, Output, Role, Task, CandidateProfile, ExpectedProfile, _key() (+14 more)

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.42
Nodes (9): ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1(), test_an_invalid_note_names_the_file_writes_nothing_and_exits_1(), test_it_prints_the_counts_and_exits_0(), test_warnings_are_printed_without_note_text(), test_without_the_google_key_it_says_what_to_set_and_exits_1() (+1 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "scrub_contacts"
Cohesion: 0.30
Nodes (11): The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed(), test_phone_numbers_in_common_formats_are_removed(), test_several_contacts_in_one_line_are_all_removed() (+3 more)

### Community 160 - "follow_up"
Cohesion: 0.16
Nodes (13): Slice 3: Structured follow-up decisions, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+5 more)

### Community 161 - "Tracer"
Cohesion: 0.04
Nodes (52): AbstractContextManager, Generation, Any, The stream was closed before it finished (client left, or the turn's deadline…, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable… (+44 more)

### Community 162 - "read_rankings"
Cohesion: 0.19
Nodes (17): build_sheet(), Exception, _ranking(), The grading file can't be read; the message starts with the line and gives the…, One block per setup with each arm's question set under a neutral label in a…, Every setup of the key must have one complete ranking; anything else, and any…, read_rankings(), SheetError (+9 more)

### Community 163 - "Implementation: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Changes Made, Completed Steps, Current Step, Deviations from Plan, Gate: Step 10, real-model runs (yours), Implementation: Résumé-aware interview (Slice 8d), Known Issues, Links (+7 more)

### Community 164 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.11
Nodes (16): UUID, The user's stored profile for an interview prompt, read live (never copied onto…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me (+8 more)

### Community 165 - "json"
Cohesion: 0.23
Nodes (13): json, opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent() (+5 more)

### Community 166 - "done"
Cohesion: 0.14
Nodes (16): done(), Deviations from Plan, Step 2: Event contract, Testing Strategy, Acceptance Criteria, Blockers, Constraints, Edge Cases (+8 more)

### Community 167 - "llm"
Cohesion: 0.16
Nodes (11): as_v5_text(), _decision_json(), llm(), script(), script_decide(), script_score(), script_write(), unique_question() (+3 more)

### Community 168 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 169 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 170 - "JobRole"
Cohesion: 0.05
Nodes (87): A running note is optional model output about the latest answer; it is sent…, validate_note(), InterviewType, JobRole, Level, Every check and read of an answer turn, before any LLM call. Raises the usual…, EvalSetup, FeedbackEvalSetup (+79 more)

### Community 171 - "traced"
Cohesion: 0.24
Nodes (15): result(), test_a_redacted_call_records_a_placeholder_instead_of_the_messages(), test_a_redacted_success_keeps_model_usage_and_labels_but_not_the_reply(), test_an_unlabelled_call_still_records_full_content(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage(), test_failed_call_is_marked_error_and_the_same_exception_is_raised(), test_missing_usage_is_omitted_never_guessed() (+7 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.15
Nodes (16): Baseline Failures, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL), Testing Strategy (+8 more)

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

### Community 178 - "test_profile_redaction.py"
Cohesion: 0.32
Nodes (14): assert_redacted(), assert_traced_in_full(), generations(), inputs(), anyio, resume-aware-interview Step 5: a write whose prompt carries the profile is…, run_stream_write(), run_write() (+6 more)

### Community 179 - "test_stream_answer.py"
Cohesion: 0.12
Nodes (22): Save one whole turn in one commit: advance the session, the answer, the…, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+14 more)

### Community 180 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.13
Nodes (14): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional (+6 more)

### Community 181 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 182 - "StreamedTurn"
Cohesion: 0.15
Nodes (11): parse_sse(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json() (+3 more)

### Community 183 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 184 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 185 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

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

### Community 193 - "require_permissions"
Cohesion: 0.03
Nodes (86): ErrorResponse, ForbiddenError, RequestIdFilter, get_current_user(), Depends, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions() (+78 more)

### Community 203 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.17
Nodes (10): Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., Affected Files & Patterns, Blockers & Resolutions, Implementation Deviations (recorded during /implement), Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement (+2 more)

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.18
Nodes (21): embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, 15 cases with the kinds the label rules require: most expect API design first;…, run() (+13 more)

### Community 220 - "main.py"
Cohesion: 0.07
Nodes (15): setup_logging(), Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send (+7 more)

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
Cohesion: 0.17
Nodes (11): Architecture & Design, Blockers & Resolutions, Decisions (grill-me, 2026-11-14), Deviations during implementation (2026-11-14, see task.md), Implementation Plan: Résumé-aware interview (Slice 8d), Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "profile_service.py"
Cohesion: 0.08
Nodes (35): ProfileExtractionFailedError, ProfileNotFoundError, ProfileUnavailableError, Over the byte, page or unzipped-size limit of a résumé upload., Not a PDF or a Word document by its content (the file name is never trusted)., Encrypted, corrupt, scanned, too little text, or no usable profile in it., The model gave no valid profile after the retry, timed out, or the provider…, ResumeTooLargeError (+27 more)

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
Cohesion: 0.07
Nodes (42): alias, AnswerControllerDep, UUID, Voice answers: request -> TranscriptionService, text -> TranscriptionOut. The…, TranscriptionController, answer_question(), answer_question_stream(), generate_feedback() (+34 more)

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
Cohesion: 0.12
Nodes (19): _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), job_term_hits(), _plain(), _posting_text(), Turn a fetched job page into plain job-description text (Slice 8b). Pure… (+11 more)

### Community 251 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 252 - "fixture"
Cohesion: 0.17
Nodes (12): answer(), _answer(), anyio_backend(), fixture, POST an answer; `question_id` defaults to whatever the caller passes, body…, Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a recording to the transcription endpoint; `audio=None` sends no file part…, POST a setup for `user`; any field can be overridden, or dropped by passing… (+4 more)

### Community 253 - "test_fallback_pick.py"
Cohesion: 0.27
Nodes (11): fixture_bank(), pick(), fixture, parametrize, test_general_and_role_specific_questions_are_both_eligible(), test_level_must_match(), test_mixed_alternates_starting_with_behavioral(), test_nothing_left_raises() (+3 more)

### Community 255 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 256 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 257 - "test_generation_eval.py"
Cohesion: 0.15
Nodes (32): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), arm_of(), fill(), generated(), posted(), parametrize, quiet() (+24 more)

### Community 258 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 259 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 260 - "test_profile_evals.py"
Cohesion: 0.11
Nodes (19): ExtractionFailedError, Exception, No valid profile: `reason` is invalid_reply, empty_reply, no_time or the…, build_file(), EvalCase, load_cases(), BaseModel, Path (+11 more)

### Community 261 - "Learn: Résumé upload and the candidate profile (Slice 8c)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Résumé upload and the candidate profile (Slice 8c)

### Community 262 - "FakeLangfuse"
Cohesion: 0.09
Nodes (15): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+7 more)

### Community 263 - "pytest"
Cohesion: 0.25
Nodes (4): pytest, parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 265 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

### Community 266 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 267 - "limit_job_imports"
Cohesion: 0.11
Nodes (15): get_job_url_controller(), get_job_url_limiter(), get_job_url_service(), get_page_fetcher(), limit_job_imports(), Depends, interviews_create, Tests swap in a fresh limiter so counts never leak between them. (+7 more)

### Community 268 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 269 - "InterviewQuestion"
Cohesion: 0.06
Nodes (44): InterviewMessage, InterviewQuestion, InterviewSession, A candidate answer or the interviewer's reaction to one question. The questions…, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Any, datetime (+36 more)

### Community 270 - "FakeStream"
Cohesion: 0.25
Nodes (9): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, drain(), test_a_redacted_failure_records_no_partial_text(), test_a_redacted_stream_closed_early_records_no_partial_text(), test_stream_closed_early_is_warning_cancelled_with_partial_text(), test_stream_failure_is_error_with_partial_text_and_reraised() (+1 more)

### Community 271 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 272 - "Affected Files & Patterns"
Cohesion: 0.29
Nodes (6): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Affected Files & Patterns

### Community 273 - "check_layers"
Cohesion: 0.25
Nodes (8): Blockers & Resolutions, Known Issues, check_layers(), _imports(), Every layer-rule violation in `files` (repo-relative path -> source), as…, (absolute module, imported names) per import statement; relative imports…, test_clean_layer_imports_have_no_violations(), _violation()

### Community 274 - "Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 275 - "Implementation Plan: Agentic Workflow v2"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: Agentic Workflow v2, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 276 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 277 - "clock"
Cohesion: 0.33
Nodes (4): 9. Still open, Known Issues, clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 290 - "interviews_reply.py"
Cohesion: 0.07
Nodes (35): _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_interviewer_reply(), parse_streamed_reply(), BaseModel, NamedTuple (+27 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 293 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+2 more)

### Community 294 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository)

### Community 295 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 296 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

### Community 297 - "Learn: Adding interview roles (designer, qa, devops)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, Learn: Adding interview roles (designer, qa, devops)

### Community 298 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 299 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 300 - "interviews_prompt_registry.py"
Cohesion: 0.33
Nodes (4): Every interviews prompt version, and which one each LLM call sends. Data only:…, contextvars, A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and…, types

### Community 302 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 303 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 304 - "test_user_ids.py"
Cohesion: 0.70
Nodes (4): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7()

### Community 305 - "interviews_constants.py"
Cohesion: 0.07
Nodes (60): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, FeedbackStatus, LevelGroup, MessageKind, MessageRole, StrEnum, QuestionCategory (+52 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 315 - "interviews_feedback_service.py"
Cohesion: 0.13
Nodes (24): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackScoreInputs, Plain values for the score call: the whole interview, read once the interview… (+16 more)

## Knowledge Gaps
- **961 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+956 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2283 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **61 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `test_generation_eval.py`, `test_profile_evals.py`, `FakeLangfuse`, `LLMProvider`, `Completed Steps`, `experiments`, `test_feedback_evals.py`, `test_prompt_registry.py`, `interviews/conftest.py`, `interviews_answer_service.py`, `test_feedback_endpoint.py`, `interviews_rag_evals.py`, `LLMResult`, `traced`, `traces`, `ProfileLLM`, `test_evals.py`, `test_profile_redaction.py`, `Feature: Langfuse experiments for the interviews evals`, `interviews_feedback_service.py`, `test_tracing_routes.py`, `test_profile_routes.py`, `interviews_feedback_evals.py`, `interviews_evals.py`, `ChatMessage`, `Embedder`, `test_retrieval_eval.py`, `User`, `test_tracing.py`, `FakeClient`, `Implementation: Eval runs in Langfuse (scores + datasets)`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `config.py`, `typing`, `tests/conftest.py`, `limit_job_imports`, `InterviewQuestion`, `interviews/conftest.py`, `profile_dependencies.py`, `interviews_answer_service.py`, `JobRole`, `interviews_job_url_service.py`, `interviews_constants.py`, `interviews_model.py`, `profile_controller.py`, `test_create_interview.py`, `interviews_feedback_service.py`, `SessionStatus`, `errors.py`, `require_permissions`, `Implementation: Langfuse Tracing`, `profile_service.py`, `interviews_route.py`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `provider.py`, `test_generation_eval.py`, `test_profile_evals.py`, `test_job_description_summary.py`, `test_feedback_evals.py`, `test_turn_budget.py`, `Tracer`, `interviews_reply.py`, `JobRole`, `traced`, `test_evals.py`, `interviews_constants.py`, `InterviewerInputs`, `test_start_llm.py`, `test_openai_compatible_stream.py`, `interviews_feedback_service.py`, `test_answer_llm.py`, `interviews_feedback_evals.py`, `test_generation_arms.py`, `re`, `interviews_evals.py`, `ChatMessage`, `User`, `LLMBadResponseError`, `test_tracing.py`, `fake.py`, `interviews_context.py`, `profile_service.py`, `Feature: Langfuse Tracing`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Are the 49 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 49 INFERRED edges - model-reasoned connections that need verification._
- **Are the 40 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Are the 29 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 29 INFERRED edges - model-reasoned connections that need verification._
- **Are the 69 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 69 INFERRED edges - model-reasoned connections that need verification._