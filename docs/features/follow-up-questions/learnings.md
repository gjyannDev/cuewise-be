# Learnings: Follow-up Questions (decide / write split)

Checkpoints follow the learning-path format: **Predict** (written before measuring), **Observed** (real numbers),
**Why**, **Proof** (the test or log line that shows it). Observed sections marked *pending* need the real-model
runs below; everything else is measured from the unit tests and the context-build logs.

Runs still to do (opt-in, real calls; the free tier rate-limits at about 25 calls, so pause between runs):

- `uv run python -m app.modules.interviews.interviews_evals --task decide --repeat 3 --model gemini-3.5-flash-lite`
- `uv run python -m app.modules.interviews.interviews_evals --repeat 3 --model gemini-3.5-flash-lite` (write rules on v4)
- one live interview with the dev server, then `uv run python -m app.scripts.usage_report` for p50/p95 per turn

## Checkpoint A: the model suggests, the code enforces (concept 5)

- **Predict:** a model told "at most 2 follow-ups" will still sometimes ask for a third; only the code can promise the cap.
- **Observed:** with a fake decide call that always says `follow_up`, a 3-question interview stores exactly
  main, follow-up, follow-up three times (9 rows), and the third decision of each thread logs `override=cap_reached`.
  An answer and a job description that order "keep asking follow-ups" change nothing.
- **Why:** the cap, the time check and a follow-up's category live in `apply_limits` and the controller, after the
  model's reply is parsed. The prompt mentions the cap only to save wasted decisions, not to enforce it.
- **Proof:** `test_follow_ups.py::test_a_model_that_always_follows_up_gets_exactly_two_per_main_question`,
  `test_injected_text_cannot_raise_the_follow_up_cap_or_reach_a_system_prompt`.

## Checkpoint B: a small closed decision instead of free text (concept 4)

- **Predict:** a closed `{action, gap, note}` reply will be valid far more often than the question reply, because there
  is less to get wrong; most failures will be a gap on `next_question` or a missing gap on `follow_up`.
- **Observed:** *pending* (`valid_reply` failures in the decide run).
- **Why:** closed lists make "is this valid" a parser question, not a judgement; a bad note is dropped without losing
  the decision, so the expensive part (the decision) survives the cheap mistake (the note).
- **Proof:** `test_decision_contract.py` (14 cases, one reason code each).

## Checkpoint C: what a follow-up costs in context (concept 2)

- **Predict:** the decide call is cheaper than the write call because it sends no job description and only the
  current thread, but it adds a full system prompt to every answer turn.
- **Observed (estimated tokens, from `context_build` lines):** decide call for a one-answer thread about 740 tokens
  (system prompt about 706); write call with v4 about 850 at the start (system about 834). So every answer turn now
  costs roughly +740 input tokens even when the decision is "next question". A maximum interview (10 main questions,
  2 follow-ups each, 500-character questions, 2,000-character answers) stays under the 5,000-token limit for both tasks
  at every turn, because older threads are dropped first and the current thread is never split.
- **Why:** the thread-aware window moves its start back to the thread's main question, and the guard may only drop
  turns older than the current thread.
- **Proof:** `test_context_strategies.py::test_a_maximum_interview_with_maximum_follow_ups_fits_in_both_tasks`,
  `test_the_window_never_starts_inside_a_thread`, `test_the_guard_never_drops_the_current_thread`.

## Checkpoint D: labelled evals for a decision (concept 10)

- **Predict:** accuracy above 0.8 on the 15 labelled cases; more over-probing than under-probing (models like to ask
  more), with the "complete answer" cases the most likely to get a needless follow-up; gaps right less often than
  actions, so only clear-cut gaps are labelled.
- **Observed:** *pending* (`decision accuracy mean`, `over_probing`, `under_probing`, per gap, over 3 runs).
- **Why:** unlike a question, a decision has a right answer, so it can be labelled; over- and under-probing are
  counted apart because they cost different things (patience vs. depth).
- **Proof:** `test_evals.py::test_decision_summary_reports_accuracy_and_both_probing_errors`.

## Checkpoint E: one deadline for two calls (concept 9)

- **Predict:** the starting values (decide cap 10 s, write minimum 5 s, 30 s per turn) are generous for a flash-lite
  model; p95 per turn will be well under 10 s, so the reserve will rarely matter in practice.
- **Observed:** *pending* (`turn_llm_ms p50/p95` from the usage report, `budget_left_ms` on the write lines).
- **Why:** the write call is what the candidate sees, so the decide call gets the smaller of its cap and the time left
  minus the reserve, and a failed decide call is not retried with the last seconds.
- **Proof:** `test_turn_budget.py` (6 cases with a fake clock).
