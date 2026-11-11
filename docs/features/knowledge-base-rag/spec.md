# Feature: Knowledge-Base RAG for the Question Writer (Slice 8a)

## Problem
The LLM writes every main question from the role, level, interview type, the job description (or its summary) and the interview so far. Nothing grounds it in what an interviewer for that role and level actually probes, so question coverage depends on what the model happens to think of, and the prompt can only say "spread the questions over different competencies". The project also has no retrieval layer, which the next slices (job URL, résumé, feedback grounding) and later features need to build on.

A second problem makes extending the interviewer harder: `app/modules/interviews/ai/interviews_turn.py` is about 790 lines, and it mixes six concerns in one class (types, limits, logging, the decide call, the blocking write and the streamed write; ruff's C901 scores its longest method 14, under the limit of 15, so the problem is size and mixing, not one tangled function). Every further slice would pile onto it.

## Goal
Two parts, built and reviewable one after the other:

1. **Refactor (no behavior change):** split `interviews_turn.py` by responsibility so each piece is small and testable, with the existing tests unchanged apart from import lines.
2. **Knowledge-base RAG:** at interview start, pick up to 6 interview notes for the candidate's role, level and job description from a curated corpus, store them for that interview with their rank, and give them to every **main-question** write as delimited data (`interviewer_v6` for the streaming writer, `interviewer_v6_json` for the JSON writer used at start and by the JSON route). With a job description the notes are ranked by meaning (vector mode); without one, or when vector ranking is not possible, they come from the role and level filter alone (filter mode). If no notes can be found at all, the interview runs exactly as it does today.

Measured by:
- the split passes the existing test suite with only import lines changed in tests, and no resulting function exceeds complexity 15 (starting target);
- recall@5 and MRR on at least 15 labelled queries, for vector retrieval and for the filter-only baseline;
- a **three-arm generation eval** on the existing eval setups with repeats: **A** no notes (`interviewer_v5`), **B** `interviewer_v6` with filter-only notes, **C** `interviewer_v6` with vector notes. Rule metrics per arm: distinct competencies per interview, job-description skill coverage, rule checks still passing, added prompt tokens, added start latency;
- a **blind ranking by the user** of the three arms' question sets on about 10 setups, reported as how often each arm ranked first (the rule metrics are gameable, so this is the main quality signal);
- a failing embedder never stops an interview from starting or finishing.

## Project Conventions
- Rule files consulted: `CLAUDE.md` (project root; there is no `.claude/rules/`), `docs/ai-engineering-learning-path.md` (Slice 8a and concepts 2, 8, 9, 12), and the specs and learnings of `llm-interviewer`, `follow-up-questions`, `sse-streaming`, `context-management` and `interview-feedback` (prompt versioning, the shared deadline, snapshotting, fenced untrusted data, eval logs). graphify and lean-ctx used for orientation.
- Constraints those rules impose on this feature:
  - Layers: route -> controller -> service -> repository inside `app/modules/interviews/`, files prefixed `interviews_`; no business logic in routes or controllers, no SQL outside the repository, no SDK or HTTP calls to a provider outside `app/core/ai/`.
  - Every table's primary key is a UUIDv7 generated in the app via `UUIDPrimaryKeyMixin`; every foreign key to it is a UUID. The notes table and the per-interview table follow this.
  - Schema change only through a new Alembic migration; applied migrations are not edited.
  - The embedding call sits behind an interface in `app/core/ai/` (like `LLMProvider` and `Transcriber`) with a fake for tests; model names, URLs and keys come from config (`pydantic-settings`, `.env.example` updated), never hard-coded.
  - Prompts are versioned files (six-part structure: Role, Task, Input, Output, Constraints, Capabilities); `interviewer_v5` stays untouched and `interviewer_v6` is new. No prompt text inline in code.
  - RAG steps are separate and individually testable: ingestion, chunking, embedding, retrieval, generation.
  - Prompt-injection safety: retrieved text is data inside delimiters, never instructions; the job description stays untrusted and can only influence ranking, never which role or level is searched.
  - Privacy: the job description is personal data. The query text is never written to app logs, traces or reports; only ids, counts, ranks, scores, model name, latency and outcome codes are.
  - Reliability: the embedding call has a time cap, and any failure degrades (to filter mode, or to no notes). It never blocks or fails an interview.
  - Tests use the fake embedder; real-model runs are opt-in evals. An eval set is part of the feature (CLAUDE.md, "Evaluation").
  - A new dependency needs a stated reason: see Constraints.
  - `uv run pytest` and `uv run ruff check .` pass; `graphify update .` after code changes; do not commit or push.
  - Learning-project deliverable: `docs/features/knowledge-base-rag/learnings.md` in the tutorial template of `docs/ai-engineering-learning-path.md`.
- Decided with the user (this conversation):
  - The **question bank plays no part**: no retrieval from it, no changes to it. Removing it belongs to Slice 10.
  - The corpus is about 15 to 20 markdown notes by role and level (competencies, what interviewers probe, what strong and weak answers look like), **drafted by Claude and reviewed by the user**. To avoid a model grounding a model on its own knowledge, **at least a third of the notes come from material the user supplies or approves** (skills distilled from real job postings, the user's own level expectations, and the level lines of `feedback_rubric_v1` if they fit). Every note records its source kind.
  - Notes are **chunked by heading**, each chunk carrying roles, levels and a competency.
  - **Retrieve once, at interview start.** Results are stored per interview (session, chunk, rank, score, mode).
  - **The vector query is the job description only** (the summary when there is one, else the text as entered). Role and level are never put in the query text; they are hard filters only.
  - **No job description -> no embedding call.** Notes come from the role and level filter alone (filter mode), chosen deterministically from the interview's id.
  - Filter by role and level first, then rank by cosine similarity, **top 6**, with a similarity threshold taken from the eval (not guessed).
  - **No exact role/level match** -> use notes tagged for all roles ("general"); if nothing matches, no notes.
  - **Same notes all interview**: re-ingesting or editing the corpus never changes the notes of an interview already started.
  - **5-second cap** on the embedding call at start.
  - **pgvector** in Postgres through the **pgvector Docker image** for local development (the dev Postgres 18.6 has no pgvector).
  - Embedding model **`gemini-embedding-001`** through the existing Google AI Studio key; the model name is config and is stored on each note row. Documents and queries use the model's matching task types if it supports them.
  - The refactor is the **first, separate part**; existing tests may change **import lines only**.
  - Quality is judged by **three-arm rule metrics plus the user's blind ranking** (there is no LLM judge: Slice 7 was skipped by choice). The rule metrics' weakness is a recorded limitation.
  - No LangChain, LlamaIndex or other RAG framework.
  - **Tests:** the vector column is a portable type (pgvector on Postgres, JSON on SQLite) so the existing SQLite suite keeps running; the real `<=>` query is checked by an opt-in Postgres test.
  - **Vector size 768**; a **native Google embedding client** (task types and size verified on the project's key).
  - **Two write paths get notes:** `interviewer_v6` (streaming, plain text) and `interviewer_v6_json` (first question and JSON route); an interview without notes keeps the unchanged v4 and v5 prompts.
  - **Three eval arms** (no notes, filter-only notes, vector notes); no static-checklist arm.
  - **Vector mode degrades to filter mode** on failure or when nothing clears the threshold.
- Follow-ups explicitly **not** in this slice: assigning notes to question slots by competency (a possible 8a-2 after the baseline numbers), a local-embedding experiment, and a Postgres full-text keyword baseline.

## User Flow
Operator (once, and after any corpus edit):
1. Write or edit notes under the interviews data folder.
2. Run the ingestion command. It validates every note, embeds only new or changed chunks, and stores them.

Candidate (no new screens or endpoints):
1. The candidate starts an interview as today.
2. The API summarizes a long job description (as today). Then:
   - **With a job description:** it embeds the job description, filters by role and level, ranks by similarity and keeps up to 6 above the threshold (vector mode).
   - **Without one, or if vector mode cannot produce notes:** it picks up to 6 notes by the role and level filter alone (filter mode).
   - It stores the notes for that interview.
3. The first question is written with the notes available to the writer. The same stored notes are used for every later main question; follow-up questions are written as today.
4. If no notes can be found at all, step 3 happens without notes and the log records why.

## Requirements

### Functional

**Part 1: refactor**
- Split `interviews_turn.py` by responsibility (for example: deadline and limits, the decide step, the write and stream step, the logging helpers). Behavior, event order, log lines, prompts and API responses stay the same.
- Test changes are limited to import lines; no assertion, fixture or expectation is edited.

**Part 2: ingestion, chunking, embedding**
- A corpus of markdown notes; each note declares the roles and levels it applies to and a **source kind** (for example drafted, posting-derived, user-written), and each heading section is a chunk with a competency. A note tagged for all roles ("general") applies to every role.
- Invalid notes (unknown role or level, missing competency or source kind, empty section, hidden or zero-width characters) fail ingestion with a message that names the file; nothing from that run is written for that file. Instruction-like phrases (for example "ignore previous instructions") do not fail ingestion but are listed as warnings in its output, because posting-derived text is third-party.
- Each chunk has a stable key (file and heading) that eval labels refer to, since chunk ids differ between environments.
- At least a third of the shipped notes have a source kind other than "drafted".
- Ingestion is idempotent: unchanged chunks cause no embedding call and no row change; changed or new chunks are embedded and stored; chunks of notes that were removed are retired from retrieval.
- A chunk that any interview references is never deleted or edited. A changed section becomes a new row.
- Each row stores its embedding model name; vector mode only considers rows embedded with the configured model.
- An `Embedder` interface in `app/core/ai/`, with a fake for tests and a real implementation for the Google embedding model, behind config. Chunks are embedded as documents and queries as queries using the model's query and document task types. *(verified on the project's key)*

**Part 2: retrieval and generation**
- **Vector mode** (a job description with usable text exists): after the summary step, embed the job description summary (or the text as entered when there is no summary), using only that text. Filter by role (including "general") and level, rank by cosine similarity, drop results under the threshold, keep up to 6, and store each with its rank (1 first), score and mode.
- **Filter mode** (no job description, or a blank one; or vector mode could not produce notes): no embedding call. Filter by role (including "general") and level, and pick up to 6 of the eligible chunks in an order seeded by the interview's id, so the same interview id always gives the same notes and different interviews can differ. Stored with ranks 1..n, no score, and mode `filter`.
- Vector mode **degrades to filter mode**, logging `retrieval_degraded:<reason>`, when: embedding is not configured, the embedder fails, is rate limited or times out (5-second cap), the query embedding does not match the stored vector size, or nothing is above the threshold.
- Retrieval is **skipped**, logging `retrieval_skipped:<reason>`, when: the LLM is off (questions come from the bank), the corpus has no eligible note for the setup (`no_match`, including an empty corpus), or the database read fails.
- The stored notes go to every main-question write of that interview as a delimited `<reference_notes>` block, in `interviewer_v6` (plain text, the streaming writer) or `interviewer_v6_json` (the JSON writer used for the first question and by the JSON answer route). An interview with no stored notes keeps using the unchanged v4 and v5 prompts. Decide and follow-up writes do not receive the notes. If the input would pass the size limit, the notes are dropped first and the question is still written by the LLM.
- The notes appear in the interview report and in the traces as ids, ranks, scores, mode and outcome code only. They are not exposed in any API response.
- Every embedding call logs model, input token count when the provider reports it, latency and outcome; never the input text.

**Evals**
- A retrieval eval: at least 15 labelled queries (job-description style text with the chunk ids that should come back), including at least 3 synonym job descriptions, at least 1 vague one and at least 1 role-boundary one. It reports recall@5 and MRR for vector retrieval and for the filter-only baseline (averaged over a fixed number of seeded orderings of the eligible chunks), and the similarity threshold used.
- A generation eval with three arms (A, B, C above) on the existing eval setups with repeats, reporting per arm the rule metrics listed in Goal. Competency and skill matching is rule-based (keywords defined in the eval data) and recorded as a limitation.
- A blind ranking: a command builds a sheet for about 10 setups in which the three arms' question sets appear in random order with neutral labels; the arm key is stored apart from the sheet. After the user fills in the ranking, a command reads it and reports, per arm, how often it ranked first. A setup where any arm failed to produce a full question set is left out of the sheet and counted in the report.
- Both evals run as opt-in commands for real-model runs, and their cheap rule parts run on the fakes in the normal test suite. Results go in the eval log of `learnings.md`.

### Non-Functional
- Latency: vector mode adds at most one embedding call (5-second cap) to interview start, filter mode only a database read; the added time is measured and reported, not assumed.
- Cost: embedding tokens are logged per call; the added prompt tokens per main question are reported by the generation eval.
- Reliability: no retrieval failure can fail or delay (beyond the cap) an interview.
- Privacy: see Project Conventions; the embedding provider receives the job description summary, as the LLM provider already does.
- Scale: the corpus is small (about 100 chunks), so no vector index is required.

## UX Requirements
- No candidate-facing change and no new endpoint. Candidates cannot tell whether notes were used, except through question quality.
- Operator-facing: the ingestion command prints counts (new, changed, unchanged, retired) and, on failure, the file and reason. No raw note or job-description text in logs beyond the file name. The blind-ranking commands reject an incomplete or invalid grading file with the line and reason, and report nothing partial.

## Constraints
- **New dependency: `pgvector` (Python package)**, for the SQLAlchemy vector column type and distance operators. Reason: the alternative is hand-written casts and operators for every query. No other new dependency.
- **Database:** the Alembic migration enables the `vector` extension, so every environment's Postgres must provide it. For local development, run Postgres from the pgvector Docker image; this needs a documented setup (README or docs) and moving or recreating the dev data.
- The vector column has a fixed size, so changing to an embedding model with a different vector size needs a new migration and re-ingestion.
- The Google AI Studio free tier limits calls per minute; ingestion of about 100 chunks and the eval runs must pause or batch accordingly.
- The corpus tags use only the existing `JobRole` and `Level` values and "general".

## Blockers
- **Dev database:** the pgvector Docker image must be set up by the user (moving or recreating the dev data) before the migration can run. *Owner: user.*
- **Corpus material:** the user must supply or approve the non-drafted material (skills from real postings, own level expectations) and review the drafted notes, before the retrieval eval labels are written (so labels are not written from the headings). *Owner: user.*
- **Production database:** whether the target Postgres provides `vector` is unknown. *(assumption: verify before deploying.)*
- **Resolved:** when vector mode cannot produce notes (embedder failure, timeout, or nothing above the threshold) the interview degrades to filter-mode notes instead of "no notes" (confirmed in planning).

## Assumptions to verify
- `gemini-embedding-001` accepts a reduced output size so the stored vector fits the chosen column size. *(verified on the project's key: 768 works, the default is 3072; the plan uses 768)*
- The model supports query and document task types. *(verified on the project's key: both are accepted by the native endpoint)*
- The embedding model is reached through Google's native embedding endpoint with the already installed `httpx`, in a small client in `app/core/ai/`. *(verified: the OpenAI-compatible endpoint also serves embeddings, but only the native one was shown to accept task types and a reduced size)*
- The 5-second cap is realistic for one embedding call; the first real run records the typical time and may tighten it.

## Edge Cases
Format: condition -> expected outcome.

- **EC1:** the interview has no job description, or a blank one -> filter mode: no embedding call, up to 6 eligible notes, mode `filter`, no scores.
- **EC2:** the job description is short, so no summary exists -> the text as entered is the query text (vector mode).
- **EC3:** a long job description whose summary failed -> the text as entered (at most 2000 characters) is the query text.
- **EC4:** no note matches the exact role and level -> notes tagged for all roles that match the level are used; if none match, no notes and `retrieval_skipped:no_match`.
- **EC5:** in vector mode fewer than 6 notes clear the threshold, but at least one does -> only those are stored; filter-mode notes do not pad the list.
- **EC6:** in vector mode nothing clears the threshold (for example a vague job description) -> filter mode and `retrieval_degraded:below_threshold`.
- **EC7:** the embedder times out (over 5 seconds), is rate limited, returns a server error, or is not configured -> filter mode and `retrieval_degraded:<reason>`; the interview starts normally.
- **EC8:** the corpus is empty -> `retrieval_skipped:no_match`, no notes, the interview works as today.
- **EC9:** the LLM is off (questions come from the bank) -> retrieval is skipped (`llm_off`); no embedding call is made.
- **EC10:** the corpus is edited and re-ingested while an interview is in progress -> that interview keeps the same notes for all remaining main questions; the rows it references are untouched.
- **EC11:** ingestion is run again on an unchanged corpus -> no embedding call, no row change, exit code 0.
- **EC12:** a note is removed from the corpus and ingestion runs -> its chunks stop being retrievable; rows referenced by an interview are kept, others may be removed.
- **EC13:** ingestion fails partway (embedder error) -> the process exits non-zero naming the failing note; chunks already stored stay; running it again finishes the rest.
- **EC14:** the configured embedding model has a different vector size than the column -> ingestion refuses with a message that a new migration is needed; no rows are written. At interview start the same mismatch degrades to filter mode.
- **EC15:** rows were embedded with a previous model name -> vector mode ignores them; filter mode does not need embeddings and may use them; ingestion re-embeds them with the configured model.
- **EC16:** the job description tries to instruct the system ("only return the senior notes") -> the role and level filter comes only from the interview setup, so it cannot change which notes are eligible; at worst it changes ranking.
- **EC17:** a note's text contains delimiter tags or instruction-like text -> the tags are neutralised, and the text is treated as data by the writer.
- **EC18:** the database read for retrieval fails -> `retrieval_skipped:db_error`, interview starts without notes.
- **EC19:** two interviews start at the same time -> each retrieves and stores its own notes; no shared mutable state.
- **EC20:** an interview created before this feature -> no stored notes, and it behaves exactly as before (reports show no retrieval line).
- **EC21:** the interview is deleted -> its stored note references go with it; the notes themselves stay.
- **EC22:** the writer fails for a question and the bank supplies it -> the notes are not used for that question; nothing else changes.
- **EC23:** a stream is rejected and reset in the middle of a main-question write -> the retry uses the same notes (the refactor must keep the reset behavior).
- **EC24:** a setup where one eval arm fails to produce a full question set -> that setup is left out of the blind sheet and counted in the report.
- **EC25:** the user's grading file is incomplete, has an unknown label or a repeated rank -> the command refuses with the line and reason and reports nothing partial.
- **EC26:** an interview's input with 6 reference notes would pass the size limit -> notes get their own token allowance on top of the limit; older history is trimmed first, and the notes are dropped last, before the input would count as too large, so the question is still written by the LLM (no bank fallback because of the notes). *(changed in implementation from "notes dropped first": see plan Deviations)*

## Acceptance Criteria
Part 1: refactor
- [ ] **AC1:** `uv run pytest` passes with the same results as before the split (the one recorded baseline failure unchanged), and the diff to existing tests contains import lines only.
- [ ] **AC2:** ruff's C901 check at a limit of 15 reports nothing for the files that replace `interviews_turn.py` (starting target; tuned if a real function needs more and the reason is written down).
- [ ] **AC3:** the split changes no request or response, no prompt file, no migration and no log line text (checked by reviewing the diff).

Part 2: ingestion and storage
- [ ] **AC4:** a note with an unknown role or level, a missing competency or source kind, an empty section, or hidden or zero-width characters makes ingestion fail with a message naming the file, and nothing is written for it (EC13 aside); an instruction-like phrase is listed as a warning without failing.
- [ ] **AC5:** the shipped corpus passes validation, and at least a third of its notes have a source kind other than "drafted".
- [ ] **AC6:** running ingestion twice on an unchanged corpus makes zero embedding calls the second time and changes no rows (EC11); editing one section embeds exactly that chunk.
- [ ] **AC7:** a chunk referenced by an interview is never deleted or edited by ingestion; a changed section becomes a new row (EC10, EC12).
- [ ] **AC8:** each stored row has its embedding model name; vector mode ignores rows with a different model name (EC15); a model with a different vector size is refused at ingestion (EC14).
- [ ] **AC9:** the `Embedder` interface has a fake used by every unit test; no unit test calls the network.
- [ ] **AC10:** the fake embedder shows chunks being embedded as documents and the job description as a query when task types are supported; if the model does not support them, the learnings say so.

Part 2: retrieval and generation
- [ ] **AC11:** with fixed fake vectors, vector mode returns only notes whose roles include the interview's role or "general" and whose levels include its level, ordered by score, at most 6, none under the threshold (EC4, EC5).
- [ ] **AC12:** the text sent to the embedder equals the job description summary (or the text as entered) and contains no role or level text added by the app.
- [ ] **AC13:** with no job description (or a blank one), no embedding call is made; up to 6 eligible notes are stored with mode `filter` and no score; the same interview id always gives the same notes (EC1).
- [ ] **AC14:** for each degrade reason (not configured, embedder error, rate limit, timeout, size mismatch, nothing above the threshold), a test shows the interview starts, filter-mode notes are stored, and the log says `retrieval_degraded:<reason>` (EC6, EC7).
- [ ] **AC15:** for each skip reason (LLM off, no eligible note, database error), a test shows the interview starts, the first and later questions are written without notes, no stored rows exist, and the log says `retrieval_skipped:<reason>` (EC4, EC8, EC9, EC18).
- [ ] **AC16:** after retrieval, one stored row per note exists for the interview with rank 1..n, its score (empty in filter mode) and its mode; no API response contains the notes.
- [ ] **AC17:** with stored notes, each main-question write of that interview (the first question and the streamed and JSON answer routes) receives them inside a delimited `<reference_notes>` block of `interviewer_v6` or `interviewer_v6_json`; decide calls and follow-up writes do not; with no stored notes, the v4 and v5 prompts render exactly as before.
- [ ] **AC18:** delimiter tags inside a note are neutralised in the rendered prompt (EC17).
- [ ] **AC19:** a test with a fake embedder slower than the cap shows interview start is delayed by no more than the cap plus a small margin, and degrades to filter mode (EC7).
- [ ] **AC20:** no log line, trace or report contains the query text; they contain only ids, counts, ranks, scores, mode, model name, latency and outcome codes.
- [ ] **AC21:** deleting an interview removes its stored note references and keeps the notes (EC21); an interview from before the feature starts, runs and reports without error (EC20).
- [ ] **AC22:** a job description that tries to restrict or change the searched role or level does not change the eligible notes (EC16).

Part 2: evals and documentation
- [ ] **AC23:** the retrieval eval has at least 15 labelled queries with the required kinds (3 synonym, 1 vague, 1 role-boundary), and its command prints recall@5 and MRR for vectors and for the filter-only baseline, and the threshold used.
- [ ] **AC24:** the generation eval prints, for arms A, B and C over the existing setups with repeats: distinct competencies per interview, job-description skill coverage, rule-check pass counts, added prompt tokens per main question and the start latency; the rule parts run on the fakes in `uv run pytest`.
- [ ] **AC25:** the blind-ranking command builds a sheet for at least 8 setups with the three arms in random order under neutral labels and the key stored apart; given a filled grading file it reports, per arm, how often it ranked first; incomplete or invalid grading files are refused (EC24, EC25).
- [ ] **AC26:** the real-model results of the evals and the user's blind ranking are recorded in the eval log of `learnings.md`, including one documented retrieval failure with its cause and the known limitation of rule-based measures.
- [ ] **AC27:** `.env.example` documents the new settings, the README or docs explain running the dev database from the pgvector image, and `docs/features/knowledge-base-rag/learnings.md` exists in the tutorial template.
- [ ] **AC28:** `uv run pytest` and `uv run ruff check .` pass (no new findings in touched files).
- [ ] **AC29:** a test with the largest allowed interview plus 6 reference notes shows the notes fit, and a test with a tiny input limit shows the notes are dropped and the question is still written by the LLM (EC26).

## Out of Scope
- Using or changing the question bank, and removing it (Slice 10).
- Job URL (8b), résumé upload (8c), résumé-aware questions (8d) and feedback grounding (8e).
- Assigning retrieved notes to individual questions by competency (a possible 8a-2), per-turn retrieval, reranking, hybrid keyword and vector search, vector indexes, a retrieval API or admin screens.
- A local-embedding experiment and a Postgres full-text keyword baseline.
- Grading through Langfuse's annotation tools (the blind ranking is file-based).
- Exposing the retrieved notes to candidates.
- An LLM judge (Slice 7); question quality is measured with rule checks and the user's blind ranking.
- LangChain, LlamaIndex or any RAG framework.
- Changing the follow-up, decide, feedback or summary prompts.
