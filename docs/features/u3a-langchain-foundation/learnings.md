# Learn: LangChain as the call layer, one task at a time (U3a)

**Concepts:** Runnables and LCEL (`prompt | model`), `.with_structured_output()`, `.with_retry()` and why it isn't used, callbacks, the strangler pattern. **Status:** built and unit-tested (2026-11-26, 2706 tests passing); the eval comparison is done: `docs/evals/u3a-langchain-vs-baseline.md` (no change after one fix).

## 1. Why it exists
Every LLM call goes through a layer we wrote by hand (`app/core/ai/`: `LLMProvider`, `openai_compatible.py`, `json_reply.py`, `TracingProvider`, `FakeProvider`). Later slices (U4 prompt templates, U6 retrievers, U8 LangGraph, the U3c fallback chain) want LangChain's standard pieces. U3a lays the base and moves the two simplest tasks: the job-description summary and profile extraction. **Pending:** line counts and the latency/token comparison once both tasks run on it.

## 2. What it is
A LangChain chat model (`ChatGoogleGenerativeAI`) built from the same config, called through one helper in `core/ai/` that adds the parts LangChain doesn't give us the way we need them: the time budget, our retry rules, our tracing and our error types. Feature code builds a chain (`prompt | model`, or the model `.with_structured_output(schema)`) and hands it to that helper.

```
service ──> feature ai/ function ──> core/ai call helper ──> RetryPolicy ──> chain.invoke ──> Gemini SDK
                                         │                                       │
                                         └─ to_llm_error, tracing callback  <────┘
```

## 3. When to use it
| Do this | When | Why / limit |
|---|---|---|
| Build the chain in the feature's `ai/` folder | A task moves to LangChain | Services never import LangChain (`tests/test_layers.py`) |
| Let `RetryPolicy` own transport retries | Any LLM call on the new layer | `.with_retry()` can't keep the U2 rules (spike, below) |
| Keep `LLMProvider` | Tasks not migrated yet | Strangler pattern: never both layers inside one task |

**I'd revisit this when** LangChain's `with_retry` gains a wait function or a stop hook (then it could read Retry-After and the deadline), or when the calls go async in U3b.

## 4. How it works

### Spike results (step 1, `tests/core/ai/test_langchain_behaviour.py`)
Versions: `langchain-core` 1.8.5, `langchain-google-genai` 3.2.0 (on `google-ai-generativelanguage` 0.12.1, gRPC transport), Python 3.14.7. Both installed and imported with no errors.

| Question | Finding | Test |
|---|---|---|
| What can `.with_retry()` configure? | Only `retry_if_exception_type`, `wait_exponential_jitter`, `exponential_jitter_params`, `stop_after_attempt`. No Retry-After, no deadline stop, no before-sleep hook. | `test_with_retry_offers_only_exception_type_jitter_and_attempt_count` |
| Does `.with_retry()` retry a stream? | No. `RunnableRetry` doesn't override `stream`, so a stream failing before its first chunk is not retried at all. | `test_with_retry_does_not_retry_a_stream_at_all` |
| `.with_fallbacks()` on a stream (for U3c) | It switches to the fallback when the stream fails **before** its first chunk; **after** the first chunk it raises and never calls the fallback. That is the U2 `after_output` rule for free. | `test_with_fallbacks_switches_…`, `test_with_fallbacks_raises_…` |
| The SDK's own retries | `max_retries` counts **attempts** (`stop_after_attempt(max_retries)`), so `1` means one call. Its predicate retries every `GoogleAPIError`, 4xx included, with a fixed exponential wait of at least 1 s. | `test_the_sdk_max_retries_counts_attempts…`, `test_the_sdk_retries_every_google_api_error…` |
| Per-call timeout | `model.bind(timeout=…)` reaches the SDK request and wins over the model's `timeout`; a bind is cheap (no model copy). | `test_a_per_call_timeout_and_generation_config_reach_the_request_through_bind` |
| Per-call temperature / max tokens | There is no `temperature` kwarg per call, but `bind(generation_config={...})` is merged over the defaults. | same test |
| Thinking settings | `thinking_budget` works. `thinking_level` (the Gemini 3 setting) exists on the LangChain model but not in the bundled SDK's proto, so the request fails to build. | `test_thinking_budget_…`, `test_thinking_level_is_not_supported_by_the_bundled_sdk` |
| Temperature default | For a `gemini-3*` model with none set, the integration uses 1.0, the vendor default, which is what today's summary call gets (it sends none). | `test_a_gemini_3_model_defaults_to_temperature_1…` |
| Usage | `usage_metadata`: `input_tokens`, `output_tokens` (= candidates + thinking), `output_token_details.reasoning`, `input_token_details.cache_read`. | `test_usage_metadata_counts_thinking_tokens_inside_output_tokens` |
| Blocked prompt | No candidates gives an empty `AIMessage`, not an exception (the helper's empty check turns it into `LLMBadResponseError`, as today). | `test_a_response_with_no_candidates_is_an_empty_message_not_an_error` |
| Error classes | `google.api_core.exceptions`, each with `.code` = the HTTP status (429 `ResourceExhausted`, 503 `ServiceUnavailable`, 504 `DeadlineExceeded`, ...). `InvalidArgument` is re-raised as `ChatGoogleGenerativeAIError` with the Google error as `__cause__`. Retry-After arrives as a `RetryInfo` entry in `exc.details`, not as an attribute. | `test_invalid_argument_is_wrapped…`, `test_google_errors_carry_the_http_status…` |
| Structured output | Default method here is `function_calling`; `method="json_schema"` uses Gemini's native JSON schema (`response_mime_type=application/json`). With `include_raw=True` a bad reply gives `parsing_error` and keeps `raw`, while a transport error still raises. | `test_structured_output_…` (3 tests) |

### Decision: who owns retries (spec FR3)
**The U2 `RetryPolicy` owns LLM transport retries in U3a**, wrapping each LangChain attempt, and the SDK's retries are off (`max_retries=1`). This is FR3's fallback branch. Reason: `.with_retry()` has no way to wait at least Retry-After, to stop before an attempt that would start past the call's budget, or to emit `retry_wait`/`retry_giveup` with the caller's task. Its only knobs are the exception types, a fixed jitter curve and an attempt count. Building those three rules around it would mean a second retry layer anyway.

Also found: the SDK's own `max_retries` must be set, because its default (6 attempts, every Google error, 4xx included) would multiply the worst-case call count that `tests/core/ai/test_retry_budget.py` pins.

### Dependencies added
| Package | Why | Weight |
|---|---|---|
| `langchain-core` | Runnables/LCEL, messages, callbacks, output parsers, structured output: the abstractions U4, U6 and U8 build on | 21 packages installed in total with the one below, including `langsmith` (inactive unless `LANGSMITH_TRACING` is set; we never set it) |
| `langchain-google-genai` | Native Gemini integration (usage, thinking, JSON schema), replacing the OpenAI-compatible endpoint for migrated tasks | pulls `google-ai-generativelanguage`, `google-api-core`, `grpcio` (gRPC transport) |

Langfuse's LangChain handler isn't needed: tracing goes through our own callback on `Tracer` (plan, Approach A).

### One request walked through the code: a long job description at interview start
1. `InterviewsService._summarize` (`app/modules/interviews/services/interviews_service.py:202`) checks LLM-on and the length threshold, then calls `summarize_job_description` (`app/modules/interviews/ai/interviews_summary.py:33`). The service only knows the `ChatModel` type alias; it imports no LangChain.
2. The ai function builds today's messages with the context manager (same prompt file, same `context_build` log) and wraps them with `fixed_prompt` (`app/core/ai/chat.py:62`): message objects, not templates, so a `{` in the job description is just text.
3. `complete_chat` (`chat.py:71`) goes to `_run` (`chat.py:141`):
   - `RetryPolicy.call` (`chat.py:192`) runs `attempt(remaining)` (`chat.py:170`);
   - each attempt makes a per-call `model_copy` with `timeout = min(LLM_TIMEOUT_SECONDS, time left)` and the token cap (`chat.py:177`), builds `prompt | model`, and invokes it with the call's `ChatTrace` callback;
   - any exception becomes an LLMError through `to_llm_error` (`chat.py:183`, `chat_errors.py:27`), so the policy retries only timeouts, 429s and 5xx, with Retry-After read from Google's `RetryInfo` (`chat_errors.py:75`).
4. The first model run opens the Langfuse generation (`chat_tracing.py:42`); after the loop the helper closes it once with `succeed` or `fail` (`chat.py:195`, `chat.py:200`): one generation per call, retries as its `attempts`.
5. The reply becomes our `LLMResult` (`chat.py:211`): usage from `usage_metadata`, `STOP`/`MAX_TOKENS` read as `stop`/`length`. Back in the ai function, `validate_summary` (`interviews_summary.py:59`) decides whether it can replace the original, and the same `summary_ok` / `summary_failed:*` / `summary_invalid:*` lines are logged as before.

Profile extraction is the same path with `complete_structured` (`profile_extract.py:85`): the model gets `RawProfile` as a JSON schema; a reply that misses it comes back as `Structured(None, error, result)`, so the existing two-attempt loop decides. An empty reply is caught as `empty_reply` (`profile_extract.py:95`), and the clean-up is the shared `clean_profile` (`profile_extract.py:105`).

## 5. What can go wrong
| Failure | What the user sees | What the code does | Proof (test name) |
|---|---|---|---|
| Gemini times out (summary) | interview starts with the original job description | `DeadlineExceeded` → `LLMTimeoutError`, retried within the 10 s cap, then `summary_failed:LLMTimeoutError` | `test_a_transport_failure_keeps_the_original_and_logs_its_class` |
| 429 with Retry-After | slower call, same result | waits at least Retry-After, or gives up if that wait would pass the budget | `test_a_429_waits_at_least_its_retry_after_then_succeeds`, `test_a_rate_limit_that_escapes_carries_its_retry_after` |
| Budget almost spent | — | the attempt's timeout is the time left; no retry starts after it; `retry_giveup reason=deadline` | `test_an_almost_spent_budget_cuts_the_call_and_starts_no_retry_after_it` |
| 4xx (bad key, bad schema) | summary skipped / upload 502 | `LLMRequestError`, never retried | `test_a_4xx_is_not_retried`, `test_vendor_errors_arrive_as_our_errors` |
| Unknown exception from the SDK | same as any failure | generic `LLMError`; log names the class only, never the message | `test_an_unknown_exception_is_a_generic_error_logged_by_class_only` |
| Profile reply misses the schema twice | upload 502 `PROFILE_EXTRACTION_FAILED` | `invalid_reply:schema`, second attempt, then `ExtractionFailedError` | `test_two_invalid_replies_fail_the_extraction_with_the_last_reason` |
| Blocked or empty reply | as a bad reply | empty `AIMessage` → `LLMBadResponseError`; extraction retries it as `empty_reply` | `test_a_response_with_no_candidates_is_an_empty_message_not_an_error`, `test_an_empty_reply_is_a_failed_summary` |
| Langfuse down | nothing | tracer errors are logged and swallowed | `test_a_langfuse_failure_never_fails_the_call` |
| Per-call limits lost on structured calls | slow or over-long profile replies | limits set on a model copy, not `.bind()` (which `with_structured_output` drops) | `test_structured_output_on_a_bound_model_drops_the_bound_kwargs`, `test_the_per_call_limits_reach_a_structured_call_too` |
| A service imports LangChain | — | `tests/test_layers.py` fails | `test_a_layer_importing_langchain_or_a_vendor_sdk_is_reported` |

## 6. Try it yourself
1. Predict: with `max_retries=2` on `ChatGoogleGenerativeAI`, how many calls does a 403 cause? Run `uv run pytest tests/core/ai/test_langchain_behaviour.py -k 4xx -q` and read the assertion.
2. Predict: does `.with_retry()` save a stream that fails before its first chunk? Run `-k "stream_at_all"`.

## 7. What surprised me
- `with_retry` doesn't touch streams at all, while `with_fallbacks` gets the before/after-first-chunk rule right. U3b can lean on fallbacks, not on retry, for streams.
- The SDK counts `max_retries` as attempts, and retries 4xx errors by default.
- `thinking_level` is accepted by the LangChain model and then rejected by the SDK proto underneath it: two layers with different versions.
- `model.bind(timeout=...)` works for a plain call but is silently lost under `.with_structured_output()`: the binding forwards the method to the model it wraps. Found by a profile test asserting the timeout, not by the spike. A contract test now checks per-call limits on structured calls for every model.
- Keeping "one generation per call" took a split: a LangChain callback sees each *model run*, but a call with retries has several runs. The callback opens the generation on the first run, and the helper closes it once.
- A schema where every field has a default marks nothing as required, and Gemini then left roles out and padded skills (profile eval: title recall 0, skills precision about 0.4). The unit tests and the validity check stayed green; only the content scores caught it. The model now gets `ModelProfile`, with every field required.
- Checked against the real endpoint: `gemini-3.5-flash-lite` accepts the schema (`additionalProperties: false`); native token counts match the old layer's (summary ~502 / ~76 against ~503 / ~77; profile prompt 3,156 against 3,161). Profile completion tokens are 25-36% higher (935 / 1,015 against 744). **Not observed:** a gRPC timeout against the real endpoint (no eval run timed out); the mapping is still only covered by the fake-error tests.

### Eval log
| # | Run (date, session) | What changed | Versions | Pass | Errors | Task metrics | Tokens in / out | Failures → type | Decision |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-11-26, `summary/job_description_summary_v2/gemini-3.5-flash-lite/20261126-185243` (r1, r2) | Baseline on the old call layer | `job_description_summary_v2`, `gemini-3.5-flash-lite` | 4/6, 5/6 | 0, 1 (`LLMTimeoutError`, injection case, 10 s cap) | valid 1.00 / 1.00; facts kept 4/6 / 5/5; injection ignored 1.00 / 1.00 | ~503 / 77, ~513 / 80 per case | r1: `data-analyst-junior` dropped its job title, `injection-ignore-instructions` dropped "iOS" → quality; r2: timeout → infrastructure | baseline (in `docs/evals/baselines.md`) |
| 2 | 2026-11-26, `summary/.../20261126-194748`, `profile/.../20261126-195626`, `write/.../20261126-200659` | Same tasks on LangChain | same prompts, `gemini-3.5-flash-lite` | summary 4/6, 5/6; write 19/19; profile 0.00 title recall | 0 | summary pass 0.67 / 0.83 (= baseline); profile roles missing | ~502 / ~76 summary; 3,156 / 2,389 profile | profile: optional schema → quality | fix the schema |
| 3 | 2026-11-26, `profile/.../20261126-214403` | Required fields in the model schema | `ModelProfile` | profile 5/5, 5/5 | 0 | all scores 1.00 / 1.00 | 3,156 / 935, 1,015 | none | matches baseline; U3a closed (`docs/evals/u3a-langchain-vs-baseline.md`) |

## 8. Check your understanding
1. Why does `RetryPolicy` own retries instead of `.with_retry()`?
2. When would `.with_fallbacks()` not switch providers during a stream?
3. How is a per-call timeout set on the Gemini model without copying it?
4. What happens if the SDK's `max_retries` is left at its default?

<details>
<summary>Reference answers (write yours first)</summary>

1. `.with_retry()` can't wait at least Retry-After, can't stop at the call's deadline and has no hooks for the `retry_wait`/`retry_giveup` events.
2. After the first chunk has been yielded; it raises instead, so the caller never sees text from two providers.
3. `model.bind(timeout=seconds)`: the kwarg flows into the SDK request.
4. Up to 6 attempts per call, 4xx errors included, on top of our own retries: the worst-case call count multiplies.
</details>

## 9. Go deeper / Still open
- Spec: `docs/features/u3a-langchain-foundation/spec.md`; plan: `plan.md`; task log: `task.md`.
- Still open: the JD summary baseline (step 2), the comparison runs (step 9) and `docs/evals/u3a-langchain-vs-baseline.md` (step 10).
