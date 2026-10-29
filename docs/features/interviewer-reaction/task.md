# Implementation: Answer a Question and Get the Interviewer's Reaction (LLM Slice 1)

## Status
Code complete (Steps 1-10 and 12 done). Step 11 is partly done: the opt-in live test is written; the real-API run and the Checkpoint G experiments wait for an OpenRouter key and model id. Not ready for PR until AC19/AC21 are verified with a real call (see Open Questions).

## Completed Steps
- [x] 1. Wiring and permission
- [x] 2. Settings
- [x] 3. Provider package `app/core/ai/`
- [x] 4. Data model and migration
- [x] 5. Prompt and pure helpers
- [x] 6. Answer endpoint: state machine (no LLM yet)
- [x] 7. Answer endpoint: guards
- [x] 8. Answer endpoint: LLM in the flow
- [x] 9. Usage logging
- [x] 10. Transcript endpoint
- [ ] 11. Live verification and learnings: live test written and skipped by default; **blocked on key** for the real run, response-shape confirmation and Checkpoint G
- [x] 12. Finish (lint on changed files, full suite, architecture checks, `graphify update .`)

## Current Step
### 11. Live verification (waiting on the owner)
1. Add `OPENROUTER_API_KEY` and `LLM_MODEL` to `.env` (both, or the app refuses to start) and set a spend limit on the key.
2. `LLM_LIVE_TEST=1 uv run pytest tests/live -q -s`: one real call; confirms the response shape (AC19).
3. Restart the server, run one full interview from the client or Swagger, then fill Checkpoint G in `learnings.md` (AC21).

## Changes Made
No commits (the user commits). Suggested split, one commit per layer:
- `feat(auth): add interviews:answer permission`: `auth_constants.py`, `tests/modules/auth/*`
- `feat(core): add LLM settings and OpenRouter provider behind an interface`: `core/config.py`, `core/errors.py`, `core/ai/*`, `main.py`, `.env.example`, `pyproject.toml`, `uv.lock`, `tests/core/*`
- `feat(interviews): add interview messages table and current position`: model, `db/models.py`, migration `084c9be8b5d2`
- `feat(interviews): answer questions and get an LLM reaction`: constants, schema, repository, controller, dependencies, route, utils, `prompts/reaction_v1.md`, tests
- `feat(interviews): add conversation transcript endpoint`: transcript schema/util/controller/route, `test_transcript.py`
- `docs(interviews): add slice 1 spec, plan, task and learnings`: `docs/`

## Test Results
- Full suite: **340 passed, 1 skipped** (the opt-in live test). Baseline before: 232 passed. 108 new tests.
- Migration `084c9be8b5d2` on dev Postgres: upgrade OK (9 existing sessions got `current_position = 1`), downgrade removes table and column, re-upgrade OK. DB is at head.
- Mutation checks (tests proven able to fail): no budget check (1 failure), retry every error (11), no question-id guard (+2), no status guard (+2), building LLM messages after the commit (1).
- Lint: `uvx ruff check --line-length 120` on all changed files: clean except baseline RUF012 in `core/errors.py`. `uvx ruff format --line-length 120` applied to new and changed files (not `auth_constants.py`, see Known Issues).
- Architecture: `httpx` imported only in `core/ai/openrouter.py`; no model name or URL outside settings; `core/ai` imports no feature module; the interviews module only uses the provider interface.
- App start with the real `.env` (no key): one `app.llm` warning, `/health` 200, provider `None`.

## Tests Pending
- AC19 (live call) and AC21 (Checkpoint G numbers): need the key.
- Concurrent double-submit on real Postgres: covered deterministically (stale `question_id` + compare-and-swap tests); a true race was not run by hand.

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | role map and `/auth/me` include `interviews:answer` | spec | AC6 | pass |
| T2 | 2 | defaults off; both set; one set refused; blank = unset; key not in repr; limits > 0; `.env.example` | spec + inferred | AC16, EC18, EC19 | pass |
| T3 | 3 | success parse, request body, temperature only when given | spec | AC12, AC13 | pass |
| T4 | 3 | missing usage, length finish, unusable body not retried | spec | EC15-EC17 | pass |
| T5 | 3 | 429 then OK; transient x3 gives up; 4xx never retried; budget stops retries; per-attempt timeout capped; slow OK; no body in error text | spec + inferred | EC11-EC14, EC24 | pass |
| T6 | 3 | factory: none + one warning / OpenRouter; fake records and scripts | spec | AC13, EC18 | pass |
| T7 | 5 | message building: first turn, merged turn, missing reaction, growth, injection only in user turns, prompt file, history pairing | spec | AC9, AC10, EC23, EC26 | pass |
| T8 | 6 | answer advances; full interview without LLM; restart after completion; GET current / completed / abandoned | spec | AC2-AC4, AC17, EC18, EC20, EC25 | pass |
| T9 | 7 | 401, 403, identical 404, 422 variants, 2000 ok, not in progress, not current (stale/future/foreign/random), double submit, CAS loser, unique backstop, DB failure, OpenAPI | spec | AC5-AC8, AC18, AC20, EC1-EC10, EC21 | pass |
| T10 | 8 | reaction stored with metadata; no usage in response; history resent; prompt has role/level, no JD; every failure kind gives null; retried result; null usage; no open transaction during call; DB failure on reaction; full interview | spec + code-derived | AC4, AC9-AC11, AC14, AC18, EC11-EC13, EC15, EC17, EC22, EC23 | pass |
| T11 | 9 | one line with all fields; finish=length; levels per failure; attempts; no personal text or key in any log; no line when off | spec | AC15, EC11, EC12, EC16, EC18 | pass |
| T12 | 10 | fresh session; order; missing reaction; no leaks; completed; abandoned; identical 404; 401/403/422; OpenAPI | spec | AC23-AC25, EC27-EC30 | pass |
| T13 | 11 | real call returns text, usage, finish reason | spec | AC19 | skipped (needs key) |
| T14 | 4 | migration up/down on Postgres with existing sessions | spec | AC1 | pass (manual) |

## Open Questions
- AC19, AC21: need `OPENROUTER_API_KEY` + `LLM_MODEL` from the owner. Until then the response shape (`choices[0].message.content`, `usage`, 401 on a bad key) is an assumption covered only by mocks.
- Predict and Proof sections in `learnings.md` are intentionally left for you (agreed: build straight through, predictions written afterwards from memory).

## Baseline Failures
- No failing tests before the change (232 passed).
- `ruff` is not a project dependency (run via `uvx ruff`), and the repo has no ruff config. Default settings report 23 pre-existing lint errors (mostly `alembic/`, plus `core/errors.py` RUF012 and an import-order issue) and would reformat 37 files because the code is written at ~120 columns. Not fixed (out of scope).

## Known Issues
- `ruff format` would also rewrite `except (ValueError, KeyError):` in `auth_constants.py` to Python 3.14's parenthesis-less form. Left as is: unrelated to this change.
- Suggest adding `[tool.ruff] line-length = 120` (and ruff as a dev dependency) so lint results match the code style. Not done: it is a project decision.
- The in-process observation runs for `learnings.md` appended a few lines to the local `logs/app.log` (gitignored).

## Deviations from Plan
- Finding: transcript question items have no meaningful timestamp -> `created_at` is null for them; spec.md and plan.md updated -> decided during implementation (small, additive).
- Finding: failure log lines need attempts and latency -> `LLMError` carries `attempts` and `latency_ms`; plan.md trade-offs updated.
- Finding: repo is formatted at 120 columns with no ruff config -> new code formatted with `--line-length 120`; plan.md updated.
- Finding: the Step 3 retry loop was written together with the first parsing round, so the retry tests went green at once -> mutation checks were run to prove they can fail (recorded above).

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| setup | find-skills | Searched skills.sh for LLM/OpenRouter, SQLAlchemy/Alembic, pytest and prompt skills; most hits had very low installs |
| setup | python-testing-patterns (installed, wshobson/agents, 37.5K installs) | pytest fixtures, mocking and parametrize patterns for the provider and endpoint tests |
| 5 | prompt-engineering-patterns (installed, wshobson/agents, 23.7K installs) | system-prompt structure (role, rules, output format, constraints) for `reaction_v1.md` |
| all | lean-ctx, graphify | exploration, edits, test runs; graph updated at the end |

## Links
- Spec: docs/features/interviewer-reaction/spec.md
- Plan: docs/features/interviewer-reaction/plan.md
- Learning log: docs/features/interviewer-reaction/learnings.md
- Learning path: docs/ai-engineering-learning-path.md

---

## Validation Checklist (before PR)
- [ ] All plan.md steps complete (Step 11 waits on the key)
- [x] Full test suite + build green (340 passed, 1 skipped)
- [ ] Every spec.md acceptance criterion met by actual code and covered by a passing spec test (or verification noted): all except AC19 and AC21, which need a real call
- [x] Open Questions resolved or explicitly surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately (the one skip is the opt-in live test, by design)
- [x] task.md fully updated
- [x] Commits documented (suggested split above; the user commits)
- [ ] No open blockers (the key for Step 11)
- [x] Code follows project rules (CLAUDE.md)
- [x] No unresolved plan deviations
