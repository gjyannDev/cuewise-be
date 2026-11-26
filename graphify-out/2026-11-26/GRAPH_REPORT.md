# Graph Report - cuewise-be  (2026-11-26)

## Corpus Check
- 506 files · ~469,596 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 9 file(s) not represented in the graph (top: (none) 4, .example 1, .ini 1)

## Summary
- 7176 nodes · 20292 edges · 351 communities (292 shown, 59 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 3862 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dc0ee662`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_langchain_behaviour.py
- test_retry.py
- test_profile_eval_metrics.py
- config.py
- test_interview_report.py
- User
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- Completed Steps
- Tracer
- WithInterviewData
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)
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
- test_rag_evals.py
- test_tracing.py
- Feature: Context Management for the Interview LLM Calls
- FakeChatModel
- interviews_rag_evals.py
- typing
- interviews_service.py
- llm
- interviews_knowledge_utils.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- test_chat_contract.py
- interviews_job_url_service.py
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_evals.py
- test_feedback_contract.py
- get_logger
- InterviewerInputs
- Implementation Plan: Résumé-aware interview (Slice 8d)
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- ContextManager
- logging.py
- test_context_controller.py
- Rules
- job_description_summary_v2.md
- errors.py
- FakeEmbedder
- test_stream_turn.py
- test_profile_routes.py
- openai_compatible.py
- test_answer_llm.py
- test_knowledge_postgres.py
- KnowledgeRepository
- exception_handlers.py
- profile_extract.py
- fake.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- InvalidReplyError
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- interviews_report_render.py
- run_stream_case
- profile_resume_files.py
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_profile_redaction.py
- pydantic
- RetryPolicy
- LLMBadResponseError
- RateLimiter
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- profile_schema.py
- test_retrieval_profile_cases.py
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
- QuestionCategory
- Role
- test_reaction_pick.py
- Langfuse Dataset Construction
- parse_log
- ChatTrace
- Implementation: U3a LangChain foundation + first chains
- test_follow_ups.py
- Feature: Langfuse Tracing
- Langfuse
- load_prompt
- Feature: Interview Feedback and Scoring (Slice 6)
- tests/conftest.py
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- test_guards.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Agentic Workflow v2 (debug, review-feature, gated loop)
- test_profile_read_resume.py
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Feature: Résumé upload and candidate profile (Slice 8c)
- How to evaluate an AI feature: from the command to the fix
- Feature: Résumé-aware interview (Slice 8d)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- interviews_model.py
- Implementation: Interview History List (backend)
- Judge Calibration
- profile_resume_utils.py
- build_usage_report
- Setup complete-behavioral-junior
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- ReferenceNote
- follow_up
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
- json
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- scrub_contacts
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Steps
- InterviewMessage
- Implementation: Résumé-aware interview (Slice 8d)
- Learn: Résumé-aware interview (Slice 8d)
- interviews_context.py
- test_feedback_context.py
- Implementation Steps
- interviews_utils.py
- hint_for
- summarize_job_description
- test_request_context.py
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- Feature: Interview History List (backend)
- feedback_score_v1.md
- feedback_write_v1.md
- interviews_shared_dependencies.py
- JobRole
- Slices in detail
- Feature: Langfuse experiments for the interviews evals
- Implementation: LLM as the Interviewer (it asks the questions)
- test_start_with_profile.py
- interviews_schema.py
- test_streamed_reply.py
- _Tts
- pytest
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
- LLMServerError
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
- Feature: Follow-up Questions (decide / write split)
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
- limit_feedback
- test_answer_interview.py
- Implementation: Prompt Registry
- interviews_feedback_controller.py
- FakeLangfuse
- bind_log_context
- test_answer_with_profile.py
- chat_fake.py
- Web
- Implementation: Layered Modules (route -> controller -> service -> repository)
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation: Eval runs in Langfuse (scores + datasets)
- test_fallback_pick.py
- test_job_description_summary.py
- types.py
- Implementation Plan: UUID primary keys
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- AI Engineering Learning Path (Cuewise)
- Learn: Splitting the interviews dependency wiring
- test_stream_answer.py
- Langfuse Observability
- check_layers
- interviews_knowledge_ingest.py
- Implementation Plan: Role-Based Access Control (single JWT)
- FakeClient
- Feature: Layered Modules (route -> controller -> service -> repository)
- Langfuse Prompt Migration
- profile_extract_v1.md
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- Langfuse Prompt Migration
- test_factory.py
- Slices in detail
- test_get_interview.py
- Implementation Plan: U1 structlog (structured JSON logs)
- InterviewQuestion
- Implementation Steps
- interview-room/README.md
- test_list_users.py
- check_core
- interviews_prompt_registry.py
- test_log_context.py
- Implementation Plan: Context Management for the Interview LLM Calls
- Implementation Plan: Follow-up Questions (decide / write split)
- experiments
- interviews_feedback_service.py
- U0 baselines
- clock
- test_eval_runs.py
- Feature: U3a LangChain foundation + first chains
- test_chat_tracing.py
- test_profile_extract.py
- Learn: Adding interview roles (designer, qa, devops)
- Learn: Prompt registry (one place for prompt versions and routing)
- test_profile_evals.py
- _Stt
- traces
- RecordingClient
- SafeFetcher
- Langfuse
- Learn: Layered architecture (route -> controller -> service -> repository)
- test_me.py
- ProfileService
- U2 (tenacity) vs. the U0 baseline
- .agents/skills/langfuse/SKILL.md
- Langfuse CLI Reference
- 2. Langfuse Documentation
- 2. Langfuse Documentation
- test_user_ids.py
- ._generate

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
- `Acceptance Criteria` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py

## Import Cycles
- None detected.

## Communities (351 total, 59 thin omitted)

### Community 0 - "test_langchain_behaviour.py"
Cohesion: 0.09
Nodes (43): ChatGenerationChunk, ChatGoogleGenerativeAI, Spike results (step 1, `tests/core/ai/test_langchain_behaviour.py`), GenerateContentResponse, google_ai_generativelanguage_v1beta_types, google_protobuf, google_rpc, MonkeyPatch (+35 more)

### Community 1 - "test_retry.py"
Cohesion: 0.14
Nodes (42): anyio_lowlevel, parse_retry_after(), The Retry-After header as seconds. Only the delta-seconds form is read; an HTTP…, 5. What can go wrong, anyio_backend(), Clock, fields(), make_policy() (+34 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.08
Nodes (53): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, _injection_share(), _mention_share(), notes_overlap() (+45 more)

### Community 3 - "config.py"
Cohesion: 0.09
Nodes (39): BaseModel, Every speech setting in one read-only group, so the speech factories depend on…, Speech-to-text (voice answers)., Text-to-speech (the interviewer's voice)., The speech vendor's settings, grouped (see `Settings.speech`). One key and base…, _SpeechPart, SpeechSettings, SttSettings (+31 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.10
Nodes (63): analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start(), html_for() (+55 more)

### Community 5 - "User"
Cohesion: 0.07
Nodes (53): InvalidCredentialsError, hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), get_current_user(), get_service() (+45 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "Completed Steps"
Cohesion: 0.08
Nodes (33): Embedder, Protocol, log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip (+25 more)

### Community 9 - "Tracer"
Cohesion: 0.07
Nodes (46): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, wait(), Check, check_summary(), _has_fact(), load_summary_cases(), _print_case() (+38 more)

### Community 10 - "WithInterviewData"
Cohesion: 0.06
Nodes (37): build_context_manager(), FullHistory, A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WithInterviewData, The labelled text the write call is asked for (the parser reads it back…, 6. Try it yourself (+29 more)

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
Nodes (42): Review, anyio_backend(), audio(), Clock, listen_body(), make_synthesizer(), _make(), make_transcriber() (+34 more)

### Community 16 - "Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)"
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 8. Check your understanding, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.05
Nodes (94): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for() (+86 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.12
Nodes (42): Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, Request, Response (+34 more)

### Community 19 - "test_knowledge_ingest.py"
Cohesion: 0.15
Nodes (32): _embed(), ingest_corpus(), IngestCounts, IngestError, Exception, NamedTuple, Ingestion: turn the validated note chunks into stored rows with their…, Ingestion stopped; the message names the chunk (or the setting) and the reason,… (+24 more)

### Community 20 - "test_prompt_registry.py"
Cohesion: 0.17
Nodes (19): Data, What an interviewer write carries beyond the job description; it picks the…, 5. What can go wrong, catalog_mismatches(), Collection, The prompt registry's guards (prompt-registry AC1, AC2, AC6, EC1-EC4). Each…, A string literal that is exactly a version name, outside the registry: a…, real_routes() (+11 more)

### Community 26 - "interviews/conftest.py"
Cohesion: 0.07
Nodes (35): answer(), _answer(), anyio_backend(), _bank_question(), _decision_json(), delete_profile(), _delete(), make_bank_question() (+27 more)

### Community 27 - "interviews_answer_service.py"
Cohesion: 0.07
Nodes (54): QuestionNotCurrentError, SessionNotInProgressError, log_stream_summary(), How a streamed turn felt and ended: time to the first event and to the first…, PhaseChanged, QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and… (+46 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.11
Nodes (62): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 5. What can go wrong, fresh_limiter(), happy() (+54 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.18
Nodes (35): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+27 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.09
Nodes (16): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+8 more)

### Community 31 - "test_rag_evals.py"
Cohesion: 0.11
Nodes (37): build_sheet(), competencies_of(), Exception, _ranking(), _rating(), The grading file can't be read; the message starts with the line and gives the…, The share of the job description's skills that at least one question mentions;…, One interview's main questions through the streamed writer's text format (the… (+29 more)

### Community 32 - "test_tracing.py"
Cohesion: 0.09
Nodes (29): drain(), Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), _settings(), test_a_redacted_call_records_a_placeholder_instead_of_the_messages(), test_a_redacted_failure_records_no_partial_text(), test_a_redacted_stream_closed_early_records_no_partial_text(), test_a_redacted_success_keeps_model_usage_and_labels_but_not_the_reply() (+21 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "FakeChatModel"
Cohesion: 0.08
Nodes (48): fake_reply(), FakeChatModel, AIMessage, Any, BaseChatModel, BaseMessage, BaseModel, ChatResult (+40 more)

### Community 35 - "interviews_rag_evals.py"
Cohesion: 0.04
Nodes (130): anyio_from_thread, build_tracer(), ExperimentRun, NamedTuple, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, What a recorded experiment run left behind: its name and link, and the trace of…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, final_line() (+122 more)

### Community 36 - "typing"
Cohesion: 0.05
Nodes (50): Protocol, The text-to-speech contract features code against, next to the speech-to-text…, `text` spoken in the configured voice, as one whole clip., SpeechSynthesizer, Protocol, The speech-to-text contract features code against, separate from the text-only…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber (+42 more)

### Community 37 - "interviews_service.py"
Cohesion: 0.09
Nodes (42): ProfileRequiredError, An interview asked to use the candidate's profile, and there is none to use…, HistorySortColumn, StrEnum, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, interview_out() (+34 more)

### Community 38 - "llm"
Cohesion: 0.07
Nodes (29): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+21 more)

### Community 39 - "interviews_knowledge_utils.py"
Cohesion: 0.09
Nodes (46): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+38 more)

### Community 40 - "test_layers.py"
Cohesion: 0.20
Nodes (17): ast, 5. What can go wrong, _is_llm_library(), _one(), parametrize, The layer rules of app/modules (CLAUDE.md, "Architecture"): route -> controller…, test_a_feature_ai_folder_may_import_langchain(), test_a_feature_importing_another_features_repository_is_reported() (+9 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues, Links (+7 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "test_chat_contract.py"
Cohesion: 0.12
Nodes (31): complete_chat(), complete_structured(), AIMessage, Any, ChatModel, Runnable, T, TraceLabels (+23 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.11
Nodes (32): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, Any network-side failure of a job link. One message for every cause, so…, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, JobTextFormat, Which clipboard copy the client sent: the HTML one when the browser has it (its… (+24 more)

### Community 45 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Architecture & Design, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview (+6 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.08
Nodes (29): audio_container(), AudioContainer, _has_signature(), StrEnum, Audio rules every speech feature shares: which recording containers are…, Recording containers an upload may arrive in (what browsers' MediaRecorder…, The container of an uploaded recording, or None when its declared type isn't…, parametrize (+21 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.06
Nodes (104): FakeProvider, load_cases(), main(), pause_for(), Path, Seconds to wait between cases: what `--pause-seconds` asked for, else the…, run_case(), 5. What can go wrong (+96 more)

### Community 49 - "test_feedback_contract.py"
Cohesion: 0.07
Nodes (72): assess_evidence(), build_threads(), _check_lengths(), compute_overall(), Evidence, FeedbackThread, _has_markup(), _normalized() (+64 more)

### Community 50 - "get_logger"
Cohesion: 0.06
Nodes (48): _default_request_id(), get_logger(), _merge_request_fields(), Any, Logger, Path, Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything…, Dev console: time, level, short request id, logger, event, then one aligned… (+40 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.09
Nodes (51): InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, apply_limits(), Deadline, _decision_label(), plan_write() (+43 more)

### Community 52 - "Implementation Plan: Résumé-aware interview (Slice 8d)"
Cohesion: 0.08
Nodes (20): ProfileRepository, datetime, Session, UUID, End the read transaction before the slow model call, so no connection sits idle…, The user's one profile, inserted or replaced in one commit. Select-then-write…, Hard delete; a no-op when there is none., ChatModel (+12 more)

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
Cohesion: 0.11
Nodes (34): Review, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok() (+26 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (61): Call, group_requests(), _int(), NamedTuple, The events of each request, oldest request first (the id is on every line of…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer., Turn (+53 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (37): Deviations from Plan, busy(), Clock, completion(), make_provider(), fixture, parametrize, Response (+29 more)

### Community 59 - "ContextManager"
Cohesion: 0.10
Nodes (49): ContextManager, estimate_tokens(), Task, WindowLedger, 5. What can go wrong, test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), test_the_guard_never_drops_the_current_thread() (+41 more)

### Community 60 - "logging.py"
Cohesion: 0.12
Nodes (11): _formatter(), _json(), _json_renderer(), The app's logging: structlog on top of the standard library's `logging`. Every…, contextlib, Constraints, logging_handlers, Processor (+3 more)

### Community 61 - "test_context_controller.py"
Cohesion: 0.25
Nodes (12): candidate_messages(), noted(), fixture, run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer() (+4 more)

### Community 62 - "Rules"
Cohesion: 0.09
Nodes (20): caveman, Example output, How to invoke, See also, What it does, 1. Answer first, 2. Kill ceremony, 3. Short word (+12 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "errors.py"
Cohesion: 0.08
Nodes (47): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ErrorBody, NoSpeechError, ProfileExtractionFailedError, ProfileNotFoundError (+39 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.10
Nodes (45): EmbedCall, FakeEmbedder, NamedTuple, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), embedder_for() (+37 more)

### Community 66 - "test_stream_turn.py"
Cohesion: 0.16
Nodes (34): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase (+26 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.10
Nodes (36): 5. What can go wrong, Synthetic résumé data and the scripted model shared by the profile tests (no…, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,…, Swagger UI builds its request from the OpenAPI schema. Declared as a url-… (+28 more)

### Community 68 - "openai_compatible.py"
Cohesion: 0.11
Nodes (16): _int_or_none(), Any, ReasoningEffort, Response, OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, Same request with `stream: true`: chunks as they arrive, then the final…, One streamed request, ending by `end` on the clock: its text chunks, then an…, The caller's task (e.g. `follow_up_decision`) for the retry events, so they… (+8 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.11
Nodes (22): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions() (+14 more)

### Community 71 - "test_knowledge_postgres.py"
Cohesion: 0.17
Nodes (17): alembic_config, cosine_similarity(), 1 = same direction (same meaning), 0 = unrelated, -1 = opposite. Length is…, cuewise-be, Development database (Postgres 18 + pgvector), Reference notes (knowledge-base RAG), alembic_config(), make_chunk() (+9 more)

### Community 72 - "KnowledgeRepository"
Cohesion: 0.09
Nodes (25): KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, Store one chunk with its scopes, retiring the row it replaces, in one commit (a…, parse_arms(), `--arms`: comma-separated arm letters (any case), at least two (a ranking…, parametrize (+17 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.13
Nodes (27): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, BaseException, Exception (+19 more)

### Community 74 - "profile_extract.py"
Cohesion: 0.10
Nodes (29): fixed_prompt(), A prompt of already-built messages (our context manager's output), sent exactly…, Condense a long job description once, so later calls send less…, build_messages(), extract_profile(), Extraction, ChatModel, NamedTuple (+21 more)

### Community 75 - "fake.py"
Cohesion: 0.05
Nodes (64): anyio, _DeepgramAdapter, DeepgramSynthesizer, attempt(), DeepgramTranscriber, attempt(), _parse(), Any (+56 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues (+8 more)

### Community 77 - "InvalidReplyError"
Cohesion: 0.12
Nodes (30): InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, parse_profile_reply(), A JSON-text reply, checked against `RawProfile`, then `clean_profile`. The live…, 1. Why it exists (+22 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.22
Nodes (6): Credentials, Discovery, Install, Langfuse CLI Reference, Skill Feedback, Submission options

### Community 80 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (29): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+21 more)

### Community 81 - "run_stream_case"
Cohesion: 0.06
Nodes (54): _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, Check, check_decision(), check_reply(), check_streamed_reply() (+46 more)

### Community 82 - "profile_resume_files.py"
Cohesion: 0.12
Nodes (26): build_file(), The case as the file a candidate would upload. Hidden lines are white (PDF) or…, _content(), _escape(), _fill(), Image, make_pdf(), plain_zip() (+18 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+6 more)

### Community 84 - "test_profile_redaction.py"
Cohesion: 0.32
Nodes (14): assert_redacted(), assert_traced_in_full(), generations(), inputs(), anyio, resume-aware-interview Step 5: a write whose prompt carries the profile is…, run_stream_write(), run_write() (+6 more)

### Community 85 - "pydantic"
Cohesion: 0.07
Nodes (40): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewListOut (+32 more)

### Community 86 - "RetryPolicy"
Cohesion: 0.03
Nodes (69): AsyncBaseTransport, T, BaseTransport, open_stream(), AsyncBaseTransport, BaseTransport, Attempted, _Call (+61 more)

### Community 87 - "LLMBadResponseError"
Cohesion: 0.06
Nodes (53): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, GoogleEmbedder (+45 more)

### Community 88 - "RateLimiter"
Cohesion: 0.06
Nodes (42): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, Per-user caps on paid speech calls. One limiter instance per process: every…, Limits, thresholds and messages of the résumé upload (resume-upload spec)., _out(), ProfileController, The signed-in user's résumé profile: request -> ProfileService, stored row ->… (+34 more)

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
Cohesion: 0.14
Nodes (26): candidate_profile_block(), profile_items(), profile_query_text(), The candidate profile as interview input: a fenced prompt block and a short…, The profile fenced as data, like the job description. Summaries and…, The profile's short items: skills and technologies first (closest to note…, The profile's short items as one retrieval query. None: nothing to embed., Project (+18 more)

### Community 93 - "test_retrieval_profile_cases.py"
Cohesion: 0.30
Nodes (11): case_set_problems(), _is_short_items(), _retrieval_cases(), case(), parametrize, Profile cases in the retrieval eval (resume-aware-interview Step 9c; seam S5).…, row(), test_a_profile_case_must_be_short_items() (+3 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "interviews_constants.py"
Cohesion: 0.04
Nodes (83): ContextReport, ContextTooLargeError, _log(), Exception, Context management: the one place that decides what each LLM call sends. The…, Even with every droppable entry gone the input is over the strategy's limit., LLMProvider, LLMResult (+75 more)

### Community 97 - "InterviewType"
Cohesion: 0.23
Nodes (21): NotEnoughQuestionsError, InterviewType, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), 4. How it works, _bank(), parametrize, _q() (+13 more)

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
Cohesion: 0.07
Nodes (32): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+24 more)

### Community 104 - "QuestionCategory"
Cohesion: 0.10
Nodes (40): _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_decision_reply(), parse_interviewer_reply(), parse_streamed_reply(), BaseModel (+32 more)

### Community 105 - "Role"
Cohesion: 0.18
Nodes (22): EmptyProfileError, Exception, No skills and no roles: not a résumé we can use (refused as unreadable, nothing…, Role, _appears(), ground_profile(), keep(), _normalized() (+14 more)

### Community 106 - "test_reaction_pick.py"
Cohesion: 0.11
Nodes (24): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), A predefined, neutral acknowledgement for the answer just given; never the same…, Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`) (+16 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "parse_log"
Cohesion: 0.08
Nodes (33): _json_event(), LogEvent, parse_log(), Reading the app's own log back: what each request did for an interview, from…, Old text lines: `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]).…, The requests that logged this session, oldest first: the start, then one…, Reads both log formats, so a log that rotated mid-change (`app.log.1` text,…, _split_fields() (+25 more)

### Community 109 - "ChatTrace"
Cohesion: 0.18
Nodes (9): _chat_messages(), ChatTrace, Any, BaseMessage, TraceLabels, One traced call: started by the first model run it sees, finished by the call…, LangChain messages in our own shape, so the trace reads like the old layer's…, BaseCallbackHandler (+1 more)

### Community 110 - "Implementation: U3a LangChain foundation + first chains"
Cohesion: 0.13
Nodes (14): 9 -> 10. Stop: user-run comparison evals, Completed Steps, Current Step, Debug Log, Implementation: U3a LangChain foundation + first chains, Known Issues, Links, Open Questions (+6 more)

### Community 111 - "test_follow_ups.py"
Cohesion: 0.23
Nodes (18): 5. What can go wrong, answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+10 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 114 - "load_prompt"
Cohesion: 0.09
Nodes (37): _interviewer(), The startup prompt check: every routed prompt version loads and renders through…, _routed(), load_prompt(), An interviews prompt by version (cached; the startup check reads every routed…, Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt() (+29 more)

### Community 115 - "Feature: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 116 - "tests/conftest.py"
Cohesion: 0.04
Nodes (58): ConflictError, health_check(), Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links (+50 more)

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
Cohesion: 0.15
Nodes (17): CurrentUserDep, _assert_401(), authenticated(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access(), test_guards_allow_or_forbid_by_db_role() (+9 more)

### Community 121 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "test_profile_read_resume.py"
Cohesion: 0.13
Nodes (40): make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), Exception, Why a file was refused; `reason` is short and machine-readable (logged, never…, read_resume(), ResumeRefusal, ResumeUnreadableRefusal (+32 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+5 more)

### Community 125 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+7 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.12
Nodes (19): injection_ignored(), 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+11 more)

### Community 127 - "Feature: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Decisions, Edge Cases, Feature: Résumé-aware interview (Slice 8d), Functional, Goal, Known limits (+7 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "interviews_model.py"
Cohesion: 0.10
Nodes (35): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, InterviewSessionChunk (+27 more)

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

### Community 140 - "ReferenceNote"
Cohesion: 0.27
Nodes (16): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, A note an interview was given: what the question writer sees (competency and…, ReferenceNote, names(), ranked(), merge_note_rankings: the quota merge of the job-description and profile…, Notes named by single letters, ranked in the given order with falling scores. (+8 more)

### Community 142 - "follow_up"
Cohesion: 0.18
Nodes (12): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split), follow_up() (+4 more)

### Community 143 - "QuestionTurn"
Cohesion: 0.09
Nodes (40): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the… (+32 more)

### Community 144 - "CandidateProfile"
Cohesion: 0.12
Nodes (29): Output, CandidateProfile, ExpectedProfile, _key(), ProfileScore, BaseModel, NamedTuple, Scoring an extracted profile against a hand-labelled synthetic résumé (resume-… (+21 more)

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

### Community 151 - "interviews_start_dependencies.py"
Cohesion: 0.11
Nodes (40): get_llm_provider(), Built once at startup (app lifespan); None when no key is configured or the…, get_db(), Session, get_answer_controller(), get_answer_service(), Depends, Session (+32 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.13
Nodes (27): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+19 more)

### Community 156 - "json"
Cohesion: 0.11
Nodes (23): load_bank(), Path, Read and validate a question bank file; a bad file fails loudly instead of at…, 5. What can go wrong, Test Results, Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend) (+15 more)

### Community 157 - "Implementation: Interview Room (backend)"
Cohesion: 0.12
Nodes (15): Changes Made, Current Step, Debug Log, Deviations from Plan, Done. Next: `/review-feature`, Implementation: Interview Room (backend), Known Issues, Links (+7 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (14): 9. Review gate (user), Baseline Failures, Changes Made, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions (+6 more)

### Community 159 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 160 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 161 - "Implementation Steps"
Cohesion: 0.04
Nodes (56): AbstractContextManager, Generation, Any, TraceLabels, The stream was closed before it finished (client left, or the turn's deadline…, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a… (+48 more)

### Community 162 - "InterviewMessage"
Cohesion: 0.14
Nodes (24): MessageKind, MessageRole, Transcript item kinds: a question comes from interview_questions, the other two…, InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut, build_transcript() (+16 more)

### Community 163 - "Implementation: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gate: Step 10, real-model runs (yours), Implementation: Résumé-aware interview (Slice 8d), Known Issues (+8 more)

### Community 164 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open, Eval log (+1 more)

### Community 165 - "interviews_context.py"
Cohesion: 0.06
Nodes (45): BuiltContext, NamedTuple, StrategyOutput, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:… (+37 more)

### Community 166 - "test_feedback_context.py"
Cohesion: 0.19
Nodes (21): FeedbackScore, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, The score call: every thread whole, nothing droppable. Over its own limit it…, Step 4 of the feedback plan: what the score and write calls send, through the… (+13 more)

### Community 167 - "Implementation Steps"
Cohesion: 0.09
Nodes (21): Affected Files & Patterns, Blockers & Resolutions, Deviations Found During Implementation, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps, Overview, Phase A: plumbing and progress events, Phase B: streaming the question text (+13 more)

### Community 168 - "interviews_utils.py"
Cohesion: 0.10
Nodes (27): model_validator, Self, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, interview_categories(), load_rubric(), pick_fallback_question(), Collection (+19 more)

### Community 169 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 170 - "summarize_job_description"
Cohesion: 0.17
Nodes (19): ChatModel, NamedTuple, What one summary call gave: the usable summary (None when it can't replace the…, One summary call; see `SummaryOutcome`. A reply that `validate_summary` rejects…, summarize_job_description(), SummaryOutcome, llm_lines(), no_retry_waits() (+11 more)

### Community 171 - "test_request_context.py"
Cohesion: 0.12
Nodes (8): asyncio, fastapi_responses, anyio_backend(), fixture, parametrize, test_a_log_line_after_the_request_is_outside_it(), test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.10
Nodes (23): Baseline Failures, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL), 1. Why it exists (+15 more)

### Community 174 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "interviews_shared_dependencies.py"
Cohesion: 0.16
Nodes (17): get_chat_model(), get_synthesizer(), get_tracer(), get_transcriber(), ChatModel, Request, Request dependencies for the AI services every feature shares, built once at…, The LangChain chat model, built once at startup; None when LLM is off or the… (+9 more)

### Community 178 - "JobRole"
Cohesion: 0.10
Nodes (26): JobRole, Level, EvalSetup, FeedbackEvalSetup, ExtraSetup, ExtraSetupFields, BaseModel, A generation-only setup, run with arm D or E: the injection and the mismatch… (+18 more)

### Community 179 - "Slices in detail"
Cohesion: 0.14
Nodes (13): AI Engineering Upgrade Path (Cuewise), Build order, How to make it stick, Progress, Slices in detail, U0: Baselines, U1: structlog, U4: Prompt templates + Langfuse Prompt Management (+5 more)

### Community 180 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.17
Nodes (11): Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Goal, Out of Scope, Problem (+3 more)

### Community 181 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 182 - "test_start_with_profile.py"
Cohesion: 0.21
Nodes (18): 5. What can go wrong, embedder(), first_question(), profile_of(), fixture, Starting an interview with the candidate's profile (resume-aware-interview Step…, A synthetic profile whose every free-text field carries `marker`, so a leak…, sent() (+10 more)

### Community 183 - "interviews_schema.py"
Cohesion: 0.09
Nodes (39): current_request_id(), The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), AnswerController, _error_event(), _event(), _frame() (+31 more)

### Community 184 - "test_streamed_reply.py"
Cohesion: 0.18
Nodes (17): interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), read(), parse(), parametrize, interviewer_v5's streamed reply: a `CATEGORY:` header line (next-question mode…, test_a_header_split_across_chunks_is_read_once_its_line_ends(), test_a_long_first_line_is_no_header_without_waiting_for_its_end() (+9 more)

### Community 185 - "_Tts"
Cohesion: 0.33
Nodes (3): The text-to-speech seam of a test: a scripted synthesizer and a fresh per-test…, No synthesizer configured (DEEPGRAM_API_KEY blank)., _Tts

### Community 186 - "pytest"
Cohesion: 0.11
Nodes (19): load_prompt(), Path, Prompt files: versioned Markdown read once per process. Feature modules pass…, `<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in…, functools, pytest, The shared prompt loader (prompt-registry AC9, EC13): one cached read per…, test_a_second_call_does_not_read_the_file_again() (+11 more)

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
Nodes (62): ErrorResponse, Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Notes (added during /implement) (+54 more)

### Community 203 - "main"
Cohesion: 0.16
Nodes (18): html_target(), main(), Path, Session, UUID, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines() (+10 more)

### Community 207 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.16
Nodes (23): corpus(), embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, Ingests the three notes; returns the vector each note text gets (the embedder… (+15 more)

### Community 220 - "LLMServerError"
Cohesion: 0.06
Nodes (72): _from_status(), _google_error(), _mapped(), BaseException, Map what the LangChain/Gemini call layer raises to our LLMError types (spec…, The LLMError for `exc`, with `exc` as its cause. Messages are fixed text: a…, Seconds from the error's `google.rpc.RetryInfo` detail (Google's Retry-After);…, _retry_after() (+64 more)

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

### Community 234 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

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
Cohesion: 0.12
Nodes (15): 15. Evals, fault check and graph, Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U2 — One tenacity retry policy for the AI call layer, Known Issues, Links (+7 more)

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
Nodes (63): alias, AnswerControllerDep, ForbiddenError, Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role (+55 more)

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

### Community 252 - "check_prompts"
Cohesion: 0.21
Nodes (16): check_prompts(), PromptCheckError, Exception, One or more routed prompts cannot be sent; the message lists each one., Raises PromptCheckError naming every routed version whose file is missing or…, 4. How it works, loader(), load() (+8 more)

### Community 253 - "test_tracing_lifespan.py"
Cohesion: 0.20
Nodes (7): fastapi_testclient, The app lifespan runs the prompt check before anything else (prompt-registry…, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 255 - "Feature: U1 structlog (structured JSON logs)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: U1 structlog (structured JSON logs), Functional, Goal, Non-Functional (+6 more)

### Community 256 - "Feature: Job URL (Slice 8b)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Job URL (Slice 8b), Functional, Goal, Non-Functional (+6 more)

### Community 257 - "test_generation_eval.py"
Cohesion: 0.16
Nodes (30): arm_of(), fill(), generated(), posted(), parametrize, quiet(), `run_generation` as Langfuse experiment runs (langfuse-experiments Step 11;…, The console with each arm row's start_ms (wall-clock time) dropped, and without… (+22 more)

### Community 258 - "limit_feedback"
Cohesion: 0.12
Nodes (16): get_feedback_limiter(), limit_feedback(), Depends, interviews_feedback, Tests swap in a fresh limiter so counts never leak between them., Per-user cap on feedback requests, checked before anything that can cost an LLM…, Affected Files & Patterns, Architecture & Design (+8 more)

### Community 259 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 260 - "Implementation: Prompt Registry"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Known Issues (+8 more)

### Community 261 - "interviews_feedback_controller.py"
Cohesion: 0.21
Nodes (12): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, get_feedback_controller(), FeedbackEvidenceOut (+4 more)

### Community 262 - "FakeLangfuse"
Cohesion: 0.09
Nodes (15): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+7 more)

### Community 263 - "bind_log_context"
Cohesion: 0.14
Nodes (25): bind_log_context(), Adds fields to every later log line of the current request (or, outside a…, log_retrieval(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, Which reference notes an interview got at start: mode, count, scores, how many…, render_text(), Implementation Steps (+17 more)

### Community 264 - "test_answer_with_profile.py"
Cohesion: 0.25
Nodes (12): opted_in(), profile_of(), fixture, question_at(), Answer turns of an interview that uses the candidate's profile (resume-aware-…, A user with profile ZZOLD and an interview started with use_profile; returns…, sent(), test_a_follow_up_turn_and_its_decide_call_never_carry_the_profile() (+4 more)

### Community 265 - "chat_fake.py"
Cohesion: 0.17
Nodes (10): A LangChain chat model for tests (spec FR6): scripted replies or errors, every…, Langfuse tracing for the LangChain call layer, through our own `Tracer` (U3a,…, collections, langchain_core_callbacks, langchain_core_language_models, langchain_core_messages, langchain_core_output_parsers, langchain_core_outputs (+2 more)

### Community 266 - "Web"
Cohesion: 0.17
Nodes (7): get_page_fetcher(), Tests swap in a fetcher with a fake resolver and transport: no network., fixture, Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 267 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Changes Made, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 268 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 269 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 270 - "test_fallback_pick.py"
Cohesion: 0.27
Nodes (11): fixture_bank(), pick(), fixture, parametrize, test_general_and_role_specific_questions_are_both_eligible(), test_level_must_match(), test_mixed_alternates_starting_with_behavioral(), test_nothing_left_raises() (+3 more)

### Community 271 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 272 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 273 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 274 - "Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 275 - "Implementation Plan: Agentic Workflow v2"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: Agentic Workflow v2, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 276 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.18
Nodes (10): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slices (+2 more)

### Community 277 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 8. Check your understanding, 9. Still open, Learn: Splitting the interviews dependency wiring

### Community 290 - "test_stream_answer.py"
Cohesion: 0.07
Nodes (43): Save one whole turn in one commit: advance the session, the answer, the…, AnswerOut, done(), Deviations from Plan, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong (+35 more)

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "check_layers"
Cohesion: 0.12
Nodes (15): Blockers & Resolutions, Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+7 more)

### Community 293 - "interviews_knowledge_ingest.py"
Cohesion: 0.22
Nodes (15): main(), _parser(), ArgumentParser, Session, Ingest the reference notes into the database (knowledge-base RAG). uv run…, sys, ingest(), Path (+7 more)

### Community 294 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.22
Nodes (8): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Trade-offs & Rationale

### Community 295 - "FakeClient"
Cohesion: 0.08
Nodes (13): client(), FakeClient, FakeObservation, propagated(), fixture, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_reports_whether_it_was_sent() (+5 more)

### Community 296 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "profile_extract_v1.md"
Cohesion: 0.40
Nodes (4): Constraints, Input, Role, Task

### Community 299 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 301 - "test_factory.py"
Cohesion: 0.05
Nodes (68): build_chat_model(), build_embedder(), build_provider(), build_synthesizer(), build_transcriber(), _google_chat_model(), ChatModel, Embeddings for reference-note retrieval; None without the Google key (notes are… (+60 more)

### Community 302 - "Slices in detail"
Cohesion: 0.18
Nodes (11): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 6: Feedback and scoring, Slice 7: Eval maturity (trust the judge, catch regressions) (+3 more)

### Community 303 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 304 - "Implementation Plan: U1 structlog (structured JSON logs)"
Cohesion: 0.18
Nodes (10): Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: U1 structlog (structured JSON logs), Overview, Project Rules Applied, Ready to Implement, Spec Requirements -> Implementation (+2 more)

### Community 305 - "InterviewQuestion"
Cohesion: 0.05
Nodes (42): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter(), InterviewsRepository, Any, datetime, Session (+34 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 308 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 309 - "check_core"
Cohesion: 0.25
Nodes (8): Skills Consulted During Implementation, check_core(), _imports(), Every `app/core` import of a feature module (`app.modules...`): core is shared…, (absolute module, imported names) per import statement; relative imports…, test_a_core_file_importing_a_feature_module_is_reported(), test_a_core_file_importing_only_core_and_libraries_is_clean(), test_the_real_core_imports_no_feature_module()

### Community 310 - "interviews_prompt_registry.py"
Cohesion: 0.33
Nodes (9): PromptVersion, StrEnum, Every interviews prompt version, and which one each LLM call sends. Data only:…, Status, archived_routes(), incomplete_entries(), test_a_route_to_an_archived_or_unknown_version_is_named(), test_an_entry_with_no_reason_or_a_wrong_name_is_named() (+1 more)

### Community 311 - "test_log_context.py"
Cohesion: 0.29
Nodes (9): fixture, Log context on real interview requests (U1 structlog, AC4): `session` and…, Every line of the one request whose access line ends with `path_end`., _request_lines(), started(), test_a_request_for_someone_elses_interview_logs_the_id_it_asked_for(), test_a_start_request_logs_the_new_session_and_the_user_on_every_line(), test_a_streamed_turn_logs_its_session_and_user_from_inside_the_stream() (+1 more)

### Community 312 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 313 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 314 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 315 - "interviews_feedback_service.py"
Cohesion: 0.12
Nodes (28): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, CallUsage, log_feedback_summary() (+20 more)

### Community 316 - "U0 baselines"
Cohesion: 0.25
Nodes (7): Before relying on this, Cost, Eval baselines, How to use this file, Live interviews (from `logs/app.log`, before U1), Prompts with no eval baseline (gaps), U0 baselines

### Community 317 - "clock"
Cohesion: 0.20
Nodes (6): Known Issues, Project Conventions, _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 318 - "test_eval_runs.py"
Cohesion: 0.06
Nodes (39): _evaluation(), Any, Score, Run every case once, in order, as one Langfuse experiment run; whatever the run…, run_cases(), item_scores(), C, contextvars (+31 more)

### Community 319 - "Feature: U3a LangChain foundation + first chains"
Cohesion: 0.20
Nodes (9): Blockers, Constraints, Feature: U3a LangChain foundation + first chains, Goal, Non-Functional, Out of Scope, Requirements, User Flow (+1 more)

### Community 320 - "test_chat_tracing.py"
Cohesion: 0.42
Nodes (9): The LangChain tracing callback (spec FR5, AC8, EC14, EC15): one Langfuse…, result(), test_a_call_records_one_generation_with_its_messages_labels_and_usage(), test_a_disabled_tracer_records_nothing(), test_a_failed_call_records_an_error_with_the_error_class(), test_a_langfuse_failure_never_fails_the_call(), test_a_redacted_call_records_the_placeholder_for_input_and_output(), test_retried_attempts_are_still_one_generation_with_the_attempt_count() (+1 more)

### Community 321 - "test_profile_extract.py"
Cohesion: 0.12
Nodes (23): Carries the app's Tracer on a chat model (`build_chat_model(..., tracer=)`…, TracerHandle, ExtractionFailedError, Exception, No valid profile: `reason` is invalid_reply, empty_reply, no_time or the…, extract(), no_retry_waits(), fixture (+15 more)

### Community 322 - "Learn: Adding interview roles (designer, qa, devops)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open, Learn: Adding interview roles (designer, qa, devops)

### Community 323 - "Learn: Prompt registry (one place for prompt versions and routing)"
Cohesion: 0.22
Nodes (8): 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Eval log (AI features only), Learn: Prompt registry (one place for prompt versions and routing)

### Community 324 - "test_profile_evals.py"
Cohesion: 0.28
Nodes (6): LabelledModel, Any, The profile eval runner offline: every synthetic case builds into a readable…, Answers each case with its own label, so the scores test the pipeline and the…, test_a_model_that_answers_the_labels_scores_one_everywhere(), test_the_hidden_injection_is_dropped_before_the_model()

### Community 325 - "_Stt"
Cohesion: 0.25
Nodes (5): get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them., The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank)., _Stt

### Community 326 - "traces"
Cohesion: 0.25
Nodes (4): Tips, fixture, RecordingClient, traces()

### Community 327 - "RecordingClient"
Cohesion: 0.22
Nodes (3): Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, recording(), RecordingClient

### Community 328 - "SafeFetcher"
Cohesion: 0.07
Nodes (29): _decode(), FetchedPage, FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach… (+21 more)

### Community 329 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 330 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.29
Nodes (6): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository)

### Community 331 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 332 - "ProfileService"
Cohesion: 0.33
Nodes (3): ProfileService, UUID, The user's stored profile for an interview prompt, read live (never copied onto…

### Community 333 - "U2 (tenacity) vs. the U0 baseline"
Cohesion: 0.33
Nodes (5): An extra set of runs (not used for the verdict), Failures, Scores, Still to do, U2 (tenacity) vs. the U0 baseline

### Community 335 - "Langfuse CLI Reference"
Cohesion: 0.40
Nodes (5): Credentials, Discovery, Install, Langfuse CLI Reference, Tips

### Community 336 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 337 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 338 - "test_user_ids.py"
Cohesion: 0.70
Nodes (4): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7()

## Knowledge Gaps
- **1099 isolated node(s):** `cuewise-be`, `What it does`, `How to invoke`, `Example output`, `See also` (+1094 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2675 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **59 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LLMError` connect `LLMServerError` to `Cuewise BE — Project Instructions`, `Completed Steps`, `chat_fake.py`, `test_deepgram.py`, `test_knowledge_ingest.py`, `interviews_answer_service.py`, `test_rag_evals.py`, `Implementation Steps`, `FakeChatModel`, `interviews_rag_evals.py`, `typing`, `interviews_context.py`, `Implementation Steps`, `summarize_job_description`, `test_chat_contract.py`, `test_factory.py`, `test_evals.py`, `InterviewerInputs`, `interviews_feedback_service.py`, `clock`, `Feature: U3a LangChain foundation + first chains`, `errors.py`, `FakeEmbedder`, `test_stream_turn.py`, `openai_compatible.py`, `profile_extract.py`, `fake.py`, `run_stream_case`, `RetryPolicy`, `LLMBadResponseError`, `interviews_constants.py`, `test_speech.py`, `QuestionCategory`, `ChatTrace`, `Feature: Langfuse Tracing`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `interviews_model.py`, `limit_feedback`, `interviews_feedback_controller.py`, `Implementation Plan: UUID primary keys`, `interviews_start_dependencies.py`, `interviews_answer_service.py`, `typing`, `interviews_service.py`, `interviews_job_url_service.py`, `InterviewQuestion`, `test_create_interview.py`, `interviews_schema.py`, `interviews_feedback_service.py`, `errors.py`, `test_knowledge_postgres.py`, `ProfileService`, `pydantic`, `RateLimiter`, `Implementation: Langfuse Tracing`, `interviews_route.py`, `tests/conftest.py`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `test_generation_eval.py`, `User`, `FakeLangfuse`, `Completed Steps`, `chat_fake.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `test_feedback_evals.py`, `interviews_start_dependencies.py`, `interviews_answer_service.py`, `test_feedback_endpoint.py`, `test_tracing.py`, `Implementation Steps`, `FakeChatModel`, `interviews_rag_evals.py`, `interviews_context.py`, `interviews_service.py`, `FakeClient`, `summarize_job_description`, `test_factory.py`, `test_evals.py`, `interviews_shared_dependencies.py`, `Feature: Langfuse experiments for the interviews evals`, `test_openai_compatible_stream.py`, `experiments`, `interviews_feedback_service.py`, `logging.py`, `test_eval_runs.py`, `test_chat_tracing.py`, `test_profile_extract.py`, `test_profile_routes.py`, `test_profile_evals.py`, `traces`, `RecordingClient`, `run_stream_case`, `test_retrieval_eval.py`, `test_profile_redaction.py`, `RetryPolicy`, `LLMServerError`, `interviews_constants.py`, `ChatTrace`, `test_tracing_lifespan.py`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Tracer` (e.g. with `ChatTrace` and `TracerHandle`) actually correct?**
  _`Tracer` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 51 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 56 inferred relationships involving `LLMResult` (e.g. with `complete_chat()` and `_run()`) actually correct?**
  _`LLMResult` has 56 INFERRED edges - model-reasoned connections that need verification._
- **Are the 33 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 33 INFERRED edges - model-reasoned connections that need verification._