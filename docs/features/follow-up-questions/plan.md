# Implementation Plan: Follow-up Questions (decide / write split)

## Overview
After each answer a small LLM "decide" call judges whether to dig deeper, the code applies its limits, and a second "write" call produces the one question, so the model suggests and the code enforces (concept 5) while the interview never stalls.

## Architecture & Design
A new `interviews_turn.py` owns one answer turn: a `Deadline` shared by both calls, the decide step, `apply_limits`, and the write step (the existing `_ask_llm` logic generalised to two modes). The controller keeps routing-level orchestration: it reads plain values, asks the turn module what to store, picks the reaction, and saves the whole turn through the existing compare-and-swap. The `ContextManager` gets a second task for the decision and a thread-aware `window_ledger` for writing. Follow-ups are ordinary `interview_questions` rows (`kind`, `parent_question_id`, stored `main_number`) on the same sequential `position`, so ordering, the unique constraint and the compare-and-swap are untouched.

## Spec Requirements -> Implementation
- Decide call, strict output, rubric (AC1, AC9, EC3, EC7, EC17-18) -> Steps 2, 4
- Code limits: cap of 2, time checks, last question (AC2, AC5, AC13, AC18, EC1-2, EC6, EC8-9, EC20-21) -> Steps 1, 8, 9
- Write call modes, category inheritance, repeat check (EC14-15) -> Steps 3, 4, 8
- Data, migration, API fields, optional reaction (AC6-8, AC16, EC19) -> Step 6
- Context tasks and the thread kept whole (AC11-12, EC10, EC16) -> Step 5
- Fallbacks, LLM off, up-front sessions, concurrency (AC3-4, AC7, AC14, EC4-5, EC11-13) -> Steps 8, 9
- Usage summing, logs, `budget_left_ms`, report (AC10, AC19, AC20) -> Steps 8, 10
- Evals with `expect` (AC15) -> Step 11
- Learnings, tuning of the budget, learning-path line (AC17) -> Step 12

## Implementation Steps
1. **Constants and enums.** In `interviews_constants.py`, next to `MIN_SECONDS_FOR_RETRY`: `QuestionKind`, `FollowUpAction`, `FollowUpGap` (StrEnums), the cap of 2 follow-ups, `DECIDE_MAX_SECONDS` (10), `MIN_SECONDS_FOR_WRITE` (5), `WRITE_RESERVE_SECONDS` (= the minimum), the decision task name and the two new prompt versions. Starting values are proposals, tuned in Step 12. — Test: skip (config)
2. **Decision parser.** In `interviews_reply.py`, add a `Decision` result and `parse_decision_reply`, built like `parse_interviewer_reply`: fence and JSON handling, a strict Pydantic model with `extra="forbid"`, closed action and gap lists, gap present exactly when the action is `follow_up`, note validated by `validate_note` (a bad note is dropped, never costs the decision). Reason codes only, never raw text. — Test: first. Seam: `parse_decision_reply` (user-confirmed). Slices: valid follow_up with gap; valid next_question with null gap; not JSON; extra key; unknown action; unknown gap; gap on next_question; missing gap on follow_up; bad note dropped.
3. **Write parser modes.** Extend `parse_interviewer_reply` with a mode, default `next_question` so every existing call and test is unchanged. In `follow_up` mode the reply is the question only, the category comes from the caller (the parent's), the repeat check runs over every earlier question including follow-ups, and the one-question-mark rule stays. The note stays optional so `interviewer_v3` ablations still parse. — Test: first. Seam: `parse_interviewer_reply` (user-confirmed). Slices: follow-up accepted without category; category not accepted from the model in follow-up mode; repeat of an earlier follow-up rejected; main mode unchanged.
4. **Prompts.** New `prompts/follow_up_decision_v1.md` (the rubric, closed lists, level placeholder, data-not-instructions line, output shape) and `prompts/interviewer_v4.md` (v3 without the note and without "never follow up"; the two modes are announced by the status block, not by the system prompt, so the prefix stays identical). Both follow the six-part layout. Loaded at import like the others, rendered with the existing `render_template`. v1-v3 untouched. — Test: first for structure, after for wording. Seam: `load_prompt` plus the six-heading check pattern in `test_context_prompts.py`; also a check that every action and gap value appears in the decide prompt. Wording quality is judged by Step 11 and Step 12 evals.
5. **Context tasks.** `QuestionTurn` gains `kind` and `main_number` (defaults keep old callers working); `interviewer_history` fills them from the rows. `InterviewerInputs` gains the mode, the gap and the follow-ups left. `WindowLedger` becomes thread-aware: the window never starts inside the current thread, `droppable` counts only turns older than the current thread, the status block states the mode, main number, follow-ups left and gap (neutralised, app data). Add a decision strategy with the same stable-prefix layout and register it as the second task in `build_context_manager`; `window_ledger` defaults to v4 for writing, `full_history` stays v1 and writes no follow-ups. — Test: first. Seam: `ContextManager.build` (user-confirmed). Slices: decision messages carry the thread whole; untrusted text only in user messages (AC11); window never splits a thread; over-limit raises `ContextTooLargeError` (EC16); prefix identical across calls of a task; max interview with max follow-ups stays under the limit (AC12).
6. **Data and API.** `InterviewQuestion` gets `kind`, nullable `parent_question_id` (self FK, cascade), `main_number` and nullable `decision_prompt_version`; new Alembic migration (backfill `kind=main`, `main_number=position`; clean downgrade; no edit of applied migrations). Schemas: `question_kind` and `main_number` on `QuestionOut` and on question items of `TranscriptItemOut` (the transcript's own `kind` already means question/answer/reaction); `AnswerOut.reaction` optional; `build_transcript` passes the new fields; `record_turn` accepts a missing reaction. — Test: first for transcript and schema, after for the migration. Seam: `build_transcript` (user-confirmed); the migration is run by hand with `alembic upgrade` then `downgrade` on a scratch database, because the test database uses `create_all`.
7. **Task-routing test double.** In `tests/modules/interviews/conftest.py`, make the `llm` fixture route each call to a decide queue or a write queue by looking at the system message, with a default decision of `next_question` and a `script_decide` method plus a `decision_json` helper. Existing tests that script write replies keep working untouched. — Test: skip (test infrastructure); verified by running the existing interview tests unchanged.
8. **Turn module.** New `interviews_turn.py`: `Deadline` (injectable clock, remaining seconds), `apply_limits` (follow-ups left, time left, last-question rule), the decide step (budget = min of its cap and time left minus the reserve; one retry on an invalid reply only if time allows; provider error, empty reply or too-large context all mean `next_question` with no note), the write step (modes, one retry, bank signal on failure), usage summed over all attempts of both steps, one log line per call with the task name, `budget_left_ms`, `action` and `gap`, plus one summary line per turn (the model's decision, the final action, the override reason `cap_reached` or `no_time`, the source `llm` or `bank` with its fallback reason, total LLM time; reason codes only). The two log helpers move here from the controller because both steps use them. Reuse the existing retry rule, `LLMError` handling and `_sum_known`. — Test: first. Seam: `POST /interviews/{id}/messages` with the scripted `llm` and fake `clock` fixtures (user-confirmed). Slices: a decide call stopped at its cap leaves the write call its reserve (AC18, EC20); a failed decide call is not retried with the last seconds (EC21); no write call below the minimum (AC13, EC6); decide garbage twice falls through (AC3, EC3); usage and logs (AC10, AC19, no raw text in logs); the turn summary line shows `override=cap_reached` for a third `follow_up` decision and `source=bank` with its fallback reason when the write call fails (AC20).
9. **Controller wiring.** `answer()` computes the thread state (main number, follow-ups used, parent), runs the turn module, then decides what to store and which reaction to return: a follow-up question gets no reaction; moving on or completing gets the predefined one (`final` only when the thread ends on the last main question). `completes` is now decided after the decision, not from `position`. `start()` uses the write step in `next_question` mode with no decide call. LLM off or a later question row already stored means the old path with no follow-ups. A follow-up row copies the parent's category, `main_number` and id. Write failure after a follow-up decision serves the next main bank question, or completes on the last main question. — Test: first. Seam: the answer endpoint (user-confirmed). Slices, in order: LLM off unchanged (AC14); decide says next_question matches today's behavior; follow-up stored with parent, kind and category and no reaction (AC6, AC8); always-follow_up stops at 2 per question (AC2); follow-up on the last main question and completion (AC5); write fails after a follow-up decision (AC4, EC5); up-front session (EC13); injected answer and job description (AC11); double submit (AC7); atomic save still holds (EC17).
10. **Usage report.** `build_usage_report` and `app/scripts/usage_report.py` show follow-up counts and tokens by question kind (a follow-up row's tokens already include its decide call), plus p50/p95 of the summed LLM time per turn. Decide-only tokens stay in the per-call log lines. — Test: first. Seam: `build_usage_report` (user-confirmed).
11. **Evals.** `eval_cases.json` cases may carry `expect` (action, optional gap) and a thread already at the cap; add cases until at least 10 are labelled (vague behavioral, vague technical, complete answer, "idk", off-topic, near-empty, at-the-cap thread, injected answer, injected job description, both forcing follow-ups). The runner gets `--task decide|write` (default `write`, so today's behavior and flags are unchanged); decision runs report accuracy, over-probing, under-probing and per-gap results, aggregated over `--repeat`. — Test: first for the check and summary functions with the fake provider (seam: the runner's public functions in `test_evals.py`), after for real-model runs (opt-in, never in pytest).
12. **Measure, tune, document.** Run the decide evals three times on `gemini-3.5-flash-lite` (pause between runs, the free tier rate limits at about 25 calls), tune the rubric and the budget constants from the logged latencies, record `learnings.md` checkpoints (concepts 5, 4, 2, 10, 9) and tick the learning-path line. Run `uv run ruff check . && uv run ruff format .`, `uv run pytest`, then `graphify update .`. — Test: after

## Affected Files & Patterns
- `app/modules/interviews/interviews_turn.py` (new) — deadline, limits, decide and write steps, log helpers.
- `interviews_reply.py` — `Decision`, `parse_decision_reply`, parser modes.
- `interviews_constants.py` — enums, limits, budget constants, task and prompt names.
- `interviews_context.py` — thread-aware `WindowLedger`, decision strategy, task registration.
- `interviews_utils.py` — `QuestionTurn` fields, `interviewer_history`, prompt rendering, `build_transcript`, `build_usage_report`.
- `interviews_model.py`, `interviews_schema.py`, `interviews_repository.py`, `interviews_controller.py`, `interviews_evals.py`, `data/eval_cases.json`, `app/scripts/usage_report.py`.
- `prompts/follow_up_decision_v1.md`, `prompts/interviewer_v4.md` (new); `alembic/versions/` (new migration).
- `tests/modules/interviews/`: new `test_decision_contract.py`, `test_follow_ups.py`, `test_turn_budget.py`; extend `conftest.py`, `test_reply_contract.py`, `test_context_strategies.py`, `test_context_prompts.py`, `test_transcript.py`, `test_usage_report.py`, `test_evals.py`.
- `docs/features/follow-up-questions/learnings.md` (new) and the progress line of `docs/ai-engineering-learning-path.md`.
- Patterns to follow: the strict-model parser in `interviews_reply.py`; the context `Task` and `Strategy` protocol in `app/core/ai/context.py`; the compare-and-swap in `record_turn`; scripted fake plus injectable clock in the existing tests.
- Risks: existing tests script write replies in a fixed order, so the decide call must not consume them (Step 7); `completes` no longer equals `position == question_count`, so every place that assumed it needs checking (controller, reaction, evals); `AnswerOut.reaction` becoming optional is a client-visible change; the migration adds a self-referencing foreign key and server defaults, so run it on the real database engine, not only sqlite.

## Testing Strategy
- Framework & command: `uv run pytest tests/modules/interviews` while working, `uv run pytest` before finishing; lint with `uv run ruff check . && uv run ruff format .`. Real-model evals: `uv run python -m app.modules.interviews.interviews_evals --task decide --repeat 3 --model gemini-3.5-flash-lite` (opt-in).
- Coverage map:

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1, EC3, EC18 | 2 | first | parser slices |
| AC2, EC1, EC2, EC8 | 9 | first | always-follow_up fake |
| AC3, EC3, EC4 | 8, 9 | first | garbage and provider error |
| AC4, EC5, EC14 | 3, 9 | first | write fails or repeats |
| AC5, EC9 | 9 | first | last main question thread |
| AC6, EC15 | 6, 9 | first | parent, kind, category, main number |
| AC7, EC11, EC17 | 9 | first | double submit; atomic save |
| AC8 | 6, 9 | first | no reaction before a follow-up; fields in responses |
| AC9 | 4 | first | headings, enum values in prompt, v1-v3 unchanged |
| AC10 | 8 | first | usage summing, log lines without raw text |
| AC11, EC10 | 5, 9 | first | user-only roles; injected cases |
| AC12, EC16 | 5 | first | thread whole, limit, too large |
| AC13, EC6 | 8 | first | controllable clock |
| AC14, EC12, EC13 | 9 | first | LLM off; later row stored |
| AC15 | 11 | first | check and summary functions |
| AC16, EC19 | 6 | after | alembic upgrade and downgrade by hand |
| AC17 | 12 | after | real numbers in learnings |
| AC18, EC20, EC21 | 8 | first | slow decide, no retry with last seconds |
| AC19 | 8, 10 | first | `budget_left_ms`; p50/p95 |
| AC20 | 8 | first | turn summary line: override and fallback reasons |
| EC7 | 4, 11 | after | no code guard; measured by the decide evals |

- Must verify, not assume: that the real model returns valid decision JSON and judges gaps usefully (Steps 11-12); real decide and write latencies against the budget values; that the provider honors `budget_seconds` for the decide cap; the migration on the real database engine; that the client's fetch timeout exceeds the turn deadline; the context-limit headroom with a max-size interview.
- Open questions: none (every EC has an outcome). Known limitation, see Blockers: EC13 on the last question of an up-front session.
- Known baseline failures: not checked yet; `/implement` runs the suite first and records any here.

## Blockers & Resolutions
- Existing tests script write replies in order -> Step 7 routes calls by task with a valid default decision, so they stay unchanged.
- Name clash: `TranscriptItemOut.kind` already exists -> API fields are `question_kind` and `main_number`; the column stays `kind` (spec wording updated).
- Spec asked the report to show decide-call tokens, but usage is summed onto the question -> the report shows tokens by question kind; decide-only tokens stay in the log lines (spec updated).
- EC13: a session stored up front is detected by a later question row existing, so its final question cannot be told apart -> accepted limitation for pre-slice-2 development data only; to confirm there is none to protect.
- `completes` depended on `position` -> now decided after the decision and tested in Step 9.
- Budget values are guesses -> constants, logged per call, tuned in Step 12.
- Edge cases EC1-EC21 -> each handled in the step listed in the coverage map.

## Trade-offs & Rationale
- New `interviews_turn.py` over growing the controller (user choice): the controller is ~490 lines and `_ask_llm` is cc=28; the deadline and both steps are testable together.
- Stored `main_number` over deriving it (user choice): every response reads it from the row; costs one backfilled column.
- One deadline and a reserve for the write call: the write step is what the user sees, so it is never starved by a slow decide call.
- Write step reuses the existing `interviewer_turn` task; decide is a second task: matches the `ContextManager` design and keeps `full_history` as the untouched baseline.
- Note stays optional in the write parser: lets `--prompt interviewer_v3` ablations keep parsing, costs one tolerated field.
- No code guard for tiny answers (user choice): the rubric and evals decide first; add a guard only if evals show wasted calls.
- Decision and cap stay out of the prompt-only layer: the cap, the time check and the category are in code, so an injection cannot change them.

## Project Rules Applied
- `CLAUDE.md` (project) -> router/controller/repository layering, `interviews_` file prefix, Alembic-only schema changes, UUID keys, prompts as versioned data, Pydantic validation with retry and fallback, no raw content in logs, mocked LLM in tests, learnings as a deliverable, no commit or push.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | controller flow, context strategies, repository, schemas, fixtures, constants |
| graphify | answer-turn code paths (query run during the spec phase) |
| grill-me (via AskUserQuestion) | module placement, stored main number, API names, test seams |
| security-review, ponytail | not run; injection surface covered by AC11/EC10 and the existing layered defences, and scope decisions are listed under Trade-offs |

## Ready to Implement
- All spec requirements mapped to steps; every step has a Test tag; every AC and EC is in the coverage map.
- Seams are user-confirmed.
- Deviations from the spec, all small and written back into the spec: API field names (`question_kind`, `main_number`), a stored `main_number` column, report by question kind instead of decide-only tokens, and the EC13 last-question limitation.

## Deviations Found During Implementation
- `QuestionTurn` gained only `kind`, not `main_number`: main numbers and threads are derived from the kinds (`main_numbers`, `thread_start`), so old callers and eval cases need nothing new.
- The decide call gets no job description: judging an answer doesn't need it, and leaving it out removes a whole injection path into the decision (the job-description injection case still runs in the decide evals).
- `question_kind` and `main_number` are on every transcript item (answers and reactions carry their question's), not only on question items: simpler for the client.
- The migration's downgrade keeps follow-up rows (as ordinary questions) instead of deleting answers.
- The per-turn summary line is also written for turns without the LLM (`decision=skipped`, `source=bank` or `stored`), so every answer turn has one; `decide_failed` is not used as a fallback reason, because a failed decision still lets the write call run (`decision=none` shows it).
- A bank question that replaces a failed write stores no usage (as before follow-ups); the failed calls are in the per-call log lines.
- The window moves its start back to the thread's main question (up to 5 turns in full), rather than forward.
