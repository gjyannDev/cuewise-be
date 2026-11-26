# Learn: one retry policy on tenacity, and why reply retries stay out of it (U2)

**Concepts:** transport retries vs. content retries, full jitter, Retry-After, retry budgets across layers, retrying a stream only before its first chunk, per-call state on a shared object. **Status:** built, unit-tested, eval-checked and fault-checked on 2026-11-26.

## 1. Why it exists
Before U2, the AI call layer retried failed network calls with hand-written code in four places:
- `openai_compatible.py`: `complete` (sync) and `stream` (async), two near-identical loops.
- `google_embedder.py`: a third copy of the loop, with a hard-coded `MAX_RETRIES = 1`.
- `deepgram.py`: through `run_with_retries` in `retry.py`.

The same rules (what to retry, how long to wait, when to give up) lived in several places. And the logs never said when a retry happened, or why a call stopped retrying.

Separately, the four interview reply loops (decide, write, write stream, feedback turn) each repeated the same attempt header: count to 2, work out the time left, skip a retry under 5 s.

## 2. What it is
Two retry layers, each in one place, kept apart on purpose:

    service ─► reply loop (ReplyAttempts: content retries, max 2, time-bounded)
                  └─► adapter.complete / stream / embed / transcribe
                         └─► RetryPolicy (transport retries on tenacity: max_retries + 1, full jitter, budget stop)
                                └─► one HTTP call

- **Transport retry**: the call never got an answer (a timeout, a 429, a 5xx). Wait and ask again.
- **Content retry**: the model answered, but the reply was malformed or empty. Ask again at once; there's no server to back off from.

The two multiply. One LLM task makes at most `(llm_max_retries + 1) x MAX_REPLY_ATTEMPTS` HTTP calls, 3 x 2 = 6 with today's defaults. A test pins that number.

## 3. When to use it
| Do this | When | Why / limit |
|---|---|---|
| Build a `RetryPolicy` in the adapter's constructor | A new vendor adapter in `core/ai` | One place for the rules; pass the adapter's own clock and sleep so tests control time |
| `policy.call(attempt, budget=...)` / `await policy.acall(...)` | Sync callers / async callers | `attempt` gets the remaining budget, so each HTTP timeout is `min(timeout, remaining)` |
| `ReplyAttempts(time_left)` | A loop that re-asks the model after a bad reply | Content retries only; it never sleeps and never sees HTTP errors |
| Read `retry_wait` / `retry_giveup` in `logs/app.log` | "Why was this turn slow / why did it fail?" | Joined to `llm_call` by `request_id`; no payload, ever |

**I'd revisit this when** U3 moves LLM transport retries to LangChain's `.with_retry()`. The rules here are the spec it has to match. Tenacity stays for Deepgram.

## 4. How it works
| Option | Verdict |
|---|---|
| One `RetryPolicy` class per vendor; the stream retries only "open + first chunk" | **Chosen**: rules, logging and stamping in one class; adapters shrink to "build the request, parse the response" |
| `@retry` decorators on each method | Rejected: the injected clock and sleep, the stamping and the stream don't fit a decorator |
| `async for attempt in AsyncRetrying` around the whole stream | Rejected: tenacity's attempt block catches exceptions, including cancellation, inside an async generator |
| Reply loops on tenacity too | Rejected: content retries have no backoff, no Retry-After and no HTTP errors; mixing them blurs the two layers |
| Tenacity's built-in `stop_before_delay` for the budget | Rejected after the spike: it reads tenacity's own clock, which tests can only fake by patching a private attribute. A five-line stop on the adapter's clock replaces it (user decision) |

**One failing `complete`, walked through the code:**
1. The adapter's constructor built its policy once: `RetryPolicy(max_retries=..., task="chat", logger=get_logger("app.llm"), clock=..., sleep=...)` (`app/core/ai/openai_compatible.py:53`).
2. `complete` calls `self._retry.call(lambda remaining: self._attempt(body, remaining=remaining), budget=...)` (`app/core/ai/openai_compatible.py:89`).
3. `call` builds a fresh `_Call` (start time, attempt count) and a fresh tenacity `Retrying` for this call only (`app/core/ai/retry.py:102`). One adapter serves concurrent requests and worker threads, so nothing per-call lives on the policy.
4. The attempt raises `LLMServerError` (a 503). `once` stamps `attempts` and `latency_ms` on it, then re-raises.
5. Tenacity asks `retry_if_exception(_transient)` (`:181`): yes, `retryable` is true.
6. Tenacity runs the **wait before the stop**. `_wait` (`:186`) draws full jitter (`_jitter`, `:36`: random from 0 up to 0.5 s, then 1 s, ...) and raises it to `Retry-After` if the vendor sent one.
7. Then the stop: `stop_after_attempt(max_retries + 1) | _OutOfTime(state)` (`:67`, a small `stop_base` subclass), which checks `elapsed + coming wait >= budget` on the adapter's clock. Because the wait is already known, a wait that doesn't fit stops the call without sleeping.
8. Otherwise `_log_wait` (`:153`) logs `retry_wait`, tenacity sleeps with the injected `sleep`, and attempt 2 starts with what is left of the budget.
9. On the final failure, `call` catches the `LLMError`, `log_giveup` (`:162`) works out the reason (`not_retryable`, `max_attempts` or `deadline`) and logs `retry_giveup`, and the stamped error is raised to the reply loop.
10. The reply loop (`app/modules/interviews/ai/interviews_decide.py:50`) catches the `LLMError` and stops: no content retry on a transport failure.

**The stream** (`app/core/ai/openai_compatible.py:119`): the retried step is `open_stream`, which opens the request and reads the first chunk. After the first chunk, a failure is stamped `after_output=True`, logged as a `not_retryable` give-up and raised (`:134`). It's never retried: the caller may already have shown the text, so a retry would duplicate it. A `finally` closes the inner generator (`:137`), also when the caller stops reading early.

**The reply header** (`app/modules/interviews/ai/interviews_reply_attempts.py:17`): iterating `ReplyAttempts` yields `(attempt, seconds_left)`. It stops after 2 attempts, at zero time, or (after the first) under 5 s. `stopped_at` tells the feedback turn which outcome to record (`no_time` or `retry_skipped:no_time`, `interviews_feedback_turn.py:332`).

## 5. What can go wrong
| Failure | What the user sees | What the code does | Proof (test name) |
|---|---|---|---|
| A 429 with `Retry-After: 10` | A slower turn | Waits 10 s, never less | `test_the_retry_waits_at_least_as_long_as_the_vendor_asked` |
| `Retry-After` longer than the budget | The fallback question, at once | Gives up without sleeping, reason `deadline` | `test_no_attempt_starts_once_the_asked_wait_would_pass_the_budget` |
| A 401 or a malformed 200 | The fallback | One attempt, reason `not_retryable` | `test_a_non_retryable_failure_is_raised_at_once_with_attempts_and_latency` |
| A bug (`ValueError`) inside an attempt | A 500 | Propagates unchanged, not retried, not stamped | `test_an_exception_that_is_not_an_llm_error_propagates_unchanged` |
| A stream drops after the first chunk | The draft is taken back (Reset) | Raised with `after_output=True`, never retried | `test_a_failure_after_output_waits_for_nothing_and_logs_a_not_retryable_give_up` |
| The client disconnects during a wait | Nothing | Cancellation propagates, no give-up event | `test_a_cancelled_wait_stops_at_once_without_a_give_up_event` |
| Two requests retry on one adapter at once | Nothing | Each keeps its own attempts and waits | `test_two_concurrent_calls_on_one_policy_keep_their_own_attempts` |
| Both layers fully used | A slow turn | Never more than 6 HTTP calls per LLM task | `test_both_layers_fully_used_never_exceed_the_worst_case` |
| The retry events change the report | Wrong report numbers | They don't; the golden test guards it | `test_retry_events_in_the_log_leave_the_report_unchanged` |
| Full jitter draws a near-zero wait after a 429 with no `Retry-After` | Nothing visible | Retries almost at once; `max_retries` bounds the extra calls | known trade-off, `test_each_wait_is_a_random_value_up_to_its_doubling_cap` |

## 6. Try it yourself
1. **Predict:** with `max_retries=2` and three 503s in a row, how many `retry_wait` lines and how many `retry_giveup` lines are written, and with which reason? Check with `uv run pytest tests/core/ai/test_retry.py -q -k give_up`.
2. **Predict:** set `LLM_MAX_RETRIES=3` and run `uv run pytest tests/core/ai/test_retry_budget.py -q`. Which assertion fails, and why is that the point of the test?
3. **Predict:** in `test_a_failure_after_output_...`, what changes if `stream` retried the whole generator instead of only the open step? (Hint: what would the caller see twice?)
4. Read the retry events of a real interview: `uv run python -c "import json; [print(l['event'], l.get('reason') or l.get('wait_seconds')) for l in map(json.loads, open('logs/app.log', encoding='utf-8')) if l['event'].startswith('retry_')]"`.

## 7. What surprised me
- **The spike settled the design** (tenacity 9.2.1, Python 3.14.7, 2026-11-26, a throwaway script):
  - Tenacity runs `wait` before `stop`, so a stop sees the coming wait, including one raised to `Retry-After`. A 50 s `Retry-After` with a 10 s budget stopped after 1 call, no sleep.
  - The built-in `stop_before_delay` reads only `tenacity.time.monotonic()`. Faking it means replacing a private module attribute in every adapter test file. The five-line stop on the adapter's clock avoided that.
  - `CancelledError` and a non-matching `ValueError` are re-raised at once with `reraise=True`.
- **Full jitter broke five existing tests that weren't about the wait.** They checked "the budget stops retries after N attempts" and quietly relied on the old 0.5 s minimum wait. With waits from 0 up to the cap, how many fit a budget changes run to run. They now send a fixed `Retry-After`, so the same assertion holds every run.
- **A failed stream open leaves nothing open.** The exception already finishes the generator. The real leak was a caller that stops reading after the first chunk; `stream` now closes the inner generator in a `finally`.
- **No reply loop needed its own rule.** Write and write-stream never checked "no time" on their first attempt; the shared header does, and no existing test depended on the old behaviour.
- **Suite:** 2548 passed, 7 skipped (`uv run pytest -q`, 2026-11-26), one known Windows flake passing on re-run.
- **Evals vs. baseline** (2026-11-26, user's runs): no change on write, stream, decide or feedback; see `docs/evals/u2-tenacity-vs-baseline.md`. An extra set of runs Claude started by mistake hit the provider's free-tier rate limit (`LLMRateLimitError` on 1 to 3 items per run); the user's runs minutes later had none.
- **Fault check** (2026-11-26, one live interview, `LLM_TIMEOUT_SECONDS=0.05`): 12 retry events over 2 answer turns. Every timeout got a `retry_wait` inside its cap (first waits 0.047-0.474 s, cap 0.5; second 0.092-0.832 s, cap 1.0), every call gave up after 3 attempts (`reason: max_attempts`), decide did not re-ask after the transport error, the turn fell back to a bank question, and `interview_report --last 1` printed normally.
- **A 1 s timeout never fired.** httpx's timeout applies to each network step (connect, each read), not to the whole call: a 1.1 s call whose steps each take under 1 s never times out. It took 0.05 s to force the fault.
- **The fault check showed the retry events saying `task: "chat"`**, the adapter's label, not the interview task. Fixed after review (R2): `complete` and `stream` now pass the caller's `trace_labels["task"]` to the policy, and `TracingProvider` had been dropping `trace_labels` before the adapter, so it now passes them on. The embedder and Deepgram keep their own labels (`embed`, `transcribe`, `synthesize`).

### Eval log
| Date | What changed | Versions | Summary | Failures | Decision |
|---|---|---|---|---|---|
| 2026-11-26 | U2 retry layers (no prompt or model change) | interviewer_v4, interviewer_v5, follow_up_decision_v1, feedback_score_v2; gemini-3.5-flash-lite | write 1.00/1.00, stream 1.00/1.00, decide 0.80/0.80, feedback 0.90/1.00; all inside the baseline margins | feedback r1: 1 case failed (model noise, the baseline had the same) | no change; `baselines.md` kept |

Full comparison, with the Langfuse run names: `docs/evals/u2-tenacity-vs-baseline.md`.

## 8. Check your understanding
1. Why must a stream never retry after its first chunk, when `complete` may retry freely?
2. Why does the policy build a new tenacity object on every call instead of keeping one?
3. A 503 comes back with `Retry-After: 0`. How long does the policy wait?
4. Why doesn't a transport failure inside `decide` trigger a content retry?
5. With `LLM_MAX_RETRIES=2` and `MAX_REPLY_ATTEMPTS=2`, what is the worst case, and what would a third layer of 3 attempts make it?

<details>
<summary>Reference answers (write yours first)</summary>

1. The caller may already have shown the chunk to the candidate. A retry would send the text again, duplicated or different. `complete` returns nothing until it has the whole reply, so a retry is invisible.
2. One adapter, so one policy, serves concurrent requests, and `complete` runs in worker threads. Tenacity keeps the attempt number and statistics on its object, so a shared one would mix two calls' counts.
3. A random value from 0 up to 0.5 s. `Retry-After` is a minimum, never a shortening, and 0 is below any backoff.
4. The transport layer already retried it as far as the budget allowed. Asking again would only multiply the calls on the same outage: `decide` catches the `LLMError` and stops.
5. (2 + 1) x 2 = 6 HTTP calls. A third layer of 3 attempts makes it 18. That is why the budget test pins 6.

</details>

## 9. Go deeper / Still open
- Spec: `docs/features/u2-tenacity/spec.md`; plan: `docs/features/u2-tenacity/plan.md`; progress: `docs/features/u2-tenacity/task.md`.
- Next slice that uses this: U3 (LangChain) moves LLM transport retries to `.with_retry()`; `RetryPolicy` stays for Deepgram and the embedder.
- Still open:
  - Eval runs compared with the baseline: done, no change (`docs/evals/u2-tenacity-vs-baseline.md`).
  - Fault check: done, passed (section 7).
  - A retries section in `interview_report` (retries per call, give-up reasons): a later slice; the event names are stable for it.
