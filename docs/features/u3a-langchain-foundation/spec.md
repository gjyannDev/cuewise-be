# Feature: U3a LangChain foundation + first chains

## Problem
Every LLM call in Cuewise goes through a layer we wrote by hand in `app/core/ai/`: `LLMProvider`, `openai_compatible.py`, `json_reply.py`, `TracingProvider`, `FakeProvider`, about 2,000 lines we maintain ourselves. The upgrade path (`docs/ai-engineering-upgrade-path.md`, U3) replaces it with LangChain so that later slices (U4 prompt templates, U6 retrievers, U8 LangGraph, the U3c fallback chain) can build on the standard abstractions. U3 is too big for one slice, so it runs as U3a, U3b and U3c. U3a lays the base and moves the two simplest tasks.

## Goal
- The LangChain base exists in `app/core/ai/`: a chat model built from config, vendor errors mapped to our `LLMError` types, the time budget enforced on each call, Langfuse tracing through LangChain's callback, a fake chat model for tests, and a contract test every factory model passes.
- The **job-description summary** and **profile extraction** run on LangChain.
- Both tasks score the same as before within the noise margin (profile: `profile_extract_v1` baseline in `docs/evals/baselines.md`; JD summary: a new eval with a baseline taken on the old code first), and nothing changes for the candidate.
- Learning goal: Runnables and LCEL (`prompt | model`), `.with_structured_output()`, `.with_retry()`, callbacks, and the strangler pattern.

## Project Conventions
- Rule files consulted: `CLAUDE.md` (repo root); no `.claude/rules/`. Upgrade path: `docs/ai-engineering-upgrade-path.md` (U3 and U3a sections). Carried-over rules: `docs/features/u2-tenacity/learnings.md`.
- Constraints those rules impose:
  - LangChain is imported only in `app/core/ai/` and the feature `ai/` folders (`interviews/ai/`, `profile/ai/`). Routes, controllers, services and repositories never import LangChain or a vendor SDK; services call the feature's `ai/` functions.
  - Vendor exceptions are mapped to the `LLMError` types before they leave `core/ai/`.
  - Models, keys and URLs come from config (`core/config.py`, `LLM_PROVIDERS` + `LLM_<VENDOR>_*`), never hardcoded.
  - Prompts stay as the versioned `.md` files; no prompt text in code.
  - One owner per concern: old and new layers may coexist during U3, never inside the same task.
  - Every new dependency is justified (what it replaces, what it adds, its weight) and checked for Python 3.14 support.
  - User text (job descriptions, résumés) is untrusted data and stays apart from instructions; résumé content is personal data and never reaches logs or Langfuse.
  - Unit tests mock the LLM (fake chat model); real-model runs are opt-in. The user launches real-model eval runs; Claude compares them in Langfuse and writes `docs/evals/u3a-langchain-vs-baseline.md`.
  - Layers only call downward (`tests/test_layers.py`).
- Code findings that frame this slice:
  - The JD summary call lives in the service today (`InterviewsService._summarize` calls `self.llm.complete` directly). Because services can't import LangChain, the call has to move behind an `interviews/ai/` function.
  - Profile extraction is already an `ai/` function (`profile/ai/profile_extract.py::extract_profile`): an attempt loop (`MAX_ATTEMPTS = 2`) within `PROFILE_TOTAL_SECONDS = 20`, parsing with `parse_profile_reply`, raising `ExtractionFailedError` / `EmptyProfileError`.
  - Both callers are synchronous (`InterviewsService.start`, `ProfileService.upload`), and so is the eval tooling.
  - Profile extraction marks its trace `redact` (`REDACT_LABEL`), so Langfuse stores a placeholder instead of the résumé and the reply. The JD summary is not redacted.

## User Flow
Nothing changes for the candidate.

1. The candidate starts an interview with a long job description. The app condenses it once (the JD summary). If that fails, the interview carries on with the original text, as today.
2. The candidate uploads a résumé. The app extracts a profile from it, or returns the same error responses as today.

For the developer:
1. Run the unit tests with the fake chat model, no network.
2. Run the new JD summary eval and the profile eval on the old code (baseline), then on the LangChain code, and compare them in Langfuse.

## Requirements

### Functional
- **FR1: chat model from config.** A factory in `core/ai/` builds a LangChain chat model from the existing LLM config. Gemini goes through the native `ChatGoogleGenerativeAI` integration. Settings that LangChain doesn't unify across vendors (reasoning/thinking) come from a small vendor → parameter table in config, not from code. With `LLM_PROVIDERS` empty the factory returns no model, as `build_provider` does today ("LLM off"). Chat models only; embeddings stay on `GoogleEmbedder` until U3b.
- **FR2: error mapping.** Errors from LangChain or the vendor SDK leave `core/ai/` only as our `LLMError` types (timeout, rate limit with its Retry-After, server error, bad request, bad response). An exception that isn't recognised becomes a generic `LLMError`, and the log names the original exception class but not its message.
- **FR3: retries on the chain.** Transport retries for the migrated tasks belong to `.with_retry()` on the chain, and the SDK's own retries are turned off, so exactly one layer retries. The U2 rules still hold: retry only timeouts, 429s and 5xx errors; full jitter; never wait less than Retry-After; never start an attempt past the call's time budget; the `retry_wait` / `retry_giveup` events go out with the caller's task; `llm_max_retries` from config sets the count. **If the step 1 spike shows that `.with_retry()` can't keep these rules, the U2 `RetryPolicy` owns LLM retries for U3a instead, and the reason is written down in `learnings.md`.**
- **FR4: time budget.** Each migrated call stops at its own budget: the summary's `SUMMARY_TIME_CAP_SECONDS`, and the remaining part of `PROFILE_TOTAL_SECONDS` for each extraction attempt. A call with no time left is not sent.
- **FR5: tracing.** Migrated calls appear in Langfuse as a generation inside the existing trace (for example `start-interview`), with the same `task` and `prompt_version` labels, token usage and latency as today. Profile extraction stays redacted: no résumé text and no reply in the trace.
- **FR6: fake chat model.** A LangChain fake chat model serves the unit tests of the migrated tasks. It can return set replies, return structured replies, and raise any of the mapped errors.
- **FR7: contract test.** One test suite runs against every model the factory can build (fake included): plain text reply, structured reply, usage reported, vendor errors arriving as our `LLMError` types.
- **FR8: JD summary on LangChain.** The summary is built from `job_description_summary_v2.md` as a `prompt | model` chain inside `interviews/ai/`, and the service calls that function. Behavior is unchanged: it runs only when the job description is longer than `SUMMARY_THRESHOLD`, makes a single attempt, keeps the original text on any failure, checks the reply with `validate_summary`, and logs `summary_ok` / `summary_failed:*` / `summary_invalid:*` as today.
- **FR9: profile extraction with structured output.** Extraction uses `.with_structured_output()` with the profile schema, built from `profile_extract_v1.md`. Today's clean-up (fit to caps, dedupe) still runs on the result. A reply that is empty or fails the schema counts as an invalid reply and uses the existing attempt loop (`MAX_ATTEMPTS`), then `ExtractionFailedError`. A valid reply with no skills and no roles still raises `EmptyProfileError`. The service-level errors and HTTP responses don't change.
- **FR10: JD summary eval.** A small eval set (about 5-6 cases) for `job_description_summary_v2`, run through the existing eval tooling and Langfuse experiments. It scores: the reply passes `validate_summary` (within the cap, shorter than the original, not empty); must-keep facts per case (role, seniority, key skills) are in the summary; a job description with injected instructions still gets a plain summary that doesn't follow them; token usage per case. The baseline is run on the old code before migrating and is added to `docs/evals/baselines.md`.
- **FR11: direct replacement.** Each task switches to LangChain outright: no config switch back to the old path. The old layer stays for the tasks that haven't migrated yet.
- **FR12: eval tooling follows the tasks.** The eval runners for the summary and the profile call the same `ai/` functions the app uses, so an eval measures the LangChain path.

### Non-Functional
- **Latency:** at least as fast as the U0 profile eval and the summary step today. No new per-call overhead beyond LangChain's own.
- **Cost:** token usage per call is the same as U0 within the noise margin (same prompts, same model). It's logged and traced per call.
- **Privacy:** résumé text and the extraction reply never appear in logs or Langfuse. Job description text never appears in logs (traces only, as today).
- **Security:** user text goes in only as the user message (fenced as today, e.g. `<resume>`), never into the system prompt. Keys come only from config.
- **Dependencies:** each new package (expected: `langchain-core`, `langchain-google-genai`, Langfuse's LangChain integration if separate) is justified in the plan and supports Python 3.14.

## UX Requirements
- No visible change. Error responses (status codes, messages, SSE events) for interview start and résumé upload stay exactly as today.

## Constraints
- Python 3.14, `uv`; the callers and the eval tooling are synchronous today, and U3a doesn't make them async.
- LangChain 1.x moves fast (some pieces moved to `langchain-classic`). Import paths and the retry/streaming behavior are confirmed in a step 1 spike with tests, not assumed.
- Only these two tasks migrate. Decide, write, write-stream, feedback, the eval tooling for those tasks, the embedder and Deepgram stay on the current code.
- The user runs real-model evals (`--repeat 2`, same model as U0: `gemini-3.5-flash-lite`). Claude doesn't launch them.

## Blockers
- **Spike result for FR3** (assumption to verify): whether `.with_retry()` can respect Retry-After, the call's time budget and the U2 retry events. If not, the FR3 fallback applies (the U2 `RetryPolicy` owns retries).
- **Python 3.14 support** of `langchain-core`, `langchain-google-genai` and Langfuse's LangChain callback (assumption to verify before adding them).
- **`ChatGoogleGenerativeAI` with the current Gemini model and key** (assumption to verify): the native integration accepts the configured model name and the AI Studio key, reports token usage, and its thinking settings cover what `reasoning_effort` does today.
- **Structured output on Gemini** (assumption to verify): `.with_structured_output()` works with the profile schema on `gemini-3.5-flash-lite`, without schema features Gemini rejects.
- **JD summary baseline:** the user must run the new eval on the old code before the summary migrates.

## Edge Cases
- **EC1:** `LLM_PROVIDERS` empty (LLM off) -> no model is built; the summary is skipped (original text kept); résumé upload behaves exactly as today with no LLM.
- **EC2:** job description at or under `SUMMARY_THRESHOLD` -> no summary call, no trace generation, as today.
- **EC3:** the summary call times out, is rate-limited or gets a 5xx error after its retries -> the interview starts with the original job description; the log says `summary_failed:<LLMError class>`.
- **EC4:** the summary reply fails `validate_summary` (empty, too long, longer than the original) -> the original text is kept; the log says `summary_invalid:<reason>`.
- **EC5:** the vendor raises a rate-limit error with Retry-After -> it reaches our code as `LLMRateLimitError` carrying the Retry-After value, and no retry waits less than it.
- **EC6:** the vendor raises an exception `to_llm_error()` doesn't recognise -> it becomes a generic `LLMError`; the summary keeps the original text and extraction fails with its usual error; the log names the original class, never its message.
- **EC7:** the call's time budget is almost spent -> the call is cut off at the budget and surfaces as `LLMTimeoutError`; no retry starts after the budget runs out.
- **EC8:** a profile extraction reply is empty or doesn't match the schema on the first attempt and is valid on the second -> the profile is saved, and both calls are counted.
- **EC9:** both extraction attempts give invalid replies -> `ExtractionFailedError` with reason `invalid_reply:*` (or `empty_reply`); the upload returns today's extraction-failed response.
- **EC10:** extraction gets a valid reply with no skills and no roles -> `EmptyProfileError`; the upload returns today's empty-profile response; no further attempt.
- **EC11:** extraction gets a transport error that escapes the retries -> `ExtractionFailedError` named after the `LLMError` class; the upload returns today's extraction-failed response.
- **EC12:** a structured reply has fields longer than the caps, or duplicates -> trimmed and deduplicated as today; the saved profile respects every cap.
- **EC13:** the résumé or the job description contains instructions ("ignore the above...") -> the output doesn't follow them (the eval's injection case for the summary; the profile eval's existing cases).
- **EC14:** a profile extraction trace -> Langfuse stores the redacted placeholder for input and output; usage, latency, task and prompt version are still recorded.
- **EC15:** Langfuse is unreachable or not configured -> the call still runs and returns as today; tracing failures never fail the request.
- **EC16:** the model reports no token usage -> the call succeeds; usage is logged as unknown/zero, as the current layer does.

## Acceptance Criteria
- [ ] **AC1:** The factory builds a LangChain chat model from the existing config (Gemini through `ChatGoogleGenerativeAI`), returns no model when `LLM_PROVIDERS` is empty, and contains no hardcoded model names or keys.
- [ ] **AC2:** A test where the fake model raises a vendor rate-limit error shows it arriving as `LLMRateLimitError` with its Retry-After; similar tests cover timeout, server error, bad request, bad response and an unknown exception (generic `LLMError`).
- [ ] **AC3:** A test with an almost-spent time budget shows the call cut off at the budget, raising `LLMTimeoutError`, and no retry started after it.
- [ ] **AC4:** Tests show the U2 retry rules holding on the migrated calls: only timeout/429/5xx are retried, waits are never shorter than Retry-After, the retry count follows `llm_max_retries`, the SDK makes no retries of its own, and `retry_wait` / `retry_giveup` are logged with the caller's task. (If the FR3 fallback applies, the same tests run against the `RetryPolicy` path.)
- [ ] **AC5:** The contract test passes for every model the factory can build plus the fake model: text reply, structured reply, usage reported, errors mapped.
- [ ] **AC6:** The JD summary runs through a LangChain chain in `interviews/ai/`; `InterviewsService` no longer calls `LLMProvider` for it; EC2-EC4 behave as written (unit tests with the fake model).
- [ ] **AC7:** Profile extraction uses `.with_structured_output()`; EC8-EC12 behave as written; the upload's HTTP responses are unchanged (existing profile tests pass unchanged or with fake-model setup only).
- [ ] **AC8:** A test shows that profile extraction traces carry the redacted placeholder and never the résumé or the reply, and that the summary generation sits inside the `start-interview` trace with its `task` and `prompt_version` labels.
- [ ] **AC9:** The new JD summary eval exists (about 5-6 cases, including one injection case), scores the four checks in FR10, and its old-code baseline is in `docs/evals/baselines.md`.
- [ ] **AC10:** The user-run evals (2 repeats, same model) for the JD summary and the profile match their baselines within the noise margin. The comparison is written to `docs/evals/u3a-langchain-vs-baseline.md` and linked from `learnings.md`.
- [ ] **AC11:** `tests/test_layers.py` fails if a route, controller, service or repository imports `langchain*` (the rule starts being enforced now, not in U3c).
- [ ] **AC12:** `uv run pytest -q` and `uv run --with ruff ruff check app tests` pass; `graphify update .` has been run.
- [ ] **AC13:** `learnings.md` records the spike results (import paths, `.with_retry()` vs the U2 rules, streaming retry/fallback behavior for U3b), the dependencies added with their justification, and what LangChain hid or added compared with the hand-built layer.

## Out of Scope
- **Decide, write, write-stream, feedback:** U3b. They keep the current layer.
- **Embeddings, retrieval, ingestion splitters:** U3b.
- **Provider fallback chain, removing the question bank, deleting the old layer:** U3c.
- **Making the callers async:** not needed for these two tasks; the call layer stays synchronous.
- **Langfuse Prompt Management and template contracts:** U4.
- **A config switch back to the old path:** git and the evals are the rollback (decision FR11).
- **Retries for Deepgram and the embedder:** stay on the U2 `RetryPolicy`.
- **Changing the prompts:** same `.md` files and versions, so any score difference comes from the migration, not the prompt.
