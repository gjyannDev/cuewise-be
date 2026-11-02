# Implementation: Langfuse Tracing

## Status
Ready for review (all 7 plan steps done; not committed).

## Completed Steps
- [x] 1. Config + `.env.example` (Settings fields, `langfuse_enabled`, `APP_ENV`)
- [x] 2. Tracer core (`app/core/ai/tracing.py`: `Tracer`, `Generation`, `build_tracer`, fail-open guard)
- [x] 3. `TracingProvider` + `trace_labels` kwarg on protocol/OpenAICompatible/Fake; wired in `build_provider`
- [x] 4. Trace boundaries in `InterviewsController` (start, answer, stream_answer) + labels at 4 LLM call sites
- [x] 5. Lifespan builds the tracer and flushes/shuts it down after the provider closes
- [x] 6. Eval script traces under `environment=eval` and flushes on exit
- [x] 7. Verify: full suite, smoke trace against real Langfuse, `graphify update .`

## Test Results
`uv run pytest`: 847 passed, 1 skipped, 1 failed (baseline, see below). New: 21 tracer/provider, 2 lifespan, 6 route, 5 config, 1 factory.
Smoke (dummy data, real Langfuse project): generation nests under its trace; user_id, session_id, environment, model,
usage, labels, full input/output present; async-generator stream also nests correctly. Dummy traces use user `smoke-user`.

## Test Cases
Spec ACs/ECs map as in plan.md. AC12 (eval env) verified by code path only, not run (costs real LLM calls). AC11 covered by route tests.

## Baseline Failures
- `tests/core/test_config.py::test_llm_settings_default_to_off_with_documented_limits`: expects `llm_max_tokens == 800`, config default is 4000. Not caused by this feature.

## Open Questions
- Root trace span has no output (only input); add one if the dashboard list view feels empty.
- `.env` still holds removed `OPENROUTER_API_KEY` / `LLM_MODEL` / `LLM_BASE_URL`, which makes `Settings()` raise at app start (pre-existing; smoke ran with them blanked).

## Known Issues
- Ruff is not a project dependency and has no config; `uvx ruff` with defaults flags style noise project-wide, so format/lint was not enforced on the new files.
- Root-span exceptions are not marked on the trace (the body's own exception still propagates unchanged).

## Deviations from Plan
- Trace boundary uses `Tracer.trace()` (a context manager) instead of `@observe`: `@observe` captures all function args as trace input (the `User` object, ids), the Langfuse skill's own warning; input is set explicitly instead.
- Session id for `start` was a plan blocker; resolved without fallback: the session UUID is generated before any LLM call.
- `TurnContext` gained `user_id` (the ORM session reloads after its transaction ends). plan.md note only; no scope change.

## Skills Consulted During Implementation
| Step | Skill | Why |
|------|-------|-----|
| 0 | find-skills / langfuse (installed to `.agents/skills/langfuse`, linked in `.claude/`, `skills-lock.json`) | tracing baseline, verify via CLI |
| all | lean-ctx, graphify | exploration, graph refresh |

## Commit message suggestion
feat(ai): trace every LLM call and interview request in Langfuse with fail-open tracing

## Links
- Spec: docs/features/langfuse-tracing/spec.md
- Plan: docs/features/langfuse-tracing/plan.md

## Validation Checklist (before PR)
- [x] All plan.md steps complete
- [x] Full suite green except the listed baseline failure
- [x] Spec ACs met by code and tests (AC12 by inspection)
- [x] Open questions surfaced
- [x] No skipped/loosened tests
