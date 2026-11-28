# Implementation Plan: U3c — Fallback chain, question bank removal, old LLM layer deleted

## Overview
Make the LangChain chat model a provider chain (ordered from `LLM_PROVIDERS`), turn every "the LLM could not write the
question" case into one retryable 503 instead of a bank question, remove the bank and the "LLM off" modes, and delete the
old `LLMProvider` layer, ending with a layer test that confines LangChain to `core/ai` and feature `ai/` folders.

## Architecture & Design
A small `ChatChain` (ordered `(provider name, chat model)` pairs, built by the factory) is what `build_chat_model` returns
and services receive as `ChatModel`. The three call helpers (`complete_chat`, `complete_structured`, `stream_chat`) loop
over it inside the step `RetryPolicy` already retries, so every provider keeps our per-attempt rules (model copy with the
time left, token cap, error mapping, one Langfuse generation). A transport error (timeout, rate limit, server) moves to
the next provider at once; other errors raise; when every provider failed, `RetryPolicy` backs off and retries the whole
chain, so the worst case is (1 + max_retries) x providers calls per reply attempt. A stream is committed to the provider
that gave its first chunk. A turn whose question cannot be written ends in a new `InterviewerUnavailableError` (503,
`INTERVIEWER_UNAVAILABLE`) raised by the services before anything is saved, or sent as the SSE failed event after
`reset`. The bank and its fallbacks, the `source = bank` value, `bank_id` and the old layer are deleted.

## Approaches Considered
| Approach | Trade-offs | Chosen? |
|----------|-----------|---------|
| A. Explicit loop over a `ChatChain` in our helpers | ~30 lines per helper, exact control of the deadline, retry budget and which errors switch; the chain is testable with the existing fake chat model | **Yes** — user choice (grilling, 2026-11-28); fits the existing per-attempt rules (`chat.py`, `chat_stream.py`) |
| B. `model.with_fallbacks([...])` on the chat model | Loses `model_copy` per attempt, the per-attempt timeout and the retry policy; `with_structured_output` has to be rebuilt per branch | No — skips our rules |
| C. `.with_fallbacks()` over lazy `RunnableLambda`/`RunnableGenerator` branches | Keeps LangChain's first-chunk rule, but the wrappers recompute time, map errors and open streams, so they hide what `.with_fallbacks()` does | No — user chose A; the finding goes in `learnings.md` |
Spec deviation (approved by the answer above): the spec said "compose with `.with_fallbacks()`"; the plan builds the chain
by an explicit loop. The spec's Functional bullet is updated to match. A failed **decide** also fails the turn (user choice).

## Spec Requirements -> Implementation
- Chain, what switches, streams, time, provider in trace -> Step 1
- Startup refuses an empty list; off-modes removed -> Steps 2, 3
- Retryable error for start, blocking turn and stream -> Step 4
- Bank removed, old data migration, stored-question path stays -> Step 5
- Old layer deleted, `LLMError` family kept -> Step 6
- Layer test, note parser (R3) -> Step 7
- Evals, docs, gates -> Step 8

## Implementation Steps
Checkpoint interval: every 3 steps (after steps 3 and 6).

Every step ends with the gate commands (`uv run pytest`, `uv run --with ruff ruff check app tests`).

1. **Provider chain in the call helpers.** Add `ChatChain` (ordered named models; `as_chain()` accepts a bare model too, so
   the ~35 test files that pass `FakeChatModel` keep working); `ChatModel` becomes `BaseChatModel | ChatChain`. Loop over
   the chain in `_run` (blocking) and in `open_stream` (the retried step of the stream); switch only on `LLMTimeoutError`,
   `LLMRateLimitError`, `LLMServerError`; each provider gets a model copy with the time left; the first chunk commits the
   stream; add `provider` to `LLMResult` and to the generation metadata and the log line; log one `llm_provider_switch`
   event (from, to, reason; no text). Record the `.with_fallbacks()` finding in `learnings.md`.
   Files: new `app/core/ai/chat_chain.py`; `app/core/ai/chat.py`, `chat_stream.py`, `chat_tracing.py`, `tracing.py`
   (generation metadata), `provider.py` (`LLMResult.provider`, default None); `app/modules/interviews/ai/interviews_turn_log.py`
   (`log_result` adds provider); new `tests/core/ai/test_chat_chain.py`; `tests/core/ai/test_retry_budget.py` (chain case).
   Verify: `uv run pytest tests/core/ai -q` + gate. Test: first (seam: the three helpers with a `ChatChain` of fakes).
2. **Config and factory build every provider.** `Settings` refuses an empty or blank `LLM_PROVIDERS`; remove
   `llm_configured` and every "LLM disabled" branch; `build_chat_model` builds one model per entry (the `--model` override
   still replaces the primary's) and returns a `ChatChain`, never None; `main.py` lifespan and `get_chat_model` no longer
   allow None; test env sets a dummy Google provider; `.env.example` and the config test stay in sync.
   Files: `app/core/config.py`, `app/core/ai/factory.py`, `app/core/ai/dependencies.py`, `app/main.py`, `.env.example`,
   `tests/conftest.py` (env), `tests/core/test_config.py`, `tests/core/ai/test_chat_factory.py`.
   Verify: `uv run pytest tests/core -q` + gate. Test: first for Settings (seam: `Settings` from env); the factory wiring: after.
3. **Remove the "LLM off" modes from the modules.** `chat_model` is required everywhere (no `| None`): interviews,
   answer, feedback and profile services and their dependencies, retrieval (`llm_on` flag gone), the three eval entry points
   (`interviews_evals.py`, `interviews_rag_evals.py`, `profile_evals.py`). Delete the branches that only ran with the LLM
   off (feedback "503 when off", profile "unavailable", the answer service's `interviewer is None` path); keep the
   stored-question path (`stored_next`). Tests built with `chat_model=None` are deleted or given a fake chain.
   Files: `app/modules/interviews/services/{interviews_service,interviews_answer_service,interviews_feedback_service,interviews_retrieval_service}.py`,
   `app/modules/profile/services/profile_service.py`, the `*_dependencies.py` that take `ChatModel | None`, the three
   `tooling/*_evals.py`, and the tests that use them (find with `ctx_search` for `chat_model=None`, `llm_on`, `LLM_PROVIDERS`).
   Verify: `uv run pytest -q` + gate; `ctx_search` finds no `llm_configured`, "LLM disabled" or `llm_on`. Test: after.
   **Checkpoint 1.**
4. **A turn that cannot write ends in the retryable error.** Add `InterviewerUnavailableError` (503,
   `INTERVIEWER_UNAVAILABLE`, generic message) to `core/errors.py`. In `ai/`: a failed decide, a failed or unusable write
   (invalid twice, no time, input too long) and a failed follow-up all end the turn as failed (the outcome says so; the
   `fallback`/"bank" wording goes). In the services: `InterviewsService.start`, `AnswerService.answer` and `stream_answer`
   raise or yield the failed event (after any `reset`) before saving anything. Route `responses=` documents the 503.
   Files: `app/core/errors.py`, `app/modules/interviews/ai/{interviews_turn,interviews_turn_limits,interviews_turn_types,interviews_write,interviews_write_stream,interviews_turn_log}.py`,
   `services/{interviews_service,interviews_answer_service}.py`, `routes/interviews_route.py`, and their tests
   (`tests/modules/interviews/{ai,routes}/test_*`, e.g. `test_write.py`, `test_write_expired_deadline.py`, `test_start_llm.py`,
   `test_answer_stream.py`, `test_stream_turn.py`). Verify: `uv run pytest tests/modules/interviews -q` + gate.
   Test: first (seam: `AnswerService.answer`, `AnswerService.stream_answer`, `InterviewsService.start` with a fake chain:
   the error, the events, no rows written).
5. **Remove the bank and migrate old rows.** Delete `data/questions.json`, `BankQuestion`/`QuestionBank`, `load_bank`,
   `select_questions`, `pick_fallback_question`, `bank_question`, `get_bank`, the `bank` parameters, `used_bank_ids`,
   `NotEnoughQuestionsError`; setup validation uses the enums only. `QuestionSource.bank` becomes `stored`; drop the
   `bank_id` column from the model; new Alembic migration (rename rows `bank` -> `stored`, drop `bank_id`, set the
   column default to `llm`, a working downgrade). History, report and usage code read `stored` as "not LLM-written".
   Files: `app/modules/interviews/{utils/interviews_utils.py,utils/interviews_session_utils.py,schemas/interviews_schema.py,constants/interviews_constants.py,dependencies/models/interviews_model.py,dependencies/interviews_shared_dependencies.py,dependencies/interviews_start_dependencies.py,dependencies/interviews_answer_dependencies.py,tooling/interviews_report.py}`,
   `core/errors.py`, `alembic/versions/<new>_replace_bank_with_stored.py`, `tests/modules/interviews/utils/test_question_bank.py`
   (deleted) and every test or fixture using the bank (`conftest.py` `bank` fixture, `test_start_with_profile.py`, ...).
   Verify: `uv run pytest -q` + gate, then `uv run alembic upgrade head`, `downgrade -1`, `upgrade head` on the dev
   database (the user runs it; give the commands). Test: after (migration: run, not unit-tested).
6. **Delete the old layer.** Remove `LLMProvider` (keep `ChatMessage`, `LLMResult`, the `LLMError` family), `OpenAICompatibleProvider`
   (`openai_compatible.py`), `TracingProvider` (keep `Tracer`, `Generation`, `Step`, `ExperimentRun`, `build_tracer`),
   `FakeProvider` and `FakeStream` (keep the other fakes), `build_provider`. `json_reply.py` stays in `core/ai` (the profile feature uses it too; see Blockers & Resolutions). Remove `ProviderConfig.base_url`
   and `LLM_GOOGLE_BASE_URL` if nothing else reads them; fix the docstrings in `embedder.py` and `transcriber.py`.
   Delete or port the old-layer tests; port `FakeProvider` users to `FakeChatModel`. Remove the `openai` dependency
   (user-approved 2026-11-28) with `uv remove openai` once `ctx_search` shows nothing in `app` or `tests` imports it;
   if something still does, stop and report it instead of removing.
   Files: `app/core/ai/{provider,openai_compatible,tracing,fake,factory,json_reply,embedder,transcriber}.py`, `app/core/config.py`,
   `.env.example`, `pyproject.toml`, `uv.lock`, `app/modules/interviews/ai/interviews_reply.py`; tests: `tests/core/ai/{test_factory,test_openai_compatible_stream,test_tracing}.py`,
   `tests/live/test_openai_compatible_live.py`, `tests/modules/interviews/{conftest.py,ai/test_write_expired_deadline.py,ai/test_reference_note_context.py,ai/test_stream_turn.py,ai/test_streamed_reply.py,ai/test_context_prompts.py,ai/test_reply_contract.py,ai/test_feedback_hints.py}` and the others `ctx_search` finds.
   Verify: `uv run pytest -q` + gate; `ctx_search` for `LLMProvider|build_provider|FakeProvider|TracingProvider|OpenAICompatibleProvider|json_reply`
   in `app` and `tests` is empty (the string only in docs). Test: after. **Checkpoint 2.**
7. **Layer test and the note parser (R3).** New rule in `tests/test_layers.py`: any module under `app/` outside
   `app/core/ai/` and `app/modules/*/ai/` that imports `langchain*` or a vendor SDK is reported (replaces the four-folder
   check; `dependencies/`, `utils/`, `tooling/`, `core/` other than `core/ai` are covered), and `utils/` must not import `ai/`.
   Fix `interviews_knowledge_utils.py` (it imports `ai/interviews_split.py`): move the part that calls `split_sections` into
   `ai/`, or pass the splitter in from the service; take the smaller diff.
   Files: `tests/test_layers.py`, `app/modules/interviews/utils/interviews_knowledge_utils.py`, `app/modules/interviews/ai/interviews_split.py`
   (or a new `ai/` file), the knowledge service/tooling that calls it, and their tests.
   Verify: `uv run pytest tests/test_layers.py tests/modules/interviews -q` + gate. Test: first (seam: `check_layers` on synthetic sources).
8. **Evals, docs, final gates.** Give the user the eval commands; once run, write the comparison. Update the upgrade path
   (U3c result), the feature `task.md` and `learnings.md`, `docs/evals/baselines.md` only if a score moved on purpose, and
   run `graphify update .`.
   Files: `docs/evals/u3c-chain-vs-baseline.md`, `docs/ai-engineering-upgrade-path.md`, `docs/features/u3c-fallback-chain/{task,learnings}.md`.
   Verify: `uv run pytest` + `uv run --with ruff ruff check app tests` + `graphify update .`. Test: skip (docs and evals; the code is
   covered by the gate commands, and the evals are run by the user).

## Affected Files & Patterns
- Core: `app/core/ai/{chat,chat_stream,chat_chain (new),chat_tracing,tracing,provider,factory,fake,openai_compatible,json_reply,dependencies}.py`,
  `app/core/{config,errors}.py`, `app/main.py`.
- Interviews feature: `ai/` turn files (above), services (`interviews`, `answer`, `feedback`, `retrieval`), `utils/` bank code, `schemas`,
  `constants`, the model, `dependencies/`, `routes/interviews_route.py`, `tooling/`, `data/questions.json`.
- Profile: `services/profile_service.py`, `dependencies/profile_dependencies.py`, `tooling/profile_evals.py`.
- DB: new migration; `interview_questions.source` / `bank_id` (see the migration `51dfe1f2b1fd_add_question_source_and_usage.py` for the column).
- Reuse: `RetryPolicy` (`retry.py`), `to_llm_error` (`chat_errors.py`), `FakeChatModel`/`fake_chunks` (`chat_fake.py`, scripted errors before
  and after the first chunk), the `FeedbackUnavailableError`/`ProfileUnavailableError` pattern in `core/errors.py`, `TurnFailed`/`Reset` events.
- Risks: the worst-case call count multiplies by the provider count (pinned in `test_retry_budget.py`); removing `| None` touches many
  signatures and ~30 test files (bank fixtures, `chat_model=None`); the migration touches stored history; `ChatModel` becomes a union,
  so places that call model methods directly (e.g. `_tracer_of`, `model_copy`) must go through the chain.

## Testing Strategy
- Framework & command: `pytest` (`uv run pytest <path> -q`); LLM calls always on `FakeChatModel`; real-model runs are the user's.
- Gate commands: `uv run pytest`; `uv run --with ruff ruff check app tests` (not the whole repo: `alembic/` has 47 old errors);
  `tests/test_layers.py` runs inside pytest. After code changes: `graphify update .`.
- Coverage map:

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 1 | first | fake chain: first times out, second answers, log/trace name it |
| AC2 | 1, 4 | first | stream: failure after first chunk (no switch, `reset`, failed event), before first chunk (switch) |
| AC3 | 1, 4 | first | invalid reply never switches; the attempt loop then the retryable error |
| AC4 | 4 | first | start, blocking and streamed turn; no row created or changed |
| AC5 | 1 | first | scripted clock: second gets only the time left; none left -> no further provider |
| AC6 | 1 | first | `test_retry_budget.py` chain worst case (decide: (R+1) x reply attempts x providers) |
| AC7 | 2, 3 | first, after | Settings raises; `ctx_search` for `llm_configured`/"LLM disabled"/`llm_on` is empty |
| AC8 | 5 | after | `ctx_search` for bank names empty; setup validation test passes without a bank |
| AC9 | 5 | after | migration run up, down, up on a database (user runs); `stored` rows read in history/report tests |
| AC10 | 6 | after | `ctx_search` empty; `LLMError` family still imported by services |
| AC11 | 7 | first | `check_layers` reports a `langchain*` import in `utils/`, `dependencies/`, `tooling/`, `core/` (not `core/ai`) |
| AC12 | 8 | after | evals run by the user, comparison file written |
| AC13 | 8 | after | full pytest, ruff, `.env.example`/config test, `graphify update .`, a grep that logs hold no text |
| EC1, EC2 | 1 | first | timeout, rate limit and 5xx each switch |
| EC3 | 1, 4 | first | invalid reply: no switch; turn error after the limit; a failed decide also ends the turn (user choice) |
| EC4, EC11, EC12 | 4 | first | all providers down (one provider too); start creates no session |
| EC5, EC6 | 1, 4 | first | stream before/after the first chunk |
| EC7 | 1 | first | the deadline bounds the whole chain |
| EC8 | 4 | first | oversize input ends in the error, nothing saved |
| EC9, EC10 | 2 | first | empty/blank list, missing settings, unknown, duplicate |
| EC13, EC14 | 5 | after | `stored` rows; migration on an empty table |
| EC15 | 4 | first | summary/retrieval failure at start stays non-fatal (existing tests keep passing) |
| EC16 | 1 | first | worst-case attempts for the chain |

- Must verify, not assume: (1) `FakeChatModel` raising before vs after the first chunk gives the same `after_output` marking through the loop;
  (2) the test env can build the Google chat model with a dummy key without a network call; (3) the migration on a database that has
  `source = bank` rows with and without `bank_id`; (4) every old-layer test either ports to the chat model or is deleted with the code it tested.
- Seams (user-confirmed 2026-11-28): the three call helpers with a `ChatChain` of fakes; `Settings` from env; `AnswerService.answer`,
  `AnswerService.stream_answer`, `InterviewsService.start` with a fake chain; `check_layers` on synthetic sources.
- Open questions: none.
- Known baseline failures: flaky `tests/modules/profile/utils/test_profile_read_resume.py` (passes alone); pre-existing pyright errors
  in `interviews_feedback.py`, `interviews_report.py`, `profile_schema.py`; `ruff check .` on `alembic/` only.

## Blockers & Resolutions
- Step 6 findings (user-approved 2026-11-28): `json_reply.py` is used by the profile feature too, so it **stays in `core/ai`** (not moved into `interviews/ai/`; it is feature-agnostic, not part of the old layer). `FakeProvider`/`FakeStream` drive the shared `llm` test fixture (22 files), so they **move to `tests/provider_fakes.py`** instead of being ported to `FakeChatModel` (porting is a later cleanup); `app/` has no old layer left.
- Step 6: `LLM_GOOGLE_BASE_URL` is no longer read or required, but the setting stays accepted and ignored, because unknown `.env` keys are refused and the maintainer's `.env` still has the line. Delete it from `.env`, then the field in `config.py`.
- Chain mechanism -> explicit loop (user choice); `.with_fallbacks()` finding recorded in `learnings.md`.
- Failed decide -> fails the turn (user choice; the spec's EC3 now says so).
- Default `source` for new rows after the bank is gone -> `llm` (every new row is LLM-written).
- Switching on 4xx request errors (bad key) -> no: they raise at once, so a misconfigured primary is not hidden.
- When every provider failed -> the chain raises the last switchable error, so `RetryPolicy` keeps its Retry-After and backoff rules.
- Provider B real comparison -> out of scope (no second vendor); the chain is proven with fakes.

## Trade-offs & Rationale
- Loop in the helpers over `.with_fallbacks()`: the helpers already own timeouts, retries and tracing per attempt; bounded by the deadline.
- Union `ChatModel`: keeps the many fake-model tests and callers unchanged instead of a signature sweep.
- Services raise the 503 (`ai/` stays free of HTTP errors): matches `FeedbackUnavailableError` and keeps `ai/` returning outcomes.
- `stored` rename over dropping `source`: history stays truthful and `llm`-vs-other counts in reports keep working.

## Project Rules Applied
- `CLAUDE.md`: layers (route -> controller -> service -> repository), LangChain only in `core/ai` and feature `ai/`; structured errors from `core/errors.py`;
  migration for schema changes, never an applied one edited; UUID keys untouched; config from env with `.env.example` in sync; no hardcoded models; AI changes
  compared against baselines with the user running evals; never commit/stage; `graphify update .` after code.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| graphify / lean-ctx | importers of the old layer, bank footprint (~23 app files, ~28 test files), `test_layers.py` shape, `fallbacks.py` source check |
| grilling | chain mechanism, decide failure, seams, checkpoint interval (all answered) |
| ponytail | explicit loop and union type over new wrappers; no new dependency |
| llm-security | no vendor or prompt text in the error, logs or traces; generic message; request id only |

## Ready to Implement
- All spec requirements mapped to steps; every AC and EC mapped in the coverage table (none uncovered)
- Every step has a Test tag, exact files and a verification command; gate commands listed; checkpoints every 3 steps
- Approaches Considered filled; seams confirmed; blockers resolved
- Spec deviations (explicit loop instead of `.with_fallbacks()`; failed decide fails the turn) approved by the user and applied to the spec
