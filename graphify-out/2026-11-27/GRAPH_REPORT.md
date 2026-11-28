# Graph Report - cuewise-be  (2026-11-27)

## Corpus Check
- 533 files · ~500,943 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 9 file(s) not represented in the graph (top: (none) 4, .example 1, .ini 1)

## Summary
- 7574 nodes · 21635 edges · 337 communities (286 shown, 51 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 4220 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3f0090aa`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_langchain_behaviour.py
- LLMServerError
- test_profile_eval_metrics.py
- decode_token
- test_interview_report.py
- auth_dependencies.py
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- Completed Steps
- test_summary_evals.py
- upload_resume
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- test_profile_extract.py
- test_feedback_evals.py
- test_safe_fetch.py
- test_knowledge_ingest.py
- test_prompt_registry.py
- cuewise-be
- test_feedback_contract.py
- interviews_constants.py
- test_feedback_endpoint.py
- test_context_strategies.py
- Interviewer
- run_generation
- Tracer
- Feature: Context Management for the Interview LLM Calls
- FakeChatModel
- ContextManager
- test_list_users.py
- test_profile_read_resume.py
- test_openai_compatible.py
- interviews_knowledge_utils.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- test_chat_contract.py
- ProfileService
- test_chat_stream.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_generation_arms.py
- interviews_job_url_service.py
- get_logger
- read_resume
- interviews_feedback_evals.py
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- errors.py
- test_profile_context.py
- test_tracing_routes.py
- Implementation: U3b2 — Retrieval on LangChain
- Rules
- job_description_summary_v2.md
- test_evals.py
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- interviews_feedback.py
- test_answer_llm.py
- test_feedback_turn.py
- FakeProvider
- exception_handlers.py
- Implementation Plan: Start an Interview (backend)
- test_gateway.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- CandidateProfile
- Slices in detail
- Langfuse
- interviews_report_render.py
- interviews_evals.py
- test_retry_budget.py
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation: U3b1 Interview calls on LangChain
- decision
- RetryPolicy
- EmbeddingKind
- InterviewQuestion
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- Project
- Settings
- Langfuse Observability
- interviewer_v3.md
- test_context_controller.py
- test_select_questions.py
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_speech.py
- interviews_answer_service.py
- interviews_model.py
- test_answer_stream.py
- Langfuse Dataset Construction
- parse_log
- Feature: Résumé upload and candidate profile (Slice 8c)
- Learn: Résumé-aware interview (Slice 8d)
- test_follow_ups.py
- Feature: Langfuse Tracing
- Langfuse
- JobRole
- merge_note_rankings
- test_decide.py
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- User
- test_write.py
- Feature: Agentic Workflow v2 (debug, review-feature, gated loop)
- Implementation Plan: Interview Room (backend)
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- json
- build_chat_model
- Feature: Résumé-aware interview (Slice 8d)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- run_task
- Implementation: Interview History List (backend)
- Judge Calibration
- profile_resume_utils.py
- build_usage_report
- Blind ranking
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- Implementation: U3a LangChain foundation + first chains
- log_llm_call
- summarize_job_description
- test_reaction_pick.py
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- test_reply_contract.py
- score_json
- Implementation: Agentic Workflow v2
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- How to evaluate an AI feature: from the command to the fix
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- audio_container
- profile_reply.py
- Implementation Plan: Langfuse experiments for the interviews evals
- Feature: Interview History List (backend)
- FetchError
- test_start_with_profile.py
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Implementation: LLM as the Interviewer (it asks the questions)
- LLMError
- scrub_contacts
- pytest
- test_fallback_pick.py
- U3b1 stage 2 (decide on LangChain, structured output) vs. the baseline
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Implementation: U1 structlog (structured JSON logs)
- feedback_score_v1.md
- feedback_write_v1.md
- ErrorResponse
- test_profile_evals.py
- failed
- interviews/conftest.py
- interviews_rag_evals.py
- load_prompt
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- hints_of
- test_answer_with_profile.py
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- Implementation: Error Handling
- tests/conftest.py
- clock
- test_retrieval_eval.py
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
- test_transcript.py
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
- ._post
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- check_prompts
- test_tracing_lifespan.py
- Feature: U1 structlog (structured JSON logs)
- Feature: Job URL (Slice 8b)
- test_generation_eval.py
- re
- interviews_context.py
- Implementation: Prompt Registry
- PromptCheckError
- FakeSynthesizer
- test_question_bank.py
- QuestionCategory
- done
- safe_fetch.py
- Implementation Plan: UUID primary keys
- profile_resume_files.py
- config.py
- Learn: Splitting the interviews dependency wiring
- Feature: Langfuse experiments for the interviews evals
- Implementation: Start an Interview (backend)
- LLMResult
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation: Layered Modules (route -> controller -> service -> repository)
- RateLimiter
- Langfuse Observability
- Implementation Plan: Context Management for the Interview LLM Calls
- follow_up
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- .record_turn
- Langfuse Prompt Migration
- main
- U0 baselines
- Langfuse Prompt Migration
- Learn: Layered architecture (route -> controller -> service -> repository)
- test_log_context.py
- test_get_interview.py
- Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)
- get_current_user
- Implementation Steps
- interview-room/README.md
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- 5. What can go wrong
- test_answer_interview.py
- Implementation Plan: U1 structlog (structured JSON logs)
- test_llm_fixture.py
- test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only
- Implementation Plan: Split interviews_dependencies.py by responsibility
- app_logs
- FakeLangfuse
- Learn: Job URL import and SSRF (Slice 8b)
- test_eval_runs.py
- U2 (tenacity) vs. the U0 baseline
- .__call__
- _reset_request_id
- llm
- test_factory.py
- RecordingClient
- summary
- ._covers_every_criterion
- interviews_voice_dependencies.py
- chat_fake.py
- profile_evals.py
- Clock
- Slices in detail
- .insert_feedback
- GoogleEmbedder
- Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)
- fixture
- _RoutedChatModel

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 161 edges
2. `FakeChatModel` - 141 edges
3. `LLMResult` - 138 edges
4. `FakeProvider` - 131 edges
5. `User` - 131 edges
6. `LLMError` - 129 edges
7. `JobRole` - 126 edges
8. `LLMServerError` - 116 edges
9. `Level` - 111 edges
10. `InterviewType` - 107 edges

## Surprising Connections (you probably didn't know these)
- `Completed Steps` --references--> `to_llm_error()`  [INFERRED]
  docs/features/u3a-langchain-foundation/task.md → app/core/ai/chat_errors.py
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `1. Why it exists` --references--> `DeepgramTranscriber`  [INFERRED]
  docs/features/interview-room/learnings.md → app/core/ai/deepgram.py
- `6. Try it yourself` --references--> `get_tracer()`  [INFERRED]
  docs/features/split-interviews-dependencies/learnings.md → app/core/ai/dependencies.py
- `6. Try it yourself` --references--> `EmbeddingSizeError`  [INFERRED]
  docs/features/u3b2-retrieval/learnings.md → app/core/ai/embedder.py

## Import Cycles
- None detected.

## Communities (337 total, 51 thin omitted)

### Community 0 - "test_langchain_behaviour.py"
Cohesion: 0.09
Nodes (43): ChatGoogleGenerativeAI, Spike results (step 1, `tests/core/ai/test_langchain_behaviour.py`), GenerateContentResponse, google_ai_generativelanguage_v1beta_types, google_protobuf, google_rpc, MonkeyPatch, _Flaky (+35 more)

### Community 1 - "LLMServerError"
Cohesion: 0.10
Nodes (57): anyio_lowlevel, Any, LLMRateLimitError, LLMServerError, 5xx or a dropped connection: the provider's side failed., parse_retry_after(), raise_for_status(), The Retry-After header as seconds. Only the delta-seconds form is read; an HTTP… (+49 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.09
Nodes (50): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, _injection_share(), _mention_share(), notes_overlap() (+42 more)

### Community 3 - "decode_token"
Cohesion: 0.12
Nodes (32): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+24 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.11
Nodes (62): analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start(), html_for() (+54 more)

### Community 5 - "auth_dependencies.py"
Cohesion: 0.06
Nodes (53): hash_password(), verify_password(), permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, AuthController, Request -> service call, domain result -> response schema. (+45 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.07
Nodes (54): extract_job_text(), _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), job_term_hits(), pasted_job_text(), _plain() (+46 more)

### Community 8 - "Completed Steps"
Cohesion: 0.10
Nodes (17): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, _eligible(), EligibleChunk, NamedTuple (+9 more)

### Community 9 - "test_summary_evals.py"
Cohesion: 0.07
Nodes (52): wait(), Check, check_summary(), _dataset_items(), _has_fact(), load_summary_cases(), _print_case(), _print_summary() (+44 more)

### Community 10 - "upload_resume"
Cohesion: 0.22
Nodes (11): delete_profile(), get_profile(), post, ProfileUser, A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes…, The signed-in user's profile; 404 `PROFILE_NOT_FOUND` before the first upload., Remove the signed-in user's profile for good; 204 also when there was none., upload_resume() (+3 more)

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
Nodes (35): ProviderConfig, One listed provider, resolved from its vendor block., _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url() (+27 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.13
Nodes (35): anyio_backend(), audio(), listen_body(), make_synthesizer(), make_transcriber(), ok(), fixture, parametrize (+27 more)

### Community 16 - "test_profile_extract.py"
Cohesion: 0.12
Nodes (22): Carries the app's Tracer on a chat model (`build_chat_model(..., tracer=)`…, TracerHandle, BaseCallbackHandler, extract(), no_retry_waits(), fixture, parametrize, `extract_profile` on the LangChain layer: structured output inside the existing… (+14 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.05
Nodes (77): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, criterion_spread(), feedback_dataset_items(), feedback_hints_for(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult (+69 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.14
Nodes (39): Refused before connecting, or the network side failed (DNS, timeout,…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize (+31 more)

### Community 19 - "test_knowledge_ingest.py"
Cohesion: 0.21
Nodes (23): IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, active(), chunks(), corpus(), FailingOn, interview() (+15 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.20
Nodes (18): Data, PromptVersion, StrEnum, Every interviews prompt version, and which one each LLM call sends. Data only:…, What an interviewer write carries beyond the job description; it picks the…, Status, archived_routes(), incomplete_entries() (+10 more)

### Community 26 - "test_feedback_contract.py"
Cohesion: 0.13
Nodes (41): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, Failures, Langfuse nesting (spec assumption to verify) (+33 more)

### Community 27 - "interviews_constants.py"
Cohesion: 0.09
Nodes (47): FeedbackStatus, MessageKind, MessageRole, StrEnum, A feedback row's life: `generating` while a request holds it, then `generated`…, Why an interview has no reference notes at all (logged as…, Transcript item kinds: a question comes from interview_questions, the other two…, RetrievalSkip (+39 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.17
Nodes (40): InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, 5. What can go wrong, interview(), post(), parametrize, POST and GET /api/v1/interviews/{id}/feedback: the end-to-end seam for the…, Insert a stored interview: one main question per answer, optional follow-ups… (+32 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.15
Nodes (38): SummaryInputs, decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+30 more)

### Community 30 - "Interviewer"
Cohesion: 0.09
Nodes (46): Decision, Interviewer, apply_limits(), _decision_label(), plan_write(), UUID, The code's say over an answer turn: the shared deadline, the follow-up cap and…, The code's say over the model's: returns the action and why it overrode the… (+38 more)

### Community 31 - "run_generation"
Cohesion: 0.06
Nodes (56): Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, Unique per command, repeat and arm (Langfuse merges runs that share a name on…, Local time, as the Langfuse list shows the run's start: the name and the…, run_name(), run_stamp(), feedback_run_scores() (+48 more)

### Community 32 - "Tracer"
Cohesion: 0.04
Nodes (72): TraceLabels, build_tracer(), Send what is still buffered, then stop the background exporter. Called once at…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, Tracer, ChatModel, Architecture & Design, Decisions (grilled with the user) (+64 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "FakeChatModel"
Cohesion: 0.07
Nodes (60): fake_reply(), FakeChatModel, AIMessage, Any, BaseChatModel, BaseMessage, BaseModel, ChatGenerationChunk (+52 more)

### Community 35 - "ContextManager"
Cohesion: 0.07
Nodes (37): ContextManager, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., Task, Architecture & Design, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split) (+29 more)

### Community 36 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 37 - "test_profile_read_resume.py"
Cohesion: 0.19
Nodes (24): _content(), Image, make_pdf(), A PDF with one page per list. `encrypt` adds a standard security handler whose…, Rect, Text, test_a_long_resume_is_cut_at_the_cap_and_the_log_says_so(), one_column() (+16 more)

### Community 38 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (37): Deviations from Plan, busy(), Clock, completion(), make_provider(), fixture, parametrize, Response (+29 more)

### Community 39 - "interviews_knowledge_utils.py"
Cohesion: 0.06
Nodes (69): Splitting a note's body into its `##` sections with LangChain's…, Each `##` heading's text; text before the first `##` (the `#` title) has no…, split_sections(), NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, main(), _parser(), ArgumentParser (+61 more)

### Community 40 - "test_layers.py"
Cohesion: 0.11
Nodes (31): ast, Skills Consulted During Implementation, 5. What can go wrong, Blockers & Resolutions, Known Issues, check_core(), check_layers(), _imports() (+23 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues, Links (+7 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "test_chat_contract.py"
Cohesion: 0.10
Nodes (31): Build, langchain_core_prompts, StreamOutcome, _collect(), _fake_stream(), _gemini(), _gemini_stream(), Profile (+23 more)

### Community 44 - "ProfileService"
Cohesion: 0.10
Nodes (19): ChatModel, Random, _out(), ProfileController, The signed-in user's résumé profile: request -> ProfileService, stored row ->…, get_profile_controller(), CandidateProfileRow, A user's résumé profile: at most one per user (the unique user_id is the… (+11 more)

### Community 45 - "test_chat_stream.py"
Cohesion: 0.15
Nodes (28): fake_chunks(), BaseException, A streamed reply: one chunk per text part, an exception raised where it stands…, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, Learn: the interview calls on LangChain (U3b1) (+20 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_generation_arms.py"
Cohesion: 0.09
Nodes (27): parse_arms(), `--arms`: comma-separated arm letters (any case), at least two (a ranking…, parametrize, The generation eval's arms D and E (resume-aware-interview Step 9a; seam S5).…, A fake LLM that keeps every prompt, answering each main question with a new…, RecordingWriter, run(), test_arms_are_parsed_case_insensitively_in_a_fixed_order() (+19 more)

### Community 49 - "interviews_job_url_service.py"
Cohesion: 0.07
Nodes (48): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, Any network-side failure of a job link. One message for every cause, so…, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, SafeFetcher, JobTextFormat (+40 more)

### Community 50 - "get_logger"
Cohesion: 0.05
Nodes (57): bind_log_context(), get_logger(), Logger, Adds fields to every later log line of the current request (or, outside a…, log_retrieval(), log_stream_summary(), Which reference notes an interview got at start: mode, count, scores, how many…, How a streamed turn felt and ended: time to the first event and to the first… (+49 more)

### Community 51 - "read_resume"
Cohesion: 0.17
Nodes (21): make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), read_resume(), Run, parametrize, test_a_corrupt_docx_is_unreadable(), test_a_corrupt_pdf_is_unreadable() (+13 more)

### Community 52 - "interviews_feedback_evals.py"
Cohesion: 0.05
Nodes (64): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackScoreInputs, FeedbackWriteInputs (+56 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (21): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+13 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.17
Nodes (18): call_lines(), llm_lines(), parametrize, The `llm_call` lines only (the call layer's `retry_wait` / `retry_giveup`…, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_after_the_call_layer(), test_an_invalid_reply_is_retried_once() (+10 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.12
Nodes (41): 5. What can go wrong, auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, fail(), error(), import_url(), _post() (+33 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.11
Nodes (33): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+25 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.09
Nodes (53): analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table(), Checks, bad_parent() (+45 more)

### Community 58 - "errors.py"
Cohesion: 0.06
Nodes (56): open_stream(), AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, NoSpeechError, ProfileExtractionFailedError (+48 more)

### Community 59 - "test_profile_context.py"
Cohesion: 0.09
Nodes (48): BuiltContext, ContextReport, estimate_tokens(), _log(), NamedTuple, Context management: the one place that decides what each LLM call sends. The…, A note an interview was given: what the question writer sees (competency and…, ReferenceNote (+40 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 61 - "Implementation: U3b2 — Retrieval on LangChain"
Cohesion: 0.05
Nodes (38): _Chunk, Nearest, NamedTuple, Protocol, UUID, Vector search as a LangChain retriever (U3b2). A retriever is LangChain's "text…, The search's chunks for `vector`, most similar first, through the retriever., VectorRetriever (+30 more)

### Community 62 - "Rules"
Cohesion: 0.09
Nodes (20): caveman, Example output, How to invoke, See also, What it does, 1. Answer first, 2. Kill ceremony, 3. Short word (+12 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_evals.py"
Cohesion: 0.13
Nodes (32): load_cases(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, case(), experiments(), last_line(), main() (+24 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.07
Nodes (62): EmbedCall, FakeEmbedder, NamedTuple, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, KnowledgeRepository, Session (+54 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.16
Nodes (34): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase (+26 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (35): 5. What can go wrong, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,…, Swagger UI builds its request from the OpenAPI schema. Declared as a url-…, stored() (+27 more)

### Community 68 - "interviews_feedback.py"
Cohesion: 0.08
Nodes (54): FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, build_threads(), _check_lengths(), Evidence, FeedbackThread, _has_markup(), _normalized() (+46 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.10
Nodes (24): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., failing_commit(), messages() (+16 more)

### Community 71 - "test_feedback_turn.py"
Cohesion: 0.12
Nodes (25): _RawScoreReply, ModelDecision, ModelEvidence, ModelQuestionScore, ModelScore, BaseModel, What the model is asked to fill on the LangChain layer's structured calls…, The decide call's reply (follow_up_decision_v1): `gap` is null for… (+17 more)

### Community 72 - "FakeProvider"
Cohesion: 0.16
Nodes (17): FakeProvider, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Reply, long_case(), reply(), run_case(), test_a_provider_error_fails_the_case_without_crashing() (+9 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.19
Nodes (22): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, BaseException, Exception (+14 more)

### Community 74 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.10
Nodes (20): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules, Overview, Project Rules Applied, Ready to Implement (+12 more)

### Community 75 - "test_gateway.py"
Cohesion: 0.09
Nodes (36): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, anyio_backend(), _Broken (+28 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues (+8 more)

### Community 77 - "CandidateProfile"
Cohesion: 0.22
Nodes (17): CandidateProfile, UUID, The user's stored profile for an interview prompt, read live (never copied onto…, ExpectedProfile, _key(), BaseModel, Scoring an extracted profile against a hand-labelled synthetic résumé (resume-…, score_profile() (+9 more)

### Community 78 - "Slices in detail"
Cohesion: 0.12
Nodes (17): 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety (+9 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (30): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+22 more)

### Community 81 - "interviews_evals.py"
Cohesion: 0.06
Nodes (80): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_reply() (+72 more)

### Community 82 - "test_retry_budget.py"
Cohesion: 0.09
Nodes (26): decide(), ChatModel, UUID, The decide step of an answer turn: the model suggests following up or moving…, At most two attempts within the decide cap; any failure means "next_question"…, The attempt header the four reply loops share: decide, write, write stream and…, Iterate to get `(attempt, seconds_left)` for each reply attempt that may start.…, ReplyAttempts (+18 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+6 more)

### Community 84 - "Implementation: U3b1 Interview calls on LangChain"
Cohesion: 0.09
Nodes (22): When a client leaves mid-stream (stage 3), Baseline Failures, Changes Made, Current Step, Debug Log, Deviations from Plan, Done, Implementation: U3b1 Interview calls on LangChain (+14 more)

### Community 85 - "decision"
Cohesion: 0.22
Nodes (20): decision(), labelled_cases(), The console lines but the last, with the measured latencies blanked., run_decide(), same_but_latency(), scores_on(), test_a_failed_decision_shows_the_verdict_the_decision_and_the_expected_one(), test_a_passing_case_says_pass_and_a_label_with_a_gap_shows_it() (+12 more)

### Community 86 - "RetryPolicy"
Cohesion: 0.03
Nodes (78): AsyncBaseTransport, BaseTransport, AsyncBaseTransport, BaseTransport, Attempted, _Call, _OutOfTime, Logger (+70 more)

### Community 87 - "EmbeddingKind"
Cohesion: 0.14
Nodes (29): EmbeddingKind, StrEnum, 5. What can go wrong, langchain_core_embeddings, Clock, make_embedder(), _make(), handler() (+21 more)

### Community 88 - "InterviewQuestion"
Cohesion: 0.04
Nodes (64): HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, InterviewMessage, InterviewQuestion, InterviewSession, A candidate answer or the interviewer's reaction to one question. The questions…, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter() (+56 more)

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

### Community 93 - "Settings"
Cohesion: 0.12
Nodes (10): model_validator, Self, The vendor's chat-model settings from `LLM_VENDOR_CHAT_PARAMS` that are set…, Settings, BaseSettings, Step 0: Rename the provider to a vendor-neutral name, field_validator, _settings() (+2 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 97 - "test_select_questions.py"
Cohesion: 0.11
Nodes (31): NotEnoughQuestionsError, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 4. How it works, Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops) (+23 more)

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
Nodes (27): 5. What can go wrong, Review, test_any_other_speak_request_failure_is_a_server_error_not_a_crash(), test_every_configurable_encoding_has_a_media_type(), answered(), assert_hidden(), code(), fixture (+19 more)

### Community 104 - "interviews_answer_service.py"
Cohesion: 0.04
Nodes (92): QuestionNotCurrentError, SessionNotInProgressError, current_request_id(), The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), AnswerController, _error_event() (+84 more)

### Community 105 - "interviews_model.py"
Cohesion: 0.04
Nodes (51): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+43 more)

### Community 106 - "test_answer_stream.py"
Cohesion: 0.06
Nodes (33): 5. What can go wrong, 6. Try it yourself, AnswerController.stream_answer driven directly, for what a test client can't…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing() (+25 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "parse_log"
Cohesion: 0.09
Nodes (31): QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Call, group_requests(), _int(), _json_event(), LogEvent, parse_log() (+23 more)

### Community 109 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+7 more)

### Community 110 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.14
Nodes (13): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+5 more)

### Community 111 - "test_follow_ups.py"
Cohesion: 0.27
Nodes (16): answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries(), test_a_failed_follow_up_write_falls_back_to_the_next_main_bank_question() (+8 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "JobRole"
Cohesion: 0.05
Nodes (102): InterviewType, JobRole, Level, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, EvalSetup, FeedbackEvalSetup, ExtraSetupFields (+94 more)

### Community 115 - "merge_note_rankings"
Cohesion: 0.07
Nodes (41): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, Architecture & Design, Blockers & Resolutions, Decisions (grill-me, 2026-11-14), Deviations during implementation (2026-11-14, see task.md), Implementation Plan: Résumé-aware interview (Slice 8d), Overview (+33 more)

### Community 116 - "test_decide.py"
Cohesion: 0.27
Nodes (18): call_lines(), decision(), inputs(), outcomes(), The decide call on the LangChain call layer with structured output (U3b1 step…, run(), test_a_bad_note_is_dropped_and_the_decision_kept(), test_a_context_too_large_makes_no_call() (+10 more)

### Community 117 - "The fundamentals"
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+17 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "User"
Cohesion: 0.07
Nodes (37): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, User (+29 more)

### Community 121 - "test_write.py"
Cohesion: 0.29
Nodes (17): call_lines(), inputs(), The blocking write on the LangChain call layer (U3b1 step 5, FR5, AC5, AC10):…, reply(), run(), test_a_context_too_large_makes_no_call(), build(), test_a_follow_up_takes_the_main_questions_category() (+9 more)

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "Implementation Plan: Interview Room (backend)"
Cohesion: 0.08
Nodes (24): BaseModel, Every speech setting in one read-only group, so the speech factories depend on…, Speech-to-text (voice answers)., Text-to-speech (the interviewer's voice)., The speech vendor's settings, grouped (see `Settings.speech`). One key and base…, _SpeechPart, SpeechSettings, SttSettings (+16 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+5 more)

### Community 125 - "json"
Cohesion: 0.11
Nodes (31): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, parse_profile_reply(), A JSON-text reply, checked against `RawProfile`, then `clean_profile`. The live…, 1. Why it exists (+23 more)

### Community 126 - "build_chat_model"
Cohesion: 0.23
Nodes (15): build_chat_model(), _google_chat_model(), ChatModel, The LangChain chat model for the primary provider (the tasks migrated in U3a…, langchain_google_genai, fixture, `build_chat_model`: the LangChain chat model built from the same LLM config as…, settings_with() (+7 more)

### Community 127 - "Feature: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Decisions, Edge Cases, Feature: Résumé-aware interview (Slice 8d), Functional, Goal, Known limits (+7 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "run_task"
Cohesion: 0.18
Nodes (18): console_number(), The trace id the fake gives a case in the given repeat's run (write and stream…, run_task(), test_a_failed_check_is_scored_false_with_its_detail(), test_a_good_streamed_reply_passes_every_check(), test_a_provider_error_scores_the_case_failed_and_errored_with_the_class(), down(), test_a_write_result_shows_the_reply_and_the_notes_but_no_expected_action() (+10 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "profile_resume_utils.py"
Cohesion: 0.10
Nodes (38): _clean(), _docx_lines(), paragraph(), table(), _docx_run_visible(), _effective(), _find_columns(), _has_external_relationship() (+30 more)

### Community 134 - "build_usage_report"
Cohesion: 0.22
Nodes (15): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, main(), Session, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately() (+7 more)

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

### Community 140 - "Implementation: U3a LangChain foundation + first chains"
Cohesion: 0.12
Nodes (15): 9 -> 10. Stop: user-run comparison evals, Check results, Completed Steps, Current Step, Debug Log, Implementation: U3a LangChain foundation + first chains, Known Issues, Links (+7 more)

### Community 142 - "log_llm_call"
Cohesion: 0.03
Nodes (68): _default_request_id(), _formatter(), _json(), _json_renderer(), _merge_request_fields(), Any, Path, Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything… (+60 more)

### Community 143 - "summarize_job_description"
Cohesion: 0.21
Nodes (16): ChatModel, One summary call; see `SummaryOutcome`. A reply that `validate_summary` rejects…, summarize_job_description(), llm_lines(), no_retry_waits(), fixture, parametrize, The job-description summary on the LangChain layer… (+8 more)

### Community 144 - "test_reaction_pick.py"
Cohesion: 0.21
Nodes (16): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), Random, A predefined, neutral acknowledgement for the answer just given; never the same…, test_the_rubric_anchors_five_levels_for_every_criterion_and_both_level_groups(), pick(), parametrize (+8 more)

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
Cohesion: 0.26
Nodes (19): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_follow_up_still_asks_one_question_only(), test_a_follow_up_that_repeats_an_earlier_follow_up_is_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing() (+11 more)

### Community 151 - "score_json"
Cohesion: 0.19
Nodes (14): 8. Check your understanding, score_json(), stored_scores_json(), test_a_mixed_interview_scores_each_question_on_its_own_categorys_criteria(), test_a_rejected_reply_and_the_template_fallback_stand_out_in_the_trace(), test_a_stale_row_with_stored_scores_is_taken_over_and_only_the_write_call_runs(), test_a_stated_total_and_an_injected_answer_cannot_move_the_overall(), test_an_invalid_score_reply_is_retried_once_and_a_valid_retry_is_used() (+6 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.13
Nodes (27): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+19 more)

### Community 156 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.14
Nodes (17): injection_ignored(), 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+9 more)

### Community 157 - "Implementation: Interview Room (backend)"
Cohesion: 0.12
Nodes (15): Changes Made, Current Step, Debug Log, Deviations from Plan, Done. Next: `/review-feature`, Implementation: Interview Room (backend), Known Issues, Links (+7 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "audio_container"
Cohesion: 0.25
Nodes (14): audio_container(), AudioContainer, _has_signature(), StrEnum, Audio rules every speech feature shares: which recording containers are…, Recording containers an upload may arrive in (what browsers' MediaRecorder…, The container of an uploaded recording, or None when its declared type isn't…, enum (+6 more)

### Community 160 - "profile_reply.py"
Cohesion: 0.14
Nodes (22): clean_profile(), fit(), ModelProfile, ModelProject, ModelRole, BaseModel, The contract for the profile-extraction reply, and the check that enforces it.…, A schema-valid reply made safe to store: trimmed and cut to the caps, blanks… (+14 more)

### Community 161 - "Implementation Plan: Langfuse experiments for the interviews evals"
Cohesion: 0.05
Nodes (38): AbstractContextManager, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, Run an SDK call; on any failure log what failed (not why: the message could… (+30 more)

### Community 162 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 163 - "FetchError"
Cohesion: 0.33
Nodes (4): FetchError, BaseTransport, Exception, Resolver

### Community 164 - "test_start_with_profile.py"
Cohesion: 0.21
Nodes (18): 5. What can go wrong, embedder(), first_question(), profile_of(), fixture, Starting an interview with the candidate's profile (resume-aware-interview Step…, A synthetic profile whose every free-text field carries `marker`, so a leak…, sent() (+10 more)

### Community 165 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 166 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.13
Nodes (14): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+6 more)

### Community 167 - "LLMError"
Cohesion: 0.06
Nodes (61): anyio, _finish_reason(), The LangChain call layer's public face (U3a): the `ChatModel` type services are…, attempt(), The streamed call of the LangChain call layer (U3b1): `astream()` under the…, Langfuse tracing for the LangChain call layer, through our own `Tracer` (U3a,…, Deepgram over plain httpx: pre-recorded speech-to-text (`POST /v1/listen`, Nova…, EmbeddingSizeError (+53 more)

### Community 168 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 169 - "pytest"
Cohesion: 0.12
Nodes (12): pytest, parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions(), parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms() (+4 more)

### Community 170 - "test_fallback_pick.py"
Cohesion: 0.21
Nodes (14): pick_fallback_question(), Collection, One unused bank question for `position`, used when the LLM is off or its reply…, fixture_bank(), pick(), fixture, parametrize, test_general_and_role_specific_questions_are_both_eligible() (+6 more)

### Community 171 - "U3b1 stage 2 (decide on LangChain, structured output) vs. the baseline"
Cohesion: 0.10
Nodes (15): Failures, Scores, Should this be the new baseline?, U3b1 stage 2 (decide on LangChain, structured output) vs. the baseline, Why it may have improved, Baseline, Failures, Scores (+7 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.10
Nodes (22): Baseline Failures, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL), 1. Why it exists (+14 more)

### Community 174 - "Implementation: U1 structlog (structured JSON logs)"
Cohesion: 0.14
Nodes (13): Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U1 structlog (structured JSON logs), Known Issues, Links, Open Questions (+5 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "ErrorResponse"
Cohesion: 0.04
Nodes (49): ErrorBody, ErrorResponse, BaseModel, Project Conventions, Project Conventions, Acceptance Criteria, Blockers, Constraints (+41 more)

### Community 178 - "test_profile_evals.py"
Cohesion: 0.21
Nodes (10): build_file(), The case as the file a candidate would upload. Hidden lines are white (PDF) or…, LabelledModel, Any, The profile eval runner offline: every synthetic case builds into a readable…, Answers each case with its own label, so the scores test the pipeline and the…, test_a_model_that_answers_the_labels_scores_one_everywhere(), test_every_case_builds_into_a_file_whose_visible_text_holds_its_labels() (+2 more)

### Community 179 - "failed"
Cohesion: 0.10
Nodes (23): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional (+15 more)

### Community 180 - "interviews/conftest.py"
Cohesion: 0.07
Nodes (38): Deviations from Plan, langchain_core_outputs, answer(), _answer(), anyio_backend(), bank(), _bank_question(), _decision_json() (+30 more)

### Community 181 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (82): _arm_notes(), ArmSummary, build_sheet(), case_set_problems(), competencies_of(), ExtraSetup, filter_baseline(), _is_short_items() (+74 more)

### Community 182 - "load_prompt"
Cohesion: 0.24
Nodes (10): load_prompt(), Path, Prompt files: versioned Markdown read once per process. Feature modules pass…, `<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in…, functools, The shared prompt loader (prompt-registry AC9, EC13): one cached read per…, test_a_second_call_does_not_read_the_file_again(), test_an_unknown_version_raises_file_not_found_naming_the_path() (+2 more)

### Community 183 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (10): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+2 more)

### Community 184 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 185 - "hints_of"
Cohesion: 0.26
Nodes (12): hints_of(), mentions(), The hints on one case's result in Langfuse., test_a_cut_off_reply_hints_at_max_tokens_before_quality(), test_a_passing_case_has_no_hints(), test_a_provider_error_hints_that_it_is_not_a_quality_problem(), down(), test_a_reply_that_does_not_parse_hints_at_the_format() (+4 more)

### Community 186 - "test_answer_with_profile.py"
Cohesion: 0.25
Nodes (12): opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent(), test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile() (+4 more)

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

### Community 193 - "Implementation: Error Handling"
Cohesion: 0.17
Nodes (11): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+3 more)

### Community 203 - "tests/conftest.py"
Cohesion: 0.05
Nodes (38): health_check(), CurrentUserDep, sqlalchemy_pool, StringIO, structlog, tempfile, AppLogs, LogCapture (+30 more)

### Community 207 - "clock"
Cohesion: 0.08
Nodes (19): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+11 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.16
Nodes (22): contextvars, A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and…, embedder(), labelled(), quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, 15 cases with the kinds the label rules require: most expect API design first;…, run() (+14 more)

### Community 220 - "LLMTimeoutError"
Cohesion: 0.05
Nodes (60): _from_status(), _google_error(), _mapped(), BaseException, Map what the LangChain/Gemini call layer raises to our LLMError types (spec…, The LLMError for `exc`, with `exc` as its cause. Messages are fixed text: a…, Seconds from the error's `google.rpc.RetryInfo` detail (Google's Retry-After);…, _retry_after() (+52 more)

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

### Community 234 - "test_transcript.py"
Cohesion: 0.28
Nodes (10): fixture, shape(), started(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question(), test_missing_and_foreign_sessions_are_the_same_404() (+2 more)

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
Cohesion: 0.10
Nodes (45): alias, AnswerControllerDep, Permission, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), _per_user_limit(), A route dependency that charges the signed-in user one hit on `get_limiter()`'s…, answer_question() (+37 more)

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

### Community 250 - "._post"
Cohesion: 0.24
Nodes (7): attempt(), attempt(), _parse(), Response, T, The first channel's best transcript (blank for silence) and the reported audio…, One POST that never waits past the total budget; a non-2xx or failed request…

### Community 251 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 252 - "check_prompts"
Cohesion: 0.24
Nodes (12): check_prompts(), Raises PromptCheckError naming every routed version whose file is missing or…, Known Issues, Skills Consulted During Implementation, loader(), load(), The startup prompt check (prompt-registry AC8, EC5, EC6): every routed version…, The real files, except versions that are missing or get extra text appended. (+4 more)

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
Cohesion: 0.16
Nodes (33): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), 5. What can go wrong, arm_of(), fill(), generated(), posted(), parametrize (+25 more)

### Community 258 - "re"
Cohesion: 0.16
Nodes (24): EmptyProfileError, Exception, No skills and no roles: not a résumé we can use (refused as unreadable, nothing…, Role, _appears(), ground_profile(), keep(), _normalized() (+16 more)

### Community 259 - "interviews_context.py"
Cohesion: 0.04
Nodes (81): StrategyOutput, build_context_manager(), _counts(), FeedbackWrite, FollowUpDecision, FullHistory, InterviewerInputs, JobDescriptionSummary (+73 more)

### Community 260 - "Implementation: Prompt Registry"
Cohesion: 0.13
Nodes (14): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Links (+6 more)

### Community 261 - "PromptCheckError"
Cohesion: 0.24
Nodes (7): PromptCheckError, Exception, One or more routed prompts cannot be sent; the message lists each one., fastapi_testclient, The app lifespan runs the prompt check before anything else (prompt-registry…, test_a_failed_prompt_check_stops_startup_before_the_provider_is_built(), broken()

### Community 262 - "FakeSynthesizer"
Cohesion: 0.16
Nodes (9): FakeSynthesizer, Scripted clips (bytes, a full result, or an error), one per call; records each…, BaseModel, One spoken clip. `content_type` is what the vendor says the audio is: the…, `text` spoken in the configured voice, as one whole clip., SynthesisResult, The text-to-speech seam of a test: a scripted synthesizer and a fresh per-test…, No synthesizer configured (DEEPGRAM_API_KEY blank). (+1 more)

### Community 263 - "test_question_bank.py"
Cohesion: 0.14
Nodes (19): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me (+11 more)

### Community 264 - "QuestionCategory"
Cohesion: 0.06
Nodes (77): The labels of one write call. A write whose prompt carries the candidate…, write_trace_labels(), _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_decision_reply(), parse_interviewer_reply() (+69 more)

### Community 265 - "done"
Cohesion: 0.10
Nodes (21): done(), 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, Learn: Streaming and latency (Slice 4, SSE), Testing Strategy (+13 more)

### Community 266 - "safe_fetch.py"
Cohesion: 0.10
Nodes (19): _decode(), FetchedPage, is_public_address(), Response, Fetch a web page whose address a user chose, without letting that user reach…, Scheme, credentials, port and every resolved address. Returns the address to…, One hop: a page, or the redirect's Location to check next., Header charset, else a <meta> charset, else UTF-8; never raises (bad bytes… (+11 more)

### Community 267 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 268 - "profile_resume_files.py"
Cohesion: 0.15
Nodes (12): _escape(), _fill(), plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build…, Color, docx, docx_oxml, docx_oxml_ns (+4 more)

### Community 269 - "config.py"
Cohesion: 0.07
Nodes (70): get_chat_model(), get_synthesizer(), get_tracer(), get_transcriber(), ChatModel, Request, Request dependencies for the AI services every feature shares, built once at…, The LangChain chat model, built once at startup; None when LLM is off or the… (+62 more)

### Community 270 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

### Community 271 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.13
Nodes (14): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional (+6 more)

### Community 272 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 273 - "LLMResult"
Cohesion: 0.03
Nodes (102): complete_chat(), complete_structured(), fixed_prompt(), AIMessage, Any, ChatModel, NamedTuple, Runnable (+94 more)

### Community 274 - "Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 275 - "Implementation Plan: Agentic Workflow v2"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: Agentic Workflow v2, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 276 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 277 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Changes Made, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 290 - "RateLimiter"
Cohesion: 0.12
Nodes (21): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, Per-user caps on paid speech calls. One limiter instance per process: every…, get_resume_limiter(), limit_resume_uploads(), Depends, ProfileUser (+13 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 293 - "follow_up"
Cohesion: 0.09
Nodes (27): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+19 more)

### Community 294 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 295 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 296 - ".record_turn"
Cohesion: 0.07
Nodes (27): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Save one whole turn in one commit: advance the session, the answer, the…, Affected Files & Patterns, Architecture & Design, Deviations from Plan (+19 more)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "main"
Cohesion: 0.16
Nodes (18): html_target(), main(), Path, Session, UUID, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines() (+10 more)

### Community 299 - "U0 baselines"
Cohesion: 0.22
Nodes (8): Before relying on this, Cost, Eval baselines, How to use this file, Live interviews (from `logs/app.log`, before U1), Prompts with no eval baseline (gaps), U0 baselines, U3b1 baselines (old call layer, before the interview calls move to LangChain)

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 301 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository)

### Community 302 - "test_log_context.py"
Cohesion: 0.29
Nodes (9): fixture, Log context on real interview requests (U1 structlog, AC4): `session` and…, Every line of the one request whose access line ends with `path_end`., _request_lines(), started(), test_a_request_for_someone_elses_interview_logs_the_id_it_asked_for(), test_a_start_request_logs_the_new_session_and_the_user_on_every_line(), test_a_streamed_turn_logs_its_session_and_user_from_inside_the_stream() (+1 more)

### Community 303 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 304 - "Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)

### Community 305 - "get_current_user"
Cohesion: 0.11
Nodes (22): ForbiddenError, get_current_user(), Depends, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, check(), require_roles(), check(), AuthServiceDep (+14 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 308 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 309 - "5. What can go wrong"
Cohesion: 0.24
Nodes (10): 5. What can go wrong, catalog_mismatches(), Collection, A string literal that is exactly a version name, outside the registry: a…, test_a_file_without_an_entry_and_an_entry_without_a_file_are_named(), test_a_version_literal_is_named_but_prose_mentioning_one_is_not(), test_no_version_name_is_written_outside_the_registry(), test_the_catalog_matches_the_prompt_files() (+2 more)

### Community 310 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 311 - "Implementation Plan: U1 structlog (structured JSON logs)"
Cohesion: 0.20
Nodes (9): Approaches Considered, Blockers & Resolutions, Implementation Plan: U1 structlog (structured JSON logs), Overview, Project Rules Applied, Ready to Implement, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 312 - "test_llm_fixture.py"
Cohesion: 0.33
Nodes (9): _ask(), parametrize, The `llm` fixture (U3b1): the chat model the app gets serves every task,…, _streamed(), test_a_scripted_error_reaches_the_chat_model_caller_unchanged(), test_one_write_script_serves_blocking_and_streamed_calls_in_order(), test_the_chat_model_routes_by_system_prompt(), test_the_summary_goes_to_its_own_chat_fake() (+1 more)

### Community 313 - "test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only"
Cohesion: 0.36
Nodes (9): Baseline Failures, Baseline Failures, Testing Strategy, Baseline Failures, Testing Strategy, Baseline Failures, result(), test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only() (+1 more)

### Community 314 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 315 - "app_logs"
Cohesion: 0.25
Nodes (8): Completed Steps, Deviations from Plan, Affected Files & Patterns, Affected Files & Patterns, Testing Strategy, Skills Consulted, app_logs(), Every line the real pipeline wrote (after redaction), at DEBUG for the app's…

### Community 316 - "FakeLangfuse"
Cohesion: 0.07
Nodes (24): 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Eval log (AI features only), Learn: Prompt registry (one place for prompt versions and routing), experiment() (+16 more)

### Community 317 - "Learn: Job URL import and SSRF (Slice 8b)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Job URL import and SSRF (Slice 8b)

### Community 318 - "test_eval_runs.py"
Cohesion: 0.05
Nodes (57): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), notes_fingerprint(), pacer() (+49 more)

### Community 319 - "U2 (tenacity) vs. the U0 baseline"
Cohesion: 0.33
Nodes (5): An extra set of runs (not used for the verdict), Failures, Scores, Still to do, U2 (tenacity) vs. the U0 baseline

### Community 323 - "llm"
Cohesion: 0.08
Nodes (30): Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional, Goal (+22 more)

### Community 324 - "test_factory.py"
Cohesion: 0.07
Nodes (49): _DeepgramAdapter, DeepgramSynthesizer, DeepgramTranscriber, Any, Aura text-to-speech: the text goes in a JSON body, the voice (`model`) and…, What both Deepgram adapters share: one authenticated client, the retry policy…, build_embedder(), build_provider() (+41 more)

### Community 327 - "RecordingClient"
Cohesion: 0.13
Nodes (9): fresh_limiter(), happy(), owner(), fixture, Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, Fake wall clock for the claim token and the stale takeover., recording(), RecordingClient (+1 more)

### Community 328 - "summary"
Cohesion: 0.25
Nodes (6): Constraints, Input, Output, Role, Task, summary()

### Community 330 - "interviews_voice_dependencies.py"
Cohesion: 0.08
Nodes (38): Protocol, The text-to-speech contract features code against, next to the speech-to-text…, SpeechSynthesizer, Protocol, Transcriber, NotFoundError, Response, UUID (+30 more)

### Community 331 - "chat_fake.py"
Cohesion: 0.17
Nodes (12): A LangChain chat model for tests (spec FR6): scripted replies or errors, every…, google_api_core, langchain_core_language_models, langchain_core_output_parsers, operator, parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call() (+4 more)

### Community 332 - "profile_evals.py"
Cohesion: 0.07
Nodes (36): build_messages(), extract_profile(), Extraction, ExtractionFailedError, ChatModel, Exception, NamedTuple, The extraction call: scrubbed résumé text in, a validated profile out (resume-… (+28 more)

### Community 336 - "Slices in detail"
Cohesion: 0.14
Nodes (13): AI Engineering Upgrade Path (Cuewise), Build order, How to make it stick, Progress, Slices in detail, U0: Baselines, U1: structlog, U4: Prompt templates + Langfuse Prompt Management (+5 more)

### Community 341 - "GoogleEmbedder"
Cohesion: 0.04
Nodes (62): Embedder, EmbeddingResult, BaseModel, Protocol, GoogleEmbedder, _log_level(), NamedTuple, UUID (+54 more)

### Community 342 - "Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)"
Cohesion: 0.33
Nodes (5): 1. Why it exists, 2. What it is, 3. When to use it, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)

### Community 354 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 356 - "_RoutedChatModel"
Cohesion: 0.20
Nodes (9): Any, BaseMessage, ChatResult, The chat model of the `llm` fixture: the summary goes to `llm.summary`; every…, _RoutedChatModel, as_chat(), run_stream_case(), test_a_streamed_provider_error_fails_the_case_without_crashing() (+1 more)

## Knowledge Gaps
- **1150 isolated node(s):** `cuewise-be`, `What it does`, `How to invoke`, `Example output`, `See also` (+1145 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2802 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **51 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `test_generation_eval.py`, `QuestionCategory`, `test_summary_evals.py`, `config.py`, `log_llm_call`, `Feature: Langfuse experiments for the interviews evals`, `test_profile_extract.py`, `LLMResult`, `summarize_job_description`, `test_feedback_evals.py`, `test_feedback_endpoint.py`, `run_generation`, `Implementation Plan: Langfuse experiments for the interviews evals`, `FakeChatModel`, `LLMError`, `ProfileService`, `test_chat_stream.py`, `test_profile_evals.py`, `interviews_feedback_evals.py`, `interviews_rag_evals.py`, `test_openai_compatible_stream.py`, `FakeLangfuse`, `test_tracing_routes.py`, `test_eval_runs.py`, `test_evals.py`, `test_factory.py`, `test_feedback_turn.py`, `RecordingClient`, `profile_evals.py`, `interviews_evals.py`, `test_retrieval_eval.py`, `GoogleEmbedder`, `RetryPolicy`, `InterviewQuestion`, `LLMTimeoutError`, `interviews_answer_service.py`, `test_decide.py`, `test_write.py`, `test_tracing_lifespan.py`, `build_chat_model`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Why does `LLMError` connect `LLMError` to `LLMServerError`, `FakeSynthesizer`, `Cuewise BE — Project Instructions`, `QuestionCategory`, `log_llm_call`, `summarize_job_description`, `LLMResult`, `Interviewer`, `FakeChatModel`, `.record_turn`, `test_chat_stream.py`, `Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)`, `interviews_feedback_evals.py`, `interviews_rag_evals.py`, `errors.py`, `FakeEmbedder`, `test_stream_turn.py`, `llm`, `FakeProvider`, `interviews_voice_dependencies.py`, `test_gateway.py`, `profile_evals.py`, `interviews_evals.py`, `test_retry_budget.py`, `GoogleEmbedder`, `RetryPolicy`, `LLMTimeoutError`, `test_speech.py`, `parse_log`, `Feature: Langfuse Tracing`, `Implementation Plan: Interview Room (backend)`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Why does `FakeProvider` connect `FakeProvider` to `run_task`, `interviews_context.py`, `QuestionCategory`, `done`, `LLMResult`, `score_json`, `test_feedback_endpoint.py`, `run_generation`, `Tracer`, `Feature: Context Management for the Interview LLM Calls`, `Implementation Plan: Langfuse experiments for the interviews evals`, `LLMError`, `.record_turn`, `test_chat_stream.py`, `test_generation_arms.py`, `ErrorResponse`, `failed`, `interviews/conftest.py`, `interviews_rag_evals.py`, `hints_of`, `test_evals.py`, `llm`, `test_factory.py`, `test_feedback_turn.py`, `Slices in detail`, `Implementation: U3b1 Interview calls on LangChain`, `decision`, `RetryPolicy`, `_RoutedChatModel`, `JobRole`, `The fundamentals`, `Implementation Plan: Résumé upload and candidate profile (Slice 8c)`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Tracer` (e.g. with `ChatTrace` and `TracerHandle`) actually correct?**
  _`Tracer` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 14 inferred relationships involving `FakeChatModel` (e.g. with `U3: Migrate to LangChain + provider fallback chain` and `2. What it is`) actually correct?**
  _`FakeChatModel` has 14 INFERRED edges - model-reasoned connections that need verification._
- **Are the 66 inferred relationships involving `LLMResult` (e.g. with `complete_chat()` and `_run()`) actually correct?**
  _`LLMResult` has 66 INFERRED edges - model-reasoned connections that need verification._
- **Are the 44 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 44 INFERRED edges - model-reasoned connections that need verification._