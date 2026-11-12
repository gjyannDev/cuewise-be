# Graph Report - cuewise-be  (2026-11-11)

## Corpus Check
- 343 files · ~286,367 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 4520 nodes · 12637 edges · 263 communities (222 shown, 41 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 2371 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3bd96fbe`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- auth_service.py
- LLMTimeoutError
- TurnContext
- decode_token
- test_interview_report.py
- interviews_route.py
- Cuewise BE — Project Instructions
- test_rag_evals.py
- interviews_knowledge_utils.py
- test_guards.py
- Implementation Steps
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- StrategyOutput
- test_feedback_evals.py
- QuestionKind
- cuewise-be
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_feedback_contract.py
- re
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- interviews_rag_evals.py
- QuestionTurn
- test_reply_contract.py
- Feature: LLM as the Interviewer (it asks the questions)
- interviews_constants.py
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- interviews_repository.py
- interviews_schema.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- test_feedback_prompts.py
- interviews_model.py
- InterviewerInputs
- JobRole
- test_create_interview.py
- test_start_llm.py
- Implementation Steps
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- InterviewType
- test_tracing_routes.py
- InterviewQuestion
- ConsoleFormatter
- job_description_summary_v2.md
- test_follow_ups.py
- FakeEmbedder
- test_context.py
- QuestionCategory
- ._run
- AnswerOut
- Any
- test_streamed_reply.py
- exception_handlers.py
- errors.py
- RateLimiter
- interviews_feedback_controller.py
- run_case
- RecordingClient
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- EmbeddingKind
- Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)
- interviews_feedback.py
- test_reference_note_context.py
- build_context_manager
- Feature: Follow-up Questions (decide / write split)
- Implementation: Langfuse Tracing
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- FakeClient
- hint_for
- Langfuse Observability
- interviewer_v3.md
- Implementation: LLM as the Interviewer (it asks the questions)
- fixture
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation: Split interviews_dependencies.py by responsibility
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_factory.py
- tests/conftest.py
- test_answer_llm.py
- interviews_utils.py
- Langfuse Dataset Construction
- interviews_evals.py
- llm
- interview_report.py
- Learn: Knowledge-base RAG for the question writer (Slice 8a)
- Feature: Langfuse Tracing
- Langfuse
- test_evals.py
- Implementation Steps
- test_transcript.py
- LLMResult
- Langfuse Implementation Notes
- interviewer_v5.md
- OpenAICompatibleProvider
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- Implementation Plan: UUID primary keys
- InterviewMessage
- Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)
- test_turn_budget.py
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
- Settings
- Langfuse Implementation Notes
- test_get_interview.py
- test_knowledge_ingest.py
- interviews_feedback_evals.py
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- test_context_controller.py
- ContextManager
- failed
- LLMServerError
- test_start_reference_notes.py
- WriteText
- test_knowledge_ingest_cli.py
- Implementation: Interview Feedback and Scoring (Slice 6)
- json
- Learn: Layered architecture (route -> controller -> service -> repository)
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_answer_interview.py
- parse_log
- test_list_users.py
- ErrorResponse
- Implementation Plan: Three New Interview Roles (designer, qa, devops)
- RequestContextMiddleware
- Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)
- Implementation Plan: Layered Modules (route -> controller -> service -> repository)
- types.py
- pytest
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- ChatMessage
- feedback_score_v1.md
- feedback_write_v1.md
- test_me.py
- BaseModel
- WindowLedger
- Implementation Plan: Langfuse Tracing
- User
- Langfuse CLI Reference
- Feature: Layered Modules (route -> controller -> service -> repository)
- test_job_description_summary.py
- StreamedTurn
- Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection
- Implementation Plan: Split interviews_dependencies.py by responsibility
- Platform and DevOps practice
- interviewer_v6.md
- interviewer_v6_json.md
- Langfuse
- users_utils.py
- _reset_request_id
- Generation
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
- _Stt
- Communication and priorities
- Engineering habits
- Senior judgement
- Affected Files & Patterns
- Design fundamentals
- DevOps fundamentals
- Test strategy and quality leadership
- Quality assurance basics
- Writing a knowledge-base note (guide)
- RubricCriterion
- Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)
- fixture
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- Implementation Plan: Role-Based Access Control (single JWT)
- TranscriptionResult
- build_tracer
- RecordingClient
- stream_answer
- traces
- client
- ContextReport
- 2. Langfuse Documentation
- Steps
- .__init__
- _LostClaim
- ProviderConfig
- started

## God Nodes (most connected - your core abstractions)
1. `JobRole` - 102 edges
2. `User` - 100 edges
3. `FakeProvider` - 96 edges
4. `LLMResult` - 91 edges
5. `InterviewQuestion` - 88 edges
6. `Level` - 87 edges
7. `InterviewType` - 87 edges
8. `Tracer` - 86 edges
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

## Communities (263 total, 41 thin omitted)

### Community 0 - "auth_service.py"
Cohesion: 0.11
Nodes (28): hash_password(), verify_password(), AuthController, Request -> service call, domain result -> response schema., get_controller(), login(), me(), register() (+20 more)

### Community 1 - "LLMTimeoutError"
Cohesion: 0.08
Nodes (18): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, The first channel's best transcript (blank for silence) and the reported audio…, EmbedCall, NamedTuple (+10 more)

### Community 2 - "TurnContext"
Cohesion: 0.11
Nodes (18): QuestionNotCurrentError, AnswerController, UUID, The checks and reads before the stream opens (sync DB work: the route runs it…, AnswerIn, _elapsed_ms(), AnswerEvent, UUID (+10 more)

### Community 3 - "decode_token"
Cohesion: 0.14
Nodes (27): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Implementation Steps (+19 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.13
Nodes (54): analysis(), answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start(), html_for() (+46 more)

### Community 5 - "interviews_route.py"
Cohesion: 0.07
Nodes (48): alias, AnswerControllerDep, ForbiddenError, get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check() (+40 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "test_rag_evals.py"
Cohesion: 0.08
Nodes (44): ArmSummary, build_sheet(), case_set_problems(), competencies_of(), BaseModel, Exception, NamedTuple, _ranking() (+36 more)

### Community 8 - "interviews_knowledge_utils.py"
Cohesion: 0.09
Nodes (45): NoteSource, Where a note's content came from. A model grounding a model on its own drafts…, _check_hidden(), Corpus, CorpusError, _hash(), _listed(), load_corpus() (+37 more)

### Community 9 - "test_guards.py"
Cohesion: 0.13
Nodes (20): CurrentUserDep, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired() (+12 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.16
Nodes (24): parse_decision_reply(), BaseModel, The decide call suggests; the code still applies the follow-up cap and the time…, A follow-up carries no category: it inherits its main question's, so the model…, _RawDecision, _RawFollowUp, FollowUpAction, FollowUpGap (+16 more)

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
Nodes (30): os, _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored() (+22 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - "StrategyOutput"
Cohesion: 0.09
Nodes (18): StrategyOutput, _counts(), FeedbackWrite, FollowUpDecision, FullHistory, JobDescriptionSummary, An earlier question as the model would have written it. A follow-up was written…, The decide call: the current thread in full (it judges the latest answer within… (+10 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.09
Nodes (36): One case through the same pre-check, score call, write call and template…, run_feedback_case(), case(), Grader, parametrize, Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The…, Records traces (spans), steps (chains) and checks (guardrails) apart, like the…, A fake provider: scores every criterion `value`, quoting the start of each… (+28 more)

### Community 18 - "QuestionKind"
Cohesion: 0.08
Nodes (34): QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that…, Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from… (+26 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.16
Nodes (34): FakeStream, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one…, Reset, What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase (+26 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.07
Nodes (73): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists, 2. What it is, 3. When to use it (+65 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (36): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+28 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.07
Nodes (21): assert_one_terminal(), follow_up_json(), message_count(), anyio, fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,… (+13 more)

### Community 31 - "test_feedback_contract.py"
Cohesion: 0.18
Nodes (33): assess_evidence(), compute_overall(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The mean of every criterion score of every main question, rounded half up to…, The pre-check, before any LLM call: enough main questions have a real answer to…, 6. Try it yourself, parametrize (+25 more)

### Community 32 - "re"
Cohesion: 0.14
Nodes (16): LevelGroup, Reactions are warmer for people early in their career and briefer for…, re, pick(), parametrize, test_a_one_entry_pool_still_works(), test_every_category_and_level_group_has_a_pool(), test_final_answer_uses_the_closing_pool() (+8 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 35 - "interviews_rag_evals.py"
Cohesion: 0.06
Nodes (57): Embedder, Protocol, Why vector mode fell back to filter mode (logged as…, Why an interview has no reference notes at all (logged as…, RetrievalDegrade, RetrievalSkip, _eligible(), EligibleChunk (+49 more)

### Community 36 - "QuestionTurn"
Cohesion: 0.10
Nodes (36): build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the… (+28 more)

### Community 37 - "test_reply_contract.py"
Cohesion: 0.23
Nodes (22): follow_up(), parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_follow_up_in_a_behavioral_only_interview_keeps_the_behavioral_category(), test_a_follow_up_is_accepted_without_a_category_and_inherits_the_parents() (+14 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "interviews_constants.py"
Cohesion: 0.08
Nodes (44): anyio, Context management: the one place that decides what each LLM call sends. The…, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The embedding contract features code against, separate from the chat…, Test doubles for LLMProvider, Transcriber and Embedder: scripted replies or…, OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, The LLM contract every feature codes against: message/result types, typed…, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`… (+36 more)

### Community 40 - "test_layers.py"
Cohesion: 0.06
Nodes (41): ast, 5. What can go wrong, Blockers & Resolutions, Baseline Failures, Changes Made, Deviations from Plan, Implementation: Layered Modules (route -> controller -> service -> repository), Known Issues (+33 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (26): _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card(), _html_metric_row(), _html_table() (+18 more)

### Community 44 - "interviews_repository.py"
Cohesion: 0.12
Nodes (25): HistorySortColumn, StrEnum, QuestionSource, The history columns GET /interviews sorts by; the values are the response's…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, SessionStatus, SortDirection, InterviewsController (+17 more)

### Community 45 - "interviews_schema.py"
Cohesion: 0.15
Nodes (26): answer_out(), _frame(), AnswerEvent, Answer turns: request -> AnswerService, domain result -> AnswerOut, and the…, _reaction_out(), question_out(), QuestionDeltaOut, The next chunk of the question being written; the client appends it to the text… (+18 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.14
Nodes (12): code(), parametrize, test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long(), test_a_session_not_in_progress_is_409(), test_an_empty_file_is_no_speech(), test_every_vendor_failure_is_a_generic_503() (+4 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.11
Nodes (20): drain(), Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), test_call_without_labels_still_gets_a_name(), test_close_on_a_disabled_tracer_does_nothing(), test_complete_records_one_generation_with_full_content_and_usage(), test_disabled_tracer_is_a_pass_through(), test_failed_call_is_marked_error_and_the_same_exception_is_raised() (+12 more)

### Community 49 - "test_feedback_prompts.py"
Cohesion: 0.12
Nodes (22): The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric, interview_categories(), load_rubric(), Path, Read and validate a feedback rubric file; a bad one fails loudly at startup,…, The question categories an interview of this type can hold (mixed: both)., The anchors of the criteria this interview can be scored on, with this level… (+14 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.04
Nodes (43): alembic_config, Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+35 more)

### Community 51 - "InterviewerInputs"
Cohesion: 0.08
Nodes (44): InterviewerInputs, Plain values for one interviewer or decide call., Interviewer, UUID, The same turn as `answer_turn` (same decide, limits and fallbacks), telling the…, ActionKnown, PhaseChanged, NamedTuple (+36 more)

### Community 52 - "JobRole"
Cohesion: 0.17
Nodes (26): JobRole, Level, EvalSetup, FeedbackEvalSetup, load_prompt(), Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt() (+18 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.16
Nodes (19): parametrize, _question_count(), _questions(), _sessions(), test_a_new_role_is_returned_by_get_and_list(), test_a_new_role_starts_a_technical_interview_from_the_shipped_bank(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+11 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "Implementation Steps"
Cohesion: 0.19
Nodes (16): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, _error_event(), _event(), BaseModel, NamedTuple, One event of a streamed turn as the controller yields it; the route encodes it…, StreamEventOut (+8 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.12
Nodes (27): LLMBadResponseError, A 200 whose body is unusable (not JSON, no choices, blank text). Not transient,…, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider() (+19 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.13
Nodes (40): analyze_interview(), analyze_rollup(), _avg(), _call_table(), _cost(), _counts(), _dash(), _effectiveness() (+32 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "InterviewType"
Cohesion: 0.31
Nodes (17): InterviewType, _bank(), parametrize, _q(), _select(), test_general_question_is_eligible_for_every_role(), test_mixed_even_count_is_an_exact_split(), test_mixed_short_on_one_type_is_rejected_without_rebalancing() (+9 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.09
Nodes (26): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Any, datetime, Session, UUID (+18 more)

### Community 62 - "ConsoleFormatter"
Cohesion: 0.20
Nodes (13): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), LogRecord, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success() (+5 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_follow_ups.py"
Cohesion: 0.13
Nodes (28): apply_limits(), The code's say over the model's: returns the action and why it overrode the…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+20 more)

### Community 65 - "FakeEmbedder"
Cohesion: 0.16
Nodes (30): FakeEmbedder, Deterministic vectors (seeded by each text), or scripted ones per text so a…, How an interview's reference notes were picked: ranked by meaning against the…, RetrievalMode, competencies(), corpus(), note_text(), fixture (+22 more)

### Community 66 - "test_context.py"
Cohesion: 0.19
Nodes (13): Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default(), test_a_strategy_without_a_limit_is_never_trimmed() (+5 more)

### Community 67 - "QuestionCategory"
Cohesion: 0.07
Nodes (63): ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., decide(), UUID, The decide step of an answer turn: the model suggests following up or moving…, At most two attempts within the decide cap; any failure means "next_question"…, _check_question() (+55 more)

### Community 68 - "._run"
Cohesion: 0.31
Nodes (8): _Claim, _Interview, _Outcome, Any, NamedTuple, Too little to assess (the code's pre-check, or the model's flag): final, with…, The interview as plain values, read before the claim's commit expires the…, How a generation ended, for the trace (metadata only).

### Community 69 - "AnswerOut"
Cohesion: 0.15
Nodes (14): AnswerOut, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Functional, Goal (+6 more)

### Community 71 - "Any"
Cohesion: 0.13
Nodes (14): AbstractContextManager, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Set the output of the trace being built (call it inside `trace()`): what a…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, Run an SDK call; on any failure log what failed (not why: the message could…, _safe() (+6 more)

### Community 72 - "test_streamed_reply.py"
Cohesion: 0.18
Nodes (17): interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), read(), parse(), parametrize, interviewer_v5's streamed reply: a `CATEGORY:` header line (next-question mode…, test_a_header_split_across_chunks_is_read_once_its_line_ends(), test_a_long_first_line_is_no_header_without_waiting_for_its_end() (+9 more)

### Community 73 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 74 - "errors.py"
Cohesion: 0.09
Nodes (39): Protocol, Transcriber, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody (+31 more)

### Community 75 - "RateLimiter"
Cohesion: 0.20
Nodes (11): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, math, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window() (+3 more)

### Community 76 - "interviews_feedback_controller.py"
Cohesion: 0.21
Nodes (12): feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or…, get_feedback_controller(), FeedbackEvidenceOut (+4 more)

### Community 77 - "run_case"
Cohesion: 0.26
Nodes (15): run_case(), long_case(), noted(), reply(), test_a_v3_window_reply_must_carry_a_note_when_there_is_an_answer(), test_an_unusable_summary_falls_back_to_the_original(), test_finish_length_is_recorded_and_counted(), test_no_note_check_for_full_history_or_the_first_question() (+7 more)

### Community 78 - "RecordingClient"
Cohesion: 0.12
Nodes (7): case(), langfuse(), fixture, A Langfuse client stand-in. Entering a trace sets `current_trace`, like the SDK…, RecordingClient, test_a_failed_dataset_upsert_still_scores_the_cases(), test_a_langfuse_outage_does_not_change_the_run()

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 82 - "EmbeddingKind"
Cohesion: 0.16
Nodes (26): EmbeddingKind, EmbeddingSizeError, StrEnum, A vector of another length than configured. Vectors of different sizes can't be…, LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., Clock, make_embedder() (+18 more)

### Community 83 - "Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Assumptions to verify, Blockers, Edge Cases, Feature: Knowledge-Base RAG for the Question Writer (Slice 8a), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "interviews_feedback.py"
Cohesion: 0.09
Nodes (46): estimate_tokens(), FeedbackScore, The score call: every thread whole, nothing droppable. Over its own limit it…, Evidence, FeedbackThread, _has_markup(), _normalized(), BaseModel (+38 more)

### Community 85 - "test_reference_note_context.py"
Cohesion: 0.27
Nodes (13): 5. What can go wrong, first_user(), inputs(), _max_note(), parametrize, Reference notes in the question writer's input (knowledge-base-rag Step 9;…, test_a_main_question_write_gets_the_notes_after_the_job_description_in_rank_order(), test_tags_inside_a_note_are_neutralised() (+5 more)

### Community 86 - "build_context_manager"
Cohesion: 0.11
Nodes (19): build_context_manager(), `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, A running note is optional model output about the latest answer; it is sent…, The job-description summary replaces the original on every later call, so it…, validate_note(), validate_summary(), Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls (+11 more)

### Community 87 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 88 - "Implementation: Langfuse Tracing"
Cohesion: 0.14
Nodes (12): Baseline Failures, Commit message suggestion, Completed Steps, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+4 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "FakeClient"
Cohesion: 0.11
Nodes (8): FakeClient, FakeObservation, test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises(), test_steps_and_checks_are_no_ops_when_off_and_never_raise_when_langfuse_fails(), test_trace_with_a_broken_sdk_still_runs_the_body_and_keeps_its_exception(), test_upsert_dataset_reports_false_when_off_or_failing_and_never_raises()

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

### Community 97 - "fixture"
Cohesion: 0.29
Nodes (7): no_embedding_env(), no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 98 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.17
Nodes (11): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

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
Cohesion: 0.13
Nodes (23): build_embedder(), build_transcriber(), Speech-to-text for voice answers; None without a key. Never traced: audio and…, Embeddings for reference-note retrieval; None without the Google key (notes are…, setup_logging(), lifespan(), FastAPI, Affected Files & Patterns (+15 more)

### Community 104 - "tests/conftest.py"
Cohesion: 0.05
Nodes (45): RequestIdFilter, health_check(), Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links (+37 more)

### Community 105 - "test_answer_llm.py"
Cohesion: 0.10
Nodes (25): 2. What it is, Learning Log (`learnings.md`), 5. What can go wrong, Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages() (+17 more)

### Community 106 - "interviews_utils.py"
Cohesion: 0.09
Nodes (31): NotEnoughQuestionsError, pick_fallback_question(), pick_reaction(), Collection, Random, One unused bank question for `position`, used when the LLM is off or its reply…, A predefined, neutral acknowledgement for the answer just given; never the same…, Pick `count` distinct questions for the setup, in interview order. The single… (+23 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.08
Nodes (56): anyio_from_thread, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, dataset_items(), dataset_name(), DecisionSummary (+48 more)

### Community 109 - "llm"
Cohesion: 0.18
Nodes (9): Skills Consulted, as_v5_text(), llm(), script(), script_score(), script_write(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;… (+1 more)

### Community 110 - "interview_report.py"
Cohesion: 0.14
Nodes (20): html_target(), main(), Path, Session, UUID, Print the cost, effectiveness and efficiency of the interviewer. Numbers and…, A path ending in .html is the file; anything else is a folder, and the file is…, The rotated log first, so the lines stay in time order. (+12 more)

### Community 111 - "Learn: Knowledge-base RAG for the question writer (Slice 8a)"
Cohesion: 0.22
Nodes (8): 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open, Learn: Knowledge-base RAG for the question writer (Slice 8a)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.17
Nodes (12): 1. Langfuse API via CLI, 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Core Principles, Credentials, Detailed CLI Reference (+4 more)

### Community 114 - "test_evals.py"
Cohesion: 0.12
Nodes (47): FakeProvider, load_cases(), Path, decision(), hints_of(), labelled(), mentions(), run_main() (+39 more)

### Community 115 - "Implementation Steps"
Cohesion: 0.15
Nodes (12): Affected Files & Patterns, Implementation Steps, Phase A: plumbing and progress events, Phase B: streaming the question text, Step 10: `OpenAICompatibleProvider.stream`, Step 14: The event loop stays free, Step 15: Evals, Step 16: Measure, document, finish (+4 more)

### Community 116 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 117 - "LLMResult"
Cohesion: 0.05
Nodes (42): BuiltContext, LLMError, LLMProvider, LLMResult, Exception, Protocol, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined… (+34 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "OpenAICompatibleProvider"
Cohesion: 0.13
Nodes (16): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, _int_or_none(), OpenAICompatibleProvider, Any, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final… (+8 more)

### Community 121 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "InterviewMessage"
Cohesion: 0.10
Nodes (24): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, MessageRole, InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, build_transcript(), The chat as the user saw it: each question, then its answer and reaction when…, test_threads_group_follow_ups_under_their_main_question_in_order() (+16 more)

### Community 124 - "Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.15
Nodes (12): 11. Corpus review (your gate), then 12. Real runs, Baseline Failures, Changes Made, Current Step, Implementation: Knowledge-Base RAG for the Question Writer (Slice 8a), Known Issues, Links, Open Questions (+4 more)

### Community 125 - "test_turn_budget.py"
Cohesion: 0.07
Nodes (29): 9. Still open, Changes Made, Completed Steps, Deviations from Plan, Implementation: Three New Interview Roles (designer, qa, devops), Known Issues, Links, Open Questions (+21 more)

### Community 126 - "LLMRateLimitError"
Cohesion: 0.12
Nodes (16): LLMRateLimitError, 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+8 more)

### Community 127 - "Feature: Interview History List (backend)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+5 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "test_stream_answer.py"
Cohesion: 0.11
Nodes (24): Save one whole turn in one commit: advance the session, the answer, the…, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+16 more)

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
Cohesion: 0.20
Nodes (16): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, main(), Session, Print stored LLM usage per interview: tokens per question position and per…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind() (+8 more)

### Community 135 - "The fundamentals"
Cohesion: 0.05
Nodes (42): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+34 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "Settings"
Cohesion: 0.20
Nodes (6): model_validator, Self, Settings, BaseSettings, Step 0: Rename the provider to a vendor-neutral name, field_validator

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 142 - "test_knowledge_ingest.py"
Cohesion: 0.16
Nodes (30): _embed(), ingest_corpus(), IngestError, Exception, Ingestion stopped; the message names the chunk (or the setting) and the reason,…, main(), _parser(), ArgumentParser (+22 more)

### Community 143 - "interviews_feedback_evals.py"
Cohesion: 0.09
Nodes (43): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), check_feedback(), criterion_spread(), feedback_dataset_items(), feedback_hints_for() (+35 more)

### Community 144 - "PageParams"
Cohesion: 0.08
Nodes (36): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, UsersController (+28 more)

### Community 145 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 146 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 147 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 148 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 149 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 150 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 151 - "ContextManager"
Cohesion: 0.09
Nodes (51): ContextManager, get_db(), Session, get_answer_controller(), get_answer_service(), Depends, Session, get_feedback_limiter() (+43 more)

### Community 152 - "failed"
Cohesion: 0.08
Nodes (32): Check, check_decision(), check_reply(), check_streamed_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format., The decide reply against the case's label; the injection check reads the raw… (+24 more)

### Community 154 - "LLMServerError"
Cohesion: 0.09
Nodes (22): EmbeddingResult, BaseModel, GoogleEmbedder, Any, BaseTransport, Random, Response, Gemini embeddings through Google's native `batchEmbedContents` endpoint, over… (+14 more)

### Community 155 - "test_start_reference_notes.py"
Cohesion: 0.14
Nodes (26): corpus(), embedder(), has_notes(), fixture, UUID, Reference notes at interview start: retrieved, stored with the interview,…, retrieval_lines(), session_of() (+18 more)

### Community 156 - "WriteText"
Cohesion: 0.27
Nodes (9): _check_lengths(), parse_write_reply(), The labelled text the write call is asked for (the parser reads it back…, The write call's text, slot by slot: every section once and in order, list…, _slots(), WriteText, test_a_valid_write_reply_is_parsed_into_slots(), test_blank_lines_and_a_wrapped_summary_are_accepted() (+1 more)

### Community 157 - "test_knowledge_ingest_cli.py"
Cohesion: 0.42
Nodes (9): ingest(), Path, The ingest command: python -m…, test_a_failure_partway_names_the_chunk_and_exits_1(), test_an_invalid_note_names_the_file_writes_nothing_and_exits_1(), test_it_prints_the_counts_and_exits_0(), test_warnings_are_printed_without_note_text(), test_without_the_google_key_it_says_what_to_set_and_exits_1() (+1 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.12
Nodes (15): 9. Review gate (user), Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links (+7 more)

### Community 159 - "json"
Cohesion: 0.13
Nodes (20): load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+12 more)

### Community 160 - "Learn: Layered architecture (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (9): Reload rows a commit expired, so reading their fields later needs no database…, 1. Why it exists, 2. What it is, 3. When to use it, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.10
Nodes (20): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Architecture & Design, Decisions (grilled with the user), Deviations from the first version of this plan (found during /implement), Implementation Plan: Eval runs in Langfuse (scores + datasets) (+12 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "parse_log"
Cohesion: 0.29
Nodes (10): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), lines_of(), Collapse the table padding so assertions don't depend on column widths., rollup(), rollup_analysis(), squash() (+2 more)

### Community 164 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 165 - "ErrorResponse"
Cohesion: 0.04
Nodes (56): ErrorResponse, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied, Ready to Implement (+48 more)

### Community 166 - "Implementation Plan: Three New Interview Roles (designer, qa, devops)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Blockers & Resolutions, Goals and edge cases (stand-in for the spec), Implementation Plan: Three New Interview Roles (designer, qa, devops), Implementation Steps, Overview, Project Rules Applied, Ready to Implement (+3 more)

### Community 167 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 168 - "Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Knowledge-Base RAG for the Question Writer (Slice 8a), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "Implementation Plan: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.13
Nodes (14): MessageKind, Transcript item kinds: a question comes from interview_questions, the other two…, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut, Affected Files & Patterns, Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview (+6 more)

### Community 170 - "types.py"
Cohesion: 0.18
Nodes (8): downgrade(), Downgrade schema. The `vector` extension stays: other database objects may use…, portable_vector(), Column types shared by every module., A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list…, pgvector_sqlalchemy, sqlalchemy_types, TypeEngine

### Community 171 - "pytest"
Cohesion: 0.13
Nodes (20): AudioContainer, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't…, pytest, parametrize, test_each_role_list_includes_the_shared_terms_once() (+12 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.15
Nodes (16): Baseline Failures, 1. Where 8a stands, 2. Open work on 8a (yours, in this order), 3. Commands, 4. Environment gotchas, 5. Test baseline to compare against, 7. Reference material, Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL) (+8 more)

### Community 174 - "ChatMessage"
Cohesion: 0.17
Nodes (12): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:…, Step 11: `FakeProvider.stream`, Reply, test_a_second_task_with_its_own_strategy_leaves_the_first_alone() (+4 more)

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 178 - "BaseModel"
Cohesion: 0.33
Nodes (9): interview_out(), InterviewCreateIn, InterviewOut, BaseModel, QuestionOut, SessionOut, TranscriptOut, Implementation Steps (+1 more)

### Community 179 - "WindowLedger"
Cohesion: 0.11
Nodes (21): Task, A main-question write of an interview with reference notes: the notes-aware…, WindowLedger, WithReferenceNotes, Affected Files & Patterns, Blockers & Resolutions, Deviations Found During Implementation, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4) (+13 more)

### Community 180 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 181 - "User"
Cohesion: 0.07
Nodes (44): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, get_service(), Depends, Session (+36 more)

### Community 182 - "Langfuse CLI Reference"
Cohesion: 0.20
Nodes (7): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options

### Community 183 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.20
Nodes (9): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Requirements, User Flow (+1 more)

### Community 184 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 185 - "StreamedTurn"
Cohesion: 0.25
Nodes (6): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

### Community 186 - "Learn: The LLM as the interviewer (Slice 2): prompts, structured output, injection"
Cohesion: 0.20
Nodes (9): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 6. Try it yourself, 7. What surprised me, 8. Check your understanding, 9. Go deeper / Still open (+1 more)

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

### Community 191 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 220 - "Generation"
Cohesion: 0.29
Nodes (4): Generation, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, The stream was closed before it finished (client left, or the turn's deadline…, TraceLabels

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

### Community 234 - "_Stt"
Cohesion: 0.22
Nodes (7): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them., The speech-to-text seam of a test: a scripted transcriber and a fresh per-test…, No transcriber configured (DEEPGRAM_API_KEY blank)., _Stt

### Community 235 - "Communication and priorities"
Cohesion: 0.50
Nodes (3): Communication and priorities, Explaining technical work, Prioritising under pressure

### Community 236 - "Engineering habits"
Cohesion: 0.50
Nodes (3): Code review, Engineering habits, Testing strategy

### Community 237 - "Senior judgement"
Cohesion: 0.50
Nodes (3): Ambiguous problems, Senior judgement, Technical direction

### Community 238 - "Affected Files & Patterns"
Cohesion: 0.33
Nodes (5): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns

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

### Community 244 - "RubricCriterion"
Cohesion: 0.40
Nodes (4): model_validator, Self, One criterion of the feedback rubric: what it asks, an anchor per score, and…, RubricCriterion

### Community 245 - "Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)"
Cohesion: 0.50
Nodes (3): Debugging a slow endpoint in production, Rolling out a risky change, Template (copy to app/modules/interviews/data/knowledge/<topic>.md, then replace everything below the header; roles: see note-guide.md)

### Community 246 - "fixture"
Cohesion: 0.14
Nodes (14): answer(), _answer(), anyio_backend(), _decision_json(), fixture, Builds a reply in the exact shape the decide call must produce., Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a recording to the transcription endpoint; `audio=None` sends no file part… (+6 more)

### Community 247 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 248 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.22
Nodes (8): Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Role-Based Access Control (single JWT), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Trade-offs & Rationale

### Community 249 - "TranscriptionResult"
Cohesion: 0.25
Nodes (5): BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, `audio` is a whole recording in a container the vendor detects itself (WebM,…, TranscriptionResult, test_125_s_or_an_unreported_duration_is_accepted()

### Community 250 - "build_tracer"
Cohesion: 0.47
Nodes (6): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 252 - "stream_answer"
Cohesion: 0.29
Nodes (7): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream(), test_done_has_the_json_endpoints_shape_and_content(), run()

### Community 253 - "traces"
Cohesion: 0.29
Nodes (3): fixture, RecordingClient, traces()

### Community 254 - "client"
Cohesion: 0.67
Nodes (3): client(), propagated(), fixture

### Community 255 - "ContextReport"
Cohesion: 0.40
Nodes (3): ContextReport, _log(), NamedTuple

### Community 256 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 258 - ".__init__"
Cohesion: 0.50
Nodes (3): AsyncBaseTransport, BaseTransport, Random

### Community 259 - "_LostClaim"
Cohesion: 0.67
Nodes (3): _LostClaim, Exception, Another request took the row over while this one ran: this one's writes are…

### Community 260 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 262 - "started"
Cohesion: 0.67
Nodes (3): fixture, An owner with a started backend interview: (owner, session_id)., started()

## Knowledge Gaps
- **755 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+750 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1760 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **41 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `auth_service.py`, `TurnContext`, `decode_token`, `interviews_route.py`, `PageParams`, `ContextManager`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `interviews_constants.py`, `interviews_repository.py`, `interviews_schema.py`, `interviews_model.py`, `BaseModel`, `InterviewerInputs`, `test_create_interview.py`, `Implementation Steps`, `InterviewQuestion`, `errors.py`, `interviews_feedback_controller.py`, `tests/conftest.py`, `Implementation Plan: UUID primary keys`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **Why does `Tracer` connect `interviews_constants.py` to `test_rag_evals.py`, `interviews_feedback_evals.py`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `ContextManager`, `failed`, `test_feedback_endpoint.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `interviews_rag_evals.py`, `ChatMessage`, `test_tracing.py`, `InterviewerInputs`, `test_tracing_routes.py`, `Any`, `RecordingClient`, `Implementation: Langfuse Tracing`, `FakeClient`, `Generation`, `test_factory.py`, `interviews_evals.py`, `test_evals.py`, `LLMResult`, `OpenAICompatibleProvider`, `build_tracer`, `traces`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `interviews_feedback_evals.py`, `test_feedback_evals.py`, `ContextManager`, `interviews_constants.py`, `ChatMessage`, `test_tracing.py`, `BaseModel`, `InterviewerInputs`, `test_start_llm.py`, `test_openai_compatible_stream.py`, `test_job_description_summary.py`, `QuestionCategory`, `._run`, `run_case`, `build_context_manager`, `Generation`, `test_factory.py`, `test_answer_llm.py`, `interviews_evals.py`, `test_evals.py`, `OpenAICompatibleProvider`, `test_turn_budget.py`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Are the 63 inferred relationships involving `JobRole` (e.g. with `FeedbackScoreInputs` and `FeedbackWriteInputs`) actually correct?**
  _`JobRole` has 63 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 37 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 37 INFERRED edges - model-reasoned connections that need verification._