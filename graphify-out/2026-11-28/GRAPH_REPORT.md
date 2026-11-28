# Graph Report - cuewise-be  (2026-11-28)

## Corpus Check
- 537 files · ~505,996 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 9 file(s) not represented in the graph (top: (none) 4, .example 1, .ini 1)

## Summary
- 7486 nodes · 21163 edges · 356 communities (298 shown, 58 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 4145 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3b801c71`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_langchain_behaviour.py
- test_retry.py
- test_profile_eval_metrics.py
- main.py
- test_interview_report.py
- User
- _LostClaim
- test_job_url_utils.py
- StrategyOutput
- test_summary_evals.py
- profile_route.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- TracerHandle
- test_feedback_evals.py
- test_safe_fetch.py
- test_knowledge_ingest.py
- Implementation: Prompt Registry
- cuewise-be
- test_feedback_contract.py
- score
- test_feedback_endpoint.py
- test_context_strategies.py
- LLMResult
- interviews_rag_evals.py
- ChatTrace
- Feature: Context Management for the Interview LLM Calls
- FakeChatModel
- test_answer_stream.py
- run_generation
- _Tts
- profile_evals.py
- interviews_knowledge_utils.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- test_chat_contract.py
- get_interviews_service
- test_chat_stream.py
- test_transcribe.py
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- read_resume
- AppError
- test_request_context.py
- test_profile_read_resume.py
- app_logs
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- Feature: Résumé-aware interview (Slice 8d)
- interviews_report.py
- test_rag_evals.py
- decode_token
- test_tracing_routes.py
- 4. How it works
- Rules
- job_description_summary_v2.md
- test_evals.py
- FakeEmbedder
- Implementation Steps
- test_profile_routes.py
- setup_logging
- .acall
- interviews_job_url_utils.py
- noted
- exception_handlers.py
- test_guards.py
- test_gateway.py
- Implementation: Résumé upload and candidate profile (Slice 8c)
- Project
- scrub_contacts
- Langfuse
- interviews_report_render.py
- CaseResult
- Web
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- stream_chat
- FakeProvider
- RetryPolicy
- EmbeddingKind
- InterviewQuestion
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- interviews_constants.py
- LLMServerError
- Langfuse Observability
- interviewer_v3.md
- CandidateProfile
- Implementation Plan: Interview Room (backend)
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_speech.py
- InterviewMessage
- test_retry_budget.py
- test_stream_turn.py
- Langfuse Dataset Construction
- parse_log
- Feature: Résumé upload and candidate profile (Slice 8c)
- interviews_retrieve.py
- Completed Steps
- Feature: Langfuse Tracing
- Langfuse
- Learn: Résumé-aware interview (Slice 8d)
- ReferenceNote
- test_decide.py
- The fundamentals
- Langfuse Implementation Notes
- interviewer_v5.md
- PageParams
- test_write.py
- Feature: Agentic Workflow v2 (debug, review-feature, gated loop)
- ._next
- How to evaluate an AI feature: from the command to the fix
- parse_profile_reply
- test_profile_context.py
- summarize_job_description
- Langfuse Dataset Construction
- Langfuse v4 project migration
- test_chat_stream_live.py
- Implementation: Interview History List (backend)
- Judge Calibration
- profile_resume_utils.py
- build_usage_report
- Blind ranking
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- done
- bind_log_context
- check_prompts
- test_reference_note_context.py
- Langfuse v4 project migration
- Judge Calibration
- test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only
- Langfuse CI/CD
- Prompt Engineering
- test_reply_contract.py
- Implementation: U3c — Fallback chain, question bank removal, old LLM layer deleted
- Implementation: Agentic Workflow v2
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- interviews_evals.py
- Implementation: Interview Room (backend)
- Implementation: Interview Feedback and Scoring (Slice 6)
- QuestionTurn
- profile_reply.py
- Tracer
- interviews_knowledge_ingest.py
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_start_with_profile.py
- Implementation Plan: Follow-up Questions (decide / write split)
- Implementation: LLM as the Interviewer (it asks the questions)
- provider.py
- test_prompt_registry.py
- ChatMessage
- failed
- U3b1 stage 2 (decide on LangChain, structured output) vs. the baseline
- feedback_score_v2.md
- pytest
- Implementation: U1 structlog (structured JSON logs)
- feedback_score_v1.md
- feedback_write_v1.md
- ErrorResponse
- get_logger
- Implementation: Langfuse experiments for the interviews evals
- StreamedTurn
- Feature: Interview History List (backend)
- profile_extract.py
- test_answer_guards.py
- Implementation Plan: Start an Interview (backend)
- hint_for
- test_answer_with_profile.py
- interviewer_v8.md
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviewer_v8_json.md
- users_utils.py
- interviews_model.py
- LoggedLine
- Implementation: Résumé-aware interview (Slice 8d)
- test_retrieval_eval.py
- RateLimiter
- LLMError
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
- case
- Communication and priorities
- Engineering habits
- Senior judgement
- Implementation: U3a LangChain foundation + first chains
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- interviews_schema.py
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- Cuewise BE — Project Instructions
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- _DeepgramAdapter
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- Feature: U3c — Fallback chain, question bank removal, old LLM layer deleted
- test_tracing_lifespan.py
- Feature: U1 structlog (structured JSON logs)
- Feature: Job URL (Slice 8b)
- KnowledgeRepository
- Role
- WithInterviewData
- test_answer_llm.py
- Role
- Implementation Plan: Langfuse Tracing
- clock
- FeedbackCaseResult
- Implementation Plan: Résumé-aware interview (Slice 8d)
- interviews_route.py
- Implementation Plan: UUID primary keys
- profile_resume_files.py
- interviews_voice_dependencies.py
- Learn: Splitting the interviews dependency wiring
- run_name
- Implementation: Start an Interview (backend)
- Implementation: Follow-up Questions (decide / write split)
- Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)
- Implementation Plan: Agentic Workflow v2
- test_transcript.py
- _Stt
- Langfuse Observability
- Implementation: U3b1 Interview calls on LangChain
- test_reaction_pick.py
- get_chat_model
- Implementation: Error Handling
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Prompt Migration
- main
- Learn: a provider fallback chain (U3c, built; real-model runs pending)
- Langfuse Prompt Migration
- LogCapture
- test_context_controller.py
- test_get_interview.py
- Embedder
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation Steps
- interview-room/README.md
- types.py
- Implementation Plan: Context Management for the Interview LLM Calls
- test_answer_interview.py
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Learn: one retry policy on tenacity, and why reply retries stay out of it (U2)
- Implementation Plan: U3b1 Interview calls on LangChain
- test_job_description_summary.py
- Learn: Prompt registry (one place for prompt versions and routing)
- test_tracing.py
- Implementation Plan: U3c — Fallback chain, question bank removal, old LLM layer deleted
- test_eval_runs.py
- synthesize
- Status
- Feature: U3b1 Interview calls on LangChain
- _RoutedChatModel
- Feature: LLM as the Interviewer (it asks the questions)
- get_current_user
- _StderrHandler
- Settings
- RecordingClient
- llm
- load_feedback_cases
- interviews/conftest.py
- ._ordered
- feedback_dataset_items
- U0 baselines
- test_speech_contracts.py
- Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)
- ProviderChatModel
- Slices in detail
- GoogleEmbedder
- Learn: Résumé upload and the candidate profile (Slice 8c)
- safe_fetch.py
- test_log_context.py
- profile_service.py
- lf
- .__init__
- .insert_feedback
- fixture
- ._covers_every_criterion

## God Nodes (most connected - your core abstractions)
1. `FakeChatModel` - 165 edges
2. `Tracer` - 153 edges
3. `LLMError` - 141 edges
4. `FakeProvider` - 136 edges
5. `User` - 131 edges
6. `LLMResult` - 125 edges
7. `JobRole` - 111 edges
8. `LLMServerError` - 105 edges
9. `InterviewQuestion` - 98 edges
10. `Level` - 96 edges

## Surprising Connections (you probably didn't know these)
- `2. What it is` --references--> `ChatChain`  [INFERRED]
  docs/features/u3c-fallback-chain/learnings.md → app/core/ai/chat_chain.py
- `Completed Steps` --references--> `to_llm_error()`  [INFERRED]
  docs/features/u3a-langchain-foundation/task.md → app/core/ai/chat_errors.py
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `1. Why it exists` --references--> `DeepgramTranscriber`  [INFERRED]
  docs/features/interview-room/learnings.md → app/core/ai/deepgram.py

## Import Cycles
- None detected.

## Communities (356 total, 58 thin omitted)

### Community 0 - "test_langchain_behaviour.py"
Cohesion: 0.09
Nodes (42): ChatGoogleGenerativeAI, Spike results (step 1, `tests/core/ai/test_langchain_behaviour.py`), GenerateContentResponse, google_ai_generativelanguage_v1beta_types, langchain_google_genai, MonkeyPatch, _Flaky, _gemini() (+34 more)

### Community 1 - "test_retry.py"
Cohesion: 0.13
Nodes (42): anyio_lowlevel, 5. What can go wrong, anyio_backend(), Clock, fields(), make_policy(), anyio, fixture (+34 more)

### Community 2 - "test_profile_eval_metrics.py"
Cohesion: 0.09
Nodes (48): ArmProfileSummary, coverage_spread(), guard_verdict(), GuardStatus, GuardVerdict, _injection_share(), _mention_share(), notes_overlap() (+40 more)

### Community 3 - "main.py"
Cohesion: 0.12
Nodes (29): DeepgramSynthesizer, DeepgramTranscriber, Any, Aura text-to-speech: the text goes in a JSON body, the voice (`model`) and…, build_embedder(), build_synthesizer(), build_transcriber(), Speech-to-text for voice answers; None without a key. Never traced: audio and… (+21 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.10
Nodes (66): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a…, analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http() (+58 more)

### Community 5 - "User"
Cohesion: 0.08
Nodes (35): hash_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), get_service(), Depends, Session, User (+27 more)

### Community 6 - "_LostClaim"
Cohesion: 0.67
Nodes (3): _LostClaim, Exception, Another request took the row over while this one ran: this one's writes are…

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.11
Nodes (41): extract_job_text(), job_term_hits(), looks_like_job_posting(), pasted_job_text(), The posting as plain text, or None when the page has too little text to be one…, A page the candidate copied from their own browser (for sites that block our…, How many different job-ad terms the text contains; repeats count once., At most `limit` characters, cut at the last whitespace so no word is split;… (+33 more)

### Community 8 - "StrategyOutput"
Cohesion: 0.07
Nodes (26): StrategyOutput, _counts(), FeedbackScore, FeedbackWrite, FollowUpDecision, An earlier question as the model would have written it. A follow-up was written…, The decide call: the current thread in full (it judges the latest answer within…, App data at the end of the last user message; untrusted parts (questions,… (+18 more)

### Community 9 - "test_summary_evals.py"
Cohesion: 0.08
Nodes (49): Check, check_summary(), _dataset_items(), _has_fact(), load_summary_cases(), _print_case(), _print_summary(), Any (+41 more)

### Community 10 - "profile_route.py"
Cohesion: 0.13
Nodes (19): limit_resume_uploads(), ProfileUser, Checked before the body is read: every upload is a parse and a model call., delete_profile(), get_profile(), post, ProfileUser, A PDF or Word résumé (multipart part `file`, up to 2 MB and 5 pages) becomes… (+11 more)

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
Cohesion: 0.11
Nodes (34): _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_an_empty_or_blank_provider_list_refuses_to_start(), test_api_key_never_shows_in_repr_or_errors() (+26 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.10
Nodes (40): Review, anyio_backend(), audio(), Clock, listen_body(), make_synthesizer(), make_transcriber(), ok() (+32 more)

### Community 16 - "TracerHandle"
Cohesion: 0.13
Nodes (21): Carries the app's Tracer on a chat model (`build_chat_model(..., tracer=)`…, TracerHandle, BaseCallbackHandler, extract(), no_retry_waits(), fixture, parametrize, `extract_profile` on the LangChain layer: structured output inside the existing… (+13 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.16
Nodes (20): Grader, main(), Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The…, A fake provider: scores every criterion `value`, quoting the start of each…, _result(), run_main(), scores_on(), test_a_langfuse_outage_does_not_change_the_run() (+12 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.11
Nodes (47): FetchedPage, Response, One hop: a page, or the redirect's Location to check next., Refused before connecting, or the network side failed (DNS, timeout,…, The server answered, but not with an HTML page we are willing to read., ResponseUnreadableError, UrlUnreachableError, Client (+39 more)

### Community 19 - "test_knowledge_ingest.py"
Cohesion: 0.14
Nodes (33): log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, _embed(), ingest_corpus(), IngestCounts, IngestError, Exception, NamedTuple (+25 more)

### Community 20 - "Implementation: Prompt Registry"
Cohesion: 0.13
Nodes (14): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Implementation: Prompt Registry, Links (+6 more)

### Community 26 - "test_feedback_contract.py"
Cohesion: 0.17
Nodes (34): assess_evidence(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize, question_json(), The feedback contract (interviews_feedback.py): the code pre-check, the score… (+26 more)

### Community 27 - "score"
Cohesion: 0.23
Nodes (13): Uses up the budget on its first call, so a retry would start with less than…, score(), score_json(), SlowFirstCall, test_a_cut_off_reply_is_truncated_even_if_it_parses(), test_a_reply_that_breaks_the_schema_is_retried(), test_a_schema_valid_reply_with_a_made_up_quote_is_rejected_by_the_parser(), test_a_transport_error_is_retried_by_the_call_layer_then_fails() (+5 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.13
Nodes (53): InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, 5. What can go wrong, 8. Check your understanding, happy(), interview(), post(), parametrize (+45 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.16
Nodes (38): 5. What can go wrong, decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+30 more)

### Community 30 - "LLMResult"
Cohesion: 0.03
Nodes (150): fixed_prompt(), A prompt of already-built messages (our context manager's output), sent exactly…, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., LLMResult, InterviewerInputs, The labels of one write call. A write whose prompt carries the candidate… (+142 more)

### Community 31 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (71): Local time, as the Langfuse list shows the run's start: the name and the…, run_stamp(), _arm_notes(), ArmInterview, ArmSummary, case_set_problems(), ExtraSetup, filter_baseline() (+63 more)

### Community 32 - "ChatTrace"
Cohesion: 0.07
Nodes (26): _chat_messages(), ChatTrace, Any, BaseMessage, TraceLabels, One traced call: started by the first model run it sees, finished by the call…, A stream closed before it finished (client left, or the turn's deadline ran…, LangChain messages in our own shape, so the trace reads as role + text. (+18 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "FakeChatModel"
Cohesion: 0.08
Nodes (61): fake_reply(), FakeChatModel, BaseChatModel, An AIMessage shaped like Gemini's: usage in `usage_metadata` (None = the vendor…, Pops one scripted reply per call: text (wrapped by `fake_reply`), a ready…, NamedTuple, A structured call's outcome: the parsed object, or None with `error` saying why…, Structured (+53 more)

### Community 35 - "test_answer_stream.py"
Cohesion: 0.06
Nodes (29): 6. Try it yourself, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing(), test_the_first_event_is_sent_before_any_llm_call_returns(), test_the_stream_summary_is_metadata_only() (+21 more)

### Community 36 - "run_generation"
Cohesion: 0.06
Nodes (64): Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, _action_and_gap(), dataset_items(), dataset_name(), decide_run_scores(), DecisionSummary, experiment_scores_for(), interviewer_prompt_version() (+56 more)

### Community 37 - "_Tts"
Cohesion: 0.25
Nodes (5): get_speech_limiter(), Tests swap in a fresh limiter so counts never leak between them., The text-to-speech seam of a test: a scripted synthesizer and a fresh per-test…, No synthesizer configured (DEEPGRAM_API_KEY blank)., _Tts

### Community 38 - "profile_evals.py"
Cohesion: 0.06
Nodes (44): build_tracer(), ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, final_line(), pacer(), wait() (+36 more)

### Community 39 - "interviews_knowledge_utils.py"
Cohesion: 0.06
Nodes (56): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+48 more)

### Community 40 - "test_layers.py"
Cohesion: 0.05
Nodes (59): Skills Consulted During Implementation, 5. What can go wrong, Blockers & Resolutions, Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement (+51 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues, Links (+7 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "test_chat_contract.py"
Cohesion: 0.10
Nodes (32): Build, langchain_core_prompts, StreamOutcome, _collect(), _fake(), _fake_stream(), _gemini(), _gemini_stream() (+24 more)

### Community 44 - "get_interviews_service"
Cohesion: 0.08
Nodes (42): get_tracer(), Built once at startup (app lifespan); a disabled tracer when the lifespan…, get_answer_controller(), get_answer_service(), ChatModel, Depends, Session, get_feedback_limiter() (+34 more)

### Community 45 - "test_chat_stream.py"
Cohesion: 0.10
Nodes (37): fake_chunks(), BaseException, A streamed reply: one chunk per text part, an exception raised where it stands…, 1. Why it exists, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Still open (+29 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.13
Nodes (14): Baseline Failures, Baseline Failures, Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions (+6 more)

### Community 48 - "read_resume"
Cohesion: 0.16
Nodes (24): build_file(), The case as the file a candidate would upload. Hidden lines are white (PDF) or…, make_docx(), A copy of a zip (a DOCX) with parts added or replaced: macros, embedded…, rezip(), read_resume(), ResumeUnsupportedRefusal, Run (+16 more)

### Community 49 - "AppError"
Cohesion: 0.09
Nodes (44): AppError, JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, Exception, RateLimitedError, Any network-side failure of a job link. One message for every cause, so…, The job link answered, but no job description could be read from it (not HTML,… (+36 more)

### Community 50 - "test_request_context.py"
Cohesion: 0.05
Nodes (30): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, asyncio, Architecture & Design, 1. Why it exists, 2. What it is, 3. When to use it (+22 more)

### Community 51 - "test_profile_read_resume.py"
Cohesion: 0.19
Nodes (26): _content(), Image, make_pdf(), A PDF with one page per list. `encrypt` adds a standard security handler whose…, Rect, Text, test_a_long_resume_is_cut_at_the_cap_and_the_log_says_so(), one_column() (+18 more)

### Community 52 - "app_logs"
Cohesion: 0.17
Nodes (13): Affected Files & Patterns, Completed Steps, Deviations from Plan, Affected Files & Patterns, Testing Strategy, Deviations from Plan, app_logs(), client() (+5 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.17
Nodes (18): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview(), test_different_users_each_keep_their_own_in_progress_session(), test_failure_while_saving_questions_rolls_everything_back() (+10 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.17
Nodes (19): assert_unavailable(), call_lines(), llm_lines(), parametrize, The `llm_call` lines only (the call layer's `retry_wait` / `retry_giveup`…, result(), stored_questions(), test_a_provider_error_fails_the_start_after_the_call_layer() (+11 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.15
Nodes (36): 5. What can go wrong, fail(), error(), import_url(), _post(), long_posting(), page(), paste() (+28 more)

### Community 56 - "Feature: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Decisions, Edge Cases, Feature: Résumé-aware interview (Slice 8d), Functional, Goal, Known limits (+7 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.09
Nodes (57): group_requests(), The events of each request, oldest request first (the id is on every line of…, analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table() (+49 more)

### Community 58 - "test_rag_evals.py"
Cohesion: 0.08
Nodes (44): _non_negative_seconds(), _parser(), _positive(), ArgumentParser, build_sheet(), competencies_of(), Exception, _ranking() (+36 more)

### Community 59 - "decode_token"
Cohesion: 0.12
Nodes (32): BadRequestError, InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token() (+24 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 61 - "4. How it works"
Cohesion: 0.11
Nodes (20): _default_request_id(), _merge_request_fields(), Any, Replaces the value of every sensitive key (see SENSITIVE_KEYS) before anything…, Dev console: time, level, short request id, logger, event, then one aligned…, ReadableRenderer, redact_sensitive(), _redacted() (+12 more)

### Community 62 - "Rules"
Cohesion: 0.09
Nodes (20): caveman, Example output, How to invoke, See also, What it does, 1. Answer first, 2. Kill ceremony, 3. Short word (+12 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_evals.py"
Cohesion: 0.13
Nodes (37): load_cases(), Path, console_number(), hints_of(), mentions(), The hints on one case's result in Langfuse., The trace id the fake gives a case in the given repeat's run (write and stream…, run_stream_case() (+29 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.09
Nodes (49): EmbedCall, FakeEmbedder, NamedTuple, Test doubles for the Transcriber, SpeechSynthesizer and Embedder: scripted…, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, hashlib (+41 more)

### Community 66 - "Implementation Steps"
Cohesion: 0.18
Nodes (19): get_synthesizer(), get_transcriber(), Request, Built once at startup (app lifespan); None when no Deepgram key is configured…, Built once at startup (app lifespan); None when no Deepgram key is configured…, audio_container(), AudioContainer, _has_signature() (+11 more)

### Community 67 - "test_profile_routes.py"
Cohesion: 0.11
Nodes (35): 5. What can go wrong, Synthetic résumé data and the scripted model shared by the profile tests (no…, resume_docx(), resume_pdf(), body_profile(), parametrize, The profile routes end to end: scripted model behind the real tracing wrapper,…, Swagger UI builds its request from the OpenAPI schema. Declared as a url-… (+27 more)

### Community 68 - "setup_logging"
Cohesion: 0.20
Nodes (12): _formatter(), _json(), _json_renderer(), Path, Routes every logger through the processor chain. Safe to call again (tests do):…, setup_logging(), Constraints, Processor (+4 more)

### Community 69 - ".acall"
Cohesion: 0.09
Nodes (21): _Call, _OutOfTime, BaseException, T, Run `attempt(remaining_budget)` until it returns or the rules say stop (sync…, The same rules for an async attempt; waits are awaited, so the event loop stays…, Log why a stamped error ends the call. Public for the stream, whose failure…, The state of one call (its start, budget, attempt count and event label). Built… (+13 more)

### Community 71 - "interviews_job_url_utils.py"
Cohesion: 0.06
Nodes (37): is_public_address(), Scheme, credentials, port and every resolved address. Returns the address to…, True only for a globally routable unicast address., import_job_text_paste(), import_job_url(), interviews_create, Read the job description from a posting link, for the candidate to review…, Clean a whole posting page the candidate copied from their own browser: the… (+29 more)

### Community 72 - "noted"
Cohesion: 0.14
Nodes (25): long_case(), main(), noted(), reply(), run_case(), test_a_langfuse_outage_does_not_change_the_write_run(), test_a_negative_pause_is_refused(), test_a_provider_error_fails_the_case_without_crashing() (+17 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.16
Nodes (25): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, BaseException, Exception (+17 more)

### Community 74 - "test_guards.py"
Cohesion: 0.10
Nodes (27): health_check(), CurrentUserDep, raise_conflict(), raise_crash(), raise_db_down(), raise_expired(), raise_integrity(), admin_role() (+19 more)

### Community 75 - "test_gateway.py"
Cohesion: 0.10
Nodes (36): FakeSynthesizer, FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, Scripted clips (bytes, a full result, or an error), one per call; records each…, BaseModel, One spoken clip. `content_type` is what the vendor says the audio is: the…, SynthesisResult, BaseModel (+28 more)

### Community 76 - "Implementation: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gates for you, Implementation: Résumé upload and candidate profile (Slice 8c), Known Issues (+8 more)

### Community 77 - "Project"
Cohesion: 0.22
Nodes (20): candidate_profile_block(), profile_query_text(), The candidate profile as interview input: a fenced prompt block and a short…, The profile fenced as data, like the job description. Summaries and…, The profile's short items as one retrieval query. None: nothing to embed., Project, Testing Strategy, _profile() (+12 more)

### Community 78 - "scrub_contacts"
Cohesion: 0.24
Nodes (13): _phone_or_keep(), The text with email addresses and phone numbers replaced by placeholders;…, scrub_contacts(), Match, parametrize, scrub_contacts: email addresses and phone numbers removed before the résumé…, test_a_plain_email_is_removed(), test_an_email_with_plus_dots_and_subdomains_is_removed() (+5 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "interviews_report_render.py"
Cohesion: 0.15
Nodes (26): _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card(), _html_metric_row(), _html_table() (+18 more)

### Community 81 - "CaseResult"
Cohesion: 0.11
Nodes (30): _add_usage(), _case_inputs(), CaseResult, EvalCase, _print_case(), ChatModel, Namespace, One decide call on the case's latest answer, as the app makes it after every… (+22 more)

### Community 82 - "Web"
Cohesion: 0.20
Nodes (5): fixture, Request, Response, The outside world of a test: which names resolve where, what each host serves,…, Web

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+6 more)

### Community 84 - "stream_chat"
Cohesion: 0.06
Nodes (56): as_chain(), BaseChatModel, A bare chat model (tests, a single provider) is a chain of one., complete_chat(), complete_structured(), AIMessage, Any, BaseChatModel (+48 more)

### Community 85 - "FakeProvider"
Cohesion: 0.19
Nodes (26): 5. What can go wrong, Deviations from Plan, decision(), labelled_cases(), last_line(), The console lines but the last, with the measured latencies blanked., run_decide(), same_but_latency() (+18 more)

### Community 86 - "RetryPolicy"
Cohesion: 0.04
Nodes (54): parse_retry_after(), Logger, The Retry-After header as seconds. Only the delta-seconds form is read; an HTTP…, The transport retry rules for one vendor adapter, on tenacity. It holds…, RetryPolicy, One budget for the whole generation, started when the request holds its claim., U2: tenacity, An extra set of runs (not used for the verdict) (+46 more)

### Community 87 - "EmbeddingKind"
Cohesion: 0.11
Nodes (32): EmbeddingKind, EmbeddingSizeError, StrEnum, The embedding contract features code against, separate from the chat model. An…, A vector of another length than configured. Vectors of different sizes can't be…, Response, langchain_core_embeddings, Clock (+24 more)

### Community 88 - "InterviewQuestion"
Cohesion: 0.06
Nodes (38): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or (older sessions) stored up…, _history_filter(), _history_order(), InterviewsRepository, Any, datetime (+30 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "interviews_constants.py"
Cohesion: 0.03
Nodes (174): BuiltContext, FeedbackFailedError, FeedbackInProgressError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple (+166 more)

### Community 93 - "LLMServerError"
Cohesion: 0.07
Nodes (34): attempt(), _parse(), Response, The first channel's best transcript (blank for silence) and the reported audio…, One POST that never waits past the total budget; a non-2xx or failed request…, Any, LLMServerError, 5xx or a dropped connection: the provider's side failed. (+26 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "CandidateProfile"
Cohesion: 0.20
Nodes (18): CandidateProfile, The candidate profile: what a résumé becomes, what is stored, and what the API…, ExpectedProfile, _key(), ProfileScore, BaseModel, NamedTuple, Scoring an extracted profile against a hand-labelled synthetic résumé (resume-… (+10 more)

### Community 97 - "Implementation Plan: Interview Room (backend)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Blockers & Resolutions, Implementation Plan: Interview Room (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.15
Nodes (12): Baseline Failures, Commit message suggestion, Deviations from Plan, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

### Community 99 - "Implementation: Split interviews_dependencies.py by responsibility"
Cohesion: 0.05
Nodes (36): 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL), Architecture & Design (+28 more)

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
Nodes (31): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+23 more)

### Community 104 - "InterviewMessage"
Cohesion: 0.06
Nodes (52): QuestionNotCurrentError, InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, Reload rows a commit expired, so reading their fields later needs no database…, AnswerService, _elapsed_ms(), AnswerEvent, ChatModel (+44 more)

### Community 105 - "test_retry_budget.py"
Cohesion: 0.22
Nodes (9): anyio_backend(), Clock, fixture, The worst-case number of HTTP calls one logical call can make, across both…, Fake time: only the retry waits move it, so the HTTP calls themselves are…, run_decide(), test_a_transport_error_stops_the_reply_loop(), test_both_layers_fully_used_never_exceed_the_worst_case() (+1 more)

### Community 106 - "test_stream_turn.py"
Cohesion: 0.06
Nodes (68): ActionKnown, Delta, PhaseChanged, The turn's final action, sent only once nothing can change it (a follow-up only…, The next chunk of the question being written (shown as it arrives)., Settled, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase (+60 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "parse_log"
Cohesion: 0.07
Nodes (37): Call, _int(), _json_event(), LogEvent, parse_log(), NamedTuple, Reading the app's own log back: what each request did for an interview, from…, Old text lines: `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]).… (+29 more)

### Community 109 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Decisions, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal (+7 more)

### Community 110 - "interviews_retrieve.py"
Cohesion: 0.20
Nodes (7): _Chunk, Protocol, UUID, Vector search as a LangChain retriever (U3b2). A retriever is LangChain's "text…, langchain_core_callbacks, langchain_core_documents, langchain_core_retrievers

### Community 111 - "Completed Steps"
Cohesion: 0.16
Nodes (21): Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, EligibleChunk, NamedTuple, The k eligible chunks embedded with `model` that are most similar to the query,…, _degrade_reason() (+13 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "Learn: Résumé-aware interview (Slice 8d)"
Cohesion: 0.11
Nodes (16): UUID, The user's stored profile for an interview prompt, read live (never copied onto…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me (+8 more)

### Community 115 - "ReferenceNote"
Cohesion: 0.27
Nodes (16): merge_note_rankings(), The quota merge: job-description notes first, then at most `profile_slots`…, A note an interview was given: what the question writer sees (competency and…, ReferenceNote, names(), ranked(), merge_note_rankings: the quota merge of the job-description and profile…, Notes named by single letters, ranked in the given order with falling scores. (+8 more)

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
Cohesion: 0.07
Nodes (37): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewListOut (+29 more)

### Community 121 - "test_write.py"
Cohesion: 0.31
Nodes (16): call_lines(), The blocking write on the LangChain call layer (U3b1 step 5, FR5, AC5, AC10):…, reply(), run(), test_a_context_too_large_makes_no_call(), build(), test_a_follow_up_takes_the_main_questions_category(), test_a_rejected_request_is_not_retried() (+8 more)

### Community 122 - "Feature: Agentic Workflow v2 (debug, review-feature, gated loop)"
Cohesion: 0.14
Nodes (15): Overview, Project Rules Applied, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Agentic Workflow v2 (debug, review-feature, gated loop), Functional (+7 more)

### Community 123 - "._next"
Cohesion: 0.15
Nodes (11): AIMessage, Any, BaseMessage, BaseModel, ChatGenerationChunk, ChatResult, Runnable, Approaches Considered (+3 more)

### Community 124 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.14
Nodes (17): injection_ignored(), 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+9 more)

### Community 125 - "parse_profile_reply"
Cohesion: 0.29
Nodes (16): parse_profile_reply(), A JSON-text reply, checked against `RawProfile`, then `clean_profile`. The live…, parametrize, parse_profile_reply: the model's JSON -> a capped, cleaned CandidateProfile, or…, reply(), test_a_fenced_reply_is_read(), test_a_reply_outside_the_schema_is_invalid(), test_a_reply_that_is_not_one_json_object_is_invalid() (+8 more)

### Community 126 - "test_profile_context.py"
Cohesion: 0.20
Nodes (23): estimate_tokens(), default_strategy(), everything(), fingerprint(), golden_inputs(), inputs(), manager_for(), max_profile() (+15 more)

### Community 127 - "summarize_job_description"
Cohesion: 0.21
Nodes (16): ChatModel, One summary call; see `SummaryOutcome`. A reply that `validate_summary` rejects…, summarize_job_description(), llm_lines(), no_retry_waits(), fixture, parametrize, The job-description summary on the LangChain layer… (+8 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "test_chat_stream_live.py"
Cohesion: 0.29
Nodes (7): _model(), AIMessageChunk, Opt-in spike (U3b1 FR1): how the real Gemini chat model streams through…, _stream(), test_stream_usage_and_finish_reason_match_a_blocking_call(), test_tiny_timeout_fails_before_the_first_chunk(), test_whether_the_timeout_bounds_the_whole_stream()

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

### Community 138 - "Implementation Plan: Job URL (Slice 8b)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Job URL (Slice 8b), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "done"
Cohesion: 0.09
Nodes (25): done(), Slice 4: SSE streaming, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 7. What surprised me (+17 more)

### Community 142 - "bind_log_context"
Cohesion: 0.20
Nodes (18): bind_log_context(), Adds fields to every later log line of the current request (or, outside a…, log_retrieval(), Which reference notes an interview got at start: mode, count, scores, how many…, render_text(), structlog, _call(), _context_build() (+10 more)

### Community 143 - "check_prompts"
Cohesion: 0.18
Nodes (18): check_prompts(), PromptCheckError, Exception, One or more routed prompts cannot be sent; the message lists each one., Raises PromptCheckError naming every routed version whose file is missing or…, 4. How it works, Known Issues, Skills Consulted During Implementation (+10 more)

### Community 144 - "test_reference_note_context.py"
Cohesion: 0.15
Nodes (24): Task, WindowLedger, 5. What can go wrong, manager(), manager(), first_user(), inputs(), _max_note() (+16 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only"
Cohesion: 0.05
Nodes (47): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Known Issues, Links, Open Questions (+39 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_reply_contract.py"
Cohesion: 0.08
Nodes (43): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split), Acceptance Criteria (+35 more)

### Community 151 - "Implementation: U3c — Fallback chain, question bank removal, old LLM layer deleted"
Cohesion: 0.12
Nodes (15): Baseline Failures, Completed Steps, Current Step, Debug Log, Implementation: U3c — Fallback chain, question bank removal, old LLM layer deleted, Known Issues, Links, Open Questions (+7 more)

### Community 152 - "Implementation: Agentic Workflow v2"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Debug Log, Deviations from Plan, Dry runs (needs the user), Implementation: Agentic Workflow v2 (+8 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.13
Nodes (27): corpus(), embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of() (+19 more)

### Community 156 - "interviews_evals.py"
Cohesion: 0.05
Nodes (71): anyio_from_thread, InvalidReplyError, load_object(), Exception, Reading a model's JSON reply: one optional ```json fence around one JSON…, The reply as a JSON object: one optional fence around it, nothing else before…, _check_question(), InterviewerReply (+63 more)

### Community 157 - "Implementation: Interview Room (backend)"
Cohesion: 0.08
Nodes (26): BaseModel, Every speech setting in one read-only group, so the speech factories depend on…, Speech-to-text (voice answers)., Text-to-speech (the interviewer's voice)., The speech vendor's settings, grouped (see `Settings.speech`). One key and base…, _SpeechPart, SpeechSettings, SttSettings (+18 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (14): 9. Review gate (user), Baseline Failures, Changes Made, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions (+6 more)

### Community 159 - "QuestionTurn"
Cohesion: 0.09
Nodes (39): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the… (+31 more)

### Community 160 - "profile_reply.py"
Cohesion: 0.12
Nodes (26): NamedTuple, What one summary call gave: the usable summary (None when it can't replace the…, SummaryOutcome, clean_profile(), fit(), ModelProfile, ModelProject, ModelRole (+18 more)

### Community 161 - "Tracer"
Cohesion: 0.05
Nodes (46): AbstractContextManager, Any, TraceLabels, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,… (+38 more)

### Community 162 - "interviews_knowledge_ingest.py"
Cohesion: 0.12
Nodes (23): Splitting a note's body into its `##` sections with LangChain's…, Each `##` heading's text; text before the first `##` (the `#` title) has no…, split_sections(), main(), _parser(), ArgumentParser, Session, Ingest the reference notes into the database (knowledge-base RAG). uv run… (+15 more)

### Community 163 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 164 - "test_start_with_profile.py"
Cohesion: 0.22
Nodes (17): 5. What can go wrong, embedder(), first_question(), profile_of(), fixture, Starting an interview with the candidate's profile (resume-aware-interview Step…, A synthetic profile whose every free-text field carries `marker`, so a leak…, sent() (+9 more)

### Community 165 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 166 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.13
Nodes (14): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+6 more)

### Community 167 - "provider.py"
Cohesion: 0.04
Nodes (101): anyio, The provider chain (U3c): the chat models of `LLM_PROVIDERS`, in order, which…, A LangChain chat model for tests (spec FR6): scripted replies or errors, every…, _finish_reason(), The LangChain call layer's public face (U3a): the `ChatModel` type services are…, The streamed call of the LangChain call layer (U3b1): `astream()` under the…, Langfuse tracing for the LangChain call layer, through our own `Tracer` (U3a,…, ContextManager (+93 more)

### Community 168 - "test_prompt_registry.py"
Cohesion: 0.16
Nodes (20): Data, What an interviewer write carries beyond the job description; it picks the…, ast, 5. What can go wrong, catalog_mismatches(), Collection, The prompt registry's guards (prompt-registry AC1, AC2, AC6, EC1-EC4). Each…, A string literal that is exactly a version name, outside the registry: a… (+12 more)

### Community 169 - "ChatMessage"
Cohesion: 0.08
Nodes (30): ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, JobDescriptionSummary, SummaryInputs, Step 11: `FakeProvider.stream`, ReasoningEffort, Reply (+22 more)

### Community 170 - "failed"
Cohesion: 0.11
Nodes (27): Check, check_decision(), check_reply(), check_streamed_reply(), pause_for(), Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format. (+19 more)

### Community 171 - "U3b1 stage 2 (decide on LangChain, structured output) vs. the baseline"
Cohesion: 0.10
Nodes (15): Failures, Scores, Should this be the new baseline?, U3b1 stage 2 (decide on LangChain, structured output) vs. the baseline, Why it may have improved, Baseline, Failures, Scores (+7 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "pytest"
Cohesion: 0.09
Nodes (23): pytest, anyio_backend(), _lines(), fixture, Opt-in: real calls to Deepgram Aura text-to-speech (interview-room Phase 0…, test_aura_speaks_each_kind_of_line_in_the_configured_format(), parametrize, test_auth_routes_document_error_responses() (+15 more)

### Community 174 - "Implementation: U1 structlog (structured JSON logs)"
Cohesion: 0.15
Nodes (12): Changes Made, Completed Steps, Current Step, Debug Log, Implementation: U1 structlog (structured JSON logs), Known Issues, Links, Open Questions (+4 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "ErrorResponse"
Cohesion: 0.03
Nodes (68): ErrorBody, ErrorResponse, BaseModel, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview (+60 more)

### Community 178 - "get_logger"
Cohesion: 0.17
Nodes (20): BaseTransport, get_logger(), Logger, 5. What can go wrong, parametrize, The logging pipeline (U1 structlog): what actually lands in the log file and on…, test_a_key_that_only_contains_a_sensitive_word_is_kept(), test_a_logged_exception_is_one_line_with_the_traceback() (+12 more)

### Community 179 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.13
Nodes (14): 13. Phase 2 real runs (yours), Baseline Failures, Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions (+6 more)

### Community 180 - "StreamedTurn"
Cohesion: 0.18
Nodes (9): parse_sse(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream() (+1 more)

### Community 181 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 182 - "profile_extract.py"
Cohesion: 0.07
Nodes (32): load_prompt(), Path, Prompt files: versioned Markdown read once per process. Feature modules pass…, `<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in…, Condense a long job description once, so later calls send less…, build_messages(), extract_profile(), Extraction (+24 more)

### Community 183 - "test_answer_guards.py"
Cohesion: 0.13
Nodes (14): message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_a_future_question_is_not_current_either(), test_any_question_but_the_current_one_is_the_same_409(), test_database_failure_while_saving_the_answer_persists_nothing() (+6 more)

### Community 184 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.11
Nodes (18): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules, Overview, Project Rules Applied, Ready to Implement (+10 more)

### Community 185 - "hint_for"
Cohesion: 0.18
Nodes (12): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+4 more)

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

### Community 193 - "interviews_model.py"
Cohesion: 0.06
Nodes (60): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+52 more)

### Community 203 - "LoggedLine"
Cohesion: 0.33
Nodes (3): LoggedLine, One JSON line of the log file, read the way older tests read a log record:…, _shown()

### Community 207 - "Implementation: Résumé-aware interview (Slice 8d)"
Cohesion: 0.12
Nodes (16): Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Gate: Step 10, real-model runs (yours), Implementation: Résumé-aware interview (Slice 8d), Known Issues (+8 more)

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.16
Nodes (23): corpus(), embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, Ingests the three notes; returns the vector each note text gets (the embedder… (+15 more)

### Community 212 - "RateLimiter"
Cohesion: 0.19
Nodes (11): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, Per-user caps on paid speech calls. One limiter instance per process: every…, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window() (+3 more)

### Community 220 - "LLMError"
Cohesion: 0.07
Nodes (61): log_switch(), Logger, One event per hand-over: provider names and the error class only, never text., _from_status(), _google_error(), _mapped(), BaseException, Map what the LangChain/Gemini call layer raises to our LLMError types (spec… (+53 more)

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

### Community 234 - "case"
Cohesion: 0.22
Nodes (16): feedback_trace_output(), What came out next to what was wanted: the verdict, the overall against its…, case(), run_feedback_case(), test_a_case_in_its_band_passes_every_check(), test_a_passing_case_has_no_hints(), test_a_provider_error_is_the_cases_error(), test_an_errored_case_scores_only_validity_and_the_verdict() (+8 more)

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "Implementation: U3a LangChain foundation + first chains"
Cohesion: 0.12
Nodes (15): 9 -> 10. Stop: user-run comparison evals, Check results, Completed Steps, Current Step, Debug Log, Implementation: U3a LangChain foundation + first chains, Known Issues, Links (+7 more)

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

### Community 244 - "interviews_schema.py"
Cohesion: 0.04
Nodes (92): current_request_id(), FeedbackStatus, MessageKind, MessageRole, StrEnum, The SSE event names of a streamed turn: the contract with the client. `done`…, A feedback row's life: `generating` while a request holds it, then `generated`…, Transcript item kinds: a question comes from interview_questions, the other two… (+84 more)

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "interviewer_v7.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 249 - "interviewer_v7_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 250 - "_DeepgramAdapter"
Cohesion: 0.18
Nodes (7): _DeepgramAdapter, attempt(), T, What both Deepgram adapters share: one authenticated client, the retry policy…, Attempted, What one call returned, plus how many attempts and how long it took (for the…, AsyncBaseTransport

### Community 251 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Blockers & Resolutions, Deviations found during implementation (2026-11-14), Implementation Plan: Résumé upload and candidate profile (Slice 8c), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 252 - "Feature: U3c — Fallback chain, question bank removal, old LLM layer deleted"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: U3c — Fallback chain, question bank removal, old LLM layer deleted, Functional, Goal, Non-Functional (+6 more)

### Community 253 - "test_tracing_lifespan.py"
Cohesion: 0.20
Nodes (7): fastapi_testclient, The app lifespan runs the prompt check before anything else (prompt-registry…, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 255 - "Feature: U1 structlog (structured JSON logs)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: U1 structlog (structured JSON logs), Functional, Goal, Non-Functional (+6 more)

### Community 256 - "Feature: Job URL (Slice 8b)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Job URL (Slice 8b), Functional, Goal, Non-Functional (+7 more)

### Community 257 - "KnowledgeRepository"
Cohesion: 0.07
Nodes (54): KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, parse_arms(), `--arms`: comma-separated arm letters (any case), at least two (a ranking…, parametrize, The generation eval's arms D and E (resume-aware-interview Step 9a; seam S5).… (+46 more)

### Community 258 - "Role"
Cohesion: 0.21
Nodes (19): Role, _appears(), ground_profile(), keep(), _normalized(), Pure helpers of the profile feature: contact scrubbing, résumé reading,…, `item` occurs in `source` as a whole word or phrase, ignoring case and spacing…, The profile with every short item the source text does not contain dropped, and… (+11 more)

### Community 259 - "WithInterviewData"
Cohesion: 0.07
Nodes (34): build_context_manager(), FullHistory, A main-question write that carries the interview's own data: reference notes…, How many notes and whether the profile went into this write (numbers only, for…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, WithInterviewData, The labelled text the write call is asked for (the parser reads it back…, Affected Files & Patterns (+26 more)

### Community 260 - "test_answer_llm.py"
Cohesion: 0.07
Nodes (30): 2. What it is, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied (+22 more)

### Community 261 - "Role"
Cohesion: 0.10
Nodes (24): verify_password(), permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, main(), Session, test_admin_holds_every_user_permission() (+16 more)

### Community 262 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.18
Nodes (10): Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Implementation Steps, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 263 - "clock"
Cohesion: 0.11
Nodes (16): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+8 more)

### Community 264 - "FeedbackCaseResult"
Cohesion: 0.20
Nodes (14): criterion_spread(), feedback_hints_for(), FeedbackCaseResult, level_gap_check(), _print_case(), The pair's check, or None when there is nothing to compare: no pair, or either…, Per case: the largest gap between the highest and lowest score any one…, Where to look first for each failed check (or the error), in the order the… (+6 more)

### Community 265 - "Implementation Plan: Résumé-aware interview (Slice 8d)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Decisions (grill-me, 2026-11-14), Deviations during implementation (2026-11-14, see task.md), Implementation Plan: Résumé-aware interview (Slice 8d), Overview, Ready to Implement, Skills Consulted (+2 more)

### Community 266 - "interviews_route.py"
Cohesion: 0.10
Nodes (45): alias, AnswerControllerDep, Permission, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), limit_feedback(), interviews_feedback, Per-user cap on feedback requests, checked before anything that can cost an LLM… (+37 more)

### Community 267 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 268 - "profile_resume_files.py"
Cohesion: 0.15
Nodes (12): _escape(), _fill(), plain_zip(), Synthetic résumé files written in code: the tests and the profile eval build…, Color, docx, docx_oxml, docx_oxml_ns (+4 more)

### Community 269 - "interviews_voice_dependencies.py"
Cohesion: 0.10
Nodes (23): Response, UUID, The interview voice adapter, HTTP side: request -> VoiceService, domain result…, The clip with the media type the synthesizer reported, never a hardcoded one.…, VoiceController, get_voice_controller(), get_voice_service(), Depends (+15 more)

### Community 270 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

### Community 271 - "run_name"
Cohesion: 0.11
Nodes (18): Unique per command, repeat and arm (Langfuse merges runs that share a name on…, run_name(), Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional (+10 more)

### Community 272 - "Implementation: Start an Interview (backend)"
Cohesion: 0.13
Nodes (14): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions (+6 more)

### Community 273 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 274 - "Learn: Agentic workflow patterns (reflection, tool use, bounded autonomy)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 275 - "Implementation Plan: Agentic Workflow v2"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Approaches Considered, Architecture & Design, Blockers & Resolutions, Implementation Plan: Agentic Workflow v2, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 276 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 290 - "_Stt"
Cohesion: 0.25
Nodes (5): get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them., The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank)., _Stt

### Community 291 - "Langfuse Observability"
Cohesion: 0.20
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 292 - "Implementation: U3b1 Interview calls on LangChain"
Cohesion: 0.15
Nodes (12): Baseline Failures, Changes Made, Current Step, Debug Log, Done, Implementation: U3b1 Interview calls on LangChain, Known Issues, Links (+4 more)

### Community 293 - "test_reaction_pick.py"
Cohesion: 0.21
Nodes (16): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), Random, A predefined, neutral acknowledgement for the answer just given; never the same…, random, pick(), parametrize (+8 more)

### Community 294 - "get_chat_model"
Cohesion: 0.23
Nodes (11): get_chat_model(), ChatModel, The provider chain, built once at startup (app lifespan). Tests override this…, get_resume_limiter(), Tests swap in a fresh limiter so counts never leak between them., Deviations from Plan, fresh_limiter(), profile_llm() (+3 more)

### Community 295 - "Implementation: Error Handling"
Cohesion: 0.17
Nodes (11): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+3 more)

### Community 296 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Implementation Steps, Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 297 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 298 - "main"
Cohesion: 0.16
Nodes (18): html_target(), main(), Path, Session, UUID, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order., read_log_lines() (+10 more)

### Community 299 - "Learn: a provider fallback chain (U3c, built; real-model runs pending)"
Cohesion: 0.17
Nodes (11): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Eval log (AI features only) (+3 more)

### Community 300 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 301 - "LogCapture"
Cohesion: 0.18
Nodes (5): StringIO, AppLogs, LogCapture, Path, What the real logging pipeline wrote during a test: the file's JSON lines and…

### Community 302 - "test_context_controller.py"
Cohesion: 0.28
Nodes (12): candidate_messages(), noted(), fixture, run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_ends_the_start_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_without_one_in_the_reply_or_for_the_final_answer() (+4 more)

### Community 303 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 304 - "Embedder"
Cohesion: 0.06
Nodes (31): Embedder, Protocol, 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e) (+23 more)

### Community 305 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 306 - "Implementation Steps"
Cohesion: 0.50
Nodes (4): Implementation Steps, Milestone A: reliability and recovery, Milestone B: techniques, Step 0 (setup)

### Community 308 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 309 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 310 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 311 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (13): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied (+5 more)

### Community 312 - "Learn: one retry policy on tenacity, and why reply retries stay out of it (U2)"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Eval log (+1 more)

### Community 313 - "Implementation Plan: U3b1 Interview calls on LangChain"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: U3b1 Interview calls on LangChain, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 314 - "test_job_description_summary.py"
Cohesion: 0.29
Nodes (7): google_api_core, parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version()

### Community 315 - "Learn: Prompt registry (one place for prompt versions and routing)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Eval log (AI features only), Learn: Prompt registry (one place for prompt versions and routing)

### Community 316 - "test_tracing.py"
Cohesion: 0.04
Nodes (45): The LangChain tracing callback (spec FR5, AC8, EC14, EC15): one Langfuse…, result(), test_a_call_records_one_generation_with_its_messages_labels_and_usage(), test_a_disabled_tracer_records_nothing(), test_a_failed_call_records_an_error_with_the_error_class(), test_a_langfuse_failure_never_fails_the_call(), test_a_redacted_call_records_the_placeholder_for_input_and_output(), test_retried_attempts_are_still_one_generation_with_the_attempt_count() (+37 more)

### Community 317 - "Implementation Plan: U3c — Fallback chain, question bank removal, old LLM layer deleted"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: U3c — Fallback chain, question bank removal, old LLM layer deleted, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 318 - "test_eval_runs.py"
Cohesion: 0.06
Nodes (45): _evaluation(), git_commit(), notes_fingerprint(), Any, Score, What every eval task moved onto Langfuse experiments shares (langfuse-…, Run every case once, in order, as one Langfuse experiment run; whatever the run…, The short commit hash, `-dirty` when the working tree has changes, `unknown`… (+37 more)

### Community 319 - "synthesize"
Cohesion: 0.29
Nodes (8): Text-to-speech is off (no key) or its vendor failed. The interview still works:…, SpeechUnavailableError, _log(), Logger, `text` spoken by the configured voice, as one whole clip. The caller decides…, synthesize(), LogFields, synthesize()

### Community 320 - "Status"
Cohesion: 0.43
Nodes (8): PromptVersion, StrEnum, Status, archived_routes(), incomplete_entries(), test_a_route_to_an_archived_or_unknown_version_is_named(), test_an_entry_with_no_reason_or_a_wrong_name_is_named(), test_every_catalog_entry_has_a_status_and_a_reason()

### Community 321 - "Feature: U3b1 Interview calls on LangChain"
Cohesion: 0.29
Nodes (6): Blockers, Constraints, Feature: U3b1 Interview calls on LangChain, Goal, Out of Scope, User Flow

### Community 322 - "_RoutedChatModel"
Cohesion: 0.29
Nodes (6): Any, BaseMessage, ChatResult, The chat model of the `llm` fixture: the summary goes to `llm.summary`; every…, _RoutedChatModel, as_chat()

### Community 323 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional, Goal (+7 more)

### Community 324 - "get_current_user"
Cohesion: 0.10
Nodes (24): ForbiddenError, get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, check(), require_roles(), check(), AuthServiceDep, bearer_scheme (+16 more)

### Community 325 - "_StderrHandler"
Cohesion: 0.33
Nodes (4): Writes to whatever `sys.stderr` is at the time of the write (test runners and…, _StderrHandler, setter, TextIO

### Community 326 - "Settings"
Cohesion: 0.09
Nodes (30): ChatChain, Ordered `(provider name, chat model)` pairs; the first is the primary., build_chat_model(), _google_chat_model(), BaseChatModel, The provider chain: one LangChain chat model per entry of `LLM_PROVIDERS`, in…, ProviderConfig, model_validator (+22 more)

### Community 327 - "RecordingClient"
Cohesion: 0.12
Nodes (10): stream(), submit_the_same_answer_elsewhere(), fresh_limiter(), owner(), fixture, Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, Fake wall clock for the claim token and the stale takeover., recording() (+2 more)

### Community 328 - "llm"
Cohesion: 0.12
Nodes (24): Functional, Non-Functional, Requirements, Skills Consulted, Functional, Non-Functional, Requirements, as_v5_text() (+16 more)

### Community 329 - "load_feedback_cases"
Cohesion: 0.40
Nodes (5): load_feedback_cases(), Path, parametrize, test_a_badly_labelled_case_is_rejected(), test_a_pair_must_name_an_earlier_case()

### Community 330 - "interviews/conftest.py"
Cohesion: 0.12
Nodes (18): auth_header(), _header(), Bearer header for a user; pass role to mint a token whose role claim differs…, answer(), _answer(), anyio_backend(), Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a recording to the transcription endpoint; `audio=None` sends no file part… (+10 more)

### Community 332 - "feedback_dataset_items"
Cohesion: 0.50
Nodes (4): feedback_dataset_items(), Any, The cases as dataset items: the interview as input, the bands as the expected…, test_the_dataset_items_carry_the_interview_and_the_expected_bands()

### Community 334 - "U0 baselines"
Cohesion: 0.25
Nodes (7): Before relying on this, Cost, Eval baselines, How to use this file, Live interviews (from `logs/app.log`, before U1), Prompts with no eval baseline (gaps), U0 baselines

### Community 336 - "test_speech_contracts.py"
Cohesion: 0.08
Nodes (26): Protocol, `text` spoken in the configured voice, as one whole clip., SpeechSynthesizer, Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, AI Engineering Upgrade Path (Cuewise), Build order (+18 more)

### Community 337 - "Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)"
Cohesion: 0.33
Nodes (5): 1. Why it exists, 2. What it is, 3. When to use it, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)

### Community 338 - "ProviderChatModel"
Cohesion: 0.29
Nodes (8): _message(), ProviderChatModel, AIMessage, Any, BaseMessage, ChatGenerationChunk, ChatResult, `route` is one provider, or a function from the call's system prompt to the…

### Community 339 - "Slices in detail"
Cohesion: 0.10
Nodes (20): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style), Progress, Slice 10: Provider fallback chain (+12 more)

### Community 341 - "GoogleEmbedder"
Cohesion: 0.04
Nodes (70): invoke(), EmbeddingResult, BaseModel, GoogleEmbedder, Nearest, NamedTuple, The search's chunks for `vector`, most similar first, through the retriever., VectorRetriever (+62 more)

### Community 342 - "Learn: Résumé upload and the candidate profile (Slice 8c)"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 8. Check your understanding, 9. Go deeper / Still open, Learn: Résumé upload and the candidate profile (Slice 8c)

### Community 344 - "safe_fetch.py"
Cohesion: 0.14
Nodes (10): _decode(), FetchError, BaseTransport, Exception, Fetch a web page whose address a user chose, without letting that user reach…, Header charset, else a <meta> charset, else UTF-8; never raises (bad bytes…, codecs, ipaddress (+2 more)

### Community 347 - "test_log_context.py"
Cohesion: 0.29
Nodes (9): fixture, Log context on real interview requests (U1 structlog, AC4): `session` and…, Every line of the one request whose access line ends with `path_end`., _request_lines(), started(), test_a_request_for_someone_elses_interview_logs_the_id_it_asked_for(), test_a_start_request_logs_the_new_session_and_the_user_on_every_line(), test_a_streamed_turn_logs_its_session_and_user_from_inside_the_stream() (+1 more)

### Community 348 - "profile_service.py"
Cohesion: 0.07
Nodes (44): ProfileExtractionFailedError, ProfileNotFoundError, Over the byte, page or unzipped-size limit of a résumé upload., Not a PDF or a Word document by its content (the file name is never trusted)., Encrypted, corrupt, scanned, too little text, or no usable profile in it., The model gave no valid profile after the retry, timed out, or the provider…, ResumeTooLargeError, ResumeUnreadableError (+36 more)

### Community 351 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

### Community 354 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

## Knowledge Gaps
- **1206 isolated node(s):** `cuewise-be`, `What it does`, `How to invoke`, `Example output`, `See also` (+1201 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2837 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **58 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `LLMError` connect `LLMError` to `main.py`, `Implementation Plan: Langfuse Tracing`, `clock`, `interviews_route.py`, `test_deepgram.py`, `test_knowledge_ingest.py`, `interviews_evals.py`, `LLMResult`, `interviews_rag_evals.py`, `ChatTrace`, `profile_reply.py`, `FakeChatModel`, `provider.py`, `Implementation Plan: LLM as the Interviewer (it asks the questions)`, `ChatMessage`, `test_chat_stream.py`, `Embedder`, `profile_extract.py`, `Learn: one retry policy on tenacity, and why reply retries stay out of it (U2)`, `Implementation Plan: U3b1 Interview calls on LangChain`, `Implementation Plan: U3c — Fallback chain, question bank removal, old LLM layer deleted`, `synthesize`, `FakeEmbedder`, `Implementation Steps`, `.acall`, `Settings`, `llm`, `test_gateway.py`, `test_speech_contracts.py`, `CaseResult`, `stream_chat`, `GoogleEmbedder`, `RetryPolicy`, `FakeProvider`, `interviews_constants.py`, `LLMServerError`, `Implementation Plan: Interview Room (backend)`, `test_speech.py`, `test_stream_turn.py`, `Completed Steps`, `Feature: Langfuse Tracing`, `Cuewise BE — Project Instructions`, `Feature: U3c — Fallback chain, question bank removal, old LLM layer deleted`, `summarize_job_description`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Why does `Tracer` connect `Tracer` to `KnowledgeRepository`, `main.py`, `test_summary_evals.py`, `run_name`, `TracerHandle`, `test_feedback_evals.py`, `score`, `interviews_evals.py`, `test_feedback_endpoint.py`, `LLMResult`, `interviews_rag_evals.py`, `ChatTrace`, `FakeChatModel`, `run_generation`, `profile_evals.py`, `provider.py`, `ChatMessage`, `get_interviews_service`, `test_chat_stream.py`, `Embedder`, `profile_extract.py`, `test_tracing.py`, `test_tracing_routes.py`, `test_eval_runs.py`, `test_evals.py`, `test_profile_routes.py`, `Settings`, `RecordingClient`, `noted`, `CaseResult`, `test_retrieval_eval.py`, `FakeProvider`, `RetryPolicy`, `profile_service.py`, `interviews_constants.py`, `LLMError`, `InterviewMessage`, `Completed Steps`, `test_decide.py`, `test_write.py`, `test_tracing_lifespan.py`, `summarize_job_description`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `KnowledgeRepository`, `main.py`, `test_answer_llm.py`, `test_feedback_evals.py`, `test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`, `interviews_evals.py`, `QuestionTurn`, `ChatTrace`, `profile_reply.py`, `FakeChatModel`, `Tracer`, `profile_evals.py`, `provider.py`, `ChatMessage`, `test_chat_stream.py`, `pytest`, `Embedder`, `profile_extract.py`, `test_start_llm.py`, `test_tracing.py`, `test_evals.py`, `noted`, `CaseResult`, `ProviderChatModel`, `stream_chat`, `FakeProvider`, `RetryPolicy`, `LLMError`, `profile_service.py`, `interviews_constants.py`, `test_stream_turn.py`, `interviews_schema.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `FakeChatModel` (e.g. with `U3: Migrate to LangChain + provider fallback chain` and `2. What it is`) actually correct?**
  _`FakeChatModel` has 25 INFERRED edges - model-reasoned connections that need verification._
- **Are the 50 inferred relationships involving `Tracer` (e.g. with `ChatTrace` and `TracerHandle`) actually correct?**
  _`Tracer` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 98 inferred relationships involving `LLMError` (e.g. with `log_switch()` and `_from_status()`) actually correct?**
  _`LLMError` has 98 INFERRED edges - model-reasoned connections that need verification._
- **Are the 53 inferred relationships involving `FakeProvider` (e.g. with `Build order: "Chat with the interviewer"` and `Slice 1: Answer → reply (no streaming)`) actually correct?**
  _`FakeProvider` has 53 INFERRED edges - model-reasoned connections that need verification._