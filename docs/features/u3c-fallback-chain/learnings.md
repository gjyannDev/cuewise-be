# Learn: a provider fallback chain (U3c, built; real-model runs pending)

**Concepts:** provider fallback chain, which errors may switch provider, one turn deadline across providers, why not `.with_fallbacks()`, removing a silent fallback (the question bank), an honest retryable error. **Status:** built, tested with fakes and measured on the real model (2026-11-28): no change in quality.

## 1. Why it exists
`LLM_PROVIDERS` listed providers in order, but only the first was ever built, so one provider outage was a total outage. The question bank also hid LLM failures: a failed turn quietly became a canned question and the metrics never showed it. U3c makes the list a real chain and (steps 4-5, **pending**) turns "the LLM could not write" into one honest, retryable 503.

## 2. What it is
A `ChatChain` is an ordered list of `(provider name, chat model)` pairs. The call helpers try the first model; if it fails with a *transport* error (timeout, 429, 5xx) they try the next one inside the same turn deadline.

```
LLM_PROVIDERS=google,other  ->  ChatChain((("google", model_a), ("other", model_b)))
call -> model_a: timeout -> model_b: answers  (result.provider == "other", one llm_provider_switch log line)
```

## 3. When to use it
| Do this | When | Why / limit |
|---|---|---|
| Switch to the next provider | timeout, rate limit, 5xx | the call never got an answer; another vendor may |
| Raise at once | rejected request (bad key, bad request) | a misconfigured primary must not be hidden by a working second |
| Stay in the content loop (no switch) | invalid or rule-breaking reply | the model answered; another vendor is not the fix |
| Never switch mid-stream | after the first chunk | the candidate may already have read the text |

**I'd revisit this when** a second real vendor exists: then compare score and cost per provider (out of scope here), and consider circuit breaking so a dead primary does not cost its timeout on every call.

## 4. How it works
| Approach | Result |
|---|---|
| A. Explicit loop in our helpers (chosen) | keeps the per-attempt rules: the time left as timeout, token cap, error mapping, one Langfuse generation, `RetryPolicy` backoff |
| B. `model.with_fallbacks([...])` | runs each branch with none of those rules (no per-attempt copy with the time left, no our retry policy) |
| C. `.with_fallbacks()` over lazy wrapper runnables | the wrappers would have to redo timeout, mapping and stream opening, hiding what `.with_fallbacks()` does |

(The `.with_fallbacks()` verdict comes from reading the helpers' responsibilities, not from a measurement; the spec's assumption about its first-chunk behavior on the real Gemini model was not tested because the approach was not used.)

One blocking call, through `complete_chat`:
1. `chat.py:191` `attempt(remaining)` loops over the chain members; each gets `left = remaining - elapsed`; no time left ends the loop (`chat.py:196`).
2. `chat.py:173` `invoke` copies the member with `timeout=min(per_call_timeout, left)` and runs it; vendor errors are mapped by `to_llm_error`.
3. A retryable `LLMError` records itself and moves on (a `llm_provider_switch` line names both providers and the error class, never text, `chat_chain.py:38`); a non-retryable one raises.
4. If every provider failed, the last error raises and `RetryPolicy` backs off and runs the whole chain again, so the worst case is (retries + 1) x reply attempts x providers (12 calls with two providers and today's defaults, pinned in `tests/core/ai/test_retry_budget.py`).
5. The winner's name goes into `LLMResult.provider`, the trace metadata and the `llm_call` log line. A stream does the same in `chat_stream.py:78`; the first chunk commits it to its provider (`chat_stream.py:62` `open_member`).

Settings now refuse an empty `LLM_PROVIDERS` (`config.py:189`), so there is no "LLM off" mode: `build_chat_model` (`factory.py:39`) always returns a chain, and the services take a required chat model.

## 5. What can go wrong
| Failure | What the user sees | What the code does | Proof (test name) |
|---|---|---|---|
| Primary times out / 429 / 5xx | nothing, the second answers | switch within the deadline | `test_a_transport_error_hands_the_call_to_the_next_provider` |
| Primary has a bad key | an error | raises, no switch | `test_a_request_error_does_not_switch_so_a_bad_key_is_not_hidden` |
| Invalid reply | the attempt loop retries | no switch | `test_an_invalid_reply_never_switches_provider` |
| Slow primary eats the deadline | the second gets only the time left; none left, no second call | bounded | `test_the_next_provider_gets_only_the_time_left`, `test_no_time_left_starts_no_further_provider` |
| Stream breaks after text | `reset`, then an `error` event with `INTERVIEWER_UNAVAILABLE` | no switch, `after_output` set; the write step takes the draft back and retries once, then the turn fails | `test_a_stream_that_breaks_after_text_resets_then_fails` |
| Every provider down | a 503 `INTERVIEWER_UNAVAILABLE` ("try again"), nothing saved | whole chain retried, last error raised, services map it | `test_a_write_that_fails_ends_the_turn_and_saves_nothing`, `test_a_provider_error_fails_the_start_after_the_call_layer` |
| The decide call fails | the same 503, no write call is made | `fail_undecided` ends the turn first (user choice) | `test_a_failed_decide_also_ends_the_turn_without_a_write` |
| No time left for the write | the same 503 | `settle` raises `InterviewerFailedError` | `test_no_write_call_starts_below_its_minimum_and_the_turn_ends` |
| Empty `LLM_PROVIDERS` | the app refuses to start | `Settings` raises, names `LLM_PROVIDERS` | `test_an_empty_or_blank_provider_list_refuses_to_start` |

## 6. Try it yourself
Prediction first: with two fake providers where the first always returns a 503 and `llm_max_retries=1`, how many calls does each make? (Answer in section 8.) Then run `uv run pytest tests/core/ai/test_chat_chain.py -q` and read `test_when_every_provider_fails_...`.

## 7. What surprised me
- Making `LLM_PROVIDERS` required meant the tests need a dummy Google provider in the environment (`tests/conftest.py`); the same key also turns embeddings "on", but the lifespan never runs in tests, so no embedder is built.
- Many tests passed in "LLM off" mode only because the bank answered. Removing the bank forced a default LLM for the interviews tests that writes a valid question of the interview's own type (`_llm_by_default` in `tests/modules/interviews/conftest.py`).
- Pydantic settings refuse unknown `.env` keys. Dropping `LLM_GOOGLE_BASE_URL` from the code would have broken every run until the line left `.env`, so it is accepted and ignored for now (delete it from `.env`, then the field).
- `json_reply.py` was assumed to be old-layer code; the profile feature uses it too, so it stays in `core/ai`. `FakeProvider` is old-layer code that 22 test files still use; it now lives in `tests/provider_fakes.py` until those tests are ported to `FakeChatModel`.
- Real-model runs (the user, 2026-11-28, `--repeat 2`): every score equals its baseline; latencies are the same or a little lower. The chain was exercised on one provider, so a failing-over call is proven only with fakes.

### Eval log (AI features only)
| # | Run (date, session) | What changed | Versions | Pass | Errors | Task metrics | Tokens in / out | Failures → type | Decision |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-11-28, U3c | chain, bank removal, old layer deleted (one provider configured) | interviewer_v4 / v5, follow_up_decision_v1, feedback_score_v2 + write_v1 | write 1.00 / 1.00; stream 1.00 / 1.00; decide 0.933 / 0.933; feedback 0.90 / 1.00 | 0 | write latency 797 / 840 ms; stream first token 742 / 705 ms; decide over/under-probing 0 / 0; feedback in-band 0.889 / 1.00 | — | one out-of-band feedback case in r1 (quality), same count as the baseline | keep; no baseline row changes (`docs/evals/u3c-chain-vs-baseline.md`) |

## 8. Check your understanding
1. Why does a rejected request (bad key) not switch provider?
2. When is it safe to switch provider during a stream, and when not?
3. How many calls does each provider make in section 6's prediction?
4. What if both providers time out at 15 s and the turn budget is 20 s?

<details>
<summary>Reference answers (write yours first)</summary>

1. A bad key is a configuration fault; switching would hide a broken primary behind a working second one.
2. Only before the first chunk: after it the candidate may have read text, so a switch would show two different questions.
3. 2 each: (1 + `llm_max_retries`) passes over the chain, every pass tries both.
4. The first uses its 15 s; the second gets the 5 s left (`min(15, 5)`); then no time is left and the call fails with a timeout.
</details>

## 9. Go deeper / Still open
- Spec: `docs/features/u3c-fallback-chain/spec.md`; plan: `plan.md`; progress: `task.md`.
- Comparison: `docs/evals/u3c-chain-vs-baseline.md`.
- Still open: the migration run by the user (`uv run alembic upgrade head`, `downgrade -1`, `upgrade head`), deleting `LLM_GOOGLE_BASE_URL` from `.env` and the ignored field in `config.py`, porting the 22 test files off `FakeProvider`, and a second real vendor to answer "provider B scores N/M at X times the cost of A".

## Layer test and the note parser (step 7)
- `tests/test_layers.py` now reports any `app/` file outside `app/core/ai/` and a feature's `ai/` folder that imports `langchain*` or a vendor SDK (`check_sdks`, also run on the real tree), and a `utils/` file that imports `ai/`.
- The second rule found five real imports the plan had not counted: the turn-row helpers in `interviews_session_utils.py` (moved to `ai/interviews_turn_rows.py`), `EmptyProfileError` (moved down to `profile_utils.py`), and the note parser's splitter (now a `split` argument; the ingest tool passes it, tests use `tests/note_parsing.py`). Proof: `test_utils_importing_an_ai_folder_is_reported`, `test_the_real_tree_imports_langchain_and_vendor_sdks_only_in_core_ai_and_feature_ai_folders`.
