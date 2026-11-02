# Feature: SSE Streaming of the Interview Turn (Slice 4)

## Problem
Answering a question is one blocking `POST /interviews/{id}/messages`. The candidate waits on a spinner while the decide call and the write call run (several seconds, up to the 30 s turn deadline), then the whole next question appears at once. The page gives no sign of what is happening, and the wait feels longer than it is. The learning path's concept 7 (streaming and latency) is also unproven: nothing yet shows why streaming needs `async`, how structured output and streaming conflict, or how a turn is saved when it is only complete after the stream ends.

## Goal
A new streaming endpoint sends the turn as Server-Sent Events. The candidate sees progress at once ("received", "deciding") and then the next question written out word by word. Two targets are measured and logged per turn:


- the first event arrives within 1 s of the request;
- the first question token arrives within 1 s of the write call starting.

The interview stays consistent whatever happens mid-stream: a turn is either saved whole or not at all. AI behaviour stays measurable: `interviewer_v5`, which can be streamed, is compared with `interviewer_v4` on the eval set.



Delivered in two phases:
- **Phase A, plumbing:** the stream endpoint, the event contract, progress events, and the turn sent whole in `done`. No prompt change.
- **Phase B, tokens:** an async provider `stream()`, `interviewer_v5`, the question streamed token by token, and the reset/retry/fallback rule.

## Project Conventions
- Rule files consulted: `CLAUDE.md` (project root; there is no `.claude/` directory), the user's global `~/.claude/CLAUDE.md`, `docs/ai-engineering-learning-path.md` (Slice 4, concept 7), and the specs of `follow-up-questions` and `context-management`.
- Constraints those rules impose on this feature:
  - Router → controller → repository. Feature files keep the `interviews_` prefix. The route stays thin and holds no turn logic.
  - **New dependency: `sse-starlette`** (the user's choice). Why: the route returns the stream explicitly, so pre-stream checks fail as normal HTTP errors before any byte is sent; it also detects disconnects explicitly and lets the ping interval be configured. FastAPI 0.162's built-in `fastapi.sse` was considered and not chosen. The reason goes in the PR description.
  - Prompts are versioned data files. `interviewer_v1`–`v4` stay untouched. The streamable format is a new `interviewer_v5.md` with the six parts (Role, Task, Input, Output, Constraints, Capabilities).
  - LLM calls stay behind the `LLMProvider` interface (`app/core/ai/`) and the `ContextManager`. Nothing vendor-specific reaches the interviews module. `FakeProvider` gains streaming for tests.
  - LLM output is still validated before it is saved, with a retry and a safe fallback (the bank).
  - Every call logs model, prompt version, tokens, latency and outcome. **Logs never contain question, answer or job-description text, and neither do the SSE error events.**
  - Candidate and job-description text stays untrusted and appears only in `user` messages.
  - Errors use the structured `AppError` types and `ErrorBody` (`code`, `message`, `request_id`). Clients get generic messages; details go to logs.
  - Tests mock the LLM. Real-model eval runs stay opt-in.
  - `docs/features/sse-streaming/learnings.md` is a deliverable (Predict / Observed / Why / Proof, including concept 7's Proof answers). The learning-path progress line for Slice 4 is updated.
  - Nothing is committed or pushed.
- Findings from the code that frame this spec:
  - Everything is sync today: `def` routes, sync httpx `complete()` with `time.sleep` backoff, sync SQLAlchemy.
  - The controller reads all state, calls `repo.release()` before the LLM calls, and saves the turn with one atomic `record_turn`, which returns `False` when it loses a race. This already gives "saved whole or not at all".
  - `interviewer_v4` returns JSON (`{question}` in follow-up mode, `{question, category}` in next-question mode). The running note comes from the decide call, not the write call.
  - The reaction line is predefined (`pick_reaction`), not LLM text.

## User Flow
1. The candidate submits an answer. The Next.js client calls `POST /interviews/{id}/messages/stream` with `fetch` and reads the body as a stream. The httpOnly cookie is sent, and `EventSource` is not used because it only supports GET.
2. If the request is invalid (not signed in, no permission, not their interview, interview not in progress, not the current question, bad body), the client gets a normal JSON error with the usual status code and no stream starts.
3. Otherwise the stream opens and `status: received` arrives at once, followed by `status: deciding` while the decide call runs.
4. When the turn moves on or completes, the predefined reaction arrives as its own event before the next question.
5. `status: writing`, then the next question appears word by word.
   - If the finished question fails the checks, or the provider or deadline fails mid-question, a `reset` event clears the text. Then either the retry streams, or the bank question arrives whole.
6. `done` arrives with the same body `POST /messages` returns today (`AnswerOut`), and the stream closes. The turn is now saved.
7. If the candidate closes the tab before `done`, nothing is saved. On return, `GET /interviews/{id}` shows the same question, and they submit the answer again.

```
event: status    data: {"phase":"received"}
event: status    data: {"phase":"deciding"}
event: reaction  data: {"text":"Thanks, that gives me a clear picture."}
event: status    data: {"phase":"writing"}
event: question.delta  data: {"text":"Tell me about"}
event: question.delta  data: {"text":" a time you..."}
event: done      data: {"session":{...},"reaction":{...},"current_question":{...}}
```

## Requirements

### Functional
**Endpoint**
- New `POST /interviews/{session_id}/messages/stream`. It takes the same body (`AnswerIn`) and permission (`interviews_answer`) as `POST /messages`.
- `POST /messages` (JSON) keeps its behaviour and keeps using `interviewer_v4`.
- `POST /interviews` (start) is unchanged.
- These checks run **before the stream opens** and return normal JSON errors:
  - 401 (no or invalid token)
  - 403 (missing permission)
  - 404 (unknown or not-owned session, the same response for both)
  - 409 `SESSION_NOT_IN_PROGRESS`
  - 409 `QUESTION_NOT_CURRENT`
  - 422 (body validation)
- The response is `text/event-stream`, uncached and unbuffered by proxies, with heartbeat comments while the stream is idle.

**Event contract** (each event is a typed schema, and the contract is documented for the Next.js side)
- `status`: `phase` ∈ `received` | `deciding` | `writing`.
- `reaction`: the predefined reaction text. Sent as soon as the final action is certain to be "move on" or "complete". When a follow-up falls back to the bank, the reaction is sent only in `done`.
- `question.delta`: a chunk of the next question's text (Phase B).
- `reset`: discard the question text streamed so far (Phase B).
- `done`: the `AnswerOut` body, the same shape `POST /messages` returns. This is the single source of truth for the saved turn.
- `error`: `code` and a generic `message` (plus `request_id`), never raw exception or LLM text.
- Every stream that opens ends with **exactly one** terminal event, `done` or `error`, and then closes. Nothing comes after it.

**Turn behaviour on the stream path**
- Same decide call, the same code-enforced follow-up cap, and one shared turn deadline, exactly as in `follow-up-questions`.
- Same outcomes as the JSON endpoint for the same inputs: the same actions, fallbacks and saved rows. The only difference is the prompt version recorded on LLM-written questions.
- Sessions without an LLM, and pre-stored sessions, still work: `received` → (`reaction`) → `done`.
- The turn is saved once, with the existing atomic `record_turn`, after the question is final and before `done`. No DB session or transaction is held open while waiting on the LLM.

**Phase B: streaming the question**
- `LLMProvider` gains an async streaming method that yields text chunks and ends with the same usage record as `complete()` (model, tokens, cached and reasoning tokens when reported, latency, finish reason). It keeps the timeout and budget rules. It retries only before the first chunk; once a chunk has been yielded, a failure ends the attempt and is never retried silently.
- `OpenRouterProvider` implements it with an async HTTP client. `FakeProvider` can script chunk sequences, mid-stream failures and delays.
- `interviewer_v5.md`: in next-question mode, the first line is a header naming the category, followed by the plain question text. In follow-up mode it is the plain question text only. There is no JSON and no code fence. The code reads the header before streaming any text, so the category is never shown to the candidate.
- The complete question goes through the same checks as today (one question mark at most, correct category for non-mixed interviews, not a repeat of any earlier question). If it fails, send `reset`, then make one retry if the deadline allows (the same `MIN_SECONDS_FOR_RETRY` rule); otherwise the bank question is sent whole in `done`.
- A provider failure or a deadline expiry after some question text was sent is handled the same way (`reset`, then retry or bank). The candidate is never left without a next question, and the turn is saved normally.
- The decide call stays a non-streamed call. It runs off the event loop so it doesn't block other requests.

**Disconnect**
- When the client disconnects before `done`:
  - the in-flight streaming LLM call is cancelled;
  - nothing is saved (the session stays on the same question);
  - the usage of any call already made is still logged, marked as cancelled.
- A decide call that is already running finishes in the background and its result is discarded.

**Observability (per turn, no text)**
- These are logged: time to first event, time to first question token (from the write call starting), total turn time, the number of resets, whether the turn was cancelled, and the terminal event.

**Evals**
- The eval runner can run `interviewer_v5` on the existing write cases. A real-model comparison (3 repeats, opt-in) of v4 and v5 is recorded in `learnings.md`.

### Non-Functional
- **Latency:** the first event within 1 s of the request (server side, fake provider). The first question token within 1 s of the write call starting (real model, measured from logs, recorded in learnings).
- **Concurrency:** while a stream waits on the provider, other requests are served. The streaming path doesn't block the event loop, and sync DB work runs off the event loop.
- **Cost:** a disconnect stops paying for the write call. Usage is never lost from the logs.
- **Security:** the same auth, permission and ownership checks as the JSON endpoint, before any stream opens. Untrusted text is handled as today. No PII or LLM text appears in logs or error events.

## UX Requirements
- The candidate sees something within about 1 s of submitting: a `received`, then a `deciding` state.
- The question "types" in. A `reset` clears it cleanly, with no half-old, half-new text.
- `error` events give a generic message and a code the client can act on. For example, `QUESTION_NOT_CURRENT` means reload the interview.
- Closing the tab is safe: on return, the same question is waiting and the answer can be resubmitted.
- The client contract (event names, payloads, terminal rule, abort on unmount) is written down for the Next.js side.

## Constraints
- FastAPI 0.162, Python 3.14, `uv`, sync SQLAlchemy (no async engine in this slice).
- Async only on the streaming path. The existing sync routes, `complete()` and the `Interviewer` sync path stay.
- OpenRouter is the only real provider.
- Single backend instance: no pub/sub, no background workers.

## Blockers
- None. All decisions settled in the spec interview (2026-11-01):
  - scope: full Slice 4, phased
  - v5 header-line format
  - reset → retry → bank
  - stop and save nothing on disconnect
  - async on the stream path only
  - two latency targets
  - new endpoint
  - answers only
  - v5 on stream only
  - v5 no worse than v4 on evals
- Assumptions to verify in the plan (external behaviour):
  - OpenRouter's streaming mode reports token usage at the end of the stream, and reports mid-stream errors as an error chunk rather than an HTTP status *(assumption — verify)*.
  - `sse-starlette` detects client disconnects and cancels the async generator so cleanup runs *(assumption — verify)*.
  - The Next.js proxy path doesn't buffer `text/event-stream` *(assumption — verify on the client side)*.

## Edge Cases
- **EC1:** Not signed in, missing permission, or bad body → 401 / 403 / 422 JSON error, no stream.
- **EC2:** A session that doesn't exist or belongs to another user → 404 JSON error (the same body for both), no stream.
- **EC3:** A completed session → 409 `SESSION_NOT_IN_PROGRESS` JSON error, no stream.
- **EC4:** The `question_id` isn't the current question → 409 `QUESTION_NOT_CURRENT` JSON error, no stream.
- **EC5:** Two tabs submit the same question at once → both may stream. Exactly one saves the turn and gets `done`. The other gets an `error` event `QUESTION_NOT_CURRENT` and saves nothing.
- **EC6:** The client disconnects during `deciding` or `writing` → the streaming LLM call is cancelled, nothing is saved, the session stays on the same question, and usage made so far is logged as cancelled.
- **EC7:** The streamed question fails the checks (two question marks, wrong category, repeat) and there is time to retry → `reset`, then the retry streams, then `done`.
- **EC8:** The streamed question fails the checks and there is no time to retry → `reset`, then `done` with the bank question.
- **EC9:** The provider fails or the deadline expires after some question text → `reset`, then retry (if time allows) or the bank question, then `done`. The turn is saved.
- **EC10:** The provider fails before any text → no `reset` (nothing to clear). Same retry-or-bank rule, then `done`.
- **EC11:** The v5 header line is missing or names an invalid category in next-question mode → counted as an invalid reply (retry or bank). No question text is streamed for that attempt.
- **EC12:** The decide call fails or returns invalid JSON → the same fallback as today (`next_question`), and the stream continues to `writing`.
- **EC13:** The action is a follow-up and the write succeeds → no `reaction` event, and `done.reaction` is `null`.
- **EC14:** The action is a follow-up and the write falls back → the action becomes move on or complete. The reaction is sent only in `done`, with the bank question.
- **EC15:** The last main question's thread ends → `reaction` (final), then `done` with `current_question: null` and the session completed. No `writing`.
- **EC16:** The session has no LLM configured, or is pre-stored → `received`, then `reaction`, then `done`. No `deciding` or `writing`.
- **EC17:** An unexpected server error after the stream opened → one `error` event (`INTERNAL_ERROR`, generic message, `request_id`), nothing saved, and details only in the logs.
- **EC18:** `record_turn` fails after the question was streamed → `error` event, nothing saved. The candidate resubmits.
- **EC19:** An idle wait longer than the ping interval → heartbeat comments keep the connection open, and no data events are invented.

## Acceptance Criteria
**Phase A**
- [ ] **AC1:** `POST /interviews/{id}/messages/stream` exists. On success it returns `text/event-stream` with no-cache and no-buffering headers. `POST /messages` and its tests are unchanged.
- [ ] **AC2:** Every pre-stream failure (EC1–EC4) returns the normal JSON `ErrorResponse` with the same status and code as `POST /messages`, and no stream body.
- [ ] **AC3:** A successful stream sends events in contract order (`status: received` → `status: deciding` → optional `reaction` → `status: writing` → … → `done`) and ends with exactly one terminal event.
- [ ] **AC4:** The `done` payload validates as `AnswerOut` and equals what the JSON endpoint returns for the same scripted inputs.
- [ ] **AC5:** After `done`, the DB holds exactly the rows the JSON endpoint would save for the same turn: answer, note, reaction, next question, position or completion.
- [ ] **AC6:** A client disconnect before `done` saves nothing, and the session's current question is unchanged (EC6).
- [ ] **AC7:** EC5 (two concurrent submits): exactly one `done` and one `error` `QUESTION_NOT_CURRENT`, and exactly one saved turn.
- [ ] **AC8:** EC17 and EC18 produce a single `error` event with `code`, a generic `message` and `request_id`. The event never contains exception text, LLM text or answer text.
- [ ] **AC9:** EC13–EC16 send `reaction` and `writing` exactly as specified.
- [ ] **AC10:** With the fake provider, the first event is sent within 1 s of the request, and the time to first event is logged.

**Phase B**
- [ ] **AC11:** `LLMProvider` has an async streaming method. `OpenRouterProvider` and `FakeProvider` implement it and yield chunks plus a final usage record with the same fields as `complete()`. It retries only before the first chunk.
- [ ] **AC12:** `interviewer_v5.md` exists with the six parts. v1–v4 are byte-for-byte unchanged.
- [ ] **AC13:** The question arrives as two or more `question.delta` events for a multi-chunk fake reply, and their joined text equals the saved question. The category header is never in any delta.
- [ ] **AC14:** EC7–EC11 behave as specified: `reset` only when text was already sent, then a retry or the bank question, and the turn is saved.
- [ ] **AC15:** A disconnect during `writing` cancels the streaming provider call (the fake records the cancellation), and usage is logged as cancelled.
- [ ] **AC16:** While one stream waits on a slow fake provider, a second request to another endpoint completes without waiting for it.
- [ ] **AC17:** Per-turn logs include the time to first event, the time to first token, total time, resets, cancelled and the terminal event, and contain no question, answer or job-description text.
- [ ] **AC18:** The eval runner can run v5. A real-model v4 vs v5 comparison (3 repeats) is recorded in `learnings.md`, and v5 is no worse than v4 on valid replies and on the injection cases.
- [ ] **AC19:** The real-model time to first token from the write call starting is measured in a live run and recorded in `learnings.md` against the 1 s target.
- [ ] **AC20:** `learnings.md` answers concept 7's Proof (why streaming needs `async`; how a turn that is only complete when the stream ends is saved). The learning-path progress line for Slice 4 is updated.
- [ ] **AC21:** The event contract (names, payloads, terminal rule, error codes) is documented for the Next.js client.

## Out of Scope
- **Streaming the interview start** (`POST /interviews`): a follow-up, kept as JSON to keep this slice to one streaming route.
- **Streaming the decide call:** its output is internal JSON and never shown.
- **Making the whole stack async** (the async SQLAlchemy engine, an async `complete()`, async JSON routes): too big for this slice. Only the streaming path is async.
- **Resume or replay of a dropped stream** (`Last-Event-ID`, stored events): a dropped turn is simply resubmitted.
- **Finishing generation after a disconnect, background workers, pub/sub or multiple instances:** not needed on a single instance, and it would pay for tokens nobody sees.
- **Switching the JSON endpoint to v5:** only after the eval comparison argues for it.
- **The Next.js implementation itself:** this repo documents the contract only.
- **Rate limiting the new endpoint:** it follows whatever the existing `POST /messages` has. No new limits here.
