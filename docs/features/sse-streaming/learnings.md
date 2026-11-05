# Learn: Streaming and latency (Slice 4, SSE)

**Concept 7** in `docs/ai-engineering-learning-path.md`. Related: structured output (4), reliability (6).
Read this top to bottom once, then do section 6 with the app running.

---

## 1. Why it exists

Before this slice, answering a question was one blocking request: decide what to do, write the next question, save,
return. The candidate stared at a silent page for the whole decide + write time (several seconds with a real model).
Nothing on screen said the app was alive.

Two things make that worse for LLMs than for normal APIs:

- A model call is slow and its duration varies (queueing, input length, output length).
- You can't tell in advance how long it will take, so a plain spinner can't promise anything.

## 2. What it is

**Streaming** means sending the answer to the client in pieces while it is still being produced, instead of waiting
for the whole thing.

- The model API supports it: with `stream: true` it sends tokens as small chunks.
- **SSE (server-sent events)** is how Cuewise forwards them to the browser: one long-lived HTTP response with the
  header `text/event-stream`. Each event is a few text lines: `event: <name>`, `data: <json>`, then a blank line.
- Streaming doesn't make the model faster. It changes what the candidate **sees** and when: the first words (or a
  progress message) appear early.

Two numbers describe latency, and they are not the same:

| Metric | Meaning |
|---|---|
| **Time to first token (TTFT)** | From the request until the first piece of text arrives. Drives how fast it *feels*. |
| **Total latency** | Until the last piece arrives. Drives how long the reply takes to read fully. |

TTFT is mostly queueing plus the model **reading your input** (prefill). Total latency adds the time to **write**
the output. That distinction matters in section 7.

## 3. When to use it

| Stream the text when | Don't expect much when |
|---|---|
| The output is long (hundreds of tokens), like the end-of-interview feedback: generation time dominates | The output is short, like a ~30-token question: the model spends its time *before* the first token (section 7) |
| The wait is long and silent: progress events alone already help | The reply must be validated before anyone may see it (a rejected draft has to be taken back) |
| The candidate reads while it is written | Nobody is watching (a background job) |

What streaming gave *this* slice was mostly the **progress events** (`received`, `deciding`, `writing`), not the
token-by-token text.

**I'd revisit this when** the end-of-interview feedback is built: that is the output where token streaming should
pay off, and it will need the same save-at-the-end rule.

## 4. How it works

**The options.** The hard part: slice 3 made the interviewer's output **JSON** (`{action, message}`), and you can't
show half a JSON object to a user.

| Option | How it works | Trade-off |
|---|---|---|
| Stream the JSON, parse at the end | Show nothing until the JSON is complete | No benefit: it is the old behavior |
| Parse the JSON as it streams | Incremental JSON parser, show the `message` field early | Fragile; a malformed prefix breaks it |
| **Two calls: decide, then write** (chosen) | A small structured **decide** call picks the action; a second **write** call streams plain text | One extra call, but each call has one job |
| Plain text with a header line (`interviewer_v5`, chosen for the write call) | First line `CATEGORY: <x>` (never shown), then the question text | Validation happens **after** display, so a bad draft must be taken back |

Decision: keep the JSON decide call from slice 3 (the model decides, the code enforces), and stream only the write
call as plain text. The header line is read before any text is sent, so a reply without one shows nothing.

**The flow.**

```
POST /interviews/{id}/messages/stream
  route        interviews_route.py:126   answer_question_stream: runs the checks, then opens the stream
  controller   interviews_controller.py:446   stream_answer: turns internal events into SSE events
  turn         interviews_turn.py:211   stream_turn: decide (worker thread) -> write (async stream)
  write        interviews_turn.py:246   _stream_write: attempts, validation, Reset on a bad draft
  provider     openai_compatible.py:102   stream(): chunks, then a final LLMResult with token usage
  save         interviews_repository.py:163   record_turn: one atomic save, then `done`
```

Follow one turn:

1. **The route runs the checks first** (`prepare_answer`, in a threadpool), so ownership or "not current question"
   errors come back as plain JSON errors, before any stream opens.
2. **`stream_answer` sends `status: received`** at once. This is the first thing the candidate sees.
3. **`stream_turn` yields `deciding`**, runs the blocking decide call in a worker thread (so the event loop stays free),
   then yields `ActionKnown` when the action is not a follow-up. The controller turns that into a `reaction` event.
4. **It yields `writing`**, then `_stream_write` calls the provider's `stream()`. Each chunk becomes a
   `question.delta` event.
5. **If the finished draft is invalid** (for example it repeats an earlier question), the turn sends `reset`, the client
   clears the text, and the write is retried or falls back to the bank.
6. **`finish_answer` saves everything in one commit** (`record_turn`), and only then is `done` sent.

The event contract with the client is the `StreamEvent` enum (`interviews_constants.py:106`): `status`, `reaction`,
`question.delta`, `reset`, `done`, `error`. Every stream ends with exactly one `done` or `error`.

The provider stays vendor-neutral: `stream()` is part of the `LLMProvider` interface (`provider.py:94`), so the
streaming logic doesn't know it is talking to Google. Retries happen only **before the first chunk** is yielded,
because after that the candidate may already have read it (`openai_compatible.py:113`).

## 5. What can go wrong

| Failure | What the candidate sees | What the code does | Proof |
|---|---|---|---|
| Not the current question, or not the owner | A plain JSON error (409/404), no stream | Checked in `prepare_answer` before the stream opens | `test_a_question_that_is_not_current_is_a_json_409` |
| Candidate leaves while deciding | Nothing | The stream is cancelled, the decide result is dropped, nothing is saved | `test_leaving_while_the_decide_call_runs_saves_nothing` |
| Candidate leaves while the question streams | Nothing | The provider's HTTP stream is closed (no more tokens), nothing is saved | `test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing` |
| Provider fails after text was shown | The draft disappears (`reset`), then a new attempt | `_stream_write` sends `reset` and retries (the provider can't: it already sent text) | `after_output` handling in `_stream_write` |
| Reply has no or a broken `CATEGORY:` line | Nothing of that draft | `InvalidReplyError`, logged, next attempt | `_stream_write` (`invalid_reply:*` log) |
| Finished draft fails a check (e.g. repeats a question) | The text, then `reset` | Retry, or fall back to the bank | `_stream_write` |
| Two tabs submit the same answer | One tab: `done`. The other: `error QUESTION_NOT_CURRENT` | Compare-and-swap in `record_turn` | `test_two_submits_of_one_question_save_one_turn_and_the_loser_gets_an_error_event` |
| The save fails | One generic `error` event | Nothing was written, `INTERNAL_ERROR` logged | `stream_answer`'s `except Exception` branch |
| Context too large for the write call | Falls back | Logs `context_too_large` and yields no draft | `_stream_write` |
| How Google reports an error *mid-stream* | not observed | Both an error chunk and a dropped connection are handled and unit-tested | still open (section 9) |

## 6. Try it yourself

Do these in order. **Write your prediction first**, then run.

**Exercise A: how early is the first token?**

1. Predict: the first question token will arrive after about half of the total write time. Yes or no?
2. Run `uv run python -m app.modules.interviews.interviews_evals --task stream --repeat 1`.
3. Compare `average_first_token_ms` with the average total latency. Where did your prediction go wrong?

**Exercise B: what does a dropped stream leave behind?**

1. Predict what the database holds if you close the tab during `writing`.
2. Read `tests/modules/interviews/test_stream_answer.py` and find
   `test_leaving_while_the_question_streams_cancels_the_call_and_saves_nothing`.
3. Check your prediction against what `record_turn` saved (nothing, and why).

**Exercise C: a race between two tabs**

1. Read `record_turn` (`interviews_repository.py:163`) and find the conditional `UPDATE ... WHERE current_position`.
2. Predict what the second tab gets if both submit the same answer.
3. Find the matching test:
   `test_two_submits_of_one_question_save_one_turn_and_the_loser_gets_an_error_event` in
   `tests/modules/interviews/test_answer_stream.py`.

**Exercise D: is the server blocked while a stream waits?**

Run `test_other_requests_are_served_while_a_stream_waits_on_the_llm` (in `test_answer_stream.py`) and read why it
passes. Then think about what would change if `stream_answer` were a plain `def`.

## 7. What surprised me

These are the real results from the build. Each one is a lesson.

**Surprise 1: streaming barely moved the wait for the question text.** Measured with `--task stream --repeat 1`,
`gemini-3.5-flash-lite`, 19 cases, 2026-11-02:

| | value |
|---|---|
| valid replies | 19/19 (both injection cases ignored) |
| average time to first question token | 2,001 ms (567 to 4,226 ms) |
| under the 1 s target | 7 of 19 |
| average total latency of the write call | 2,231 ms |
| output per question | about 30 tokens, in 1 to 2 chunks |

My prediction was that the first words would appear well before the whole question. They didn't: **a question is short**
(about 30 tokens). The model spends almost all its time *before* the first token (queueing, reading 850 to 1,450 input
tokens), then sends the whole question in one or two chunks. The first token arrives about 100 ms before the last.

What actually helped:

- **Progress events.** `received` arrives at once and `deciding`/`writing` show the app is working. Before this slice
  the page was silent.
- **Shorter input and a faster model**, because TTFT follows prefill and queueing, not output length. This ties back to
  context management (concept 2).

**Surprise 2: the real cost of streaming is validating after display.** v4 (JSON) validates before anything is shown.
v5 (header + text) shows text first, so a bad draft has already been read:

| | v4 (JSON) | v5 (header + text) |
|---|---|---|
| shown while streaming | no (half a JSON object) | yes, after the first line |
| parse failure mode | broken JSON | a missing or broken header line |
| what reaches the candidate on failure | nothing (validated first) | a draft, taken back by `reset` |
| category | a field | the first line, never shown |

v5 passed 19/19 on one repeat with no header failures. The 3-repeat v4 baseline is still open (section 9).

**Surprise 3: "save at the end, all or nothing" removed a whole class of problems.** The turn already had one atomic
save. The streamed turn calls it once, after the question is final and before `done`. A client that leaves before that
point cancels the stream and nothing is saved, so the same question is still current. That needs no half-turn state,
no resume protocol and no regenerate endpoint. The cost: a re-submit after a dropped connection, which is fine because
the answer is still in the client's input box.

## 8. Check your understanding

Answer these without scrolling up, then compare.

1. **(Proof)** Why does streaming need `async`?
2. **(Proof)** How is a message saved that is only complete when the stream ends?
3. **(Why)** Why is the average time to first token about 2 s even though streaming works?
4. **(When)** For which future feature would token streaming help more than it does here, and why?
5. **(How)** How does the code handle a provider failure after the first chunk was already shown?
6. **(What if)** What if `done` were sent *before* the commit in `record_turn`?

<details>
<summary>Reference answers (write yours first)</summary>

1. A stream keeps the request open for seconds while it waits on the model. With a blocking call, each waiting stream
   would hold a worker thread for its whole lifetime, and the threadpool caps how many candidates can wait at once.
   With `async`, waiting for the next chunk gives control back to the event loop, so one process serves other requests
   meanwhile. `async` also makes cancellation possible: when the client leaves, the task is cancelled and the
   provider's HTTP stream is closed, so no more tokens are generated. The decide call is still the sync `complete()`
   run in a worker thread; it can't be cancelled mid-call, so its result is dropped, which is fine for about a second.
2. It isn't saved while it streams. The streamed text is a preview, and the saved row is built from the final,
   validated reply. That row is saved in one transaction with the answer, the reaction and the session's new position,
   and `done` is only sent after that commit. If the stream stops before then, nothing was written. A race between two
   submits is settled by the compare-and-swap in `record_turn`, not by the stream.
3. A question is short (about 30 tokens), so almost all the time is spent before the first token: queueing and reading
   the input. Streaming cannot shorten that part.
4. The end-of-interview feedback: hundreds of tokens, where generation time dominates, so the first words can appear
   long before the last.
5. The provider can't retry (it already sent text), so it raises the error with `after_output` set. `_stream_write`
   sends `reset` so the client clears the draft, then retries the attempt itself.
6. The client would believe the turn was saved when it might not be: a failed commit would leave the candidate on a
   question the server never advanced, with no way to know. That is why `done` is the last event, after the commit.

</details>

## 9. Go deeper / Still open

- Spec and plan: `docs/features/sse-streaming/spec.md`, `plan.md`.
- Why `EventSource` doesn't fit a POST: it only supports GET, so the Next.js side reads the stream with `fetch` and a
  reader.
- Next concept this unlocks: long outputs (end-of-interview feedback), where streaming pays off more.

**Still open:**

- The 3-repeat comparison on the same cases (pause between runs: the free tier rate-limits at about 25 calls):
  `uv run python -m app.modules.interviews.interviews_evals --task write --repeat 3` (v4) against
  `uv run python -m app.modules.interviews.interviews_evals --task stream --repeat 3` (v5). AC18 asks for v5 to be no
  worse than v4.
- The time to first token in a live interview through `POST /messages/stream`, read from the `stream_turn_summary` log
  lines (`first_event_ms`, `first_token_ms`). The numbers above come from the eval runner calling the same `stream()`.
  First migrate `.env` to `LLM_PROVIDERS` and `LLM_GOOGLE_*`.
- How Google's endpoint reports an error mid-stream (an error chunk or a dropped connection) was not observed. Both
  paths are handled and unit-tested.
