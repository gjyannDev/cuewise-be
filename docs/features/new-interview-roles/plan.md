# Implementation Plan: Three New Interview Roles (designer, qa, devops)

No spec.md (you approved that). The goals below stand in for it; plan steps refer to them as G1-G6 and edge cases as E1-E6.

## Overview
Let a candidate practice as a UI/UX designer, a quality engineer or a DevOps engineer by adding `designer`, `qa` and `devops` as interview roles, with their voice terms, bank questions and reference notes, without changing how the existing five roles behave.

## Goals and edge cases (stand-in for the spec)
- G1: `POST /api/v1/interviews` accepts `designer`, `qa`, `devops` (and list/get return them); any other role is still 422.
- G2: a technical, behavioral or mixed interview can start for each new role at every level (the bank can back it).
- G3: reference-note headers accept the new roles; each new role has role-specific notes for **all four levels** (intern, junior, mid, senior), following the split the existing roles use (`<role>-fundamentals.md` for intern and junior, a second note for mid and senior, e.g. `backend-fundamentals.md` + `backend-design.md`). The three notes written from your postings supply one band per role; three more fill the other band.
- G4: each new role has voice keyterms (shared terms plus its own) within Deepgram's limit.
- G5: no migration, no change for the five existing roles, full suite equals the baseline.
- G6: shipped prompts are untouched (known limitation: they say "{{role}} developer role").
- E1: existing sessions keep working (the `role` column is `String(32)`, not a DB enum).
- E2: a new role at a level with no role-specific notes falls back to the `general` notes (at least 6 per level today).
- E3: retagging a note changes its content hash (roles are hashed), so already-ingested chunks are retired and re-embedded on the next ingest. Nothing else breaks; interviews that used the old rows keep them.
- E4: until Step 5 lands, `qa` has notes for intern and junior only, and `devops` and `designer` for mid and senior only; the other band uses the `general` notes. After Step 5 no new role falls back to `general` alone at any level.
- E5: an unknown role in a note header is still refused by the parser.
- E6: the client dropdown and the BFF live outside this repo and must offer the new values (not part of this plan).

## Architecture & Design
Roles are one `JobRole` string enum in the interviews constants. Everything else already keys off it: the request and response schemas, the prompts, the services, the note parser (`_KNOWN_ROLES = {*JobRole, "general"}`) and the retrieval scope filter. So adding three enum values opens the API and the notes, and the rest is data: per-role keyterms, per-role bank questions, and the role tags on the notes. No new layer, no new file in `app/`, no schema change.

## Spec Requirements -> Implementation
- G1 -> Steps 1, 3
- G2 -> Step 2
- G3, E3, E4, E5 -> Steps 4, 5
- G4 -> Step 1
- G5, E1, E2 -> Steps 1, 6 (suite), and no migration
- G6 -> Step 1 (no prompt edit), recorded under Blockers
- E6 -> Handoff note in Step 6

## Implementation Steps
1. **Add the roles and their voice terms.** Add `designer`, `qa`, `devops` to `JobRole`, then add terms for each in `_ROLE_ONLY_KEYTERMS` (plain text, no duplicates of `SHARED_KEYTERMS`, which already holds CI/CD, Docker, Kubernetes, AWS). Seam: `ROLE_KEYTERMS`, observed through the existing role-looping tests in `test_keyterms.py`; adding the enum first turns them red, the terms turn them green. — Test: first
2. **Bank questions.** Add 2 technical questions per new role to `data/questions.json` (ids `des-tech-01`, `qa-tech-01`, `devops-tech-01`, ...; levels spread like the `mob-tech` pair). I draft, you review the wording. Seam: `load_bank(QUESTION_BANK_PATH)` and `select_questions`. Slices: (a) the shipped bank covers every role, (b) a technical interview can be selected for each new role at every level. — Test: first
3. **API acceptance.** No schema edit expected (`InterviewCreateIn.role` is `JobRole`). Add route tests, parametrized over the three roles: start returns 201 with that role echoed, get and list return it; an unknown role still returns 422. Seam: `POST /api/v1/interviews` (confirmed). — Test: first
4. **Retag the notes you already have.** Headers: `qa-testing-fundamentals.md` -> `qa` (intern, junior); `devops-platform.md` -> `devops` (mid, senior); `ux-design-collaboration.md` -> `designer` (mid, senior). Update `note-guide.md` and `note-template.md` to list the new roles (the role list is already added; remove its "only after" caveat). Seams: `load_corpus(KNOWLEDGE_DIR)` and `RetrievalService.retrieve`. Slices: (a) the retagged corpus loads with no warning, (b) a `devops` start gets `devops` and `general` notes and no `qa` or `designer` ones. — Test: first
5. **Fill the missing level band so each role covers all four levels.** Reference for structure and length: the three notes from your postings (probe, strong, weak, follow-up, under 600 characters, 4 to 6 sections) and the existing pairs `backend-fundamentals.md` / `backend-design.md`. Follow `note-template.md` and `note-guide.md`.

   | New note | Roles | Levels | Sections to write (topics) |
   |----------|-------|--------|----------------------------|
   | `qa-test-strategy.md` | qa | mid, senior | risk-based test planning; the test pyramid and what to automate; quality gates in CI and releases; quality metrics that matter; leading a release sign-off |
   | `devops-fundamentals.md` | devops | intern, junior | Linux and shell basics; Git and a basic CI pipeline; containers with Docker; reading logs and basic monitoring; cloud basics (compute, storage, networking, IAM) |
   | `designer-fundamentals.md` | designer | intern, junior | visual hierarchy and layout; accessibility basics; user flows and wireframes; receiving and acting on critique; handing a design to developers |

   Source: no posting exists for these bands, so they are `drafted` unless you supply material (a posting for a junior DevOps or a senior QA role would let them be `posting`). Seam: `load_corpus`. Slices: (a) every new role has at least one role-specific section for each of the four levels, (b) each new note loads with no warning and every section is within 600 characters, (c) a `qa` senior start gets `qa` notes, not only `general`. — Test: first
6. **Wrap-up.** `uv run pytest` (expect only the 2 known failures), ruff on touched files, `graphify update .`, `task.md` and `learnings.md` for this feature, note E6 for the client. — Test: skip

## Affected Files & Patterns
- `app/modules/interviews/constants/interviews_constants.py` — `JobRole` (line 6) and `_ROLE_ONLY_KEYTERMS` / `ROLE_KEYTERMS` (about lines 229-329).
- `app/modules/interviews/data/questions.json` — 6 new entries, 23 today (mobile has 2 role-specific; 6 `gen-tech` serve everyone).
- `app/modules/interviews/data/knowledge/` — header lines of the three posting notes (Step 4); three new notes `qa-test-strategy.md`, `devops-fundamentals.md`, `designer-fundamentals.md` (Step 5).
- `docs/features/knowledge-base-rag/note-guide.md`, `note-template.md` — role lists.
- Tests to add: `tests/modules/interviews/routes/` (start per role), `utils/test_shipped_corpus.py` (role-specific note), `services/test_retrieval_service.py` (devops scope).
- Already role-looping, no edit expected: `constants/test_keyterms.py`, `utils/test_question_bank.py`, `utils/test_shipped_corpus.py` (6 eligible per role and level).
- Pattern to follow: how the `mobile` and `data` entries were added (bank entries, keyterm tuples).
- No change: models, repositories, migrations, prompts, eval cases (`eval_cases.json` has no required role coverage; a case per new role is optional later).
- Risks: low. The enum is the only code change; a typo in a note header makes the whole corpus refuse to load (the parser names the file).

## Testing Strategy
- Framework & command: `uv run pytest tests/modules/interviews -q` while working; `uv run pytest` once at the end; `uv run --with ruff ruff check <touched paths>`.
- Coverage map:

| ID | Step | Test mode | Notes |
|----|------|-----------|-------|
| G1 | 3 | first | start 201 per role; unknown role 422; get/list echo the role |
| G2 | 2 | first | shipped bank covers every role; technical interview selectable per role and level |
| G3 | 4, 5 | first | headers parse (4); every new role has a role-specific section at each of the four levels (5); E5 unknown role still refused |
| G4 | 1 | first | existing keyterm tests, parametrized over `JobRole` |
| G5 | 6 | skip | full suite equals the baseline |
| E1 | 6 | skip | no migration; checked by reading the column type (`String(32)`) |
| E2 | 4 | first | existing eligible-notes test already loops over every role and level |
| E3 | 4 | after | verify on the real DB at the next ingest: old rows retired, new rows embedded |
| E4 | 5 | first | `qa` senior and `devops` junior retrieval return role notes, not only `general` |

- Must verify, not assume: how `qa`/`devops`/`designer` interviews read with the real model, given the prompts' "developer role" wording (G6). One real start per role, by hand, after the opt-in eval keys are set up.
- Open questions: none blocking. Role display labels ("QA Engineer") belong to the client.
- Known baseline failures: `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`; `test_at_least_a_third_of_the_shipped_notes_are_not_drafted`. Today 3 of 18 notes are non-drafted (6 needed). After Step 5 there are 21 notes, so 7 are needed: 4 more non-drafted (or 4 drafted ones replaced by your own). Step 5's drafted notes make the gap bigger, which is why they are the first candidates to replace with posting material. Neither failure is caused by this feature.

## Blockers & Resolutions
- Prompts say "{{level}} {{role}} developer role" -> accepted: shipped versions are never edited in place; drop "developer" in the `interviewer_v8` that Slice 8d cuts (`interviewer_v7` became the notes prompt in 8a; v8 drops it for profile interviews only, no-profile prompts keep it until a later bump). The job description and the reference notes steer the model meanwhile. Confirmed by you.
- Retagging the notes before the enum exists would make the corpus unloadable -> notes are retagged in Step 4, after Step 1.
- Bank thinness: a technical interview for a new role leans on the 6 general technical questions plus its 2 own. Same as mobile today; enough to start (max 10 questions, the LLM writes the real ones). Extend the bank later.
- Gate for 8a is unchanged in kind but grows in size: the 3 posting notes count as non-drafted; the 3 Step 5 notes are drafted unless you supply material; see the baseline line above for the count.
- A new role with only one level band would fall back to `general` notes for the rest (E4) -> Step 5 writes the missing band for each role.

## Trade-offs & Rationale
- One-word role values (`designer`, `qa`, `devops`) -> same style as the existing roles; display names are the client's job. Confirmed by you.
- 2 technical bank questions per role (not 4 with behavioral) -> matches mobile, quick to review, behavioral comes from the general pool. Confirmed by you.
- Two notes per new role, split intern/junior and mid/senior -> same as the existing roles, and it keeps each note about one level of depth. The new bands are drafted by default because no posting exists for them; the cost is the larger gate gap, accepted so every level works now and replaced with real material later.
- No new prompt versions now -> avoids moving four prompt versions, their constants, tests and eval comparisons for a wording nuance; 8d needs a new version anyway.
- No `eval_cases.json` entries now -> the eval set is for tracking prompt changes, and those are not changing here.

## Project Rules Applied
- `CLAUDE.md`: schema changes only through Alembic -> none needed. Config and constants in constants files, no hardcoded values elsewhere. Tests mirror `app/modules`. Never commit, push or stage; changes stay in the working tree. Run `graphify update .` after code changes.
- `tests/test_layers.py` -> unaffected (no new imports).

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| lean-ctx | where `JobRole` is used (18 files), the role-looping tests, the bank and keyterm structures |
| graphify | JobRole dependency map (1,347 nodes; confirmed the services only pass the role through) |
| grill-me (AskUserQuestion) | role values, prompt wording, bank depth, test seams |

## Ready to Implement
- All goals mapped to steps; every step tagged
- Seams confirmed by you: `POST /api/v1/interviews` plus the existing role-looping tests. Seams for the notes (`load_corpus`, `RetrievalService.retrieve`) follow the same style but were not asked separately; say so if you want another.
- Blockers resolved, edge cases handled, trade-offs documented
- Next: `/implement docs/features/new-interview-roles/plan.md`
