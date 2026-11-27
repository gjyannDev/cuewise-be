# Graph Report - cuewise-be  (2026-11-27)

## Corpus Check
- 524 files · ~492,729 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 9 file(s) not represented in the graph (top: (none) 4, .example 1, .ini 1)

## Summary
- 7463 nodes · 21397 edges · 357 communities (310 shown, 47 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 4118 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3b44fef2`
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
- Completed Steps
- test_summary_evals.py
- Feature: Prompt Registry (one place for prompt versions and routing)
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- test_chat_tracing.py
- test_feedback_evals.py
- test_safe_fetch.py
- test_knowledge_ingest.py
- test_prompt_registry.py
- cuewise-be
- AppLogs
- interviews_schema.py
- test_feedback_endpoint.py
- test_context_strategies.py
- Interviewer
- ChatMessage
- test_tracing.py
- Feature: Context Management for the Interview LLM Calls
- FakeChatModel
- test_context.py
- User
- test_profile_read_resume.py
- noted
- test_knowledge_utils.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- test_chat_contract.py
- test_chat_stream.py
- test_write.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- run_generation
- interviews_job_url_service.py
- test_request_context.py
- LLMResult
- errors.py
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- test_profile_context.py
- test_tracing_routes.py
- test_generation_arms.py
- Rules
- job_description_summary_v2.md
- FakeProvider
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- test_feedback_contract.py
- test_answer_llm.py
- test_feedback_turn.py
- Implementation: U3b1 Interview calls on LangChain
- exception_handlers.py
- setup_logging
- test_gateway.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- InvalidReplyError
- test_evals.py
- Langfuse
- interviews_report_render.py
- interviews_evals.py
- read_resume
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- ChatTrace
- Rubric
- LLMError
- EmbeddingKind
- InterviewQuestion
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- Project
- test_rag_evals.py
- Langfuse Observability
- interviewer_v3.md
- ContextManager
- InterviewType
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_speech.py
- AnswerService
- provider.py
- test_answer_stream.py
- Langfuse Dataset Construction
- parse_log
- Feature: Résumé upload and candidate profile (Slice 8c)
- Role
- test_follow_ups.py
- Feature: Langfuse Tracing
- Langfuse
- load_prompt
- Implementation: Résumé-aware interview (Slice 8d)
- test_decide.py
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- Implementation Steps
- Implementation: U3a LangChain foundation + first chains
- Feature: Agentic Workflow v2 (debug, review-feature, gated loop)
- get_chat_model
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_profile_extract.py
- How to evaluate an AI feature: from the command to the fix
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
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- stream_chat
- ReadableRenderer
- QuestionTurn
- CandidateProfile
- Langfuse v4 project migration
- Judge Calibration
- test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only
- Langfuse CI/CD
- Prompt Engineering
- test_reply_contract.py
- Level
- Implementation: Agentic Workflow v2
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- skill_coverage
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- audio_container
- profile_reply.py
- Tracer
- test_transcript.py
- ReferenceNote
- Learn: Résumé-aware interview (Slice 8d)
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Implementation: LLM as the Interviewer (it asks the questions)
- profile_evals.py
- Implementation: U1 structlog (structured JSON logs)
- test_llm_fixture.py
- interviews_feedback_evals.py
- LLMProvider
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Feature: Interview History List (backend)
- feedback_score_v1.md
- feedback_write_v1.md
- Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)
- test_knowledge_postgres.py
- ingest_corpus
- auth_header
- interviews_rag_evals.py
- test_start_with_profile.py
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- interviews_constants.py
- interviews_feedback.py
- profile_resume_files.py
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- ErrorResponse
- test_guards.py
- Implementation: Three New Interview Roles (designer, qa, devops)
- KnowledgeRepository
- LLMTimeoutError
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
- JobRole
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
- check_prompts
- test_tracing_lifespan.py
- Feature: U1 structlog (structured JSON logs)
- Feature: Job URL (Slice 8b)
- test_generation_eval.py
- scrub_contacts
- QuestionKind
- Implementation: Prompt Registry
- follow_up
- test_speech_contracts.py
- bind_log_context
- parse_interviewer_reply
- test_list_users.py
- Web
- Implementation: Layered Modules (route -> controller -> service -> repository)
- 5. What can go wrong
- get_interviews_service
- Learn: Splitting the interviews dependency wiring
- interviews_model.py
- Implementation: Start an Interview (backend)
- config.py
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- StrategyOutput
- RateLimiter
- Langfuse Observability
- ._attempts
- Feature: Follow-up Questions (decide / write split)
- get_logger
- Learn: Adding interview roles (designer, qa, devops)
- .record_turn
- Langfuse Prompt Migration
- summary
- ModelDecision
- Langfuse Prompt Migration
- TranscriptionOut
- test_context_prompts.py
- test_get_interview.py
- test_answer_with_profile.py
- InterviewsService
- Implementation Steps
- interview-room/README.md
- app_logs
- Implementation: Eval runs in Langfuse (scores + datasets)
- InterviewMessage
- test_log_context.py
- Implementation Plan: Start an Interview (backend)
- test_retrieval_profile.py
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Feature: Layered Modules (route -> controller -> service -> repository)
- Slices in detail
- InterviewerInputs
- FakeLangfuse
- run_task
- llm
- test_retry_budget.py
- Learn: LangChain as the call layer, one task at a time (U3a)
- Feature: LLM as the Interviewer (it asks the questions)
- test_reference_note_context.py
- experiment
- test_answer_interview.py
- get_feedback_limiter
- safe_fetch.py
- FollowUpAction
- MessageRole
- pytest
- test_profile_evals.py
- CandidateProfileRow
- summarize_job_description
- fake_reply
- Slices in detail
- .__init__
- test_fallback_pick.py
- test_profile_redaction.py
- raise_for_status
- Embedder
- Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)
- types.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: Follow-up Questions (decide / write split)
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- .stream
- profile_fixtures.py
- Implementation Plan: Role-Based Access Control (single JWT)
- Implementation Steps
- Implementation Plan: U3b1 Interview calls on LangChain
- Feature: U3b1 Interview calls on LangChain
- Learn: Langfuse experiments for the interviews evals
- fixture
- test_user_ids.py
- ._generate

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 161 edges
2. `FakeChatModel` - 140 edges
3. `LLMResult` - 138 edges
4. `FakeProvider` - 131 edges
5. `User` - 131 edges
6. `JobRole` - 126 edges
7. `LLMError` - 122 edges
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
- `Acceptance Criteria` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py

## Import Cycles
- None detected.

## Communities (357 total, 47 thin omitted)

### Community 0 - "test_langchain_behaviour.py"
Cohesion: 0.07
Nodes (46): ChatGoogleGenerativeAI, Spike results (step 1, `tests/core/ai/test_langchain_behaviour.py`), GenerateContentResponse, google_ai_generativelanguage_v1beta_types, google_protobuf, google_rpc, MonkeyPatch, Any (+38 more)

### Community 1 - "LLMServerError"
Cohesion: 0.13
Nodes (44): anyio_lowlevel, LLMServerError, 5xx or a dropped connection: the provider's side failed., 5. What can go wrong, anyio_backend(), Clock, fields(), make_policy() (+36 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.09
Nodes (49): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, _injection_share(), _mention_share(), notes_overlap() (+41 more)

### Community 3 - "decode_token"
Cohesion: 0.08
Nodes (42): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+34 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.07
Nodes (83): render_text(), html_target(), main(), Path, Session, UUID, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+75 more)

### Community 5 - "auth_service.py"
Cohesion: 0.07
Nodes (44): ConflictError, hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), get_service(), Depends (+36 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (42): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+34 more)

### Community 8 - "Completed Steps"
Cohesion: 0.16
Nodes (17): Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, EligibleChunk, NamedTuple, The k eligible chunks embedded with `model` that are most similar to the query,…, _log_level() (+9 more)

### Community 9 - "test_summary_evals.py"
Cohesion: 0.08
Nodes (49): Check, check_summary(), _dataset_items(), _has_fact(), load_summary_cases(), _print_case(), _print_summary(), Any (+41 more)

### Community 10 - "Feature: Prompt Registry (one place for prompt versions and routing)"
Cohesion: 0.12
Nodes (16): The labelled text the write call is asked for (the parser reads it back…, 6. Try it yourself, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Prompt Registry (one place for prompt versions and routing), Functional (+8 more)

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
Cohesion: 0.10
Nodes (39): anyio_backend(), audio(), Clock, listen_body(), make_synthesizer(), _make(), make_transcriber(), _make() (+31 more)

### Community 16 - "test_chat_tracing.py"
Cohesion: 0.42
Nodes (9): The LangChain tracing callback (spec FR5, AC8, EC14, EC15): one Langfuse…, result(), test_a_call_records_one_generation_with_its_messages_labels_and_usage(), test_a_disabled_tracer_records_nothing(), test_a_failed_call_records_an_error_with_the_error_class(), test_a_langfuse_failure_never_fails_the_call(), test_a_redacted_call_records_the_placeholder_for_input_and_output(), test_retried_attempts_are_still_one_generation_with_the_attempt_count() (+1 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.08
Nodes (54): feedback_dataset_items(), feedback_scores_for(), feedback_trace_output(), load_feedback_cases(), Any, Path, The cases as dataset items: the interview as input, the bands as the expected…, What came out next to what was wanted: the verdict, the overall against its… (+46 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.13
Nodes (42): FetchedPage, Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request (+34 more)

### Community 19 - "test_knowledge_ingest.py"
Cohesion: 0.21
Nodes (23): IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, active(), chunks(), corpus(), FailingOn, interview() (+15 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.20
Nodes (18): Data, PromptVersion, StrEnum, What an interviewer write carries beyond the job description; it picks the…, Status, ast, archived_routes(), incomplete_entries() (+10 more)

### Community 26 - "AppLogs"
Cohesion: 0.20
Nodes (4): AppLogs, LoggedLine, One JSON line of the log file, read the way older tests read a log record:…, _shown()

### Community 27 - "interviews_schema.py"
Cohesion: 0.10
Nodes (41): current_request_id(), Delta, PhaseChanged, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent (+33 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.15
Nodes (45): 5. What can go wrong, interview(), post(), parametrize, POST and GET /api/v1/interviews/{id}/feedback: the end-to-end seam for the…, Insert a stored interview: one main question per answer, optional follow-ups…, row(), rows() (+37 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (37): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+29 more)

### Community 30 - "Interviewer"
Cohesion: 0.11
Nodes (33): Decision, Interviewer, apply_limits(), Deadline, _decision_label(), plan_write(), UUID, The turn's LLM time budget, set once and asked by every call (an injectable… (+25 more)

### Community 31 - "ChatMessage"
Cohesion: 0.06
Nodes (32): OpenAICompatibleProvider, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final…, The caller's task (e.g. `follow_up_decision`) for the retry events, so they…, _task_label(), ChatMessage, BaseModel (+24 more)

### Community 32 - "test_tracing.py"
Cohesion: 0.05
Nodes (41): client(), drain(), FakeClient, FakeObservation, propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result() (+33 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "FakeChatModel"
Cohesion: 0.10
Nodes (41): FakeChatModel, BaseChatModel, BaseModel, Runnable, Pops one scripted reply per call: text (wrapped by `fake_reply`), a ready…, NamedTuple, A structured call's outcome: the parsed object, or None with `error` saying why…, Structured (+33 more)

### Community 35 - "test_context.py"
Cohesion: 0.18
Nodes (14): Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default(), test_a_strategy_without_a_limit_is_never_trimmed() (+6 more)

### Community 36 - "User"
Cohesion: 0.05
Nodes (62): _DeepgramAdapter, attempt(), DeepgramTranscriber, attempt(), _parse(), Response, T, The first channel's best transcript (blank for silence) and the reported audio… (+54 more)

### Community 37 - "test_profile_read_resume.py"
Cohesion: 0.17
Nodes (27): _content(), Image, make_pdf(), A PDF with one page per list. `encrypt` adds a standard security handler whose…, Rect, Text, test_a_long_resume_is_cut_at_the_cap_and_the_log_says_so(), one_column() (+19 more)

### Community 38 - "noted"
Cohesion: 0.15
Nodes (23): long_case(), main(), noted(), reply(), run_case(), test_a_langfuse_outage_does_not_change_the_write_run(), test_a_negative_pause_is_refused(), test_a_provider_error_fails_the_case_without_crashing() (+15 more)

### Community 39 - "test_knowledge_utils.py"
Cohesion: 0.07
Nodes (50): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+42 more)

### Community 40 - "test_layers.py"
Cohesion: 0.12
Nodes (29): Skills Consulted During Implementation, 5. What can go wrong, Known Issues, check_core(), check_layers(), _imports(), _is_llm_library(), _one() (+21 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues, Links (+7 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "test_chat_contract.py"
Cohesion: 0.16
Nodes (23): Build, langchain_core_prompts, _collect(), Profile, AIMessageChunk, BaseException, BaseModel, Exception (+15 more)

### Community 44 - "test_chat_stream.py"
Cohesion: 0.11
Nodes (33): fake_chunks(), BaseException, A streamed reply: one chunk per text part, an exception raised where it stands…, 5. What can go wrong, 6. Try it yourself, StreamOutcome, _fake_stream(), _gemini() (+25 more)

### Community 45 - "test_write.py"
Cohesion: 0.29
Nodes (17): call_lines(), inputs(), The blocking write on the LangChain call layer (U3b1 step 5, FR5, AC5, AC10):…, reply(), run(), test_a_context_too_large_makes_no_call(), build(), test_a_follow_up_takes_the_main_questions_category() (+9 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "run_generation"
Cohesion: 0.07
Nodes (60): build_tracer(), ExperimentRun, NamedTuple, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, What a recorded experiment run left behind: its name and link, and the trace of…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, final_line(), pacer() (+52 more)

### Community 49 - "interviews_job_url_service.py"
Cohesion: 0.09
Nodes (37): JobTextUnreadableError, A pasted page held no job description (too little text, or not recognisably a…, _decode(), Response, Scheme, credentials, port and every resolved address. Returns the address to…, One hop: a page, or the redirect's Location to check next., Header charset, else a <meta> charset, else UTF-8; never raises (bad bytes…, The server answered, but not with an HTML page we are willing to read. (+29 more)

### Community 50 - "test_request_context.py"
Cohesion: 0.07
Nodes (20): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, asyncio, Architecture & Design, fastapi_responses, Receive, Scope (+12 more)

### Community 51 - "LLMResult"
Cohesion: 0.06
Nodes (57): fixed_prompt(), A prompt of already-built messages (our context manager's output), sent exactly…, BuiltContext, ContextTooLargeError, Exception, Context management: the one place that decides what each LLM call sends. The…, Even with every droppable entry gone the input is over the strategy's limit., LLMResult (+49 more)

### Community 52 - "errors.py"
Cohesion: 0.07
Nodes (49): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, JobUrlUnreachableError, JobUrlUnreadableError, NoSpeechError, ProfileExtractionFailedError (+41 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (21): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+13 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.17
Nodes (18): call_lines(), llm_lines(), parametrize, The `llm_call` lines only (the call layer's `retry_wait` / `retry_giveup`…, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_after_the_call_layer(), test_an_invalid_reply_is_retried_once() (+10 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.14
Nodes (36): Open Questions, fail(), error(), import_url(), _post(), long_posting(), page(), paste() (+28 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.09
Nodes (38): TracingProvider, Review, Problem, anyio_backend(), chunk(), Clock, drain(), Interrupted (+30 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.09
Nodes (53): analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table(), Checks, bad_parent() (+45 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.10
Nodes (38): Deviations from Plan, busy(), Clock, completion(), make_provider(), _make(), fixture, parametrize (+30 more)

### Community 59 - "test_profile_context.py"
Cohesion: 0.16
Nodes (26): ContextReport, estimate_tokens(), _log(), NamedTuple, default_strategy(), everything(), fingerprint(), golden_inputs() (+18 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 61 - "test_generation_arms.py"
Cohesion: 0.09
Nodes (28): parse_arms(), `--arms`: comma-separated arm letters (any case), at least two (a ranking…, argparse, parametrize, The generation eval's arms D and E (resume-aware-interview Step 9a; seam S5).…, A fake LLM that keeps every prompt, answering each main question with a new…, RecordingWriter, run() (+20 more)

### Community 62 - "Rules"
Cohesion: 0.09
Nodes (20): caveman, Example output, How to invoke, See also, What it does, 1. Answer first, 2. Kill ceremony, 3. Short word (+12 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "FakeProvider"
Cohesion: 0.14
Nodes (35): FakeProvider, 5. What can go wrong, Deviations from Plan, decision(), hints_of(), labelled_cases(), last_line(), mentions() (+27 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.18
Nodes (26): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, test_a_slow_fake_embedder_waits_at_most_its_budget_then_times_out(), test_fake_embedder_honors_scripted_vectors_and_errors(), test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets(), competencies(), parametrize, RetrievalService.retrieve: the vector / filter / skip ladder (knowledge-base-… (+18 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.18
Nodes (29): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, collect(), follow_up_json(), inputs(), kinds() (+21 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (35): 5. What can go wrong, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,…, Swagger UI builds its request from the OpenAPI schema. Declared as a url-…, stored() (+27 more)

### Community 68 - "test_feedback_contract.py"
Cohesion: 0.16
Nodes (36): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+28 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.10
Nodes (24): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions() (+16 more)

### Community 71 - "test_feedback_turn.py"
Cohesion: 0.16
Nodes (22): Clock, generator(), End-of-interview feedback on the LangChain call layer (U3b1 step 16, FR8, AC8,…, Uses up the budget on its first call, so a retry would start with less than…, score(), score_inputs(), score_json(), SlowFirstCall (+14 more)

### Community 72 - "Implementation: U3b1 Interview calls on LangChain"
Cohesion: 0.11
Nodes (17): When a client leaves mid-stream (stage 3), Baseline Failures, Changes Made, Current Step, Debug Log, Implementation: U3b1 Interview calls on LangChain, Known Issues, Links (+9 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.17
Nodes (24): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, BaseException, Exception (+16 more)

### Community 74 - "setup_logging"
Cohesion: 0.05
Nodes (35): Every speech setting in one read-only group, so the speech factories depend on…, _formatter(), _json(), _json_renderer(), Path, Writes to whatever `sys.stderr` is at the time of the write (test runners and…, Routes every logger through the processor chain. Safe to call again (tests do):…, setup_logging() (+27 more)

### Community 75 - "test_gateway.py"
Cohesion: 0.07
Nodes (42): FakeSynthesizer, FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, Scripted clips (bytes, a full result, or an error), one per call; records each…, BaseModel, One spoken clip. `content_type` is what the vendor says the audio is: the…, `text` spoken in the configured voice, as one whole clip., SynthesisResult (+34 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues, Links (+7 more)

### Community 77 - "InvalidReplyError"
Cohesion: 0.12
Nodes (30): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, parse_profile_reply(), A JSON-text reply, checked against `RawProfile`, then `clean_profile`. The live…, 1. Why it exists (+22 more)

### Community 78 - "test_evals.py"
Cohesion: 0.09
Nodes (38): load_cases(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, Slice 6: Feedback and scoring, The chat model of the `llm` fixture: the summary goes to `llm.summary`; every…, _RoutedChatModel, as_chat() (+30 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "interviews_report_render.py"
Cohesion: 0.15
Nodes (28): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+20 more)

### Community 81 - "interviews_evals.py"
Cohesion: 0.07
Nodes (60): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_reply() (+52 more)

### Community 82 - "read_resume"
Cohesion: 0.12
Nodes (34): make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), _clean(), _has_external_relationship(), Exception, NamedTuple, Reading an uploaded résumé: untrusted bytes in, visible text in reading order… (+26 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.07
Nodes (27): delete_profile(), get_profile(), post, ProfileUser, A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes…, The signed-in user's profile; 404 `PROFILE_NOT_FOUND` before the first upload., Remove the signed-in user's profile for good; 204 also when there was none., upload_resume() (+19 more)

### Community 84 - "ChatTrace"
Cohesion: 0.11
Nodes (13): _chat_messages(), ChatTrace, Any, BaseMessage, TraceLabels, One traced call: started by the first model run it sees, finished by the call…, A stream closed before it finished (client left, or the turn's deadline ran…, LangChain messages in our own shape, so the trace reads like the old layer's… (+5 more)

### Community 85 - "Rubric"
Cohesion: 0.22
Nodes (8): model_validator, Self, One criterion of the feedback rubric: what it asks, an anchor per score, and…, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, RubricCriterion, The anchors of the criteria this interview can be scored on, with this level…, render_rubric()

### Community 86 - "LLMError"
Cohesion: 0.03
Nodes (85): LLMError, LLMRateLimitError, Exception, Base for every provider failure. `retryable` marks faults that may pass on…, _Call, _OutOfTime, parse_retry_after(), BaseException (+77 more)

### Community 87 - "EmbeddingKind"
Cohesion: 0.12
Nodes (27): EmbeddingKind, EmbeddingResult, BaseModel, StrEnum, Clock, make_embedder(), _make(), handler() (+19 more)

### Community 88 - "InterviewQuestion"
Cohesion: 0.07
Nodes (29): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Any, datetime, Session, UUID (+21 more)

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

### Community 93 - "test_rag_evals.py"
Cohesion: 0.08
Nodes (47): _non_negative_seconds(), _parser(), _positive(), ArgumentParser, build_sheet(), competencies_of(), filter_baseline(), Collection (+39 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "ContextManager"
Cohesion: 0.11
Nodes (33): ContextManager, Task, build_context_manager(), FullHistory, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WindowLedger, get_context_manager(), Decides what each LLM call sends; tests swap in one with a tiny limit. (+25 more)

### Community 97 - "InterviewType"
Cohesion: 0.21
Nodes (22): NotEnoughQuestionsError, InterviewType, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 4. How it works, Architecture & Design, _bank(), parametrize (+14 more)

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
Nodes (23): 5. What can go wrong, test_a_transcription_fills_every_result_field(), test_a_vendor_failure_is_an_llm_error_with_its_attempts(), answered(), assert_hidden(), code(), fixture, GET /interviews/{id}/questions/{qid}/speech and /messages/{mid}/speech: the… (+15 more)

### Community 104 - "AnswerService"
Cohesion: 0.08
Nodes (31): AnswerController, UUID, The checks and reads before the stream opens (sync DB work: the route runs it…, AnswerIn, NamedTuple, One event of a streamed turn as the controller yields it; the route encodes it…, StreamEventOut, AnswerService (+23 more)

### Community 105 - "provider.py"
Cohesion: 0.06
Nodes (63): anyio, A LangChain chat model for tests (spec FR6): scripted replies or errors, every…, _finish_reason(), AIMessage, The LangChain call layer's public face (U3a): the `ChatModel` type services are…, _result(), The streamed call of the LangChain call layer (U3b1): `astream()` under the…, Langfuse tracing for the LangChain call layer, through our own `Tracer` (U3a,… (+55 more)

### Community 106 - "test_answer_stream.py"
Cohesion: 0.06
Nodes (34): 5. What can go wrong, 6. Try it yourself, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing() (+26 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "parse_log"
Cohesion: 0.11
Nodes (27): Call, group_requests(), _int(), _json_event(), LogEvent, parse_log(), NamedTuple, Reading the app's own log back: what each request did for an interview, from… (+19 more)

### Community 109 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+7 more)

### Community 110 - "Role"
Cohesion: 0.18
Nodes (22): EmptyProfileError, Exception, No skills and no roles: not a résumé we can use (refused as unreadable, nothing…, Role, _appears(), ground_profile(), keep(), _normalized() (+14 more)

### Community 111 - "test_follow_ups.py"
Cohesion: 0.24
Nodes (18): 5. What can go wrong, 8. Check your understanding, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end() (+10 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional (+6 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "load_prompt"
Cohesion: 0.08
Nodes (37): LevelGroup, Reactions are warmer for people early in their career and briefer for…, _interviewer(), The startup prompt check: every routed prompt version loads and renders through…, _routed(), load_prompt(), load_rubric(), Path (+29 more)

### Community 115 - "Implementation: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Changes Made, Completed Steps, Current Step, Deviations from Plan, Gate: Step 10, real-model runs (yours), Implementation: Résumé-aware interview (Slice 8d), Known Issues, Links (+7 more)

### Community 116 - "test_decide.py"
Cohesion: 0.27
Nodes (18): call_lines(), decision(), inputs(), outcomes(), The decide call on the LangChain call layer with structured output (U3b1 step…, run(), test_a_bad_note_is_dropped_and_the_decision_kept(), test_a_context_too_large_makes_no_call() (+10 more)

### Community 117 - "The fundamentals"
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Implementation Steps"
Cohesion: 0.10
Nodes (24): Page, page_params(), BaseModel, Query, Offset pagination shared by every list endpoint, so clients see one query…, UsersController, get_controller(), get_service() (+16 more)

### Community 121 - "Implementation: U3a LangChain foundation + first chains"
Cohesion: 0.13
Nodes (14): 9 -> 10. Stop: user-run comparison evals, Check results, Completed Steps, Current Step, Debug Log, Implementation: U3a LangChain foundation + first chains, Known Issues, Links (+6 more)

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "get_chat_model"
Cohesion: 0.07
Nodes (33): get_chat_model(), ChatModel, The LangChain chat model, built once at startup; None when LLM is off or the…, get_feedback_service(), ChatModel, datetime, Depends, Session (+25 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "test_profile_extract.py"
Cohesion: 0.11
Nodes (24): Carries the app's Tracer on a chat model (`build_chat_model(..., tracer=)`…, TracerHandle, ExtractionFailedError, Exception, No valid profile: `reason` is invalid_reply, empty_reply, no_time or the…, BaseCallbackHandler, extract(), no_retry_waits() (+16 more)

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

### Community 130 - "test_knowledge_ingest_cli.py"
Cohesion: 0.27
Nodes (13): main(), _parser(), ArgumentParser, Session, ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1() (+5 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "4. How it works"
Cohesion: 0.13
Nodes (24): _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _hex_lightness(), _in_reading_order() (+16 more)

### Community 134 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 135 - "Blind ranking"
Cohesion: 0.12
Nodes (16): Blind ranking, Setup complete-behavioral-junior, Setup near-empty-data-intern, Setup profile-injection-backend-mid, Setup profile-mismatch-backend-mid, Setup strong-backend-mid, X, X (+8 more)

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

### Community 140 - "stream_chat"
Cohesion: 0.10
Nodes (35): complete_chat(), complete_structured(), Any, ChatModel, Runnable, T, TraceLabels, `prompt | model.with_structured_output(schema)` (Gemini's native JSON schema).… (+27 more)

### Community 142 - "ReadableRenderer"
Cohesion: 0.19
Nodes (11): _default_request_id(), _merge_request_fields(), Any, Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything…, Dev console: time, level, short request id, logger, event, then one aligned…, ReadableRenderer, redact_sensitive(), _redacted() (+3 more)

### Community 143 - "QuestionTurn"
Cohesion: 0.10
Nodes (36): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the… (+28 more)

### Community 144 - "CandidateProfile"
Cohesion: 0.22
Nodes (18): CandidateProfile, BaseModel, The multipart upload: exactly one part, `file`. Extra form fields are refused., ResumeUploadIn, ExpectedProfile, _key(), BaseModel, Scoring an extracted profile against a hand-labelled synthetic résumé (resume-… (+10 more)

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
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 151 - "Level"
Cohesion: 0.08
Nodes (45): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackWriteInputs, Plain values for the write call: the stored scores and evidence, never the… (+37 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Skills Consulted During Implementation, Status (+4 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.13
Nodes (27): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+19 more)

### Community 156 - "skill_coverage"
Cohesion: 0.11
Nodes (17): The share of the job description's skills that at least one question mentions;…, skill_coverage(), 6a. Compare experiment runs, Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals (+9 more)

### Community 157 - "Implementation: Interview Room (backend)"
Cohesion: 0.12
Nodes (15): Changes Made, Current Step, Debug Log, Deviations from Plan, Done. Next: `/review-feature`, Implementation: Interview Room (backend), Known Issues, Links (+7 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (14): 9. Review gate (user), Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions (+6 more)

### Community 159 - "audio_container"
Cohesion: 0.28
Nodes (13): audio_container(), AudioContainer, _has_signature(), StrEnum, Audio rules every speech feature shares: which recording containers are…, Recording containers an upload may arrive in (what browsers' MediaRecorder…, The container of an uploaded recording, or None when its declared type isn't…, parametrize (+5 more)

### Community 160 - "profile_reply.py"
Cohesion: 0.14
Nodes (23): NamedTuple, What one summary call gave: the usable summary (None when it can't replace the…, SummaryOutcome, clean_profile(), fit(), ModelProfile, ModelProject, ModelRole (+15 more)

### Community 161 - "Tracer"
Cohesion: 0.05
Nodes (45): AbstractContextManager, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, A named step inside the current trace (a Langfuse `chain`): the generations and… (+37 more)

### Community 162 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 163 - "ReferenceNote"
Cohesion: 0.27
Nodes (16): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, A note an interview was given: what the question writer sees (competency and…, ReferenceNote, names(), ranked(), merge_note_rankings: the quota merge of the job-description and profile…, Notes named by single letters, ranked in the given order with falling scores. (+8 more)

### Community 164 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.11
Nodes (16): UUID, The user's stored profile for an interview prompt, read live (never copied onto…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me (+8 more)

### Community 165 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6) (+7 more)

### Community 166 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 167 - "profile_evals.py"
Cohesion: 0.09
Nodes (26): load_prompt(), Path, Prompt files: versioned Markdown read once per process. Feature modules pass…, `<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in…, build_messages(), extract_profile(), Extraction, ChatModel (+18 more)

### Community 168 - "Implementation: U1 structlog (structured JSON logs)"
Cohesion: 0.13
Nodes (14): Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U1 structlog (structured JSON logs), Known Issues, Links, Open Questions (+6 more)

### Community 169 - "test_llm_fixture.py"
Cohesion: 0.33
Nodes (9): _ask(), parametrize, The `llm` fixture (U3b1): the chat model the app gets serves every task,…, _streamed(), test_a_scripted_error_reaches_the_chat_model_caller_unchanged(), test_one_write_script_serves_blocking_and_streamed_calls_in_order(), test_the_chat_model_routes_by_system_prompt(), test_the_summary_goes_to_its_own_chat_fake() (+1 more)

### Community 170 - "interviews_feedback_evals.py"
Cohesion: 0.08
Nodes (41): FeedbackGenerator, ChatModel, Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), check_feedback(), criterion_spread() (+33 more)

### Community 171 - "LLMProvider"
Cohesion: 0.05
Nodes (39): LLMProvider, Protocol, AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style) (+31 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.09
Nodes (25): Baseline Failures, Baseline Failures, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+17 more)

### Community 174 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)

### Community 178 - "test_knowledge_postgres.py"
Cohesion: 0.08
Nodes (36): alembic_config, InterviewSessionChunk, KnowledgeChunk, KnowledgeChunkScope, One (role, level) a chunk applies to. Rows instead of array columns, so the…, A reference note one interview was given at start: the same notes for every…, _eligible(), Database access for the reference-note corpus. No business rules: which rows to… (+28 more)

### Community 179 - "ingest_corpus"
Cohesion: 0.20
Nodes (14): _embed(), ingest_corpus(), IngestCounts, NamedTuple, embedding_text(), NoteChunk, What a chunk is embedded as: its heading, then its text. The heading names the…, corpus() (+6 more)

### Community 180 - "auth_header"
Cohesion: 0.07
Nodes (30): auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, answer(), _answer(), anyio_backend(), parse_sse(), fixture (+22 more)

### Community 181 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (69): _arm_notes(), ArmInterview, ArmSummary, case_set_problems(), ExtraSetup, ExtraSetupFields, generation_item(), generation_run_scores() (+61 more)

### Community 182 - "test_start_with_profile.py"
Cohesion: 0.25
Nodes (16): 5. What can go wrong, first_question(), profile_of(), Starting an interview with the candidate's profile (resume-aware-interview Step…, A synthetic profile whose every free-text field carries `marker`, so a leak…, sent(), sessions(), test_a_refused_start_leaves_the_interview_in_progress_alone() (+8 more)

### Community 183 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+2 more)

### Community 184 - "interviews_constants.py"
Cohesion: 0.06
Nodes (62): What the interview LLM calls send: the tasks and strategies registered with the…, HeaderSplit, BaseModel, The contract for what the interviewer LLM must reply, and the check that…, A follow-up carries no category: it inherits its main question's, so the model…, _RawFollowUp, _RawReply, The code's say over an answer turn: the shared deadline, the follow-up cap and… (+54 more)

### Community 185 - "interviews_feedback.py"
Cohesion: 0.12
Nodes (30): _check_lengths(), _has_markup(), _normalized(), parse_write_reply(), BaseModel, NamedTuple, _question_score(), QuestionScore (+22 more)

### Community 186 - "profile_resume_files.py"
Cohesion: 0.17
Nodes (11): _escape(), _fill(), plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build…, Color, docx, docx_oxml, docx_oxml_ns (+3 more)

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
Nodes (68): open_stream(), ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied (+60 more)

### Community 203 - "test_guards.py"
Cohesion: 0.10
Nodes (27): health_check(), CurrentUserDep, raise_conflict(), raise_crash(), raise_db_down(), raise_expired(), raise_integrity(), admin_role() (+19 more)

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.15
Nodes (12): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

### Community 211 - "KnowledgeRepository"
Cohesion: 0.12
Nodes (29): KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, notes_fingerprint(), A short id for the ingested notes: changes when any note changes, not when the…, Rank the notes for every labelled query and score where the right note landed,…, run_retrieval() (+21 more)

### Community 220 - "LLMTimeoutError"
Cohesion: 0.06
Nodes (53): _from_status(), _google_error(), _mapped(), BaseException, Map what the LangChain/Gemini call layer raises to our LLMError types (spec…, The LLMError for `exc`, with `exc` as its cause. Messages are fixed text: a…, Seconds from the error's `google.rpc.RetryInfo` detail (Google's Retry-After);…, _retry_after() (+45 more)

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

### Community 234 - "JobRole"
Cohesion: 0.14
Nodes (18): JobRole, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Implementation Steps, Overview (+10 more)

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
Nodes (13): 15. Evals, fault check and graph, Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U2 — One tenacity retry policy for the AI call layer, Links, Open Questions (+5 more)

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
Cohesion: 0.05
Nodes (81): alias, AnswerControllerDep, ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role (+73 more)

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

### Community 252 - "check_prompts"
Cohesion: 0.18
Nodes (18): check_prompts(), PromptCheckError, Exception, One or more routed prompts cannot be sent; the message lists each one., Raises PromptCheckError naming every routed version whose file is missing or…, 4. How it works, 7. What surprised me, Eval log (AI features only) (+10 more)

### Community 253 - "test_tracing_lifespan.py"
Cohesion: 0.20
Nodes (7): fastapi_testclient, The app lifespan runs the prompt check before anything else (prompt-registry…, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 255 - "Feature: U1 structlog (structured JSON logs)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: U1 structlog (structured JSON logs), Functional, Goal, Non-Functional (+6 more)

### Community 256 - "Feature: Job URL (Slice 8b)"
Cohesion: 0.11
Nodes (18): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Job URL (Slice 8b), Functional, Goal, Non-Functional (+10 more)

### Community 257 - "test_generation_eval.py"
Cohesion: 0.15
Nodes (32): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), arm_of(), fill(), generated(), posted(), parametrize, quiet() (+24 more)

### Community 258 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 259 - "QuestionKind"
Cohesion: 0.15
Nodes (28): FeedbackScore, FeedbackScoreInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, The score call: every thread whole, nothing droppable. Over its own limit it…, build_threads(), Evidence, FeedbackThread (+20 more)

### Community 260 - "Implementation: Prompt Registry"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Known Issues (+8 more)

### Community 261 - "follow_up"
Cohesion: 0.16
Nodes (14): Slice 3: Structured follow-up decisions, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open (+6 more)

### Community 262 - "test_speech_contracts.py"
Cohesion: 0.24
Nodes (11): anyio_backend(), _aura(), _deepgram(), _no_wait(), fixture, Response, One contract per speech protocol, run against the fake AND the real adapter (on…, synthesizers() (+3 more)

### Community 263 - "bind_log_context"
Cohesion: 0.16
Nodes (23): bind_log_context(), Adds fields to every later log line of the current request (or, outside a…, log_retrieval(), log_stream_summary(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, Which reference notes an interview got at start: mode, count, scores, how many…, How a streamed turn felt and ended: time to the first event and to the first… (+15 more)

### Community 264 - "parse_interviewer_reply"
Cohesion: 0.13
Nodes (26): _check_question(), InterviewerReply, _normalized(), parse_interviewer_reply(), parse_streamed_reply(), NamedTuple, interviewer_v5's finished question text, checked like a v4 reply. It was…, The rules every written question must pass, whatever format it came in. (+18 more)

### Community 265 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 266 - "Web"
Cohesion: 0.20
Nodes (5): fixture, Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 267 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Changes Made, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 268 - "5. What can go wrong"
Cohesion: 0.24
Nodes (10): 5. What can go wrong, catalog_mismatches(), Collection, A string literal that is exactly a version name, outside the registry: a…, test_a_file_without_an_entry_and_an_entry_without_a_file_are_named(), test_a_version_literal_is_named_but_prose_mentioning_one_is_not(), test_no_version_name_is_written_outside_the_registry(), test_the_catalog_matches_the_prompt_files() (+2 more)

### Community 269 - "get_interviews_service"
Cohesion: 0.13
Nodes (30): get_tracer(), Built once at startup (app lifespan); a disabled tracer when the lifespan…, get_answer_controller(), get_answer_service(), ChatModel, Depends, Session, get_bank() (+22 more)

### Community 270 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 8. Check your understanding, 9. Still open, Learn: Splitting the interviews dependency wiring

### Community 271 - "interviews_model.py"
Cohesion: 0.06
Nodes (18): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, The reference-note corpus (knowledge-base RAG) and the notes each interview was… (+10 more)

### Community 272 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 273 - "config.py"
Cohesion: 0.05
Nodes (71): DeepgramSynthesizer, Aura text-to-speech: the text goes in a JSON body, the voice (`model`) and…, build_chat_model(), build_embedder(), build_provider(), build_synthesizer(), build_transcriber(), _google_chat_model() (+63 more)

### Community 274 - "Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 275 - "Implementation Plan: Agentic Workflow v2"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: Agentic Workflow v2, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 276 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 277 - "StrategyOutput"
Cohesion: 0.10
Nodes (17): StrategyOutput, _counts(), FeedbackWrite, FollowUpDecision, An earlier question as the model would have written it. A follow-up was written…, The decide call: the current thread in full (it judges the latest answer within…, App data at the end of the last user message; untrusted parts (questions,…, The write call: scores, evidence and question texts only; small whatever the… (+9 more)

### Community 290 - "RateLimiter"
Cohesion: 0.08
Nodes (24): RateLimiter, Count one request for `key`: None when allowed, else whole seconds until its…, get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them., Affected Files & Patterns, Approaches Considered, Blockers & Resolutions, Implementation Plan: Interview Room (backend) (+16 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "._attempts"
Cohesion: 0.12
Nodes (18): hint_for(), BaseModel, T, UUID, At most two attempts; a retry only for a reply that came back but broke the…, At most two attempts of the write call only. Failing is fine: the template…, `schema` set: a structured call (the model fills it; `parse` still checks the…, The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a… (+10 more)

### Community 293 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 294 - "get_logger"
Cohesion: 0.13
Nodes (23): AsyncBaseTransport, BaseTransport, AsyncBaseTransport, BaseTransport, get_logger(), Logger, 5. What can go wrong, parametrize (+15 more)

### Community 295 - "Learn: Adding interview roles (designer, qa, devops)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open, Learn: Adding interview roles (designer, qa, devops)

### Community 296 - ".record_turn"
Cohesion: 0.04
Nodes (64): ErrorBody, BaseModel, QuestionNotCurrentError, ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Save one whole turn in one commit: advance the session, the answer, the…, AnswerOut, The predefined acknowledgement for moving on (or completing). The id is set… (+56 more)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "summary"
Cohesion: 0.18
Nodes (9): Constraints, Input, Output, Role, Task, summary(), Functional, Non-Functional (+1 more)

### Community 299 - "ModelDecision"
Cohesion: 0.11
Nodes (22): _RawScoreReply, ModelDecision, ModelEvidence, ModelQuestionScore, ModelScore, BaseModel, The decide call's reply (follow_up_decision_v1): `gap` is null for…, The feedback score call's reply (feedback_score_v2), same shape as… (+14 more)

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 301 - "TranscriptionOut"
Cohesion: 0.15
Nodes (11): Reload rows a commit expired, so reading their fields later needs no database…, POST /interviews/{id}/transcriptions: what the candidate said, for them to…, TranscriptionOut, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me (+3 more)

### Community 302 - "test_context_prompts.py"
Cohesion: 0.14
Nodes (21): A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt(), Testing Strategy, Deviations from Plan (+13 more)

### Community 303 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 304 - "test_answer_with_profile.py"
Cohesion: 0.25
Nodes (12): opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent(), test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile() (+4 more)

### Community 305 - "InterviewsService"
Cohesion: 0.06
Nodes (58): PageParams, NamedTuple, HistorySortColumn, StrEnum, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, interview_out() (+50 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 308 - "app_logs"
Cohesion: 0.04
Nodes (44): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+36 more)

### Community 309 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

### Community 310 - "InterviewMessage"
Cohesion: 0.13
Nodes (17): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409() (+9 more)

### Community 311 - "test_log_context.py"
Cohesion: 0.29
Nodes (9): fixture, Log context on real interview requests (U1 structlog, AC4): `session` and…, Every line of the one request whose access line ends with `path_end`., _request_lines(), started(), test_a_request_for_someone_elses_interview_logs_the_id_it_asked_for(), test_a_start_request_logs_the_new_session_and_the_user_on_every_line(), test_a_streamed_turn_logs_its_session_and_user_from_inside_the_stream() (+1 more)

### Community 312 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.13
Nodes (21): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, 5. What can go wrong, Test Results, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules, Overview (+13 more)

### Community 313 - "test_retrieval_profile.py"
Cohesion: 0.21
Nodes (18): EmbedCall, NamedTuple, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), embedder_for(), RetrievalService.retrieve with the candidate profile's query (resume-aware-…, retrieve() (+10 more)

### Community 314 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 315 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 316 - "Slices in detail"
Cohesion: 0.20
Nodes (10): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 7: Eval maturity (trust the judge, catch regressions), Slice 9: Tool use and agents, Slice: Context management (added after Slice 2) (+2 more)

### Community 317 - "InterviewerInputs"
Cohesion: 0.08
Nodes (28): InterviewerInputs, A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, Plain values for one interviewer or decide call., WithInterviewData, interviewer_inputs(), Affected Files & Patterns, Approaches Considered (+20 more)

### Community 318 - "FakeLangfuse"
Cohesion: 0.06
Nodes (34): _evaluation(), git_commit(), Any, Score, What every eval task moved onto Langfuse experiments shares (langfuse-…, Run every case once, in order, as one Langfuse experiment run; whatever the run…, The short commit hash, `-dirty` when the working tree has changes, `unknown`…, `--note` as the run's description: blank gives none, a long one is cut. (+26 more)

### Community 319 - "run_task"
Cohesion: 0.25
Nodes (15): console_number(), The trace id the fake gives a case in the given repeat's run (write and stream…, run_task(), scores_on(), test_a_failed_check_is_scored_false_with_its_detail(), test_a_provider_error_scores_the_case_failed_and_errored_with_the_class(), test_a_write_result_shows_the_reply_and_the_notes_but_no_expected_action(), test_a_write_run_per_repeat_carries_what_produced_it() (+7 more)

### Community 320 - "llm"
Cohesion: 0.15
Nodes (19): The same rules for an async attempt; waits are awaited, so the event loop stays…, Skills Consulted, 2. What it is, The order of the checks (stages 2 and 4), Approaches Considered, Functional, as_v5_text(), _decision_json() (+11 more)

### Community 321 - "test_retry_budget.py"
Cohesion: 0.14
Nodes (15): anyio_backend(), Clock, counting(), handler(), anyio, fixture, parametrize, The worst-case number of HTTP calls one logical call can make, across both… (+7 more)

### Community 322 - "Learn: LangChain as the call layer, one task at a time (U3a)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Decision: who owns retries (spec FR3) (+2 more)

### Community 323 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 324 - "test_reference_note_context.py"
Cohesion: 0.20
Nodes (18): 5. What can go wrong, first_user(), inputs(), _max_note(), anyio, parametrize, Reference notes in the question writer's input (knowledge-base-rag Step 9;…, test_a_follow_up_write_gets_no_notes_and_the_plain_prompt() (+10 more)

### Community 325 - "experiment"
Cohesion: 0.14
Nodes (18): 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Prompt registry (one place for prompt versions and routing), experiment(), parametrize (+10 more)

### Community 326 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 327 - "get_feedback_limiter"
Cohesion: 0.12
Nodes (11): get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., fresh_limiter(), happy(), owner(), fixture, Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, Fake wall clock for the claim token and the stale takeover. (+3 more)

### Community 328 - "safe_fetch.py"
Cohesion: 0.09
Nodes (17): FetchError, is_public_address(), BaseTransport, Exception, Fetch a web page whose address a user chose, without letting that user reach…, True only for a globally routable unicast address., codecs, 1. Why it exists (+9 more)

### Community 329 - "FollowUpAction"
Cohesion: 0.21
Nodes (19): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect (+11 more)

### Community 330 - "MessageRole"
Cohesion: 0.13
Nodes (19): MessageKind, MessageRole, Transcript item kinds: a question comes from interview_questions, the other two…, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut, build_transcript(), The chat as the user saw it: each question, then its answer and reaction when…, Implementation Steps (+11 more)

### Community 331 - "pytest"
Cohesion: 0.16
Nodes (10): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call() (+2 more)

### Community 332 - "test_profile_evals.py"
Cohesion: 0.15
Nodes (16): build_file(), EvalCase, load_cases(), BaseModel, ChatModel, Path, The case as the file a candidate would upload. Hidden lines are white (PDF) or…, run_case() (+8 more)

### Community 333 - "CandidateProfileRow"
Cohesion: 0.17
Nodes (12): CandidateProfileRow, A user's résumé profile: at most one per user (the unique user_id is the…, ProfileRepository, datetime, Session, UUID, End the read transaction before the slow model call, so no connection sits idle…, The user's one profile, inserted or replaced in one commit. Select-then-write… (+4 more)

### Community 334 - "summarize_job_description"
Cohesion: 0.21
Nodes (16): ChatModel, One summary call; see `SummaryOutcome`. A reply that `validate_summary` rejects…, summarize_job_description(), llm_lines(), no_retry_waits(), fixture, parametrize, The job-description summary on the LangChain layer… (+8 more)

### Community 335 - "fake_reply"
Cohesion: 0.18
Nodes (11): fake_reply(), AIMessage, Any, BaseMessage, ChatGenerationChunk, ChatResult, An AIMessage shaped like Gemini's: usage in `usage_metadata` (None = the vendor…, FakeChatReply (+3 more)

### Community 336 - "Slices in detail"
Cohesion: 0.15
Nodes (12): AI Engineering Upgrade Path (Cuewise), Build order, How to make it stick, Progress, Slices in detail, U0: Baselines, U1: structlog, U4: Prompt templates + Langfuse Prompt Management (+4 more)

### Community 338 - "test_fallback_pick.py"
Cohesion: 0.19
Nodes (15): pick_fallback_question(), Collection, Random, One unused bank question for `position`, used when the LLM is off or its reply…, fixture_bank(), pick(), fixture, parametrize (+7 more)

### Community 339 - "test_profile_redaction.py"
Cohesion: 0.29
Nodes (15): assert_redacted(), assert_traced_in_full(), generations(), inputs(), anyio, resume-aware-interview Step 5: a write whose prompt carries the profile is…, A chat model replying `reply`, with the tracer riding on it as the factory…, run_stream_write() (+7 more)

### Community 340 - "raise_for_status"
Cohesion: 0.19
Nodes (10): Any, _int_or_none(), Any, One streamed request, ending by `end` on the clock: its text chunks, then an…, The token counts an OpenAI-compatible usage object reports; None for any it…, _usage(), raise_for_status(), Map a vendor's HTTP status to the typed errors; 200 passes. `retry_after` is… (+2 more)

### Community 341 - "Embedder"
Cohesion: 0.18
Nodes (8): Embedder, Protocol, 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e)

### Community 342 - "Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 8. Check your understanding, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback), stored_scores_json(), test_a_stale_row_with_stored_scores_is_taken_over_and_only_the_write_call_runs() (+1 more)

### Community 343 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 344 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 345 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 346 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 347 - ".stream"
Cohesion: 0.31
Nodes (4): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Step 11: `FakeProvider.stream`, Reply

### Community 348 - "profile_fixtures.py"
Cohesion: 0.22
Nodes (6): Every interviews prompt version, and which one each LLM call sends. Data only:…, contextvars, dataclasses, A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and…, Synthetic résumé data and the scripted model shared by the profile tests (no…, types

### Community 349 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.22
Nodes (8): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Trade-offs & Rationale

### Community 350 - "Implementation Steps"
Cohesion: 0.22
Nodes (8): Approaches Considered, Blockers & Resolutions, Implementation Plan: U3a LangChain foundation + first chains, Implementation Steps, Overview, Project Rules Applied, Ready to Implement, Spec Requirements -> Implementation

### Community 351 - "Implementation Plan: U3b1 Interview calls on LangChain"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: U3b1 Interview calls on LangChain, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 352 - "Feature: U3b1 Interview calls on LangChain"
Cohesion: 0.22
Nodes (8): Blockers, Constraints, Feature: U3b1 Interview calls on LangChain, Goal, Non-Functional, Out of Scope, Requirements, User Flow

### Community 353 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 354 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 355 - "test_user_ids.py"
Cohesion: 0.70
Nodes (4): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7()

### Community 356 - "._generate"
Cohesion: 0.50
Nodes (3): Any, BaseMessage, ChatResult

## Knowledge Gaps
- **1125 isolated node(s):** `cuewise-be`, `What it does`, `How to invoke`, `Example output`, `See also` (+1120 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2755 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **47 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LLMError` connect `LLMError` to `LLMServerError`, `Cuewise BE — Project Instructions`, `test_speech_contracts.py`, `Completed Steps`, `stream_chat`, `config.py`, `Level`, `interviews_schema.py`, `Interviewer`, `ChatMessage`, `profile_reply.py`, `RateLimiter`, `FakeChatModel`, `User`, `profile_evals.py`, `.record_turn`, `interviews_feedback_evals.py`, `test_chat_stream.py`, `Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)`, `InterviewsService`, `LLMResult`, `errors.py`, `ingest_corpus`, `interviews_rag_evals.py`, `test_openai_compatible_stream.py`, `interviews_constants.py`, `FakeProvider`, `FakeEmbedder`, `test_stream_turn.py`, `llm`, `FollowUpAction`, `test_gateway.py`, `summarize_job_description`, `interviews_evals.py`, `ChatTrace`, `.stream`, `LLMTimeoutError`, `Implementation Steps`, `Implementation Plan: U3b1 Interview calls on LangChain`, `test_speech.py`, `provider.py`, `Feature: Langfuse Tracing`, `get_chat_model`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `test_generation_eval.py`, `Completed Steps`, `test_summary_evals.py`, `stream_chat`, `get_interviews_service`, `test_chat_tracing.py`, `config.py`, `test_feedback_evals.py`, `Level`, `skill_coverage`, `test_feedback_endpoint.py`, `ChatMessage`, `test_tracing.py`, `FakeChatModel`, `noted`, `profile_evals.py`, `interviews_feedback_evals.py`, `test_chat_stream.py`, `test_write.py`, `run_generation`, `InterviewsService`, `LLMResult`, `interviews_rag_evals.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `test_openai_compatible_stream.py`, `interviews_constants.py`, `test_tracing_routes.py`, `FakeLangfuse`, `FakeProvider`, `Learn: LangChain as the call layer, one task at a time (U3a)`, `experiment`, `test_feedback_turn.py`, `get_feedback_limiter`, `test_profile_evals.py`, `summarize_job_description`, `test_evals.py`, `interviews_evals.py`, `KnowledgeRepository`, `ChatTrace`, `Embedder`, `test_profile_redaction.py`, `profile_fixtures.py`, `Implementation Steps`, `AnswerService`, `provider.py`, `test_decide.py`, `test_tracing_lifespan.py`, `get_chat_model`, `test_profile_extract.py`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `Implementation: Langfuse Tracing`, `decode_token`, `auth_service.py`, `AnswerService`, `provider.py`, `InterviewQuestion`, `get_interviews_service`, `interviews_model.py`, `InterviewsService`, `interviews_job_url_service.py`, `test_knowledge_postgres.py`, `interviews_route.py`, `errors.py`, `test_create_interview.py`, `Level`, `interviews_constants.py`, `interviews_schema.py`, `Implementation Steps`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Tracer` (e.g. with `ChatTrace` and `TracerHandle`) actually correct?**
  _`Tracer` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `FakeChatModel` (e.g. with `U3: Migrate to LangChain + provider fallback chain` and `2. What it is`) actually correct?**
  _`FakeChatModel` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 66 inferred relationships involving `LLMResult` (e.g. with `complete_chat()` and `_run()`) actually correct?**
  _`LLMResult` has 66 INFERRED edges - model-reasoned connections that need verification._
- **Are the 44 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 44 INFERRED edges - model-reasoned connections that need verification._