# Implementation Plan: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)

## Overview
Add answering to the interviews module: a candidate submits an answer, the API saves it, advances the session, asks an LLM (behind a provider interface) for a short reaction, and returns the reaction plus the next question; a transcript endpoint redraws the conversation after a reload. The interview must never break because of the LLM.

## Architecture & Design
Two layers of new code. (1) `app/core/ai/`: a provider interface, an OpenRouter implementation on plain `httpx` (timeout, retry with backoff and jitter, total budget), a fake for tests, and a factory that returns no provider when no key is configured. (2) The interviews module: `current_position` and a `completed` status on the session, an `interview_messages` table, an `answer` flow in the controller, a pure transcript builder shared by the LLM history and the transcript endpoint, and a versioned prompt file.

The answer flow is built around three rules. **Guard with compare-and-swap:** advancing the session is one conditional update (only if the session is `in_progress` and still at the expected position); zero rows updated means `QUESTION_NOT_CURRENT`. That makes double-submit deterministic and testable on SQLite, and the unique (question, role) index is only a backstop. **Short write, slow call, short write:** read everything the LLM call needs and turn it into plain values first, commit the answer and the advance, call the LLM with no transaction open, then commit the reaction. Reading ORM attributes after a commit re-opens a transaction (default expire-on-commit), so the prompt is assembled from plain values before the first commit. **Fallback is a value, not an error:** any provider failure or unusable reply becomes `reaction = None`; only a database failure surfaces as 500.

## Spec Requirements -> Implementation
- Permission `interviews:answer`, `completed` status, constants, two 409 errors -> Step 1
- Settings, key+model together, `.env.example` -> Step 2
- Provider interface, OpenRouter with retries/budget, fake, factory -> Step 3
- `current_position`, `interview_messages` (usage columns), migration -> Step 4
- Versioned prompt, transcript builder, LLM message builder -> Step 5
- `POST /interviews/{id}/messages` state machine, `GET` changes -> Steps 6, 7
- LLM call outside a transaction, history, fallback, metadata -> Step 8
- One `app.llm` log line per call, no content in logs -> Step 9
- `GET /interviews/{id}/messages` transcript (approved spec addition) -> Step 10
- Real-API verification, final learnings numbers -> Step 11
- Learning log (`learnings.md`, kept alongside `task.md` from the first step) -> Learning Log section, updated in every step it names
- Lint, full test run, graph update, architecture checks -> Step 12

## Implementation Steps
1. **Wiring and permission.** In `auth_constants.py` add `Permission.interviews_answer` to the interview permission set for both roles. In `interviews_constants.py` add `SessionStatus.completed`, `MAX_ANSWER_LENGTH` (2000), `MessageRole` (candidate, interviewer), `MessageKind` (question, answer, reaction) and the prompt version constant. In `core/errors.py` add `SessionNotInProgressError` and `QuestionNotCurrentError` (ConflictError subclasses, as `NotEnoughQuestionsError`). Declare `httpx` in `pyproject.toml`. Update `tests/modules/auth/test_me.py`. — Test: first for the permission (seam: `permissions_for` and `/auth/me`); the rest skip.
2. **Settings.** In `core/config.py` add `openrouter_api_key` (secret, optional), `llm_base_url`, `llm_model` (optional), `llm_timeout_seconds` (15), `llm_max_retries` (2), `llm_total_budget_seconds` (30), `llm_max_tokens` (150), with a validator: key and model set together or both unset. Add them to `.env.example`. — Test: first. Seam: `Settings` built with the env file disabled. Slices: defaults; both set; both unset; only one set raises (EC19); the key is not in the repr.
3. **Provider package `app/core/ai/`.** `provider.py` holds the chat message type, `LLMResult` (text, model, prompt/completion tokens, latency, finish reason, attempts), the error hierarchy (timeout, rate limit, server, non-retryable, bad response; each carries attempts) and the provider protocol. `openrouter.py` holds the real client with a constructor that accepts an injected transport, sleep and clock so tests never wait. `complete` also takes an optional `temperature` (provider default when omitted) so the learning experiments can compare values; the app itself never sets it. `fake.py` returns scripted text or raises scripted errors, records every call, and exposes a hook run at call time. `factory.py` builds the provider from settings, or returns none and logs one warning; `main.py` calls it at startup. — Test: first. Seam: `OpenRouterProvider.complete` with a mock transport. Slices in order: success parse (reply, model, tokens, finish reason, request body has model, messages and `max_tokens`, bearer header); missing `usage` gives None counts (EC17); length finish reason passes through (EC16); blank or malformed body raises a bad-response error with no retry (EC15); 429 then success reports attempts 2 (EC13); 5xx or timeout on every attempt raises after the configured retries (EC11); 400/401/403 not retried (EC12); budget exhausted stops further retries (EC14); a slow-but-successful call is unremarkable (EC24).
4. **Data model and migration.** In `interviews_model.py` add `current_position` (default 1) to the session and an `InterviewMessage` model (UUID key, FK to session with cascade, FK to question, role, content, created_at, nullable model/prompt_version/prompt_tokens/completion_tokens/latency_ms, unique on question and role). Generate the Alembic revision after the existing interviews one, review it by hand, and check the model is registered where `app/db/models.py` imports models. — Test: after (model via `create_all` in every test; migration up/down on dev Postgres with existing sessions).
5. **Prompt and pure helpers.** Add `prompts/reaction_v1.md` in the interviews module (persona, reply rules from the spec; placeholders for role and level only). In `interviews_utils.py` add: load and render the system prompt; `build_transcript` (questions up to the current one plus messages, flat, in order); `build_llm_messages` (system prompt, strictly alternating assistant and user turns where a reaction and the next question share one assistant turn, ending with the new answer). — Test: first. Seam: `build_llm_messages` (and `build_transcript` through Step 10). Slices: single question; two questions with a reaction; a missing reaction still alternates (EC26); system prompt carries role and level but never the job description; candidate text appears only in user turns, including an injection-style answer (EC23).
6. **Answer endpoint: state machine, no LLM yet.** Schemas (`AnswerIn` with `extra="forbid"`, trimmed 1-2000 chars, `question_id` UUID; `ReactionOut`; `AnswerOut`; nullable `current_question` on `InterviewOut`). Repository: the compare-and-swap advance (two variants, normal and last-question-completes) plus the candidate insert in one commit. Controller `answer`; route `POST /{session_id}/messages` (201, `interviews:answer`); `get` returns the question at `current_position` or none when completed. Dependency `get_llm_provider` returns the factory result, none in tests. — Test: first. Seam: `POST` and `GET /api/v1/interviews/...`. Slices: non-last answer (201, row saved, position +1, next question, no `bank_id`, reaction null); last answer completes and the user can start again (EC20); no provider configured still completes a full interview (EC18, AC4); `GET` after answering and on completed or abandoned sessions (EC25).
7. **Answer endpoint: guards.** Error responses and checks in the order from the spec; `responses=` documents 401/403/404/409/422. — Test: first. Seam: `POST`. Slices: no or bad token (EC1); lacking permission (EC2); missing and foreign session give identical 404 and nothing saved (EC3); bad UUIDs, blank, over-limit and exactly-2000 answers, unknown fields (EC4-EC7); abandoned and completed sessions (EC8); stale, future, foreign and random `question_id` all give the same 409 (EC9); second submit for the same question gives 409 and one stored answer (EC10); forced DB failure while saving the answer persists nothing and the provider is never called (EC21); OpenAPI lists the documented responses (AC20).
8. **Answer endpoint: LLM in the flow.** Controller assembles the messages as plain values before committing, calls the provider with no open transaction, then saves the reaction row with model, prompt version, tokens and latency; any provider error or blank text gives `reaction` none and no row. Provider usage fields stay out of responses. — Test: first. Seam: `POST` with the fake provider override. Slices: reaction returned and stored with metadata (AC14); history on turn 3 is longer than turn 1 and ends with the new answer (AC9); injection-style answer only in user turns (EC23, AC10); scripted timeout, 5xx, 4xx, blank text all give 201 with null reaction and the interview advanced (EC11, EC12, EC15); retry-then-success reply returned (EC13); missing usage stored as nulls (EC17); the fake's hook asserts the session is not in a transaction at call time; forced DB failure while saving the reaction gives 500 with the answer and advance kept (EC22).
9. **Usage logging.** Controller logs exactly one `app.llm` line per call with session id, model, prompt version, tokens, latency, attempts, finish reason, outcome; warning on failure, error on non-retryable. No content or key anywhere. — Test: first. Seam: `POST` plus the existing `app_logs` fixture. Slices: success line has every field; failure levels (EC11, EC12); length finish reason logged (EC16); no answer, reaction, job description or key text in any record (AC15).
10. **Transcript endpoint.** Schema `TranscriptOut` with flat items; repository lists questions up to the current one and messages; controller reuses `build_transcript`; route `GET /{session_id}/messages` (200, `interviews:read_self`). — Test: first. Seam: `GET /api/v1/interviews/{id}/messages`. Slices: fresh session has only question 1 (EC27); answered turns in order; missing reaction has no item (EC28); never a later question or `bank_id` or usage fields (AC25); completed shows all, abandoned stops at its position (EC30); 404/422/401/403 behavior and OpenAPI responses (EC29, AC24).
11. **Live verification and learnings.** Opt-in pytest test (skipped unless an explicit env flag and a key are set) doing one real call through `OpenRouterProvider`; manual runs against real OpenRouter and Postgres; run the experiments listed in the Learning Log with a throwaway script (not committed) and finish `learnings.md` with the measured values and the Proof answers. — Test: after.
12. **Finish.** `uv run ruff check . && uv run ruff format .`, full `uv run pytest`, search that `httpx` is imported only in `openrouter.py` and that no model name, key or URL is hardcoded outside settings defaults, then `graphify update .`. — Test: skip.

## Learning Log (`learnings.md`)
This is a learning project, so `docs/features/interviewer-reaction/learnings.md` is a deliverable of its own, not an afterthought. `/implement` creates it at the start next to `task.md`, with one section per checkpoint below. Each checkpoint has four parts: **Predict** (written by you, in your own words, before the step starts), **Observed** (real output, numbers or log lines from the running code, filled in while building), **Why** (a short explanation of the concept, drafted together), and **Proof** (the question from the learning path, answered by you in your own words). A step is not done in `task.md` until its checkpoint is written. Claude leaves the Predict and Proof parts for you; it only fills Observed from real runs. The file name matches AC21 and `docs/ai-engineering-learning-path.md`.

| After step | Concept (learning path) | Predict before | Observe and record |
|-----------|-------------------------|----------------|--------------------|
| 3 | 6 Reliability; 1 How a call works | Which failures deserve a retry, and which never? What does the raw request look like? | The redacted request and response body (`messages`, `usage`, `finish_reason`); behavior per failure type from the mock-transport tests |
| 5 | 1 Stateless calls; 2 Context; 3 Prompts as data; 8 Injection baseline | How many messages are sent on turn 3? Where does the candidate's text go and why? | The message list for turn 1 vs turn 3 (count and characters); the rendered system prompt |
| 6, 7 | 5 Code decides, LLM comments | What happens on a double-click, and who decides the interview moves on? | The 409 response for a stale submit; where in code the progression rule lives |
| 8 | 1, 2 Context cost; 6 Fallback | Will the user notice when the LLM is down? What does turn 3 cost compared to turn 1? | Prompt tokens per turn from stored rows; behavior with a wrong key or a tiny timeout |
| 9 | 9 Observability and cost | What should one log line tell you? What must never be in it? | Real `app.llm` lines; the query that sums tokens per session |
| 10 | 2 Context vs what the user sees | Is the transcript the same as what the model receives? | The two outputs side by side from the same session |
| 11 | 1, 2, 6, 9 (Proof round) | Your estimate of the cost of one full interview | Experiments: prompt tokens on turn 1 vs last turn; same answer five times at two temperatures; `max_tokens` very small and the cut-off reply; token total and cost for one full interview |

## Affected Files & Patterns
- New: `app/core/ai/{provider,openrouter,fake,factory}.py` (+ `__init__.py`), `app/modules/interviews/prompts/reaction_v1.md`, one Alembic revision, test files under `tests/core/ai/` and `tests/modules/interviews/`, the opt-in live test, `learnings.md`.
- Changed: `core/config.py`, `core/errors.py`, `main.py` (startup provider check), `auth_constants.py`, `interviews_{constants,model,schema,repository,controller,route,dependencies,utils}.py`, `tests/modules/interviews/conftest.py` (fake provider override, answer helper), `tests/modules/auth/test_me.py`, `.env.example`, `pyproject.toml`/`uv.lock`.
- Patterns to follow: ConflictError subclasses with a distinct `code` (`NotEnoughQuestionsError`); dependency override for an external source (`get_bank` fixture, now `get_llm_provider`); repository owns commit/rollback (`start`); module-load constants for loaded data (`QUESTION_BANK`); `app_logs` fixture for log assertions; ownership via `get_for_user` returning none.
- Risks: reading ORM attributes after a commit silently re-opens a transaction (Step 8 test guards it); the sync retry sleeps hold a worker thread for up to the budget (acceptable now, revisited in Slice 4); SQLite cannot show real lock waiting, so the concurrent case is checked on Postgres by hand; adding `current_position` to existing rows relies on the server default.

## Testing Strategy
- Framework & command: pytest on in-memory SQLite via existing fixtures; `uv run pytest tests/core tests/modules/interviews` while working, full `uv run pytest` and `uv run ruff check .` at the end. No automated test uses the network: the provider is tested through `httpx` mock transport, the endpoints through the fake provider.
- Test seams (user-confirmed): `POST` and `GET /api/v1/interviews/{id}/messages`, `GET /api/v1/interviews/{id}`, `OpenRouterProvider.complete`, `build_llm_messages`, `Settings` validation, `permissions_for` + `/auth/me`. Concurrency: deterministic (stale `question_id` and the compare-and-swap guard, plus a direct duplicate-insert check of the backstop index); real race checked manually on Postgres.

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1 | 4, 11 | after | migration up/down on dev Postgres with existing sessions |
| AC2, AC3, AC4 | 6 | first | state machine; full N-question interview |
| AC5, EC4-EC7 | 7 | first | 422 variants, 2000 ok, trimming |
| AC6, EC1, EC2, EC3 | 1, 7 | first | permission map, `/auth/me`, 401/403, identical 404 |
| AC7, EC8, EC9 | 7 | first | both 409 codes; no save, zero provider calls |
| AC8, EC10 | 7 | first | stale submit; one answer stored; Postgres race manual (Step 11) |
| AC9, EC26 | 5, 8 | first | recorded messages; alternation with a missing reaction |
| AC10, EC23 | 5, 8 | first | candidate text only in user turns; no job description |
| AC11, EC11, EC12, EC15 | 3, 8 | first | scripted failures give 201 and null reaction |
| AC12, EC13, EC14, EC24 | 3 | first | retry rules via mock transport and injected sleep |
| AC13 | 3, 8, 12 | first / skip | interface used by controller; import search in Step 12 |
| AC14, EC17 | 3, 8 | first | metadata stored; nulls when usage absent |
| AC15, EC16 | 3, 9 | first | one line per call; no content or key in logs |
| AC16, EC18, EC19 | 2, 6, 12 | first | settings rules; no provider path; hardcode search |
| AC17, EC25 | 6 | first | `GET` returns current question, none when completed |
| AC18, EC21, EC22 | 7, 8 | first | forced DB failures at both write points |
| AC19 | 11 | after | live call confirms response-shape assumptions |
| AC20 | 7, 10 | first | OpenAPI response documentation |
| AC21 | 11 | after | measured numbers from a real run |
| AC22 | 1, 12 | first / skip | updated `test_me`; full pytest and ruff |
| EC20 | 6 | first | last answer: reaction path plus completed |
| AC23, AC24, AC25, EC27-EC30 | 10 | first | transcript contents, order, access, no leakage |
| EC28 | 8, 10 | first | missing reaction yields no item |

- Must verify, not assume: OpenRouter response shape (`choices[0].message.content`, `finish_reason`, `usage`) and that 401/403 means bad key (Step 11); migration on real Postgres including existing rows; the concurrent double-submit on Postgres; the app refusing to start with only one of key/model set (also covered by the settings test); that no transaction is open during the call under the real session setup.
- Open questions: none; every EC has a stated outcome. EC22 (a lost reaction on a database failure) is accepted by the spec.
- Known baseline failures: none seen (tests not run during planning).

## Blockers & Resolutions
- OpenRouter key and model id needed only for Step 11 -> owner supplies them via env; automated work needs neither.
- Reload gap (no history) -> resolved by Step 10; spec updated with AC23-AC25 and EC27-EC30 after approval.
- Double-submit and race (EC10) -> compare-and-swap advance plus unique backstop.
- LLM failure (EC11-EC15) -> fallback to null reaction; interview never blocks.
- Transaction held during a slow call -> plain-value prompt assembly before commit, plus a fake-provider assertion.
- Rate limiting -> deferred by the owner; exposure stays in the spec's Out of Scope.

## Trade-offs & Rationale
- Plain `httpx`, no SDK: shows the real request and the retry code, which is the learning goal; no new package (already installed via `fastapi[standard]`).
- Sync call inside a sync route: matches the codebase today; Slice 4 moves to async when streaming needs it.
- Fake provider in `app/core/ai/fake.py`: simple import, same override pattern as the question bank; the cost is a small test double inside the package.
- Compare-and-swap over locking reads: works the same on SQLite and Postgres, needs no row lock, and the failing case is a plain zero-row result.
- A reaction and the following question share one assistant turn in the LLM history: keeps roles strictly alternating, which providers handle most predictably.
- Transcript not paginated: bounded at 30 items by the 10-question cap; a documented exception to the paginate-lists rule.
- `LLMResult.attempts` is an addition to the spec's field list, needed for the log line and the retry tests. The optional `temperature` argument on `complete` is also additive, needed only for the temperature experiment.
- (Implementation) `LLMError` also carries `attempts` and `latency_ms`, so failure log lines report them; the failure line logs `model=-` because a failed call has no response model.
- (Implementation) Transcript `question` items have `created_at: null`: questions are stored at session start, so no honest "shown at" time exists. Spec updated.
- (Implementation) New code is formatted with `ruff format --line-length 120` to match the existing code (the repo has no ruff config; the default 88 columns would reformat 37 untouched files).
- `learnings.md` is written step by step, with you writing the predictions and the Proof answers: it costs a little time per step, but it is the point of the project, and answers written afterwards from memory lose the real numbers.
- No retry on malformed replies: a bad body is not a transient fault, and one retry would double cost for no gain.

## Project Rules Applied
- `CLAUDE.md` layers: routes thin, controller orchestrates, repository owns SQL and commit/rollback; files prefixed `interviews_`.
- `CLAUDE.md` AI guidelines: provider abstraction in `core/ai/`, prompts as a versioned file, tests mock the LLM, real-model test opt-in, no raw content in logs, timeouts/retries/token cap/usage logging, candidate text kept out of the system prompt.
- `CLAUDE.md` security and data: UUID keys via `UUIDPrimaryKeyMixin`, Pydantic `extra="forbid"`, ownership in the controller, structured errors, secrets only from env, Alembic only, no commits or pushes.
- Spec decisions are inherited from `docs/features/interviewer-reaction/spec.md`; learning goals from `docs/ai-engineering-learning-path.md`.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| graphify | `graphify query` on settings, errors, logging and interviews code paths; confirmed module layout |
| lean-ctx | read interviews module, permissions, error handlers, test fixtures, logging; found reusable patterns |
| grill-me (via AskUserQuestion) | approved the transcript endpoint, flat shape, test seams, fake provider location |
| tdd | seams only; no loop run during planning |
| ponytail | applied inline: no SDK, no new package, no DB-backed limiter, no abstraction beyond the mandated interface |
| security-review | not invoked (it reviews a pending diff); run it after Step 12. Surface noted: untrusted answer text, PII to a third party, API key handling |

## Ready to Implement
- All spec requirements (including AC23-AC25, EC27-EC30) mapped to steps
- Every step has a Test tag; every AC and EC appears in the coverage map
- Affected files identified; blockers resolved or owned
- `learnings.md` is created at the start with the checkpoints from the Learning Log and updated in the steps it names
- One approved deviation from the original spec: the transcript endpoint (spec updated); one additive field, `LLMResult.attempts`
