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

**Opt-in Postgres tests.** The normal suite runs on in-memory SQLite. The checks that need real pgvector (the
migration round trip, cascades, `<=>` ordering) run against a throwaway database:

```sh
docker compose exec db createdb -U postgres cuewise_test
TEST_POSTGRES_URL=postgresql+psycopg://postgres:postgres_236@127.0.0.1:5433/cuewise_test uv run pytest -m postgres
```

## Reference notes (knowledge-base RAG)

Interview notes live in `app/modules/interviews/data/knowledge/*.md` (a small header with roles, levels and source,
then one `##` section per competency). After any edit, ingest them; it validates every note first and embeds only new
or changed sections (needs `LLM_GOOGLE_API_KEY` and the pgvector database):

```sh
uv run python -m app.modules.interviews.tooling.interviews_knowledge_ingest
```

Opt-in evals (real calls; see `app/modules/interviews/tooling/interviews_rag_evals.py`):

```sh
uv run python -m app.modules.interviews.tooling.interviews_evals --task retrieval
uv run python -m app.modules.interviews.tooling.interviews_evals --task generation --repeat 3 --sheet blind.md
uv run python -m app.modules.interviews.tooling.interviews_evals --task ranking --sheet blind.md
```

