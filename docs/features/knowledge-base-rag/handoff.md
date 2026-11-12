# Handoff: Slice 8a (Knowledge-Base RAG) -> Slice 8b (Job URL)

Written 2026-11-11 on branch `feat/rag-integration`, working tree clean at `3bd96fb`.

## 1. Where 8a stands

The **code is done and committed**. The **measurements are not**: Steps 11 (your corpus review) and 12 (real runs) are
still open, so 8a's "Done when" in `docs/ai-engineering-learning-path.md` is not met yet, and its progress checkbox
is still unticked. 8b does not depend on 8a, so you can start it now and come back for the 8a measurements.

| Commit | What |
|---|---|
| `4a8fe75` | Split `interviews_turn.py` into six `ai/` files, no behavior change |
| `a99f0b9` | `Embedder` interface, `GoogleEmbedder`, `FakeEmbedder`, `build_embedder` |
| `36cf546` | pgvector tables, models, repository, migration `9b4e2d7c1a35` |
| `851f244` | 15 drafted notes, chunking, idempotent ingest CLI |
| `e9ff837` | Retrieval at interview start, `interviewer_v6` / `v6_json` with `<reference_notes>` |
| `625f963` | Retrieval line in reports, RAG evals (`--task retrieval / generation / ranking`) |
| `c2d315f` | Docs (spec, plan, task, learnings, learning path, README) |
| `3bd96fb` | Split `interviews_dependencies.py` into shared / start / answer / feedback / transcription |

Full detail: `task.md` (steps, 66 test cases, deviations), `learnings.md` (how it works, eval log),
`docs/features/split-interviews-dependencies/` (the dependencies split).

## 2. Open work on 8a (yours, in this order)

1. **Corpus gate (Step 11).** All 15 notes in `app/modules/interviews/data/knowledge/` are still `source: drafted`.
   Rewrite or replace at least 5 with your own material (`source: user` or `source: posting`).
   `test_shipped_corpus.py::test_at_least_a_third_of_the_shipped_notes_are_not_drafted` stays red until then (by design).
2. **Labelled data.** Write `data/retrieval_eval_cases.json` (15+ queries: at least 3 synonym, 1 vague,
   1 role-boundary, not copied from headings) and `data/generation_eval_keywords.json` (`competencies`, `setups`).
3. ~~**Database by hand.**~~ **Done 2026-11-11:** `pytest -m postgres` gave 5 passed (T20, T45) on the throwaway
   `cuewise_test` database. Still needed before the evals: `uv run alembic upgrade head` on the dev database.
4. **Real runs (Step 12).** Retrieval eval done 2026-11-11 (vector recall@5 1.000 / MRR 0.909 vs filter
   0.506 / 0.288; `RETRIEVAL_MIN_SIMILARITY` set to 0.55 from the sweep). Left: the generation eval, your blind
   ranking, typical embedding time vs the 5 s cap and the manual check; fill those rows in `learnings.md` §7.
5. **Approve two deviations** recorded in `task.md`: the C901 numbers in the spec came from another metric (Step 1),
   and EC26 was changed so notes get a 1,500-token allowance and are dropped *last*, not first (Step 9).
6. Tick Slice 8a in the learning path once the "Done when" list holds.

## 3. Commands

```
docker compose up -d                                   # pgvector Postgres on host port 5433
uv run alembic upgrade head
uv run python -m app.modules.interviews.tooling.interviews_knowledge_ingest
uv run python -m app.modules.interviews.tooling.interviews_evals --task retrieval
uv run python -m app.modules.interviews.tooling.interviews_evals --task generation --repeat 3 --sheet blind.md
uv run python -m app.modules.interviews.tooling.interviews_evals --task ranking --sheet blind.md
uv run pytest                                          # expected: 2 known failures, see §5
uv run --with ruff ruff check <changed paths>
graphify update .
```

## 4. Environment gotchas

- **Use `127.0.0.1:5433`, never `localhost:5433`**, in `DATABASE_URL`, `TEST_POSTGRES_URL` and the BFF's backend URL
  (`http://127.0.0.1:8000`). On this Windows machine `localhost` tries IPv6 `::1` first and compose publishes IPv4 only:
  each connection waited ~20 s (BFF `timeout of 15000ms exceeded`, a 17-minute pytest run).
- `TEST_POSTGRES_URL` and `POSTGRES_PASSWORD` must not go into `.env`: `Settings` forbids unknown keys.
- No `LLM_GOOGLE_API_KEY` means no embedder: retrieval falls back to role/level filter mode (logged as
  `retrieval_degraded:not_configured`), and the interview still runs.

## 5. Test baseline to compare against

`uv run pytest`: **1411 passed, 6 skipped, 2 failed**. The two failures are known:
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits` (expects `llm_max_tokens` 800,
  default is 4000; unrelated, older than 8a)
- the corpus gate test above

Ruff: 64 findings repo-wide, all pre-existing; touched files are clean.

## 6. What 8b can reuse

8b (per the learning path): fetch a job posting URL, extract its text, feed the **existing job-description path**,
with SSRF defences; a blocked or JavaScript-only page tells the user to paste the text instead.

The job description already flows through these, so 8b only has to produce the text:

| Piece | Where | Note for 8b |
|---|---|---|
| Input field | `InterviewCreateIn.job_description` (`schemas/interviews_schema.py:112`) | Max `JOB_DESCRIPTION_MAX_LENGTH` = 2000 chars (`constants:162`). Extracted page text must be trimmed or rejected to fit. |
| Stored | `InterviewSession.job_description`, `job_description_summary` (`models/interviews_model.py:54-56`) | Decide whether to also store the source URL (would need a migration). |
| Summary | `InterviewsService._summarize` (`services/interviews_service.py:186`) | Runs only when LLM is on and text > `SUMMARY_THRESHOLD` = 600; summary max 500. |
| Retrieval query | `query_text(summary, job_description)` (`utils/interviews_knowledge_utils.py:145`) | Fetched text automatically improves note ranking; nothing to change. |
| Prompt block | `job_description_block` (`utils/interviews_utils.py:379`) | Already fences the text as data. |
| Injection defence | `neutralize_app_tags` (`utils/interviews_utils.py:175`) | Reuse for fetched text; a page with instructions must not change behavior (8b "Done when"). |
| Flow | `InterviewsService.start` (`:104`) | Calls `repo.release()` before slow work. Do the fetch **before** or alongside that, never holding a DB transaction open. |

Design points to settle in the 8b spec (`/feature`):
- **Where the fetch lives:** an interface in `app/core/` (like `Embedder`) with a fake for tests, built by a factory
  and stored on `app.state` (see `core/ai/factory.py` and `main.py` lifespan).
- **SSRF:** allow only `http`/`https`; resolve DNS and refuse private, loopback, link-local and metadata addresses
  *before connecting and on every redirect*; cap size, time and redirects; check content type.
- **Separate endpoint or field:** a `POST` that returns extracted text for the user to review (like transcriptions:
  nothing saved), or a `job_url` field on interview start. The review step matches how voice answers work.
- **Tests offline:** saved HTML fixtures, no network (8b "Done when").
- **New dependency?** An HTML-to-text extractor would be one; say why, or try the stdlib `html.parser` first.

Patterns to copy: the transcription feature is the closest shape (external call, rate limit via
`interviews_transcription_dependencies.py`, typed errors such as `UnsupportedAudioError` / `AudioTooLargeError` in
`core/errors.py`, a result returned for review and not saved).

## 7. Reference material

- Backend field guide (architecture, request flow, DI, factories, glossary): https://claude.ai/artifact/BqFY2FZWdsjH9cVshp5Xcb
- Interview flow incl. "How text becomes vectors": https://claude.ai/artifact/XM82ZrN1QMJHvQPbx2mu1V
- Next workflow step: `/feature` for 8b, then `/create-plan`, then `/implement`.
