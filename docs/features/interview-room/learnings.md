# Learn: A speech layer that doesn't leak into features (STT + TTS for the interview room)

**Concepts:** layered dependencies (feature → generic layer → vendor), vendor adapters behind a protocol, a shared retry loop, contract tests that keep fakes honest, generic logging, measuring a vendor before trusting it. **Status:** backend built and tested 2026-11-15 (Steps 1–10); the user's browser and pricing checks are **pending**; the FE room is the next plan.

## 1. Why it exists
Voice answers (speech-to-text) worked, but their code was spread through the interviews module:
- the audio-format checks and size limits sat in `interviews_constants.py` / `interviews_utils.py`;
- the vendor error → `503` mapping and the `app.stt` log line sat in the interview transcription service.

The interview room adds text-to-speech. Built the same way, TTS would copy the error mapping, the logging and the retry loop (which already existed twice: once in the LLM provider and once in `DeepgramTranscriber`). The interviews module would end up owning vendors, audio formats and chat all at once.

## 2. What it is
Three layers, each knowing one thing, and imports only point down:

```
modules/interviews  interviews_voice_{service,controller,dependencies}   knows interviews, not vendors
        │
core/speech         audio.py · limits.py · gateway.py                    knows speech rules, not interviews
        │
core/ai             Transcriber / (SpeechSynthesizer) · deepgram.py      knows vendors, not speech rules
                    retry.run_with_retries
```

A layer test fails the build if anything in `app/core` imports `app.modules`.

## 3. When to use it
| Do this | When | Why / limit |
|---|---|---|
| Call `core/speech/gateway` from a feature adapter | Any new feature that transcribes or speaks | It already does the checks, the 503 mapping and the log line; the feature adds only its own rules |
| Add a vendor adapter in `core/ai` behind the protocol | Swapping or adding a speech vendor | The feature and the gateway don't change; the contract test shows whether the adapter behaves like the fake |
| Use `run_with_retries` | Any async request/response vendor call | Not for sync calls or streams that must not retry after output (the LLM provider keeps its own loops) |

**I'd revisit this when** a second feature needs speech with different access rules, or the vendor list grows past one (then a vendor registry earns its place).

## 4. How it works
Options considered (from `plan.md`):

| Option | Won? | Why |
|---|---|---|
| Generic `core/speech` gateway + one interview voice adapter | ✅ | One place for checks, errors, logs and limits; `core` stays feature-free |
| `interviews_speech_*` files next to the transcription ones | ❌ | Copies the error mapping and logging; two adapters |
| A standalone `modules/speech` feature | ❌ | Its routes would need interview ownership, so it would import interviews: a cross-feature dependency |

One transcription request, walked through the real code:
1. `POST /api/v1/interviews/{id}/transcriptions` → `transcribe_answer` (`app/modules/interviews/routes/interviews_route.py:276`). `limit_transcriptions` (`app/modules/interviews/dependencies/interviews_voice_dependencies.py:26`) has already charged one of the user's 10-per-minute (`app/core/speech/limits.py:12`).
2. `VoiceService.prepare_transcription` (`app/modules/interviews/services/interviews_voice_service.py:62`) checks ownership and that the interview is in progress, returns the role, and releases the DB connection.
3. The route reads at most `TRANSCRIPTION_MAX_BYTES + 1` (`interviews_route.py:286`), enough to know the file is too large without holding it.
4. `VoiceService.transcribe` (`interviews_voice_service.py:73`) passes the role's keyterms, the 2000-character cap and the log fields `user` and `session` to `gateway.transcribe` (`app/core/speech/gateway.py:37`).
5. The gateway runs `_check_audio` (`gateway.py:125`, which uses `audio_container` from `app/core/speech/audio.py:49`), then calls the vendor. `DeepgramTranscriber` runs its attempts through the shared `_DeepgramAdapter` (`app/core/ai/deepgram.py:38`): `_with_retries` → `run_with_retries` (`app/core/ai/retry.py:27`), and `_post` (`deepgram.py:91`) for the request.
6. Any `LLMError` becomes `TRANSCRIPTION_UNAVAILABLE`; any other exception is logged as `outcome=error` and re-raised. The `finally` block writes one line through `_log` (`gateway.py:138`): the caller's fields first, then the metrics. The line is byte-identical to the one before the refactor.

One speech request (the interviewer's question), walked through the real code:
1. `GET /api/v1/interviews/{id}/questions/{qid}/speech` → `speak_question` (`app/modules/interviews/routes/interviews_route.py:309`). `limit_speech` (`app/modules/interviews/dependencies/interviews_voice_dependencies.py:56`, built by `_per_user_limit` at line 39) has charged one of the user's 30 per minute; the counter is shared with `speak_reaction` (`interviews_route.py:328`).
2. The route runs `ctrl.prepare_question_speech` in the threadpool (`interviews_route.py:317`). `VoiceService.prepare_question_speech` (`app/modules/interviews/services/interviews_voice_service.py:86`) checks ownership, then `get_shown_question` (`app/modules/interviews/repositories/interviews_repository.py:180`) returns the question only if it belongs to the session **and** `position <= current_position`. Every miss raises the same "Interview not found". The text is copied into a `SpeakableLine`, and `repo.release()` ends the read transaction **before** the slow vendor call, so no pooled connection waits on Deepgram.
3. `VoiceService.speak` (`interviews_voice_service.py:109`) takes only that `SpeakableLine`, never free text, and passes it with the log fields `user`, `session`, `id`, `kind` to `gateway.synthesize` (`app/core/speech/gateway.py:90`). That calls `DeepgramSynthesizer.synthesize` (`app/core/ai/deepgram.py:167`); the shared `_DeepgramAdapter._post` (`deepgram.py:91`) does the `POST v1/speak` and maps every request failure to an `LLMError`.
4. `VoiceController.speak` (`app/modules/interviews/controllers/interviews_voice_controller.py:32`) returns the bytes with **the result's** content type and `Cache-Control: private, no-store`.

## 5. What can go wrong
| Failure | What the user sees | What the code does | Proof (test name) |
|---|---|---|---|
| Someone imports a feature module from `core` | — (the build fails) | The layer test reports the import | `test_a_core_file_importing_a_feature_module_is_reported`, `test_the_real_core_imports_no_feature_module` |
| Vendor down, rate limited or bad key | "Voice answers aren't available right now" | Retries the transient ones within the budget, then 503 | `test_every_vendor_failure_is_unavailable`, `test_a_retryable_failure_then_success_takes_two_attempts_and_one_wait` |
| A retry would pass the time budget | Same 503, sooner | No attempt starts | `test_no_attempt_starts_once_the_wait_would_pass_the_budget` |
| The fake drifts from the real adapter | — (route tests would lie) | The same checks run on both | `test_a_transcription_fills_every_result_field`, `test_a_vendor_failure_is_an_llm_error_with_its_attempts` |
| Junk upload | "Couldn't process that recording" | Refused before the vendor is called (no cost) | `test_a_bad_upload_is_refused_before_the_vendor_is_called` |
| Personal data in logs | — | Only metadata is logged | `test_one_log_line_with_the_callers_fields_and_never_the_text`, `test_one_speech_log_line_with_the_callers_fields_and_never_the_text` |
| No TTS key, or Aura down or rate limited | The line stays in the transcript; the FE shows "Couldn't play the interviewer's voice" | `SPEECH_UNAVAILABLE` (503) after retries | `test_no_synthesizer_configured_is_speech_unavailable`, `test_every_speech_vendor_failure_is_speech_unavailable` |
| Aura returns a 200 that isn't audio | Same 503 | Not retried (`LLMBadResponseError`) | `test_an_empty_or_non_audio_200_is_a_bad_response_and_not_retried` |
| The speech routes asked for someone else's line, an upcoming question, a candidate answer, or an id on the wrong route | The same 404 every time | No synthesis; a uniform message | `test_another_users_interview_is_not_found`, `test_a_question_not_shown_yet_is_not_found`, `test_a_candidate_answer_is_never_spoken`, `test_an_id_sent_to_the_other_route_is_not_found` |
| More than 30 spoken lines a minute | 429 with `Retry-After` | One counter for both speech routes, separate from transcription | `test_the_limit_is_shared_by_both_routes_and_says_when_to_retry` |
| A client tries to make it speak its own text | The stored line is spoken anyway | The request's text is never read | `test_text_sent_by_the_client_is_ignored` |

## 6. Try it yourself
1. Predict: if you add `from app.modules.interviews.constants.interviews_constants import JobRole` to `app/core/speech/gateway.py`, which test fails? Run `uv run pytest tests/test_layers.py -q`.
2. Predict how many sleeps a 503 followed by a 200 causes with `max_retries=1`. Check with `uv run pytest tests/core/ai/test_retry.py -k two_attempts -q`.
3. Change `FakeTranscriber`'s default `model` to `""` and run `tests/core/ai/test_speech_contracts.py`. Which contract check catches it?

## 7. What surprised me
- `git mv` **stages** the rename, and this repo's rules forbid staging. I unstaged it with `git restore --staged` (the working tree kept the move). Use plain `mv` for refactors here.
- A parametrize case holding a 3 MB `bytes` value breaks pytest on Windows: the case id goes into the `PYTEST_CURRENT_TEST` env var, which has a 32,767-character limit. Fixed with explicit `ids=`.
- Two existing tests are intermittently flaky and unrelated to speech (`test_turn_budget` usage logging, `test_profile_read_resume` docx). Recorded in `task.md` Baseline Failures.
- **The voice model, not buffering, drove TTS latency** (live spike, 2026-11-15, `SPEECH_LIVE_TEST=1 uv run pytest tests/live/test_deepgram_aura_live.py -q -s`, plus a time-to-first-byte script). My prediction was "streaming would fix slow clips". Wrong for MP3: Aura 2 (`aura-2-thalia-en`) sends an MP3 all at once (first byte ≈ whole clip: 805 ms for 43 characters, ~2 s for 114), so streaming saves nothing. Only `linear16` streams (first byte ~300 ms), at ~8× the size. Aura 1 (`aura-asteria-en`) returns the whole MP3 in ~330–535 ms even for the longest question. Switching the voice beat redesigning the transport.
- Cold start counts: the first clip after startup took 1049 ms (opening the connection), the next ones 512 and 328 ms. The app reuses one client, so only the first clip pays that.
- The root `tests/conftest.py` blanks `DEEPGRAM_API_KEY` for every test, so the opt-in live test skipped silently at first. The fix mirrors the existing `LLM_LIVE_TEST` guard. Also, on this machine `VAR=1 cmd` in the shell didn't reach pytest; pass the variable through the tool's env.
- Still **pending** (user checks): playback in Chrome and Safari (including iOS), the price per character, the data-use terms, the usage alert.
- I expected to test "an upcoming question" through the API. You can't: each question is stored only when it is shown. The guard still earns its place (it's the spec's no-leak rule, and it stays right if questions are ever pre-generated), so the test inserts the row by hand.
- The review found what my own tests missed: the speech lookup held its DB transaction open across the vendor call (fixed with `release()`, the pattern the answer and feedback services already used); the 404 bodies said two different things while the tests compared only the code; and `httpx.DecodingError` isn't a `TransportError`, so mapping only transport errors let it escape as a 500. Lesson: assert the whole error body, and map the base error class (`httpx.RequestError`), not the one you happened to think of.

## 8. Check your understanding
1. Why do the rate-limit *dependencies* live in interviews while the limiter *instances* live in `core/speech`?
2. When would you *not* use `run_with_retries`?
3. How does the gateway log a session id without knowing what a session is?
4. What if a new adapter returns a result with `attempts=0`?

<details>
<summary>Reference answers (write yours first)</summary>

1. The dependency needs the signed-in user from auth's `require_permissions`, and `core` may not import `app.modules`. A counter needs no user model, so it can be generic.
2. For sync calls (the LLM `complete`) and for streams, which must not retry once output has been sent.
3. The caller passes `log_fields` as ordered `(key, value)` pairs; the gateway only formats them.
4. The contract test (`attempts >= 1`) fails for that adapter, before any route test runs on a wrong assumption.
</details>

## 9. Go deeper / Still open
- Spec: `../cuewise-fe/docs/features/interview-room/spec.md` (API Contract, Decoupling rules). Plan: `plan.md`. Progress: `task.md`.
- Next: the FE plan (the room, the lobby, the camera, the voice facade) consumes the two speech routes. It must read the `Content-Type` header, not assume MP3.
- Later, deliberately not now: renaming `LLMError` to a vendor-neutral name; Redis-backed limits; a server-side TTS cache.
