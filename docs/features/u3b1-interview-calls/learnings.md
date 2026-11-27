# Learn: the interview calls on LangChain (U3b1)

Status: built and evaluated (2026-11-27). All four interview calls (write, decide, write-stream, feedback) run on
the LangChain chat model; the app no longer builds or wires the hand-built `LLMProvider` (its classes stay in
`app/core/ai/` until U3c deletes them). Review (`/review-feature`) pending.

## 1. Why it exists
U3a moved the job-description summary and profile extraction onto the LangChain call layer. U3b1 moves the interview's
own calls (write, decide, write-stream, feedback) so U3c can delete the hand-built `LLMProvider` layer. Each task moved
in its own stage, and a user-run eval against a fresh baseline proved it before the next stage started.

## 2. What it is
- **The test fakes.** `FakeChatModel` streams (`app/core/ai/chat_fake.py`): `fake_chunks(...)` scripts a stream,
  including an error before the first chunk or after some text; `chunk_delay` makes it slow. The contract test
  (`tests/core/ai/test_chat_contract.py`) runs the same stream cases against the real Gemini integration (its async
  client scripted), so the fake can't drift.
- **The `llm` test fixture** (`tests/modules/interviews/conftest.py`) gives the app one chat model, `llm.chat`, which
  routes each call by its system prompt to scripted `FakeProvider`s (`tests/provider_chat.py::ProviderChatModel`). So
  the old test style survives: `llm.script(...)`, `script_decide`, `script_score`, `script_write`, and
  `llm.<name>.calls`, `.budgets`, `.cancelled`, `on_call`. During the stages it was dual-backed (the app also got the
  old provider); step 19 removed that half.
- **`--blocking` on the generation eval** runs the arms on the JSON writer (v4, v7_json, v8_json), the prompts the
  blocking answer route sends; it gave those prompts their first baseline.
- **Stage 1 (write):** `write()` (`app/modules/interviews/ai/interviews_write.py`) sends the same built messages
  through `complete_chat(model, fixed_prompt(built.messages), {}, ...)`, the U3a summary's shape.
- **Stage 2 (decide):** `decide()` (`interviews_decide.py`) sends the built messages through
  `complete_structured(..., ModelDecision, ...)` (`interviews_decide.py:65`). `ModelDecision`
  (`interviews_model_schemas.py:14`) has every field required, `gap` and `note` nullable.
  `parse_decision_reply(result.text)` still runs as the second check (`interviews_decide.py:83`), so the gap and note
  rules stay in one place.
- **Stage 3 (write-stream):** `stream_chat` (`app/core/ai/chat_stream.py:34`) is the async helper:
  `(prompt | model).astream(...)` under `RetryPolicy.acall`, at most `LLM_TIMEOUT_SECONDS` for the first chunk, the
  time left in the turn as the vendor's own timeout, then text chunks and the merged `LLMResult`. `stream_draft` /
  `stream_write` (`interviews_write_stream.py`) call it; the Delta / Reset / Written events are unchanged.
- **Stage 4 (feedback):** `FeedbackGenerator` (`interviews_feedback_turn.py`) takes the chat model. The score call
  sends `ModelScore` (`interviews_model_schemas.py:41`: questions, a criterion -> score map, evidence; every field
  required) through `complete_structured`; the write call is `complete_chat`. `parse_score_reply` /
  `parse_write_reply` still check what a schema can't: quotes found in the answers, the right criteria per thread,
  the caps.
- **Step 19 (wiring):** `Interviewer`, `InterviewsService`, `AnswerService` and `FeedbackService` take only the chat
  model; `get_llm_provider`, `app.state.llm_provider` and the provider's build and close in `app/main.py` are gone; the
  eval runner builds only the chat model, and its `--reasoning-effort` flag is removed (the chat model's thinking
  setting comes from the config).

### The order of the checks (stages 2 and 4)
The parser runs first, then the schema check. With the schema check first, a reply that wasn't JSON at all was logged
as a generic `invalid_reply:schema`, hiding the precise `not_json` and its hint. A reply the parser accepts but the
schema doesn't still counts as invalid (FR6, FR8).

### Why structured output plus the old parser (stages 2 and 4)
- **What structured output is:** instead of asking for JSON in the prompt and hoping, the request carries a JSON
  schema and Gemini's decoder is constrained to it. So the reply always has the fields, with legal enum values.
- **Why the parser still runs:** a JSON schema can't say "gap is required only when action is follow_up" or "this
  quote must appear in that thread's answers", and the length and markup rules live in the parsers. The schema
  removes format failures; the parser keeps the business rules.
- **Why every field is required:** the U3a profile lesson. A field with a default is optional in the schema, and the
  model may leave it out.
- **Why not `strict=True`** (as `ModelProfile` has): LangChain's parser validates a Python dict, and strict pydantic
  rejects a plain `"follow_up"` string for an enum field in that mode (checked: python mode rejects, JSON mode
  accepts).
- **Why `ModelScore`'s top level ignores extra keys:** `_RawScoreReply` already ignores a stated `overall` (the code
  computes it), so the schema shouldn't turn that into a failure. The nested models still forbid extras.

### When a client leaves mid-stream (stage 3)
- Closing `stream_chat` closes LangChain's stream, but LangChain's `astream` doesn't close the model's own stream
  inside it. Python then lets go of that inner generator, and asyncio's async-generator finalizer closes it a few
  event-loop turns later (about 15 with the Gemini integration). So the vendor stream does stop, just not in the same
  instant: the old hand-built provider closed its HTTP stream at once.
- Tests that check a client leaving wait for it, bounded (`tests/provider_chat.py::closed_soon`), and
  `test_chat_stream.py::test_closing_early_closes_the_gemini_stream_too` pins it on the Gemini integration.
- A bug the new tests caught: the `finally` that marks an early-closed stream `cancelled` also ran after a stream
  that finished, before `succeed`, so every finished stream's generation was recorded as cancelled. Fixed by marking
  only a stream that wasn't read to the end (`chat_stream.py:96`).

## 3. When to use it
- `complete_chat` for a plain-text call, `complete_structured` with a required-fields `Model*` schema for a JSON
  reply (then the feature's parser as the second check), `stream_chat` for text a user sees while it is written.
- `fake_chunks` for any test of a streamed call; `FakeChatModel(..., chunk_delay=...)` for timing.
- `ProviderChatModel` only for tests that still script `FakeProvider`s; new tests use `FakeChatModel` directly.
- `--blocking` to compare the JSON writers' question quality after a change to the blocking write.

## 4. How it works
### One streamed answer turn, through the code
1. `Interviewer.stream_turn` (`interviews_turn.py:86`) runs decide in a worker thread, then starts
   `stream_write(self.chat_model, ...)` (`interviews_turn.py:105`).
2. `stream_write` (`interviews_write_stream.py:34`) loops over `ReplyAttempts`; each attempt is one `stream_draft`
   (`interviews_write_stream.py:141`), which calls `stream_chat` with the turn's remaining time as `budget_seconds`
   (`interviews_write_stream.py:156`).
3. `stream_chat` (`chat_stream.py:34`) retries `open_stream` (`chat_stream.py:59`) through `policy.acall`
   (`chat_stream.py:79`): each try copies the model with `timeout=<time left>`, starts `astream`, and waits for the
   first chunk under `anyio.fail_after(min(LLM_TIMEOUT_SECONDS, time left))` (`chat_stream.py:70`).
4. After the first chunk it yields text as it arrives and merges chunks for usage and finish reason. A failure now is
   mapped by `to_llm_error`, flagged `after_output` when text was yielded (`chat_stream.py:100`), and never retried.
5. Back in `stream_write`: a failure after text sends `Reset` and retries the draft (`interviews_write_stream.py:81`);
   a CATEGORY line that is missing or broken is an invalid reply before any text was shown.

### Spike results (step 1, `tests/live/test_chat_stream_live.py`, 2026-11-27, configured Gemini model, 3 passed)
Run by the user (PowerShell): `$env:LLM_LIVE_TEST = "1"; uv run pytest tests/live/test_chat_stream_live.py -q -s`.
- **Usage adds up.** Per-chunk usage arrives as differences (first chunk input 22 / output 2, then input 0 and
  output 19, 10, 0). Merged: input 22, output 31. A blocking call of the same prompt: input 22, output 29 (a different
  reply, so only the input side must match, and it does).
- **Finish reason is not on the last chunk.** The merged message says `STOP`, but the very last chunk is LangChain's
  empty closing chunk (metadata `{}`, usage None). Read the finish reason and usage from the merged chunks.
- **First chunk** after 808 ms on this short prompt.
- **Failure before the first chunk:** a 0.001 s timeout raises `google.api_core.exceptions.DeadlineExceeded` with no
  chunks; `to_llm_error` maps it to `LLMTimeoutError`.
- **The timeout is one deadline for the whole stream.** With `timeout=3` a long reply was cut at 3.0 s after 29
  chunks (3,280 characters), with `DeadlineExceeded`. So a plain `timeout=LLM_TIMEOUT_SECONDS` would cut long
  questions (EC7).

### Decision: write-stream can be built (step 11, FR1)
FR1's conditions, checked against the spike:
- **Usage and finish reason at the end:** kept, from the merged chunks.
- **A failure after the first chunk can be told apart:** kept. The helper knows whether it has yielded text, so it
  sets `after_output` itself; retries happen only before the first chunk.
- **No whole-stream cap below the turn deadline:** kept, by giving the vendor the time left in the turn and
  enforcing `LLM_TIMEOUT_SECONDS` in the helper, on the first chunk only.
- **A real timeout:** arrives as `DeadlineExceeded` and maps to `LLMTimeoutError`.

### What the scripted contract test showed (no network)
- The bundled integration turns Gemini's cumulative stream usage into per-chunk differences: two chunks scripted
  with cumulative (7, 1) then (7, 3) merge to (7, 3).
- Merging chunks joins string metadata: a `finish_reason` on every chunk merges to `"STOPSTOP"`. Gemini sends it on
  the last chunk only, so the fake does the same (and puts `model_name` on the last chunk only, for the same reason).
- `astream` ends with an empty extra chunk (LangChain marks the last position), so callers filter empty text.

## 5. What can go wrong
- **Transient errors are retried by the call layer, not by the reply loops.** A loop only retries a reply that broke
  the contract. A 503 or a timeout is retried inside the helper (`RetryPolicy`, `LLM_MAX_RETRIES`), as the old
  provider did inside itself (`test_write.py::test_a_transport_error_is_retried_by_the_call_layer_only`, the same in
  `test_decide.py` and `test_feedback_turn.py`).
- **An empty reply is `LLMBadResponseError`, never retried.** Every task logs it as `outcome=empty_reply` with the
  finish reason (`interviews_turn_log.py::log_llm_error`; `test_write.py::test_an_empty_reply_is_not_retried`,
  `test_feedback_turn.py::test_an_empty_reply_keeps_its_failure_code`).
- **Each blocking attempt's timeout is capped** at `LLM_TIMEOUT_SECONDS`
  (`test_start_llm.py::test_the_retry_only_gets_the_time_that_is_left`).
- **A stream gets two limits:** the first chunk within `LLM_TIMEOUT_SECONDS`
  (`test_chat_stream.py::test_the_first_chunk_must_come_within_its_limit`), then it may run past it
  (`test_a_stream_may_run_past_the_first_chunk_limit`); the vendor's timeout is the time left in the turn
  (`test_the_vendor_timeout_is_the_time_left_in_the_turn`).
- **A failure after text is never retried by the helper** and is flagged `after_output`
  (`test_chat_stream.py::test_a_failure_after_text_is_never_retried_and_flagged`); the write loop takes the draft back
  with `Reset` (`test_stream_turn.py`).
- **A schema-valid reply can still break a rule:** follow_up without a gap, or a quote the candidate never said; it
  counts as invalid (`test_decide.py::test_a_schema_valid_reply_the_parser_rejects_is_retried`,
  `test_feedback_turn.py::test_a_schema_valid_reply_with_a_made_up_quote_is_rejected_by_the_parser`).
- **The worst case is still 6 calls** per decide: (LLM_MAX_RETRIES + 1) transport attempts x 2 reply attempts
  (`tests/core/ai/test_retry_budget.py`, now on the fake chat model).
- **Profile-carrying writes stay redacted** in Langfuse on the new path, blocking and streamed
  (`test_profile_redaction.py`).
- **A client that leaves** stops the vendor stream a few loop turns later, not at once (section 2).

## 6. Try it yourself
1. In `test_chat_stream.py`, change `first_chunk_seconds=0.2` in
   `test_a_stream_may_run_past_the_first_chunk_limit` to `0.02`. Prediction: the first chunk (50 ms) now misses the
   limit, every attempt times out, and the stream ends in `LLMTimeoutError` with no text.
2. In `interviews_model_schemas.py`, give `ModelDecision.note` a default (`note: str | None = None`) and run
   `test_decide.py::test_the_schema_requires_every_field`. Prediction: it fails, because `note` drops out of
   `required`: exactly the U3a profile bug, caught before any eval.
3. In `interviews_decide.py`, swap the parser and schema checks back (schema first) and run
   `test_decide.py`. Prediction: the tests still pass (both give `schema` for `{"action": "dance"}`), but in
   `test_feedback_endpoint.py::test_no_retry_when_the_budget_is_nearly_spent` the same swap in feedback turns
   `invalid_reply:not_json` into `invalid_reply:schema`.
4. Remove the `read_all` guard in `chat_stream.py` (always call `trace.cancel`). Prediction:
   `test_one_generation_per_call_with_its_labels_and_usage` fails: the finished stream's generation is "cancelled".

## 7. What surprised me
- **Decide got better.** With the schema, decide accuracy rose from 0.800 / 0.867 to 0.933 three times running, all
  of it fewer unneeded follow-ups. The prompt didn't change; only the reply format became enforced.
- **Streaming got faster.** Time to the first token fell by 300-600 ms (793 / 776 / 734 ms vs 1,089 / 1,386 ms); the
  native Gemini client streams sooner than the OpenAI-compatible endpoint did. The blocking write didn't speed up.
- **LangChain doesn't close the vendor stream** when its caller stops; asyncio's finalizer does, a little later.
- **Every `--repeat 3` run until the stream run lost its third repeat** in Langfuse (write, generation, decide);
  the stream and feedback runs had all three. The cause wasn't found.

### Eval log
| Date | Run | What changed | Result | Decision |
|------|-----|--------------|--------|----------|
| 2026-11-27 | generation `--blocking` C,D, `20261127-130930` (2 repeats) + `20261127-132414` (the third) | baseline on the old layer (v7_json, v8_json) | C skill coverage 0.800 / 0.717 / 0.700, valid 1.00 / 1.00 / 0.971; D 0.667 / 0.592 / 0.425, valid 0.971 / 1.00 / 0.952 (2 errored items in all) | recorded in `docs/evals/baselines.md`; judge with the streamed arms' margins (0.233 / 0.275) |
| 2026-11-27 | write `20261127-140210`, generation A,C,D `20261127-143009`, `--blocking` C,D `20261127-145438` (2 repeats each reached Langfuse) | stage 1: write on LangChain | write 1.00 / 1.00; skill coverage A 0.85 / 0.75, C 0.75 / 0.68, D 0.63 / 0.58, blocking C 0.79 / 0.69, blocking D 0.50 / 0.54; 1 errored setup in 5 of the 10 arm runs (cause not recorded, likely the free-tier limit) | no change ([comparison](../../evals/u3b1-write-vs-baseline.md)); next stage: decide |
| 2026-11-27 | decide `20261127-153726` (2 of 3 repeats reached Langfuse) | stage 2: decide on LangChain with `ModelDecision` | accuracy 0.933 / 0.933 (baseline 0.800 / 0.867); over-probing 0 / 0 (baseline 2 / 1); 0 errored | better by 1-2 cases ([comparison](../../evals/u3b1-decide-vs-baseline.md)); one more repeat before it becomes the baseline row |
| 2026-11-27 | decide `20261127-155824` (`--repeat 1`, confirm) | nothing (confirming repeat) | accuracy 0.933, over-probing 0, under-probing 0, 0 errored | gain confirmed; recorded as the new "decide (current)" row in `baselines.md` |
| 2026-11-27 | stream `20261127-163159` (all 3 repeats) | stage 3: write-stream on `stream_chat` | pass rate 1.00 x 3; first token 793 / 776 / 734 ms (baseline 1,089 / 1,386); latency 857 / 849 / 805 ms; 0 errored | no change in quality, faster ([comparison](../../evals/u3b1-stream-vs-baseline.md)); "stream (current latency)" row added |
| 2026-11-27 | feedback `20261127-171608` (all 3 repeats) | stage 4: feedback on LangChain (`ModelScore`) | pass rate 0.90 / 1.00 / 0.90 (baseline 0.90 / 1.00); in band 1.00 / 1.00 / 0.889; valid 1.00 x 3; 0 quotes rejected; 0 template texts; generations nested under `score` / `write` | no change ([comparison](../../evals/u3b1-feedback-vs-baseline.md)) |

Step 19 (removing the provider wiring) changed no LLM call, so it has no eval run: the four comparisons above stand.

## 8. Check your understanding
1. Why does `stream_chat` not pass `LLM_TIMEOUT_SECONDS` to the vendor as its timeout?
2. A decide reply is `{"action": "follow_up", "gap": null, "note": "x"}`. Does the schema accept it? Does `decide`?
3. Why does the parser run before the schema check?
4. A 503 arrives before the first chunk of a streamed question; another arrives after three chunks. What happens to
   each?
5. Why does `ModelScore` ignore extra top-level keys when `ModelDecision` forbids them?

<details>
<summary>Answers</summary>

1. The Gemini SDK treats the model's `timeout` as one deadline for the whole stream (spike: cut at 3.0 s after 29
   chunks), so 15 s would cut a long question. The vendor gets the time left in the turn; the helper enforces
   `LLM_TIMEOUT_SECONDS` on the first chunk only.
2. The schema accepts it (`gap` is nullable). `decide` doesn't: `parse_decision_reply` raises `missing_gap`, so it is
   an invalid reply and the loop tries once more.
3. For the reason code: the parser says why (`not_json`, `quote_not_found`, ...), and the stored failure and its hint
   depend on that. A reply the parser accepts and the schema rejects still fails, as `schema`.
4. Before the first chunk: `RetryPolicy.acall` retries it within the budget (up to `LLM_MAX_RETRIES`), and nothing was
   shown. After three chunks: the helper raises it with `after_output` set, never retries; `stream_write` sends `Reset`
   and retries the whole draft if time is left.
5. They mirror their parsers: `_RawScoreReply` ignores a stated `overall` (the code computes it), `_RawDecision`
   forbids extras. Refusing what the parser tolerates would turn a harmless key into a failed feedback.
</details>

## 9. Still open
- U3c deletes the old classes (`LLMProvider`, `OpenAICompatibleProvider`, `TracingProvider`, `FakeProvider`,
  `json_reply.py`) and the test bridge that still scripts `FakeProvider`s (`tests/provider_chat.py`); new tests should
  use `FakeChatModel` directly.
- The vendor stream closes a few loop turns after a client leaves, not at once (LangChain doesn't close it). Fine
  today; revisit if Langfuse ever shows streams running on after a cancel.
- Some `--repeat 3` runs lost their third repeat in Langfuse; cause unknown.
- Pre-existing pyright errors outside this work (`interviews_feedback.py:266`, `interviews_report.py`,
  `profile_schema.py`) and the known flaky docx test (`test_profile_read_resume.py`) are untouched.
