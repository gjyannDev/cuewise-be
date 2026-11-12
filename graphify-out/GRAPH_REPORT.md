# Graph Report - cuewise-be  (2026-11-12)

## Corpus Check
- 353 files · ~309,554 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 4788 nodes · 13539 edges · 254 communities (212 shown, 42 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2592 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8302c751`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- LLMServerError
- interviews_answer_service.py
- config.py
- test_interview_report.py
- interviews_route.py
- Cuewise BE — Project Instructions
- interviews_rag_evals.py
- Level
- Role
- run_generation
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- failed
- test_feedback_evals.py
- InterviewQuestion
- test_knowledge_postgres.py
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_feedback_contract.py
- interviews_knowledge_service.py
- Feature: Context Management for the Interview LLM Calls
- test_feedback_context.py
- Completed Steps
- interviews_context.py
- test_interviewer_messages.py
- Feature: LLM as the Interviewer (it asks the questions)
- LLMTimeoutError
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- RateLimiter
- interviews_schema.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- Tracer
- test_feedback_prompts.py
- interviews_model.py
- QuestionCategory
- JobRole
- test_create_interview.py
- test_start_llm.py
- FeedbackStatus
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- tests/conftest.py
- test_tracing_routes.py
- InterviewsRepository
- ConsoleFormatter
- job_description_summary_v2.md
- test_context_controller.py
- FakeEmbedder
- test_fallback_pick.py
- LLMResult
- ._run
- test_reaction_pick.py
- test_eval_runs.py
- InvalidReplyError
- exception_handlers.py
- errors.py
- FakeLangfuse
- interviews_feedback_controller.py
- test_evals.py
- experiments
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- EmbeddingKind
- Embedder
- interviews_feedback.py
- ContextManager
- limit_transcriptions
- Implementation: Langfuse experiments for the interviews evals
- decision
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- RecordingClient
- hint_for
- Langfuse Observability
- interviewer_v3.md
- Implementation: LLM as the Interviewer (it asks the questions)
- test_question_bank.py
- Implementation: Langfuse Tracing
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_factory.py
- test_get_interview.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- llm
- interview_report.py
- Implementation: Eval runs in Langfuse (scores + datasets)
- Feature: Langfuse Tracing
- Langfuse
- main
- test_turn_budget.py
- test_transcript.py
- Implementation: Three New Interview Roles (designer, qa, devops)
- Langfuse Implementation Notes
- interviewer_v5.md
- Feature: Langfuse experiments for the interviews evals
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Implementation Plan: UUID primary keys
- InterviewMessage
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- clock
- LLMRateLimitError
- Feature: Interview History List (backend)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- test_stream_answer.py
- Implementation: Interview History List (backend)
- Judge Calibration
- Langfuse Prompt Migration
- build_usage_report
- The fundamentals
- Langfuse CI/CD
- Prompt Engineering
- Implementation Plan: Context Management for the Interview LLM Calls
- Langfuse Implementation Notes
- pytest
- test_knowledge_ingest.py
- interviews_feedback_evals.py
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- Implementation: Layered Modules (route -> controller -> service -> repository)
- Langfuse CI/CD
- Prompt Engineering
- InterviewFeedback
- interviews_feedback_dependencies.py
- test_generation_eval.py
- Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)
- test_start_reference_notes.py
- Learn: Adding interview roles (designer, qa, devops)
- interviews_knowledge_ingest.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- InterviewType
- Learn: Langfuse experiments for the interviews evals
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_answer_interview.py
- Feature: Role-Based Access Control (single JWT)
- usage_report.py
- ErrorResponse
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- main.py
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Langfuse Prompt Migration
- types.py
- interviews_constants.py
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- OpenAICompatibleProvider
- feedback_score_v1.md
- feedback_write_v1.md
- test_me.py
- interviews_controller.py
- .record_turn
- Slices in detail
- _raise_location
- _eligible
- test_job_description_summary.py
- Learn: Splitting the interviews dependency wiring
- _LostClaim
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- get_feedback_controller
- users_utils.py
- _reset_request_id
- test_retrieval_eval.py
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
- hints_of
- Communication and priorities
- Engineering habits
- Senior judgement
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- Rubric
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- interviews/conftest.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- follow_up_decision_v2.md
- ProviderConfig
- lf

## God Nodes (most connected - your core abstractions)
1. `Tracer` - 112 edges
2. `FakeProvider` - 106 edges
3. `JobRole` - 104 edges
4. `User` - 100 edges
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
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Constraints` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Project Conventions` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py

## Import Cycles
- None detected.

## Communities (254 total, 42 thin omitted)

### Community 0 - "User"
Cohesion: 0.07
Nodes (45): hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), get_service(), Depends, Session (+37 more)

### Community 1 - "LLMServerError"
Cohesion: 0.07
Nodes (32): anyio, DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The first channel's best transcript (blank for silence) and the reported audio… (+24 more)

### Community 2 - "interviews_answer_service.py"
Cohesion: 0.08
Nodes (40): QuestionNotCurrentError, log_stream_summary(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, How a streamed turn felt and ended: time to the first event and to the first…, AnswerService, _elapsed_ms(), AnswerEvent (+32 more)

### Community 3 - "config.py"
Cohesion: 0.11
Nodes (33): InvalidCredentialsError, TokenExpiredError, TokenInvalidError, TokenMissingError, UnauthorizedError, create_token(), decode_token(), Any (+25 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.14
Nodes (50): answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start(), html_for(), parametrize (+42 more)

### Community 5 - "interviews_route.py"
Cohesion: 0.06
Nodes (49): alias, AnswerControllerDep, ForbiddenError, get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check() (+41 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "interviews_rag_evals.py"
Cohesion: 0.05
Nodes (88): Local time, as the Langfuse list shows the run's start: the name and the…, run_stamp(), _arm_notes(), ArmInterview, ArmSummary, build_sheet(), case_set_problems(), competencies_of() (+80 more)

### Community 8 - "Level"
Cohesion: 0.09
Nodes (46): Level, NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, cosine_similarity(), _hash() (+38 more)

### Community 9 - "Role"
Cohesion: 0.08
Nodes (31): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry(), test_unknown_role_has_no_permissions_and_is_logged() (+23 more)

### Community 10 - "run_generation"
Cohesion: 0.07
Nodes (52): ExperimentRun, NamedTuple, Run `task` once per item as one Langfuse experiment run (a dataset run the UI…, What a recorded experiment run left behind: its name and link, and the trace of…, final_line(), The console's last line: which Langfuse runs to open, or why nothing was…, What produced a run, as the strings Langfuse stores: the run explains itself…, run_metadata() (+44 more)

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
Cohesion: 0.10
Nodes (36): _google(), no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, parametrize, Settings built from a clean environment, so a developer's real key never leaks… (+28 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - "failed"
Cohesion: 0.09
Nodes (28): Check, check_decision(), check_reply(), check_streamed_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format., The decide reply against the case's label; the injection check reads the raw… (+20 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.07
Nodes (66): check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for(), feedback_scores_for(), feedback_trace_output(), FeedbackCaseResult, FeedbackEvalCase (+58 more)

### Community 18 - "InterviewQuestion"
Cohesion: 0.09
Nodes (28): QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, InterviewQuestion, A question as it was shown: written by the LLM, or snapshotted from the bank…, Every stored question, grouped by interview in creation order (UUIDv7), for the…, _Interview, The interview as plain values, read before the claim's commit expires the…, Call (+20 more)

### Community 19 - "test_knowledge_postgres.py"
Cohesion: 0.15
Nodes (17): alembic_config, KnowledgeChunk, Store one chunk with its scopes, retiring the row it replaces, in one commit (a…, cuewise-be, Development database (Postgres 18 + pgvector), Reference notes (knowledge-base RAG), alembic_config(), make_chunk() (+9 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.18
Nodes (30): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, Completed Steps, collect(), follow_up_json(), inputs() (+22 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.20
Nodes (31): interview(), post(), parametrize, POST and GET /api/v1/interviews/{id}/feedback: the end-to-end seam for the…, Insert a stored interview: one main question per answer, optional follow-ups…, row(), rows_of(), test_a_completed_interview_gets_scored_written_and_stored() (+23 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.07
Nodes (20): assert_one_terminal(), follow_up_json(), message_count(), anyio, fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,… (+12 more)

### Community 31 - "test_feedback_contract.py"
Cohesion: 0.16
Nodes (36): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+28 more)

### Community 32 - "interviews_knowledge_service.py"
Cohesion: 0.15
Nodes (20): log_embedding_call(), One line per embedding call (ingest or retrieval): metadata only, never the…, _embed(), ingest_corpus(), IngestCounts, IngestError, Exception, NamedTuple (+12 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "test_feedback_context.py"
Cohesion: 0.15
Nodes (26): FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, build_threads(), Evidence, FeedbackThread (+18 more)

### Community 35 - "Completed Steps"
Cohesion: 0.11
Nodes (32): log_retrieval(), Which reference notes an interview got at start: mode, count, scores and the…, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, EligibleChunk, NamedTuple (+24 more)

### Community 36 - "interviews_context.py"
Cohesion: 0.07
Nodes (53): StrategyOutput, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, build_context_manager(), _counts(), FeedbackScore, FeedbackWrite (+45 more)

### Community 37 - "test_interviewer_messages.py"
Cohesion: 0.11
Nodes (25): build_interviewer_messages(), Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the…, The full input for one call (the model has no memory, so the whole interview is…, render_interviewer_prompt(), render_template(), Opt-in: real calls to the configured (primary) LLM provider. Costs real calls,…, test_real_model_writes_a_valid_next_question() (+17 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "LLMTimeoutError"
Cohesion: 0.11
Nodes (15): GoogleEmbedder, Any, BaseTransport, Random, Response, LLMTimeoutError, 1. Why it exists, 3. When to use it (+7 more)

### Community 40 - "test_layers.py"
Cohesion: 0.08
Nodes (34): ast, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 7. What surprised me, 9. Go deeper / Still open, Learn: Layered architecture (route -> controller -> service -> repository) (+26 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.13
Nodes (28): _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card(), _html_metric_row(), _html_table() (+20 more)

### Community 44 - "RateLimiter"
Cohesion: 0.14
Nodes (16): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, get_feedback_limiter(), limit_feedback(), Depends, interviews_feedback, Tests swap in a fresh limiter so counts never leak between them. (+8 more)

### Community 45 - "interviews_schema.py"
Cohesion: 0.06
Nodes (57): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), AnswerController, _error_event(), _event(), _frame(), AnswerEvent (+49 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.07
Nodes (27): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope (+19 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "Tracer"
Cohesion: 0.06
Nodes (41): build_tracer(), Send what is still buffered, then stop the background exporter. Called once at…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, Tracer, client(), drain(), FakeClient, FakeObservation (+33 more)

### Community 49 - "test_feedback_prompts.py"
Cohesion: 0.14
Nodes (19): LevelGroup, Reactions are warmer for people early in their career and briefer for…, interview_categories(), load_rubric(), Path, Read and validate a feedback rubric file; a bad one fails loudly at startup,…, The question categories an interview of this type can hold (mixed: both)., Per-interview constants and the rubric only: no answer or job-description text… (+11 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.12
Nodes (27): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, InterviewSessionChunk (+19 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.08
Nodes (58): One budget for the whole generation, started when the request holds its claim., Decision, Interviewer, apply_limits(), Deadline, _decision_label(), plan_write(), UUID (+50 more)

### Community 52 - "JobRole"
Cohesion: 0.13
Nodes (24): JobRole, load_prompt(), Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt(), render_interviewer_v2_prompt(), parametrize, test_a_valid_note_is_returned_trimmed() (+16 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.17
Nodes (18): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back() (+10 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "FeedbackStatus"
Cohesion: 0.21
Nodes (16): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, 5. What can go wrong, happy(), score_json(), test_a_mixed_interview_scores_each_question_on_its_own_categorys_criteria(), test_a_request_whose_row_was_taken_over_stores_nothing(), test_a_second_post_during_generation_gets_409_and_one_row_exists() (+8 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (27): LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider() (+19 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.10
Nodes (50): group_requests(), The events of each request, oldest request first (the id is on every line of…, analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), _call_table(), _cost() (+42 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "tests/conftest.py"
Cohesion: 0.04
Nodes (55): ConflictError, RequestIdFilter, health_check(), list_users(), PageDep, CurrentUserDep, Baseline Failures, Completed Steps (+47 more)

### Community 60 - "test_tracing_routes.py"
Cohesion: 0.14
Nodes (4): fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 61 - "InterviewsRepository"
Cohesion: 0.07
Nodes (37): HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, InterviewSession, _history_filter(), _history_order(), InterviewsRepository (+29 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.22
Nodes (13): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), sys, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success() (+5 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_context_controller.py"
Cohesion: 0.05
Nodes (71): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 9. Go deeper / Still open, Learn: Follow-up questions (decide / write split) (+63 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.14
Nodes (28): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), parametrize, RetrievalService.retrieve: the vector / filter / skip ladder (knowledge-base-…, A stand-in tracer that records each step's metadata and output. (+20 more)

### Community 66 - "test_fallback_pick.py"
Cohesion: 0.21
Nodes (14): pick_fallback_question(), Collection, One unused bank question for `position`, used when the LLM is off or its reply…, fixture_bank(), pick(), fixture, parametrize, test_general_and_role_specific_questions_are_both_eligible() (+6 more)

### Community 67 - "LLMResult"
Cohesion: 0.05
Nodes (76): BuiltContext, ContextTooLargeError, Exception, Context management: the one place that decides what each LLM call sends. The…, Even with every droppable entry gone the input is over the strategy's limit., LLMError, LLMProvider, LLMResult (+68 more)

### Community 68 - "._run"
Cohesion: 0.39
Nodes (6): _Claim, _Outcome, Any, NamedTuple, Too little to assess (the code's pre-check, or the model's flag): final, with…, How a generation ended, for the trace (metadata only).

### Community 69 - "test_reaction_pick.py"
Cohesion: 0.22
Nodes (14): pick_reaction(), Random, A predefined, neutral acknowledgement for the answer just given; never the same…, Testing Strategy, pick(), parametrize, test_a_one_entry_pool_still_works(), test_every_category_and_level_group_has_a_pool() (+6 more)

### Community 71 - "test_eval_runs.py"
Cohesion: 0.08
Nodes (39): _evaluation(), git_commit(), notes_fingerprint(), Any, Score, What every eval task moved onto Langfuse experiments shares (langfuse-…, Run every case once, in order, as one Langfuse experiment run; whatever the run…, The short commit hash, `-dirty` when the working tree has changes, `unknown`… (+31 more)

### Community 72 - "InvalidReplyError"
Cohesion: 0.07
Nodes (55): _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, load_object(), _normalized(), parse_decision_reply(), parse_interviewer_reply() (+47 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.21
Nodes (20): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+12 more)

### Community 74 - "errors.py"
Cohesion: 0.07
Nodes (46): Protocol, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ErrorBody, FeedbackFailedError (+38 more)

### Community 75 - "FakeLangfuse"
Cohesion: 0.09
Nodes (15): experiment(), parametrize, quiet(), Runs `tracer.run_experiment` with a task that echoes the item id, and records…, test_a_case_removed_from_the_file_is_not_run_although_its_item_stays_in_langfuse(), test_a_langfuse_failure_returns_none_never_raises_and_logs_the_class_only(), test_an_edited_case_updates_its_item_and_the_run_sees_the_new_input(), test_an_experiment_is_a_no_op_returning_none_when_tracing_is_off() (+7 more)

### Community 76 - "interviews_feedback_controller.py"
Cohesion: 0.15
Nodes (17): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, generate_feedback(), get_feedback() (+9 more)

### Community 77 - "test_evals.py"
Cohesion: 0.14
Nodes (40): FakeProvider, run_case(), Reply, console_number(), long_case(), noted(), reply(), run_task() (+32 more)

### Community 78 - "experiments"
Cohesion: 0.50
Nodes (4): case(), experiments(), fixture, A fake Langfuse client behind a Tracer, and a fixed git state so metadata is…

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 82 - "EmbeddingKind"
Cohesion: 0.11
Nodes (31): EmbeddingKind, EmbeddingResult, EmbeddingSizeError, BaseModel, StrEnum, The embedding contract features code against, separate from the chat…, A vector of another length than configured. Vectors of different sizes can't be…, EmbedCall (+23 more)

### Community 83 - "Embedder"
Cohesion: 0.08
Nodes (22): Embedder, Protocol, 8a: Knowledge-base RAG for the question writer, 8b: Job URL, 8c: Résumé upload, 8d: Résumé-aware interview, 8e: Feedback grounding, Slice 8: Embeddings and RAG (split into 8a to 8e) (+14 more)

### Community 84 - "interviews_feedback.py"
Cohesion: 0.12
Nodes (30): _check_lengths(), _has_markup(), _normalized(), parse_write_reply(), BaseModel, _question_score(), QuestionScore, End-of-interview feedback: what the score and write calls must return, and the… (+22 more)

### Community 85 - "ContextManager"
Cohesion: 0.07
Nodes (47): ContextManager, ContextReport, estimate_tokens(), _log(), NamedTuple, Task, Project Conventions, 5. What can go wrong (+39 more)

### Community 86 - "limit_transcriptions"
Cohesion: 0.16
Nodes (10): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, get_transcription_limiter(), limit_transcriptions(), interviews_answer, Tests swap in a fresh limiter so counts never leak between them., Per-user cap on transcriptions, checked before the upload goes anywhere that…, The speech-to-text seam of a test: a scripted transcriber and a fresh per-test… (+2 more)

### Community 87 - "Implementation: Langfuse experiments for the interviews evals"
Cohesion: 0.14
Nodes (13): 13. Phase 2 real runs (yours), Changes Made, Current Step, Implementation: Langfuse experiments for the interviews evals, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 88 - "decision"
Cohesion: 0.25
Nodes (19): Deviations from Plan, decision(), labelled_cases(), The trace id the fake gives a case in the given repeat's run (write and stream…, run_decide(), scores_on(), test_a_failed_decision_shows_the_verdict_the_decision_and_the_expected_one(), test_a_passing_case_says_pass_and_a_label_with_a_gap_shows_it() (+11 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "RecordingClient"
Cohesion: 0.14
Nodes (8): fresh_limiter(), owner(), fixture, Records the trace, its steps (chains) and the code's checks (guardrails) apart,…, Fake wall clock for the claim token and the stale takeover., recording(), RecordingClient, wall()

### Community 93 - "hint_for"
Cohesion: 0.22
Nodes (10): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, inspect, parametrize, Hints for feedback failures: where to look first, shown in Langfuse next to the…, reason_codes(), test_a_rate_limit_hint_says_it_is_not_a_quality_problem(), test_every_other_failure_has_a_hint() (+2 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 97 - "test_question_bank.py"
Cohesion: 0.27
Nodes (12): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, 5. What can go wrong, Test Results, test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), _entry(), parametrize, test_every_role_has_its_own_technical_question_at_every_level() (+4 more)

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
Cohesion: 0.08
Nodes (35): build_embedder(), build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, model_validator, Self (+27 more)

### Community 104 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 105 - "test_answer_llm.py"
Cohesion: 0.05
Nodes (42): 2. What it is, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+34 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+1 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.07
Nodes (55): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, decide_run_scores(), DecisionSummary, EvalCase (+47 more)

### Community 109 - "llm"
Cohesion: 0.15
Nodes (12): Deviations from Plan, as_v5_text(), _decision_json(), llm(), script(), script_decide(), script_score(), script_write() (+4 more)

### Community 110 - "interview_report.py"
Cohesion: 0.10
Nodes (32): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+24 more)

### Community 111 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "main"
Cohesion: 0.18
Nodes (15): load_cases(), main(), Path, last_line(), parametrize, test_a_langfuse_failure_still_runs_every_case_once_and_exits_0(), test_a_langfuse_outage_does_not_change_the_write_run(), test_at_least_ten_shipped_cases_are_labelled_with_both_injections() (+7 more)

### Community 115 - "test_turn_budget.py"
Cohesion: 0.20
Nodes (15): Testing Strategy, Testing Strategy, Baseline Failures, budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result() (+7 more)

### Community 116 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 117 - "Implementation: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Feature: Langfuse experiments for the interviews evals"
Cohesion: 0.14
Nodes (13): Assumptions to verify (external system behaviour), Blockers, Edge Cases, Feature: Langfuse experiments for the interviews evals, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 121 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (14): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview (+6 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "InterviewMessage"
Cohesion: 0.11
Nodes (20): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, test_threads_group_follow_ups_under_their_main_question_in_order(), message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started() (+12 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "clock"
Cohesion: 0.14
Nodes (8): 9. Still open, Known Issues, _make(), _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 126 - "LLMRateLimitError"
Cohesion: 0.11
Nodes (18): LLMRateLimitError, 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+10 more)

### Community 127 - "Feature: Interview History List (backend)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+6 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "test_stream_answer.py"
Cohesion: 0.12
Nodes (23): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+15 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

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

### Community 138 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "pytest"
Cohesion: 0.16
Nodes (9): pytest, parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text(), parametrize, test_request_id_header_sent_exactly_once() (+1 more)

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.24
Nodes (20): active(), chunks(), corpus(), FailingOn, interview(), ingest_corpus: idempotent ingestion of the reference notes (knowledge-base-rag…, Fails on the n-th embed call (1-based), then works again., rows() (+12 more)

### Community 143 - "interviews_feedback_evals.py"
Cohesion: 0.11
Nodes (21): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), feedback_run_scores(), FeedbackEvalQuestion, FeedbackEvalSetup, FeedbackEvalTurn (+13 more)

### Community 144 - "PageParams"
Cohesion: 0.08
Nodes (34): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewListOut (+26 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "Implementation: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Changes Made, Implementation: Layered Modules (route -> controller -> service -> repository), Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "InterviewFeedback"
Cohesion: 0.25
Nodes (8): InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, rows(), test_a_second_post_returns_the_stored_feedback_with_no_llm_call(), test_a_stale_row_without_scores_runs_the_whole_generation(), test_losing_the_insert_race_answers_409(), test_without_an_llm_post_is_503_and_stores_nothing()

### Community 151 - "interviews_feedback_dependencies.py"
Cohesion: 0.12
Nodes (45): get_db(), Session, get_answer_controller(), get_answer_service(), Depends, Session, get_feedback_service(), datetime (+37 more)

### Community 152 - "test_generation_eval.py"
Cohesion: 0.13
Nodes (37): Read your filled-in sheet, print how often each arm ranked first, then post…, run_ranking(), argparse, 5. What can go wrong, arm_of(), corpus(), fill(), generated() (+29 more)

### Community 154 - "Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 8. Check your understanding, 9. Go deeper / Still open, Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback), stored_scores_json(), test_a_stale_row_with_stored_scores_is_taken_over_and_only_the_write_call_runs()

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (25): embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of(), started() (+17 more)

### Community 156 - "Learn: Adding interview roles (designer, qa, devops)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, Learn: Adding interview roles (designer, qa, devops)

### Community 157 - "interviews_knowledge_ingest.py"
Cohesion: 0.23
Nodes (15): main(), _parser(), ArgumentParser, Session, Ingest the reference notes into the database (knowledge-base RAG). uv run…, pathlib, ingest(), Path (+7 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "InterviewType"
Cohesion: 0.20
Nodes (23): NotEnoughQuestionsError, InterviewType, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Trade-offs & Rationale, Implementation Steps, Architecture & Design, _bank() (+15 more)

### Community 160 - "Learn: Langfuse experiments for the interviews evals"
Cohesion: 0.25
Nodes (7): 1. Why it exists, 2. What it is, 3. When to use it, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Langfuse experiments for the interviews evals

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.05
Nodes (40): AbstractContextManager, Generation, Any, The stream was closed before it finished (client left, or the turn's deadline…, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). A stable… (+32 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem, Requirements (+2 more)

### Community 164 - "usage_report.py"
Cohesion: 0.43
Nodes (5): main(), Session, Print stored LLM usage per interview: tokens per question position and per…, test_an_empty_database(), test_reports_stored_questions_grouped_by_interview()

### Community 165 - "ErrorResponse"
Cohesion: 0.05
Nodes (45): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+37 more)

### Community 166 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.14
Nodes (12): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Overview, Project Rules Applied, Ready to Implement (+4 more)

### Community 167 - "main.py"
Cohesion: 0.15
Nodes (9): setup_logging(), Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send (+1 more)

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 170 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 171 - "interviews_constants.py"
Cohesion: 0.14
Nodes (26): AudioContainer, MessageKind, MessageRole, StrEnum, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, Transcript item kinds: a question comes from interview_questions, the other two…, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut (+18 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.09
Nodes (24): Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+16 more)

### Community 174 - "OpenAICompatibleProvider"
Cohesion: 0.12
Nodes (15): _int_or_none(), OpenAICompatibleProvider, Any, AsyncBaseTransport, BaseTransport, Random, ReasoningEffort, Response (+7 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 178 - "interviews_controller.py"
Cohesion: 0.19
Nodes (12): interview_out(), InterviewsController, UUID, Interview lifecycle: request -> InterviewsService, domain result -> response…, InterviewCreateIn, InterviewOut, TranscriptOut, InterviewState (+4 more)

### Community 179 - ".record_turn"
Cohesion: 0.08
Nodes (24): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, Save one whole turn in one commit: advance the session, the answer, the…, Architecture & Design, Deviations from Plan, Deviations Found During Implementation, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps (+16 more)

### Community 180 - "Slices in detail"
Cohesion: 0.20
Nodes (10): Slice 10: Provider fallback chain, Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice 7: Eval maturity (trust the judge, catch regressions), Slice: Context management (added after Slice 2) (+2 more)

### Community 182 - "_raise_location"
Cohesion: 0.67
Nodes (3): _raise_location(), (path/to/file.py:42 func)' of the innermost frame, i.e. where the error was…, BaseException

### Community 183 - "_eligible"
Cohesion: 0.67
Nodes (3): _eligible(), Active chunks scoped to this role (or every role) and this level. Role and…, Select

### Community 184 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 185 - "Learn: Splitting the interviews dependency wiring"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Still open (+1 more)

### Community 186 - "_LostClaim"
Cohesion: 0.67
Nodes (3): _LostClaim, Exception, Another request took the row over while this one ran: this one's writes are…

### Community 187 - "Implementation Plan: Split interviews_dependencies.py by responsibility"
Cohesion: 0.20
Nodes (9): Architecture & Design, Goals (standing in for the spec), Implementation Plan: Split interviews_dependencies.py by responsibility, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

### Community 188 - "Platform and DevOps practice"
Cohesion: 0.25
Nodes (7): CI/CD pipelines with safe rollback, Cloud security, backup and recovery, Containers and Kubernetes troubleshooting, Infrastructure as code in practice, Monitoring, alerting and observability, Platform and DevOps practice, Production problems with no obvious cause

### Community 189 - "interviewer_v6.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 190 - "interviewer_v6_json.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 211 - "test_retrieval_eval.py"
Cohesion: 0.11
Nodes (28): KnowledgeRepository, Session, Remove retired rows no interview points at (with their scopes); returns how…, End the read transaction before a slow call (the embedding), so no connection…, contextvars, A Langfuse client stand-in for experiment runs: datasets, `run_experiment` and…, embedder(), labelled() (+20 more)

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

### Community 234 - "hints_of"
Cohesion: 0.29
Nodes (11): hints_of(), mentions(), The hints on one case's result in Langfuse., test_a_cut_off_reply_hints_at_max_tokens_before_quality(), test_a_provider_error_hints_that_it_is_not_a_quality_problem(), down(), test_a_reply_that_does_not_parse_hints_at_the_format(), test_a_right_action_with_a_different_gap_hints_at_an_ambiguous_label() (+3 more)

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

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

### Community 244 - "Rubric"
Cohesion: 0.29
Nodes (6): model_validator, Self, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, The anchors of the criteria this interview can be scored on, with this level…, render_rubric()

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "interviews/conftest.py"
Cohesion: 0.09
Nodes (27): BankQuestion, One entry of the hand-written question bank file., answer(), _answer(), anyio_backend(), _bank_question(), make_bank_question(), parse_sse() (+19 more)

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 251 - "follow_up_decision_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 260 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 268 - "lf"
Cohesion: 0.67
Nodes (3): lf(), fixture, A fake Langfuse client and a fixed git state (feedback runs as a Langfuse…

## Knowledge Gaps
- **784 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+779 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1840 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **42 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `LLMServerError`, `interviews_answer_service.py`, `interviews_rag_evals.py`, `run_generation`, `interviews_feedback_evals.py`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `interviews_feedback_dependencies.py`, `test_generation_eval.py`, `test_feedback_endpoint.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Completed Steps`, `interviews_context.py`, `test_tracing_routes.py`, `InterviewsRepository`, `LLMResult`, `test_eval_runs.py`, `errors.py`, `FakeLangfuse`, `test_evals.py`, `experiments`, `test_retrieval_eval.py`, `RecordingClient`, `test_factory.py`, `interviews_evals.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `main`, `Feature: Langfuse experiments for the interviews evals`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Why does `JobRole` connect `JobRole` to `interviews_answer_service.py`, `interviews_rag_evals.py`, `Level`, `pytest`, `interviews_feedback_evals.py`, `InterviewQuestion`, `test_stream_turn.py`, `Learn: Adding interview roles (designer, qa, devops)`, `test_context_strategies.py`, `InterviewType`, `test_feedback_context.py`, `interviews_context.py`, `test_interviewer_messages.py`, `Implementation Plan: Three New Interview Roles (designer, qa, devops)`, `interviews_constants.py`, `interviews_schema.py`, `test_llm_settings_default_to_off_with_documented_limits`, `test_transcribe.py`, `test_feedback_prompts.py`, `interviews_controller.py`, `InterviewsRepository`, `test_fallback_pick.py`, `LLMResult`, `InvalidReplyError`, `errors.py`, `Embedder`, `test_retrieval_eval.py`, `ContextManager`, `test_question_bank.py`, `interviews_evals.py`, `interviews/conftest.py`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `interviews_answer_service.py`, `config.py`, `interviews_route.py`, `Role`, `PageParams`, `test_knowledge_postgres.py`, `interviews_feedback_dependencies.py`, `RateLimiter`, `interviews_schema.py`, `interviews_model.py`, `interviews_controller.py`, `test_create_interview.py`, `tests/conftest.py`, `InterviewsRepository`, `LLMResult`, `errors.py`, `interviews_feedback_controller.py`, `limit_transcriptions`, `Implementation: Langfuse Tracing`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Tracer` (e.g. with `build_provider()` and `ChatMessage`) actually correct?**
  _`Tracer` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 64 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 64 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 42 INFERRED edges - model-reasoned connections that need verification._