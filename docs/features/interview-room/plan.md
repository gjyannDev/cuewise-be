# Implementation Plan: Interview Room (backend)

Spec: `../cuewise-fe/docs/features/interview-room/spec.md`. This repo covers **Phase 0** (the Aura spike) and **Phase 1** (cuewise-be), and implements the spec's **API Contract** exactly. The FE plan lives in the FE repo.

## Overview
First, move the existing speech-to-text code into a generic, interview-agnostic speech layer, with no behaviour change. Then add Deepgram Aura text-to-speech on top of it, behind two interview-scoped routes that speak a stored question or reaction.

## Architecture & Design
Three layers, each with one job:
- **`core/ai`** holds the vendor adapters. The existing `Transcriber`/`DeepgramTranscriber` are joined by a new `SpeechSynthesizer` protocol and a `DeepgramSynthesizer` that calls Aura `POST v1/speak` over plain httpx. Both Deepgram adapters run their attempts through one shared async retry helper in `retry.py`.
- **New `core/speech/`** is generic speech logic that knows nothing about interviews:
  - `audio.py`: container checks, accepted content types and size/duration limits, moved out of interviews;
  - `limits.py`: the per-process `RateLimiter` instances for transcription and speech;
  - `gateway.py`: plain `transcribe` and `synthesize` functions that own the availability check, vendor `LLMError` → `503` mapping, result checks and the one metadata log line (`app.stt` / `app.tts`). They take generic log fields and know no interview words.
- **interviews** gets one adapter, `interviews_voice_{service,controller,dependencies}.py`. It replaces the three transcription files and holds only interview rules:
  - ownership and `in_progress` (for STT);
  - "question already shown" and "is an interviewer reaction" (for TTS);
  - role keyterms and the answer-length cap;
  - the rate-limit dependencies, because they need auth's `require_permissions`.
  It then calls the gateway.

Speech audio is **buffered** (the whole clip) and returned as a `Response` whose media type is the synthesizer result's `content_type`. Nothing is hardcoded to `audio/mpeg`. The speech settings are read through one grouped settings object, and the env var names are unchanged.

## Approaches Considered

| Approach | Trade-offs | Chosen? |
|----------|-----------|---------|
| A. Generic `core/speech` gateway + one interview voice adapter | A one-time move of the STT code. STT and TTS share availability, error mapping, logging and limits; vendors stay swappable in `core/ai`; `core` never imports `modules` | **Yes**: spec Decision "Speech is centralized", AC17, CLAUDE.md "shared, feature-agnostic helpers go in `app/core/`" |
| B. Add `interviews_speech_*` next to the transcription files | Least churn, but the error mapping and logging are copied, audio rules stay in interviews, and there are two adapters | No: the coupling the spec rejects (AC17) |
| C. A standalone `modules/speech` feature with its own routes | Routes would need interview ownership, so speech would import interviews' service: a cross-feature dependency for no gain | No: access is decided per interview (spec, API Contract) |

Sub-decisions:
- TTS response: buffered (chosen) over a `StreamingResponse`. The FE needs the whole Blob for its replay cache, and buffering keeps failures a clean `503` with retries.
- Retry: one async helper for the Deepgram adapters (chosen) over a third copy of the loop. `OpenAICompatibleProvider` keeps its own loops: `complete` is sync, and `stream` must not retry once a chunk has been yielded, so forcing it into the same helper would add flags, not remove code.
- Settings: a read-only grouped view (chosen) over a nested settings model. pydantic-settings nesting would rename the env vars (`DEEPGRAM__API_KEY`), which is a breaking `.env` change for no gain.

## Spec Requirements -> Implementation
- Centralized speech layer (BE) → Steps 1–5
- Shared retry loop and the fake/real contract tests (Maintainability) → Steps 2, 6
- `SpeechSynthesizer` + Aura adapter, the grouped speech settings, lifespan → Step 6
- Phase 0 spike (voice, format, latency, price) → Step 7
- Gateway `synthesize` (generic log fields), `SPEECH_UNAVAILABLE`, speech limiter (30/min) → Step 8
- The two speech routes, 404 rules, no status check, text only from the DB, media type taken from the result → Step 9
- `/transcriptions` unchanged (contract, codes, limits, logs) → Steps 2–5, gated by the existing tests
- Gates and graph update → Step 10

## Implementation Steps
Checkpoint interval: after Step 5 (the refactor is complete and STT is unchanged), then every 3 steps (after 8).

Gate commands (after every step): `uv run pytest`, `uv run --with ruff ruff check app tests`.

1. **Layer rule: `core` never imports `modules`.**
   - Add a `check_core` rule plus the real-tree test to the layer tests: any `app/core/**` import of `app.modules` is a violation.
   - Today's tree already passes. Run the full suite first to confirm a green baseline.
   - Files: `tests/test_layers.py`.
   - Verify: `uv run pytest tests/test_layers.py` + gates.
   - Test: first. Seam: `check_core` over synthetic sources (the existing `test_layers.py` pattern). Slices: (a) a clean core file passes; (b) `from app.modules.x...` in core is reported; (c) the real tree passes.

2. **Shared async retry helper, plus the `Transcriber` contract test.**
   - Add one async helper to `core/ai/retry.py`. It runs an "attempt" callable (given the remaining budget) until success or until `retry_delay` says stop. It sets `attempts` and `latency_ms` on the raised `LLMError` and returns the value with its attempt count and latency, using the injected clock, sleep and rng.
   - `DeepgramTranscriber.transcribe` switches to it, keeping only its request and parse code.
   - Add a parametrized `Transcriber` contract test that runs one set of checks against `FakeTranscriber` and against `DeepgramTranscriber` on a scripted transport: the result fields are filled in; a vendor failure raises an `LLMError` subclass with `attempts` set; `aclose` works.
   - Files: `app/core/ai/retry.py`, `app/core/ai/deepgram.py`, `tests/core/ai/test_retry.py`, `tests/core/ai/test_speech_contracts.py`.
   - Verify: `uv run pytest tests/core/ai` + gates. `test_deepgram.py` must pass with unchanged assertions.
   - Test: first. Seam: the retry helper's public function (confirmed with item 1 on 2026-11-15) and the protocol contract. Slices: (a) the first success returns at once with attempts 1; (b) a retryable error then success → attempts 2 and one sleep; (c) a non-retryable error is raised right away with attempts and latency set; (d) the budget is spent → no further attempt; (e) the contract checks pass for both the fake and the real adapter.

3. **Move audio rules and limiters into `core/speech`.**
   - Move into `core/speech/audio.py`: `AudioContainer`, `AUDIO_CONTENT_TYPES`, `_has_signature`, `audio_container`, `TRANSCRIPTION_MAX_BYTES`, `TRANSCRIPTION_MAX_SECONDS`.
   - Move `TRANSCRIPTIONS_PER_MINUTE` and the `TRANSCRIPTION_LIMITER` instance into `core/speech/limits.py`.
   - Move `get_transcriber` into `core/ai/dependencies.py`. `interviews_shared_dependencies.py` re-exports it (the `# noqa: F401` pattern used for `get_llm_provider`), so override identity holds.
   - Update the imports in the route, the service, the transcription dependencies, the interviews conftest and `test_transcribe.py`.
   - Move `tests/modules/interviews/utils/test_audio_container.py` to `tests/core/speech/test_audio.py`. Only the imports change.
   - Files: `app/core/speech/__init__.py`, `app/core/speech/audio.py`, `app/core/speech/limits.py`, `app/core/ai/dependencies.py`, `app/modules/interviews/constants/interviews_constants.py`, `app/modules/interviews/utils/interviews_utils.py`, `app/modules/interviews/dependencies/interviews_shared_dependencies.py`, `app/modules/interviews/dependencies/interviews_transcription_dependencies.py`, `app/modules/interviews/services/interviews_transcription_service.py`, `app/modules/interviews/routes/interviews_route.py`, `tests/core/speech/__init__.py`, `tests/core/speech/test_audio.py`, `tests/modules/interviews/conftest.py`, `tests/modules/interviews/routes/test_transcribe.py`.
   - Verify: `uv run pytest tests/core/speech tests/modules/interviews/routes/test_transcribe.py tests/test_layers.py` + gates.
   - Test: skip (a pure move; the existing assertions are the proof).

4. **Gateway `transcribe` in `core/speech/gateway.py`.**
   - Move the generic half of `TranscriptionService.transcribe` into one gateway function: the upload checks; no transcriber → `TranscriptionUnavailableError`; `LLMError` → `TranscriptionUnavailableError` with the `cause` string; blank → `NoSpeechError`; duration over the limit → `AudioTooLongError`; trim and cap to a caller-given `max_chars`.
   - It writes the single `app.stt` line from **generic, caller-given `log_fields`** (ordered string pairs), never the audio or text. The interview service passes `user` and `session`, so the line stays byte-identical.
   - The interview service keeps `prepare_transcription` and passes `ROLE_KEYTERMS[role]` and `MAX_ANSWER_LENGTH`.
   - Files: `app/core/speech/gateway.py`, `app/modules/interviews/services/interviews_transcription_service.py`, `tests/core/speech/test_gateway.py`.
   - Verify: `uv run pytest tests/core/speech tests/modules/interviews/routes/test_transcribe.py` + gates.
   - Test: first. Seam: the gateway `transcribe` with `FakeTranscriber` (user-confirmed). Slices: (a) trimmed, capped text; (b) no transcriber → `TRANSCRIPTION_UNAVAILABLE`; (c) each `LLMError` kind → `TRANSCRIPTION_UNAVAILABLE`; (d) blank → `NO_SPEECH`; (e) over-long duration → `AUDIO_TOO_LONG`; (f) bad type, oversize or empty upload → `UNSUPPORTED_AUDIO` / `AUDIO_TOO_LARGE` / `NO_SPEECH`, vendor not called; (g) exactly one log line with the given fields, the outcome code and no text.

5. **Rename the interview adapter to `interviews_voice_*`.**
   - `interviews_transcription_{service,controller,dependencies}.py` become `interviews_voice_{service,controller,dependencies}.py`.
   - The classes become `VoiceService` / `VoiceController` / `VoiceControllerDep`. `prepare_transcription`, `transcribe`, `limit_transcriptions` and `get_transcription_limiter` keep their names; the conftest overrides the latter two.
   - The route `/transcriptions` is untouched. Delete the old files.
   - Files: the three new `interviews_voice_*.py`, the three deleted `interviews_transcription_*.py`, `app/modules/interviews/routes/interviews_route.py`, `tests/modules/interviews/conftest.py`.
   - Verify: full `uv run pytest` + gates. `git grep -n "interviews_transcription_" app tests` returns nothing.
   - Test: skip (a rename; `test_transcribe.py` and `test_layers.py` pass unchanged apart from imports).
   - **Checkpoint: the refactor is complete and STT is unchanged.**

6. **`SpeechSynthesizer`, the Aura adapter and grouped speech settings.**
   - The `SpeechSynthesizer` protocol and `SynthesisResult` live in `core/ai/synthesizer.py`. The result carries the audio bytes, **content type** (the source of truth for the response's media type), model, character count, latency and attempts. Failures raise the `LLMError` family.
   - `DeepgramSynthesizer` goes in `deepgram.py`:
     - `POST v1/speak` with `model` and `encoding` as query parameters and a JSON `{"text": …}` body;
     - the encoding comes from settings, and the content type is read from the response, falling back to the type the encoding implies;
     - it uses the Step 2 retry helper;
     - an empty or non-audio body → `LLMBadResponseError`.
   - `FakeSynthesizer` goes in `fake.py`. Extend the Step 2 contract test with a `SpeechSynthesizer` case (fake vs. real on a scripted transport).
   - Settings:
     - new fields: `deepgram_tts_model` (default `aura-asteria-en`, confirmed by the Step 7 spike on 2026-11-15: Aura 2 `aura-2-thalia-en` took ~2 s for the longest question, Aura 1 ~0.3–0.5 s), `deepgram_tts_encoding` (default `mp3`), `speech_timeout_seconds=8`, `speech_max_retries=1`, `speech_total_budget_seconds=10` (under the FE forwarder budget, per the API Contract);
     - a read-only `speech` property returns one frozen group (key, base URL, an STT part, a TTS part), following the `llm_provider_configs` property pattern;
     - env var names are unchanged.
   - `build_transcriber` and the new `build_synthesizer` read only that group. Without a key they return None, with an `app.stt` / `app.tts` warning.
   - `main.py` sets `app.state.synthesizer` at startup and closes it on shutdown. `get_synthesizer` goes in `core/ai/dependencies.py`, re-exported from the interviews shared dependencies. `.env.example` documents the new settings.
   - Files: `app/core/ai/synthesizer.py`, `app/core/ai/deepgram.py`, `app/core/ai/fake.py`, `app/core/ai/factory.py`, `app/core/ai/dependencies.py`, `app/core/config.py`, `app/main.py`, `.env.example`, `app/modules/interviews/dependencies/interviews_shared_dependencies.py`, `tests/core/ai/test_deepgram.py`, `tests/core/ai/test_speech_contracts.py`, `tests/core/ai/test_factory.py`, `tests/core/test_config.py`.
   - Verify: `uv run pytest tests/core` + gates.
   - Test: first. Seam: `DeepgramSynthesizer.synthesize` against a scripted httpx transport, the protocol contract, and the `speech` settings group (user-confirmed). Slices: (a) the request shape (path, params, JSON body, auth header, never logged); (b) returns the bytes and the response's content type; (c) a retry on 429/5xx/timeout within the budget, none on other 4xx; (d) an empty or non-audio body → `LLMBadResponseError`; (e) the contract checks pass for the fake and the real adapter; (f) `speech` groups the existing env values with the same names; (g) the factories return None without a key; (h) the config bounds reject non-positive values.

7. **Phase 0 spike: an opt-in live Aura test.**
   - Following the skip pattern of `tests/live/test_openai_compatible_live.py`, it calls `build_synthesizer` on three lines: a predefined reaction, a typical question, and the longest bank question. It asserts a non-empty audio body whose content type matches the configured encoding, and prints the latency and size.
   - Record in `task.md`: the voice, format, latency (short and long lines), price per character against the starter credit, the data-use terms for TTS input, and that a usage alert is set. Update the `deepgram_tts_model` / `deepgram_tts_encoding` defaults and `.env.example` if they change.
   - Manual check: play the clips in Chrome and Safari (including iOS).
   - **Stop and re-plan** if latency is well over 2 s or the voice is unusable.
   - Files: `tests/live/test_deepgram_aura_live.py`, `docs/features/interview-room/task.md`, possibly `app/core/config.py` and `.env.example`.
   - Verify: `uv run pytest tests/live/test_deepgram_aura_live.py -s` with a real key + gates (skipped without a key).
   - Test: after (external vendor behaviour).

8. **Gateway `synthesize`, the error, and the speech limiter.**
   - Add `SpeechUnavailableError` (503 `SPEECH_UNAVAILABLE`) to `core/errors.py`.
   - Add `SPEECH_PER_MINUTE = 30` and `SPEECH_LIMITER` to `core/speech/limits.py`. It is shared by both speech routes and separate from the transcription limiter.
   - The gateway's `synthesize(synthesizer | None, text, *, log_fields)`:
     - None → `SpeechUnavailableError`;
     - `LLMError` → `SpeechUnavailableError` (cause logged);
     - otherwise returns the `SynthesisResult`.
     - It writes one `app.tts` line: the caller's generic `log_fields` (the voice service passes `user`, `session`, `id` and `kind`; the gateway never names them), plus characters, model, latency, attempts, cause and outcome. Never the text or the audio.
   - Files: `app/core/errors.py`, `app/core/speech/limits.py`, `app/core/speech/gateway.py`, `tests/core/speech/test_gateway.py`.
   - Verify: `uv run pytest tests/core/speech tests/test_layers.py` + gates.
   - Test: first. Seam: the gateway `synthesize` with `FakeSynthesizer` (user-confirmed). Slices: (a) returns the result; (b) no synthesizer → `SPEECH_UNAVAILABLE`; (c) each `LLMError` kind → `SPEECH_UNAVAILABLE`; (d) exactly one `app.tts` line with the given fields and the outcome, and no text, on success and failure.

9. **The two speech routes and the interview voice adapter.**
   - Repository:
     - `get_shown_question(session_id, question_id, up_to_position)` returns the question only when it belongs to the session and `position <= up_to_position`;
     - `get_interviewer_reaction(session_id, message_id)` returns the message only when it belongs to the session and is the interviewer's reaction.
   - `VoiceService.speak_question` / `speak_reaction`:
     - `owned_session` (→ 404), then the lookup, then `NotFoundError` with one generic message for every miss;
     - no session-status check;
     - the stored text goes to the gateway `synthesize` with the `user`, `session`, `id` and `kind` log fields.
   - `VoiceController` returns a `Response` with the result's bytes and **its `content_type`**.
   - Dependencies:
     - `limit_speech` (permission `interviews_answer`, raising `RateLimitedError` with `Retry-After`);
     - `get_speech_limiter`, so tests can swap in a fresh limiter;
     - the synthesizer is wired into `VoiceService`.
   - Routes: `GET /{session_id}/questions/{question_id}/speech` and `GET /{session_id}/messages/{message_id}/speech`, with `status_code=200`, `response_class=Response`, `responses=` 404/429/503 (`audio/mpeg` documented as the default), and `dependencies=[Depends(limit_speech)]`.
   - Conftest: a `tts` fixture (a fake synthesizer and a fresh limiter) and a `speak` helper.
   - Files: `app/modules/interviews/repositories/interviews_repository.py`, `app/modules/interviews/services/interviews_voice_service.py`, `app/modules/interviews/controllers/interviews_voice_controller.py`, `app/modules/interviews/dependencies/interviews_voice_dependencies.py`, `app/modules/interviews/routes/interviews_route.py`, `tests/modules/interviews/conftest.py`, `tests/modules/interviews/routes/test_speech.py`.
   - Verify: `uv run pytest tests/modules/interviews/routes/test_speech.py tests/test_layers.py` + gates.
   - Test: first. Seam: the HTTP routes via TestClient with `FakeSynthesizer` (user-confirmed). Slices:
     - (a) the owner gets the current question's audio, and the synthesizer received exactly the stored text;
     - (b) the response's media type is the fake's scripted content type, not a hardcoded one;
     - (c) a follow-up question works the same way;
     - (d) the reaction route speaks a saved reaction;
     - (e) a completed interview's question can still be spoken;
     - (f) 404 for: another user's session; an unknown session; an unknown id; a question from another session; a question not shown yet; a candidate answer on the message route; a reaction id on the question route; a question id on the message route. All with the same generic body;
     - (g) 503 `SPEECH_UNAVAILABLE` with no synthesizer;
     - (h) 503 on a vendor failure;
     - (i) 429 with `Retry-After` on the 31st request in a minute, shared across both routes and independent of transcriptions;
     - (j) 401 without a token;
     - (k) no question or reaction text in the captured logs;
     - (l) no request body or text parameter is accepted.

10. **Final gates and the graph.**
    - Run the full suite, ruff and the layer tests.
    - Check that `git grep -n -E "AudioContainer|audio_container|LLMError" app/modules/interviews/services/interviews_voice_service.py` is empty (the gateway owns the vendor errors) and that `git grep -n "audio/mpeg" app` appears only in config defaults and route docs.
    - Then run `graphify update .`.
    - Files: none (verification only), plus `task.md` progress.
    - Verify: `uv run pytest` + `uv run --with ruff ruff check app tests` + `graphify update .`.
    - Test: skip (verification step).

## Affected Files & Patterns
- `app/core/speech/` (new): the audio rules, limiters and gateway. It must stay free of `app.modules` imports (Step 1).
- `app/core/ai/{retry,synthesizer,deepgram,fake,factory,dependencies}.py`: the shared retry helper and the TTS adapter next to STT.
- `app/core/{config,errors}.py`, `app/main.py`, `.env.example`: the grouped `speech` settings, `SPEECH_UNAVAILABLE`, lifespan.
- `app/modules/interviews/`: the `interviews_voice_*` trio, two repository lookups, two routes; the audio constants and utils are removed.
- Patterns to follow:
  - `DeepgramTranscriber`: client and injected transport.
  - `FakeTranscriber` and the `stt` fixture: `FakeSynthesizer` and the `tts` fixture.
  - `limit_transcriptions`: `limit_speech`.
  - `owned_session`: ownership.
  - The `get_llm_provider` re-export: override identity.
  - The `llm_provider_configs` property: the `speech` group.
  - `tests/live/test_openai_compatible_live.py`: the live test.
- Risks:
  - Override identity when moving dependency functions (handled by the re-exports).
  - The `app.stt` line must stay byte-identical (existing log tests).
  - Rewriting `DeepgramTranscriber` onto the helper could change retry timing; `test_deepgram.py` and `test_retry.py` guard it.
  - Aura's voice name and price (Step 7).

## Testing Strategy
- Framework & command: pytest (`uv run pytest`), the TestClient route tests, scripted httpx transports in `tests/core/ai/`, the fake/real protocol contract tests in `tests/core/ai/test_speech_contracts.py`, and the opt-in live tests in `tests/live/`.
- Gate commands: `uv run pytest` (including `tests/test_layers.py`) and `uv run --with ruff ruff check app tests`, after every step. `graphify update .` at the end.
- Coverage map (the BE-relevant IDs; FE-only IDs are mapped in the FE plan):

| Spec ID | Step | Test mode | Notes |
|---------|------|-----------|-------|
| AC11 | 8, 9 | first | Revealed interviewer lines only; 404/503/429; no text in logs |
| AC16 (BE half) | 10 | skip | Gates: full pytest + ruff |
| AC17 (BE half) | 1–5, 10 | first / skip | `core` imports no `modules`; audio, error mapping, logging and retries live in `core`; `test_transcribe.py` assertions unchanged |
| Maintainability (fakes match adapters) | 2, 6 | first | One contract per protocol, run against the fake and the real adapter |
| EC3 (BE side) | 8, 9 | first | Vendor failure / no key → 503 `SPEECH_UNAVAILABLE` |
| EC4 (BE side) | 9 | first | 31st request → 429 + `Retry-After` |
| EC13 (BE side) | 9 | first | Completed interview: lines still speakable |
| EC22 | 9 | first | Every miss is the same 404, nothing synthesized |
| Phase 0 spike | 7 | after | Live vendor |

- FE-only IDs, deferred to the FE plan: AC1–AC10, AC12–AC15, and EC1, EC2, EC5–EC12, EC14–EC21, EC23–EC25 (browser behaviour).
- Must verify, not assume (Step 7): Aura's voice name, the encoding and the response content type, latency, price per character, data-use terms, and playback in every target browser (iOS Safari included).
- Open questions: none for the BE.
- Known baseline failures: none seen; Step 1 confirms a green baseline first.

## Blockers & Resolutions
- Phase 0 gates the real voice. Every step except 7 runs against fakes and scripted transports.
- Questions and reactions are in different tables, so there are two routes and two lookups (spec, API Contract).
- Revealing upcoming questions is prevented by `position <= session.position`.
- An id sent to the wrong route gets the same 404 as any other miss (EC22).

## Trade-offs & Rationale
- **Buffered over streamed TTS:** clean `503`s and retries, and no FE benefit (the FE caches the Blob). Approved spec change.
- **Gateway as functions, not a class:** it holds no state (vendors are injected). Synced into the spec.
- **Generic `log_fields` in the gateway:** `core/speech` never knows "question", "reaction" or "session"; the adapter names them.
- **Media type from the result:** a format change after the spike is a settings change, not a code change.
- **One retry helper for the Deepgram adapters only:** removes the copy TTS would add; the OpenAI provider's sync and streaming loops differ in meaning and stay as they are.
- **The grouped settings are a read-only view:** the factories depend on one object, and `.env` stays as it is.
- **Limiter instances in `core/speech`, the dependencies in interviews:** they need `require_permissions` from auth, and `core` must not import `modules`. Synced into the spec.
- **Kept names** `limit_transcriptions` / `get_transcription_limiter`: the conftest overrides them, and only import-path changes are allowed for the STT tests.
- **Later, not now (YAGNI):** renaming `LLMError` to a vendor-neutral name; a vendor registry; Redis-backed limits; a server TTS cache. The design leaves one place to change for each.

## Project Rules Applied
- `CLAUDE.md` Architecture: route → controller → service → repository; the `interviews_` prefix; shared helpers in `app/core/`; the layer tests enforce it (Step 1 extends them to `core`).
- `CLAUDE.md` AI Engineering: the provider sits behind an interface in `core/ai`; timeouts, retries and latency logging; no raw content in logs; vendors mocked in unit tests, real calls opt-in.
- `CLAUDE.md` Security: default-deny, ownership in the service, generic errors, rate limiting, secrets only from env, `.env.example` updated.
- `CLAUDE.md` Code Principles: DRY (one retry loop, one error mapping), YAGNI (no registry, no nested settings model).
- Git rules: no commit, stage or push.

## Skills Consulted
| Skill | Contribution |
|-------|-------------|
| graphify | The STT cluster (Transcriber, DeepgramTranscriber, audio_container, RateLimiter, TranscriptionService) and its neighbours |
| lean-ctx / Read | deepgram, retry, openai_compatible (the loop shapes differ: sync + streaming), factory, config (`llm_provider_configs` property pattern), dependencies, layers test, conftest `stt` fixture, repository, errors |
| grilling | Buffered TTS; seams (routes, DeepgramSynthesizer, gateway); spike as an opt-in live test; the `core/speech` + `interviews_voice` layout; follow-ups approved 2026-11-15: shared retry, contract tests, generic log fields, media type from the result, grouped settings |
| ponytail | Gateway as functions; retry helper limited to the Deepgram adapters; settings view instead of a nested model; no registry or server cache |
| security-review (applied directly) | Text only from the DB; a uniform 404; no upcoming-question leak; a per-user limit; no text or audio in logs |

## Ready to Implement
- All BE spec requirements are mapped to steps.
- Every step has a Test tag. The BE-relevant AC/EC IDs are mapped; the FE-only IDs are deferred with a reason.
- Gate commands are listed, and every step names its files and a verification command.
- Approaches Considered is filled in; checkpoints are after Step 5 and Step 8.
- Blockers are resolved; the only external gate is Step 7.
- Deviations from the spec (buffered audio, gateway functions, limiter split, hygiene items) are approved and synced into the spec.
