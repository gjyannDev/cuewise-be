# Graph Report - cuewise-be  (2026-11-27)

## Corpus Check
- 524 files · ~493,910 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 9 file(s) not represented in the graph (top: (none) 4, .example 1, .ini 1)

## Summary
- 7464 nodes · 21408 edges · 356 communities (294 shown, 62 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 4126 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3b44fef2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _ScriptedClient
- LLMServerError
- test_profile_eval_metrics.py
- decode_token
- test_interview_report.py
- auth_service.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- RetrievalService
- test_summary_evals.py
- profile_route.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- FakeClient
- test_feedback_evals.py
- test_safe_fetch.py
- test_knowledge_ingest.py
- test_prompt_registry.py
- cuewise-be
- AppLogs
- ReplyAttempts
- test_feedback_endpoint.py
- test_context_strategies.py
- Interviewer
- OpenAICompatibleProvider
- test_tracing.py
- Feature: Context Management for the Interview LLM Calls
- FakeChatModel
- test_context.py
- User
- profile_service.py
- FakeProvider
- test_knowledge_utils.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- test_chat_contract.py
- test_chat_stream.py
- test_write.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_langchain_behaviour.py
- JobUrlService
- test_request_context.py
- LLMResult
- errors.py
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- interviews_knowledge_utils.py
- test_tracing_routes.py
- ProviderChatModel
- Rules
- job_description_summary_v2.md
- test_evals.py
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- test_feedback_contract.py
- InterviewQuestion
- test_feedback_turn.py
- build_chat_model
- exception_handlers.py
- app_logs
- test_gateway.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- InvalidReplyError
- failed
- Langfuse
- interviews_report_render.py
- interviews_evals.py
- StreamedTurn
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- complete_chat
- .speech
- LLMError
- EmbeddingKind
- InterviewsRepository
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- CandidateProfile
- test_retrieval_profile_cases.py
- Langfuse Observability
- interviewer_v3.md
- test_context_controller.py
- json
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_speech.py
- interviews_answer_service.py
- provider.py
- test_answer_stream.py
- Langfuse Dataset Construction
- parse_log
- Feature: Résumé upload and candidate profile (Slice 8c)
- PromptCheckError
- test_follow_ups.py
- Feature: Langfuse Tracing
- Langfuse
- JobRole
- merge_note_rankings
- test_decide.py
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- PageParams
- AI Engineering Learning Path (Cuewise)
- Feature: Agentic Workflow v2 (debug, review-feature, gated loop)
- Implementation Plan: Context Management for the Interview LLM Calls
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_profile_extract.py
- Implementation Plan: U1 structlog (structured JSON logs)
- Feature: Résumé-aware interview (Slice 8d)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- test_knowledge_ingest_cli.py
- Implementation: Interview History List (backend)
- Judge Calibration
- 4. How it works
- build_usage_report
- Blind ranking
- Langfuse CI/CD
- Prompt Engineering
- safe_fetch.py
- Langfuse Implementation Notes
- stream_chat
- 4. How it works
- QuestionTurn
- ._generate
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- test_reply_contract.py
- interviews_feedback_controller.py
- Implementation: Agentic Workflow v2
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- Feature: Langfuse experiments for the interviews evals
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- audio_container
- profile_reply.py
- Tracer
- test_transcript.py
- test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only
- test_start_with_profile.py
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Implementation: LLM as the Interviewer (it asks the questions)
- profile_extract.py
- Implementation: U1 structlog (structured JSON logs)
- LLMTimeoutError
- ._ordered
- LLMProvider
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- request_log_context
- feedback_score_v1.md
- feedback_write_v1.md
- check_core
- interviews_model.py
- make_user
- auth_header
- interviews_rag_evals.py
- LogCapture
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- parse_write_reply
- AnswerIn
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- ErrorResponse
- pytest
- Implementation: Three New Interview Roles (designer, qa, devops)
- KnowledgeRepository
- LLMBadResponseError
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
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
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
- scrub_contacts
- interviews_context.py
- Implementation: Prompt Registry
- follow_up
- test_speech_contracts.py
- check_layers
- QuestionCategory
- _formatter
- 4. How it works
- Implementation: Layered Modules (route -> controller -> service -> repository)
- 5. What can go wrong
- interviews_answer_dependencies.py
- Learn: Splitting the interviews dependency wiring
- Implementation: Start an Interview (backend)
- test_factory.py
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- _StderrHandler
- RateLimiter
- Langfuse Observability
- hint_for
- Feature: Follow-up Questions (decide / write split)
- get_logger
- Learn: Adding interview roles (designer, qa, devops)
- .record_turn
- Langfuse Prompt Migration
- html_target
- U0 baselines
- Langfuse Prompt Migration
- Learn: Layered architecture (route -> controller -> service -> repository)
- Deviations from Plan
- test_get_interview.py
- test_answer_with_profile.py
- interviews_constants.py
- Implementation Steps
- interview-room/README.md
- Implementation: Error Handling
- Implementation: Eval runs in Langfuse (scores + datasets)
- InterviewMessage
- Clock
- _ClosingStreamClient
- test_retrieval_profile.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Feature: Layered Modules (route -> controller -> service -> repository)
- experiments
- InterviewerInputs
- FakeLangfuse
- run_task
- llm
- Learn: LangChain as the call layer, one task at a time (U3a)
- Feature: LLM as the Interviewer (it asks the questions)
- Learn: Prompt registry (one place for prompt versions and routing)
- get_feedback_limiter
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- test_job_description_summary.py
- profile_evals.py
- interviews_start_dependencies.py
- summarize_job_description
- test_deepgram_makes_at_most_its_retries_plus_one_calls_per_direction
- Slices in detail
- test_profile_redaction.py
- Completed Steps
- Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)
- types.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- .stream
- cuewise-be
- .stream_generate_content
- .insert_feedback
- ._generate
- Learn: Langfuse experiments for the interviews evals
- fixture
- _RoutedChatModel

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 161 edges
2. `FakeChatModel` - 141 edges
3. `LLMResult` - 138 edges
4. `FakeProvider` - 131 edges
5. `User` - 131 edges
6. `JobRole` - 126 edges
7. `LLMError` - 123 edges
8. `LLMServerError` - 113 edges
9. `Level` - 111 edges
10. `InterviewType` - 107 edges

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

## Communities (356 total, 62 thin omitted)

### Community 0 - "_ScriptedClient"
Cohesion: 0.21
Nodes (22): ChatGoogleGenerativeAI, Spike results (step 1, `tests/core/ai/test_langchain_behaviour.py`), MonkeyPatch, _gemini(), Stands in for the SDK's `GenerativeServiceClient`: each call pops the next…, _response(), _ScriptedClient, test_a_per_call_timeout_and_generation_config_reach_the_request_through_bind() (+14 more)

### Community 1 - "LLMServerError"
Cohesion: 0.11
Nodes (52): anyio_lowlevel, Any, LLMRateLimitError, LLMServerError, 5xx or a dropped connection: the provider's side failed., parse_retry_after(), raise_for_status(), The Retry-After header as seconds. Only the delta-seconds form is read; an HTTP… (+44 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.06
Nodes (66): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, injection_ignored(), _injection_share(), _mention_share() (+58 more)

### Community 3 - "decode_token"
Cohesion: 0.07
Nodes (49): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+41 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.08
Nodes (78): bind_log_context(), Adds fields to every later log line of the current request (or, outside a…, render_text(), main(), Session, UUID, add_session(), analysis() (+70 more)

### Community 5 - "auth_service.py"
Cohesion: 0.08
Nodes (36): ConflictError, ProfileRequiredError, An interview asked to use the candidate's profile, and there is none to use…, hash_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), get_service() (+28 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "RetrievalService"
Cohesion: 0.11
Nodes (22): Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, EligibleChunk, NamedTuple, The k eligible chunks embedded with `model` that are most similar to the query,…, _log_level() (+14 more)

### Community 9 - "test_summary_evals.py"
Cohesion: 0.08
Nodes (50): wait(), Check, check_summary(), _dataset_items(), _has_fact(), load_summary_cases(), _print_case(), _print_summary() (+42 more)

### Community 10 - "profile_route.py"
Cohesion: 0.13
Nodes (17): _out(), ProfileController, The signed-in user's résumé profile: request -> ProfileService, stored row ->…, delete_profile(), get_profile(), post, ProfileUser, A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes… (+9 more)

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
Nodes (34): _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored(), test_api_key_never_shows_in_repr_or_errors() (+26 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.06
Nodes (56): _DeepgramAdapter, DeepgramSynthesizer, attempt(), attempt(), _parse(), Any, AsyncBaseTransport, Response (+48 more)

### Community 16 - "FakeClient"
Cohesion: 0.09
Nodes (20): The LangChain tracing callback (spec FR5, AC8, EC14, EC15): one Langfuse…, result(), test_a_call_records_one_generation_with_its_messages_labels_and_usage(), test_a_disabled_tracer_records_nothing(), test_a_failed_call_records_an_error_with_the_error_class(), test_a_langfuse_failure_never_fails_the_call(), test_a_redacted_call_records_the_placeholder_for_input_and_output(), test_retried_attempts_are_still_one_generation_with_the_attempt_count() (+12 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.06
Nodes (76): check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for(), feedback_run_scores(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult (+68 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (42): FetchedPage, Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request (+34 more)

### Community 19 - "test_knowledge_ingest.py"
Cohesion: 0.24
Nodes (20): active(), chunks(), corpus(), FailingOn, interview(), ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag…, Fails on the n-th embed call (1-based), then works again., rows() (+12 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.21
Nodes (16): PromptVersion, StrEnum, Status, ast, archived_routes(), incomplete_entries(), The prompt registry's guards (prompt-registry AC1, AC2, AC6, EC1-EC4). Each…, real_routes() (+8 more)

### Community 26 - "AppLogs"
Cohesion: 0.20
Nodes (4): AppLogs, LoggedLine, One JSON line of the log file, read the way older tests read a log record:…, _shown()

### Community 27 - "ReplyAttempts"
Cohesion: 0.13
Nodes (18): Iterate to get `(attempt, seconds_left)` for each reply attempt that may start.…, ReplyAttempts, asyncio, An extra set of runs (not used for the verdict), Failures, Scores, Still to do, U2 (tenacity) vs. the U0 baseline (+10 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.13
Nodes (56): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, 5. What can go wrong, happy(), interview(), post() (+48 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.16
Nodes (38): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+30 more)

### Community 30 - "Interviewer"
Cohesion: 0.10
Nodes (39): Decision, Interviewer, apply_limits(), Deadline, _decision_label(), plan_write(), UUID, The code's say over an answer turn: the shared deadline, the follow-up cap and… (+31 more)

### Community 31 - "OpenAICompatibleProvider"
Cohesion: 0.11
Nodes (15): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final… (+7 more)

### Community 32 - "test_tracing.py"
Cohesion: 0.06
Nodes (46): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, client(), drain(), experiment(), propagated(), fixture (+38 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "FakeChatModel"
Cohesion: 0.10
Nodes (43): fake_reply(), FakeChatModel, BaseChatModel, An AIMessage shaped like Gemini's: usage in `usage_metadata` (None = the vendor…, Pops one scripted reply per call: text (wrapped by `fake_reply`), a ready…, NamedTuple, A structured call's outcome: the parsed object, or None with `error` saying why…, Structured (+35 more)

### Community 35 - "test_context.py"
Cohesion: 0.18
Nodes (14): Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default(), test_a_strategy_without_a_limit_is_never_trimmed() (+6 more)

### Community 36 - "User"
Cohesion: 0.06
Nodes (58): DeepgramTranscriber, get_synthesizer(), get_transcriber(), Request, Request dependencies for the AI services every feature shares, built once at…, Built once at startup (app lifespan); None when no Deepgram key is configured…, Built once at startup (app lifespan); None when no Deepgram key is configured…, Protocol (+50 more)

### Community 37 - "profile_service.py"
Cohesion: 0.06
Nodes (83): ProfileExtractionFailedError, ProfileNotFoundError, ProfileUnavailableError, Not a PDF or a Word document by its content (the file name is never trusted)., Encrypted, corrupt, scanned, too little text, or no usable profile in it., The model gave no valid profile after the retry, timed out, or the provider…, ResumeUnreadableError, ResumeUnsupportedError (+75 more)

### Community 38 - "FakeProvider"
Cohesion: 0.12
Nodes (36): FakeProvider, hints_of(), long_case(), main(), mentions(), noted(), The hints on one case's result in Langfuse., reply() (+28 more)

### Community 39 - "test_knowledge_utils.py"
Cohesion: 0.10
Nodes (38): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+30 more)

### Community 40 - "test_layers.py"
Cohesion: 0.24
Nodes (15): 5. What can go wrong, _one(), parametrize, The layer rules of app/modules (CLAUDE.md, "Architecture"): route -> controller…, test_a_feature_ai_folder_may_import_langchain(), test_a_feature_importing_another_features_repository_is_reported(), test_a_layer_file_left_at_a_module_root_is_reported(), test_a_layer_importing_langchain_or_a_vendor_sdk_is_reported() (+7 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues, Links (+7 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "test_chat_contract.py"
Cohesion: 0.12
Nodes (29): Build, langchain_core_prompts, StreamOutcome, _collect(), _fake_stream(), _gemini(), _gemini_stream(), Profile (+21 more)

### Community 44 - "test_chat_stream.py"
Cohesion: 0.19
Nodes (24): fake_chunks(), BaseException, A streamed reply: one chunk per text part, an exception raised where it stands…, 5. What can go wrong, 6. Try it yourself, anyio_backend(), fixture, `stream_chat`, the async stream helper of the LangChain call layer (U3b1 step… (+16 more)

### Community 45 - "test_write.py"
Cohesion: 0.31
Nodes (16): call_lines(), The blocking write on the LangChain call layer (U3b1 step 5, FR5, AC5, AC10):…, reply(), run(), test_a_context_too_large_makes_no_call(), build(), test_a_follow_up_takes_the_main_questions_category(), test_a_rejected_request_is_not_retried() (+8 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_langchain_behaviour.py"
Cohesion: 0.16
Nodes (13): google_ai_generativelanguage_v1beta_types, _Flaky, BaseChatModel, BaseModel, Pins the LangChain and langchain-google-genai behavior the U3a call layer…, Fails its first `failures` calls; `fail_after_first_chunk` makes a stream fail…, _Reply, test_a_human_message_list_is_accepted_as_model_input() (+5 more)

### Community 49 - "JobUrlService"
Cohesion: 0.15
Nodes (21): JobTextFormat, Which clipboard copy the client sent: the HTML one when the browser has it (its…, JobUrlController, Job posting links and pasted pages: request -> JobUrlService, job text ->…, get_job_url_controller(), get_job_url_service(), Depends, JobTextIn (+13 more)

### Community 50 - "test_request_context.py"
Cohesion: 0.06
Nodes (22): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a) (+14 more)

### Community 51 - "LLMResult"
Cohesion: 0.06
Nodes (64): fixed_prompt(), A prompt of already-built messages (our context manager's output), sent exactly…, BuiltContext, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., LLMResult, BaseModel (+56 more)

### Community 52 - "errors.py"
Cohesion: 0.07
Nodes (51): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError (+43 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (21): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+13 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.17
Nodes (18): call_lines(), llm_lines(), parametrize, The `llm_call` lines only (the call layer's `retry_wait` / `retry_giveup`…, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_after_the_call_layer(), test_an_invalid_reply_is_retried_once() (+10 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.15
Nodes (36): 5. What can go wrong, Open Questions, fail(), error(), import_url(), long_posting(), page(), paste() (+28 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.11
Nodes (34): Review, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok() (+26 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.08
Nodes (57): group_requests(), The events of each request, oldest request first (the id is on every line of…, analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table() (+49 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.16
Nodes (28): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_retry_after_longer_than_the_budget_fails_at_once_without_waiting(), test_cached_and_reasoning_tokens_are_none_when_not_reported(), test_cached_and_reasoning_tokens_are_read_when_reported() (+20 more)

### Community 59 - "interviews_knowledge_utils.py"
Cohesion: 0.06
Nodes (71): estimate_tokens(), WindowLedger, ModelDecision, ModelEvidence, ModelQuestionScore, BaseModel, What the model is asked to fill on the LangChain layer's structured calls…, The decide call's reply (follow_up_decision_v1): `gap` is null for… (+63 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 61 - "ProviderChatModel"
Cohesion: 0.29
Nodes (8): _message(), ProviderChatModel, AIMessage, Any, BaseMessage, ChatGenerationChunk, ChatResult, `route` is one provider, or a function from the call's system prompt to the…

### Community 62 - "Rules"
Cohesion: 0.09
Nodes (20): caveman, Example output, How to invoke, See also, What it does, 1. Answer first, 2. Kill ceremony, 3. Short word (+12 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_evals.py"
Cohesion: 0.15
Nodes (35): load_cases(), Path, 5. What can go wrong, Deviations from Plan, decision(), labelled_cases(), last_line(), The trace id the fake gives a case in the given repeat's run (write and stream… (+27 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.14
Nodes (29): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, test_fake_embedder_honors_scripted_vectors_and_errors(), test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets(), competencies(), corpus(), note_text(), fixture (+21 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.11
Nodes (45): One answer turn of the LLM interviewer: decide (follow up or move on), apply…, ActionKnown, Delta, PhaseChanged, NamedTuple, StrEnum, What one answer turn of the LLM interviewer hands around: its action, its…, What the turn ends with, after the limits: the model can only ask for the first… (+37 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (35): 5. What can go wrong, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,…, Swagger UI builds its request from the OpenAPI schema. Declared as a url-…, stored() (+27 more)

### Community 68 - "test_feedback_contract.py"
Cohesion: 0.18
Nodes (33): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+25 more)

### Community 69 - "InterviewQuestion"
Cohesion: 0.09
Nodes (27): InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, Every stored question, grouped by interview in creation order (UUIDv7), for the…, 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), db() (+19 more)

### Community 71 - "test_feedback_turn.py"
Cohesion: 0.16
Nodes (22): Clock, generator(), End-of-interview feedback on the LangChain call layer (U3b1 step 16, FR8, AC8,…, Uses up the budget on its first call, so a retry would start with less than…, score(), score_inputs(), score_json(), SlowFirstCall (+14 more)

### Community 72 - "build_chat_model"
Cohesion: 0.29
Nodes (13): build_chat_model(), The LangChain chat model for the primary provider (the tasks migrated in U3a…, langchain_google_genai, fixture, `build_chat_model`: the LangChain chat model built from the same LLM config as…, settings_with(), test_google_builds_the_native_gemini_model_from_config(), test_no_listed_provider_means_no_chat_model_and_one_warning() (+5 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.19
Nodes (22): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, BaseException, Exception (+14 more)

### Community 74 - "app_logs"
Cohesion: 0.15
Nodes (17): Path, Routes every logger through the processor chain. Safe to call again (tests do):…, setup_logging(), Completed Steps, Deviations from Plan, Affected Files & Patterns, 6. Try it yourself, Affected Files & Patterns (+9 more)

### Community 75 - "test_gateway.py"
Cohesion: 0.05
Nodes (54): FakeSynthesizer, FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, Scripted clips (bytes, a full result, or an error), one per call; records each…, BaseModel, One spoken clip. `content_type` is what the vendor says the audio is: the…, `text` spoken in the configured voice, as one whole clip., SynthesisResult (+46 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues (+8 more)

### Community 77 - "InvalidReplyError"
Cohesion: 0.12
Nodes (30): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, parse_profile_reply(), A JSON-text reply, checked against `RawProfile`, then `clean_profile`. The live…, 1. Why it exists (+22 more)

### Community 78 - "failed"
Cohesion: 0.08
Nodes (28): check_decision(), check_reply(), pause_for(), Rule checks for one reply. Text checks look at the parsed question, or at the…, The decide reply against the case's label; the injection check reads the raw…, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming) (+20 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (27): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+19 more)

### Community 81 - "interviews_evals.py"
Cohesion: 0.08
Nodes (52): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_streamed_reply(), decide_run_scores() (+44 more)

### Community 82 - "StreamedTurn"
Cohesion: 0.18
Nodes (9): Affected Files & Patterns, parse_sse(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream() (+1 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 84 - "complete_chat"
Cohesion: 0.06
Nodes (39): complete_chat(), complete_structured(), Any, ChatModel, Runnable, T, TraceLabels, `prompt | model.with_structured_output(schema)` (Gemini's native JSON schema).… (+31 more)

### Community 85 - ".speech"
Cohesion: 0.22
Nodes (10): BaseModel, Every speech setting in one read-only group, so the speech factories depend on…, Speech-to-text (voice answers)., Text-to-speech (the interviewer's voice)., The speech vendor's settings, grouped (see `Settings.speech`). One key and base…, _SpeechPart, SpeechSettings, SttSettings (+2 more)

### Community 86 - "LLMError"
Cohesion: 0.04
Nodes (73): T, LLMError, Exception, Base for every provider failure. `retryable` marks faults that may pass on…, Attempted, _Call, _OutOfTime, BaseException (+65 more)

### Community 87 - "EmbeddingKind"
Cohesion: 0.10
Nodes (31): EmbeddingKind, EmbeddingSizeError, StrEnum, A vector of another length than configured. Vectors of different sizes can't be…, GoogleEmbedder, BaseTransport, Response, Clock (+23 more)

### Community 88 - "InterviewsRepository"
Cohesion: 0.05
Nodes (42): InterviewSession, _history_filter(), _history_order(), InterviewsRepository, Any, datetime, Session, UUID (+34 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "CandidateProfile"
Cohesion: 0.08
Nodes (56): candidate_profile_block(), profile_query_text(), The profile fenced as data, like the job description. Summaries and…, The profile's short items as one retrieval query. None: nothing to embed., CandidateProfile, Project, BaseModel, The candidate profile: what a résumé becomes, what is stored, and what the API… (+48 more)

### Community 93 - "test_retrieval_profile_cases.py"
Cohesion: 0.23
Nodes (15): case_set_problems(), BaseModel, _retrieval_cases(), RetrievalCase, CaseKind, case(), test_the_labelled_set_needs_15_queries_with_the_required_kinds(), case() (+7 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 97 - "json"
Cohesion: 0.05
Nodes (64): NotEnoughQuestionsError, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), load_bank(), pick_fallback_question(), Collection, Random (+56 more)

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.17
Nodes (11): Commit message suggestion, Deviations from Plan, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

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
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "test_speech.py"
Cohesion: 0.09
Nodes (22): answered(), assert_hidden(), code(), fixture, parametrize, GET /interviews/{id}/questions/{qid}/speech and /messages/{mid}/speech: the…, An owner with a started backend interview: (owner, session_id, first question)., The first question answered: (owner, session_id, q1, the reaction, q2). (+14 more)

### Community 104 - "interviews_answer_service.py"
Cohesion: 0.05
Nodes (68): SessionNotInProgressError, current_request_id(), QuestionSource, The SSE event names of a streamed turn: the contract with the client. `done`…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, StreamEvent, answer_out(), _error_event() (+60 more)

### Community 105 - "provider.py"
Cohesion: 0.07
Nodes (53): anyio, A LangChain chat model for tests (spec FR6): scripted replies or errors, every…, _finish_reason(), AIMessage, The LangChain call layer's public face (U3a): the `ChatModel` type services are…, _result(), The streamed call of the LangChain call layer (U3b1): `astream()` under the…, Langfuse tracing for the LangChain call layer, through our own `Tracer` (U3a,… (+45 more)

### Community 106 - "test_answer_stream.py"
Cohesion: 0.06
Nodes (36): 5. What can go wrong, 6. Try it yourself, fixture, AnswerController.stream_answer driven directly, for what a test client can't…, A started interview and a controller wired like the app's: returns (controller,…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing() (+28 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "parse_log"
Cohesion: 0.10
Nodes (27): Call, _int(), _json_event(), LogEvent, parse_log(), NamedTuple, Reading the app's own log back: what each request did for an interview, from…, Old text lines: `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]).… (+19 more)

### Community 109 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+7 more)

### Community 110 - "PromptCheckError"
Cohesion: 0.22
Nodes (8): PromptCheckError, Exception, One or more routed prompts cannot be sent; the message lists each one., 4. How it works, fastapi_testclient, The app lifespan runs the prompt check before anything else (prompt-registry…, test_a_failed_prompt_check_stops_startup_before_the_provider_is_built(), broken()

### Community 111 - "test_follow_ups.py"
Cohesion: 0.27
Nodes (16): answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries(), test_a_failed_follow_up_write_falls_back_to_the_next_main_bank_question() (+8 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional (+6 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "JobRole"
Cohesion: 0.06
Nodes (74): InterviewType, JobRole, Level, _Interview, The interview as plain values, read before the claim's commit expires the…, EvalSetup, FeedbackEvalSetup, ExtraSetupFields (+66 more)

### Community 115 - "merge_note_rankings"
Cohesion: 0.07
Nodes (41): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, Architecture & Design, Blockers & Resolutions, Decisions (grill-me, 2026-11-14), Deviations during implementation (2026-11-14, see task.md), Implementation Plan: Résumé-aware interview (Slice 8d), Overview (+33 more)

### Community 116 - "test_decide.py"
Cohesion: 0.29
Nodes (17): call_lines(), decision(), outcomes(), The decide call on the LangChain call layer with structured output (U3b1 step…, run(), test_a_bad_note_is_dropped_and_the_decision_kept(), test_a_context_too_large_makes_no_call(), build() (+9 more)

### Community 117 - "The fundamentals"
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "PageParams"
Cohesion: 0.05
Nodes (48): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewListOut (+40 more)

### Community 121 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.18
Nodes (10): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slices (+2 more)

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.12
Nodes (14): The notes stored for this interview at start, rank order; none for interviews…, 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links (+6 more)

### Community 125 - "test_profile_extract.py"
Cohesion: 0.13
Nodes (21): Carries the app's Tracer on a chat model (`build_chat_model(..., tracer=)`…, TracerHandle, BaseCallbackHandler, extract(), no_retry_waits(), fixture, parametrize, `extract_profile` on the LangChain layer: structured output inside the existing… (+13 more)

### Community 126 - "Implementation Plan: U1 structlog (structured JSON logs)"
Cohesion: 0.20
Nodes (9): Approaches Considered, Blockers & Resolutions, Implementation Plan: U1 structlog (structured JSON logs), Overview, Project Rules Applied, Ready to Implement, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 127 - "Feature: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Decisions, Edge Cases, Feature: Résumé-aware interview (Slice 8d), Functional, Goal, Known limits (+7 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "test_knowledge_ingest_cli.py"
Cohesion: 0.27
Nodes (13): main(), _parser(), ArgumentParser, Session, ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1() (+5 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.15
Nodes (12): Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "4. How it works"
Cohesion: 0.11
Nodes (26): _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _has_external_relationship(), _hex_lightness() (+18 more)

### Community 134 - "build_usage_report"
Cohesion: 0.20
Nodes (16): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, main(), Session, Print stored LLM usage per interview: tokens per question position and per…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind() (+8 more)

### Community 135 - "Blind ranking"
Cohesion: 0.12
Nodes (16): Blind ranking, Setup complete-behavioral-junior, Setup near-empty-data-intern, Setup profile-injection-backend-mid, Setup profile-mismatch-backend-mid, Setup strong-backend-mid, X, X (+8 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "safe_fetch.py"
Cohesion: 0.08
Nodes (22): FetchError, BaseTransport, Exception, Fetch a web page whose address a user chose, without letting that user reach…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError, codecs, Affected Files & Patterns (+14 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "stream_chat"
Cohesion: 0.09
Nodes (28): Any, ChatModel, Runnable, TraceLabels, `prompt | model` streamed: text chunks, then the LLMResult. Raises an LLMError…, stream_chat(), Draft, One streamed write attempt, finished: the category (from its CATEGORY line, or… (+20 more)

### Community 142 - "4. How it works"
Cohesion: 0.11
Nodes (19): _default_request_id(), _merge_request_fields(), Any, Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything…, Dev console: time, level, short request id, logger, event, then one aligned…, ReadableRenderer, redact_sensitive(), _redacted() (+11 more)

### Community 143 - "QuestionTurn"
Cohesion: 0.04
Nodes (73): _counts(), FollowUpDecision, An earlier question as the model would have written it. A follow-up was written…, The decide call: the current thread in full (it judges the latest answer within…, App data at the end of the last user message; untrusted parts (questions,…, _status_block(), A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it… (+65 more)

### Community 144 - "._generate"
Cohesion: 0.22
Nodes (6): GenerateContentResponse, Any, BaseMessage, ChatGenerationChunk, ChatResult, Exception

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

### Community 150 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 151 - "interviews_feedback_controller.py"
Cohesion: 0.18
Nodes (13): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, get_feedback_controller(), FeedbackOut (+5 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Skills Consulted During Implementation, Status (+4 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.13
Nodes (27): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+19 more)

### Community 156 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.13
Nodes (14): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional (+6 more)

### Community 157 - "Implementation: Interview Room (backend)"
Cohesion: 0.12
Nodes (15): Changes Made, Current Step, Debug Log, Deviations from Plan, Done. Next: `/review-feature`, Implementation: Interview Room (backend), Known Issues, Links (+7 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.14
Nodes (13): 9. Review gate (user), Changes Made, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 159 - "audio_container"
Cohesion: 0.28
Nodes (13): audio_container(), AudioContainer, _has_signature(), StrEnum, Audio rules every speech feature shares: which recording containers are…, Recording containers an upload may arrive in (what browsers' MediaRecorder…, The container of an uploaded recording, or None when its declared type isn't…, parametrize (+5 more)

### Community 160 - "profile_reply.py"
Cohesion: 0.07
Nodes (37): clean_profile(), fit(), ModelProfile, ModelProject, ModelRole, BaseModel, The contract for the profile-extraction reply, and the check that enforces it.…, A schema-valid reply made safe to store: trimmed and cut to the caps, blanks… (+29 more)

### Community 161 - "Tracer"
Cohesion: 0.03
Nodes (100): AbstractContextManager, build_tracer(), ExperimentRun, Any, NamedTuple, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a… (+92 more)

### Community 162 - "test_transcript.py"
Cohesion: 0.25
Nodes (12): fixture, shape(), started(), test_a_follow_up_is_shown_with_its_kind_and_its_main_questions_number(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question() (+4 more)

### Community 163 - "test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only"
Cohesion: 0.36
Nodes (9): Baseline Failures, Baseline Failures, Testing Strategy, Baseline Failures, Testing Strategy, Baseline Failures, result(), test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only() (+1 more)

### Community 164 - "test_start_with_profile.py"
Cohesion: 0.09
Nodes (31): UUID, The user's stored profile for an interview prompt, read live (never copied onto…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+23 more)

### Community 165 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Architecture & Design, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview (+6 more)

### Community 166 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 167 - "profile_extract.py"
Cohesion: 0.08
Nodes (33): load_prompt(), Path, Prompt files: versioned Markdown read once per process. Feature modules pass…, `<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in…, Condense a long job description once, so later calls send less…, build_messages(), extract_profile(), Extraction (+25 more)

### Community 168 - "Implementation: U1 structlog (structured JSON logs)"
Cohesion: 0.14
Nodes (13): Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U1 structlog (structured JSON logs), Known Issues, Links, Open Questions (+5 more)

### Community 169 - "LLMTimeoutError"
Cohesion: 0.10
Nodes (25): LLMTimeoutError, _degrade_reason(), 1. Why it exists, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me (+17 more)

### Community 171 - "LLMProvider"
Cohesion: 0.05
Nodes (38): LLMProvider, Protocol, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Failures, Scores, Should this be the new baseline?, U3b1 stage 2 (decide on LangChain, structured output) vs. the baseline (+30 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.11
Nodes (21): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas (+13 more)

### Community 174 - "request_log_context"
Cohesion: 0.25
Nodes (6): Makes `fields` (at least `request_id`) part of every log line inside the block., request_log_context(), Deviations from Plan, Receive, Scope, Send

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "check_core"
Cohesion: 0.25
Nodes (8): Skills Consulted During Implementation, check_core(), _imports(), Every `app/core` import of a feature module (`app.modules...`): core is shared…, (absolute module, imported names) per import statement; relative imports…, test_a_core_file_importing_a_feature_module_is_reported(), test_a_core_file_importing_only_core_and_libraries_is_clean(), test_the_real_core_imports_no_feature_module()

### Community 178 - "interviews_model.py"
Cohesion: 0.06
Nodes (63): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+55 more)

### Community 179 - "make_user"
Cohesion: 0.25
Nodes (8): Affected Files & Patterns, make_user(), _make(), Insert a user straight into the test DB; password defaults to 'password123'., test_a_streamed_turn_saves_the_rows_the_json_turn_would(), run(), test_done_has_the_json_endpoints_shape_and_content(), run()

### Community 180 - "auth_header"
Cohesion: 0.11
Nodes (18): auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, answer(), _answer(), POST a setup for `user`; any field can be overridden, or dropped by passing…, POST an answer; `question_id` defaults to whatever the caller passes, body…, POST a recording to the transcription endpoint; `audio=None` sends no file part… (+10 more)

### Community 181 - "interviews_rag_evals.py"
Cohesion: 0.04
Nodes (86): _arm_notes(), ArmInterview, ArmSummary, build_sheet(), competencies_of(), ExtraSetup, filter_baseline(), generation_run_scores() (+78 more)

### Community 182 - "LogCapture"
Cohesion: 0.29
Nodes (4): StringIO, LogCapture, Path, What the real logging pipeline wrote during a test: the file's JSON lines and…

### Community 183 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 184 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 185 - "parse_write_reply"
Cohesion: 0.31
Nodes (8): _check_lengths(), parse_write_reply(), The write call's text, slot by slot: every section once and in order, list…, _slots(), WriteText, test_a_valid_write_reply_is_parsed_into_slots(), test_blank_lines_and_a_wrapped_summary_are_accepted(), write_reply()

### Community 186 - "AnswerIn"
Cohesion: 0.43
Nodes (4): AnswerController, UUID, The checks and reads before the stream opens (sync DB work: the route runs it…, AnswerIn

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
Cohesion: 0.03
Nodes (75): open_stream(), ErrorResponse, Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions (+67 more)

### Community 203 - "pytest"
Cohesion: 0.04
Nodes (53): verify_password(), health_check(), StrEnum, Role, list_users(), PageDep, main(), Session (+45 more)

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 211 - "KnowledgeRepository"
Cohesion: 0.12
Nodes (29): KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, notes_fingerprint(), A short id for the ingested notes: changes when any note changes, not when the…, Rank the notes for every labelled query and score where the right note landed,…, run_retrieval() (+21 more)

### Community 220 - "LLMBadResponseError"
Cohesion: 0.07
Nodes (48): _from_status(), _google_error(), _mapped(), BaseException, Map what the LangChain/Gemini call layer raises to our LLMError types (spec…, The LLMError for `exc`, with `exc` as its cause. Messages are fixed text: a…, Seconds from the error's `google.rpc.RetryInfo` detail (Google's Retry-After);…, _retry_after() (+40 more)

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

### Community 234 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

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
Cohesion: 0.14
Nodes (13): 15. Evals, fault check and graph, Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U2 — One tenacity retry policy for the AI call layer, Known Issues, Links (+5 more)

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
Cohesion: 0.06
Nodes (77): alias, AnswerControllerDep, ForbiddenError, RateLimitedError, Raise with `headers={"Retry-After": "<seconds>"}`., Permission, permissions_for(), The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later. (+69 more)

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

### Community 252 - "Data"
Cohesion: 0.22
Nodes (14): Data, What an interviewer write carries beyond the job description; it picks the…, check_prompts(), Raises PromptCheckError naming every routed version whose file is missing or…, Known Issues, Skills Consulted During Implementation, loader(), load() (+6 more)

### Community 253 - "test_tracing_lifespan.py"
Cohesion: 0.33
Nodes (5): The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 255 - "Feature: U1 structlog (structured JSON logs)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: U1 structlog (structured JSON logs), Functional, Goal, Non-Functional (+6 more)

### Community 256 - "Feature: Job URL (Slice 8b)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Job URL (Slice 8b), Functional, Goal, Non-Functional (+7 more)

### Community 257 - "test_generation_eval.py"
Cohesion: 0.07
Nodes (57): _non_negative_seconds(), _parser(), _positive(), ArgumentParser, parse_arms(), Read your filled-in sheet, print how often each arm ranked first, then post…, `--arms`: comma-separated arm letters (any case), at least two (a ranking…, run_ranking() (+49 more)

### Community 258 - "scrub_contacts"
Cohesion: 0.16
Nodes (18): _appears(), keep(), _normalized(), _phone_or_keep(), Pure helpers of the profile feature: contact scrubbing, résumé reading,…, The text with email addresses and phone numbers replaced by placeholders;…, `item` occurs in `source` as a whole word or phrase, ignoring case and spacing…, scrub_contacts() (+10 more)

### Community 259 - "interviews_context.py"
Cohesion: 0.04
Nodes (90): ContextManager, ContextReport, _log(), NamedTuple, Context management: the one place that decides what each LLM call sends. The…, StrategyOutput, Task, FeedbackScore (+82 more)

### Community 260 - "Implementation: Prompt Registry"
Cohesion: 0.13
Nodes (14): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Links (+6 more)

### Community 261 - "follow_up"
Cohesion: 0.16
Nodes (13): Slice 3: Structured follow-up decisions, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+5 more)

### Community 262 - "test_speech_contracts.py"
Cohesion: 0.20
Nodes (13): anyio_backend(), _aura(), _deepgram(), _no_wait(), fixture, Response, One contract per speech protocol, run against the fake AND the real adapter (on…, synthesizers() (+5 more)

### Community 263 - "check_layers"
Cohesion: 0.29
Nodes (7): Blockers & Resolutions, Known Issues, check_layers(), _is_llm_library(), Every layer-rule violation in `files` (repo-relative path -> source), as…, test_clean_layer_imports_have_no_violations(), _violation()

### Community 264 - "QuestionCategory"
Cohesion: 0.09
Nodes (48): _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_interviewer_reply(), parse_streamed_reply(), BaseModel, NamedTuple (+40 more)

### Community 265 - "_formatter"
Cohesion: 0.33
Nodes (6): _formatter(), _json(), _json_renderer(), Constraints, Processor, ProcessorFormatter

### Community 266 - "4. How it works"
Cohesion: 0.07
Nodes (27): _decode(), is_public_address(), Response, Scheme, credentials, port and every resolved address. Returns the address to…, One hop: a page, or the redirect's Location to check next., Header charset, else a <meta> charset, else UTF-8; never raises (bad bytes…, True only for a globally routable unicast address., SafeFetcher (+19 more)

### Community 267 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Changes Made, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 268 - "5. What can go wrong"
Cohesion: 0.24
Nodes (10): 5. What can go wrong, catalog_mismatches(), Collection, A string literal that is exactly a version name, outside the registry: a…, test_a_file_without_an_entry_and_an_entry_without_a_file_are_named(), test_a_version_literal_is_named_but_prose_mentioning_one_is_not(), test_no_version_name_is_written_outside_the_registry(), test_the_catalog_matches_the_prompt_files() (+2 more)

### Community 269 - "interviews_answer_dependencies.py"
Cohesion: 0.10
Nodes (40): get_tracer(), Built once at startup (app lifespan); a disabled tracer when the lifespan…, get_answer_controller(), get_answer_service(), ChatModel, Depends, Session, get_feedback_service() (+32 more)

### Community 270 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

### Community 272 - "Implementation: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 273 - "test_factory.py"
Cohesion: 0.04
Nodes (67): build_embedder(), build_provider(), build_synthesizer(), build_transcriber(), Embeddings for reference-note retrieval; None without the Google key (notes are…, The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Text-to-speech for the interviewer's voice; None without a key (the interview… (+59 more)

### Community 274 - "Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 275 - "Implementation Plan: Agentic Workflow v2"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: Agentic Workflow v2, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 276 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 277 - "_StderrHandler"
Cohesion: 0.33
Nodes (4): Writes to whatever `sys.stderr` is at the time of the write (test runners and…, _StderrHandler, setter, TextIO

### Community 290 - "RateLimiter"
Cohesion: 0.15
Nodes (17): RateLimiter, Count one request for `key`: None when allowed, else whole seconds until its…, get_resume_limiter(), limit_resume_uploads(), ProfileUser, Tests swap in a fresh limiter so counts never leak between them., Checked before the body is read: every upload is a parse and a model call., Clock (+9 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 293 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 294 - "get_logger"
Cohesion: 0.11
Nodes (35): get_logger(), Logger, log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, 5. What can go wrong, structlog, parametrize, The logging pipeline (U1 structlog): what actually lands in the log file and on… (+27 more)

### Community 295 - "Learn: Adding interview roles (designer, qa, devops)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open, Learn: Adding interview roles (designer, qa, devops)

### Community 296 - ".record_turn"
Cohesion: 0.05
Nodes (53): ErrorBody, BaseModel, QuestionNotCurrentError, Save one whole turn in one commit: advance the session, the answer, the…, AnswerOut, Turn the outcome into rows and save the whole turn in one commit. `reaction` is…, done(), Deviations from Plan (+45 more)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "html_target"
Cohesion: 0.33
Nodes (6): html_target(), Path, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines(), test_the_script_reads_the_rotated_log_before_the_current_one()

### Community 299 - "U0 baselines"
Cohesion: 0.22
Nodes (8): Before relying on this, Cost, Eval baselines, How to use this file, Live interviews (from `logs/app.log`, before U1), Prompts with no eval baseline (gaps), U0 baselines, U3b1 baselines (old call layer, before the interview calls move to LangChain)

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 301 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (9): Reload rows a commit expired, so reading their fields later needs no database…, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 302 - "Deviations from Plan"
Cohesion: 0.53
Nodes (6): Deviations from Plan, busy(), Response, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_retries_stop_when_the_total_budget_would_be_exceeded()

### Community 303 - "test_get_interview.py"
Cohesion: 0.10
Nodes (14): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses(), fixture, Log context on real interview requests (U1 structlog, AC4): `session` and…, Every line of the one request whose access line ends with `path_end`. (+6 more)

### Community 304 - "test_answer_with_profile.py"
Cohesion: 0.25
Nodes (12): opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent(), test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile() (+4 more)

### Community 305 - "interviews_constants.py"
Cohesion: 0.09
Nodes (45): HistorySortColumn, MessageKind, MessageRole, StrEnum, Who wrote the feedback text: the write call, or the code's template when that…, The history columns GET /interviews sorts by; the values are the response's…, Transcript item kinds: a question comes from interview_questions, the other two…, SessionStatus (+37 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 308 - "Implementation: Error Handling"
Cohesion: 0.17
Nodes (11): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+3 more)

### Community 309 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

### Community 310 - "InterviewMessage"
Cohesion: 0.09
Nodes (22): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409() (+14 more)

### Community 311 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 312 - "_ClosingStreamClient"
Cohesion: 0.40
Nodes (3): _ClosingStreamClient, chunks(), The Gemini SDK's async client, streaming slowly and recording when its stream…

### Community 313 - "test_retrieval_profile.py"
Cohesion: 0.22
Nodes (17): EmbedCall, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), embedder_for(), RetrievalService.retrieve with the candidate profile's query (resume-aware-…, retrieve(), test_a_job_description_below_the_threshold_falls_back_to_filter_mode() (+9 more)

### Community 314 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 315 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.22
Nodes (8): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Out of Scope, Problem, Project Conventions, User Flow, UX Requirements

### Community 316 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 317 - "InterviewerInputs"
Cohesion: 0.06
Nodes (42): build_context_manager(), FullHistory, InterviewerInputs, A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, Plain values for one interviewer or decide call., WithInterviewData (+34 more)

### Community 318 - "FakeLangfuse"
Cohesion: 0.05
Nodes (46): _evaluation(), git_commit(), Any, Score, What every eval task moved onto Langfuse experiments shares (langfuse-…, Run every case once, in order, as one Langfuse experiment run; whatever the run…, The short commit hash, `-dirty` when the working tree has changes, `unknown`…, What produced a run, as the strings Langfuse stores: the run explains itself… (+38 more)

### Community 319 - "run_task"
Cohesion: 0.24
Nodes (13): console_number(), run_task(), test_a_good_streamed_reply_passes_every_check(), test_a_write_result_shows_the_reply_and_the_notes_but_no_expected_action(), test_a_write_run_per_repeat_carries_what_produced_it(), test_each_case_shows_what_was_judged(), test_every_check_is_scored_on_each_write_case(), test_main_runs_the_streamed_task_and_prints_the_first_token() (+5 more)

### Community 320 - "llm"
Cohesion: 0.06
Nodes (46): ModelScore, The feedback score call's reply (feedback_score_v2), same shape as…, Skills Consulted, 2. What it is, The order of the checks (stages 2 and 4), When a client leaves mid-stream (stage 3), Why structured output plus the old parser (stages 2 and 4), Functional (+38 more)

### Community 322 - "Learn: LangChain as the call layer, one task at a time (U3a)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Decision: who owns retries (spec FR3) (+2 more)

### Community 323 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.11
Nodes (19): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+11 more)

### Community 325 - "Learn: Prompt registry (one place for prompt versions and routing)"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Eval log (AI features only) (+1 more)

### Community 327 - "get_feedback_limiter"
Cohesion: 0.13
Nodes (10): get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., fresh_limiter(), owner(), fixture, Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, Fake wall clock for the claim token and the stale takeover., recording() (+2 more)

### Community 330 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 331 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): google_api_core, parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_without_an_llm_no_summary_is_made()

### Community 332 - "profile_evals.py"
Cohesion: 0.07
Nodes (34): Constraints, Input, Output, Role, Task, build_file(), case_scores(), CaseResult (+26 more)

### Community 333 - "interviews_start_dependencies.py"
Cohesion: 0.12
Nodes (19): get_db(), Session, get_profile_clock(), get_profile_controller(), get_profile_now(), get_profile_service(), ChatModel, datetime (+11 more)

### Community 334 - "summarize_job_description"
Cohesion: 0.21
Nodes (16): ChatModel, One summary call; see `SummaryOutcome`. A reply that `validate_summary` rejects…, summarize_job_description(), llm_lines(), no_retry_waits(), fixture, parametrize, The job-description summary on the LangChain layer… (+8 more)

### Community 335 - "test_deepgram_makes_at_most_its_retries_plus_one_calls_per_direction"
Cohesion: 0.11
Nodes (15): AIMessage, Any, BaseMessage, BaseModel, ChatGenerationChunk, ChatResult, Runnable, FakeChatReply (+7 more)

### Community 336 - "Slices in detail"
Cohesion: 0.14
Nodes (13): AI Engineering Upgrade Path (Cuewise), Build order, How to make it stick, Progress, Slices in detail, U0: Baselines, U1: structlog, U4: Prompt templates + Langfuse Prompt Management (+5 more)

### Community 339 - "test_profile_redaction.py"
Cohesion: 0.29
Nodes (15): assert_redacted(), assert_traced_in_full(), generations(), inputs(), anyio, resume-aware-interview Step 5: a write whose prompt carries the profile is…, A chat model replying `reply`, with the tracer riding on it as the factory…, run_stream_write() (+7 more)

### Community 341 - "Completed Steps"
Cohesion: 0.10
Nodes (28): Embedder, Protocol, log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, _embed(), ingest_corpus(), IngestCounts, IngestError (+20 more)

### Community 342 - "Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)"
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 8. Check your understanding, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)

### Community 343 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 344 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 346 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 347 - ".stream"
Cohesion: 0.31
Nodes (4): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Step 11: `FakeProvider.stream`, Reply

### Community 353 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 354 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 356 - "_RoutedChatModel"
Cohesion: 0.15
Nodes (13): Any, BaseMessage, ChatResult, The chat model of the `llm` fixture: the summary goes to `llm.summary`; every…, _RoutedChatModel, as_chat(), labelled(), run_decide_case() (+5 more)

## Knowledge Gaps
- **1124 isolated node(s):** `cuewise-be`, `What it does`, `How to invoke`, `Example output`, `See also` (+1119 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2754 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **62 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LLMError` connect `LLMError` to `LLMServerError`, `Cuewise BE — Project Instructions`, `test_speech_contracts.py`, `RetrievalService`, `stream_chat`, `test_deepgram.py`, `test_factory.py`, `Interviewer`, `OpenAICompatibleProvider`, `test_tracing.py`, `FakeChatModel`, `User`, `FakeProvider`, `profile_extract.py`, `.record_turn`, `LLMTimeoutError`, `LLMProvider`, `test_chat_stream.py`, `LLMResult`, `errors.py`, `interviews_rag_evals.py`, `interviews_knowledge_utils.py`, `llm`, `FakeEmbedder`, `test_stream_turn.py`, `test_gateway.py`, `summarize_job_description`, `interviews_evals.py`, `complete_chat`, `Completed Steps`, `.stream`, `LLMBadResponseError`, `interviews_answer_service.py`, `provider.py`, `Feature: Langfuse Tracing`, `JobRole`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `test_generation_eval.py`, `interviews_context.py`, `RetrievalService`, `test_summary_evals.py`, `interviews_answer_dependencies.py`, `FakeClient`, `test_factory.py`, `test_feedback_evals.py`, `Feature: Langfuse experiments for the interviews evals`, `test_feedback_endpoint.py`, `test_tracing.py`, `FakeChatModel`, `User`, `profile_extract.py`, `test_chat_stream.py`, `test_write.py`, `interviews_constants.py`, `LLMResult`, `errors.py`, `interviews_rag_evals.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `test_openai_compatible_stream.py`, `test_tracing_routes.py`, `experiments`, `FakeLangfuse`, `test_evals.py`, `Learn: LangChain as the call layer, one task at a time (U3a)`, `test_feedback_turn.py`, `build_chat_model`, `get_feedback_limiter`, `profile_evals.py`, `interviews_start_dependencies.py`, `summarize_job_description`, `failed`, `interviews_evals.py`, `KnowledgeRepository`, `complete_chat`, `test_profile_redaction.py`, `InterviewsRepository`, `interviews_answer_service.py`, `provider.py`, `interviews_route.py`, `test_decide.py`, `test_tracing_lifespan.py`, `test_profile_extract.py`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `decode_token`, `interviews_context.py`, `auth_service.py`, `profile_route.py`, `interviews_answer_dependencies.py`, `interviews_feedback_controller.py`, `profile_service.py`, `interviews_constants.py`, `interviews_model.py`, `JobUrlService`, `errors.py`, `make_user`, `test_create_interview.py`, `AnswerIn`, `pytest`, `interviews_start_dependencies.py`, `InterviewsRepository`, `Implementation: Langfuse Tracing`, `interviews_answer_service.py`, `interviews_route.py`, `PageParams`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Tracer` (e.g. with `ChatTrace` and `TracerHandle`) actually correct?**
  _`Tracer` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 14 inferred relationships involving `FakeChatModel` (e.g. with `U3: Migrate to LangChain + provider fallback chain` and `2. What it is`) actually correct?**
  _`FakeChatModel` has 14 INFERRED edges - model-reasoned connections that need verification._
- **Are the 66 inferred relationships involving `LLMResult` (e.g. with `complete_chat()` and `_run()`) actually correct?**
  _`LLMResult` has 66 INFERRED edges - model-reasoned connections that need verification._
- **Are the 44 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 44 INFERRED edges - model-reasoned connections that need verification._