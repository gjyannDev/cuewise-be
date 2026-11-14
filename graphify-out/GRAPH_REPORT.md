# Graph Report - cuewise-be  (2026-11-14)

## Corpus Check
- 369 files · ~335,757 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 5145 nodes · 14513 edges · 260 communities (222 shown, 38 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2784 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e45e503f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- interviews_constants.py
- LLMServerError
- KnowledgeRepository
- decode_token
- test_interview_report.py
- User
- Cuewise BE — Project Instructions
- test_job_url_utils.py
- pytest
- tests/conftest.py
- interviews_rag_evals.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- test_stream_answer.py
- test_feedback_evals.py
- test_safe_fetch.py
- interviews_route.py
- test_tracing_lifespan.py
- cuewise-be
- LLMResult
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_transcript.py
- Slice 8: Embeddings and RAG (split into 8a to 8e)
- Feature: Context Management for the Interview LLM Calls
- RateLimiter
- interviews_retrieval_service.py
- test_reference_note_context.py
- safe_fetch.py
- Feature: LLM as the Interviewer (it asks the questions)
- QuestionTurn
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- interviews_job_url_service.py
- interviews_schema.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_evals.py
- test_feedback_contract.py
- interviews_model.py
- InterviewerInputs
- Implementation Steps
- test_create_interview.py
- test_start_llm.py
- test_job_url.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- FakeClient
- test_tracing_routes.py
- InterviewQuestion
- ConsoleFormatter
- job_description_summary_v2.md
- FakeProvider
- FakeEmbedder
- test_follow_ups.py
- re
- InterviewMessage
- test_answer_llm.py
- test_eval_runs.py
- decision
- exception_handlers.py
- errors.py
- test_tracing.py
- ._ordered
- test_question_bank.py
- Implementation: Start an Interview (backend)
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Langfuse Prompt Migration
- EmbeddingKind
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Bundle
- build_context_manager
- LLMTimeoutError
- run_task
- test_reaction_pick.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- interviews_feedback_evals.py
- clock
- Langfuse Observability
- interviewer_v3.md
- Implementation: LLM as the Interviewer (it asks the questions)
- llm
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_factory.py
- test_get_interview.py
- StreamedTurn
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- interviews_feedback_turn.py
- main
- Implementation: Eval runs in Langfuse (scores + datasets)
- Feature: Langfuse Tracing
- Langfuse
- QuestionCategory
- run_generation
- audio_container
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Langfuse Implementation Notes
- interviewer_v5.md
- run_name
- types.py
- Implementation: Three New Interview Roles (designer, qa, devops)
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Feature: Résumé upload and candidate profile (Slice 8c)
- How to evaluate an AI feature: from the command to the fix
- test_context_controller.py
- Langfuse Dataset Construction
- Langfuse v4 project migration
- Implementation: Error Handling
- Implementation: Interview History List (backend)
- Judge Calibration
- Feature: Interview History List (backend)
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Job URL (Slice 8b)
- Langfuse Implementation Notes
- hints_of
- test_knowledge_ingest.py
- ChatMessage
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- test_turn_budget.py
- Langfuse CI/CD
- Prompt Engineering
- Slices in detail
- ContextManager
- auth_header
- Implementation: Job URL (Slice 8b)
- test_start_reference_notes.py
- test_me.py
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- WindowLedger
- interviews/conftest.py
- Tracer
- test_answer_interview.py
- interviews_answer_service.py
- experiments
- ErrorResponse
- .retrieve
- Implementation Plan: Role-Based Access Control (single JWT)
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_fallback_pick.py
- test_select_questions.py
- interviews_feedback.py
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- OpenAICompatibleProvider
- feedback_score_v1.md
- feedback_write_v1.md
- test_reply_contract.py
- test_keyterms.py
- .finish_answer
- JobRole
- time
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Feature: Layered Modules (route -> controller -> service -> repository)
- test_user_ids.py
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- _raise_location
- Implementation Plan: Follow-up Questions (decide / write split)
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- interviews_feedback_controller.py
- users_utils.py
- _reset_request_id
- test_job_description_summary.py
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
- _LostClaim
- Communication and priorities
- Engineering habits
- Senior judgement
- _Usage
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- .__call__
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- Langfuse CLI Reference
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- interviewer_v7.md
- interviewer_v7_json.md
- corpus
- fake.py
- Implementation Plan: Résumé upload and candidate profile (Slice 8c)
- Langfuse
- traces
- test_generation_eval.py
- 2. Langfuse Documentation
- test_feedback_context.py
- FakeLangfuse

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 113 edges
2. `User` - 112 edges
3. `FakeProvider` - 110 edges
4. `JobRole` - 104 edges
5. `LLMResult` - 94 edges
6. `Level` - 89 edges
7. `InterviewQuestion` - 88 edges
8. `InterviewType` - 87 edges
9. `QuestionCategory` - 86 edges
10. `InterviewsRepository` - 81 edges

## Surprising Connections (you probably didn't know these)
- `2. What it is` --references--> `ContextManager`  [INFERRED]
  docs/features/context-management/learnings.md → app/core/ai/context.py
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `Acceptance Criteria` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py
- `Functional` --references--> `Embedder`  [INFERRED]
  docs/features/knowledge-base-rag/spec.md → app/core/ai/embedder.py
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py

## Import Cycles
- None detected.

## Communities (260 total, 38 thin omitted)

### Community 0 - "interviews_constants.py"
Cohesion: 0.11
Nodes (31): HistorySortColumn, MessageKind, MessageRole, StrEnum, QuestionKind, The history columns GET /interviews sorts by; the values are the response's…, A main question opens a thread; a follow-up digs into the latest answer of that…, Why an interview has no reference notes at all (logged as… (+23 more)

### Community 1 - "LLMServerError"
Cohesion: 0.09
Nodes (36): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The first channel's best transcript (blank for silence) and the reported audio…, LLMRateLimitError (+28 more)

### Community 2 - "KnowledgeRepository"
Cohesion: 0.07
Nodes (41): alembic_config, InterviewSessionChunk, KnowledgeChunk, KnowledgeChunkScope, One (role, level) a chunk applies to. Rows instead of array columns, so the…, A reference note one interview was given at start: the same notes for every…, _eligible(), EligibleChunk (+33 more)

### Community 3 - "decode_token"
Cohesion: 0.08
Nodes (45): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+37 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (52): analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start(), html_for() (+44 more)

### Community 5 - "User"
Cohesion: 0.07
Nodes (50): hash_password(), verify_password(), permissions_for(), The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, AuthController, Request -> service call, domain result -> response schema., get_controller() (+42 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_job_url_utils.py"
Cohesion: 0.06
Nodes (60): extract_job_text(), _find_posting(), _from_jsonld(), _from_main_content(), _html_to_text(), pasted_job_text(), _plain(), _posting_text() (+52 more)

### Community 8 - "pytest"
Cohesion: 0.07
Nodes (52): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, Ingest the reference notes into the database (knowledge-base RAG). uv run…, _check_hidden(), Corpus, CorpusError, cosine_similarity(), _hash() (+44 more)

### Community 9 - "tests/conftest.py"
Cohesion: 0.09
Nodes (29): health_check(), CurrentUserDep, os, sqlalchemy_pool, raise_conflict(), raise_crash(), raise_db_down(), raise_expired() (+21 more)

### Community 10 - "interviews_rag_evals.py"
Cohesion: 0.06
Nodes (78): Local time, as the Langfuse list shows the run's start: the name and the…, run_stamp(), _arm_notes(), ArmSummary, build_sheet(), case_set_problems(), competencies_of(), filter_baseline() (+70 more)

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
Nodes (39): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., _google(), no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env() (+31 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - "test_stream_answer.py"
Cohesion: 0.13
Nodes (22): Save one whole turn in one commit: advance the session, the answer, the…, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+14 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.11
Nodes (39): One case through the same pre-check, score call, write call and template…, run_feedback_case(), case(), Grader, parametrize, Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The…, A fake provider: scores every criterion `value`, quoting the start of each…, _result() (+31 more)

### Community 18 - "test_safe_fetch.py"
Cohesion: 0.15
Nodes (37): Refused before connecting, or the network side failed (DNS, timeout,…, UrlUnreachableError, FakeResolver, fetcher(), public(), parametrize, SSRF-safe fetch (Slice 8b). A fake resolver and a recording MockTransport stand…, Answers from a host -> addresses table; `then` gives a different answer on… (+29 more)

### Community 19 - "interviews_route.py"
Cohesion: 0.08
Nodes (52): alias, AnswerControllerDep, Permission, StrEnum, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), limit_feedback(), Depends (+44 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "LLMResult"
Cohesion: 0.07
Nodes (48): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., LLMError, LLMProvider, LLMResult, Exception, Protocol (+40 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.19
Nodes (27): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, collect(), follow_up_json(), inputs(), kinds(), make_interviewer(), parametrize (+19 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.07
Nodes (74): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists, 2. What it is, 3. When to use it (+66 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (19): assert_one_terminal(), follow_up_json(), message_count(), anyio, fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,… (+11 more)

### Community 31 - "test_transcript.py"
Cohesion: 0.25
Nodes (12): fixture, shape(), started(), test_a_follow_up_is_shown_with_its_kind_and_its_main_questions_number(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question() (+4 more)

### Community 32 - "Slice 8: Embeddings and RAG (split into 8a to 8e)"
Cohesion: 0.33
Nodes (6): 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "RateLimiter"
Cohesion: 0.20
Nodes (11): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, math, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window() (+3 more)

### Community 35 - "interviews_retrieval_service.py"
Cohesion: 0.12
Nodes (17): Embedder, Protocol, The embedding contract features code against, separate from the chat…, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Step, log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, Why vector mode fell back to filter mode (logged as… (+9 more)

### Community 36 - "test_reference_note_context.py"
Cohesion: 0.12
Nodes (24): ContextReport, _log(), NamedTuple, A main-question write of an interview with reference notes: the notes-aware…, WithReferenceNotes, 5. What can go wrong, first_user(), inputs() (+16 more)

### Community 37 - "safe_fetch.py"
Cohesion: 0.07
Nodes (25): _decode(), FetchedPage, FetchError, is_public_address(), BaseTransport, Exception, Response, Fetch a web page whose address a user chose, without letting that user reach… (+17 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.11
Nodes (19): Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional, Goal (+11 more)

### Community 39 - "QuestionTurn"
Cohesion: 0.08
Nodes (28): _counts(), An earlier question as the model would have written it. A follow-up was written…, App data at the end of the last user message; untrusted parts (questions,…, _status_block(), build_interviewer_messages(), main_numbers(), NamedTuple, QuestionTurn (+20 more)

### Community 40 - "test_layers.py"
Cohesion: 0.06
Nodes (40): ast, 5. What can go wrong, Baseline Failures, Changes Made, Deviations from Plan, Implementation: Layered Modules (route -> controller -> service -> repository), Known Issues, Links (+32 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (27): _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card(), _html_metric_row(), _html_table() (+19 more)

### Community 44 - "interviews_job_url_service.py"
Cohesion: 0.07
Nodes (49): JobTextUnreadableError, JobUrlUnreachableError, JobUrlUnreadableError, The job link answered, but no job description could be read from it (not HTML,…, A pasted page held no job description (too little text, or not recognisably a…, Any network-side failure of a job link. One message for every cause, so…, SafeFetcher, JobTextFormat (+41 more)

### Community 45 - "interviews_schema.py"
Cohesion: 0.06
Nodes (62): What a streamed answer turn is doing, sent as `status` events so the candidate…, The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, TurnPhase, answer_out(), AnswerController, _error_event(), _event() (+54 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_evals.py"
Cohesion: 0.10
Nodes (39): check_decision(), check_reply(), load_cases(), main(), pause_for(), Path, Rule checks for one reply. Text checks look at the parsed question, or at the…, The decide reply against the case's label; the injection check reads the raw… (+31 more)

### Community 49 - "test_feedback_contract.py"
Cohesion: 0.16
Nodes (36): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+28 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.05
Nodes (22): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, The reference-note corpus (knowledge-base RAG) and the notes each interview was… (+14 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.11
Nodes (42): InterviewerInputs, Plain values for one interviewer or decide call., Decision, Interviewer, apply_limits(), Deadline, _decision_label(), plan_write() (+34 more)

### Community 52 - "Implementation Steps"
Cohesion: 0.20
Nodes (20): parse_decision_reply(), The decide call suggests; the code still applies the follow-up cap and the time…, _RawDecision, FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect (+12 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.16
Nodes (19): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+11 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "test_job_url.py"
Cohesion: 0.15
Nodes (36): 5. What can go wrong, Open Questions, fail(), error(), import_url(), long_posting(), page(), paste() (+28 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.11
Nodes (46): analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), _call_table(), _cost(), _counts(), _dash() (+38 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.11
Nodes (34): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+26 more)

### Community 59 - "FakeClient"
Cohesion: 0.08
Nodes (14): client(), FakeClient, FakeObservation, propagated(), fixture, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_reports_whether_it_was_sent() (+6 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.07
Nodes (34): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter(), _history_order(), InterviewsRepository, Any, datetime (+26 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.09
Nodes (28): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), Acceptance Criteria, Blockers, Constraints, Edge Cases (+20 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "FakeProvider"
Cohesion: 0.20
Nodes (20): FakeProvider, run_case(), long_case(), noted(), reply(), test_a_passing_case_has_no_hints(), test_a_provider_error_fails_the_case_without_crashing(), test_a_streamed_provider_error_fails_the_case_without_crashing() (+12 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.11
Nodes (35): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, test_a_slow_fake_embedder_waits_at_most_its_budget_then_times_out(), test_fake_embedder_honors_scripted_vectors_and_errors(), test_fake_embedder_is_deterministic_and_records_texts_kinds_and_budgets(), competencies() (+27 more)

### Community 66 - "test_follow_ups.py"
Cohesion: 0.27
Nodes (16): answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries(), test_a_failed_follow_up_write_falls_back_to_the_next_main_bank_question() (+8 more)

### Community 67 - "re"
Cohesion: 0.12
Nodes (14): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, re, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem() (+6 more)

### Community 68 - "InterviewMessage"
Cohesion: 0.10
Nodes (23): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, interviewer_history(), Answered questions with their answers (and the model's note on each), in…, Implementation Steps, test_threads_group_follow_ups_under_their_main_question_in_order() (+15 more)

### Community 69 - "test_answer_llm.py"
Cohesion: 0.10
Nodes (23): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions() (+15 more)

### Community 71 - "test_eval_runs.py"
Cohesion: 0.05
Nodes (56): ExperimentRun, NamedTuple, What a recorded experiment run left behind: its name and link, and the trace of…, _evaluation(), final_line(), git_commit(), notes_fingerprint(), Any (+48 more)

### Community 72 - "decision"
Cohesion: 0.22
Nodes (22): 5. What can go wrong, Deviations from Plan, decision(), labelled_cases(), last_line(), run_decide(), scores_on(), test_a_failed_decision_shows_the_verdict_the_decision_and_the_expected_one() (+14 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.21
Nodes (20): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+12 more)

### Community 74 - "errors.py"
Cohesion: 0.05
Nodes (60): Protocol, The speech-to-text contract features code against, separate from the text-only…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError (+52 more)

### Community 75 - "test_tracing.py"
Cohesion: 0.10
Nodes (23): drain(), Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), _settings(), test_both_keys_build_an_enabled_tracer(), test_call_without_labels_still_gets_a_name(), test_close_on_a_disabled_tracer_does_nothing(), test_complete_records_one_generation_with_full_content_and_usage() (+15 more)

### Community 77 - "test_question_bank.py"
Cohesion: 0.14
Nodes (19): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+11 more)

### Community 78 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "Langfuse Prompt Migration"
Cohesion: 0.13
Nodes (12): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites, 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure (+4 more)

### Community 82 - "EmbeddingKind"
Cohesion: 0.09
Nodes (34): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, A vector of another length than configured. Vectors of different sizes can't be…, GoogleEmbedder, Any (+26 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+6 more)

### Community 84 - "Bundle"
Cohesion: 0.09
Nodes (27): QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from… (+19 more)

### Community 85 - "build_context_manager"
Cohesion: 0.22
Nodes (5): build_context_manager(), FollowUpDecision, FullHistory, The decide call: the current thread in full (it judges the latest answer within…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…

### Community 86 - "LLMTimeoutError"
Cohesion: 0.14
Nodes (13): EmbedCall, NamedTuple, LLMTimeoutError, 1. Why it exists, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+5 more)

### Community 87 - "run_task"
Cohesion: 0.24
Nodes (14): console_number(), The trace id the fake gives a case in the given repeat's run (write and stream…, run_task(), test_a_failed_check_is_scored_false_with_its_detail(), test_a_provider_error_scores_the_case_failed_and_errored_with_the_class(), test_a_write_result_shows_the_reply_and_the_notes_but_no_expected_action(), test_a_write_run_per_repeat_carries_what_produced_it(), test_each_case_shows_what_was_judged() (+6 more)

### Community 88 - "test_reaction_pick.py"
Cohesion: 0.13
Nodes (21): LevelGroup, Reactions are warmer for people early in their career and briefer for…, model_validator, Self, One criterion of the feedback rubric: what it asks, an anchor per score, and…, RubricCriterion, pick_reaction(), Random (+13 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "interviews_feedback_evals.py"
Cohesion: 0.08
Nodes (48): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Check, Band, _band_check(), check_feedback(), criterion_spread(), feedback_dataset_items() (+40 more)

### Community 93 - "clock"
Cohesion: 0.17
Nodes (7): 9. Still open, Known Issues, _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 97 - "llm"
Cohesion: 0.18
Nodes (9): Deviations from Plan, as_v5_text(), llm(), script(), script_score(), script_write(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;… (+1 more)

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

### Community 103 - "test_factory.py"
Cohesion: 0.06
Nodes (46): build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, _model_parameters(), ReasoningEffort (+38 more)

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "StreamedTurn"
Cohesion: 0.18
Nodes (9): parse_sse(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream() (+1 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+1 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.06
Nodes (63): anyio_from_thread, pacer(), wait(), `wait()` sleeps `pause` seconds on every call but the first. Called before each…, _action_and_gap(), _case_inputs(), CaseResult, dataset_items() (+55 more)

### Community 109 - "interviews_feedback_turn.py"
Cohesion: 0.11
Nodes (25): BuiltContext, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, _Attempts, CallUsage (+17 more)

### Community 110 - "main"
Cohesion: 0.10
Nodes (30): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+22 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.10
Nodes (16): Generation, The stream was closed before it finished (client left, or the turn's deadline…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, Baseline Failures, Changes Made, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues (+8 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "QuestionCategory"
Cohesion: 0.08
Nodes (49): JobDescriptionSummary, _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, load_object(), _normalized(), parse_interviewer_reply() (+41 more)

### Community 115 - "run_generation"
Cohesion: 0.08
Nodes (34): ArmInterview, generation_item(), generation_run_scores(), _generation_scores(), Any, Namespace, Score, The active notes, or None after saying how to fix the database or the ingest… (+26 more)

### Community 116 - "audio_container"
Cohesion: 0.35
Nodes (11): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, parametrize, test_a_head_too_short_to_hold_the_signature_is_refused(), test_a_signature_that_does_not_match_the_declared_type_is_refused() (+3 more)

### Community 117 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "run_name"
Cohesion: 0.11
Nodes (18): Unique per command, repeat and arm (Langfuse merges runs that share a name on…, run_name(), Assumptions to verify (external system behaviour), Blockers, Constraints, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional (+10 more)

### Community 121 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 122 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 123 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope (+3 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "Feature: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Résumé upload and candidate profile (Slice 8c), Functional, Goal, Non-Functional (+6 more)

### Community 126 - "How to evaluate an AI feature: from the command to the fix"
Cohesion: 0.13
Nodes (14): 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse, 7. Fix: the smallest change in the right place (+6 more)

### Community 127 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "Implementation: Error Handling"
Cohesion: 0.12
Nodes (17): RequestIdFilter, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions (+9 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 134 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 135 - "The fundamentals"
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+17 more)

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

### Community 140 - "hints_of"
Cohesion: 0.29
Nodes (11): hints_of(), mentions(), The hints on one case's result in Langfuse., test_a_cut_off_reply_hints_at_max_tokens_before_quality(), test_a_provider_error_hints_that_it_is_not_a_quality_problem(), down(), test_a_reply_that_does_not_parse_hints_at_the_format(), test_a_right_action_with_a_different_gap_hints_at_an_ambiguous_label() (+3 more)

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.18
Nodes (27): ingest_corpus(), IngestCounts, IngestError, Exception, NamedTuple, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, NoteChunk, active() (+19 more)

### Community 143 - "ChatMessage"
Cohesion: 0.08
Nodes (31): estimate_tokens(), StrategyOutput, ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, FeedbackScore (+23 more)

### Community 144 - "PageParams"
Cohesion: 0.07
Nodes (37): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewListOut (+29 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "test_turn_budget.py"
Cohesion: 0.18
Nodes (16): Testing Strategy, Baseline Failures, Testing Strategy, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,… (+8 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "Slices in detail"
Cohesion: 0.20
Nodes (10): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 5: Evals (the habit, made repeatable), Slice 6: Feedback and scoring, Slice 7: Eval maturity (trust the judge, catch regressions), Slice: Context management (added after Slice 2) (+2 more)

### Community 151 - "ContextManager"
Cohesion: 0.10
Nodes (50): ContextManager, get_db(), Session, get_answer_controller(), get_answer_service(), Depends, Session, get_feedback_limiter() (+42 more)

### Community 152 - "auth_header"
Cohesion: 0.20
Nodes (10): auth_header(), _header(), client(), fixture, Bearer header for a user; pass role to mint a token whose role claim differs…, POST a setup for `user`; any field can be overridden, or dropped by passing…, start_interview(), _start() (+2 more)

### Community 154 - "Implementation: Job URL (Slice 8b)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: Job URL (Slice 8b), Known Issues, Links, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.13
Nodes (28): embedding_text(), What a chunk is embedded as: its heading, then its text. The heading names the…, corpus(), embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,… (+20 more)

### Community 156 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.27
Nodes (13): main(), _parser(), ArgumentParser, Session, ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1() (+5 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "WindowLedger"
Cohesion: 0.19
Nodes (13): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Task, WindowLedger, 5. What can go wrong, Affected Files & Patterns (+5 more)

### Community 160 - "interviews/conftest.py"
Cohesion: 0.17
Nodes (15): answer(), _answer(), anyio_backend(), _bank_question(), _decision_json(), make_bank_question(), fixture, Builds a reply in the exact shape the decide call must produce. (+7 more)

### Community 161 - "Tracer"
Cohesion: 0.06
Nodes (48): AbstractContextManager, build_tracer(), Any, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Run `task` once per item as one Langfuse experiment run (a dataset run the UI… (+40 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "interviews_answer_service.py"
Cohesion: 0.08
Nodes (49): Context management: the one place that decides what each LLM call sends. The…, The LLM contract every feature codes against: message/result types, typed…, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, What the interview LLM calls send: the tasks and strategies registered with the…, SummaryInputs, Delta, PhaseChanged, What one answer turn of the LLM interviewer hands around: its action, its… (+41 more)

### Community 164 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 165 - "ErrorResponse"
Cohesion: 0.03
Nodes (70): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+62 more)

### Community 166 - ".retrieve"
Cohesion: 0.08
Nodes (27): NamedTuple, UUID, Retrieval, _skipped(), query_text(), What vector mode embeds: the summary, else the job description as entered, else…, 1. Why it exists, 2. What it is (+19 more)

### Community 167 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.11
Nodes (21): ForbiddenError, get_current_user(), Depends, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, check(), require_roles(), check(), AuthServiceDep (+13 more)

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 169 - "test_fallback_pick.py"
Cohesion: 0.21
Nodes (14): pick_fallback_question(), Collection, One unused bank question for `position`, used when the LLM is off or its reply…, fixture_bank(), pick(), fixture, parametrize, test_general_and_role_specific_questions_are_both_eligible() (+6 more)

### Community 170 - "test_select_questions.py"
Cohesion: 0.12
Nodes (29): NotEnoughQuestionsError, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Module Structure & Layer Rules, Overview (+21 more)

### Community 171 - "interviews_feedback.py"
Cohesion: 0.11
Nodes (35): _check_lengths(), Evidence, _has_markup(), _normalized(), parse_write_reply(), BaseModel, NamedTuple, _question_score() (+27 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.15
Nodes (16): Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+8 more)

### Community 174 - "OpenAICompatibleProvider"
Cohesion: 0.12
Nodes (17): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+9 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "test_reply_contract.py"
Cohesion: 0.08
Nodes (43): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split), Acceptance Criteria (+35 more)

### Community 178 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 179 - ".finish_answer"
Cohesion: 0.06
Nodes (36): QuestionNotCurrentError, ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Reload rows a commit expired, so reading their fields later needs no database…, Turn the outcome into rows and save the whole turn in one commit. `reaction` is…, 1. Why it exists, 2. What it is, 3. When to use it (+28 more)

### Community 180 - "JobRole"
Cohesion: 0.07
Nodes (69): InterviewType, JobRole, Level, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, EvalSetup, FeedbackEvalSetup, interview_categories() (+61 more)

### Community 181 - "time"
Cohesion: 0.15
Nodes (9): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send, starlette_types (+1 more)

### Community 182 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 183 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Requirements, User Flow (+1 more)

### Community 184 - "test_user_ids.py"
Cohesion: 0.70
Nodes (4): test_me_returns_the_uuid7_id(), test_registered_user_gets_a_uuid7_id(), test_users_list_ids_are_uuid7_in_creation_order(), _uuid7()

### Community 185 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 186 - "_raise_location"
Cohesion: 0.67
Nodes (3): _raise_location(), (path/to/file.py:42 func)' of the innermost frame, i.e. where the error was…, BaseException

### Community 187 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.09
Nodes (18): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+10 more)

### Community 188 - "Platform and DevOps practice"
Cohesion: 0.25
Nodes (7): CI/CD pipelines with safe rollback, Cloud security, backup and recovery, Containers and Kubernetes troubleshooting, Infrastructure as code in practice, Monitoring, alerting and observability, Platform and DevOps practice, Production problems with no obvious cause

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 191 - "interviews_feedback_controller.py"
Cohesion: 0.11
Nodes (23): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, get_feedback_controller(), FeedbackEvidenceOut (+15 more)

### Community 207 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.16
Nodes (23): corpus(), embedder(), labelled(), lf(), fixture, quiet(), `run_retrieval` as a Langfuse experiment run (langfuse-experiments Step 5;…, Ingests the three notes; returns the vector each note text gets (the embedder… (+15 more)

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

### Community 234 - "_LostClaim"
Cohesion: 0.67
Nodes (3): _LostClaim, Exception, Another request took the row over while this one ran: this one's writes are…

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "_Usage"
Cohesion: 0.67
Nodes (3): The four usage fields of FeedbackCaseResult, so `**_usage(...)` is checked…, _Usage, TypedDict

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

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "interviewer_v7.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 249 - "interviewer_v7_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 250 - "corpus"
Cohesion: 0.67
Nodes (3): corpus(), lf(), fixture

### Community 251 - "fake.py"
Cohesion: 0.12
Nodes (14): anyio, FakeTranscriber, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or…, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, TranscriptionResult, collections (+6 more)

### Community 253 - "Implementation Plan: Résumé upload and candidate profile (Slice 8c)"
Cohesion: 0.20
Nodes (9): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Résumé upload and candidate profile (Slice 8c), Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 255 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 256 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 257 - "test_generation_eval.py"
Cohesion: 0.12
Nodes (37): _post_judgements(), Path, The sheet's third file: setup, then arm, then the Langfuse trace of that arm's…, Read your filled-in sheet, print how often each arm ranked first, then post…, Post every rank (and rating) to its arm's result; returns the line saying what…, run_ranking(), _write_traces(), arm_of() (+29 more)

### Community 258 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 264 - "test_feedback_context.py"
Cohesion: 0.27
Nodes (16): FeedbackThread, One main question with its follow-ups and every answer: what one set of scores…, ThreadTurn, Step 4 of the feedback plan: what the score and write calls send, through the…, score_inputs(), test_an_answer_over_the_cap_is_shortened_and_counted_but_quotes_still_verify(), test_an_interview_over_the_limit_raises_instead_of_dropping_an_answer(), test_closing_tags_inside_untrusted_text_are_neutralised() (+8 more)

### Community 268 - "FakeLangfuse"
Cohesion: 0.08
Nodes (18): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+10 more)

## Knowledge Gaps
- **832 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+827 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1958 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `traces`, `test_generation_eval.py`, `interviews_rag_evals.py`, `FakeLangfuse`, `ChatMessage`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `ContextManager`, `LLMResult`, `test_feedback_endpoint.py`, `interviews_answer_service.py`, `interviews_retrieval_service.py`, `experiments`, `test_evals.py`, `FakeClient`, `test_tracing_routes.py`, `test_eval_runs.py`, `decision`, `errors.py`, `test_tracing.py`, `test_retrieval_eval.py`, `interviews_feedback_evals.py`, `test_factory.py`, `interviews_evals.py`, `interviews_feedback_turn.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `run_generation`, `run_name`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `interviews_constants.py`, `Implementation: Langfuse Tracing`, `decode_token`, `interviews_answer_service.py`, `KnowledgeRepository`, `Implementation Plan: Role-Based Access Control (single JWT)`, `tests/conftest.py`, `errors.py`, `interviews_job_url_service.py`, `interviews_schema.py`, `PageParams`, `interviews_model.py`, `interviews_route.py`, `test_create_interview.py`, `ContextManager`, `InterviewQuestion`, `interviews_feedback_controller.py`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `interviews_constants.py`, `test_generation_eval.py`, `hints_of`, `ChatMessage`, `test_feedback_evals.py`, `test_turn_budget.py`, `interviews_answer_service.py`, `OpenAICompatibleProvider`, `test_evals.py`, `InterviewerInputs`, `.finish_answer`, `test_start_llm.py`, `test_openai_compatible_stream.py`, `FakeProvider`, `test_answer_llm.py`, `errors.py`, `test_tracing.py`, `test_job_description_summary.py`, `LLMTimeoutError`, `interviews_feedback_evals.py`, `test_factory.py`, `interviews_evals.py`, `interviews_feedback_turn.py`, `_Usage`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `QuestionCategory`, `fake.py`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 47 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Are the 28 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 28 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._