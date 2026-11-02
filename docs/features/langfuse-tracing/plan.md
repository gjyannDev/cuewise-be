# Implementation Plan: Langfuse Tracing

## Overview
Record every LLM call as a Langfuse generation, grouped into one trace per LLM-capable request with user and session ids, full content, fail-open, flushed on shutdown. Source: `spec.md` (medium: ~8 files, ~250 lines).

## Architecture & Design
- **TracingProvider wrapper** (new `app/core/ai/tracing.py`): implements `LLMProvider`, wraps the real provider, records one generation per `complete()` / `stream()`. Applied inside `build_provider()`, the one place providers are picked. `OpenAICompatibleProvider` stays untouched (deviation from spec wording "in OpenAICompatibleProvider", same goal; user-confirmed). A future fallback chain gets traced for free.
- **Client factory** in the same module: builds a `Langfuse` client from `Settings` (SDK reads `os.environ`, `.env` only feeds pydantic) and returns a no-op when keys are missing. One tracer object is shared by the wrapper, the trace boundaries and the lifespan.
- **Trace boundaries:** `@observe` on the three LLM-capable controller entry points (`start`, `answer`, `stream_answer`). The async-generator case (`stream_answer`) opens its span inside the generator, because the route returns before the stream runs. User id is set at the boundary; session id too, except in `start` where it is set once the session exists (updating the current trace).
- **Labels:** `complete()` / `stream()` gain an optional keyword-only `trace_labels` (task, prompt_version, budget_left_ms). Callers in `interviews_turn.py` and `interviews_controller._summarize` pass what they already log through `log_llm_call`. `attempts`, `finish_reason`, usage, latency come from `LLMResult`.
- **Failure handling:** every SDK touch sits behind one small guard that swallows and logs class name only (no content). LLM exceptions are re-raised unchanged after the generation is closed as ERROR (error class + status code). Streams: `finally` closes the generation; partial text, WARNING, `cancelled` when closed early.
- **Config:** `langfuse_public_key`, `langfuse_secret_key` (`SecretStr | None`), `langfuse_base_url`, `app_env` (default `development`); blank means unset (reuse the existing blank-is-unset validator pattern). Half-set keys: tracing off + one startup warning.
- **Environment:** from `app_env`; eval script overrides to `eval` via a `build_provider` argument.
- **Lifespan:** after the provider closes, flush then shut down the client; both guarded.

## Spec Requirements -> Implementation
| Requirement | Step |
|---|---|
| Settings, APP_ENV, half-set keys | 1 |
| Generation per call, usage, labels, ERROR, cancelled, retries as metadata | 2, 3 |
| Fail-open, no-op without keys | 2 |
| Trace per request, user/session ids | 4 |
| Flush on shutdown | 5 |
| Eval env=eval | 6 |
| `.env.example`, graph update | 1, 7 |

## Implementation Steps
1. **Config + `.env.example`** — Test: first. Seam: `Settings(...)`. Add four fields and blank-is-unset handling; add `LANGFUSE_*` and `APP_ENV` to `.env.example`.
2. **Tracer core** — Test: first. Seam: `build_tracer(settings)` public result. Enabled/disabled/half-set logic, guard helper, no-op tracer.
3. **TracingProvider** — Test: first. Seam: `TracingProvider.complete` / `.stream` with an injected fake Langfuse client. Slices: success + usage; retried (attempts metadata); `LLMError` -> ERROR and re-raised; usage None omitted; stream success; stream closed early -> WARNING cancelled; SDK raising -> result unchanged. Also: add `trace_labels` to the `LLMProvider` protocol, `OpenAICompatibleProvider` (accepted and ignored), `FakeProvider`, and wrap in `build_provider`.
4. **Trace boundaries** — Test: after. Seam: routes via TestClient with a fake tracer. `@observe` on `start`, `answer`, `stream_answer`; set user id / session id; pass `trace_labels` at the five `complete`/`stream` call sites. Other routes untouched. Concurrency check for ids.
5. **Lifespan flush** — Test: first. Seam: app lifespan with a fake tracer: flush called once on shutdown; flush raising does not break shutdown.
6. **Eval script** — Test: skip. Pass `environment="eval"` where `interviews_evals.py` builds its provider.
7. **Verify** — `uv run pytest`, `uv run ruff check . && uv run ruff format .`, one manual smoke against real Langfuse (keys in `.env`), then `graphify update .`.

## Affected Files & Patterns
- New: `app/core/ai/tracing.py`; tests under `tests/core/ai/` (tracer, provider wrapper) and `tests/modules/interviews/` (route-level).
- Edit: `app/core/config.py`, `.env.example`, `app/core/ai/provider.py` (protocol), `app/core/ai/factory.py`, `app/core/ai/openai_compatible.py` (kwarg only), `app/core/ai/fake.py`, `app/main.py`, `app/modules/interviews/interviews_controller.py`, `interviews_turn.py`, `interviews_evals.py`.
- Patterns reused: blank-is-unset validator in `Settings`; `build_provider` as single construction point; `log_llm_call` labels; test `llm` fixture accepts `**kwargs` already, so route tests keep working.
- Graph: nodes `OpenAICompatibleProvider`, `log_llm_call` / `log_result` are the observability neighbours (graphify query).

## Testing Strategy
Framework: pytest (`uv run pytest`); lint `uv run ruff check .`. No test makes network calls; Langfuse is always a fake client.

| Spec ID | Step | Test mode | Notes |
|---|---|---|---|
| AC1 | 4 | after | start trace has summary generation, user_id, session_id (set after creation), environment |
| AC2 | 3, 4 | first/after | all turn calls under one trace |
| AC3 | 3, 4 | first/after | stream generation ends with text, usage, latency |
| AC4 | 3 | first | labels + usage fields; absent usage omitted (EC8) |
| AC5 | 3 | first | attempts > 1, single generation |
| AC6 | 3 | first | ERROR + same exception (EC5) |
| AC7 | 3 | first | early close and deadline cut (EC6, EC7) |
| AC8 | 1, 2 | first | blank keys, half-set (EC1, EC2) |
| AC9 | 2, 3 | first | SDK raises / unreachable (EC3, EC4) |
| AC10 | 5 | first | flush once; failure tolerated (EC10) |
| AC11 | 4 | after | auth/users/health/get/transcript/report create no trace |
| AC12 | 6 | skip | verified manually once in the dashboard |
| AC13 | 7 | after | whole suite, no network |
| AC14 | 1, 7 | first/after | `.env.example`; no key values in captured logs |
| EC9 | 3 | first | call with no active trace does not crash |
| EC11 | 4 | after | two concurrent requests keep separate ids |
| EC12 | 7 | after | fake tracer in `conftest` |

Verify against the real service (not assumed): SDK v5 behaviour of `@observe` on async generators, `propagate_attributes` / updating the current trace after start, usage field names and `cancelled` rendering in the dashboard, shutdown timeout (EC10), Hobby limits.

## Blockers & Resolutions
- None open. Spec wording "inside OpenAICompatibleProvider" resolved by user as a wrapper.
- Open to verify in step 4: if the SDK cannot set session id after span start in `start`, fall back to setting only user id there and logging the session id as metadata.

## Trade-offs & Rationale
- Wrapper over in-class edits: vendor-neutral, no httpx coupling, small blast radius; cost is one extra kwarg on the protocol.
- Explicit `trace_labels` over ContextVar: visible at call sites and testable; slightly more verbose.
- One generation per logical call: matches `log_llm_call`, keeps Hobby units low.
- Full content: owner's decision; revisit before real users (masking hook is the later switch).

## Project Rules Applied
- Vendor SDK only in `core/ai/`; routers untouched; config via pydantic-settings with `SecretStr`; `.env.example` updated.
- No content in our own logs; LLM mocked in tests; no new dependency (langfuse already present); no commit/push.

## Skills Consulted
| Skill | Contribution |
|---|---|
| lean-ctx | provider, factory, call sites, lifespan |
| graphify | observability neighbours (`log_llm_call`, usage report) |
| grill-me | wrapper vs in-class, label passing, test seams (confirmed) |
| ponytail | no new dependency; one wrapper, one tracer, no sampling |
| llm-security | full-content exposure noted as accepted risk |

## Ready to Implement
Yes. Seams user-confirmed. Next: `/implement`.
