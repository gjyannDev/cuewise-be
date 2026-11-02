# Learnings: SSE Streaming of the Interview Turn (Slice 4)

Concept 7 (streaming and latency), with the conflict between streaming and structured output (concept 2) and the
provider abstraction (concept 6). Format per checkpoint: **Predict** (before running), **Observed**, **Why**, and the
concept's **Proof** at the end.

## Checkpoint A: what the candidate waits for

**Predict.** Streaming makes the wait feel shorter mainly through the question text: the first words appear well before
the whole question.

**Observed** (`--task stream --repeat 1`, `gemini-3.5-flash-lite`, 19 cases, 2026-11-02; one live call earlier the same
day showed the same pattern):

| | value |
|---|---|
| valid replies | 19/19 (both injection cases ignored) |
| average time to first question token | 2,001 ms (567 to 4,226 ms) |
| under the 1 s target | 7 of 19 |
| average total latency of the write call | 2,231 ms |
| output per question | about 30 tokens, in 1 to 2 chunks |

**Why.** A question is short. The model spends almost all of its time *before* the first token: queueing, then reading
about 850 to 1,450 input tokens. It then emits the whole question in one or two chunks, so the first token arrives only
about 100 ms before the last. So streaming the question text barely moves the wait for this reply. What does move it:

- **The progress events.** `received` arrives at once (well under 1 s, measured with fakes), and `deciding`/`writing`
  tell the candidate the app is working. Before this slice, the page was silent for the whole decide + write time.
- **Shorter input** (concept 4) and a faster model, because time to first token tracks prefill and queueing, not output length.

Streaming will matter more for long outputs, such as the end-of-interview feedback (Slice 3). A paragraph of feedback is
hundreds of tokens, where generation time dominates.

## Checkpoint B: streaming vs structured output

**Predict.** v4's JSON can't be shown while it streams, so v5's plain text with a `CATEGORY:` first line costs some
validity.

**Observed.** v5 passed 19/19 on one repeat, with no header failures. The v4 baseline for the same cases at 3 repeats is
still open (below).

**Why.** The two output shapes trade risks differently:

| | v4 (JSON) | v5 (header + text) |
|---|---|---|
| shown while streaming | no (half a JSON object) | yes, after the first line |
| parse failure mode | broken JSON | a missing or broken header line |
| what reaches the candidate on failure | nothing (validated first) | a draft, taken back by `reset` |
| category | a field | the first line, never shown |

The real cost of streaming is that **validation happens after display**. A question that turns out to repeat an earlier
one has already been read, so the turn sends `reset` and retries, or falls back to the bank. The header line is read
before any text is sent, so a reply without one shows nothing.

## Checkpoint C: what a dropped stream leaves behind

**Predict.** The hard part is saving a turn that is complete only when the stream ends.

**Observed.** The turn already had one atomic save (`record_turn`, a compare-and-swap on the session position). The
streamed turn calls it once, after the question is final and before `done`. A client that leaves before that point
cancels the stream, and nothing is saved, so the same question is still current. Tests cover leaving during `deciding`,
leaving during `writing` (the provider's stream is closed), two tabs racing (one `done`, one `error
QUESTION_NOT_CURRENT`), and a save that fails (one generic `error`).

**Why.** "Save at the end, all or nothing" needs no half-turn state, no resume protocol and no regenerate endpoint. The
cost is a re-submit after a dropped connection. That is acceptable, because the answer is still in the client's input box.

## Still open

- The 3-repeat comparison on the same cases (pause between runs: the free tier rate-limits at about 25 calls):
  `uv run python -m app.modules.interviews.interviews_evals --task write --repeat 3` (v4) against
  `uv run python -m app.modules.interviews.interviews_evals --task stream --repeat 3` (v5). AC18 asks for v5 to be no
  worse than v4.
- The time to first token in a live interview through `POST /messages/stream`, read from the `stream_turn_summary` log
  lines (`first_event_ms`, `first_token_ms`). The numbers above come from the eval runner calling the same `stream()`.
  First migrate `.env` to `LLM_PROVIDERS` and `LLM_GOOGLE_*`.
- How Google's endpoint reports an error mid-stream (an error chunk or a dropped connection) was not observed. Both
  paths are handled and unit-tested.

## Proof (concept 7)

**Why does streaming need `async`?** A stream keeps the request open for seconds while it waits on the model. With a
blocking call, each waiting stream would hold a worker thread for its whole lifetime, and the threadpool caps how many
candidates can wait at once. With `async`, waiting for the next chunk gives control back to the event loop. One process
then serves other requests in the meantime, which `test_other_requests_are_served_while_a_stream_waits_on_the_llm`
checks. `async` also makes cancellation possible: when the client leaves, the task is cancelled and the
provider's HTTP stream is closed, so no more tokens are generated. The decide call is still the sync `complete()` run in
a worker thread. It can't be cancelled mid-call, so its result is dropped, which is fine for a call of about a second.

**How is a message saved that is only complete when the stream ends?** It isn't saved while it streams. The streamed text
is a preview, and the saved row is built from the final, validated reply. That row is saved in one transaction with the
answer, the reaction and the session's new position, and `done` is only sent after that commit. If the stream stops
before then, nothing was written, so the interview is exactly where it was. A race between two submits is settled by the
compare-and-swap, not by the stream.
