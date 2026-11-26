# Implementation Plan: U3a LangChain foundation + first chains

## Overview
Add the LangChain base in `app/core/ai/` (chat model factory, error mapping, time-budgeted call helper, a callback that drives the existing `Tracer`, a fake chat model, a contract test) and move the job-description summary and profile extraction onto it without changing behavior. Spec: `docs/features/u3a-langchain-foundation/spec.md`.

## Architecture & Design
- **One core call helper:** the migrated `ai/` functions call a single helper in `core/ai/`. It runs a LangChain runnable (`prompt | model`, or the model `.with_structured_output()`) under the call's time budget, with exactly one retry owner. It attaches our tracing callback and returns our existing `LLMResult`, or the structured object plus an `LLMResult`, or raises our `LLMError` types.
- **Why `LLMResult` stays:** services, `log_result` and the logs stay as they are until U3c deletes the old layer.
- **Wiring:** the app builds the chat model at startup next to the `LLMProvider`, and a `get_chat_model` dependency hands it to the two services. They type it with an alias defined in `core/ai/`, so no service imports `langchain*`.
- **Strangler shape:** only these two tasks switch. Every other task keeps `LLMProvider` untouched.

## Approaches Considered

| Approach | Trade-offs | Chosen? |
|----------|-----------|---------|
| A. Core call helper + alias + `LLMResult` kept; tracing through our own LangChain callback driving `Tracer` | Redaction, labels, usage and nesting reuse tested code. Services and logs unchanged. One owner for tracing. Doesn't use Langfuse's own handler. | **Yes**: grilling answers (tracing, wiring); "one owner per concern" rule; ponytail (no second tracing path) |
| B. Langfuse `CallbackHandler`, subclassed for redaction; ai functions return `AIMessage` | The standard route, but redaction depends on overriding the handler's internals. `Tracer` and the handler would both write generations. Every caller's logging changes. | No: two tracing owners, more churn |
| C. Own `ChatClient` wrapper class around the model | Hides LangChain completely, but it's a new hand-built abstraction on top of the one being replaced | No: user choice; YAGNI |

**Retry owner:** settled by spec FR3. `.with_retry()` owns retries unless the step 1 spike shows it can't keep the U2 rules. In that case the U2 `RetryPolicy` wraps each LangChain attempt, and the reason goes in `learnings.md`.

What `.with_retry()` exposes: `retry_if_exception_type`, `wait_exponential_jitter`, `stop_after_attempt`. It has no Retry-After, no deadline stop and no `retry_wait`/`retry_giveup` hooks, so the fallback is the expected result. The spike confirms it rather than assuming it.

## Spec Requirements -> Implementation
- FR1 chat model from config -> Step 4
- FR2 error mapping -> Step 3
- FR3 retries -> Step 1 (decision), Step 6
- FR4 time budget -> Step 6
- FR5 tracing -> Step 5 (callback), Step 6 (attached per call)
- FR6 fake chat model -> Step 5
- FR7 contract test -> Step 6
- FR8 JD summary on LangChain -> Step 8
- FR9 profile extraction with structured output -> Step 9
- FR10 JD summary eval -> Step 2
- FR11 direct replacement -> Steps 8, 9
- FR12 eval tooling follows the tasks -> Steps 8, 9
- Non-functional (latency, cost, privacy, security, dependencies) -> Steps 1, 5, 10

## Implementation Steps
Checkpoint interval: every 3 steps. Hard stops after Step 2 (the user runs the JD summary baseline) and after Step 9 (the user runs the comparison evals).

1. **Spike: dependencies and the library behavior U3a relies on.**
   - Add `langchain-core` and `langchain-google-genai` with `uv add`, after checking that both install and import on Python 3.14. Langfuse is not needed for LangChain because tracing goes through our own callback.
   - Pin the behaviors we rely on in tests, using LangChain's fake chat models (no network):
     - what `.with_retry()` can and can't configure (Retry-After, deadline stop, hooks);
     - that `with_structured_output(..., include_raw=True)` returns `parsing_error` instead of raising;
     - that `AIMessage.usage_metadata` is read the way we expect;
     - that `ChatGoogleGenerativeAI` accepts `max_retries=0`, a `timeout`, the API key and the thinking settings;
     - how a per-call timeout can be set (a bind, a model copy, or a request option);
     - which exception classes its SDK raises for 429, 5xx, 4xx and timeouts.
   - For U3b, also record how a stream behaves under `.with_retry()` and `.with_fallbacks()` (before and after the first chunk).
   - Write the findings and the retry-owner decision in `learnings.md`.
   - Files: `pyproject.toml`, `uv.lock`, `tests/core/ai/test_langchain_behaviour.py` (new), `docs/features/u3a-langchain-foundation/learnings.md` (new).
   - Verify: `uv run pytest tests/core/ai/test_langchain_behaviour.py -q` + gate commands.
   - Test: after (pins external library behavior).

2. **JD summary eval on the old code (FR10).**
   - Add a `summary` task to the eval runner, with about 5–6 cases (one injection case, each with must-keep facts) in the existing eval data style.
   - Four scorers: `validate_summary` passes; must-keep facts are present; injected text isn't followed; token usage is recorded. Results go to Langfuse experiments like the other tasks.
   - The run calls today's summary path, so it gives the baseline.
   - Files: `app/modules/interviews/tooling/interviews_evals.py`, the summary eval cases next to the existing eval data (`app/modules/interviews/data/`), `tests/modules/interviews/tooling/test_evals.py`.
   - Verify: `uv run pytest tests/modules/interviews/tooling -q` + gate commands.
   - Test: first. Seam: the runner's public run-case and scoring functions, as the existing tests use them (confirmed).
   - **Stop:**
     - the user runs `uv run python -m app.modules.interviews.tooling.interviews_evals --task summary --model gemini-3.5-flash-lite --repeat 2`;
     - Claude reads the runs in Langfuse and adds the baseline row to `docs/evals/baselines.md`, and removes `job_description_summary_v2` from the gaps list.

3. **`to_llm_error()` (FR2).**
   - Maps LangChain and Google SDK exceptions (the classes found in Step 1) to `LLMTimeoutError`, `LLMRateLimitError` (with Retry-After), `LLMServerError`, `LLMRequestError` and `LLMBadResponseError`.
   - Anything else becomes a generic `LLMError`, and the log names the original class only, never its message.
   - Files: `app/core/ai/chat_errors.py` (new), `tests/core/ai/test_chat_errors.py` (new).
   - Verify: `uv run pytest tests/core/ai/test_chat_errors.py -q` + gate commands.
   - Test: first. Seam: `to_llm_error(exc)` (confirmed).
   - Slices, one behavior each:
     1. rate limit with Retry-After;
     2. rate limit without it;
     3. timeout;
     4. 5xx;
     5. 4xx;
     6. bad or blocked response;
     7. unknown exception, logged by class only.

4. **Chat model factory (FR1).**
   - `build_chat_model(settings, *, model=None)` returns a LangChain chat model for the primary provider in `LLM_PROVIDERS`, or None when the list is empty. Gemini goes through `ChatGoogleGenerativeAI` with the vendor's key and model, the SDK's own retries off, and `llm_timeout_seconds`.
   - Add a small vendor → reasoning/thinking parameter table to config, read by the factory, with no hardcoded model names or keys. (Step 1 finding: only `thinking_budget` works with the bundled SDK; `thinking_level` fails to build the request. The table's default is "no thinking setting", matching today's calls.)
   - Define the `ChatModel` type alias that services import.
   - `base_url` stays in use by the old provider only.
   - Files: `app/core/ai/factory.py`, `app/core/ai/chat.py` (new, alias), `app/core/config.py`, `.env.example`, `tests/core/ai/test_chat_factory.py` (new).
   - Verify: `uv run pytest tests/core/ai/test_chat_factory.py tests/core -q` + gate commands.
   - Test: first. Seam: `build_chat_model(settings)` (confirmed).
   - Slices:
     1. empty `LLM_PROVIDERS` gives None (EC1);
     2. google gives a native model with key, model and timeout from config;
     3. `--model` override;
     4. SDK retries are 0;
     5. the thinking table is applied.

5. **Tracing callback + fake chat model (FR5, FR6).**
   - A LangChain callback handler in `core/ai/` turns each model run into a `Tracer.start_generation`, then `Generation.succeed` or `fail` with usage from `usage_metadata`.
   - It carries the call's labels (task, prompt_version, redact) and nests under the current trace.
   - A redacted call records the placeholder for input and output (EC14). Tracer failures never fail the call (EC15).
   - Fake chat model helpers build a LangChain fake model that returns set text, structured replies (as JSON text or tool calls, whichever Step 1 showed the structured path needs), usage, or raises a given vendor-style error.
   - Files: `app/core/ai/chat_tracing.py` (new), `app/core/ai/chat_fake.py` (new), `tests/core/ai/test_chat_tracing.py` (new).
   - Verify: `uv run pytest tests/core/ai/test_chat_tracing.py tests/core/ai/test_tracing.py -q` + gate commands.
   - Test: first. Seam: the callback through a fake-model invoke with a recording `Tracer` client, as `test_tracing.py` does today (confirmed).
   - Slices:
     1. a generation is recorded with labels and usage;
     2. redacted input and output;
     3. a failed call records `fail` with the error class;
     4. a tracer error is swallowed;
     5. a disabled tracer adds nothing.

6. **The core call helper + contract test (FR3, FR4, FR5, FR7).**
   - One synchronous helper takes a runnable, its inputs, a time budget, a max-token limit, labels, and an optional structured schema.
   - It sends nothing when the budget is already spent.
   - Each attempt runs with a per-call timeout of min(`llm_timeout_seconds`, time left), using the mechanism found in Step 1.
   - Retries follow the owner chosen in Step 1:
     - only timeout, 429 and 5xx errors;
     - full jitter, never shorter than Retry-After;
     - no attempt starts past the budget;
     - `retry_wait` and `retry_giveup` logged with the task;
     - `llm_max_retries` sets the count.
   - It attaches the Step 5 callback and maps errors through `to_llm_error`.
   - It returns `LLMResult` (text, usage, finish reason, latency, attempts); for structured calls it returns (parsed object or parsing error, `LLMResult`).
   - Contract test: one suite parametrized over every model the factory can build plus the fake. It covers text reply, structured reply, usage and error mapping. The google model runs against a scripted HTTP layer if Step 1 found one; otherwise its part is an opt-in real-model test.
   - Files: `app/core/ai/chat.py`, `tests/core/ai/test_chat.py` (new), `tests/core/ai/test_chat_contract.py` (new).
   - Verify: `uv run pytest tests/core/ai -q` + gate commands.
   - Test: first. Seam: the helper's public function, driven by the fake chat model with an injected clock and sleep (confirmed).
   - Slices:
     1. text reply gives an `LLMResult` with usage;
     2. no usage reported (EC16);
     3. spent budget, nothing sent;
     4. almost-spent budget: cut off, `LLMTimeoutError`, no later retry (EC7);
     5. 429 with Retry-After: the wait is at least Retry-After (EC5);
     6. 5xx retried up to `llm_max_retries`, then giveup logged;
     7. 4xx not retried;
     8. unknown exception becomes a generic `LLMError` (EC6);
     9. structured: valid object, or parsing error without raising.

7. **Wiring + layer rule (AC11).**
   - Build the chat model at startup next to the provider, store it on `app.state`, and close it on shutdown if it needs closing.
   - Add the `get_chat_model` dependency.
   - Extend `check_layers` so a route, controller, service or repository importing `langchain*` (or the Google SDK) is a violation, with a test for each layer.
   - Files: `app/main.py`, `app/core/ai/dependencies.py`, `tests/test_layers.py`, `tests/conftest.py` (or the app fixture that sets `app.state`) so tests get the fake chat model.
   - Verify: `uv run pytest tests/test_layers.py -q` + full gate.
   - Test: first for `check_layers` (seam: `check_layers`, confirmed); skip for the wiring itself (covered by the full suite).

8. **JD summary on LangChain (FR8, FR11, FR12).**
   - A new `interviews/ai/` function builds the summary chain from `job_description_summary_v2.md`. The messages are the same as `JobDescriptionSummary.build` produces today: a `ChatPromptTemplate` from that output, or the built messages passed as is if that is the only way to keep them identical.
   - It calls the core helper with `SUMMARY_TIME_CAP_SECONDS`, checks the reply with `validate_summary`, and logs `summary_ok`, `summary_failed:*` and `summary_invalid:*` exactly as today. It returns the summary or None.
   - `InterviewsService._summarize` keeps the LLM-off and threshold checks and calls that function. The service takes the chat model instead of calling `LLMProvider.complete` for the summary.
   - The eval runner's `_summarize`, used by the `summary`, `write` and `stream` tasks, calls the same function with a chat model built by `build_chat_model`.
   - Files: `app/modules/interviews/ai/interviews_summary.py` (new), `app/modules/interviews/services/interviews_service.py`, `app/modules/interviews/dependencies/interviews_start_dependencies.py`, `app/modules/interviews/tooling/interviews_evals.py`, `tests/modules/interviews/ai/test_summary.py` (new), the existing start-interview service and route tests.
   - Verify: `uv run pytest tests/modules/interviews -q` + gate commands.
   - Test: first. Seams: the summarize function and `InterviewsService.start` (confirmed).
   - Slices:
     1. under the threshold, no call (EC2);
     2. success: summary stored and `summary_ok` logged;
     3. transport failure keeps the original and logs `summary_failed:<class>` (EC3);
     4. invalid reply keeps the original and logs `summary_invalid:<reason>` (EC4);
     5. LLM off, no call (EC1);
     6. the generation sits inside the `start-interview` trace with task and prompt_version (AC8).

9. **Profile extraction with structured output (FR9, FR11, FR12).**
   - Split `profile_reply.py` in two: JSON-text parsing, kept only while the eval history needs it, and the clean-up from `_RawProfile` to `CandidateProfile` (fit to caps, dedupe, the empty-profile check). The clean-up is reused on the structured result.
   - `extract_profile` takes the chat model. It builds `profile_extract_v1.md` + the fenced `<resume>` message, and calls the core helper with `.with_structured_output(_RawProfile)` and `redact` set, inside the existing attempt loop (`MAX_ATTEMPTS`, `PROFILE_TOTAL_SECONDS`).
   - Outcomes:
     - empty reply or schema failure gives `empty_reply` / `invalid_reply:*` and the next attempt;
     - an escaped `LLMError` gives `ExtractionFailedError(<class>)`;
     - no skills and no roles gives `EmptyProfileError`.
   - `ProfileService`, its dependency and `profile_evals.py` switch to the chat model.
   - Files: `app/modules/profile/ai/profile_extract.py`, `app/modules/profile/ai/profile_reply.py`, `app/modules/profile/services/profile_service.py`, `app/modules/profile/dependencies/profile_dependencies.py`, `app/modules/profile/tooling/profile_evals.py`, `tests/modules/profile/` (the extraction, service and route tests).
   - Verify: `uv run pytest tests/modules/profile -q` + gate commands.
   - Test: first. Seams: `extract_profile`, `ProfileService.upload` and the upload route (confirmed).
   - Slices:
     1. valid first reply gives a profile and one call;
     2. invalid then valid gives a profile and two calls (EC8);
     3. two invalid replies give `ExtractionFailedError`, `invalid_reply:*` (EC9);
     4. empty profile gives `EmptyProfileError` with no retry (EC10);
     5. transport error gives `ExtractionFailedError(<class>)` (EC11);
     6. over-cap and duplicate fields are trimmed (EC12);
     7. trace redacted (EC14, AC8);
     8. upload HTTP responses unchanged.
   - **Stop:**
     - the user runs the comparison evals: `--task summary` and the profile eval (`uv run python -m app.modules.profile.tooling.profile_evals --model gemini-3.5-flash-lite --repeat 2`);
     - also `--task write` once, as a sanity check that the summary inside it still behaves.

10. **Compare, record, close out.**
    - Claude reads the runs in Langfuse and writes `docs/evals/u3a-langchain-vs-baseline.md`: per eval, the run names, the score of each repeat, the baseline, the noise margin and the verdict.
    - A drop beyond the margin is a regression to fix before closing.
    - Finish `learnings.md`: spike results, the retry-owner decision, dependencies and why, what LangChain hid or added, and a link to the comparison.
    - Tick U3a in `docs/ai-engineering-upgrade-path.md`, run `graphify update .`, and offer to update the tracker artifact.
    - Files: `docs/evals/u3a-langchain-vs-baseline.md` (new), `docs/features/u3a-langchain-foundation/learnings.md`, `docs/ai-engineering-upgrade-path.md`.
    - Verify: full gate + `graphify update .`.
    - Test: after (real-model evals, run by the user).

## Affected Files & Patterns
- **`app/core/ai/` (new):**
  - `chat.py`: the alias and the call helper.
  - `chat_errors.py`
  - `chat_tracing.py`
  - `chat_fake.py`
  - `factory.py` gains `build_chat_model`.
  - `dependencies.py` gains `get_chat_model`.
- **Changed feature files:**
  - `interviews/ai/interviews_summary.py` (new);
  - `interviews_service.py` and its start dependencies;
  - `profile_extract.py`, `profile_reply.py`, `profile_service.py`, `profile_dependencies.py`;
  - the eval runners (`interviews_evals.py`, `profile_evals.py`).
- **Unchanged:** `LLMProvider`, `openai_compatible.py`, `json_reply.py`, `TracingProvider`, `FakeProvider`, `RetryPolicy`. Every other task still uses them.
- **Patterns to follow:**
  - `RetryPolicy` (injected clock and sleep, `_OutOfTime` budget stop, `log_giveup`) for the retry rules and their tests;
  - `TracingProvider.complete` for how a generation is started, finished and failed;
  - `test_tracing.py`'s recording client;
  - `FakeProvider` for scripted replies;
  - `build_provider` for config reading and the LLM-off warning.
- **Risks:**
  - The LangChain or `langchain-google-genai` API differs from what's assumed. Step 1 catches it before any code depends on it.
  - Per-call timeout control on `ChatGoogleGenerativeAI` may need a model copy per call. The cost is checked in Step 1.
  - The structured-output schema may need simplifying for Gemini (Step 1, opt-in real call).
  - Two clients to Gemini exist at once, old for unmigrated tasks and new for these two. That's accepted until U3c.

## Testing Strategy
- **Framework and command:** `pytest`, with `uv run pytest -q` (about 1 minute, 2553 passed and 7 skipped at handoff).
- **Gate commands, after every step:**
  - `uv run pytest -q`
  - `uv run --with ruff ruff check app tests`
  - `tests/test_layers.py`, part of pytest
  - for new core files: `uv run --with pyright pyright <file>`
- **Coverage map:**

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 4 | first | |
| AC2 | 3, 6 | first | mapping unit tests + through the helper |
| AC3 | 6 | first | injected clock |
| AC4 | 1, 6 | after, first | Step 1 decides the owner; Step 6 tests the rules on it |
| AC5 | 6 | first | google part may be opt-in (see risks) |
| AC6 | 8 | first | |
| AC7 | 9 | first | |
| AC8 | 5, 8, 9 | first | |
| AC9 | 2 | first + user baseline run | |
| AC10 | 10 | after | user-run evals, compared in Langfuse |
| AC11 | 7 | first | |
| AC12 | every step, 10 | gate | |
| AC13 | 1, 10 | after | |
| EC1 | 4, 8, 9 | first | |
| EC2 | 8 | first | |
| EC3 | 8 | first | |
| EC4 | 8 | first | |
| EC5 | 3, 6 | first | |
| EC6 | 3, 6 | first | |
| EC7 | 6 | first | |
| EC8 | 9 | first | |
| EC9 | 9 | first | |
| EC10 | 9 | first | |
| EC11 | 9 | first | |
| EC12 | 9 | first | |
| EC13 | 2, 10 | first, after | summary injection case; existing profile eval cases |
| EC14 | 5, 9 | first | |
| EC15 | 5 | first | |
| EC16 | 6 | first | |

- **Must verify, not assume:**
  - Python 3.14 support of the new packages;
  - `.with_retry()`'s options;
  - `ChatGoogleGenerativeAI`'s `max_retries`, timeout and thinking settings, and its exception classes;
  - structured output on `gemini-3.5-flash-lite`;
  - usage reporting from the native integration;
  - stream retry and fallback behavior (recorded for U3b).
- **Open questions:** none. Every EC has an expected outcome.
- **Known baseline failures:** these are flaky and pass on re-run:
  - `test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only`;
  - `test_profile_read_resume.py::test_a_valid_docx_gives_its_paragraphs_then_its_table`;
  - an occasional WinError 10055.

## Blockers & Resolutions
- **Retry owner unknown until the spike:** Step 1 decides, under spec FR3's rule. Step 6 tests whichever owner wins against the same rules.
- **Python 3.14 support:** checked in Step 1 before anything depends on it. If a package doesn't support it, stop and report; there's no workaround in this slice.
- **No JD summary baseline:** Step 2 builds the eval, and the hard stop gets the user's baseline run before Step 8 changes the code.
- **Profile redaction under LangChain:** our own callback reuses `Tracer`'s redaction (AC8 test).
- **Services must not import LangChain:** the `ChatModel` alias is imported from `core/ai/`, and the Step 7 layer test enforces it.

## Trade-offs & Rationale
- **Own callback instead of Langfuse's `CallbackHandler`:** one tracing owner, redaction reuse, and no second writer of generations. It still teaches LangChain callbacks. Revisit in U4 if prompt linking needs the Langfuse handler.
- **`LLMResult` kept as the helper's return:** the logs and `log_result` stay unchanged, so the eval comparison only measures the model path. U3c removes it with the old layer.
- **Synchronous helper:** both callers and the eval tooling are synchronous (spec Constraints). Async comes with U3b's streaming tasks.
- **Layer rule now, not in U3c:** LangChain enters the code in this slice, so the rule should guard it from the first import (spec AC11).
- **`profile_reply.py` split instead of rewritten:** the clean-up logic is tested and shared; only the JSON-text parsing goes away from the live path.

## Project Rules Applied
- `CLAUDE.md`, provider abstraction: LangChain only in `core/ai/` and feature `ai/` folders; vendor errors mapped before leaving `core/ai/`; no vendor stores.
- `CLAUDE.md`, prompts are data: the same `.md` files and versions, loaded through `load_prompt` or templates built from it.
- `CLAUDE.md`, structured outputs: Pydantic schema, attempt loop and safe failure kept.
- `CLAUDE.md`, privacy: résumé redacted in traces and never logged.
- `CLAUDE.md`, compare AI changes against the baseline: Steps 2 and 10, with a comparison file per slice.
- `CLAUDE.md`, tests: fake model in unit tests; real-model runs opt-in and run by the user.
- `CLAUDE.md`, Don'ts: dependencies justified in Step 1 and `learnings.md`; no hardcoded model names or keys.
- Upgrade path, one owner per concern: one retry owner and one tracing owner per call.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | Mapped `core/ai` (factory, tracing, retry, fake, provider), the summary call in `InterviewsService._summarize`, `extract_profile`'s attempt loop and redaction, the eval runners' `build_provider` use, the `app.state` wiring in `main.py` |
| grilling | Tracing owner (own callback), wiring (alias + `LLMResult`), test seams confirmed |
| ponytail | Rejected the `ChatClient` wrapper and a second tracing path; chat models only (no embeddings) |
| graphify | Skipped: `/feature` already queried this domain and the results were too broad; lean-ctx symbol lookups answered the questions |

## Ready to Implement
- All FRs mapped to steps.
- Every step has a Test tag, and every AC and EC is mapped, with no uncovered IDs.
- Gate commands are listed.
- Every step names its files and its verification command.
- Approaches Considered is filled; the checkpoint is every 3 steps, plus two hard stops for the user's eval runs.
- Blockers have resolutions, and the spike-dependent ones have a decision rule.
- One deviation from the upgrade path, already in the spec: the layer rule moves into U3a (AC11).
