# Learn: Knowledge-base RAG for the question writer (Slice 8a)

> Status: **code complete, evals pending.** Steps 1-11 are built and tested with fakes. Everything measured against
> the real model (retrieval recall, the threshold, the three generation arms, your blind ranking, embedding latency)
> is **pending** until the corpus review (Step 11 gate) and the Docker pgvector database are done (Step 12).

## 1. Why it exists
The LLM wrote every main question from the role, level and job description alone, so which competencies an interview
covered depended on what the model happened to think of. Slice 8a grounds the writer in curated interview notes
("reference notes") chosen once per interview. It is also the project's first retrieval layer; later slices (job URL,
résumé, feedback grounding) build on it.

## 2. What it is
- **RAG (retrieval-augmented generation):** find relevant text at request time and give it to the model as data,
  instead of hoping it already knows. Here the text is ~15-20 markdown notes per role and level.
- **Chunking:** each note is cut into `##` sections; one section = one chunk = one row, about one competency.
- **Embedding:** a chunk (or a job description) turned into 768 numbers so that similar meanings point in similar
  directions. **Cosine similarity** compares two of them: 1 = same direction, 0 = unrelated.
- **pgvector:** a Postgres extension with a `vector` column type and a distance operator (`<=>`), so the database can
  rank rows by similarity inside the query.
- **Ingest:** validate, chunk, embed and store the notes; idempotent (unchanged chunks cost nothing on a re-run).
- Part 1 (done first): `interviews_turn.py` split by responsibility, no behavior change.

## 3. When to use it
Use retrieval when the model needs knowledge that is yours (curated, current, or private) and small enough to pick from.
Here the corpus is ~45 chunks, so no vector index and no framework: a filter, a ranking and a top-k are enough.
Prefer filter mode (role and level only) when there is no text to compare meaning with: no job description, or no
embedder. Don't embed role and level into the query: keep hard facts as filters, so untrusted text can't change them.

## 4. How it works
**Start of an interview, walked through:**
1. `InterviewsService.start` summarises a long job description, then calls retrieval
   (`app/modules/interviews/services/interviews_service.py:137`).
2. `RetrievalService.retrieve` (`services/interviews_retrieval_service.py:85`): LLM off -> skip. Otherwise
   `_retrieve` (`:124`) reads the eligible chunks (`repositories/interviews_knowledge_repository.py:58`: role or
   `general`, the level, active rows), then **ends the transaction** before the slow call.
3. No usable job description -> filter mode: `pick_filter_notes` (`utils/interviews_knowledge_utils.py:154`) shuffles
   the eligible notes with the interview id as the seed, so the same interview always gets the same notes.
4. Otherwise vector mode: `_embed` (`:154`) embeds `query_text` (`utils/interviews_knowledge_utils.py:145`: the summary,
   else the text as entered) as a *query* within the 5-second cap; `nearest_chunks`
   (`repositories/interviews_knowledge_repository.py:62`) ranks by `<=>` on Postgres or Python cosine on SQLite;
   the service keeps the top 6 above the threshold.
5. Any embedder problem, or nothing similar enough, degrades to filter mode (`_filter`, `:189`) and logs
   `retrieval_degraded:<reason>`. Nothing eligible, or a database error, skips: no notes, the interview runs as before.
6. The chosen notes are saved in `interview_session_chunks` in the same commit as the session, and every later answer
   turn reloads them (`InterviewsRepository.reference_notes`).

**Writing a main question:** `WithReferenceNotes` (`ai/interviews_context.py:226`) switches a main-question write of an
interview with notes to `interviewer_v6` (streamed) or `interviewer_v6_json`, and puts a `<reference_notes>` block right
after the job description, inside the same user message. Follow-ups and the decide call never see the notes; an
interview without notes sends exactly what it sent before.

**Decisions and why:**
- Hand-built layer, no LangChain/LlamaIndex: every step stays visible and the existing deadline, tracing and fakes stay
  in charge.
- Gemini's native embedding endpoint (task types, reduced size) over plain httpx (`app/core/ai/google_embedder.py:65`).
- Portable vector column (pgvector on Postgres, JSON on SQLite), so the whole SQLite suite keeps running; an opt-in
  Postgres test checks the real `<=>` ranking against the Python one.
- Retrieve once at start and save it: reproducible, traceable, and a later re-ingest never changes a running interview.
- Notes get a 1,500-token allowance; old history is trimmed before the notes, which go only as the last resort
  (see section 7).

## 5. What can go wrong
| Failure | What happens | Test |
|---|---|---|
| Embedder off, failing, rate limited, slow, wrong size | filter-mode notes, `retrieval_degraded:<reason>` | `tests/modules/interviews/services/test_retrieval_service.py::test_each_embedder_problem_degrades_to_filter_mode`, `::test_a_slow_embedder_is_cut_at_the_cap_and_degrades` |
| Nothing above the threshold | filter mode, `below_threshold` | `::test_nothing_above_the_threshold_degrades_to_filter_mode` |
| Empty corpus, LLM off, database error | no notes, interview as before | `::test_an_empty_corpus_skips_with_no_match`, `::test_llm_off_skips_without_reading_or_embedding`, `::test_a_database_error_skips_and_the_interview_goes_on` |
| A job description that tries to change role or level | can only change the ranking | `::test_a_job_description_cannot_change_the_searched_role_or_level` |
| A note with closing tags or injected instructions | tags neutralised, text stays data | `tests/modules/interviews/ai/test_reference_note_context.py::test_tags_inside_a_note_are_neutralised` |
| Hidden characters in a note | ingest refuses the file | `tests/modules/interviews/utils/test_knowledge_utils.py::test_an_invalid_note_fails_with_its_file_name_and_the_reason` |
| Ingest stops halfway | stored chunks kept, re-run finishes | `tests/modules/interviews/services/test_knowledge_ingest.py::test_a_failure_partway_keeps_what_was_stored_and_a_rerun_finishes` |
| Corpus edited while an interview runs | the interview keeps its rows | `::test_a_row_an_interview_points_at_is_kept_unchanged_when_its_section_changes` |
| The largest interview plus 6 notes | notes kept, older history trimmed first | `tests/modules/interviews/ai/test_reference_note_context.py::test_the_largest_interview_with_six_maximum_notes_keeps_the_notes` |

## 6. Try it yourself
1. Predict, then run `uv run pytest tests/modules/interviews/services/test_retrieval_service.py -k ranks -q`.
   The query vector is (0.9, 0.1, 0): which note comes first, and why is "CSS layout" missing although it points the
   same way? (API design; CSS is a frontend note and the interview is backend.)
2. In `tests/modules/interviews/utils/test_knowledge_utils.py`, change one level in a header and predict whether the
   hash changes. (Yes: header values are part of the hash, so a re-scoped section is re-embedded.)
3. Real runs: **pending** (Step 12): ingest, then `--task retrieval`, `--task generation`, `--task ranking`.

## 7. What surprised me
- The "cyclomatic complexity 46, 23 and 21" in the first spec draft didn't match ruff's McCabe count (14, 8, 8).
  Name the tool next to any complexity number.
- "Drop the notes first when the input is too big" sounded safe, but the largest interview is *always* over the limit
  before trimming (its worst case trims to 4,996 of 5,000 tokens), so notes-first would have removed the notes from
  every long interview. Measuring the worst case before choosing the rule changed the design.
- An editing tool decoded `​` into a real zero-width space inside a test file: exactly the hidden character the
  ingest check exists for. The test now builds it with `chr(0x200B)`.

**Eval log** (one row per real run; pending):

| Date | Change | Versions | Summary numbers | Failures by type | Decision |
|------|--------|----------|-----------------|------------------|----------|
| pending | first retrieval run on the reviewed corpus | gemini-embedding-001 768 | recall@5 / MRR vector vs filter: pending | pending | threshold: pending |
| pending | three-arm generation run | interviewer_v5 / v6 | competencies, coverage, tokens, start ms: pending | pending | pending |
| pending | your blind ranking | - | first places per arm: pending | - | pending |

Known limitation (recorded now): the generation metrics are keyword rules, so wording can game them; the blind ranking
is the real quality signal.

## 8. Check your understanding
1. Why are role and level filters and never part of the embedded query text?
2. Why does retrieval end the database transaction before the embedding call?
3. Why does an interview keep its notes even after the corpus is edited and re-ingested?
4. Why do follow-up questions not get the notes?

<details>
<summary>Answers</summary>

1. The query is the candidate's job description: untrusted text. As a filter, role and level come only from the
   interview setup, so a job description saying "only senior notes" can at worst change the ranking, never which notes
   are eligible.
2. The embedding call can take up to 5 seconds; holding a transaction (and a pooled connection) open while waiting
   wastes a scarce resource for nothing. The rows were read as plain values first, so ending it expires nothing in use.
3. Rows are never edited: a changed section becomes a new row and the old one is retired but kept while any interview
   points at it. The interview reads its saved rows, not "the current corpus".
4. A follow-up digs into the candidate's last answer on the same topic; the notes are for choosing *which* competency
   to probe next. Leaving them out keeps follow-ups focused (the cost: follow-up calls lose the cached prefix).

</details>

## 9. Go deeper / Still open
- Step 11 gate: at least a third of the notes must come from your material (posting-derived or your own level
  expectations); `tests/modules/interviews/utils/test_shipped_corpus.py::test_at_least_a_third_of_the_shipped_notes_are_not_drafted`
  stays red until then. Then write the 15+ labelled retrieval queries and the generation keyword lists.
- Step 12: Docker pgvector database, migration by hand, `pytest -m postgres`, ingest, the evals, the threshold, typical
  embedding time against the 5-second cap, one documented retrieval failure.
- Later (not this slice): assigning notes to question slots by competency (8a-2), a keyword baseline, a local embedder.
