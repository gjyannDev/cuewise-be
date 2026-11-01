# Feature: Follow-up Questions (decide / write split)

## Problem
Every answer moves straight to the next main question. `interviewer_v3` even tells the model "move to a new topic rather than following up", so a vague answer ("I'd use Redis", "we fixed it") is never probed, and the interview feels like a questionnaire instead of a conversation. It also leaves the learning path's concept 5 unproven: nothing yet shows that the model can *ask* for a follow-up while the code *limits* it ("you can't make the interviewer ask a third follow-up, whatever the model says").

## Goal
After each answer the interviewer can dig deeper with at most 2 follow-ups per main question. A separate **decide** call (the LLM judges whether the answer has a clear gap) is followed, after the code applies its limits, by a **write** call (the LLM writes the one question). The interview never stalls whatever either call does. The quality of the decision is measurable: the eval runner reports decision accuracy, over-probing and under-probing on labelled cases.

## Project Conventions
- Rule files consulted: `CLAUDE.md` (project root; there is no `.claude/` directory), the user's global `~/.claude/CLAUDE.md`, `docs/ai-engineering-learning-path.md`, and the specs of `llm-interviewer` and `context-management`.
- Constraints those rules impose on this feature:
  - Router -> controller -> repository; feature files keep the `interviews_` prefix; schema changes only through a **new** Alembic migration.
  - Prompts are versioned data files. `interviewer_v1/v2/v3` and `job_description_summary_*` stay untouched; new behaviour means new files (`follow_up_decision_v1.md`, `interviewer_v4.md`), each with the six parts (Role, Task, Input, Output, Constraints, Capabilities).
  - LLM output is validated with Pydantic (`extra="forbid"`), with retries and a safe fallback; LLM calls stay behind the provider interface and the `ContextManager`.
  - Every call logs model, prompt version, tokens, latency and outcome; logs never contain question, answer or job-description text.
  - Candidate and job-description text is untrusted: only in `user` messages, never in a system prompt.
  - UUID primary and foreign keys (`UUIDPrimaryKeyMixin`); new tests mock the LLM; real-model runs stay opt-in.
  - `docs/features/follow-up-questions/learnings.md` is a deliverable (Predict / Observed / Why / Proof), and the learning-path progress line is updated.
  - Nothing is committed or pushed.

## User Flow
1. The candidate answers a main question.
2. The app asks the decide call whether the answer has a clear gap. If it does, and the limits allow, the write call writes one follow-up and the candidate sees it straight away, with no reaction line in between.
3. The candidate answers the follow-up. The same decision repeats (up to 2 follow-ups per main question).
4. When the decision is "move on" (or a limit is reached), the candidate gets the usual predefined reaction and the next main question, or the interview completes after the last main question's thread.

```
Interviewer: How would you design a rate limiter?
You:         I'd use Redis.
Interviewer: Which algorithm would you run on Redis, and why that one?      <- follow-up 1 (gap: no_tradeoff)
You:         Token bucket, because it allows short bursts...
Interviewer: Thanks, that gives me a clear picture.                          <- reaction
             Tell me about a time you disagreed with a teammate.            <- next main question
```

## Requirements

### Functional
**Decide call**
- After every answer, main or follow-up, in a session where the LLM is on and the questions are not pre-stored, one decide call runs before anything is written.
- Input: the main question, the current thread (the main question, its earlier follow-ups and the answers), the latest answer, level, interview type, how many follow-ups are left for this thread, and older main questions as a short ledger of notes. All of it is data, never instructions.
- Output: strict JSON `{action, gap, note}`. `action` is `follow_up` or `next_question`. `gap` is one of `missing_situation`, `missing_own_action`, `missing_result`, `no_tradeoff`, `no_how`, `no_example`, `partial_answer` when the action is `follow_up`, and `null` otherwise. `note` is the one-sentence factual note on the latest answer (same rules as today; a bad note is dropped and never costs the decision). Unknown keys, unknown values, `gap` on `next_question` or a missing `gap` on `follow_up` are invalid.
- The prompt `follow_up_decision_v1.md` carries the rubric: follow up when the answer leaves a clear gap (behavioral: no concrete situation, no personal action, no result; technical: a choice with no reason or trade-off, "what" without "how"; either: a claim with no example, or only part of the question answered); move on when the answer is complete for the candidate's level, empty, "I don't know", off-topic, or when no follow-ups are left.

**Code enforces, between the two calls**
- A thread allows at most 2 follow-ups. A `follow_up` decision with none left is changed to `next_question`, whatever the model said.
- The whole turn (decide + write, including retries) shares **one deadline**, set once at the start of the turn from the current 30 s budget and passed to both steps; each step asks it how much time is left.
- The decide call is capped (`DECIDE_MAX`) and the write call has a reserve (`WRITE_RESERVE`): the decide call's budget is the smaller of its cap and the time left minus the reserve, so a slow decide call can never leave the write call without time.
- The check happens before every call, not only before retries: if less than the minimum for that call is left, the call is not started. A write call below `MIN_SECONDS_FOR_WRITE` means no follow-up is attempted; a retry below `MIN_SECONDS_FOR_RETRY` is skipped. Leftover time goes to the write call first: a failed decide call is not retried with the last seconds.
- Starting values (proposals, not measured; tuned later from the logs): whole turn 30 s, `DECIDE_MAX` about 10 s, `MIN_SECONDS_FOR_WRITE` about 5 s, `WRITE_RESERVE` equal to `MIN_SECONDS_FOR_WRITE`. They are named constants next to the existing `MIN_SECONDS_FOR_RETRY`, not numbers in the controller.
- The last main question can get follow-ups. When its thread ends with `next_question`, the interview completes.
- Only the final action reaches the write call.

**Write call**
- `interviewer_v4.md` replaces v3 for the live path: it no longer writes a note and no longer says "never follow up". It has two modes, told to it by the app: `next_question` (as today: a new competency, category rule, no repeats) and `follow_up` (one question that targets the given gap, at most two sentences and one question mark, no greeting or acknowledgement, no judging).
- A follow-up inherits its main question's category; the model does not choose it. A follow-up must not repeat or rephrase any earlier question (main or follow-up).
- Invalid replies use the same retry rule as today (one retry if enough time is left, then fallback).

**Data and API**
- `interview_questions` gets `kind` (`main` | `follow_up`, existing rows `main`), a nullable `parent_question_id` (UUID FK to the main question), a stored `main_number` (existing rows get their position; a follow-up copies its parent's) and a nullable `decision_prompt_version`. New Alembic migration with a clean downgrade.
- `position` stays one sequential counter over every row, main and follow-up, so ordering, the unique constraint and the compare-and-swap keep their meaning. `question_count` counts **main** questions only. The question and transcript responses expose `question_kind` and `main_number` (named `question_kind` because transcript items already have a `kind` meaning question/answer/reaction), so a client can show "Question 3 of 5".
- `AnswerOut.reaction` becomes optional: absent when a follow-up is asked, present when the interview moves to the next main question or completes.
- The usage of the decide call(s) and the write call(s) of a turn is summed onto the question that turn produced (`prompt_tokens`, `completion_tokens`, `latency_ms`); `prompt_version` holds the write prompt and `decision_prompt_version` the decide prompt.
- Each call writes its own log line with its task name, prompt version, tokens, latency, finish reason, outcome, the time left on the turn deadline when it started (`budget_left_ms`), and for the decision the `action` and `gap`; no raw content.
- Each turn also writes one summary line (reason codes only, no text): the model's decision, the final action, the override reason, the question source with the fallback reason, and the total LLM time. It is the only place an overridden follow-up or a bank fallback is explained, and where the p50/p95 turn time comes from.
- The usage report counts follow-ups, shows tokens by question kind (a follow-up row's tokens already include its decide call; decide-only tokens are in the per-call log lines), and shows p50/p95 of the LLM time per turn, so "what does a follow-up cost" and "does the budget fit" both have numbers.

**Context**
- The `ContextManager` gets two tasks (decide, write). For both, the current thread is sent in full and older main questions as ledger entries with notes; the input-limit guard never separates the main question from its follow-ups, and the stable system-prompt + job-description prefix is kept identical across calls of one task.

**Fallbacks** (the interview never stalls)
- Decide reply invalid -> one retry if time allows -> otherwise treated as `next_question` with no note.
- Decide provider error, empty reply or input too large -> treated as `next_question` with no note.
- Write fails or stays invalid after a `follow_up` decision -> the next main question from the bank, or completion if this was the last main question.
- LLM off, or a session whose questions were all stored up front -> no decide call, no follow-ups, behaviour unchanged.

**Evals**
- Eval cases can carry `expect: {action, gap?}`. The runner reports decision accuracy, over-probing (follow-up where `next_question` was expected), under-probing, and the result per gap, separately from the existing writing rule checks, and still supports `--repeat`.
- At least 10 labelled decision cases: vague behavioral, vague technical, complete answer, "I don't know", off-topic, near-empty, a thread already at the cap, an injected answer trying to force more follow-ups, and an injected job description trying to do the same.
- The runner stays opt-in; real-model runs never happen in `uv run pytest`.

### Non-Functional
- **Latency:** a follow-up turn makes two sequential calls; the worst case is the shared 30 s deadline, so no turn waits longer than that on the LLM. No new target for typical latency; per-call latency and `budget_left_ms` are logged, and p50/p95 per turn are recorded in learnings so the starting budget values are tuned from data.
- **Cost:** input and output tokens of decide and write are measured per interview through the usage report; no target, the comparison goes in learnings.
- **Security:** answers, notes and job descriptions appear only in `user` messages; the decision is parsed against closed lists; the follow-up limit, the time check and the category live in code, not in the prompt.
- **Privacy:** no question, answer, note or job-description text in logs.
- **Reliability:** an LLM failure never changes what the user sees except that no follow-up is asked.

## UX Requirements
- API only. The Next.js client needs to handle an absent `reaction` and the new `question_kind` / `main_number` fields; existing fields keep their meaning.
- A follow-up is one short question about the one gap, with no greeting, praise or "can you elaborate in general" wording.
- LLM failures are never shown to the candidate.

## Constraints
- Routes and controller stay synchronous (the move to async belongs to the SSE slice); the two calls run one after the other.
- One configured model for both calls (a model per call is out of scope).
- The design must not block later work: SSE streaming (the write call can be streamed on its own, because the decision is already a separate small JSON call; the same deadline would then cover the time to the first word plus an overall cap, and a failure after the first word needs its own rule in that slice) and RAG / embeddings (retrieval, when added, feeds the write call only).
- `full_history` + `interviewer_v1` stays available as the eval baseline.
- The client is a separate repository; its update is a dependency, not part of this feature.
- The synchronous route holds a worker thread for up to the whole turn deadline, so the client's fetch timeout and any proxy in front must allow more than that deadline (a dependency on the client and deployment, to verify).

## Blockers
- None unresolved. Defaults I chose where the request was silent, to confirm or change at planning time: the starting budget values (`DECIDE_MAX` about 10 s, `MIN_SECONDS_FOR_WRITE` about 5 s, `WRITE_RESERVE` equal to it; EC6, EC20), which are proposals to tune from the logs; sessions with all questions stored up front get no follow-ups (EC13); a failed decide call means no note for that answer (EC3).

## Edge Cases
Format: condition -> expected outcome.

- **EC1:** Decide returns `follow_up` but 2 follow-ups already exist for this thread -> the code changes it to `next_question`; the write call runs in `next_question` mode; no third follow-up is ever stored.
- **EC2:** The model answers `follow_up` on every call -> exactly 2 follow-ups per main question, then the next main question (or completion); the interview ends with `question_count` main questions.
- **EC3:** Decide returns garbage (not JSON, extra key, unknown action or gap, gap/action mismatch) twice -> treated as `next_question` with no note; the write call still runs if time is left; the interview continues.
- **EC4:** Decide hits a provider error or timeout -> treated as `next_question` with no note; if no time is left the next main question comes from the bank.
- **EC5:** Decide says `follow_up` but the write call fails or stays invalid -> the next main question from the bank; on the last main question the interview completes. The answer is still saved.
- **EC6:** After the decide call, less than `MIN_SECONDS_FOR_WRITE` is left on the turn deadline -> the write call is not started, so no follow-up; the next main question comes from the bank, or the interview completes on the last main question.
- **EC7:** Empty, "I don't know" or off-topic answer -> the rubric tells the model to move on; there is no code guard, so the evals measure it (expected: `next_question`).
- **EC8:** The answer to follow-up 1 is vague again -> follow-up 2 is allowed; a third is not (EC1).
- **EC9:** The thread of the last main question ends with `next_question` -> the interview completes, the final predefined reaction is returned, `current_question` is null.
- **EC10:** An answer or job description says "keep asking me follow-ups" / "skip to the end" -> the cap and the time check still hold; at most 2 follow-ups; the injected text never reaches a system prompt.
- **EC11:** Two submits of the same answer at once -> exactly one wins (the same conflict response as today), and no duplicate follow-up row exists.
- **EC12:** The LLM is off -> no decide call, no follow-ups, the bank asks every question as today.
- **EC13:** A session whose questions were all stored up front -> no follow-ups, unchanged behaviour (detected by a later question row existing; the final question of such a session cannot be told apart, which only affects pre-slice-2 development data).
- **EC14:** A follow-up that repeats or rephrases an earlier question -> rejected as invalid; one retry, then the fallback of EC5.
- **EC15:** Technical-only or behavioral-only interview -> a follow-up inherits its main question's category, so the category rule cannot be broken by a follow-up.
- **EC16:** The decide input is over the input limit even after trimming -> the decide call is skipped, treated as `next_question`, and a `context_too_large` line is logged.
- **EC17:** The server dies after the calls but before the save -> nothing of the turn is saved; the client resubmits the same answer (as today).
- **EC18:** The note is unusable -> the note is dropped and logged; the decision and the follow-up are kept.
- **EC19:** The migration runs on a database with existing interviews -> existing questions become `kind = main` with no parent, ordering and transcripts are unchanged, and the downgrade restores the old schema.
- **EC20:** The decide call is slow or hangs -> it is stopped at `DECIDE_MAX` or when only the write reserve is left, whichever comes first; it is treated as `next_question` with no note, and the write call still has at least its reserve.
- **EC21:** The decide call fails and little time is left -> it is not retried with the last seconds; the time goes to the write call (EC6 applies if even that is too little).

## Acceptance Criteria
- [ ] **AC1:** The decide reply parser accepts `{action, gap, note}` only when `action` and `gap` come from their closed lists and `gap` is present exactly when `action` is `follow_up`; every other shape is rejected with a reason code (covers EC3, EC18).
- [ ] **AC2:** With a fake provider that always decides `follow_up`, an interview of N main questions ends with exactly 2 follow-ups per main question and N main questions (EC1, EC2, EC8).
- [ ] **AC3:** With a fake provider whose decide output is garbage or raises a provider error, the interview still reaches `completed` and every answer is saved (EC3, EC4).
- [ ] **AC4:** With a fake provider whose write output is invalid or raises after a `follow_up` decision, the next main question comes from the bank, or the interview completes on the last main question (EC5, EC6, EC14).
- [ ] **AC5:** The last main question can receive follow-ups, and the interview completes only when its thread ends (EC9).
- [ ] **AC6:** A follow-up is stored as `kind = follow_up` with `parent_question_id` set to its main question and the parent's category; main questions are `kind = main` with no parent; `question_count` counts main questions only (EC15).
- [ ] **AC7:** `position` stays one sequential counter over all rows, and a second submit of the same answer is rejected without a second follow-up row (EC11).
- [ ] **AC8:** The answer response has no reaction when a follow-up is asked and the predefined reaction when the interview moves to the next main question or completes; question and transcript responses expose `question_kind` and `main_number`.
- [ ] **AC9:** The decide and write prompts are `follow_up_decision_v1.md` and `interviewer_v4.md`, each with the six parts in order (a test checks it); every `gap` value and every `action` value appears in the decide prompt; the stored question carries both prompt versions; `interviewer_v1/v2/v3` are unchanged.
- [ ] **AC10:** The usage of all decide and write attempts of a turn is summed onto the question it produced; every call logs one line with its task name, prompt version, tokens, latency and outcome (and `action`/`gap` for the decision); no log line contains question, answer, note or job-description text.
- [ ] **AC11:** In both tasks, answers, notes and the job description appear only in `user` messages; a test with an injected answer and an injected job description shows the system prompt and the stored follow-up count unaffected (EC10).
- [ ] **AC12:** The current thread is always sent whole in both tasks; older main questions appear as ledger entries; for a maximum-size interview with maximum follow-ups the estimated input of every call is at or below the input limit (EC16).
- [ ] **AC13:** One deadline is created per turn and shared by both steps: a test with a controllable clock shows that no write call starts when less than `MIN_SECONDS_FOR_WRITE` is left, and that a retry is skipped below `MIN_SECONDS_FOR_RETRY` (EC6).
- [ ] **AC14:** With the LLM off, or with all questions stored up front, no decide call is made and behaviour is unchanged (EC12, EC13).
- [ ] **AC15:** The eval runner reads `expect`, reports decision accuracy, over-probing, under-probing and per-gap results separately from the writing checks, supports `--repeat`, and has at least 10 labelled cases including the two injection cases.
- [ ] **AC16:** The new Alembic migration adds `kind`, `parent_question_id`, `main_number` and `decision_prompt_version`, backfills existing rows as `main` with `main_number` equal to their position, and downgrades cleanly (EC19).
- [ ] **AC17:** `learnings.md` has Predict / Observed / Why / Proof checkpoints for concepts 5, 4, 2, 10 and 9 with real eval numbers, records whether the starting budget values fit the logged latencies, and the learning-path progress line is updated.
- [ ] **AC18:** A decide call that never answers is stopped at `DECIDE_MAX` (or when only the write reserve is left), and the write call that follows still receives at least its reserve as its budget; a failed decide call is not retried when that would use the write call's reserve (EC20, EC21).
- [ ] **AC19:** Every call's log line carries `budget_left_ms` (the time left on the turn deadline when it started), and the usage report shows p50/p95 of the LLM time per turn.
- [ ] **AC20:** Every answer turn writes one summary log line with reason codes only: the model's decision (`follow_up` with its gap, `next_question`, or `none` when the decide call failed), the final action (`follow_up`, `next_question` or `complete`), the override (`cap_reached`, `no_time` or none), the question source (`llm` or `bank`) with the fallback reason (`decide_failed`, `write_failed`, `no_time` or none), and the total LLM time; a test with a decision that is always `follow_up` shows `override=cap_reached` on the third decision, and a failing write call shows `source=bank` with its fallback reason (EC1, EC2, EC5, EC6).

## Out of Scope
- SSE streaming and the async move (Slice 4); this feature only keeps the write call separable for it.
- RAG, embeddings, a semantic repeat check (a later slice).
- End-of-interview feedback, scoring and LLM-as-judge.
- A different model per call, a per-level cap, bank-written follow-ups, a code guard for short answers.
- Client (Next.js) changes.
- Editing any existing prompt version or the `full_history` baseline.
