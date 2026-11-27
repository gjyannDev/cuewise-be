# Implementation Plan: U3b1 Interview calls on LangChain

## Overview
Move the interview's write, write-stream, decide and feedback calls onto the U3a LangChain call layer (plus a new async stream helper), one stage at a time, each stage proven by a user-run eval against the fresh baseline, so U3c can delete the old `LLMProvider` layer.

## Architecture & Design
- Each stage swaps one task's call from `llm.complete/stream` to `complete_chat` / `complete_structured` / `stream_chat`, building the prompt with `fixed_prompt(built.messages)` exactly as the U3a summary and profile code does. The reply loops (`ReplyAttempts`), parsers, logging helpers, fallbacks and SSE events do not change.
- **Transition wiring:** while stages are in flight, `Interviewer`, the answer service and the interviews service hold two things: `llm` (the old provider, for tasks not yet moved) and `chat_model` (`ChatModel | None`, from `get_chat_model`). Each task uses exactly one of them, and **a task falls back when its own model is None** (so a moved task checks `chat_model`, an unmoved one `llm`). The `llm` parameter disappears in step 19.
- **Structured output** (decide, score): schemas with every field required (nullable where "none" is valid), in one new module `interviews_model_schemas.py` (pattern: `ModelProfile` in `profile_reply.py`). The existing parsers still run on the reply text as a second check.
- **Async streaming:** a new `core/ai/chat_stream.py` with `stream_chat`: `astream()` under `RetryPolicy.acall`, retries only before the first chunk, errors mapped by `to_llm_error`, one generation via `ChatTrace`, `after_output` set on a failure after text. It yields text chunks, then the `LLMResult`, so `stream_draft` changes as little as possible.
- **Stream timeout (found in review):** the bundled SDK passes the model's `timeout` to `stream_generate_content` as one deadline for the whole call, so a plain `timeout=15` would cut a long question (breaking EC7). `stream_chat` therefore sets the vendor timeout to the time left in the turn and enforces the per-attempt `LLM_TIMEOUT_SECONDS` itself, on the **first chunk only**. The live spike (step 1) confirms this on the real endpoint.
- **Tests:** `FakeChatModel` gains streaming. The shared `llm` fixture routes one `FakeChatModel` subclass by system-prompt marker (decide, score, feedback write, **and the job-description summary**, which it must keep serving from `llm.summary`) and is **dual-backed** until write-stream moves: each `llm.script(...)` feeds both a chat-model fake (blocking route) and an old-style fake (streaming route). `llm.<name>.calls` stays a plain list (tests mostly use `len` and equality). The old halves are removed stage by stage.
- **Each code step carries the tests that call that function directly** (they break the moment its signature changes), so the gate stays green after every step.

## Approaches Considered
| Approach | Trade-offs | Chosen? |
|----------|-----------|---------|
| A. `stream_chat` helper on `astream` + `RetryPolicy.acall` | Keeps the U2 rules (first-chunk-only retries, Retry-After, budget) in one place; reuses `ChatTrace` and `to_llm_error` | **Yes**: settled in the spec (FR7, learnings: `.with_retry()` can't keep the U2 rules) |
| B. `.with_retry()` / `.with_fallbacks()` on the stream | Less code, but ignores streams / only switches before the first chunk, so the budget and Retry-After rules are lost | No |
| C. Wrap the chat model as an `LLMProvider` bridge | One cut-over, but the evals would measure the bridge and U3c would still have to remove it | No |
| D. Fixture: dual-backed script until stream moves | Keeps staged order; some temporary test code | **Yes**: user-confirmed in /create-plan |
| E. Fixture: move write and write-stream in one stage | Simpler fixture, but write becomes blocked by the stream spike and loses its own eval | No |
| F. v7_json/v8_json eval as a `--blocking` mode of generation | Reuses the 7 cases, scoring and Langfuse setup | **Yes**: user-confirmed |

## Spec Requirements -> Implementation
- FR1 (spike) -> step 1 (live test), step 11 (decision), step 20 (findings recorded)
- FR2 (streaming fake) -> step 2; FR3 (fixture) -> steps 3, 5, 8, 13, 16, 19
- FR4 (baselines + JSON eval) -> step 4 (baseline rows for write, stream, decide, feedback are already in `baselines.md`, 2 repeats)
- FR5 (write) -> steps 5-7; FR6 (decide) -> steps 8-10; FR7 (stream) -> steps 11-15; FR8 (feedback) -> steps 16-18
- FR9 (wiring) -> steps 5, 8, 13, 16, 19; FR10 (tracing/log parity) -> steps 5, 8, 12, 16
- FR11 (eval tooling) -> steps 4, 6, 9, 14, 17; FR12 (budget test) -> step 8; FR13 (staged order) -> the stage order of this plan

## Implementation Steps
Checkpoint interval: at each stage's eval (stops after steps 4, 7, 10, 15, 18). Between stops `/implement` runs on.

**Stage 0: pre-work (nothing moves yet)**
1. Spike (live part): the opt-in live test for `astream`: usage totals and finish reason (a stream's total must equal the blocking call's), failure before vs after the first chunk, a real timeout via a tiny timeout, and whether the call timeout bounds the whole stream — Files: `tests/live/test_chat_stream_live.py` — Verify: `uv run pytest tests/live/test_chat_stream_live.py --collect-only -q` (collects, skipped without the opt-in) + gate; **the user runs it** (command in the hand-off) — Test: after (real endpoint behavior)
2. Streaming `FakeChatModel`: scripted chunks, an error before the first chunk, an error after some chunks, a last chunk with usage or without — Files: `app/core/ai/chat_fake.py`, `tests/core/ai/test_chat_contract.py` — Verify: `uv run pytest tests/core/ai/test_chat_contract.py -q` + gate — Test: first (seam: `FakeChatModel.astream`; the contract test also runs streaming for every model the factory can build)
3. Dual-backed `llm` fixture: a `FakeChatModel` subclass routing by the decide, score, feedback-write **and summary** markers (everything else is the write script), `get_chat_model` overridden to it, every `script*` also feeding the old-style fake — Files: `tests/modules/interviews/conftest.py`, `tests/modules/interviews/test_llm_fixture.py` (new) — Verify: `uv run pytest tests/modules/interviews -q` (the whole existing interview suite unchanged, summary tests included) + gate — Test: after (test infrastructure; routing and dual-feeding checked in the new file)
4. `--blocking` mode on the generation eval (arms C -> `interviewer_v7_json`, D/E -> `interviewer_v8_json`, parsed with `parse_interviewer_reply`) on the old layer — Files: `app/modules/interviews/tooling/interviews_rag_evals.py`, `app/modules/interviews/tooling/interviews_evals.py` (flag), `tests/modules/interviews/tooling/test_rag_evals.py` — Verify: `uv run pytest tests/modules/interviews/tooling -q` + gate — Test: after. **Stop 1:** the user runs the stream spike (step 1) and the baseline (`--task generation --arms C,D --blocking --repeat 3 --pause-seconds 5 --model gemini-3.5-flash-lite --note "U3b1 baseline, old layer, blocking"`); Claude adds the rows to `docs/evals/baselines.md` and the spike findings to `learnings.md`.

**Stage 1: write (blocking)**
5. `write()` through `complete_chat`; `Interviewer`, the answer and interviews services and their dependencies take `chat_model` beside `llm`; the write half of the old-style fake stays only for the streaming route — Files: `app/modules/interviews/ai/interviews_write.py`, `interviews_turn.py`, `services/interviews_service.py`, `services/interviews_answer_service.py`, `dependencies/interviews_start_dependencies.py`, `dependencies/interviews_answer_dependencies.py`, `tests/modules/interviews/ai/test_write.py` (new), and the tests that call `write` or `Interviewer` directly: `ai/test_write_expired_deadline.py`, `ai/test_profile_redaction.py`, `ai/test_reference_note_context.py` — Verify: `uv run pytest -q` + gate — Test: first (seam: `write` with the fake chat model; EC1-EC3, EC10, EC13, repeat-question check, labels and usage on the generation)
6. Eval tooling for write and generation on the chat model: `run_case` and the generation writer call the same `ai/` functions; `main()` builds the chat model with `build_chat_model` (pattern: `profile_evals.py`) beside the provider — Files: `app/modules/interviews/tooling/interviews_evals.py`, `interviews_rag_evals.py`, `tests/modules/interviews/tooling/test_evals.py`, `test_rag_evals.py` — Verify: `uv run pytest tests/modules/interviews/tooling -q` + gate — Test: after
7. **Stop 2:** the user runs `--task write`, generation arms A,C,D and generation `--blocking` C,D, all `--repeat 3` (generation with `--pause-seconds 5`; split across days if the daily limit is hit); Claude compares and writes `docs/evals/u3b1-write-vs-baseline.md` — Verify: n/a (doc) — Test: skip (`uv run pytest -q` stays green)

**Stage 2: decide**
8. `ModelDecision` (required fields) and `decide()` through `complete_structured` + `parse_decision_reply(result.text)`; `decide` takes an optional `sleep` so tests don't wait; the old-style decide fake leaves the fixture; the budget test's decide cases are ported to the fake chat model and pin the same 6 calls (embedder and Deepgram cases stay) — Files: `app/modules/interviews/ai/interviews_model_schemas.py` (new), `interviews_decide.py`, `interviews_turn.py`, `tests/modules/interviews/conftest.py`, `tests/modules/interviews/ai/test_decide.py` (new), `tests/core/ai/test_retry_budget.py`, `ai/test_stream_turn.py` (its decide scripting only) — Verify: `uv run pytest -q` + gate — Test: first (seam: `decide`; EC2, EC3, EC10, EC14, never past `DECIDE_MAX_SECONDS`, and the worst-case 6 calls)
9. Eval tooling for decide: `run_decide_case` calls `decide` — Files: `app/modules/interviews/tooling/interviews_evals.py`, `tests/modules/interviews/tooling/test_evals.py` — Verify: `uv run pytest tests/modules/interviews/tooling -q` + gate — Test: after
10. **Stop 3:** the user runs `--task decide --repeat 3`; Claude compares (one case = 0.067) and writes `docs/evals/u3b1-decide-vs-baseline.md`, and notes what structured output did on decide for `learnings.md` — Verify: n/a (doc) — Test: skip (`uv run pytest -q` stays green)

**Stage 3: write-stream**
11. Precondition: the spike findings (Stop 1) meet FR1's conditions; if not, stop and re-decide — Files: `docs/features/u3b1-interview-calls/learnings.md` — Verify: n/a (decision recorded) — Test: skip (`uv run pytest -q` stays green)
12. `stream_chat` helper (vendor timeout = time left in the turn, first-chunk limit enforced by the helper) — Files: `app/core/ai/chat_stream.py` (new), `tests/core/ai/test_chat_stream.py` (new) — Verify: `uv run pytest tests/core/ai/test_chat_stream.py -q` + gate — Test: first (seam: `stream_chat` with the streaming fake; EC4, EC7 including a stream that runs past `LLM_TIMEOUT_SECONDS`, EC8, EC10, EC11, EC12, first-chunk-only retries, `after_output`, one generation with labels)
13. `stream_draft` / `stream_write` on `stream_chat`; `Interviewer.stream_turn` uses the chat model for decide and write; the last old-style halves leave the fixture; stream tests rewritten where they script `FakeStream` — Files: `app/modules/interviews/ai/interviews_write_stream.py`, `interviews_turn.py`, `tests/modules/interviews/conftest.py`, `tests/modules/interviews/ai/test_stream_turn.py`, `routes/test_answer_stream.py`, `controllers/test_stream_answer.py`, `routes/test_turn_budget.py` — Verify: `uv run pytest -q` + gate — Test: first (seam: `stream_write`; EC4-EC10, SSE events and order unchanged)
14. Eval tooling for stream: `run_stream_case` uses `stream_chat` — Files: `app/modules/interviews/tooling/interviews_evals.py`, `tests/modules/interviews/tooling/test_evals.py` — Verify: `uv run pytest tests/modules/interviews/tooling -q` + gate — Test: after
15. **Stop 4:** the user runs `--task stream --repeat 3`; Claude compares (time to first token vs baseline) and writes `docs/evals/u3b1-stream-vs-baseline.md` — Verify: n/a (doc) — Test: skip (`uv run pytest -q` stays green)

**Stage 4: feedback**
16. `ModelScore` schema (nested, required fields); `FeedbackGenerator.score` through `complete_structured` + `parse_score_reply`, `.write` through `complete_chat` + `parse_write_reply`; Tracer steps and checks unchanged; the service and dependency take `chat_model` — Files: `app/modules/interviews/ai/interviews_model_schemas.py`, `interviews_feedback_turn.py`, `services/interviews_feedback_service.py`, `dependencies/interviews_feedback_dependencies.py`, `tests/modules/interviews/conftest.py`, `routes/test_feedback_endpoint.py`, `ai/test_feedback_turn.py` (new) — Verify: `uv run pytest -q` + gate — Test: first (seams: `FeedbackGenerator.score` and `.write`; EC2, EC3, EC10, `retry_skipped:no_time`, template fallback, generations nest in their steps)
17. Eval tooling for feedback on the chat model — Files: `app/modules/interviews/tooling/interviews_feedback_evals.py`, `tests/modules/interviews/tooling/test_feedback_evals.py` — Verify: `uv run pytest tests/modules/interviews/tooling -q` + gate — Test: after
18. **Stop 5:** the user runs `--task feedback --repeat 3`; Claude compares content scores, not only validity, and writes `docs/evals/u3b1-feedback-vs-baseline.md` — Verify: n/a (doc) — Test: skip (`uv run pytest -q` stays green)

**Stage 5: wrap-up**
19. Remove the provider wiring: `get_llm_provider`, the `llm` parameters, `app.state.llm_provider` and the provider build and close in the lifespan; the evals' `main()` builds only the chat model; the dual-backed leftovers leave the fixture; the old classes stay — Files: `app/core/ai/dependencies.py`, `app/main.py`, `app/modules/interviews/dependencies/interviews_shared_dependencies.py`, `interviews_*_dependencies.py`, the three services, `interviews_turn.py`, `tooling/interviews_evals.py`, `interviews_rag_evals.py`, `interviews_feedback_evals.py`, `tests/modules/interviews/conftest.py` — Verify: `uv run pytest -q`, and a `ctx_search` for `LLMProvider|get_llm_provider|llm_provider` outside `app/core/ai/` finds nothing, then gate — Test: after
20. `learnings.md` (spike results, structured output on decide and score, what the second check caught, stream behavior vs old layer, before/after numbers, links to the four comparison files), upgrade-path progress, `graphify update .` — Files: `docs/features/u3b1-interview-calls/learnings.md`, `docs/ai-engineering-upgrade-path.md` — Verify: `uv run pytest -q` — Test: skip (docs; suite must stay green)

## Affected Files & Patterns
- Core: `app/core/ai/chat_fake.py` (streaming), new `chat_stream.py`, `dependencies.py`, `app/main.py`.
- Interview `ai/`: `interviews_write.py`, `interviews_decide.py`, `interviews_write_stream.py`, `interviews_feedback_turn.py`, `interviews_turn.py`, new `interviews_model_schemas.py`.
- Services and dependencies: the three interview services and four dependency modules listed in the steps.
- Tooling: `interviews_evals.py`, `interviews_rag_evals.py`, `interviews_feedback_evals.py`.
- Patterns to follow: `interviews_summary.py` and `profile_extract.py` (call-site shape), `ModelProfile` (required-field schema), `chat.py` helpers (`_run`, `_result`), `profile_evals.py` (building the chat model in an eval). The SDK already turns Gemini's cumulative stream usage into per-chunk differences, so merged chunks don't double count; the spike confirms the total.
- **Tests that call the moved functions directly and are rewritten with their step (EC17):** `test_write_expired_deadline.py`, `test_profile_redaction.py`, `test_reference_note_context.py` (step 5); `test_retry_budget.py`, `test_stream_turn.py` (steps 8, 13); `test_answer_stream.py`, `test_stream_answer.py`, `test_turn_budget.py` (step 13); `test_feedback_endpoint.py` (step 16); tooling `test_evals.py`, `test_rag_evals.py`, `test_feedback_evals.py` (steps 4, 6, 9, 14, 17). Route tests that only count calls keep working through the fixture's plain-list `.calls`; each stage's `task.md` records the final per-test list.
- Risks: the dual-backed fixture is temporary code (gone by step 19); a schema Gemini's JSON mode rejects (the score schema is nested); generations may nest differently under Tracer steps with the callback; generation eval noise is wide (0.18-0.28), so only a larger drop counts.

## Testing Strategy
- Framework & command: `uv run pytest -q` (pytest under `tests/`, mirroring `app/`); per step the narrower paths named in each step.
- Gate commands (after every step): `uv run pytest -q`, `uv run --with ruff ruff check app tests`; `graphify update .` at the end of each stage and in step 20. `tests/test_layers.py` runs inside pytest (LangChain imports only in `app/core/ai/` and the feature `ai/` folders).
- Seams (user-confirmed): `FakeChatModel.astream`, `stream_chat`, `write`, `decide`, `stream_write`, `FeedbackGenerator.score` and `.write`; the HTTP routes keep their behavior tests. No test targets a private helper.
- Coverage map:

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 1, 11, 20 | after | live test run by the user; findings in `learnings.md` |
| AC2 | 2 | first | contract test covers streaming for every buildable model |
| AC3 | 3, 5, 8, 13, 16 | after | rewrites listed above |
| AC4 | 4 | after | four baselines already recorded (2 repeats); JSON eval baseline at Stop 1 |
| AC5 | 5 | first | EC1-EC3, EC10, EC13 |
| AC6 | 8 | first | EC2, EC3, EC10, EC14 |
| AC7 | 12, 13 | first | EC4-EC8, EC10, EC12; existing stream tests keep assertions |
| AC8 | 16 | first | EC2, EC3, EC10 |
| AC9 | 8 | first | pins 6 calls |
| AC10 | 5, 8, 12, 16 | first | labels, usage, nesting, log text, no raw text in logs |
| AC11 | 19 | after | search plus `tests/test_layers.py` |
| AC12 | 4, 6, 9, 14, 17 | after | |
| AC13 | 7, 10, 15, 18 | after | user-run evals, Claude writes the files |
| AC14 | every step | first/after/skip | gate commands |
| AC15 | 20 | skip | doc |
| EC1 | 5, 8, 16 | first | |
| EC2, EC3 | 5, 8, 16 | first | |
| EC4-EC8 | 12, 13 | first | EC9 keeps its existing test (decide in a worker thread, step 13) |
| EC10 | 5, 8, 12, 16 | first | |
| EC11, EC12 | 12 | first | EC11's U3a coverage reused for non-stream calls |
| EC13 | 5, 8, 16 | first | |
| EC14 | 8 | first | |
| EC15 | 12, 16 | first | |
| EC16 | 7, 10, 15, 18 | after | one extra run on a one-case drop |
| EC17 | 3, 5, 8, 13, 16 | after | |

- Must verify, not assume (real endpoint): usage and finish reason on a stream's last chunk and that merged usage equals the blocking call's; failure before vs after the first chunk; a real timeout arriving as `DeadlineExceeded`; that the call timeout is one deadline for the whole stream (the SDK source says so); Gemini taking the nested score schema (content scores must hold, not only validity); generations nesting under feedback steps in Langfuse.
- Open questions: none (every EC has a stated outcome).
- Known baseline failures: none seen (U3a final suite: 2706 passed; one known flaky test passes on re-run).

## Blockers & Resolutions
- Stream spike conditions fail -> write-stream (stage 3) stops and is re-decided; stages 1, 2 and 4 are unaffected.
- Spec asked 3 repeats for the fresh baselines; the user ran **2** for write, stream, decide and feedback (noise margin is one case, so 2 is enough to judge) and 4 for generation arms A, C, D. Post-migration stage runs use 3 repeats. Deviation accepted and noted in `baselines.md`.
- Daily request limit on the free tier was hit during baselines -> stage evals are given one at a time; generation uses arms A,C,D with `--pause-seconds 5`, and a run may be split across days (Stop 2 is the heaviest).
- `v7_json`/`v8_json` baseline -> built in step 4 on the old layer, run at Stop 1.
- The fixture serves write and write-stream from one script -> dual-backed until step 13.

## Trade-offs & Rationale
- Two params (`llm`, `chat_model`) on `Interviewer` during the transition: more wiring for four stages, but each task is on exactly one layer and every eval measures the real new path.
- A required-field schema plus the lenient parser as second check: the schema makes Gemini answer in shape (U3a profile lesson); the parser keeps the note and gap rules in one home.
- No whole-stream cap, with the helper (not the vendor) limiting the first chunk: matches today and the spec, and doesn't depend on how gRPC counts its deadline.

## Project Rules Applied
- `CLAUDE.md` AI Engineering Guidelines -> LangChain only in `core/ai/` and feature `ai/` folders; vendor errors mapped to `LLMError`; compare each stage with the baseline and write `docs/evals/u3b1-<task>-vs-baseline.md`; mock the LLM in unit tests; no new dependency; prompts unchanged.
- `CLAUDE.md` Git Rules -> nothing is committed, staged or pushed by Claude; commit commands are given per stage on request.
- Standing rule: the user runs every real-model eval and the opt-in live test; Claude gives the commands and compares in Langfuse.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx / graphify | affected files, call sites, tests that call the moved functions |
| grilling | fixture transition, JSON eval shape, live spike, seams, checkpoints |
| ponytail | no bridge, no new dependency, one new core module only |
| tdd (seams section) | seams named and user-confirmed |
| security-review | not run: no new auth, data or permission surface; logging rules carried by AC10 |

## Ready to Implement
- All spec requirements mapped to steps
- Every step has a Test tag; every AC and EC mapped in Testing Strategy, none uncovered
- Gate commands listed; every step names files and a verification command; every code step carries its direct-caller tests so the gate stays green
- Approaches Considered filled; checkpoint interval set (stage evals)
- Blockers resolved or carried; one accepted deviation (2 repeats for the four baselines)
