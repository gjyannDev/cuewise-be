# Graph Report - cuewise-be  (2026-11-04)

## Corpus Check
- 204 files · ~171,922 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 2869 nodes · 7442 edges · 154 communities (141 shown, 13 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1303 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5bf52fd1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- Feature: Start an Interview (backend)
- test_tracing_routes.py
- decode_token
- exception_handlers.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Cuewise BE — Project Instructions
- InterviewType
- uuid
- JobRole
- Implementation Steps
- interviews_controller.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- QuestionTurn
- users_utils.py
- README.md
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- LLMProvider
- interviews_utils.py
- test_start_llm.py
- Implementation Steps
- test_answer_stream.py
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- InterviewMessage
- Feature: LLM as the Interviewer (it asks the questions)
- Bundle
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- test_transcript.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- tests/conftest.py
- interviews_context.py
- test_reaction_pick.py
- test_turn_budget.py
- test_evals.py
- interviews_turn.py
- test_interview_report.py
- test_openai_compatible_stream.py
- interviews_report.py
- test_openai_compatible.py
- InterviewsController
- LLMError
- InterviewQuestion
- require_permissions
- job_description_summary_v2.md
- test_create_interview.py
- test_stream_answer.py
- interviews_dependencies.py
- test_get_interview.py
- .prepare_answer
- LLMResult
- build_usage_report
- context.py
- test_reply_contract.py
- ErrorResponse
- test_guards.py
- RecordingClient
- main.py
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- thread_start
- test_job_description_summary.py
- ConsoleFormatter
- test_transcribe.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- pytest
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- analyze_interview
- QuestionCategory
- Langfuse Observability
- interviewer_v3.md
- interviews/conftest.py
- no_llm_env
- Implementation: Langfuse Tracing
- check_streamed_reply
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- OpenAICompatibleProvider
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: Context Management for the Interview LLM Calls
- run_case
- Langfuse Dataset Construction
- interviews_evals.py
- StreamedTurn
- Implementation: Error Handling
- test_me.py
- Feature: Langfuse Tracing
- Langfuse
- Learnings: SSE Streaming of the Interview Turn (Slice 4)
- .stream_answer
- Role
- test_request_context.py
- Langfuse Implementation Notes
- interviewer_v5.md
- Implementation Plan: Langfuse Tracing
- llm
- Implementation Plan: UUID primary keys
- test_follow_ups.py
- RateLimiter
- test_answer_interview.py
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- .__init__
- Langfuse Dataset Construction
- Langfuse v4 project migration
- Clock
- _Stt
- Judge Calibration
- Langfuse Prompt Migration
- Feature: Follow-up Questions (decide / write split)
- FakeObservation
- Langfuse CI/CD
- Prompt Engineering
- fake.py
- Langfuse Implementation Notes
- LLMRequestError
- Feature: Role-Based Access Control (single JWT)
- test_list_users.py
- Implementation Plan: Start an Interview (backend)
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- Checks
- main
- Learnings: Follow-up Questions (decide / write split)

## God Nodes (most connected - your core abstractions)
1. `FakeProvider` - 87 edges
2. `InterviewsController` - 84 edges
3. `InterviewQuestion` - 71 edges
4. `LLMResult` - 64 edges
5. `QuestionCategory` - 59 edges
6. `User` - 58 edges
7. `InterviewSession` - 56 edges
8. `ChatMessage` - 54 edges
9. `InterviewType` - 54 edges
10. `Tracer` - 52 edges

## Surprising Connections (you probably didn't know these)
- `Trade-offs & Rationale` --references--> `ContextManager`  [INFERRED]
  docs/features/follow-up-questions/plan.md → app/core/ai/context.py
- `Acceptance Criteria` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Constraints` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Project Conventions` --references--> `FakeProvider`  [INFERRED]
  docs/features/context-management/spec.md → app/core/ai/fake.py
- `Trade-offs & Rationale` --references--> `LLMError`  [INFERRED]
  docs/features/interviewer-reaction/plan.md → app/core/ai/provider.py

## Import Cycles
- None detected.

## Communities (154 total, 13 thin omitted)

### Community 0 - "User"
Cohesion: 0.09
Nodes (30): InvalidCredentialsError, hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session (+22 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.14
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 2 - "test_tracing_routes.py"
Cohesion: 0.13
Nodes (6): get_tracer(), Built once at startup (app lifespan); a disabled tracer when the lifespan…, fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 3 - "decode_token"
Cohesion: 0.13
Nodes (28): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Testing Strategy (+20 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): get_bank(), get_llm_provider(), The question source; tests override it with a fixture bank., Built once at startup (app lifespan); None when no key is configured or the…, Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1) (+8 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.13
Nodes (35): NotEnoughQuestionsError, InterviewType, pick_fallback_question(), One unused bank question for `position`, used when the LLM is off or its reply…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Collection, random (+27 more)

### Community 8 - "uuid"
Cohesion: 0.18
Nodes (10): UsersController, Session, UsersRepository, get_controller(), Depends, Session, BaseModel, UserAdminOut (+2 more)

### Community 9 - "JobRole"
Cohesion: 0.13
Nodes (29): JobRole, Level, EvalSetup, load_bank(), load_prompt(), Path, Per-interview constants only, so the text is identical on every call of an…, Read and validate a question bank file; a bad file fails loudly instead of at… (+21 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.14
Nodes (26): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, _load_object(), parse_decision_reply(), The reply as a JSON object: one optional fence around it, nothing else before…, The decide call suggests; the code still applies the follow-up cap and the time… (+18 more)

### Community 11 - "interviews_controller.py"
Cohesion: 0.15
Nodes (29): What a streamed answer turn is doing, sent as `status` events so the candidate…, SessionStatus, TurnPhase, AnswerIn, BankQuestion, InterviewCreateIn, InterviewOut, BaseModel (+21 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_config.py"
Cohesion: 0.12
Nodes (29): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., os, _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset() (+21 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.12
Nodes (26): anyio_backend(), Clock, listen_body(), make_transcriber(), _make(), ok(), fixture, parametrize (+18 more)

### Community 16 - "QuestionTurn"
Cohesion: 0.09
Nodes (37): End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned… (+29 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.12
Nodes (41): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, ActionKnown, Delta, PhaseChanged, NamedTuple, StrEnum (+33 more)

### Community 28 - "LLMProvider"
Cohesion: 0.18
Nodes (5): LLMProvider, Protocol, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Random

### Community 29 - "interviews_utils.py"
Cohesion: 0.15
Nodes (25): AudioContainer, MessageKind, MessageRole, StrEnum, QuestionKind, QuestionSource, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, Who wrote a stored question: the LLM, or the hand-written bank (fallback and… (+17 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 31 - "Implementation Steps"
Cohesion: 0.09
Nodes (21): Save one whole turn in one commit: advance the session, the answer, the…, Deviations Found During Implementation, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps, Overview, Phase A: plumbing and progress events, Phase B: streaming the question text, Project Rules Applied (+13 more)

### Community 32 - "test_answer_stream.py"
Cohesion: 0.07
Nodes (20): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+12 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.18
Nodes (10): Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+2 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.07
Nodes (27): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+19 more)

### Community 37 - "InterviewMessage"
Cohesion: 0.12
Nodes (17): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, sqlalchemy_exc, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started() (+9 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.10
Nodes (20): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+12 more)

### Community 39 - "Bundle"
Cohesion: 0.11
Nodes (23): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+15 more)

### Community 40 - "test_context_strategies.py"
Cohesion: 0.16
Nodes (37): Checkpoint C: what a follow-up costs in context (concept 2), decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+29 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.15
Nodes (28): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+20 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.12
Nodes (20): Learning Log (`learnings.md`), Known Follow-ups (story 3: Chat with the interviewer), itertools, db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions(), Answer every question of a started interview; returns the list of answer… (+12 more)

### Community 45 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.08
Nodes (32): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, client(), drain(), FakeClient, propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider… (+24 more)

### Community 49 - "tests/conftest.py"
Cohesion: 0.10
Nodes (25): health_check(), list_users(), Affected Files & Patterns, ge, le, MAX_PAGE_SIZE, Query, sqlalchemy_pool (+17 more)

### Community 50 - "interviews_context.py"
Cohesion: 0.11
Nodes (27): ContextManager, Task, build_context_manager(), _counts(), FullHistory, JobDescriptionSummary, What the interview LLM calls send: the tasks and strategies registered with the…, An earlier question as the model would have written it. A follow-up was written… (+19 more)

### Community 51 - "test_reaction_pick.py"
Cohesion: 0.23
Nodes (15): LevelGroup, Reactions are warmer for people early in their career and briefer for…, pick_reaction(), Random, A predefined, neutral acknowledgement for the answer just given; never the same…, pick(), parametrize, test_a_one_entry_pool_still_works() (+7 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 53 - "test_evals.py"
Cohesion: 0.14
Nodes (42): FakeProvider, load_cases(), Path, decision(), hints_of(), labelled(), mentions(), run_main() (+34 more)

### Community 54 - "interviews_turn.py"
Cohesion: 0.12
Nodes (33): InterviewerInputs, Plain values for one interviewer or decide call., Condense a long job description once, so later calls send less. One attempt…, Decision, Deadline, _decision_label(), Interviewer, _log_error() (+25 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.07
Nodes (85): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, What needs attention comes first (watch, checks), then the sections, then the…, render_html(), render_text(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, html_target() (+77 more)

### Community 56 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.15
Nodes (27): analyze_rollup(), _avg(), _cost(), _counts(), _effectiveness(), _efficiency(), _latency_row(), _limit_tone() (+19 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.15
Nodes (29): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_cached_and_reasoning_tokens_are_none_when_not_reported() (+21 more)

### Community 59 - "InterviewsController"
Cohesion: 0.14
Nodes (26): AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody, NoSpeechError, NotFoundError (+18 more)

### Community 60 - "LLMError"
Cohesion: 0.08
Nodes (38): DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The first channel's best transcript (blank for silence) and the reported audio…, _int_or_none() (+30 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.14
Nodes (17): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Session, UUID, Abandon the user's active session and save the new one with its questions, all…, Any user's session, by id: for the report script only (the API always goes… (+9 more)

### Community 62 - "require_permissions"
Cohesion: 0.08
Nodes (42): ForbiddenError, get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), require_roles() (+34 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 65 - "test_stream_answer.py"
Cohesion: 0.40
Nodes (9): InterviewsController.stream_answer driven directly, for what a test client…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing(), test_the_first_event_is_sent_before_any_llm_call_returns(), test_the_stream_summary_is_metadata_only() (+1 more)

### Community 66 - "interviews_dependencies.py"
Cohesion: 0.07
Nodes (20): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), The speech-to-text contract features code against, separate from the text-only…, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base (+12 more)

### Community 67 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 68 - ".prepare_answer"
Cohesion: 0.10
Nodes (21): QuestionNotCurrentError, InterviewSetup, _llm_question(), NamedTuple, UUID, The session fields the interviewer needs, as plain values that survive the end…, The main question the answered question belongs to (itself, or a follow-up's…, Everything an answer turn needs, read before its LLM calls (the read… (+13 more)

### Community 71 - "LLMResult"
Cohesion: 0.12
Nodes (18): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ReasoningEffort, Same request with `stream: true`: chunks as they arrive, then the final…, ChatMessage, LLMResult, BaseModel, One turn of the conversation sent to the model. The model keeps no memory:… (+10 more)

### Community 72 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 73 - "context.py"
Cohesion: 0.10
Nodes (29): BuiltContext, ContextReport, ContextTooLargeError, estimate_tokens(), _log(), Any, Exception, NamedTuple (+21 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.21
Nodes (23): json, follow_up(), parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_follow_up_in_a_behavioral_only_interview_keeps_the_behavioral_category() (+15 more)

### Community 75 - "ErrorResponse"
Cohesion: 0.13
Nodes (16): ErrorResponse, BaseModel, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview, Project Rules Applied (+8 more)

### Community 76 - "test_guards.py"
Cohesion: 0.15
Nodes (17): CurrentUserDep, _assert_401(), authenticated(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access(), test_guards_allow_or_forbid_by_db_role() (+9 more)

### Community 77 - "RecordingClient"
Cohesion: 0.12
Nodes (7): case(), langfuse(), fixture, A Langfuse client stand-in. Entering a trace sets `current_trace`, like the SDK…, RecordingClient, test_a_failed_dataset_upsert_still_scores_the_cases(), test_a_langfuse_outage_does_not_change_the_run()

### Community 78 - "main.py"
Cohesion: 0.09
Nodes (24): build_tracer(), Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, On only when both keys are set. `environment` overrides APP_ENV (the eval…, _usage_details(), setup_logging(), Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, lifespan() (+16 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.11
Nodes (18): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4) (+10 more)

### Community 81 - "thread_start"
Cohesion: 0.09
Nodes (18): FollowUpDecision, The decide call: the current thread in full (it judges the latest answer within…, main_numbers(), The main-question number of each turn: a follow-up shares the number of the…, Index of the main question whose thread holds turn `index` (default: the latest…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt(), thread_start() (+10 more)

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.36
Nodes (6): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_without_an_llm_no_summary_is_made()

### Community 83 - "ConsoleFormatter"
Cohesion: 0.20
Nodes (13): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), LogRecord, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success() (+5 more)

### Community 84 - "test_transcribe.py"
Cohesion: 0.12
Nodes (14): code(), fixture, parametrize, An owner with a started interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+6 more)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Acceptance Criteria, Blockers, Constraints, Feature: SSE Streaming of the Interview Turn (Slice 4), Goal, Non-Functional, Out of Scope, Problem (+3 more)

### Community 87 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.06
Nodes (30): AbstractContextManager, Generation, Any, One trace for one request: everything started inside it (the generations) nests…, Set the output of the trace being built (call it inside `trace()`): what a…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Run an SDK call; on any failure log what failed (not why: the message could… (+22 more)

### Community 88 - "pytest"
Cohesion: 0.28
Nodes (11): pytest, candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer() (+3 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learnings: Context Management"
Cohesion: 0.29
Nodes (6): Checkpoint A: the baseline (before any context change), Checkpoint B: the six-part prompts (after step 3), Checkpoint C: the "before" snapshot (step 8), Checkpoint D: the comparison (step 12) - strategy comparison recorded, ablations open, Checkpoint E: where the cost went (live interview, 2026-10-30), Learnings: Context Management

### Community 92 - "analyze_interview"
Cohesion: 0.26
Nodes (12): analyze_interview(), _call_table(), _dash(), _facts(), _question_table(), Turn N answers the question at position N and asks position N+1: positions are…, Time limits nearly used up, failed or odd calls, overrides, fallbacks, missing…, _rollup_table() (+4 more)

### Community 93 - "QuestionCategory"
Cohesion: 0.11
Nodes (38): QuestionCategory, read(), _check_question(), HeaderSplit, InterviewerReply, InvalidReplyError, _normalized(), parse_interviewer_reply() (+30 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "interviews/conftest.py"
Cohesion: 0.11
Nodes (23): answer(), _answer(), anyio_backend(), _bank_question(), make_bank_question(), parse_sse(), fixture, Split a text/event-stream body into (event, data) pairs; returns them and the… (+15 more)

### Community 97 - "no_llm_env"
Cohesion: 0.33
Nodes (6): no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.18
Nodes (10): Commit message suggestion, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+2 more)

### Community 99 - "check_streamed_reply"
Cohesion: 0.17
Nodes (18): Check, check_decision(), check_reply(), check_streamed_reply(), Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format., The decide reply against the case's label; the injection check reads the raw… (+10 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "OpenAICompatibleProvider"
Cohesion: 0.10
Nodes (27): build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, OpenAICompatibleProvider, TracingProvider, Settings, BaseSettings (+19 more)

### Community 104 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (17): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional (+9 more)

### Community 105 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.10
Nodes (15): get_clock(), Monotonic clock for the per-turn LLM time budget; tests swap in a fake one., Affected Files & Patterns, Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement (+7 more)

### Community 106 - "run_case"
Cohesion: 0.18
Nodes (19): run_case(), long_case(), noted(), reply(), test_a_passing_case_has_no_hints(), test_a_provider_error_fails_the_case_without_crashing(), test_a_v3_window_reply_must_carry_a_note_when_there_is_an_answer(), test_an_unusable_summary_falls_back_to_the_original() (+11 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.07
Nodes (64): anyio_from_thread, NamedTuple, SummaryInputs, _action_and_gap(), _add_usage(), _case_inputs(), CaseResult, dataset_items() (+56 more)

### Community 109 - "StreamedTurn"
Cohesion: 0.33
Nodes (4): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, StreamedTurn

### Community 110 - "Implementation: Error Handling"
Cohesion: 0.13
Nodes (16): RequestIdFilter, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions (+8 more)

### Community 111 - "test_me.py"
Cohesion: 0.33
Nodes (3): parametrize, test_auth_routes_document_error_responses(), test_me_returns_profile_with_resolved_permissions()

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 113 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 114 - "Learnings: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.18
Nodes (9): Checkpoint A: what the candidate waits for, Checkpoint B: streaming vs structured output, Checkpoint C: what a dropped stream leaves behind, Learnings: SSE Streaming of the Interview Turn (Slice 4), Proof (concept 7), Still open, anyio, test_other_requests_are_served_while_a_stream_waits_on_the_llm() (+1 more)

### Community 115 - ".stream_answer"
Cohesion: 0.15
Nodes (17): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, _elapsed_ms(), _error_event(), _event(), BaseModel, For a turn that doesn't use the interviewer: a stored next question never…, The predefined acknowledgement for moving on (or completing). The id is set… (+9 more)

### Community 116 - "Role"
Cohesion: 0.16
Nodes (26): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, login(), me(), AuthControllerDep (+18 more)

### Community 117 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 121 - "llm"
Cohesion: 0.18
Nodes (10): Step 11: `FakeProvider.stream`, as_v5_text(), _decision_json(), llm(), script(), script_decide(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;… (+2 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): Checkpoint A: the model suggests, the code enforces (concept 5), answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 124 - "RateLimiter"
Cohesion: 0.20
Nodes (11): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, math, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window() (+3 more)

### Community 125 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 126 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 127 - ".__init__"
Cohesion: 0.50
Nodes (3): AsyncBaseTransport, Random, BaseTransport

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 131 - "_Stt"
Cohesion: 0.12
Nodes (11): Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, get_transcriber(), get_transcription_limiter(), Request, Built once at startup (app lifespan); None when no Deepgram key is configured…, Tests swap in a fresh limiter so counts never leak between them. (+3 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 134 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "fake.py"
Cohesion: 0.21
Nodes (8): anyio, FakeTranscriber, Test doubles for LLMProvider and Transcriber: scripted replies or errors,…, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, TranscriptionResult, test_125_s_or_an_unreported_duration_is_accepted()

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "LLMRequestError"
Cohesion: 0.18
Nodes (10): LLMRequestError, Other 4xx (bad key, bad request): retrying sends the same broken request again., Checkpoint A: after Step 3 (provider package), Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint) (+2 more)

### Community 142 - "Feature: Role-Based Access Control (single JWT)"
Cohesion: 0.18
Nodes (10): Blockers, Constraints, Feature: Role-Based Access Control (single JWT), Goal, Non-Functional, Out of Scope, Problem, Requirements (+2 more)

### Community 143 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 144 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.20
Nodes (9): Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+1 more)

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

### Community 150 - "Checks"
Cohesion: 0.40
Nodes (5): Checks, bad_parent(), _consistency(), Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers…

### Community 151 - "main"
Cohesion: 0.60
Nodes (4): main(), Session, test_an_empty_database(), test_reports_stored_questions_grouped_by_interview()

### Community 152 - "Learnings: Follow-up Questions (decide / write split)"
Cohesion: 0.40
Nodes (4): Checkpoint B: a small closed decision instead of free text (concept 4), Checkpoint D: labelled evals for a decision (concept 10), Checkpoint E: one deadline for two calls (concept 9), Learnings: Follow-up Questions (decide / write split)

## Knowledge Gaps
- **464 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+459 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1102 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `test_tracing.py` to `interviews_dependencies.py`, `test_tracing_routes.py`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `LLMResult`, `OpenAICompatibleProvider`, `interviews_controller.py`, `interviews_evals.py`, `RecordingClient`, `main.py`, `interviews_context.py`, `test_tracing_lifespan.py`, `test_evals.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `InterviewsController`, `LLMProvider`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `test_create_interview.py`, `interviews_dependencies.py`, `decode_token`, `.prepare_answer`, `uuid`, `interviews_controller.py`, `tests/conftest.py`, `Role`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Implementation Plan: UUID primary keys`, `InterviewsController`, `InterviewQuestion`, `require_permissions`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `InterviewsController` connect `InterviewsController` to `User`, `_Stt`, `InterviewType`, `JobRole`, `fake.py`, `interviews_controller.py`, `QuestionTurn`, `test_stream_turn.py`, `LLMProvider`, `interviews_utils.py`, `InterviewMessage`, `test_tracing.py`, `interviews_context.py`, `interviews_turn.py`, `LLMError`, `InterviewQuestion`, `test_stream_answer.py`, `interviews_dependencies.py`, `.prepare_answer`, `QuestionCategory`, `OpenAICompatibleProvider`, `interviews_evals.py`, `.stream_answer`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Are the 21 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 58 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 58 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 23 INFERRED edges - model-reasoned connections that need verification._