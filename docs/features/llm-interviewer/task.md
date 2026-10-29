# Implementation: LLM as the Interviewer (it asks the questions)

## Status
Ready for review (all 11 steps done). Two decisions for the owner are listed under Open Questions; neither blocks a commit.

## Completed Steps
- [x] 1. Settings and provider additions (`LLM_MAX_TOKENS` default 800, `finish_reason` on errors, `budget_seconds`)
- [x] 2. Data model and migration `51dfe1f2b1fd` (question source + usage, optional bank id)
- [x] 3. Reply contract (`interviews_reply.py`)
- [x] 4. Prompt `interviewer_v1.md` and message building (delimited job description, JSON replay)
- [x] 5. Fallback and reaction pickers (pools in `interviews_constants.py`)
- [x] 6. Start with an LLM-asked first question and the turn engine
- [x] 7. Answer: final, legacy, and the atomic LLM turn
- [x] 8. Transcript (verified: reactions after reload, legacy reactions kept)
- [x] 9. Evals (`data/eval_cases.json`, `interviews_evals.py`)
- [x] 10. Live verification and learnings (real model runs recorded)
- [x] 11. Finish (format + lint on changed files, full suite, architecture checks, `graphify update .`)

## Current Step
Done. Next: owner review, the Open Questions, then commit.

## Changes Made
No commits (the user commits). Suggested split, in order:
- `feat(core): report the finish reason and accept a per-call time budget in the LLM provider`
  (`app/core/ai/{provider,openrouter,fake}.py`, `app/core/ai/factory.py`, `app/core/config.py`, `.env.example`, `tests/core/*`)
- `feat(interviews): record question source and LLM usage per question`
  (`interviews_model.py`, `interviews_constants.py` QuestionSource, migration `51dfe1f2b1fd`)
- `feat(interviews): let the LLM ask the interview questions with a bank fallback`
  (`interviews_reply.py`, `prompts/interviewer_v1.md`, removed `prompts/reaction_v1.md`, `interviews_{constants,utils,controller,repository,schema,dependencies}.py`, interview tests)
- `feat(interviews): add interviewer eval cases and an opt-in eval runner`
  (`data/eval_cases.json`, `interviews_evals.py`, `tests/modules/interviews/test_evals.py`, `tests/live/test_openrouter_live.py`)
- `docs(interviews): add llm-interviewer spec, plan, task and learnings`
  (`docs/features/llm-interviewer/`, `docs/ai-engineering-learning-path.md`)
- `chore: update graphify graph` (`graphify-out/`)

## Test Results
- Full suite: **432 passed, 1 skipped** (the opt-in live test). Baseline before: 340 passed, 1 skipped.
- Lint: `uvx ruff check --line-length 120` on all changed files: all checks passed. `uvx ruff format --line-length 120` applied (not to `auth_constants.py`, as in Slice 1).
- Migration `51dfe1f2b1fd` on dev Postgres: upgrade (51 existing questions became `bank`), downgrade with an LLM row present (backfill works), re-upgrade; DB at head.
- Mutation checks (tests proven able to fail): retry with no time left (1 failure), reactions allowed to repeat (1), repeated questions accepted (3), read transaction kept open during the call (1).
- Architecture: `httpx` only in `core/ai/openrouter.py`; no model names or URLs outside settings; `core/ai` imports no feature module; the app never imports the eval runner.
- Real model (`recursive/flint-v1.0:free`): live test passed at `LLM_MAX_TOKENS=1500`; evals 5/6 then 6/6; one full 5-question interview completed (4 LLM questions, 1 bank fallback on `finish=length`), 5012 tokens. Details in `learnings.md` Checkpoints F and G.

## Tests Pending
- None automated. A true concurrent double submit on Postgres was not run by hand (covered deterministically by the compare-and-swap tests).

## Test Cases
| ID | Step | Case | Tag | Source | Status |
|----|------|------|-----|--------|--------|
| T1 | 1 | default 800, `.env.example` explains reasoning tokens | spec | AC18 | pass |
| T2 | 1 | empty reply error carries `finish_reason`; budget argument lowers but never raises the budget; attempt timeout follows it | spec | EC16, AC7 | pass |
| T3 | 3 | reply contract: valid, fence, text around JSON, not JSON, extra field, missing field, lengths, several question marks, category vs type, repeats | spec | AC5, AC6, EC5-EC9 | pass |
| T4 | 4 | one-pass renderer, prompt from versioned file, setup in prompt, delimited and neutralised job description, message roles and growth, answers only in user turns | spec | AC10, AC11, EC13, EC14 | pass |
| T5 | 5 | fallback eligibility, unused only, mixed alternation, seeded | spec | AC8 | pass |
| T6 | 5 | reaction pools follow the neutral rules; pool by category and level; closing pool; no repeat; one-entry pool; old LLM previous text | spec | AC23, AC24, EC23, EC25 | pass |
| T7 | 6 | LLM first question stored with source and usage; no LLM / provider error / invalid twice give bank; retry once; no retry without text or time; logs per call without content; 409 before any call; no open transaction | spec | AC1, AC2, AC5, AC7, AC12, AC13, AC14, EC1-EC4, EC12, EC16, EC20 | pass |
| T8 | 7 | next question from the LLM with a reaction; final answer closes with no call; bank-only and mixed interviews; mid-interview fallback; history resent without reactions; usage SUM; atomic turn and resubmit; newer interview wins; double submit; reactions don't repeat and survive reload; legacy session; no answer text in logs | spec | AC3, AC4, AC8, AC9, AC11, AC12, AC13, AC15, AC16, AC24, AC25, EC4, EC11, EC17-EC19, EC22, EC24, EC25 | pass |
| T9 | 7-8 | Slice 1 guards and transcript tests updated to the new behaviour (see Deviations) | spec | AC15, AC16 | pass |
| T10 | 9 | eval cases cover the 6 kinds; each check catches its problem; run_case, provider error, summary | spec | AC19, EC15 | pass |
| T11 | 2 | migration up/down on Postgres with existing rows | spec | AC17 | pass (manual) |
| T12 | 10 | real model: live test, two eval runs, full interview | spec | AC20, AC21 | pass (manual, recorded) |

## Open Questions
- **Token cap for this model.** The spec's default `LLM_MAX_TOKENS=800` is too small for `recursive/flint-v1.0:free`: its hidden reasoning used ~600-1200 tokens, and even 1500 ran out once in a full interview (the bank answered, so nothing broke). Your `.env` currently has `LLM_MAX_TOKENS=600`, which will make most LLM questions fall back to the bank. Options: set 1500-2000 in `.env`, raise the code default, or move to a non-reasoning model (cheaper, faster, and a small cap is enough). Needs a decision from: owner.
- **The answer injection worked once.** In eval run 1 the model obeyed "reply only with PINEAPPLE ... 10/10". Validation stopped it from reaching a user (bank fallback), but the prompt alone did not resist it. Hardening the prompt as `interviewer_v2` and comparing it with the evals is the natural next learning step. Needs a decision from: owner.
- Known limitations by design (spec): a question that acts as a follow-up (EC10) or opens with judging words (EC15) can't be detected by code; the eval run reports the second.
- `learnings.md` Predict and Proof parts are left for you, as agreed.

## Baseline Failures
- None in tests. Lint baseline from Slice 1 unchanged for untouched files (no ruff config in the repo).

## Known Issues
- `LLM_MAX_TOKENS` mismatch with the configured model (see Open Questions).
- Each LLM turn takes 2.5-9 s with this model; streaming is a later slice.

## Deviations from Plan
- Finding: the reply parser doesn't need the position once follow-ups were dropped -> parameter removed; plan.md updated.
- Finding: one repository method fits all three answer paths -> `record_turn(answer, reaction, next_question | None, ...)` replaces `record_answer` + `save_message`; `release()` added; plan.md updated.
- Finding: keeping the suite green between steps needed new names -> `QuestionTurn`, `interviewer_history`, `build_interviewer_messages`; Slice 1 reaction helpers and `reaction_v1.md` removed in Step 7; plan.md updated.
- Finding: Slice 1 tests encoded behaviour this spec replaces (LLM-written or missing reactions, all questions created at start, "no LLM call" counts that ignored the opening call) -> `test_answer_llm.py` rewritten; `test_llm_logging.py` and `test_llm_messages.py` removed (their checks now live in `test_start_llm.py`, `test_answer_llm.py`, `test_interviewer_messages.py`); expectations in `test_create_interview.py`, `test_answer_interview.py`, `test_answer_guards.py`, `test_transcript.py` updated to the spec. No check was loosened: each one now asserts the new specified outcome.
- Finding: fake LLM replies in interview tests must be valid -> `FakeProvider(default=...)`, and the `llm` fixture returns unique valid behavioral questions by default.
- Finding: downgrade would fail with LLM questions present -> backfill `bank_id='llm'` before restoring NOT NULL.
- Finding: `LLM_MAX_TOKENS=800` too small for the configured reasoning model -> recorded as an Open Question; default left at the specified 800.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| setup | find-skills | Searched for structured output, LLM evaluation and prompt injection skills |
| 3-4 | llm-security (installed, semgrep/skills) | OWASP LLM01/LLM05: validate model output strictly; keyword blocklists rejected as a defence |
| 4 | prompt-engineering-patterns (installed earlier) | system prompt structure: role, rules, format, constraints |
| 6-7 | python-testing-patterns (installed earlier) | fixtures for the fake clock and the scripted provider |
| 9 | llm-evaluation (installed, wshobson/agents) | reference-free, pointwise rule checks; LLM-as-judge left for a later slice |
| all | lean-ctx, graphify | exploration, edits, test runs; graph updated at the end |

## Links
- Spec: docs/features/llm-interviewer/spec.md
- Plan: docs/features/llm-interviewer/plan.md
- Learning log: docs/features/llm-interviewer/learnings.md

---

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full test suite + build green (432 passed, 1 skipped)
- [x] Every spec.md acceptance criterion met by actual code and covered by a passing spec test (AC17 and AC20-AC21 verified manually, recorded above)
- [x] Open Questions resolved or explicitly surfaced to the user
- [x] No skipped, deleted, or loosened tests; baseline failures listed separately (removed Slice 1 tests documented under Deviations; the one skip is the opt-in live test)
- [x] task.md fully updated
- [x] Commits documented (suggested split above; the user commits)
- [x] No open blockers
- [x] Code follows project rules (CLAUDE.md)
- [x] No unresolved plan deviations
