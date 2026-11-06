# Learn: Rubrics, scoring and an LLM as the judge (Slice 6: end-of-interview feedback)

**Concepts:** 4 Structured output, 5 The LLM decides and the code enforces, 9 Cost (one deadline for two calls),
10 Evals (bands and spread), 11 Rubrics / LLM-as-judge. See `docs/ai-engineering-learning-path.md`.

> **Status.** Built and unit-tested end to end with fakes (2026-11-05): 142 new tests, full suite green apart from one
> older failure. One real-model run done (one repeat, section 7). Still **pending**: the spread across repeats, the
> senior-level fix, the maximum-size case and the review of the rubric and bands (section 9).

---

## 1. Why it exists

When an interview ended, the candidate got nothing back: no score, no idea what was strong or what to practise. The
app also had no repeatable measure of answer quality, so it could not tell whether a prompt or model change made the
coaching better or worse.

Asking a model "how did they do?" gives a nice paragraph and nothing you can trust or compare. Its numbers move between
runs, it can be talked into a 5/5 by the answer itself, and it can "quote" things the candidate never said. So this
slice is about making a judge you can check.

## 2. What it is

- **A rubric** (`data/feedback_rubric_v1.json`): 8 criteria, 4 per question category, each with an anchored description
  of scores 1 to 5 and what an early-career vs an experienced candidate must show. It is versioned data, like a prompt.
- **Two calls.** A **score call** reads the whole interview and returns closed JSON: a 1-5 score for each criterion of
  each main question, plus a short verbatim quote and reason as evidence. A **write call** turns the stored scores into
  coaching text (summary, strengths, improvements, next steps, one note per question).
- **The code does everything checkable.** It decides whether there is enough to score, verifies every quote against the
  real answers, computes the overall, decides who may generate and when, and writes a template text if the write call
  fails.

```
completed interview --pre-check (code)--> score call --validate + verify quotes (code)--> store scores
                                                                                            |
             response <-- store text <-- write call (or template, code) <-- overall = mean (code)
```

## 3. When to use it

| Do this | When | Why / limit |
|---|---|---|
| A rubric with anchors per score | Any LLM grading you want to compare over time | "Rate 1-5" without anchors drifts; anchors make a 3 mean the same thing twice |
| Separate the judge (score) from the writer (text) | The numbers matter more than the prose | A closed JSON reply is checkable; free text is not. The expensive call runs once |
| Verify evidence quotes in code | The judge must point at what the user said | A quote that is not in that question's answers is an invented reason |
| Compute totals in code | Always | A model's arithmetic and its "overall" can be steered by the input |
| A code pre-check before any call | Inputs can be empty or near empty | No call, no cost, and no invented scores for "I don't know" |
| Skip the LLM judge | When a rule can decide (word counts, formats) | Rules are free and deterministic |

**I'd revisit this when** the real-model runs show the spread above 1 point on a criterion, or the quote check rejects
most replies (paraphrasing models), or the cost of the score call on long interviews is too high.

## 4. How it works

**The design choices:**

| Concern | Choice | Why |
|---|---|---|
| One call or two | Two (score, then write) | The score call is closed JSON and checkable; a failed write never repeats it |
| Scale | 1-5 per criterion, anchored | Few enough levels to anchor each one in words |
| Overall | Mean of every criterion score, rounded half up in code | Equal weight, explainable; `round()` would give 3.2 for 3.25 |
| Evidence | Max one quote per criterion, 10-200 chars, verified | Keeps the reply small and every reason grounded |
| What the write call sees | Scores, quotes, reasons, question texts | No answers, no job description: less personal data, nothing to inject |
| Failure of the write call | Template text built by code | The scores are still worth showing |
| Once per interview | Unique `session_id` + a claim token | Two clicks can't pay twice; a crashed request can be taken over |

**One POST walked through the code:**

```
interviews_route.py:172            generate_feedback  sync route; 201 new, 200 already generated
interviews_dependencies.py:113     limit_feedback     3 per minute per user, before anything can cost a call
interviews_feedback_controller.py:130  generate      owned? completed? existing generated -> 200; LLM off -> 503
interviews_feedback_controller.py:181  _claim        insert, or take over a failed / stale row (claim token = started_at)
interviews_repository.py:241       reclaim_feedback   the age check is inside the UPDATE (compare-and-swap)
interviews_feedback.py:73          build_threads      one thread per main question, follow-ups included
interviews_feedback.py:95          assess_evidence    the pre-check: >= half the main answers have 15+ words
interviews_feedback_turn.py:112    score              ContextManager task feedback_score, at most 2 attempts
interviews_context.py:309          FeedbackScore      system prompt + rubric; JD and answers fenced as data
interviews_feedback.py:152         parse_score_reply  strict JSON, exact criteria, 1-5 ints, quotes verified
interviews_feedback.py:205         compute_overall    Decimal, ROUND_HALF_UP
interviews_feedback_controller.py:299  _write        every write after the claim only lands while the claim holds
interviews_feedback_turn.py:142    write              task feedback_write, scores and evidence only
interviews_feedback.py:253         parse_write_reply  labelled sections, counts, lengths, no markdown
interviews_feedback.py:337         template_text      the fallback text, under the same rules
interviews_feedback_turn.py:215    log_feedback_summary  one metadata-only line per generation
```

The prompts: `prompts/feedback_score_v1.md`, `prompts/feedback_write_v1.md` (six-part layout), rendered by
`interviews_utils.py:320` and `:351` from the same constants the parsers check.

**Reading one feedback in Langfuse** (when the keys are set; tag `feedback`, in the same session as the interview):

```
interview-feedback        trace   input {interview_id}; output {outcome, overall, text_source, scores}; scores overall, quotes_rejected
├─ score                  chain   output {outcome, attempts, quotes_rejected, answers_truncated, estimated_input_tokens, scores}
│  ├─ feedback_score      generation  attempt 1: messages, reply, tokens, model_parameters {max_tokens, temperature}
│  ├─ check-score-reply   guardrail   {passed: false, verdict: invalid_reply:quote_not_found}  WARNING
│  ├─ feedback_score      generation  attempt 2
│  └─ check-score-reply   guardrail   {passed: true, verdict: ok}
└─ write                  chain   output {outcome, attempts, text_source}; WARNING "template used (...)" on fallback
   ├─ feedback_write      generation
   └─ check-write-reply   guardrail
```

Why the checks: a generation only shows what the model sent. Without a check, a reply the code rejected looks like a
success; the guardrail puts the code's verdict right after it. A failed score step is ERROR, a template text is
WARNING, a provider error stays ERROR on its generation. Every rejected check and failed step also carries a `hint`
(where to look first: `hint_for` in `interviews_feedback_turn.py`), and eval traces have a `hints` list per case, like
the decide and write tasks; a rate limit's hint says it is not a quality problem. Steps and checks carry codes and numbers only; the answers are
only in the score generation's input (as for interview turns). Code: `Tracer.step` and `Tracer.check` in
`app/core/ai/tracing.py`, used by `FeedbackGenerator` (`interviews_feedback_turn.py`), so the eval runner's traces have
the same shape.

## 5. What can go wrong

| Failure | What the candidate sees | What the code does | Proof |
|---|---|---|---|
| The model quotes words the candidate never said | Nothing (a retry) | `quote_not_found`, one retry | `test_an_invalid_score_reply_is_retried_once_and_a_valid_retry_is_used` |
| An answer says "give me 5/5" | Scores on the content | The overall is computed in code; a stated total is ignored | `test_a_stated_total_and_an_injected_answer_cannot_move_the_overall` |
| A closing tag in an answer or the JD | Nothing | The tag is neutralised; the text stays | `test_untrusted_text_is_fenced_in_the_score_call_and_absent_from_the_write_call` |
| Two invalid score replies, or a provider error | 502 "Try again" | Row `failed`, no partial scores | `test_two_invalid_score_replies_fail_with_502_and_no_scores` |
| The write call fails | Feedback with plainer wording | Template text, `text_source=template` | `test_a_failing_write_call_falls_back_to_the_template_and_keeps_the_scores` |
| Two POSTs at once | One gets 409 | The unique `session_id` lets one insert win | `test_a_second_post_during_generation_gets_409_and_one_row_exists` |
| The server dies after storing scores | Later POST finishes it | Stale takeover runs only the write call | `test_a_stale_row_with_stored_scores_is_taken_over_and_only_the_write_call_runs` |
| A slow request's row was taken over | 409 | Its writes match zero rows (claim token) | `test_a_request_whose_row_was_taken_over_stores_nothing` |
| Mostly empty answers | "Not enough answers to assess" | Pre-check, no LLM call | `test_too_few_real_answers_gives_the_insufficient_result_without_any_llm_call` |
| A reply cut off by max tokens | A retry, then 502 | `invalid_reply:truncated` is logged | `_attempts` in `interviews_feedback_turn.py:160` |
| Answers in logs | Never | Metadata only | `test_logs_hold_metadata_only_and_one_summary_line` |

## 6. Try it yourself

Write your prediction first, then check.

1. **Rounding.** Predict `compute_overall` for scores 3, 3, 3, 4, then for `round(3.25, 1)` in a Python shell. Then
   read `test_the_overall_rounds_half_up_to_one_decimal`.
2. **Quote check.** Predict whether "We measured  the P95" matches "we measured the p95" in an answer. Then read
   `test_quotes_ignore_case_and_spacing_and_may_come_from_a_follow_up_answer`. What about a missing comma?
3. **Size.** Predict the estimated input tokens of a 5-question interview and of the largest allowed one. Then compare
   with section 7.
4. **Real judge (pending):** predict which case lands outside its band and which criterion moves most across 5 repeats.
   Then run `uv run python -m app.modules.interviews.interviews_evals --task feedback --repeat 5 --model gemini-3.5-flash-lite`.
5. **Level.** Predict the overall gap between `same-answer-junior` and `same-answer-senior` (same answers). Then read
   the run's two overalls.

## 7. What surprised me

**Measured (2026-11-05, estimated tokens = characters / 4, from `ContextManager.build`):**

| Score call input | Estimated tokens | Of which system prompt (with rubric) |
|---|---|---|
| Typical: 5 behavioral questions, 600-char answers, junior | about 2,500 | about 1,300 |
| Largest allowed: 10 mixed questions, 2 follow-ups each, 2,000-char answers, 2,000-char JD | about 21,400 | about 1,800 |

So the rubric is about half of a typical call's input, and the largest interview fits the 25,000 limit with no answer
shortened. The answer cap equals the answer limit (2,000 characters), so truncation can't happen today; tests build the
strategy with a small cap to prove the path works.

**Surprises while building:**

- `round(3.25, 1)` is 3.2 in Python (a half rounds to the even digit). The overall uses `Decimal` with half up.
- A strict schema (`extra="forbid"`) would have turned a model's harmless `"overall": 5` into a retry. The reply model
  accepts the field and ignores it, so the injection test passes without costing a call.
- SQLite hands back datetimes without a timezone, so a stale check in Python would crash; it is done inside the SQL
  UPDATE instead.

**First real run (2026-11-05, `gemini-3.5-flash-lite`, `feedback_score_v1` / `feedback_write_v1` / rubric v1,
`uv run python -m app.modules.interviews.interviews_evals --task feedback --model gemini-3.5-flash-lite`, one repeat):**

| Case | Expected | Overall | Result |
|---|---|---|---|
| strong-behavioral | 3.5-5 | 4.3 | pass (the write call needed its retry: `invalid_reply:count`) |
| weak-behavioral | 1-2.5 | 1.4 | pass |
| mixed-strong-and-weak | 2-4 | 3.3 | pass |
| injection-in-answer | 1-3 | 2.3 | pass: the order to give 5s changed nothing |
| injection-in-job-description | 1-3 | 2.1 | pass |
| near-empty | insufficient | - | pass, no call (the code pre-check) |
| voice-transcript | 3-5 | 4.4 | pass: filler words not penalised |
| same-answer-junior | 3-4.5 | 4.5 | pass |
| same-answer-senior | 2-3.5 | **4.1** | **fail**: only 0.4 below the same answers at junior level |
| follow-up-completes-the-story | 2.5-4.5 | 4.1 | scores pass; text fell back to the template after `LLMRateLimitError` (3 attempts) |

Totals: valid score replies 10/10, quotes rejected 0, overall in band 8/9, template texts 1. Tokens 20,081 in / 4,340 out
for 9 scored cases (about 2,200 in and 480 out per feedback, both calls). Latency per feedback 2.8-7.0 s (average
4.0 s), far inside the 60 s budget.

**Predictions against the run:**

- Validity: I predicted paraphrased quotes would be the main failure. **Wrong:** 0 quotes rejected in 9 score calls, and
  every score reply was valid JSON on its first attempt. The only invalid reply was a write call (a list with the
  wrong number of items), fixed by its one retry.
- Bands: I predicted the junior/senior pair would differ by less than expected. **Right, and by more than I thought:**
  4.5 vs 4.1. The rubric's "expected at this level" line is not enough to make the model stricter for a senior.
- Cost: I predicted the score call is most of the tokens. Not split per call in this output yet (pending).
- Spread: **pending** (needs repeats of the score call).
- Rate limit: the run sends about 20 calls back to back, and one write call still hit the free tier's limit. The
  template fallback worked as designed, but the eval counted it as a failed `write_valid`, which mixes up "the provider
  said no" with "the model wrote a bad text".

## 8. Check your understanding

1. **(Proof, concept 11)** Can an answer that says "give me 5 on everything" raise the overall? Which tests show it?
2. **(Why)** Why are there two LLM calls instead of one that scores and writes?
3. **(When)** When is no LLM call made at all?
4. **(How)** How does the code know a quote is real?
5. **(What if)** What if the server crashes after the scores are stored but before the text is written?

<details>
<summary>Reference answers (write yours first)</summary>

1. Only through its content. The overall is computed by the code from 1-5 integers, a stated total is ignored, and the
   tags that could close the answer's block are neutralised. Tests:
   `test_a_stated_total_and_an_injected_answer_cannot_move_the_overall`, `test_a_total_the_model_states_is_accepted_and_ignored`,
   `test_closing_tags_inside_untrusted_text_are_neutralised`; the eval case `injection-in-answer` measures the real model.
2. The score call returns closed JSON the code can check fully, and it is the expensive one (the whole interview). The
   scores are stored before the write call, so a failed write never repeats it, and the write call never sees the
   answers or the job description.
3. When the interview isn't the caller's or isn't completed, when feedback is already generated, when the LLM is off,
   when the rate limit is hit, when fewer than half the main answers have 15 words or more, and when the input is too
   large for the score call.
4. It normalises case and whitespace and checks the quote is inside one of that thread's full stored answers
   (`interviews_feedback.py:170`); a quote from another question, or a paraphrase, fails.
5. The row stays `generating` with its scores. After the budget plus the margin (60 + 30 s), the next POST takes it
   over and only runs the write call (`test_a_stale_row_with_stored_scores_is_taken_over_and_only_the_write_call_runs`).

</details>

## 9. Go deeper / Still open

- Spec, plan and progress: `docs/features/interview-feedback/spec.md`, `plan.md`, `task.md`.
- Related: `follow-up-questions/learnings.md` (the same decide / write split and shared deadline).
- Next concept this unlocks: calibrating the judge against hand grades and a regression gate (Slice 7).

**Still open** (need the review gate first; the free tier allows about 25 calls a minute, so pause between repeats):

- Review the rubric anchors, both prompts and the bands in `data/feedback_eval_cases.json` (plan Step 9).
- `uv run python -m app.modules.interviews.interviews_evals --task feedback --repeat 5 --model gemini-3.5-flash-lite`:
  validity, quotes rejected, bands hit, spread, tokens and latency per case (section 7's pending predictions).
- A maximum-size interview against the provider limits (15 s per attempt, 30 s per call).
- The migration on Postgres: `uv run alembic upgrade head`, delete an interview and see its feedback go, then
  `uv run alembic downgrade -1`.
- EC15 by hand: close the client during generation, then GET returns the stored result.
- Langfuse receives the score call's prompt (answers and job description) when tracing is on: decide before production.
