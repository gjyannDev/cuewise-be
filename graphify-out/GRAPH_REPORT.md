# Graph Report - cuewise-be  (2026-11-02)

## Corpus Check
- 193 files · ~161,301 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 2482 nodes · 6609 edges · 142 communities (129 shown, 13 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1194 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `32de5899`
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
- users_route.py
- interviews_utils.py
- Implementation Steps
- typing
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- ConsoleFormatter
- QuestionTurn
- users_utils.py
- README.md
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- LLMProvider
- test_follow_ups.py
- test_start_llm.py
- Implementation Steps
- test_answer_stream.py
- Feature: Context Management for the Interview LLM Calls
- .__init__
- Implementation: LLM as the Interviewer (it asks the questions)
- The fundamentals
- InterviewMessage
- Feature: LLM as the Interviewer (it asks the questions)
- context.py
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
- Implementation Plan: Start an Interview (backend)
- QuestionCategory
- test_turn_budget.py
- test_evals.py
- Interviewer
- test_interview_report.py
- interview_report.py
- interviews_report.py
- test_openai_compatible.py
- test_answer_interview.py
- OpenAICompatibleProvider
- InterviewQuestion
- require_permissions
- job_description_summary_v2.md
- test_create_interview.py
- test_stream_answer.py
- interviews_model.py
- test_get_interview.py
- interviews_controller.py
- LLMResult
- build_usage_report
- InterviewerInputs
- test_reply_contract.py
- errors.py
- Role
- interviews_turn.py
- tracing.py
- Langfuse
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- test_job_description_summary.py
- Implementation: Error Handling
- LLMError
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- llm
- logging.py
- ContextManager
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- test_openai_compatible_stream.py
- InvalidReplyError
- Langfuse Observability
- interviewer_v3.md
- interviews_dependencies.py
- no_llm_env
- fixture
- EvalCase
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- build_provider
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Steps
- bank
- Langfuse Dataset Construction
- interviews_evals.py
- StreamedTurn
- interviews_route.py
- RequestContextMiddleware
- Feature: Langfuse Tracing
- test_llm_settings_default_to_off_with_documented_limits
- anyio
- Settings
- clock
- test_request_context.py
- Langfuse Implementation Notes
- interviewer_v5.md
- Implementation Plan: Langfuse Tracing
- Clock
- Implementation Plan: UUID primary keys
- test_list_users.py
- Feature: Follow-up Questions (decide / write split)
- AI Engineering Learning Path (Cuewise)
- Learnings: LLM Slice 2 (LLM as the Interviewer)
- Base
- build_tracer
- Langfuse v4 project migration
- follow_up
- Learnings: LLM Slice 1 (Interviewer Reaction)
- Judge Calibration
- Langfuse Prompt Migration
- Slices in detail
- FakeObservation
- Langfuse CI/CD
- Prompt Engineering
- Learnings: Follow-up Questions (decide / write split)
- FakeStream
- _reset_request_id

## God Nodes (most connected - your core abstractions)
1. `InterviewsController` - 71 edges
2. `InterviewQuestion` - 71 edges
3. `LLMResult` - 63 edges
4. `QuestionCategory` - 59 edges
5. `FakeProvider` - 58 edges
6. `ChatMessage` - 54 edges
7. `InterviewType` - 54 edges
8. `InterviewSession` - 54 edges
9. `User` - 52 edges
10. `InterviewMessage` - 50 edges

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

## Communities (142 total, 13 thin omitted)

### Community 0 - "User"
Cohesion: 0.08
Nodes (30): verify_password(), get_db(), Session, AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session (+22 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 2 - "test_tracing_routes.py"
Cohesion: 0.12
Nodes (7): get_tracer(), Request, Built once at startup (app lifespan); a disabled tracer when the lifespan…, fixture, Which requests open a Langfuse trace, and with what (langfuse-tracing AC1, AC2,…, RecordingClient, traces()

### Community 3 - "decode_token"
Cohesion: 0.14
Nodes (26): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Implementation Steps, Testing Strategy (+18 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.12
Nodes (37): NotEnoughQuestionsError, InterviewType, pick_fallback_question(), Random, One unused bank question for `position`, used when the LLM is off or its reply…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Collection (+29 more)

### Community 8 - "users_route.py"
Cohesion: 0.14
Nodes (15): UsersController, Session, UsersRepository, get_controller(), list_users(), Depends, Session, BaseModel (+7 more)

### Community 9 - "interviews_utils.py"
Cohesion: 0.12
Nodes (38): JobRole, Level, MessageKind, MessageRole, StrEnum, QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that…, Transcript item kinds: a question comes from interview_questions, the other two… (+30 more)

### Community 10 - "Implementation Steps"
Cohesion: 0.16
Nodes (26): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, WindowLedger, Expect, The label for the decide call: the action it should pick, and the gap when only…, Decision (+18 more)

### Community 11 - "typing"
Cohesion: 0.16
Nodes (19): hash_password(), health_check(), login(), me(), AuthControllerDep, post, register(), LoginIn (+11 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_config.py"
Cohesion: 0.18
Nodes (21): _google(), parametrize, _settings(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored(), test_api_key_never_shows_in_repr_or_errors(), test_blank_provider_list_means_llm_off(), test_blank_removed_settings_are_tolerated() (+13 more)

### Community 15 - "ConsoleFormatter"
Cohesion: 0.22
Nodes (13): ConsoleFormatter, `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, Dev console only: colours, and one field per line for `event key=value ...`…, split_fields(), sys, _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success() (+5 more)

### Community 16 - "QuestionTurn"
Cohesion: 0.10
Nodes (33): End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned… (+25 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.16
Nodes (33): What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, Delta, PhaseChanged, StrEnum, The next chunk of the question being written (shown as it arrives)., What the turn ends with, after the limits: the model can only ask for the first…, TurnAction (+25 more)

### Community 28 - "LLMProvider"
Cohesion: 0.18
Nodes (17): LLMProvider, Protocol, _add_usage(), _case_inputs(), CaseResult, ReasoningEffort, One decide call on the case's latest answer, as the app makes it after every…, The streamed turn's write call (interviewer_stream, v5) on one case: the same… (+9 more)

### Community 29 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): Checkpoint A: the model suggests, the code enforces (concept 5), answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 31 - "Implementation Steps"
Cohesion: 0.10
Nodes (19): Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps, Overview, Phase A: plumbing and progress events, Phase B: streaming the question text, Project Rules Applied, Ready to Implement, Skills Consulted (+11 more)

### Community 32 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (17): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+9 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - ".__init__"
Cohesion: 0.50
Nodes (3): Random, AsyncBaseTransport, BaseTransport

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "The fundamentals"
Cohesion: 0.17
Nodes (12): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+4 more)

### Community 37 - "InterviewMessage"
Cohesion: 0.12
Nodes (19): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, sqlalchemy_exc, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started() (+11 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "context.py"
Cohesion: 0.10
Nodes (28): BuiltContext, ContextReport, ContextTooLargeError, estimate_tokens(), _log(), Any, Exception, NamedTuple (+20 more)

### Community 40 - "test_context_strategies.py"
Cohesion: 0.16
Nodes (39): Checkpoint C: what a follow-up costs in context (concept 2), decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+31 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.14
Nodes (31): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+23 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.14
Nodes (18): db(), Fresh in-memory SQLite DB per test, wired into the app's get_db dependency., messages(), questions(), Answer every question of a started interview; returns the list of answer…, run_interview(), test_a_double_submit_stores_one_answer_and_makes_one_call(), test_a_legacy_session_uses_its_stored_questions_and_no_llm() (+10 more)

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
Cohesion: 0.12
Nodes (27): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, client(), drain(), FakeClient, propagated(), fixture, Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider… (+19 more)

### Community 49 - "tests/conftest.py"
Cohesion: 0.11
Nodes (24): CurrentUserDep, Affected Files & Patterns, os, sqlalchemy_pool, auth_header(), _header(), client(), make_user() (+16 more)

### Community 50 - "Implementation Plan: Start an Interview (backend)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Start an Interview (backend), Known Follow-ups (story 3: Chat with the interviewer), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.13
Nodes (28): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, load_bank(), pick_reaction(), Path, A predefined, neutral acknowledgement for the answer just given; never the same…, Read and validate a question bank file; a bad file fails loudly instead of at… (+20 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 53 - "test_evals.py"
Cohesion: 0.16
Nodes (28): load_cases(), Path, run_case(), long_case(), noted(), reply(), test_a_good_reply_passes_every_check(), test_a_good_streamed_reply_passes_every_check() (+20 more)

### Community 54 - "Interviewer"
Cohesion: 0.11
Nodes (32): Deadline, Draft, Interviewer, _log_error(), log_llm_call(), log_result(), NamedTuple, UUID (+24 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.13
Nodes (50): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start() (+42 more)

### Community 56 - "interview_report.py"
Cohesion: 0.10
Nodes (33): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+25 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.07
Nodes (65): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+57 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.15
Nodes (29): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_cached_and_reasoning_tokens_are_none_when_not_reported() (+21 more)

### Community 59 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 60 - "OpenAICompatibleProvider"
Cohesion: 0.17
Nodes (10): _int_or_none(), OpenAICompatibleProvider, Any, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final…, How long to wait before retrying, or None to give up., One streamed request: its text chunks, then an LLMResult (attempts and latency… (+2 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.13
Nodes (15): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Session, UUID, Save one whole turn in one commit: advance the session, the answer, the…, Abandon the user's active session and save the new one with its questions, all… (+7 more)

### Community 62 - "require_permissions"
Cohesion: 0.06
Nodes (40): permissions_for(), The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check() (+32 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_create_interview.py"
Cohesion: 0.18
Nodes (17): parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back(), test_first_bank_question_fits_the_setup() (+9 more)

### Community 65 - "test_stream_answer.py"
Cohesion: 0.24
Nodes (13): fixture, InterviewsController.stream_answer driven directly, for what a test client…, A started interview and a controller wired like the app's: returns (controller,…, saved_answers(), summaries(), test_closing_the_stream_mid_turn_saves_nothing(), test_leaving_while_the_decide_call_runs_saves_nothing(), test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing() (+5 more)

### Community 66 - "interviews_model.py"
Cohesion: 0.07
Nodes (14): Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, sqlalchemy, candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm() (+6 more)

### Community 67 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 68 - "interviews_controller.py"
Cohesion: 0.07
Nodes (65): QuestionNotCurrentError, SessionNotInProgressError, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, The SSE event names of a streamed turn: the contract with the client. `done`…, SessionStatus, StreamEvent, _elapsed_ms() (+57 more)

### Community 71 - "LLMResult"
Cohesion: 0.14
Nodes (20): FakeProvider, ReasoningEffort, Test double for LLMProvider: scripted replies or errors, records every call.…, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, ChatMessage, LLMResult, BaseModel, ReasoningEffort (+12 more)

### Community 72 - "build_usage_report"
Cohesion: 0.20
Nodes (16): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, main(), Session, Print stored LLM usage per interview: tokens per question position and per…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind() (+8 more)

### Community 73 - "InterviewerInputs"
Cohesion: 0.14
Nodes (15): _counts(), FollowUpDecision, InterviewerInputs, NamedTuple, An earlier question as the model would have written it. A follow-up was written…, The decide call: the current thread in full (it judges the latest answer within…, App data at the end of the last user message; untrusted parts (questions,…, Plain values for one interviewer or decide call. (+7 more)

### Community 74 - "test_reply_contract.py"
Cohesion: 0.31
Nodes (17): parse(), parametrize, reply(), test_a_bad_note_is_dropped_but_the_question_is_kept(), test_a_field_other_than_question_category_and_note_is_still_rejected(), test_a_question_already_asked_is_rejected_ignoring_case_and_spacing(), test_a_single_code_fence_is_accepted(), test_a_valid_note_is_kept_trimmed() (+9 more)

### Community 75 - "errors.py"
Cohesion: 0.10
Nodes (34): AppError, BadRequestError, ConflictError, ErrorBody, ErrorResponse, ForbiddenError, InvalidCredentialsError, NotFoundError (+26 more)

### Community 76 - "Role"
Cohesion: 0.10
Nodes (28): Permission, StrEnum, Role, _assert_401(), parametrize, test_bad_tokens_are_token_invalid(), test_expired_token_is_token_expired(), test_forged_admin_claim_does_not_grant_access() (+20 more)

### Community 77 - "interviews_turn.py"
Cohesion: 0.12
Nodes (25): _check_question(), HeaderSplit, InterviewerReply, _normalized(), parse_interviewer_reply(), parse_streamed_reply(), BaseModel, NamedTuple (+17 more)

### Community 78 - "tracing.py"
Cohesion: 0.12
Nodes (13): AbstractContextManager, Generation, Any, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, One trace for one request: everything started inside it (the generations) nests…, Run an SDK call; on any failure log what failed (not why: the message could…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, The stream was closed before it finished (client left, or the turn's deadline… (+5 more)

### Community 79 - "Langfuse"
Cohesion: 0.09
Nodes (19): Credentials, Discovery, Install, Langfuse CLI Reference, Tips, Skill Feedback, Submission options, 1. Langfuse API via CLI (+11 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.36
Nodes (6): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_without_an_llm_no_summary_is_made()

### Community 83 - "Implementation: Error Handling"
Cohesion: 0.07
Nodes (24): Baseline Failures, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Suggested Commit (+16 more)

### Community 84 - "LLMError"
Cohesion: 0.18
Nodes (18): _raise_for_status(), OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, LLMBadResponseError, LLMError, LLMRateLimitError, LLMRequestError, LLMServerError, LLMTimeoutError (+10 more)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "llm"
Cohesion: 0.16
Nodes (9): as_v5_text(), llm(), script(), unique_question(), The streamed question as the client shows it: deltas appended, a reset clearing…, Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY…, Builds a reply in the exact shape the interviewer LLM must produce. (+1 more)

### Community 87 - "logging.py"
Cohesion: 0.29
Nodes (6): setup_logging(), contextvars, logging_config, pathlib, re, starlette_types

### Community 88 - "ContextManager"
Cohesion: 0.15
Nodes (15): ContextManager, Task, build_context_manager(), FullHistory, JobDescriptionSummary, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,…, SummaryInputs, Completed Steps (+7 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learnings: Context Management"
Cohesion: 0.29
Nodes (6): Checkpoint A: the baseline (before any context change), Checkpoint B: the six-part prompts (after step 3), Checkpoint C: the "before" snapshot (step 8), Checkpoint D: the comparison (step 12) - strategy comparison recorded, ablations open, Checkpoint E: where the cost went (live interview, 2026-10-30), Learnings: Context Management

### Community 92 - "test_openai_compatible_stream.py"
Cohesion: 0.13
Nodes (25): anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider(), ok(), Exception (+17 more)

### Community 93 - "InvalidReplyError"
Cohesion: 0.18
Nodes (18): read(), InvalidReplyError, Exception, interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), parse(), parametrize, interviewer_v5's streamed reply: a `CATEGORY:` header line (next-question mode… (+10 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.18
Nodes (9): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+1 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "interviews_dependencies.py"
Cohesion: 0.14
Nodes (21): Random, get_bank(), get_clock(), get_controller(), get_llm_provider(), Depends, Session, The question source; tests override it with a fixture bank. (+13 more)

### Community 97 - "no_llm_env"
Cohesion: 0.50
Nodes (4): no_langfuse_env(), no_llm_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…

### Community 98 - "fixture"
Cohesion: 0.18
Nodes (11): answer(), _answer(), anyio_backend(), _decision_json(), fixture, Builds a reply in the exact shape the decide call must produce., Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a setup for `user`; any field can be overridden, or dropped by passing… (+3 more)

### Community 99 - "EvalCase"
Cohesion: 0.14
Nodes (23): Check, check_decision(), check_reply(), check_streamed_reply(), EvalCase, Rule checks for one reply. Text checks look at the parsed question, or at the…, check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, The checks on what the candidate would read, whatever the reply format. (+15 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "build_provider"
Cohesion: 0.17
Nodes (11): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, ReasoningEffort, TracingProvider, Implementation Steps, fixture, settings_with(), test_enabled_tracer_wraps_the_provider_and_a_disabled_one_does_not() (+3 more)

### Community 104 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional (+7 more)

### Community 105 - "Implementation Steps"
Cohesion: 0.12
Nodes (19): get_context_manager(), Decides what each LLM call sends; tests swap in one with a tiny limit., The same one-off condensation the app makes at interview start; its tokens…, summarize(), The job-description summary replaces the original on every later call, so it…, validate_summary(), Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls (+11 more)

### Community 106 - "bank"
Cohesion: 0.22
Nodes (9): Acceptance Criteria, Acceptance Criteria, Edge Cases, Functional, Non-Functional, Requirements, Test Results, bank() (+1 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.17
Nodes (19): anyio_from_thread, DecisionSummary, EvalSetup, EvalTurn, main(), _parser(), _positive(), _print_case() (+11 more)

### Community 109 - "StreamedTurn"
Cohesion: 0.22
Nodes (8): parse_sse(), NamedTuple, Event names with each run of question.delta shown once: the shape of the…, Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream(), StreamedTurn

### Community 110 - "interviews_route.py"
Cohesion: 0.19
Nodes (17): answer_question(), answer_question_stream(), get_interview(), get_transcript(), post, UUID, start_interview(), EventSourceResponse (+9 more)

### Community 111 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.15
Nodes (12): Acceptance Criteria, Blockers, Feature: Langfuse Tracing, Functional, Goal, Non-Functional, Out of Scope, Problem (+4 more)

### Community 113 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.50
Nodes (5): Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 114 - "anyio"
Cohesion: 0.18
Nodes (9): anyio, Checkpoint A: what the candidate waits for, Checkpoint B: streaming vs structured output, Checkpoint C: what a dropped stream leaves behind, Learnings: SSE Streaming of the Interview Turn (Slice 4), Proof (concept 7), Still open, test_other_requests_are_served_while_a_stream_waits_on_the_llm() (+1 more)

### Community 115 - "Settings"
Cohesion: 0.12
Nodes (12): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block., Settings, BaseSettings, Testing Strategy, Constraints, Step 0: Rename the provider to a vendor-neutral name (+4 more)

### Community 116 - "clock"
Cohesion: 0.25
Nodes (4): _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

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
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 121 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "test_list_users.py"
Cohesion: 0.18
Nodes (3): parametrize, test_out_of_range_pagination_is_422(), test_plain_user_is_forbidden()

### Community 124 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers, Constraints, Feature: Follow-up Questions (decide / write split), Goal, Out of Scope, Problem, Project Conventions, User Flow (+1 more)

### Community 125 - "AI Engineering Learning Path (Cuewise)"
Cohesion: 0.22
Nodes (8): AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", How to make it stick, Later stages (after the core is solid), Progress, Slices, The core mindset, The foundation this leaves behind

### Community 126 - "Learnings: LLM Slice 2 (LLM as the Interviewer)"
Cohesion: 0.22
Nodes (8): Checkpoint A: after Step 3 (reply contract), Checkpoint B: after Step 4 (prompt and messages), Checkpoint C: after Step 5 (pickers), Checkpoint D: after Step 6 (start + turn engine), Checkpoint E: after Step 7 (atomic answer turn), Checkpoint F: after Step 9 (evals), Checkpoint G: after Step 10 (real model, Proof round), Learnings: LLM Slice 2 (LLM as the Interviewer)

### Community 127 - "Base"
Cohesion: 0.25
Nodes (6): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, DeclarativeBase

### Community 128 - "build_tracer"
Cohesion: 0.32
Nodes (8): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, lifespan(), FastAPI, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "follow_up"
Cohesion: 0.25
Nodes (8): Edge Cases, Functional, Non-Functional, Requirements, follow_up(), test_a_follow_up_is_accepted_without_a_category_and_inherits_the_parents(), test_a_follow_up_still_asks_one_question_only(), test_a_follow_up_that_repeats_an_earlier_follow_up_is_rejected()

### Community 131 - "Learnings: LLM Slice 1 (Interviewer Reaction)"
Cohesion: 0.25
Nodes (7): Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 134 - "Slices in detail"
Cohesion: 0.29
Nodes (7): Slice 1: Answer → reply (no streaming), Slice 2: Prompts as data + injection safety, Slice 3: Structured follow-up decisions, Slice 4: SSE streaming, Slice 5: Evals (the habit, made repeatable), Slice: Context management (added after Slice 2), Slices in detail

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "Learnings: Follow-up Questions (decide / write split)"
Cohesion: 0.40
Nodes (4): Checkpoint B: a small closed decision instead of free text (concept 4), Checkpoint D: labelled evals for a decision (concept 10), Checkpoint E: one deadline for two calls (concept 9), Learnings: Follow-up Questions (decide / write split)

### Community 139 - "FakeStream"
Cohesion: 0.50
Nodes (4): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, test_the_streamed_question_is_the_saved_one_and_never_shows_its_category()

## Knowledge Gaps
- **383 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+378 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 920 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User` to `test_create_interview.py`, `interviews_model.py`, `decode_token`, `interviews_controller.py`, `users_route.py`, `typing`, `Role`, `interviews_route.py`, `tests/conftest.py`, `Implementation Plan: UUID primary keys`, `InterviewQuestion`, `require_permissions`, `Base`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Why does `LLMResult` connect `LLMResult` to `QuestionTurn`, `LLMProvider`, `test_start_llm.py`, `Implementation Steps`, `test_answer_llm.py`, `test_tracing.py`, `test_turn_budget.py`, `test_evals.py`, `Interviewer`, `OpenAICompatibleProvider`, `interviews_controller.py`, `interviews_turn.py`, `tracing.py`, `test_job_description_summary.py`, `LLMError`, `ContextManager`, `test_openai_compatible_stream.py`, `build_provider`, `interviews_evals.py`, `Implementation Plan: Langfuse Tracing`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `interviews_utils.py`, `Implementation Steps`, `FakeStream`, `QuestionTurn`, `test_follow_ups.py`, `test_start_llm.py`, `test_answer_stream.py`, `InterviewMessage`, `test_answer_llm.py`, `test_transcript.py`, `test_turn_budget.py`, `test_interview_report.py`, `interviews_report.py`, `test_create_interview.py`, `interviews_model.py`, `interviews_controller.py`, `LLMResult`, `build_usage_report`, `Base`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Are the 48 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 48 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 35 inferred relationships involving `QuestionCategory` (e.g. with `InterviewsController` and `Thread`) actually correct?**
  _`QuestionCategory` has 35 INFERRED edges - model-reasoned connections that need verification._