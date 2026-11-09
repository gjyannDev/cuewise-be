# Graph Report - cuewise-be  (2026-11-09)

## Corpus Check
- 271 files · ~233,417 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 3, .example 1, .ini 1)

## Summary
- 3713 nodes · 10188 edges · 220 communities (176 shown, 44 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1859 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `58832e23`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- typing
- LLMServerError
- interviews_answer_service.py
- decode_token
- test_interview_report.py
- Transcriber
- Cuewise BE — Project Instructions
- InterviewType
- interviews_dependencies.py
- Role
- interviews_reply.py
- test_list_interviews.py
- Implementation: Role-Based Access Control (single JWT)
- Implementation: UUID primary keys
- test_config.py
- test_deepgram.py
- build_context_manager
- test_feedback_evals.py
- README.md
- test_tracing_lifespan.py
- cuewise-be
- Implementation: Start an Interview (backend)
- test_stream_turn.py
- test_feedback_endpoint.py
- test_context_strategies.py
- test_answer_stream.py
- test_feedback_contract.py
- Level
- Feature: Context Management for the Interview LLM Calls
- Implementation: Eval runs in Langfuse (scores + datasets)
- Implementation: LLM as the Interviewer (it asks the questions)
- QuestionTurn
- InvalidReplyError
- Feature: LLM as the Interviewer (it asks the questions)
- stream_answer
- test_layers.py
- Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_error_handling.py
- interviews_report_render.py
- interviews_schema.py
- interviews_answer_controller.py
- test_transcribe.py
- Implementation: Follow-up Questions (decide / write split)
- test_tracing.py
- JobRole
- interviews_model.py
- LLMTimeoutError
- interviews/conftest.py
- test_create_interview.py
- test_start_llm.py
- interviews_utils.py
- provider.py
- interviews_report.py
- test_openai_compatible.py
- tests/conftest.py
- tracing.py
- InterviewQuestion
- interviews_log.py
- job_description_summary_v2.md
- test_follow_ups.py
- test_stream_answer.py
- test_context.py
- test_request_context.py
- Implementation Steps
- hint_for
- Any
- interviews_feedback_evals.py
- logging.py
- errors.py
- compute_overall
- QuestionKind
- interviews_feedback_controller.py
- RecordingClient
- Langfuse CLI Reference
- Implementation: SSE Streaming of the Interview Turn (Slice 4)
- Implementation Plan: Follow-up Questions (decide / write split)
- interviews_session_utils.py
- RateLimiter
- AnswerOut
- Implementation Plan: Role-Based Access Control (single JWT)
- validate_summary
- .trace
- follow_up
- interviewer_v2.md
- job_description_summary_v1.md
- Learn: Context management (what to send, and what it costs)
- QuestionCategory
- interviews_feedback_turn.py
- Langfuse Observability
- interviewer_v3.md
- Tracer
- no_llm_env
- Implementation: Langfuse Tracing
- interviews_feedback.py
- follow_up_decision_v1.md
- interviewer_v4.md
- Implementation: Context Management for the Interview LLM Calls
- pytest
- User
- test_answer_llm.py
- Implementation Plan: LLM as the Interviewer (it asks the questions)
- Langfuse Dataset Construction
- interviews_evals.py
- fixture
- main
- interviews_turn.py
- Feature: Langfuse Tracing
- Langfuse
- test_evals.py
- 9d04cd22055a_use_uuid_primary_key_for_users.py
- test_transcript.py
- interviews_feedback_service.py
- Langfuse Implementation Notes
- interviewer_v5.md
- LLMResult
- llm
- Implementation Plan: UUID primary keys
- Feature: Follow-up Questions (decide / write split)
- Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)
- test_turn_budget.py
- .write
- Feature: Interview History List (backend)
- Langfuse Dataset Construction
- Langfuse v4 project migration
- run_feedback
- Implementation: Interview History List (backend)
- Judge Calibration
- Langfuse Prompt Migration
- build_usage_report
- LLMProvider
- Langfuse CI/CD
- Prompt Engineering
- TranscriptionResult
- Langfuse Implementation Notes
- test_get_interview.py
- test_create_admin.py
- FeedbackCaseResult
- PageParams
- Langfuse v4 project migration
- Judge Calibration
- Langfuse Prompt Migration
- Langfuse CI/CD
- Prompt Engineering
- test_context_controller.py
- get_llm_provider
- test_feedback_context.py
- Feature: Layered Modules (route -> controller -> service -> repository)
- RecordingClient
- ContextManager
- Implementation Plan: Langfuse Tracing
- Implementation: Interview Feedback and Scoring (Slice 6)
- clock
- The fundamentals
- Implementation Plan: Eval runs in Langfuse (scores + datasets)
- test_answer_interview.py
- test_job_description_summary.py
- split_header
- ErrorResponse
- .update_claimed_feedback
- RequestContextMiddleware
- Implementation Plan: Interview Feedback and Scoring (Slice 6)
- StreamedTurn
- traces
- failed
- feedback_score_v2.md
- test_llm_settings_default_to_off_with_documented_limits
- .__init__
- feedback_score_v1.md
- feedback_write_v1.md
- build_tracer
- FakeObservation
- Affected Files & Patterns
- Langfuse
- test_keyterms.py
- .agents/skills/langfuse/SKILL.md
- ProviderConfig
- Langfuse CLI Reference
- 2. Langfuse Documentation
- SummaryInputs
- 2. Langfuse Documentation
- ._covers_every_criterion
- ._ordered
- sse_frames
- started
- users_utils.py
- _reset_request_id

## God Nodes (most connected - your core abstractions)
1. `User` - 97 edges
2. `FakeProvider` - 91 edges
3. `InterviewQuestion` - 88 edges
4. `LLMResult` - 80 edges
5. `QuestionCategory` - 79 edges
6. `JobRole` - 78 edges
7. `InterviewType` - 78 edges
8. `Tracer` - 73 edges
9. `InterviewSession` - 70 edges
10. `InterviewsRepository` - 70 edges

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

## Communities (220 total, 44 thin omitted)

### Community 0 - "typing"
Cohesion: 0.10
Nodes (30): AuthController, Request -> service call, domain result -> response schema., get_controller(), get_service(), Depends, Session, AuthRepository, Session (+22 more)

### Community 1 - "LLMServerError"
Cohesion: 0.07
Nodes (33): anyio, DeepgramTranscriber, _parse(), AsyncBaseTransport, Random, Response, Deepgram pre-recorded speech-to-text (`POST /v1/listen`, Nova models) over…, The first channel's best transcript (blank for silence) and the reported audio… (+25 more)

### Community 2 - "interviews_answer_service.py"
Cohesion: 0.07
Nodes (47): QuestionNotCurrentError, SessionNotInProgressError, ActionKnown, log_stream_summary(), The turn's final action, sent only once nothing can change it (a follow-up only…, How a streamed turn felt and ended: time to the first event and to the first…, AnswerController, UUID (+39 more)

### Community 3 - "decode_token"
Cohesion: 0.13
Nodes (27): TokenExpiredError, TokenInvalidError, create_token(), decode_token(), Any, UUID, datetime, Implementation Steps (+19 more)

### Community 4 - "test_interview_report.py"
Cohesion: 0.14
Nodes (50): log_turn_summary(), Why the turn ended as it did: the only place an overridden follow-up or a bank…, answer(), emit_answer_turn(), emit_call(), emit_follow_up_turn(), emit_http(), emit_start() (+42 more)

### Community 5 - "Transcriber"
Cohesion: 0.20
Nodes (7): Protocol, `audio` is a whole recording in a container the vendor detects itself (WebM,…, Transcriber, get_transcriber(), Request, Built once at startup (app lifespan); None when no Deepgram key is configured…, Slice 8: Embeddings and RAG

### Community 6 - "Cuewise BE — Project Instructions"
Cohesion: 0.14
Nodes (13): About the Project, AI Engineering Guidelines, Architecture: Modular, Feature-Driven, Code Principles, Common Commands, Cuewise BE — Project Instructions, Don'ts, FastAPI Best Practices & Standards (+5 more)

### Community 7 - "InterviewType"
Cohesion: 0.12
Nodes (36): NotEnoughQuestionsError, InterviewType, pick_fallback_question(), Random, One unused bank question for `position`, used when the LLM is off or its reply…, Pick `count` distinct questions for the setup, in interview order. The single…, select_questions(), Collection (+28 more)

### Community 8 - "interviews_dependencies.py"
Cohesion: 0.21
Nodes (21): get_db(), Session, get_answer_controller(), get_answer_service(), get_context_manager(), get_feedback_controller(), get_feedback_service(), get_interviews_controller() (+13 more)

### Community 9 - "Role"
Cohesion: 0.07
Nodes (34): permissions_for(), StrEnum, The only reader of ROLE_PERMISSIONS, so a DB-backed lookup can replace it later., Role, check(), test_admin_holds_every_user_permission(), test_every_role_has_a_permission_entry(), test_unknown_role_has_no_permissions_and_is_logged() (+26 more)

### Community 10 - "interviews_reply.py"
Cohesion: 0.12
Nodes (33): WindowLedger, Decision, HeaderSplit, parse_decision_reply(), BaseModel, NamedTuple, The contract for what the interviewer LLM must reply, and the check that…, The decide call suggests; the code still applies the follow-up cap and the time… (+25 more)

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
Cohesion: 0.14
Nodes (25): _google(), parametrize, _settings(), test_a_blank_deepgram_key_counts_as_unset(), test_a_deepgram_key_turns_transcription_on_and_never_shows(), test_a_listed_provider_needs_its_key_model_and_url(), test_a_vendor_block_that_is_not_listed_is_ignored(), test_api_key_never_shows_in_repr_or_errors() (+17 more)

### Community 15 - "test_deepgram.py"
Cohesion: 0.14
Nodes (25): anyio_backend(), Clock, listen_body(), make_transcriber(), ok(), fixture, parametrize, Response (+17 more)

### Community 16 - "build_context_manager"
Cohesion: 0.11
Nodes (17): build_context_manager(), _counts(), FollowUpDecision, FullHistory, An earlier question as the model would have written it. A follow-up was written…, The decide call: the current thread in full (it judges the latest answer within…, App data at the end of the last user message; untrusted parts (questions,…, `prompts` maps a strategy name to a prompt version (the eval runner's --prompt,… (+9 more)

### Community 17 - "test_feedback_evals.py"
Cohesion: 0.12
Nodes (31): feedback_scores_for(), One case through the same pre-check, score call, write call and template…, (name, value, comment) per check, plus `valid_reply` and `case_passed`. An…, run_feedback_case(), _usage(), case(), Grader, Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The… (+23 more)

### Community 20 - "test_tracing_lifespan.py"
Cohesion: 0.25
Nodes (6): fastapi_testclient, The app lifespan builds the tracer once and flushes it on shutdown (langfuse-…, RecordingClient, _run_app(), test_shutdown_completes_even_when_the_flush_fails(), test_shutdown_flushes_then_stops_the_tracer()

### Community 26 - "Implementation: Start an Interview (backend)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Implementation: Start an Interview (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation (+5 more)

### Community 27 - "test_stream_turn.py"
Cohesion: 0.13
Nodes (38): FakeStream, NamedTuple, A scripted streamed reply: these chunks (each after `delay` seconds), then…, Delta, PhaseChanged, StrEnum, The next chunk of the question being written (shown as it arrives)., The question text streamed so far is taken back: that draft failed, another one… (+30 more)

### Community 28 - "test_feedback_endpoint.py"
Cohesion: 0.06
Nodes (75): FeedbackWrite, The write call: scores, evidence and question texts only; small whatever the…, get_feedback_limiter(), Tests swap in a fresh limiter so counts never leak between them., InterviewFeedback, The end-of-interview feedback: at most one per interview (the unique session_id…, The first claim of an interview's feedback. False when another request inserted…, 1. Why it exists (+67 more)

### Community 29 - "test_context_strategies.py"
Cohesion: 0.18
Nodes (34): decide(), fu(), full(), inputs(), parametrize, Follow-up k on main question i., test_a_follow_up_write_call_states_the_follow_up_and_its_gap(), test_a_maximum_interview_stays_under_the_limit_and_beats_full_history_once_it_outgrows_the_window() (+26 more)

### Community 30 - "test_answer_stream.py"
Cohesion: 0.07
Nodes (21): assert_one_terminal(), follow_up_json(), message_count(), anyio, fixture, parametrize, POST /interviews/{id}/messages/stream: one answer turn as Server-Sent Events…, An owner with a started 3-question behavioral interview: (owner, session_id,… (+13 more)

### Community 31 - "test_feedback_contract.py"
Cohesion: 0.20
Nodes (30): assess_evidence(), parse_score_reply(), The score call's closed JSON, checked against the interview it scored. Raises…, The pre-check, before any LLM call: enough main questions have a real answer to…, parametrize, question_json(), The feedback contract (interviews_feedback.py): the code pre-check, the score…, reason_of() (+22 more)

### Community 32 - "Level"
Cohesion: 0.11
Nodes (28): Criterion, Level, LevelGroup, StrEnum, What the score call rates, 1 to 5. Which ones apply depends on the question's…, Reactions are warmer for people early in their career and briefer for…, The feedback rubric file: ground truth for every score, versioned like a prompt., Rubric (+20 more)

### Community 33 - "Feature: Context Management for the Interview LLM Calls"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Context Management for the Interview LLM Calls, Functional, Goal, Non-Functional (+6 more)

### Community 34 - "Implementation: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Baseline Failures, Deviations from Plan, Implementation: Eval runs in Langfuse (scores + datasets), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 35 - "Implementation: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.14
Nodes (13): Baseline Failures, Changes Made, Completed Steps, Current Step, Implementation: LLM as the Interviewer (it asks the questions), Known Issues, Links, Open Questions (+5 more)

### Community 36 - "QuestionTurn"
Cohesion: 0.11
Nodes (31): build_interviewer_messages(), job_description_block(), NamedTuple, QuestionTurn, One answered question as the interviewer LLM sees it (reactions are app copy,…, Fill {{name}} placeholders in one pass: inserted values are never scanned…, Only trusted values go in here; the job description and answers never enter the…, Untrusted text, fenced as data. Tags inside it are neutralised so it can't… (+23 more)

### Community 37 - "InvalidReplyError"
Cohesion: 0.17
Nodes (27): _check_question(), InvalidReplyError, load_object(), _normalized(), parse_interviewer_reply(), Exception, The rules every written question must pass, whatever format it came in., The reply as a JSON object: one optional fence around it, nothing else before… (+19 more)

### Community 38 - "Feature: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.11
Nodes (19): Acceptance Criteria, Acceptance Criteria, Blockers, Changes to earlier specs, Constraints, Edge Cases, Feature: LLM as the Interviewer (it asks the questions), Functional (+11 more)

### Community 39 - "stream_answer"
Cohesion: 0.29
Nodes (7): parse_sse(), Split a text/event-stream body into (event, data) pairs; returns them and the…, POST an answer to the streaming endpoint and read the whole stream (or the JSON…, stream_answer(), _stream(), test_done_has_the_json_endpoints_shape_and_content(), run()

### Community 40 - "test_layers.py"
Cohesion: 0.10
Nodes (27): ast, Blockers & Resolutions, Deviations from the spec (approved by the user; spec.md updated to match), Implementation Plan: Layered Modules (route -> controller -> service -> repository), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+19 more)

### Community 41 - "Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.12
Nodes (16): 11. Live verification (waiting on the owner), Baseline Failures, Changes Made, Completed Steps, Current Step, Deviations from Plan, Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Known Issues (+8 more)

### Community 42 - "test_error_handling.py"
Cohesion: 0.27
Nodes (10): error_of(), test_app_error_returns_standard_shape(), test_auth_error_sends_bearer_challenge_and_specific_code(), test_crash_details_shown_only_in_debug(), test_crash_returns_generic_500_without_details(), test_database_unreachable_returns_503(), test_integrity_error_returns_generic_conflict(), test_malformed_json_returns_readable_validation_error() (+2 more)

### Community 43 - "interviews_report_render.py"
Cohesion: 0.13
Nodes (30): Metric, One number with its meaning. `fraction` (0..1) draws a meter in the HTML;…, _cell_class(), _heading(), _html_block(), _html_header(), _html_item(), _html_list_card() (+22 more)

### Community 44 - "interviews_schema.py"
Cohesion: 0.19
Nodes (21): HistorySortColumn, The history columns GET /interviews sorts by; the values are the response's…, SessionStatus, SortDirection, interview_out(), InterviewsController, UUID, question_out() (+13 more)

### Community 45 - "interviews_answer_controller.py"
Cohesion: 0.16
Nodes (23): The SSE event names of a streamed turn: the contract with the client. `done`…, StreamEvent, answer_out(), _error_event(), _event(), _frame(), AnswerEvent, BaseModel (+15 more)

### Community 46 - "test_transcribe.py"
Cohesion: 0.12
Nodes (15): code(), fixture, parametrize, An owner with a started backend interview: (owner, session_id)., started(), test_a_blank_transcript_is_no_speech(), test_a_disallowed_type_or_mismatched_signature_is_415(), test_a_reported_duration_over_125_s_is_too_long() (+7 more)

### Community 47 - "Implementation: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): 12. Measure, tune, document, Changes Made, Current Step, Deviations from Plan, Implementation: Follow-up Questions (decide / write split), Known Issues, Links, Open Questions (+5 more)

### Community 48 - "test_tracing.py"
Cohesion: 0.13
Nodes (18): drain(), Langfuse tracing: the Tracer (on/off, fail-open) and the TracingProvider…, result(), test_call_without_labels_still_gets_a_name(), test_complete_records_one_generation_with_full_content_and_usage(), test_disabled_tracer_is_a_pass_through(), test_failed_call_is_marked_error_and_the_same_exception_is_raised(), test_missing_usage_is_omitted_never_guessed() (+10 more)

### Community 49 - "JobRole"
Cohesion: 0.19
Nodes (21): What the interview LLM calls send: the tasks and strategies registered with the…, JobRole, load_prompt(), Per-interview constants only, so the text is identical on every call of an…, Per-interview constants only, like v2: the decide call's system prompt never…, render_decision_prompt(), render_interviewer_v2_prompt(), render_summary_prompt() (+13 more)

### Community 50 - "interviews_model.py"
Cohesion: 0.05
Nodes (20): Run migrations in 'offline' mode. This configures the context with just a URL…, Run migrations in 'online' mode. In this scenario we need to create an Engine…, run_migrations_offline(), run_migrations_online(), Base, UUID, Create the first admin, or promote an existing user to admin. Usage: uv run…, Print the cost, effectiveness and efficiency of the interviewer. Numbers and… (+12 more)

### Community 51 - "LLMTimeoutError"
Cohesion: 0.15
Nodes (13): LLMTimeoutError, Draft, One streamed write attempt, finished: the category (from its CATEGORY line, or…, One streamed attempt: the question's text chunks (never the CATEGORY line),…, 1. Why it exists, 3. When to use it, 4. How it works, 5. What can go wrong (+5 more)

### Community 52 - "interviews/conftest.py"
Cohesion: 0.18
Nodes (15): BankQuestion, One entry of the hand-written question bank file., _unique_ids(), load_bank(), Read and validate a question bank file; a bad file fails loudly instead of at…, Deviations from Plan, json, _bank_question() (+7 more)

### Community 53 - "test_create_interview.py"
Cohesion: 0.15
Nodes (19): parametrize, _question_count(), _questions(), _sessions(), test_database_rejects_two_in_progress_sessions_for_one_user(), session_for(), test_different_users_each_keep_their_own_in_progress_session(), test_editing_the_bank_never_changes_a_saved_session() (+11 more)

### Community 54 - "test_start_llm.py"
Cohesion: 0.19
Nodes (15): llm_lines(), parametrize, result(), stored_questions(), test_a_provider_error_falls_back_to_the_bank_without_a_retry(), test_an_invalid_reply_is_retried_once(), test_cache_and_reasoning_tokens_are_logged_when_reported(), test_every_call_logs_one_line_without_any_content() (+7 more)

### Community 55 - "interviews_utils.py"
Cohesion: 0.22
Nodes (16): AudioContainer, MessageKind, Recording containers a voice answer may arrive in (what browsers' MediaRecorder…, Transcript item kinds: a question comes from interview_questions, the other two…, answered_main_questions(), audio_container(), _has_signature(), The container of an uploaded recording, or None when its declared type isn't… (+8 more)

### Community 56 - "provider.py"
Cohesion: 0.10
Nodes (33): LLMBadResponseError, LLMRateLimitError, LLMRequestError, The LLM contract every feature codes against: message/result types, typed…, Other 4xx (bad key, bad request): retrying sends the same broken request again., A 200 whose body is unusable (not JSON, no choices, blank text). Not transient,…, 7. What surprised me, Eval log (+25 more)

### Community 57 - "interviews_report.py"
Cohesion: 0.10
Nodes (51): analyze_interview(), analyze_rollup(), _answer_growth(), _avg(), Bundle, _call_table(), Checks, _consistency() (+43 more)

### Community 58 - "test_openai_compatible.py"
Cohesion: 0.12
Nodes (32): Clock, completion(), make_provider(), fixture, parametrize, A chat-completions body in the OpenAI-compatible shape that Google AI Studio,…, Fake monotonic clock: `sleep` advances it, so retry timing is exact and instant., Provider whose HTTP layer is a scripted list of responses (or exceptions), one… (+24 more)

### Community 59 - "tests/conftest.py"
Cohesion: 0.06
Nodes (40): RequestIdFilter, hash_password(), health_check(), CurrentUserDep, Baseline Failures, Completed Steps, Deviations from Plan, Implementation: Error Handling (+32 more)

### Community 60 - "tracing.py"
Cohesion: 0.10
Nodes (12): Generation, _model_parameters(), ReasoningEffort, Langfuse tracing behind the LLMProvider contract: nothing outside `core/ai/`…, What the call asked the model for, shown on the generation. A temperature only…, One LLM call as Langfuse sees it. Ends exactly once; every method is safe to…, The stream was closed before it finished (client left, or the turn's deadline…, _usage_details() (+4 more)

### Community 61 - "InterviewQuestion"
Cohesion: 0.06
Nodes (47): InterviewMessage, InterviewQuestion, InterviewSession, A candidate answer or the interviewer's reaction to one question. The questions…, A question as it was shown: written by the LLM, or snapshotted from the bank…, _history_filter(), _history_order(), InterviewsRepository (+39 more)

### Community 62 - "interviews_log.py"
Cohesion: 0.15
Nodes (14): Call, group_requests(), _int(), LogEvent, NamedTuple, Reading the app's own log back: what each request did for an interview, from…, One `llm_call` line, with the size the context builder estimated for its input…, One HTTP request that touched an interview: the start, or one answer. (+6 more)

### Community 63 - "job_description_summary_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 64 - "test_follow_ups.py"
Cohesion: 0.27
Nodes (16): answers(), follow_up_json(), Follow-up questions through the answer endpoint: the decide call suggests, the…, Answer whatever is asked until the interview completes; returns every answer…, rows(), run_to_end(), summaries(), test_a_failed_follow_up_write_falls_back_to_the_next_main_bank_question() (+8 more)

### Community 65 - "test_stream_answer.py"
Cohesion: 0.11
Nodes (23): Save one whole turn in one commit: advance the session, the answer, the…, End the read transaction before a slow call, so no connection sits idle in a…, Architecture & Design, 1. Why it exists, 2. What it is, 3. When to use it, 5. What can go wrong, 6. Try it yourself (+15 more)

### Community 66 - "test_context.py"
Cohesion: 0.16
Nodes (17): StrategyOutput, Inputs, manager(), NamedTuple, parametrize, System prompt, then every turn still kept, then the latest one; oldest turns go…, Stub, test_a_named_strategy_overrides_the_default() (+9 more)

### Community 67 - "test_request_context.py"
Cohesion: 0.29
Nodes (3): parametrize, test_request_id_header_sent_exactly_once(), test_unsafe_client_request_id_is_replaced()

### Community 68 - "Implementation Steps"
Cohesion: 0.09
Nodes (20): Blockers & Resolutions, Deviations Found During Implementation, Implementation Plan: SSE Streaming of the Interview Turn (Slice 4), Implementation Steps, Overview, Phase A: plumbing and progress events, Phase B: streaming the question text, Project Rules Applied (+12 more)

### Community 69 - "hint_for"
Cohesion: 0.15
Nodes (16): hint_for(), The hint for a failure code (`invalid_reply:<reason>`, `empty_reply`, a…, feedback_hints_for(), feedback_trace_output(), Where to look first for each failed check (or the error), in the order the…, What came out next to what was wanted: the verdict, the overall against its…, inspect, parametrize (+8 more)

### Community 71 - "Any"
Cohesion: 0.13
Nodes (14): AbstractContextManager, Any, One step of a trace as Langfuse sees it; `finish` sets its outcome. Safe when…, Set the output of the trace being built (call it inside `trace()`): what a…, A named step inside the current trace (a Langfuse `chain`): the generations and…, The code's verdict on one reply, as a Langfuse `guardrail` right after the…, Run an SDK call; on any failure log what failed (not why: the message could…, _safe() (+6 more)

### Community 72 - "interviews_feedback_evals.py"
Cohesion: 0.18
Nodes (14): Who wrote the feedback text: the write call, or the code's template when that…, TextSource, Band, _band_check(), check_feedback(), FeedbackEvalQuestion, FeedbackEvalTurn, FeedbackSummary (+6 more)

### Community 73 - "logging.py"
Cohesion: 0.08
Nodes (40): app_error_handler(), _error_response(), http_exception_handler(), integrity_error_handler(), operational_error_handler(), Any, Exception, FastAPI (+32 more)

### Community 74 - "errors.py"
Cohesion: 0.13
Nodes (28): The speech-to-text contract features code against, separate from the text-only…, AppError, AudioTooLargeError, AudioTooLongError, BadRequestError, ConflictError, ErrorBody, ForbiddenError (+20 more)

### Community 75 - "compute_overall"
Cohesion: 0.47
Nodes (6): compute_overall(), The mean of every criterion score of every main question, rounded half up to…, 6. Try it yourself, score(), test_the_overall_is_the_mean_of_every_criterion_score(), test_the_overall_rounds_half_up_to_one_decimal()

### Community 76 - "QuestionKind"
Cohesion: 0.17
Nodes (16): build_threads(), Stored rows as plain values, one thread per main question in interview order (a…, MessageRole, QuestionKind, A main question opens a thread; a follow-up digs into the latest answer of that…, One line of the chat as the user saw it. Usage metadata (model, tokens) is…, TranscriptItemOut, bad_parent() (+8 more)

### Community 77 - "interviews_feedback_controller.py"
Cohesion: 0.25
Nodes (12): FeedbackStatus, A feedback row's life: `generating` while a request holds it, then `generated`…, feedback_out(), FeedbackController, UUID, End-of-interview feedback: request -> FeedbackService, stored row ->…, The feedback and True when generated now (201), False when it was already…, What the client sees. Scores and text only once generated, so a half-written or… (+4 more)

### Community 78 - "RecordingClient"
Cohesion: 0.13
Nodes (5): case(), langfuse(), fixture, A Langfuse client stand-in. Entering a trace sets `current_trace`, like the SDK…, RecordingClient

### Community 79 - "Langfuse CLI Reference"
Cohesion: 0.22
Nodes (6): Credentials, Discovery, Install, Langfuse CLI Reference, Skill Feedback, Submission options

### Community 80 - "Implementation: SSE Streaming of the Interview Turn (Slice 4)"
Cohesion: 0.17
Nodes (11): Changes Made, Deviations from Plan, Implementation: SSE Streaming of the Interview Turn (Slice 4), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 81 - "Implementation Plan: Follow-up Questions (decide / write split)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: Follow-up Questions (decide / write split), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation (+2 more)

### Community 82 - "interviews_session_utils.py"
Cohesion: 0.21
Nodes (12): NotFoundError, QuestionSource, Who wrote a stored question: the LLM, or the hand-written bank (fallback and…, bank_question(), llm_question(), owned_session(), Random, UUID (+4 more)

### Community 83 - "RateLimiter"
Cohesion: 0.20
Nodes (11): RateLimiter, In-memory fixed-window rate limiting for sensitive endpoints. Per process only:…, Count one request for `key`: None when allowed, else whole seconds until its…, math, Clock, test_a_new_window_allows_again(), test_allows_the_limit_then_refuses_with_the_seconds_left(), test_each_key_has_its_own_window() (+3 more)

### Community 84 - "AnswerOut"
Cohesion: 0.16
Nodes (13): AnswerOut, Acceptance Criteria, Blockers, Constraints, Feature: SSE Streaming of the Interview Turn (Slice 4), Functional, Goal, Non-Functional (+5 more)

### Community 85 - "Implementation Plan: Role-Based Access Control (single JWT)"
Cohesion: 0.12
Nodes (17): get_current_user(), Route guard: the caller's DB role must be one of `roles`. Use for coarse gates…, require_roles(), check(), AuthServiceDep, bearer_scheme, Affected Files & Patterns, Architecture & Design (+9 more)

### Community 86 - "validate_summary"
Cohesion: 0.15
Nodes (12): The job-description summary replaces the original on every later call, so it…, validate_summary(), Blockers & Resolutions, Implementation Plan: Context Management for the Interview LLM Calls, Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+4 more)

### Community 87 - ".trace"
Cohesion: 0.16
Nodes (12): One trace for one request: everything started inside it (the generations) nests…, Attach a score to a trace (a bool becomes a Langfuse BOOLEAN). No-op when off…, Create the dataset if needed and upsert its items (each carries its own `id`,…, Affected Files & Patterns, Deviations from the first version of this plan (found during /implement), Implementation Steps, Completed Steps, Deviations from Plan (+4 more)

### Community 88 - "follow_up"
Cohesion: 0.21
Nodes (13): apply_limits(), The code's say over the model's: returns the action and why it overrode the…, 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself (+5 more)

### Community 89 - "interviewer_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 90 - "job_description_summary_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 91 - "Learn: Context management (what to send, and what it costs)"
Cohesion: 0.18
Nodes (10): 1. Why it exists, 2. What it is, 3. When to use it, 4. How it works, 5. What can go wrong, 6. Try it yourself, 7. What surprised me, 8. Check your understanding (+2 more)

### Community 92 - "QuestionCategory"
Cohesion: 0.13
Nodes (26): StoredQuestion, QuestionCategory, interview_categories(), pick_reaction(), The question categories an interview of this type can hold (mixed: both)., A predefined, neutral acknowledgement for the answer just given; never the same…, re, test_a_follow_up_in_a_behavioral_only_interview_keeps_the_behavioral_category() (+18 more)

### Community 93 - "interviews_feedback_turn.py"
Cohesion: 0.12
Nodes (22): BuiltContext, ContextReport, _log(), NamedTuple, Context management: the one place that decides what each LLM call sends. The…, ScoreResult, _Attempts, CallUsage (+14 more)

### Community 94 - "Langfuse Observability"
Cohesion: 0.10
Nodes (18): 1. Assess Current State, 2. Verify Baseline Requirements, 3. Run and Self-Audit the Traces (required), 4. Explore Traces With the User, Always Explain Why, Common Mistakes, Langfuse Observability, Multi-agent systems (subagent dispatch) (+10 more)

### Community 95 - "interviewer_v3.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 96 - "Tracer"
Cohesion: 0.12
Nodes (12): Send what is still buffered, then stop the background exporter. Called once at…, Tracer, FakeClient, test_close_on_a_disabled_tracer_does_nothing(), test_close_survives_a_failing_flush(), test_score_failure_is_swallowed(), test_score_makes_no_call_without_a_trace_id_or_when_tracing_is_off(), test_setting_the_trace_output_is_a_no_op_when_off_and_never_raises() (+4 more)

### Community 97 - "no_llm_env"
Cohesion: 0.33
Nodes (6): no_langfuse_env(), no_llm_env(), no_stt_env(), fixture, Settings built from a clean environment, so a developer's real key never leaks…, Settings without a developer's real Deepgram key or transcription limits.

### Community 98 - "Implementation: Langfuse Tracing"
Cohesion: 0.17
Nodes (11): Baseline Failures, Commit message suggestion, Implementation: Langfuse Tracing, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+3 more)

### Community 99 - "interviews_feedback.py"
Cohesion: 0.11
Nodes (27): _check_lengths(), _has_markup(), _normalized(), parse_write_reply(), BaseModel, _question_score(), QuestionScore, End-of-interview feedback: what the score and write calls must return, and the… (+19 more)

### Community 100 - "follow_up_decision_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 101 - "interviewer_v4.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 102 - "Implementation: Context Management for the Interview LLM Calls"
Cohesion: 0.17
Nodes (11): Changes Made, Implementation: Context Management for the Interview LLM Calls, Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status, Test Cases (+3 more)

### Community 103 - "pytest"
Cohesion: 0.08
Nodes (32): build_provider(), build_transcriber(), The one place that picks the implementation; swapping vendor or model is a…, Speech-to-text for voice answers; None without a key. Never traced: audio and…, TracingProvider, model_validator, Self, Settings (+24 more)

### Community 104 - "User"
Cohesion: 0.08
Nodes (48): alias, AnswerControllerDep, Permission, Route guard: the caller's DB role must grant every permission in `perms`., require_permissions(), User, me(), UUID (+40 more)

### Community 105 - "test_answer_llm.py"
Cohesion: 0.05
Nodes (42): 2. What it is, Architecture & Design, Blockers & Resolutions, Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement (+34 more)

### Community 106 - "Implementation Plan: LLM as the Interviewer (it asks the questions)"
Cohesion: 0.18
Nodes (10): Architecture & Design, Blockers & Resolutions, Implementation Plan: LLM as the Interviewer (it asks the questions), Learning Log (`learnings.md`), Overview, Project Rules Applied, Ready to Implement, Skills Consulted (+2 more)

### Community 107 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 108 - "interviews_evals.py"
Cohesion: 0.06
Nodes (67): anyio_from_thread, ContextTooLargeError, Exception, Even with every droppable entry gone the input is over the strategy's limit., _action_and_gap(), _add_usage(), _case_inputs(), CaseResult (+59 more)

### Community 109 - "fixture"
Cohesion: 0.14
Nodes (14): answer(), _answer(), anyio_backend(), _decision_json(), fixture, Builds a reply in the exact shape the decide call must produce., Async tests (`pytest.mark.anyio`, anyio's own pytest plugin) run on asyncio…, POST a recording to the transcription endpoint; `audio=None` sends no file part… (+6 more)

### Community 110 - "main"
Cohesion: 0.10
Nodes (31): parse_log(), Lines that aren't a log record (the continuation lines of a traceback) are…, render_text(), html_target(), main(), Path, Session, UUID (+23 more)

### Community 111 - "interviews_turn.py"
Cohesion: 0.11
Nodes (39): InterviewerInputs, Plain values for one interviewer or decide call., InterviewerReply, parse_streamed_reply(), interviewer_v5's finished question text, checked like a v4 reply. It was…, Deadline, _decision_label(), Interviewer (+31 more)

### Community 112 - "Feature: Langfuse Tracing"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Langfuse Tracing, Functional, Goal, Non-Functional (+6 more)

### Community 113 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 114 - "test_evals.py"
Cohesion: 0.11
Nodes (59): FakeProvider, load_cases(), Path, run_case(), decision(), hints_of(), long_case(), mentions() (+51 more)

### Community 115 - "9d04cd22055a_use_uuid_primary_key_for_users.py"
Cohesion: 0.39
Nodes (7): _create_users(), downgrade(), _drop_users(), Recreate users with a UUID primary key. Hand-written: Postgres can't cast…, Restore the integer-key table. Data is not restored., upgrade(), Column

### Community 116 - "test_transcript.py"
Cohesion: 0.27
Nodes (11): fixture, shape(), started(), test_a_legacy_answer_without_a_reaction_has_no_item(), test_abandoned_session_stops_where_it_was_left(), test_answered_turns_come_back_in_conversation_order(), test_completed_session_shows_every_question(), test_fresh_session_shows_only_the_first_question() (+3 more)

### Community 117 - "interviews_feedback_service.py"
Cohesion: 0.13
Nodes (24): FeedbackFailedError, FeedbackInProgressError, FeedbackNotFoundError, FeedbackUnavailableError, InterviewNotCompletedError, The LLM could not produce valid scores in time: nothing partial is returned;…, _Claim, FeedbackService (+16 more)

### Community 118 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 119 - "interviewer_v5.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 120 - "LLMResult"
Cohesion: 0.09
Nodes (22): ReasoningEffort, A text reply is streamed word by word; a FakeStream as scripted. An LLMError…, OpenAICompatibleProvider, AsyncBaseTransport, Random, ReasoningEffort, Response, Same request with `stream: true`: chunks as they arrive, then the final… (+14 more)

### Community 121 - "llm"
Cohesion: 0.16
Nodes (10): as_v5_text(), llm(), script(), script_score(), script_write(), unique_question(), Swap the LLM for a scripted fake: `llm.script(...)` queues replies/errors;…, A write reply scripted in v4's JSON, as interviewer_v5 streams it (a CATEGORY… (+2 more)

### Community 122 - "Implementation Plan: UUID primary keys"
Cohesion: 0.18
Nodes (10): Affected Files & Patterns, Architecture & Design, Blockers & Resolutions, Implementation Plan: UUID primary keys, Overview, Project Rules Applied, Ready to Implement, Requirements (no spec; derived) -> Implementation (+2 more)

### Community 123 - "Feature: Follow-up Questions (decide / write split)"
Cohesion: 0.14
Nodes (13): Blockers, Constraints, Edge Cases, Feature: Follow-up Questions (decide / write split), Functional, Goal, Non-Functional, Out of Scope (+5 more)

### Community 124 - "Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)"
Cohesion: 0.15
Nodes (12): Blockers, Constraints, Edge Cases, Feature: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1), Functional, Goal, Non-Functional, Out of Scope (+4 more)

### Community 125 - "test_turn_budget.py"
Cohesion: 0.26
Nodes (12): budget(), llm_lines(), fixture, One deadline per answer turn, shared by the decide and the write call (AC13,…, result(), start(), test_a_decide_call_that_never_answers_is_capped_and_the_write_call_keeps_its_time(), test_a_failed_decide_call_is_not_retried_with_the_last_seconds() (+4 more)

### Community 126 - ".write"
Cohesion: 0.17
Nodes (15): At most two attempts of the write call only. Failing is fine: the template…, 10. Adding an eval for a new AI feature, 1. Know what each task measures, 2. Before you run, 3. Run, 4. Read the output, 5. Triage: what kind of failure is it?, 6. Diagnose in Langfuse (+7 more)

### Community 127 - "Feature: Interview History List (backend)"
Cohesion: 0.13
Nodes (14): Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview History List (backend), Functional, Goal, Non-Functional (+6 more)

### Community 128 - "Langfuse Dataset Construction"
Cohesion: 0.12
Nodes (13): Critical Rules, Langfuse Dataset Construction, Primary Guide, Workflow, 1. Determine Online or Offline, 2. Establish the Metric Set, 3. Implement and Verify, Setting up evals (+5 more)

### Community 129 - "Langfuse v4 project migration"
Cohesion: 0.25
Nodes (7): Choose the execution mode, Langfuse v4 project migration, Migrate evaluators, Migrate exports, Migrate the codebase, Sources of truth, Validate and report

### Community 130 - "run_feedback"
Cohesion: 0.22
Nodes (13): feedback_dataset_items(), feedback_trace_input(), FeedbackEvalCase, load_feedback_cases(), Any, Namespace, Path, The cases as dataset items: the interview as input, the bands as the expected… (+5 more)

### Community 131 - "Implementation: Interview History List (backend)"
Cohesion: 0.15
Nodes (12): Completed Steps, Deviations from Plan, Implementation: Interview History List (backend), Known Issues, Links, Open Questions, Skills Consulted During Implementation, Status (+4 more)

### Community 132 - "Judge Calibration"
Cohesion: 0.29
Nodes (6): 1. Prepare the calibration, 2. Run the calibration, 3. Review the results, 4. Iterate until the judge is approved, 5. Deploy the approved judge, Judge Calibration

### Community 133 - "Langfuse Prompt Migration"
Cohesion: 0.29
Nodes (6): 1. Inventory every prompt (before writing any code), 2. Convert templating and decide structure, 3. Present the plan, then create and refactor, 4. Verify, Langfuse Prompt Migration, Prerequisites

### Community 134 - "build_usage_report"
Cohesion: 0.35
Nodes (11): build_usage_report(), Stored LLM usage per interview and question position: numbers and ids only,…, q(), test_an_empty_database_prints_an_empty_report(), test_follow_ups_are_counted_and_their_tokens_shown_by_question_kind(), test_interviews_are_reported_separately(), test_missing_usage_is_a_dash_and_left_out_of_the_sums(), test_no_percentiles_without_llm_turns() (+3 more)

### Community 135 - "LLMProvider"
Cohesion: 0.08
Nodes (23): LLMProvider, Protocol, AI Engineering Learning Path (Cuewise), Build order: "Chat with the interviewer", Build order: scoring, retrieval and tools, How to make it stick, Later stages (after the core is solid), `learnings.md` template (tutorial style) (+15 more)

### Community 136 - "Langfuse CI/CD"
Cohesion: 0.40
Nodes (4): Checklist, Common Issues, GitHub specific checklist, Langfuse CI/CD

### Community 137 - "Prompt Engineering"
Cohesion: 0.40
Nodes (4): Adjusting an existing prompt, Model-specific tuning, Prompt Engineering, Universal principles

### Community 138 - "TranscriptionResult"
Cohesion: 0.15
Nodes (11): FakeTranscriber, Scripted transcripts (text, a full result, or an error), one per call; records…, BaseModel, What the vendor heard. `text` may be blank (silence); the caller decides what…, TranscriptionResult, get_transcription_limiter(), Tests swap in a fresh limiter so counts never leak between them., The speech-to-text seam of a test: a scripted transcriber and a fresh per-test… (+3 more)

### Community 139 - "Langfuse Implementation Notes"
Cohesion: 0.18
Nodes (10): Annotation queues, Annotation target: OBSERVATION versus TRACE, Common gotchas, Credentials, Error Analysis, Langfuse Implementation Notes, Primary Guide, Prompt fixes (+2 more)

### Community 140 - "test_get_interview.py"
Cohesion: 0.15
Nodes (5): fixture, parametrize, An owner with one started 3-question interview; returns (owner, POST response…, started(), test_interview_routes_document_error_responses()

### Community 142 - "test_create_admin.py"
Cohesion: 0.40
Nodes (9): verify_password(), main(), Session, _no_prompt(), test_existing_user_is_promoted_without_touching_the_password(), test_invalid_email_is_rejected_before_prompting(), test_new_admin_password_follows_registration_rules(), test_running_twice_is_a_no_op() (+1 more)

### Community 143 - "FeedbackCaseResult"
Cohesion: 0.26
Nodes (11): criterion_spread(), FeedbackCaseResult, level_gap_check(), _print_case(), The pair's check, or None when there is nothing to compare: no pair, or either…, Per case: the largest gap between the highest and lowest score any one…, _verdict(), test_nothing_to_compare_is_not_a_level_failure() (+3 more)

### Community 144 - "PageParams"
Cohesion: 0.07
Nodes (40): Page, page_params(), PageParams, BaseModel, NamedTuple, Query, Offset pagination shared by every list endpoint, so clients see one query…, InterviewListOut (+32 more)

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

### Community 151 - "get_llm_provider"
Cohesion: 0.27
Nodes (11): get_bank(), get_clock(), get_llm_provider(), The question source; tests override it with a fixture bank., Built once at startup (app lifespan); None when no key is configured or the…, Monotonic clock for the per-turn LLM time budget; tests swap in a fake one., Affected Files & Patterns, Affected Files & Patterns (+3 more)

### Community 152 - "test_feedback_context.py"
Cohesion: 0.15
Nodes (27): estimate_tokens(), FeedbackScore, FeedbackScoreInputs, FeedbackWriteInputs, NamedTuple, Plain values for the score call: the whole interview, read once the interview…, Plain values for the write call: the stored scores and evidence, never the…, The score call: every thread whole, nothing droppable. Over its own limit it… (+19 more)

### Community 154 - "Feature: Layered Modules (route -> controller -> service -> repository)"
Cohesion: 0.18
Nodes (10): Blockers, Feature: Layered Modules (route -> controller -> service -> repository), Goal, Non-Functional, Out of Scope, Problem, Project Conventions, Requirements (+2 more)

### Community 156 - "ContextManager"
Cohesion: 0.38
Nodes (9): ContextManager, Task, test_an_oversized_decide_input_raises_and_only_older_questions_are_dropped(), test_over_the_limit_drops_ledger_entries_first_then_window_turns_never_the_latest(), manager(), test_the_guard_never_drops_the_current_thread(), manager(), fixture (+1 more)

### Community 157 - "Implementation Plan: Langfuse Tracing"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Langfuse Tracing, Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 158 - "Implementation: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.13
Nodes (14): 9. Review gate (user), Changes Made, Completed Steps, Current Step, Implementation: Interview Feedback and Scoring (Slice 6), Known Issues, Links, Open Questions (+6 more)

### Community 159 - "clock"
Cohesion: 0.20
Nodes (5): _make(), _make(), _make(), clock(), Fake monotonic clock for the per-turn LLM budget; tests advance it (e.g. inside…

### Community 160 - "The fundamentals"
Cohesion: 0.13
Nodes (15): 10. Evaluation (the most important one), 11. Rubrics, scoring and LLM-as-judge, 12. Embeddings and retrieval (RAG), 13. Tool use and agents, 1. How an LLM call actually works, 2. Context management, 3. Prompt engineering as engineering, 4. Structured output and validation (+7 more)

### Community 161 - "Implementation Plan: Eval runs in Langfuse (scores + datasets)"
Cohesion: 0.17
Nodes (11): Architecture & Design, Decisions (grilled with the user), Implementation Plan: Eval runs in Langfuse (scores + datasets), Overview, Plan-defined criteria, Project Rules Applied, Ready to Implement, Skills Consulted (+3 more)

### Community 162 - "test_answer_interview.py"
Cohesion: 0.31
Nodes (5): candidate_rows(), UUID, session_uuid(), test_answering_a_question_saves_it_and_moves_to_the_next(), test_full_interview_without_llm_completes()

### Community 163 - "test_job_description_summary.py"
Cohesion: 0.31
Nodes (7): parametrize, stored_session(), test_a_long_job_description_is_summarised_once_and_used_in_every_call(), test_a_short_or_missing_job_description_makes_no_extra_call(), test_an_unusable_summary_keeps_the_original_and_the_interview_starts(), test_summary_usage_is_logged_with_its_own_prompt_version(), test_without_an_llm_no_summary_is_made()

### Community 164 - "split_header"
Cohesion: 0.25
Nodes (9): interviewer_v5's `CATEGORY: <value>` first line (next-question mode), read…, split_header(), read(), parametrize, test_a_long_first_line_is_no_header_without_waiting_for_its_end(), test_a_missing_or_unknown_header_is_an_invalid_reply(), test_at_the_end_of_the_reply_a_header_needs_no_newline(), test_no_header_is_known_until_its_line_ends() (+1 more)

### Community 165 - "ErrorResponse"
Cohesion: 0.04
Nodes (55): ErrorResponse, Primary key for every table (CLAUDE.md IDs rule). UUIDv7 is time-ordered, so…, UUIDPrimaryKeyMixin, Affected Files & Patterns, Blockers & Resolutions, Implementation Notes (added during /implement), Implementation Plan: Error Handling, Overview (+47 more)

### Community 166 - ".update_claimed_feedback"
Cohesion: 0.29
Nodes (5): Any, datetime, Take over a `failed` row, or a `generating` one whose request died (started…, Write to the row only while this request still holds its claim (still…, taken_over()

### Community 167 - "RequestContextMiddleware"
Cohesion: 0.20
Nodes (7): Assigns each request an id, echoes it as X-Request-ID, and logs one access…, RequestContextMiddleware, ASGIApp, Architecture & Design, Receive, Scope, Send

### Community 168 - "Implementation Plan: Interview Feedback and Scoring (Slice 6)"
Cohesion: 0.20
Nodes (9): Blockers & Resolutions, Implementation Plan: Interview Feedback and Scoring (Slice 6), Overview, Project Rules Applied, Ready to Implement, Skills Consulted, Spec Requirements -> Implementation, Testing Strategy (+1 more)

### Community 169 - "StreamedTurn"
Cohesion: 0.33
Nodes (4): NamedTuple, Event names with each run of question.delta shown once: the shape of the…, The streamed question as the client shows it: deltas appended, a reset clearing…, StreamedTurn

### Community 170 - "traces"
Cohesion: 0.25
Nodes (4): Tips, fixture, RecordingClient, traces()

### Community 171 - "failed"
Cohesion: 0.07
Nodes (32): check_streamed_reply(), check_reply for interviewer_v5's streamed format: the CATEGORY line, then the…, Slice 6: Feedback and scoring, Acceptance Criteria, Blockers, Constraints, Edge Cases, Feature: Interview Feedback and Scoring (Slice 6) (+24 more)

### Community 172 - "feedback_score_v2.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 173 - "test_llm_settings_default_to_off_with_documented_limits"
Cohesion: 0.33
Nodes (7): Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, Baseline Failures, test_env_example_lists_every_llm_setting(), test_llm_settings_default_to_off_with_documented_limits()

### Community 175 - "feedback_score_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 176 - "feedback_write_v1.md"
Cohesion: 0.29
Nodes (6): Capabilities, Constraints, Input, Output, Role, Task

### Community 177 - "build_tracer"
Cohesion: 0.47
Nodes (6): build_tracer(), On only when both keys are set. `environment` overrides APP_ENV (the eval…, _settings(), test_both_keys_build_an_enabled_tracer(), test_no_keys_builds_a_disabled_tracer_without_warning(), test_one_key_builds_a_disabled_tracer_with_one_warning_that_hides_the_value()

### Community 179 - "Affected Files & Patterns"
Cohesion: 0.33
Nodes (5): Any, Protocol, How many oldest entries may be dropped; everything else is required., Strategy, Affected Files & Patterns

### Community 180 - "Langfuse"
Cohesion: 0.29
Nodes (7): 1. Langfuse API via CLI, Core Principles, Credentials, Detailed CLI Reference, Langfuse, Skill Feedback, Use case specific references

### Community 181 - "test_keyterms.py"
Cohesion: 0.47
Nodes (5): parametrize, test_each_role_list_includes_the_shared_terms_once(), test_each_role_list_stays_well_under_deepgrams_keyterm_limit(), test_every_role_has_keyterms(), test_terms_are_plain_text()

### Community 183 - "ProviderConfig"
Cohesion: 0.50
Nodes (3): ProviderConfig, BaseModel, One listed provider, resolved from its vendor block.

### Community 184 - "Langfuse CLI Reference"
Cohesion: 0.40
Nodes (5): Credentials, Discovery, Install, Langfuse CLI Reference, Tips

### Community 185 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 186 - "SummaryInputs"
Cohesion: 0.50
Nodes (3): JobDescriptionSummary, SummaryInputs, test_the_summary_task_sends_the_job_description_as_data()

### Community 187 - "2. Langfuse Documentation"
Cohesion: 0.40
Nodes (5): 2. Langfuse Documentation, 2a. Documentation Index (llms.txt), 2b. Fetch Individual Pages as Markdown, 2c. Search Documentation, Documentation Workflow

### Community 190 - "sse_frames"
Cohesion: 0.50
Nodes (4): One streamed-turn event as the dict sse-starlette encodes: the event name, and…, The controller's events as SSE frames. Closing this (a client that left) closes…, sse_frame(), sse_frames()

### Community 191 - "started"
Cohesion: 0.67
Nodes (3): fixture, An owner with a started 3-question interview: (owner, session_id, first…, started()

## Knowledge Gaps
- **562 isolated node(s):** `cuewise-be`, `Core Principles`, `Use case specific references`, `Credentials`, `Detailed CLI Reference` (+557 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1398 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **44 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tracer` connect `Tracer` to `interviews_answer_service.py`, `run_feedback`, `LLMProvider`, `interviews_dependencies.py`, `test_feedback_evals.py`, `test_tracing_lifespan.py`, `test_feedback_endpoint.py`, `Implementation Plan: Eval runs in Langfuse (scores + datasets)`, `Implementation: Eval runs in Langfuse (scores + datasets)`, `traces`, `test_tracing.py`, `build_tracer`, `tracing.py`, `InterviewQuestion`, `Any`, `interviews_feedback_evals.py`, `RecordingClient`, `.trace`, `interviews_feedback_turn.py`, `pytest`, `interviews_evals.py`, `test_evals.py`, `interviews_feedback_service.py`, `LLMResult`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Why does `LLMError` connect `LLMServerError` to `TranscriptionResult`, `interviews_reply.py`, `test_stream_turn.py`, `Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)`, `LLMTimeoutError`, `provider.py`, `tracing.py`, `InterviewQuestion`, `Implementation Steps`, `errors.py`, `interviews_session_utils.py`, `interviews_feedback_turn.py`, `pytest`, `test_answer_llm.py`, `interviews_evals.py`, `interviews_turn.py`, `Feature: Langfuse Tracing`, `test_evals.py`, `interviews_feedback_service.py`, `LLMResult`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `InterviewQuestion` connect `InterviewQuestion` to `interviews_answer_service.py`, `test_interview_report.py`, `build_usage_report`, `interviews_reply.py`, `test_list_interviews.py`, `test_context_controller.py`, `test_feedback_endpoint.py`, `test_answer_stream.py`, `test_feedback_contract.py`, `QuestionTurn`, `ErrorResponse`, `interviews_schema.py`, `interviews_model.py`, `test_create_interview.py`, `test_start_llm.py`, `interviews_utils.py`, `interviews_report.py`, `test_follow_ups.py`, `test_stream_answer.py`, `QuestionKind`, `interviews_session_utils.py`, `interviews_feedback.py`, `test_answer_llm.py`, `test_transcript.py`, `LLMResult`, `test_turn_budget.py`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 42 inferred relationships involving `User` (e.g. with `AuthController` and `get_current_user()`) actually correct?**
  _`User` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Are the 23 inferred relationships involving `FakeProvider` (e.g. with `ChatMessage` and `LLMError`) actually correct?**
  _`FakeProvider` has 23 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `InterviewQuestion` (e.g. with `build_threads()` and `question_out()`) actually correct?**
  _`InterviewQuestion` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 32 inferred relationships involving `LLMResult` (e.g. with `FakeProvider` and `OpenAICompatibleProvider`) actually correct?**
  _`LLMResult` has 32 INFERRED edges - model-reasoned connections that need verification._