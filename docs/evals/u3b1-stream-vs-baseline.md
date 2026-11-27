# U3b1 stage 3 (write-stream on LangChain) vs. the baseline

**Verdict: no change in quality, and faster.** Pass rate stays 1.00 on all three repeats. Time to first token fell
from 1,089 / 1,386 ms to 793 / 776 / 734 ms, and total latency from 1,154 / 1,548 ms to 857 / 849 / 805 ms. No
errors, no length cut-offs.

**What changed in stage 3:** the streamed write (interviewer_v5, the question shown while it is written) moved from
the hand-built `LLMProvider` (OpenAI-compatible HTTP endpoint) to LangChain's `astream()` on the native Gemini client,
through the new `stream_chat` helper (`app/core/ai/chat_stream.py`): retries only before the first chunk,
`LLM_TIMEOUT_SECONDS` on the first chunk only, the time left in the turn as the vendor's timeout. Same prompt, same
model. Details: `docs/features/u3b1-interview-calls/` (steps 11-14).

**Setup:** model `gemini-3.5-flash-lite`, run by the user on 2026-11-27 with `--repeat 3` and the note "U3b1 stage 3,
stream on LangChain". All three repeats reached Langfuse. Baseline: `docs/evals/baselines.md`, section "U3b1
baselines" (same day, so the latencies are comparable).

## Scores

| Eval | Langfuse run (prefix) | Score (r1 / r2 / r3) | Baseline (r1 / r2) | Noise margin | Verdict |
|---|---|---|---|---|---|
| stream | `stream/interviewer_v5/gemini-3.5-flash-lite/20261127-163159` | pass rate 1.00 / 1.00 / 1.00 | 1.00 / 1.00 | 0 | no change |

Secondary numbers (same runs):

| Measure | Now (r1 / r2 / r3) | Baseline (r1 / r2) | Reading |
|---|---|---|---|
| avg time to first token | 793 / 776 / 734 ms | 1,089 / 1,386 ms | faster by ~300-600 ms; the baseline's own spread was ±297 ms, and all three new repeats sit below its lower end |
| avg latency | 857 / 849 / 805 ms | 1,154 / 1,548 ms | faster, same reading |
| errored items | 0 / 0 / 0 | 0 / 0 | same |
| length cut-offs | 0 / 0 / 0 | 0 / 0 | same |

## Failures

- None. Every case passed every check in every repeat.

## Why it may be faster

- The old provider streamed over Google's OpenAI-compatible HTTP endpoint; the chat model uses the native Gemini
  client (gRPC). A different path to the same model is the likely cause. Latency is network-bound, so this is a
  same-day reading, not a guarantee; the write eval (blocking, also moved) showed no such gain (1,049 / 954 ms vs
  961 / 926 ms), so it is specific to streaming.

## Baseline

The quality score didn't move, so the stream row in `baselines.md` stays the quality reference. The faster time to
first token is recorded there as its own row ("stream (current latency)"), so later stream changes compare their
latency with the new path, not the old one.
