# Learn: Adding interview roles (designer, qa, devops)

## 1. Why it exists
Candidates practising for UI/UX design, quality engineering and DevOps jobs had to pick the nearest developer role,
so the questions, notes and voice terms fitted a different job. Adding the roles makes the whole interview (questions,
reference notes, transcription hints) belong to the job they are applying for.

## 2. What it is
Three new values of the `JobRole` enum (`designer`, `qa`, `devops`) plus the data each role needs:
- voice keyterms (`_ROLE_ONLY_KEYTERMS`, `interviews_constants.py:329`)
- two technical bank questions per role (`data/questions.json:25-30`)
- reference notes for every level: one note from your postings and one drafted note per role.

No migration: every `role` column is `String(32)`, so the database never knew the list of roles.

## 3. When to use it
Use the same recipe for any future role: enum value, keyterms, two bank questions covering all four levels, and a
pair of notes (intern/junior, mid/senior). The tests below fail until each part is there.

## 4. How it works
The enum is the single list of roles, and the rest keys off it:
- `InterviewCreateIn.role: JobRole` (schemas) makes FastAPI reject anything else with 422.
- The note parser accepts `_KNOWN_ROLES = {*JobRole, GENERAL_ROLE}` (`interviews_knowledge_utils.py:44`), so a note
  can name the new roles as soon as the enum has them, and not before.
- Questions and notes are eligible when they name the role or `general` (`interviews_utils.py:96`), so a QA candidate
  gets QA material plus the general material, and never another role's.

One request: `POST /api/v1/interviews {"role": "qa", "level": "senior", "interview_type": "technical"}`
1. Pydantic validates `qa` against `JobRole`.
2. `select_questions` finds the 6 general technical questions plus `qa-tech-02` (mid, senior), enough for up to 7.
3. Retrieval (no job description) picks notes in filter mode from `qa-test-strategy.md` (qa, mid/senior) and the
   general notes for seniors.
4. The interviewer prompt says "senior qa developer role" (see section 5).

## 5. What can go wrong
| Risk | What happens | Test that guards it |
|---|---|---|
| A role without keyterms | `KeyError` when a voice answer is transcribed | `test_keyterms.py` (loops over `JobRole`) |
| A role whose own questions miss a level | Interviews lean on general questions only | `test_every_role_has_its_own_technical_question_at_every_level` |
| The shipped bank can't back a technical interview | 409 `NOT_ENOUGH_QUESTIONS` | `test_a_new_role_starts_a_technical_interview_from_the_shipped_bank` |
| A note tagged with another role | A designer gets QA notes | `test_a_new_role_gets_its_own_notes_and_never_another_new_roles` |
| A note naming a role before the enum has it | The whole corpus refuses to load | the parser (`CorpusError: unknown role`) |
| Prompt wording | "designer developer role" | none: known limitation, fixed in `interviewer_v7` (Slice 8d) |

## 6. Try it yourself
1. Predict: what status does `POST /api/v1/interviews` return for `"role": "sre"`? Run
   `uv run pytest tests/modules/interviews/routes/test_create_interview.py -k unknown-role`. (422.)
2. Change `qa-test-strategy.md`'s header to `levels: mid` only, and predict which test fails. Run
   `uv run pytest tests/modules/interviews/services/test_retrieval_service.py -k new_role`. Put it back.

## 7. What surprised me
- Two existing tests used `devops` as their example of an *unknown* role. Adding the role made them fail; the sample
  value changed to `sre`, the check (unknown role refused) stayed.
- The question bank was never the blocker it looked like: the 6 general technical questions back every role, and
  mobile and data already work with 2 role questions each.
- `test_turn_budget.py::test_usage_of_both_calls_is_summed_and_every_call_logs_metadata_only` failed in the full run
  (`budget_left_ms=29998`, expected `30000`). The same code and tests pass on a clean copy of the repo without the
  local `.env`: the test measures real time (no fake clock), so it depends on the machine. Not caused by this feature.

## 8. Check your understanding
1. Why did no migration need to run?
2. Why must the enum change land before the notes are retagged?
3. Why does each new role need its own technical question at every level, when the general ones already fill an interview?

<details>
<summary>Answers</summary>

1. The `role` columns are plain strings; only the Python enum lists the allowed values.
2. The note parser validates roles against the enum; a note naming `qa` before `JobRole.qa` exists makes the whole
   corpus refuse to load, which breaks the tests and the ingest.
3. Without one, a QA interview at that level would only ask generic engineering questions; the role question is also
   the bank fallback when the LLM fails, so it decides what a candidate sees on a bad day.

</details>

## 9. Still open
- The three Step 5 notes are `drafted`; replace them with posting or your own material when you find it (the 8a gate
  now needs 7 non-drafted notes of 21; there are 3).
- Interviewer, decide and feedback prompts say "{{role}} developer role"; fix in `interviewer_v7` (Slice 8d) and its
  siblings.
- The client role dropdown and the BFF must offer `designer`, `qa`, `devops` (outside this repo).
- After the next ingest, check on the dev database that the three retagged notes' old rows were retired and re-embedded.
- `test_turn_budget` timing assertion: make it use the `clock` fixture (separate fix).
