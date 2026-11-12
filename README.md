# cuewise-be
Learning AI engineering by building: an LLM-powered interview and career-readiness coach.

## Development database (Postgres 18 + pgvector)

The reference notes (knowledge-base RAG) are stored with their embeddings in a `vector` column, which needs the
[pgvector](https://github.com/pgvector/pgvector) extension. A plain Postgres install doesn't have it, so the dev
database runs from the pgvector Docker image in `compose.yaml` (host port 5433, so it can sit next to a local Postgres
on 5432).

1. Start it: `docker compose up -d` (wait until `docker compose ps` shows it healthy).
2. Point the app at it in `.env`:
   `DATABASE_URL=postgresql+psycopg://postgres:postgres_236@127.0.0.1:5433/cuewise`
   (use `127.0.0.1`, not `localhost`: on Windows `localhost` can try IPv6 first and wait ~20 s before falling back,
   while Docker publishes the port on IPv4 only)
3. Then either **recreate** the schema from scratch:
   `uv run alembic upgrade head` (creates every table and enables the `vector` extension; you sign up again),
   or **move** your existing dev data from the old database on 5432 first:

   ```sh
   pg_dump -h localhost -p 5432 -U postgres -Fc cuewise > cuewise.dump
   docker compose exec -T db pg_restore -U postgres -d cuewise --no-owner < cuewise.dump
   uv run alembic upgrade head
   ```

   The dump carries its Alembic version, so `upgrade head` only adds what is newer (the knowledge-base tables).
   Delete `cuewise.dump` afterwards: it holds interview answers.

The migration fails on a Postgres without pgvector (`extension "vector" is not available`) and changes nothing; check
that any other environment's Postgres provides the extension before deploying.

**Opt-in Postgres tests (database integration tests).** The normal suite runs on in-memory SQLite. The checks that
need real pgvector run against a **throwaway database** `cuewise_test`, never the dev database `cuewise`: the tests
create and drop tables there freely. They live in `tests/modules/interviews/postgres/test_knowledge_postgres.py`,
carry the `postgres` marker, and **skip themselves unless `TEST_POSTGRES_URL` is set**, so a plain `uv run pytest`
never needs Docker.

| Test | Checks |
|---|---|
| `test_the_migration_creates_and_drops_the_tables_and_keeps_the_extension` | migration up and down on real Postgres |
| `test_a_vector_round_trips_as_pgvector` | the `vector(768)` column stores and returns a vector |
| `test_deleting_an_interview_deletes_its_note_references_and_keeps_the_note` | FK cascade from interviews |
| `test_a_note_an_interview_points_at_cannot_be_deleted` | a used note is protected |
| `test_pgvector_ranks_like_the_python_cosine_used_on_sqlite` | parity: pgvector `<=>` orders notes like the SQLite cosine |

Run them:

```sh
# 1. The database container must be running (once per boot)
docker compose up -d

# 2. Create the throwaway database (once; "already exists" is fine)
docker compose exec db createdb -U postgres cuewise_test

# 3a. Git Bash: the variable goes in front of the command
TEST_POSTGRES_URL=postgresql+psycopg://postgres:postgres_236@127.0.0.1:5433/cuewise_test uv run pytest -m postgres -v
```

```powershell
# 3b. PowerShell: set the variable for this terminal, then run
$env:TEST_POSTGRES_URL = "postgresql+psycopg://postgres:postgres_236@127.0.0.1:5433/cuewise_test"
uv run pytest -m postgres -v
```

Expect `5 passed`. `SKIPPED ... set TEST_POSTGRES_URL` means the variable wasn't set in that terminal. Add
`-k ranks_like` to run one test by name, and `--durations=10` to list the slowest. Use `127.0.0.1`, not `localhost`
(see above). Don't put `TEST_POSTGRES_URL` in `.env`: the app's settings refuse unknown keys.

## Reference notes (knowledge-base RAG)

Interview notes live in `app/modules/interviews/data/knowledge/*.md` (a small header with roles, levels and source,
then one `##` section per competency). How to write one: `docs/features/knowledge-base-rag/note-guide.md` and
`note-template.md`.

**Run the ingest after every change to the notes** (adding, editing, renaming, retagging or deleting a note). The app
never reads the `.md` files at interview time: it reads the `knowledge_chunks` table, so until you ingest, interviews
keep using the old notes.

```sh
# Once per boot: the pgvector database must be running, with the tables in place
docker compose up -d
uv run alembic upgrade head      # only needed once, or after pulling a new migration

# 1. Optional: check one note without touching the database or the API
uv run python -c "from pathlib import Path; from app.modules.interviews.utils.interviews_knowledge_utils import parse_note; p=Path('app/modules/interviews/data/knowledge/YOUR-NOTE.md'); n=parse_note(p.name,p.read_text(encoding='utf-8')); print(len(n.chunks),'chunks', n.warnings)"

# 2. Ingest: validates every note, then embeds only new or changed sections
uv run python -m app.modules.interviews.tooling.interviews_knowledge_ingest
```

What it touches: it **writes** to the database in `DATABASE_URL` (the dev database `cuewise`) and **calls the Google
embedding API** once per new or changed section (needs `LLM_GOOGLE_API_KEY`; a few hundred sections cost very
little). It pauses between calls to stay under the rate limit.

Reading the result (last line):

| Output | Meaning |
|---|---|
| `new=3 changed=0 unchanged=60 retired=0 deleted=0` | Done. `new`: sections embedded for the first time; `changed`: edited (or retagged) sections re-embedded; `unchanged`: skipped, no API call; `retired`: sections whose note was removed or edited; `deleted`: retired sections no interview points at |
| `invalid note, nothing was ingested: <file>: <reason>` | Fix that note (the reason names the rule); nothing was written |
| `warning: ...` | Ingest still runs. An instruction-like phrase in a note, or fewer than a third of the notes non-drafted (the Slice 8a gate) |
| `Embeddings are not configured` | `LLM_GOOGLE_API_KEY` is empty in `.env` |
| `ingest stopped: ...` | An API or database error; what was stored is kept, run it again to finish |

Running it twice in a row is safe: the second run prints `new=0 changed=0` and makes no API calls (each section's
content hash decides). A retagged note counts as changed, because roles and levels are part of the hash. Interviews
that already used the old version keep it.

Opt-in evals (real calls; see `app/modules/interviews/tooling/interviews_rag_evals.py`):

```sh
uv run python -m app.modules.interviews.tooling.interviews_evals --task retrieval
uv run python -m app.modules.interviews.tooling.interviews_evals --task generation --repeat 3 --sheet blind.md
uv run python -m app.modules.interviews.tooling.interviews_evals --task ranking --sheet blind.md
```

