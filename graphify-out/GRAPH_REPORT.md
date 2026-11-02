# Graph Report - cuewise-be  (2026-11-02)

## Corpus Check
- 157 files · ~137,601 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 2243 nodes · 6158 edges · 124 communities (113 shown, 11 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1120 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `853bcef4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User
- Feature: Start an Interview (backend)
- app_logs
- decode_token
- exception_handlers.py
- Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Cuewise BE — Project Instructions
- InterviewType
- users_route.py
- JobRole
- interviews_reply.py
- Implementation Steps
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_logging.py
- QuestionTurn
- users_utils.py
- README.md
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- ContextManager
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
- ChatMessage
- test_context_strategies.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- test_transcript.py
- Implementation: Follow-up Questions (decide / write split)
- Implementation: Error Handling
- tests/conftest.py
- interviews_model.py
- QuestionCategory
- test_turn_budget.py
- FakeProvider
- interviews_turn.py
- test_interview_report.py
- Bundle
- interviews_report.py
- test_openai_compatible.py
- test_answer_interview.py
- OpenAICompatibleProvider
- InterviewQuestion
- Implementation Plan: Role-Based Access Control (single JWT)
- job_description_summary_v2.md
- test_create_interview.py
- test_stream_answer.py
- provider.py
- test_get_interview.py
- interviews_controller.py
- LLMError
- build_usage_report
- interviews_context.py
- InvalidReplyError
- errors.py
- Role
- analyze_interview
- test_context_controller.py
- InterviewsController
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- test_job_description_summary.py
- Feature: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: SSE Streaming of the Interview Turn (Slice 4)
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- llm
- logging.py
- interviews_dependencies.py
- interviewer_v2.md
- job_description_summary_v1.md
- Learnings: Context Management
- test_openai_compatible_stream.py
- Checks
- Stats
- interviewer_v3.md
- interviews/conftest.py
- no_llm_env
- fixture
- test_evals.py
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- test_fallback_pick.py
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- Implementation Plan: Context Management for the Interview LLM Calls
- bank
- test_guards.py
- interviews_evals.py
- StreamedTurn
- interviews_route.py
- RequestContextMiddleware
- LLMResult
- test_llm_settings_default_to_off_with_documented_limits
- ConsoleFormatter
- test_factory.py
- clock
- test_request_context.py
- Affected Files & Patterns
- interviewer_v5.md
- stream_answer
- Clock
- main
- ProviderConfig

## God Nodes (most connected - your core abstractions)
1. `InterviewQuestion` - 71 edges
2. `InterviewsController` - 69 edges
3. `QuestionCategory` - 58 edges
4. `FakeProvider` - 54 edges
5. `InterviewType` - 54 edges
6. `InterviewSession` - 54 edges
7. `User` - 52 edges
8. `LLMResult` - 50 edges
9. `InterviewMessage` - 50 edges
10. `ChatMessage` - 47 edges

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

## Communities (124 total, 11 thin omitted)

### Community 0 - "User"
Cohesion: 0.09
Nodes (29): hash_password(), verify_password(), AuthController, Create `email` as an admin, or promote it if it exists. Safe to run repeatedly., get_controller(), Depends, Session, User (+21 more)

### Community 1 - "Feature: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Start an Interview (backend), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 2 - "app_logs"
Cohesion: 0.24
Nodes (11): get_bank(), get_llm_provider(), Request, The question source; tests override it with a fixture bank., Built once at startup (app lifespan); None when no key is configured or the…, Affected Files & Patterns, Affected Files & Patterns, Affected Files & Patterns (+3 more)

### Community 3 - "decode_token"
Cohesion: 0.08
Nodes (35): TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Affected Files & Patterns, Architecture & Design (+27 more)

### Community 4 - "exception_handlers.py"
Cohesion: 0.18
Nodes (23): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+15 more)

### Community 5 - "Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.25
Nodes (20): NotEnoughQuestionsError, InterviewType, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), _bank(), parametrize, _q(), _select() (+12 more)

### Community 8 - "users_route.py"
Cohesion: 0.12
Nodes (18): get_db(), Session, UsersController, Session, UsersRepository, get_controller(), list_users(), Depends (+10 more)

### Community 9 - "JobRole"
Cohesion: 0.12
Nodes (31): JobRole, Level, EvalSetup, load_bank(), load_prompt(), Path, Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never… (+23 more)

### Community 10 - "interviews_reply.py"
Cohesion: 0.11
Nodes (37): FollowUpAction, FollowUpGap, What the decide call may answer (a closed list: anything else is an invalid…, The one clear gap a follow-up targets. Closed, so the write call gets app data,…, Expect, The label for the decide call: the action it should pick, and the gap when only…, Decision, HeaderSplit (+29 more)

### Community 11 - "Implementation Steps"
Cohesion: 0.31
Nodes (13): login(), me(), AuthControllerDep, post, register(), LoginIn, MeOut, BaseModel (+5 more)

### Community 12 - "Implementation: Role-Based Access Control (single JWT)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: Role-Based Access Control (single JWT), Known Issues, Links, Open Questions (+5 more)

### Community 13 - "Implementation: UUID primary keys"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Deviations from Plan, Implementation: UUID primary keys, Known Issues, Links, Open Questions (+5 more)

### Community 14 - "test_config.py"
Cohesion: 0.21
Nodes (18): os, _google(), parametrize, _settings(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored(), test_api_key_never_shows_in_repr_or_errors(), test_blank_provider_list_means_llm_off() (+10 more)

### Community 15 - "test_logging.py"
Cohesion: 0.31
Nodes (10): `llm_call a=1 b=2` -> ("llm_call", [("a", "1"), ("b", "2")]). Any other message…, split_fields(), _record(), test_console_appends_the_traceback(), test_console_colours_outcome_by_success(), test_console_keeps_free_text_on_one_line(), test_console_puts_one_aligned_field_per_line(), test_console_without_colour_has_no_escape_codes() (+2 more)

### Community 16 - "QuestionTurn"
Cohesion: 0.09
Nodes (40): End the read transaction before a slow call, so no connection sits idle in a…, build_interviewer_messages(), interviewer_history(), job_description_block(), main_numbers(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,… (+32 more)

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.13
Nodes (40): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, LLMServerError, 5xx or a dropped connection: the provider's side failed., What a streamed answer turn is doing, sent as `status` events so the candidate…, TurnPhase, Delta (+32 more)

### Community 28 - "ContextManager"
Cohesion: 0.15
Nodes (20): ContextManager, LLMProvider, Protocol, _add_usage(), _case_inputs(), CaseResult, ReasoningEffort, The streamed turn's write call (interviewer_stream, v5) on one case: the same… (+12 more)

### Community 29 - "test_follow_ups.py"
Cohesion: 0.25
Nodes (17): Checkpoint A: the model suggests, the code enforces (concept 5), answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries() (+9 more)

### Community 30 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 31 - "Implementation Steps"
Cohesion: 0.12
Nodes (18): _check_question(), InterviewerReply, _normalized(), parse_streamed_reply(), interviewer_v5's finished question text, checked like a v4 reply. It was…, The rules every written question must pass, whatever format it came in., Implementation Steps, Phase A: plumbing and progress events (+10 more)

### Community 32 - "test_answer_stream.py"
Cohesion: 0.08
Nodes (18): assert_one_terminal(), follow_up_json(), message_count(), fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,…, started() (+10 more)

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
Cohesion: 0.08
Nodes (25): 10. Evaluation (the most important one), 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation, 5. The LLM decides, the code enforces, 6. Reliability, 7. Streaming and latency (+17 more)

### Community 37 - "InterviewMessage"
Cohesion: 0.14
Nodes (16): InterviewMessage, A candidate answer or the interviewer's reaction to one question. The questions…, message_count(), fixture, parametrize, An owner with a started 3-question interview: (owner, session_id, first…, started(), test_any_question_but_the_current_one_is_the_same_409() (+8 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Blockers, Changes to earlier specs, Constraints, Feature: LLM as the Interviewer (it asks the questions), Goal, Out of Scope, Problem, Project Conventions (+2 more)

### Community 39 - "ChatMessage"
Cohesion: 0.10
Nodes (28): BuiltContext, ContextReport, ContextTooLargeError, estimate_tokens(), _log(), Exception, NamedTuple, Context management: the one place that decides what each LLM call sends. The… (+20 more)

### Community 40 - "test_context_strategies.py"
Cohesion: 0.17
Nodes (37): Checkpoint C: what a follow-up costs in context (concept 2), decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap() (+29 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.15
Nodes (27): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+19 more)

### Community 44 - "test_answer_llm.py"
Cohesion: 0.08
Nodes (30): Checkpoint A: after Step 3 (provider package), Checkpoint B: after Step 5 (prompt and message building), Checkpoint C: after Steps 6-7 (answer state machine and guards), Checkpoint D: after Step 8 (LLM in the answer flow), Checkpoint E: after Step 9 (usage logging), Checkpoint F: after Step 10 (transcript endpoint), Checkpoint G: after Step 11 (real API, Proof round), Learnings: LLM Slice 1 (Interviewer Reaction) (+22 more)

### Community 45 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 46 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "Implementation: Error Handling"
Cohesion: 0.14
Nodes (13): RequestIdFilter, Baseline Failures, Deviations from Plan, Implementation: Error Handling, Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 49 - "tests/conftest.py"
Cohesion: 0.13
Nodes (22): health_check(), lifespan(), FastAPI, Completed Steps, Affected Files & Patterns, fastapi_testclient, sqlalchemy_pool, auth_header() (+14 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.11
Nodes (22): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Base, Print stored LLM usage per interview: tokens per question position and per… (+14 more)

### Community 51 - "QuestionCategory"
Cohesion: 0.12
Nodes (32): LevelGroup, QuestionCategory, Reactions are warmer for people early in their career and briefer for…, read(), interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), pick_reaction(), A predefined, neutral acknowledgement for the answer just given; never the same… (+24 more)

### Community 52 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 53 - "FakeProvider"
Cohesion: 0.23
Nodes (18): FakeProvider, run_case(), long_case(), noted(), reply(), test_a_provider_error_fails_the_case_without_crashing(), test_a_v3_window_reply_must_carry_a_note_when_there_is_an_answer(), test_an_unusable_summary_falls_back_to_the_original() (+10 more)

### Community 54 - "interviews_turn.py"
Cohesion: 0.11
Nodes (34): InterviewerInputs, Plain values for one interviewer or decide call., Condense a long job description once, so later calls send less. One attempt…, Deadline, _decision_label(), Interviewer, _log_error(), log_llm_call() (+26 more)

### Community 55 - "test_interview_report.py"
Cohesion: 0.07
Nodes (86): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, What needs attention comes first (watch, checks), then the sections, then the…, render_html(), render_text(), log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, html_target() (+78 more)

### Community 56 - "Bundle"
Cohesion: 0.15
Nodes (16): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+8 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.19
Nodes (23): analyze_rollup(), _avg(), _cost(), _counts(), _effectiveness(), _efficiency(), _latency_row(), _limit_tone() (+15 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.15
Nodes (29): completion(), make_provider(), parametrize, A chat-completions body in the OpenAI-compatible shape (Google AI Studio,…, Provider whose HTTP layer is a scripted list of responses (or exceptions), one…, test_a_larger_budget_argument_never_raises_the_configured_budget(), test_a_smaller_budget_argument_caps_retries(), test_cached_and_reasoning_tokens_are_none_when_not_reported() (+21 more)

### Community 59 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 60 - "OpenAICompatibleProvider"
Cohesion: 0.17
Nodes (10): _int_or_none(), OpenAICompatibleProvider, Any, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final…, How long to wait before retrying, or None to give up., One streamed request: its text chunks, then an LLMResult (attempts and latency… (+2 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.13
Nodes (16): InterviewQuestion, InterviewSession, A question as it was shown: written by the LLM, or snapshotted from the bank…, InterviewsRepository, Session, UUID, Save one whole turn in one commit: advance the session, the answer, the…, Abandon the user's active session and save the new one with its questions, all… (+8 more)

### Community 62 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.10
Nodes (21): get_current_user(), AuthControllerDep, Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, require_roles(), check(), bearer_scheme, Affected Files & Patterns, Architecture & Design (+13 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_create_interview.py"
Cohesion: 0.16
Nodes (18): sqlalchemy_exc, parametrize, _question_count(), _questions(), _sessions(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session(), test_failure_while_saving_questions_rolls_everything_back() (+10 more)

### Community 65 - "test_stream_answer.py"
Cohesion: 0.18
Nodes (15): anyio, test_other_requests_are_served_while_a_stream_waits_on_the_llm(), stream(), fixture, InterviewsController.stream_answer driven directly, for what a test client…, A started interview and a controller wired like the app's: returns (controller,…, saved_answers(), summaries() (+7 more)

### Community 66 - "provider.py"
Cohesion: 0.07
Nodes (11): Test double for LLMProvider: scripted replies or errors, records every call.…, _raise_for_status(), OpenAI-compatible chat completions over plain httpx (Google AI Studio,…, LLMRateLimitError, LLMRequestError, The LLM contract every feature codes against: message/result types, typed…, Other 4xx (bad key, bad request): retrying sends the same broken request again., collections (+3 more)

### Community 67 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 68 - "interviews_controller.py"
Cohesion: 0.10
Nodes (48): MessageKind, MessageRole, StrEnum, QuestionKind, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, A main question opens a thread; a follow-up digs into the latest answer of that…, Transcript item kinds: a question comes from interview_questions, the other two… (+40 more)

### Community 71 - "LLMError"
Cohesion: 0.16
Nodes (9): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, LLMError, Exception, Base for every provider failure. `retryable` marks faults that may pass on…, Step 11: `FakeProvider.stream`, Step 9: The provider contract in `app/core/ai/provider.py`, Completed Steps (+1 more)

### Community 72 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 73 - "interviews_context.py"
Cohesion: 0.11
Nodes (25): StrategyOutput, Task, build_context_manager(), _counts(), FollowUpDecision, FullHistory, JobDescriptionSummary, NamedTuple (+17 more)

### Community 74 - "InvalidReplyError"
Cohesion: 0.07
Nodes (50): InvalidReplyError, parse_interviewer_reply(), Exception, Checkpoint B: a small closed decision instead of free text (concept 4), Checkpoint D: labelled evals for a decision (concept 10), Checkpoint E: one deadline for two calls (concept 9), Learnings: Follow-up Questions (decide / write split), Blockers (+42 more)

### Community 75 - "errors.py"
Cohesion: 0.08
Nodes (40): AppError, BadRequestError, ConflictError, ErrorBody, ErrorResponse, ForbiddenError, InvalidCredentialsError, Any (+32 more)

### Community 76 - "Role"
Cohesion: 0.09
Nodes (21): Permission, permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, enum, fastapi_security, parametrize (+13 more)

### Community 77 - "analyze_interview"
Cohesion: 0.19
Nodes (15): analyze_interview(), _call_table(), _dash(), _facts(), _question_table(), Turn N answers the question at position N and asks position N+1: positions are…, Time limits nearly used up, failed or odd calls, overrides, fallbacks, missing…, _rollup_table() (+7 more)

### Community 78 - "test_context_controller.py"
Cohesion: 0.32
Nodes (10): candidate_messages(), noted(), run(), test_a_bad_note_is_dropped_the_question_kept_and_nothing_retried(), test_a_too_large_context_uses_the_bank_without_calling_the_llm(), test_a_valid_note_is_stored_and_shown_in_later_ledgers(), test_no_note_after_a_bank_fallback_or_for_the_final_answer(), test_notes_never_appear_in_responses_or_logs() (+2 more)

### Community 79 - "InterviewsController"
Cohesion: 0.11
Nodes (24): NotFoundError, QuestionNotCurrentError, SessionNotInProgressError, InterviewsController, InterviewSetup, _llm_question(), NamedTuple, UUID (+16 more)

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.13
Nodes (14): 0. Rename the provider; per-vendor config, Changes Made, Current Step, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions (+6 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 82 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 83 - "Feature: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.14
Nodes (13): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: SSE Streaming of the Interview Turn (Slice 4), Functional, Goal, Non-Functional (+5 more)

### Community 84 - "Implementation Plan: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.20
Nodes (9): ActionKnown, The turn's final action, sent only once nothing can change it (a follow-up only…, Blockers & Resolutions, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Overview, Project Rules Applied, Ready to Implement, Spec Requirements -> Implementation (+1 more)

### Community 85 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 86 - "llm"
Cohesion: 0.22
Nodes (7): Skills Consulted, as_v5_text(), llm(), script(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY…

### Community 87 - "logging.py"
Cohesion: 0.25
Nodes (7): setup_logging(), contextvars, logging_config, re, starlette_types, sys, time

### Community 88 - "interviews_dependencies.py"
Cohesion: 0.24
Nodes (9): get_clock(), get_context_manager(), get_controller(), Depends, Session, Monotonic clock for the per-turn LLM time budget; tests swap in a fake one., Decides what each LLM call sends; tests swap in one with a tiny limit., fixture (+1 more)

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
Cohesion: 0.12
Nodes (27): LLMBadResponseError, A 200 whose body is unusable (not JSON, no choices, blank text). Not transient,…, anyio_backend(), chunk(), Clock, drain(), Interrupted, make_provider() (+19 more)

### Community 93 - "Checks"
Cohesion: 0.40
Nodes (5): Checks, bad_parent(), _consistency(), Each check with the problems it found (none = passed)., Does what the log says happened match what was stored? These guard the numbers…

### Community 94 - "Stats"
Cohesion: 0.22
Nodes (8): _answer_growth(), The numbers the sections and tiles share, worked out once over a list of…, How each follow-up thread was closed, read from the turn that answered its last…, Each follow-up answer's length relative to the answer before it (characters…, Stats, decide(), _thread_endings(), Counter

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "interviews/conftest.py"
Cohesion: 0.28
Nodes (7): Random, BankQuestion, One entry of the hand-written question bank file., _unique_ids(), Deviations from Plan, _bank_question(), make_bank_question()

### Community 97 - "no_llm_env"
Cohesion: 0.67
Nodes (3): no_llm_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…

### Community 98 - "fixture"
Cohesion: 0.18
Nodes (11): answer(), _answer(), anyio_backend(), _decision_json(), fixture, Builds a reply in the exact shape the decide call must produce., Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a setup for `user`; any field can be overridden, or dropped by passing… (+3 more)

### Community 99 - "test_evals.py"
Cohesion: 0.14
Nodes (29): check_decision(), load_cases(), Path, The decide reply against the case's label; the injection check reads the raw…, One decide call on the case's latest answer, as the app makes it after every…, run_decide_case(), case(), decision() (+21 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "test_fallback_pick.py"
Cohesion: 0.18
Nodes (16): pick_fallback_question(), Random, One unused bank question for `position`, used when the LLM is off or its reply…, Collection, random, fixture_bank(), pick(), fixture (+8 more)

### Community 104 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (15): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional (+7 more)

### Community 105 - "Implementation Plan: Context Management for the Interview LLM Calls"
Cohesion: 0.22
Nodes (8): Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Trade-offs & Rationale

### Community 106 - "bank"
Cohesion: 0.22
Nodes (9): Acceptance Criteria, Acceptance Criteria, Edge Cases, Functional, Non-Functional, Requirements, Test Results, bank() (+1 more)

### Community 107 - "test_guards.py"
Cohesion: 0.12
Nodes (21): CurrentUserDep, fastapi, admin_role(), _assert_401(), authenticated(), parametrize, read_and_read_self(), test_bad_tokens_are_token_invalid() (+13 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.11
Nodes (34): anyio_from_thread, Check, check_reply(), check_streamed_reply(), DecisionSummary, EvalCase, EvalTurn, main() (+26 more)

### Community 109 - "StreamedTurn"
Cohesion: 0.25
Nodes (6): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, Builds a reply in the exact shape the interviewer LLM must produce., _reply_json(), StreamedTurn

### Community 110 - "interviews_route.py"
Cohesion: 0.19
Nodes (19): Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), check(), answer_question(), answer_question_stream(), get_interview(), get_transcript(), post (+11 more)

### Community 111 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 112 - "LLMResult"
Cohesion: 0.32
Nodes (6): LLMResult, ReasoningEffort, The reply as it is generated: text chunks, then one final LLMResult (the joined…, Step 13: The streamed write step in `stream_turn`, test_usage_is_stored_with_the_question_it_produced(), result()

### Community 113 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.50
Nodes (5): Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 114 - "ConsoleFormatter"
Cohesion: 0.36
Nodes (3): ConsoleFormatter, Dev console only: colours, and one field per line for `event key=value ...`…, LogRecord

### Community 115 - "test_factory.py"
Cohesion: 0.12
Nodes (20): build_provider(), The one place that picks the implementation; swapping vendor or model is a…, LLMTimeoutError, Settings, BaseSettings, Step 0: Rename the provider to a vendor-neutral name, field_validator, model_validator (+12 more)

### Community 116 - "clock"
Cohesion: 0.25
Nodes (4): _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 117 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 118 - "Affected Files & Patterns"
Cohesion: 0.33
Nodes (5): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "stream_answer"
Cohesion: 0.29
Nodes (7): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream(), test_done_has_the_json_endpoints_shape_and_content(), run()

### Community 121 - "Clock"
Cohesion: 0.33
Nodes (3): Clock, fixture, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant.

### Community 122 - "main"
Cohesion: 0.60
Nodes (4): main(), Session, test_an_empty_database(), test_reports_stored_questions_grouped_by_interview()

### Community 123 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

## Knowledge Gaps
- **313 isolated node(s):** `cuewise-be`, `About the Project`, `Git Rules (STRICT)`, `Tooling`, `Architecture: Modular, Feature-Driven` (+308 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 802 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `InterviewsController` connect `InterviewsController` to `User`, `interviews/conftest.py`, `test_stream_answer.py`, `interviews_controller.py`, `InterviewMessage`, `InterviewType`, `LLMError`, `JobRole`, `interviews_context.py`, `InvalidReplyError`, `QuestionTurn`, `QuestionCategory`, `Implementation Plan: SSE Streaming of the Interview Turn (Slice 4)`, `interviews_turn.py`, `interviews_dependencies.py`, `test_stream_turn.py`, `ContextManager`, `InterviewQuestion`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `interviews_reply.py`, `QuestionTurn`, `test_follow_ups.py`, `test_start_llm.py`, `test_answer_stream.py`, `InterviewMessage`, `test_answer_llm.py`, `test_transcript.py`, `interviews_model.py`, `test_turn_budget.py`, `test_interview_report.py`, `Bundle`, `interviews_report.py`, `test_create_interview.py`, `interviews_controller.py`, `build_usage_report`, `analyze_interview`, `test_context_controller.py`, `InterviewsController`, `Checks`, `Stats`, `LLMResult`, `main`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `test_create_interview.py`, `decode_token`, `interviews_controller.py`, `users_route.py`, `Implementation Steps`, `Role`, `interviews_route.py`, `InterviewsController`, `tests/conftest.py`, `interviews_model.py`, `InterviewQuestion`, `Implementation Plan: Role-Based Access Control (single JWT)`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Are the 27 inferred relationships involving `InterviewQuestion` (e.g. with `InterviewsController` and `TurnContext`) actually correct?**
  _`InterviewQuestion` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 47 inferred relationships involving `InterviewsController` (e.g. with `ContextManager` and `LLMError`) actually correct?**
  _`InterviewsController` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `QuestionCategory` (e.g. with `InterviewsController` and `Thread`) actually correct?**
  _`QuestionCategory` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 17 INFERRED edges - model-reasoned connections that need verification._