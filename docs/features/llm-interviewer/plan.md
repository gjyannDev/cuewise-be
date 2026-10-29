# Implementation Plan: LLM as the Interviewer (it asks the questions)

## Overview
Replace the question bank as the primary question source: on start and on every non-final answer, one LLM call returns the next question as validated JSON; the bank is only the fallback. The LLM-written reaction is replaced by a short predefined one picked from constant pools (no LLM, no tokens). The final answer completes the session with no LLM call.

## Architecture & Design
A **turn engine** inside the controller produces "the next question" for a session: it builds the messages from plain values, calls the provider (at most two attempts inside one shared time budget), validates the reply with a pure contract (`interviews_reply.py`), and falls back to a pure bank picker when the LLM is off, fails, or stays invalid. Start and answer both call it; neither knows how the question was produced beyond its source tag.

**Ordering decision (user-confirmed): call first, then one atomic save.** On an answer: do all reads, capture them as plain values, release the read transaction, run the engine (no transaction open), then one short transaction does the compare-and-swap advance, inserts the answer, the predefined reaction and the new question; zero rows updated means 409 and nothing is saved. On start the LLM call happens before the transaction that abandons the previous session and inserts the session with question 1. Consequences accepted: a crash mid-call saves nothing (the client resubmits); two simultaneous submits can both call the LLM, one wins, the loser's call is wasted.

Other design points: (1) the engine's total LLM time per turn is capped by passing each call only the remaining budget (a new optional provider argument, an injected clock makes this testable); (2) a call that fails or returns no usable text goes straight to the fallback, only an invalid-but-present reply earns one retry; (3) one `app.llm` line per call with outcome `ok`, `invalid_reply` or the error class, and the failure line carries the finish reason; (4) turn usage (tokens summed over its calls) is stored on the question row; (5) prompt templates use `{{name}}` placeholders replaced in one pass, because the prompt now contains literal JSON braces; (6) the job description travels in the first user message inside a delimited block with the closing delimiter neutralised; (7) legacy sessions (next question already stored) advance with no LLM call; (8) the reaction is a pure pick from constant pools, chosen before the save from plain values (the answered question's category, the level group, the previous reaction text) and stored with the turn, so it costs no tokens and works with the LLM off.

## Spec Requirements -> Implementation
- Token default 800, finish reason on failed calls, per-turn budget argument -> Step 1
- Question source and usage fields, optional bank id, migration -> Step 2
- Reply contract and invalid-reply rules (JSON, fence, category, repeat) -> Step 3
- Versioned prompt, delimited job description, message building, remove reaction prompt -> Step 4
- Bank fallback with mixed alternation and the predefined reaction picker (pools in constants) -> Step 5
- Start with LLM-asked first question, engine, retry/budget, logging, usage -> Step 6
- Answer: final, legacy, atomic turn with the predefined reaction stored and returned -> Step 7
- Transcript check (reactions appear after a reload, legacy reactions kept) -> Step 8
- Evals (cases + runner) -> Step 9
- Real-model verification, learnings numbers -> Step 10
- Lint, full suite, architecture checks, graph -> Step 11
- Learning log (`learnings.md`, created at the start of `/implement`) -> Learning Log section

## Implementation Steps
1. **Settings and provider additions.** `LLM_MAX_TOKENS` default 800 plus a comment in `.env.example` (update the existing default assertion). `LLMError` gains `finish_reason`, set when `_parse` rejects an empty or missing message. `complete` gains an optional `budget_seconds` that can only lower the configured total budget; the fake accepts it and records it. — Test: first. Seams: `Settings`, `OpenRouterProvider.complete`. Slices: new default and `.env.example` (AC18); the empty-reply error carries `length` (EC16); the budget argument caps retries and never raises the budget (AC7).
2. **Data model and migration.** Constants `QuestionSource` (llm, bank). `InterviewQuestion` gains source (default bank) and usage columns (model, prompt version, prompt/completion tokens, latency; nullable); `bank_id` becomes nullable. Hand-reviewed Alembic revision with a server default so existing rows read as bank. Columns on `interview_messages` stay (legacy reaction rows). No question kind yet: follow-ups, with their marking, are a later feature. — Test: after (create_all in every test; migration up/down on dev Postgres with existing rows, AC17).
3. **Reply contract (pure).** New `interviews_reply.py`: the strict reply model (question, category, no extra fields), code-fence stripping, and a parse function taking the interview type, the position and the earlier question texts, raising an invalid-reply error with a reason. — Test: first. Seam: the parse function. Slices in order: valid question; single fence accepted; text around JSON rejected; non-JSON; unknown field such as `reaction`; missing required field; over 500 characters; zero or several question marks; category vs type (mixed accepts both); repeated question ignoring case and spaces (EC5-EC9, AC5, AC6).
4. **Prompt and message building (pure).** New `prompts/interviewer_v1.md` (persona, rules from the spec, JSON output format; shaped with the `prompt-engineering-patterns` skill). A one-pass `{{name}}` renderer that fails on a missing value. Prompt rendering takes role, level, type, question number and total. A job-description block builder with delimiters and the closing delimiter neutralised. `Turn` becomes question plus answer; `build_llm_messages` takes the system prompt, the job description and the turns: system, then an opening user message (job description block plus a start instruction), then alternating assistant and user turns. Retire `reaction_v1.md`, the reaction renderer, `REACTION_PROMPT_VERSION` and the reaction merge; add `INTERVIEWER_PROMPT_VERSION`. — Test: first. Seam: those public util functions. Slices: system prompt has no answer or job description text; JSON braces in the template survive; job description only inside its block and a fake closing tag is neutralised (EC13); opening message without a job description; the rendered prompt asks for the question text only (no greeting or acknowledgement); answers only in user turns, roles alternate, the list grows by two per turn (AC10, AC11, EC14, EC21). Existing `test_llm_messages.py` is rewritten here.
5. **Fallback and reaction pickers (pure).** (a) A function in `interviews_utils.py` picking one unused eligible bank question for the next position (role or `general`, level, category from type or from position parity for mixed, behavioral on odd positions), with an injected random source. (b) Reaction pools as constants in `interviews_constants.py`, keyed by the answered question's category and a level group (intern and junior warmer, mid and senior briefer), plus a closing pool per level group, and a `pick_reaction` function taking the category, the level, whether this is the final answer, the previous reaction text and an injected random source. — Test: first. Seams: the fallback picker and `pick_reaction`. Slices: eligibility and `general` role; used bank ids excluded; mixed alternation; seeded determinism; raises when nothing is left (AC8); every pool has at least 5 distinct entries, each at most 120 characters, no question mark, no digit, none of a small denylist of praise, criticism and score words (AC23); the pool follows category and level group, the final answer uses the closing pool, a seeded pick is repeatable, never the previous text when the pool has more than one entry, a one-entry pool still works (AC24, EC23). `select_questions` stays only as the start-time coverage check.
6. **Start with an LLM-asked first question and the turn engine.** Controller: coverage check (existing `select_questions`, result discarded), engine, then the existing atomic `repo.start` with one question. The engine loops at most two attempts using the injected clock and passes the remaining budget; invalid reply retries once if at least 5 seconds remain (named constant); a provider error or no usable text goes straight to the fallback; it sums the usage and logs one line per call (outcome `ok`, `invalid_reply` or the error class, finish reason on failures, never any text). A clock dependency is overridable in tests. — Test: first. Seam: `POST /api/v1/interviews` with the fake LLM and a fake clock. Slices: LLM question stored with source llm and category (AC1); no key gives a bank question (EC1); provider error gives a bank question (EC2); invalid then valid on retry; invalid twice gives bank (EC3, EC4, AC5); no usable text is not retried and logs `finish=length` (EC16); too little time left means no retry and the retry gets only the remaining budget (AC7); stored usage is the sum and bank questions store none (AC13); log lines per call with no content or key (AC12); uncovered setup returns 409 before any LLM call (AC14, EC20); `question_count` 1 (EC12). Existing `test_create_interview.py`, `test_get_interview.py` and the `start_interview` fixture are updated here.
7. **Answer: final, legacy, and the atomic LLM turn.** Repository: a read-release method (the reads also fetch the previous reaction text) and one transaction method that does the compare-and-swap, inserts the answer, inserts the predefined reaction and inserts the next question; the existing answer-only method also inserts the reaction and stays for final and legacy. Controller: guards unchanged; pick the reaction (a new reaction id is generated in code); final answer completes with no LLM call and the closing reaction; a stored next question (legacy) is used with no call; otherwise read, capture plain values, release, run the engine, save atomically. Remove the LLM reaction path (`_react`, `_reaction_message`); keep `ReactionOut` and the response field, now never null. — Test: first. Seam: `POST /api/v1/interviews/{id}/messages`. Slices: final answer, no call, `current_question` null, closing reaction (AC4, EC11); legacy session with a predefined reaction (AC16, EC19, EC25); LLM next question stored with category and source plus a predefined reaction (AC3); the reaction is stored and returned, always non-null, also with no LLM configured and when the question came from the fallback (AC25, EC1, EC24); no transaction open during the call; forced failure while saving leaves no answer, reaction, advance or question and a resubmit works (AC9, EC18); fallback during an answer (EC4); history sent contains earlier questions and answers (no reactions) and grows (AC11); double submit stores one answer (AC15, EC17); a new interview started during the call makes the turn 409 and saves nothing (EC22); every Slice 1 guard still holds. `test_answer_interview.py`, `test_answer_guards.py`, `test_answer_llm.py` and `test_llm_logging.py` are rewritten or trimmed here.
8. **Transcript (verify).** No code change expected: the transcript already lists questions, answers and reaction items. — Test: first. Seam: `GET /api/v1/interviews/{id}/messages`. Slices: a new-style session lists question, answer and its predefined reaction in order and the same text after a reload (AC25); a legacy session keeps its old LLM-written reaction items (AC16). `test_transcript.py` is updated.
9. **Evals.** `data/eval_cases.json` (at least 6 cases: strong, vague, off-topic, near-empty, injection in the answer, injection in the job description), `interviews_evals.py` (case schema, rule checks, loader, runner `main`, printing one line per case and a summary with pass rate and token totals). Run with `uv run python -m app.modules.interviews.interviews_evals`; never imported by the app. — Test: first for loader and checks, after for the real run. Seam: the loader and the check function. Slices: file has at least 6 cases covering the categories; valid-reply check; single-question check; score and rating pattern check; injected marker not obeyed; runner summary counts using the fake provider (AC19).
10. **Live verification and learnings.** Update the opt-in live test to the new flow; run the evals and one full interview against the real model; measure valid-reply rate, token totals, latency; fill the checkpoints of `learnings.md`. — Test: after (AC20, AC21). Needs `LLM_MAX_TOKENS` raised in the owner's `.env`.
11. **Finish.** `uvx ruff check` and `format` at 120 columns on changed files, full `uv run pytest`, searches (httpx only in `openrouter.py`; no model names or URLs outside settings; the word reaction only in legacy transcript handling), `graphify update .`. — Test: skip (AC22).

## Learning Log (`learnings.md`)
`/implement` creates `docs/features/llm-interviewer/learnings.md` at the start with these checkpoints, same four parts as Slice 1 (Predict by you, Observed from real runs, Why, Proof by you). A step is not done in `task.md` until its checkpoint is written.

| After step | Concept | Predict before | Observe and record |
|-----------|---------|----------------|--------------------|
| 3 | 4 Structured output | What makes a model reply "invalid"? How often will a free reasoning model get the JSON right? | Accepted and rejected sample replies with the reason for each |
| 4 | 3 Prompts as data; 8 Injection | Where should the job description go and why delimiters? What if it contains the closing tag? | Rendered prompt, the message list with and without a job description, the neutralised closing tag |
| 5 | When not to use an LLM | What would an LLM-written reaction cost and risk compared with a constant? | The pools, a seeded sample of picks, the pool rules that a test enforces |
| 6 | 6 Reliability budget; 4 Fallback; 9 Cost | What happens at start when the LLM is slow? How many calls does an invalid reply cost? | Log lines for ok, invalid_reply, retry and fallback; summed usage |
| 7 | 5 Code enforces; atomic turn | What if the server dies after the LLM answers but before saving? | SQL order trace, `in_transaction` false during the call, the 409 on a race |
| 9 | 10 Evals | What pass rate do you expect on your 6 cases? | Per-case results and totals |
| 10 | 2, 4, 8, 9 Proof round | Cost of an N-question interview; the valid-JSON rate | Real numbers from the model |

## Affected Files & Patterns
- New: `interviews_reply.py`, `prompts/interviewer_v1.md`, `data/eval_cases.json`, `interviews_evals.py`, one Alembic revision, tests (`test_reply_contract.py`, `test_fallback_pick.py`, `test_reaction_pick.py`, `test_evals.py`), `learnings.md`.
- Changed: `core/config.py`, `.env.example`, `core/ai/{provider,openrouter,fake}.py`, `interviews_{constants,model,schema,repository,controller,dependencies,utils}.py`, existing interviews tests and `conftest.py` (a helper that builds a valid reply JSON, a fake clock), `test_config.py`, `test_openrouter.py`.
- Removed: `prompts/reaction_v1.md` and the LLM reaction path (`_react`, the reaction prompt renderer). `ReactionOut`, the `reaction` response field and legacy reaction rows stay.
- Patterns to follow: dependency override for external sources (`get_bank`, `get_llm_provider`); repository owns commit and rollback; the capture-plain-values-before-commit rule from Slice 1; `app_logs` fixture; ConflictError subclasses for 409s.
- Risks: a free reasoning model may fail the JSON contract often (more fallbacks; the log and evals will show it); releasing the read transaction expires ORM objects, so everything needed must be copied first; the shared budget makes the second attempt shorter; SQLite hides real lock behaviour, so the race is tested deterministically and checked by hand on Postgres; strict validation (single question mark, no extra fields) may reject good replies, to be tuned from eval data; small reaction pools can feel repetitive (the no-repeat rule helps; the placeholder wording is the owner's to improve).

## Testing Strategy
- Framework & command: pytest on in-memory SQLite; `uv run pytest tests/core tests/modules/interviews` while working, full `uv run pytest` at the end; lint with `uvx ruff check --line-length 120` on changed files. No automated test uses the network. The eval runner and the live test are opt-in.
- Test seams (user-confirmed): `POST /api/v1/interviews`, `POST /api/v1/interviews/{id}/messages`, `GET /api/v1/interviews/{id}/messages`, the reply parse function, the prompt and message-building functions, the fallback picker, `pick_reaction`, `OpenRouterProvider.complete`, `Settings`, and the eval check function. The per-turn budget uses an injected fake clock.

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC1, EC12 | 6 | first | LLM first question stored with source and category |
| AC2, EC1, EC2 | 6 | first | no key, error, invalid twice give a bank question (the reaction is covered in step 7) |
| AC3 | 7 | first | LLM next question stored with category and source, plus a predefined reaction |
| AC4, EC11 | 7 | first | final answer: no call, `current_question` null, closing reaction |
| AC5, EC3-EC9 | 3, 6, 7 | first | contract in step 3; retry then fallback through POST |
| AC6, EC9 | 3 | first | one fence accepted, other text rejected |
| AC7 | 1, 6 | first | budget argument; fake clock; no retry with too little time |
| AC8, EC4 | 5, 7 | first | picker rules; fallback during an answer |
| AC9, EC18 | 7 | first | forced save failure leaves nothing (answer, reaction, advance, question); resubmit works |
| AC10, EC13, EC14 | 4 | first | delimited job description, answers only as user turns |
| AC11 | 4, 7 | first | history grows and alternates |
| AC12, EC16 | 1, 6 | first | one line per call, finish reason, no content |
| AC13 | 6, 7 | first | summed usage on the question; none for bank |
| AC14, EC20 | 6 | first | 409 before any LLM call |
| AC15, EC17, EC22 | 7 | first | Slice 1 guards, double submit, race with a new interview |
| AC16, EC19, EC25 | 7, 8 | first | legacy session: predefined reaction, no LLM call; transcript keeps old reactions |
| AC17 | 2 | after | migration up/down on Postgres with existing rows |
| AC18 | 1 | first | default 800 and `.env.example` |
| AC19 | 9 | first | cases file and checks tested with the fake provider |
| AC20 | 10 | after | real run: valid rate, pass rate, tokens |
| AC21 | 10 | after | learnings filled with real numbers |
| AC22 | 11 | skip | full pytest and ruff |
| AC23, EC23 | 5 | first | pool rules enforced over the constants; one-entry pool works |
| AC24 | 5 | first | pool by category and level group, closing pool, seeded, no repeat |
| AC25, EC24 | 7, 8 | first | reaction stored with the turn, returned non-null, same after reload, independent of the LLM |
| EC15 | 9, 10 | after | cannot be detected by code; reported by the eval run |
| EC10 | 10 | after | a question that acts as a follow-up cannot be detected; noted from the real run |
| EC21 | 4, 10 | first / after | long job description grows tokens; seen in logs |

- Must verify, not assume: that the chosen free reasoning model returns the JSON reliably within the token cap; whether the provider honours a JSON response mode for this model (the plan does not depend on it); a real double-submit on Postgres; the migration on Postgres with the 9+ existing sessions.
- Open questions: none; every EC has a stated outcome. EC15 is a known limitation by design.
- Known baseline failures: none seen (340 passed, 1 skipped at the end of Slice 1).

## Blockers & Resolutions
- Order of LLM call and writes -> user-confirmed: call first, one atomic save.
- Per-turn time cap across two attempts -> remaining-budget argument plus an injected clock.
- JSON braces inside the prompt -> one-pass `{{name}}` renderer.
- `.env` still has `LLM_MAX_TOKENS=150` (owner's file) -> raise it to 800 before Step 10; the new default only applies when the variable is unset.
- Replies that are right in spirit but fail a strict rule -> fallback keeps the interview going; tune the rules from eval data, not in advance.

## Trade-offs & Rationale
- Atomic turn with the call first: simplest correct state (no pending state to recover), at the price of a wasted call on a race and an unsaved answer on a crash.
- One retry only on an invalid reply: a transient error was already retried inside the provider; retrying a no-text reply would repeat the same token-cap failure.
- Engine inside the controller, not a new service: the controller shrinks by the reaction code, and no second consumer exists yet.
- Fallback picker is pure and separate from `select_questions`, which stays as the start-time coverage check.
- Usage stored on the question, columns on `interview_messages` left alone: no destructive migration.
- Follow-ups are left out on purpose: no question kind, no marking, no transcript change now. They get their own spec, and adding a column with a default later is cheap.
- Predefined reactions instead of LLM-written ones: no tokens, no latency, no injection or judging risk, works with the LLM off, and the API contract keeps its `reaction` field. The price is generic wording, which the neutral-only rule and the no-repeat rule soften. Pools live in constants as the owner asked; a JSON data file would be the next step if they grow.
- Retiring `reaction_v1.md`: its label survives in stored legacy rows; git history keeps the text.
- New additive provider surface (`budget_seconds`, `finish_reason`) instead of letting the controller measure time around opaque calls.
- (Implementation) The reply parser takes no position: it only needed one for the dropped "first question can't be a follow-up" rule.
- (Implementation) One repository method, `record_turn(answer, reaction, next_question | None, ...)`, replaces `record_answer` + `save_message`: the final and legacy answers pass no new question. `release()` (a rollback) ends the read transaction before every LLM call, at start too.
- (Implementation) New names instead of rewriting the Slice 1 ones: `QuestionTurn`, `interviewer_history`, `build_interviewer_messages`; the Slice 1 reaction helpers and `reaction_v1.md` were removed in Step 7.
- (Implementation) Earlier questions are replayed to the model as the same JSON it must produce (a free few-shot example of the format).
- (Implementation) The migration's downgrade backfills `bank_id = 'llm'` for LLM-written questions so NOT NULL can be restored without deleting rows.
- (Implementation) `FakeProvider` gained a `default` reply (a string or a callable), so interview tests get unique valid questions without scripting every turn.
- (Finding) With the configured free reasoning model, `LLM_MAX_TOKENS=800` is not enough: its hidden reasoning used ~600-1200 tokens, and even 1500 ran out once in a full interview (the bank answered). The default stays 800 as specified; see task.md Open Questions.

## Project Rules Applied
- `CLAUDE.md` AI guidelines: prompt as a versioned file; Pydantic validation with retry and safe fallback; untrusted text separated from instructions; usage logging; no content in logs; a first eval set; mocked LLM in tests; opt-in real-model checks; teach as you build (learning log).
- `CLAUDE.md` architecture and security: route, controller, repository; `interviews_` prefixes; UUIDv7 keys; Alembic only; settings from env; ownership in the controller; no commits or pushes.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| graphify | `graphify query` on question source and answer flow (spec time and plan time); confirmed the change surface |
| lean-ctx | read the model, controller and tests; listed files touching the reaction flow |
| grill-me (via AskUserQuestion) | confirmed ordering, test seams and the eval runner shape |
| prompt-engineering-patterns (installed earlier) | to be applied in Step 4 for the prompt structure |
| python-testing-patterns (installed earlier) | fixtures and fake-clock patterns for Steps 6 and 7 |
| tdd | seams only; no loop run during planning |
| ponytail | applied inline: no new package, no pending-state machine, engine stays in the controller |
| security-review | not invoked (it reviews a diff); run it after Step 11 (surface: untrusted answers and job description, model output, key) |

## Ready to Implement
- All spec requirements, AC1-AC25 and EC1-EC25 mapped to steps
- Every step has a Test tag; seams user-confirmed
- Ordering decision made and recorded; blockers resolved or owned
- No deviations from the spec; additive provider arguments and one new file (`interviews_reply.py`) noted
