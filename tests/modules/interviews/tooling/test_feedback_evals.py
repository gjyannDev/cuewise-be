"""Step 8 of the feedback plan: the feedback eval task (`--task feedback`). The checks, the summary, the spread and the
Langfuse helpers run against a fake grader; real-model runs are opt-in and never part of pytest."""

import json
import re
from contextlib import nullcontext

import pytest

from app.core.ai.provider import LLMRateLimitError, LLMResult, LLMServerError
from app.core.ai.tracing import Tracer
from app.modules.interviews.ai.interviews_feedback import WriteText
from app.modules.interviews.ai.interviews_feedback_turn import hint_for
from app.modules.interviews.constants.interviews_constants import (
    CATEGORY_CRITERIA,
    FEEDBACK_SCORE_PROMPT_VERSION,
    FEEDBACK_WRITE_PROMPT_VERSION,
    Criterion,
    QuestionCategory,
)
from app.modules.interviews.tooling import interviews_evals as evals_module
from app.modules.interviews.tooling.interviews_evals import main
from app.modules.interviews.tooling.interviews_feedback_evals import (
    FEEDBACK_DATASET,
    FEEDBACK_EVAL_CASES_PATH,
    FeedbackCaseResult,
    FeedbackEvalCase,
    check_feedback,
    criterion_spread,
    feedback_dataset_items,
    feedback_scores_for,
    feedback_trace_output,
    level_gap_check,
    load_feedback_cases,
    run_feedback_case,
    summarize_feedback,
)
from app.modules.interviews.utils.interviews_utils import load_prompt
from tests.fake_langfuse import FakeLangfuse

SCORE_MARKER = load_prompt(FEEDBACK_SCORE_PROMPT_VERSION).splitlines()[1].split("{{")[0]
CASES = load_feedback_cases(FEEDBACK_EVAL_CASES_PATH)
RUN = {"score_max_tokens": 6000, "write_max_tokens": 2000, "score_temperature": 0.2, "budget_seconds": 60}


class Grader:
    """A fake provider: scores every criterion `value`, quoting the start of each thread's first answer, and writes a
    valid text. `score_values` gives one value per score call instead (a spread across repeats)."""

    def __init__(self, value=3, *, score_values=None, quote=None, fail=False, write=True, write_error=None):
        self.value, self.score_values, self.quote, self.fail, self.write_ok = value, score_values, quote, fail, write
        self.write_error = write_error
        self.score_calls = self.write_calls = 0

    def complete(self, messages, **kwargs):
        system, user = messages[0].content, messages[1].content
        if self.fail:
            raise LLMServerError("down", status_code=503)
        if SCORE_MARKER in system:
            value = self.score_values[self.score_calls] if self.score_values else self.value
            self.score_calls += 1
            return _result(self._score(user, value))
        self.write_calls += 1
        if self.write_error is not None:
            raise self.write_error
        numbers = [int(n) for n in re.findall(r"Main question (\d+) \(", user)]
        text = WriteText("Clear answers.", ("One.", "Two."), ("Three.", "Four."), ("Five.",), {n: "Note." for n in numbers})
        return _result(text.render() if self.write_ok else "not the format")

    def _score(self, user, value):
        questions = []
        for block in user.split("<question_thread>")[1:]:
            number, category = re.search(r"Main question (\d+) \((\w+)\)", block).groups()
            answer = re.search(r"<answer>\n(.*?)\n</answer>", block, re.DOTALL).group(1)
            criteria = CATEGORY_CRITERIA[QuestionCategory(category)]
            questions.append(
                {
                    "main_number": int(number),
                    "scores": {c.value: value for c in criteria},
                    "evidence": [{"criterion": criteria[0].value, "quote": self.quote or answer[:40].strip(), "reason": "Shows it."}],
                }
            )
        return json.dumps({"enough_evidence": True, "questions": questions})

    def close(self):
        pass

    async def aclose(self):
        pass


def _result(text):
    return LLMResult(text=text, model="fake", prompt_tokens=100, completion_tokens=40, latency_ms=10, finish_reason="stop", attempts=1)


def case(case_id):
    return next(c for c in CASES if c.id == case_id)


# --- the labelled cases ---


def test_the_cases_cover_every_kind_the_spec_asks_for():  # AC22
    kinds = {c.kind for c in CASES}
    assert {"strong", "weak", "mixed", "injection_answer", "injection_job_description", "near_empty", "voice",
            "level_junior", "level_senior"} <= kinds  # fmt: skip
    assert len(CASES) >= 9 and len({c.id for c in CASES}) == len(CASES)
    junior, senior = case("same-answer-junior"), case("same-answer-senior")
    assert junior.questions == senior.questions and junior.setup.level != senior.setup.level


def test_every_case_states_what_is_expected():  # AC22
    for c in CASES:
        assert c.expect_insufficient or c.expect_overall is not None


@pytest.mark.parametrize(
    "broken",
    [
        {"expect_criteria": {"1:depth": {"low": 1, "high": 2}}},  # a technical criterion on a behavioral question
        {"expect_criteria": {"9:structure": {"low": 1, "high": 2}}},  # no question 9
        {"expect_overall": {"low": 4, "high": 2}},
        {"expect_overall": None},  # nothing expected at all
    ],
)
def test_a_badly_labelled_case_is_rejected(broken):
    data = case("strong-behavioral").model_dump(mode="json") | broken

    with pytest.raises(ValueError):
        FeedbackEvalCase.model_validate(data)


# --- one case through the real feedback steps ---


def test_a_case_in_its_band_passes_every_check():  # AC22
    result = run_feedback_case(Grader(4), case("strong-behavioral"), **RUN)

    assert result.passed and result.error is None and result.overall == 4.0
    assert {c.name for c in result.checks} == {
        "enough_evidence", "overall_in_band", "quotes_verified", "write_valid", "criterion:1:outcome",
        "criterion:1:ownership",
    }  # fmt: skip
    assert result.scores["1:structure"] == 4 and result.text_source == "llm"
    assert result.prompt_tokens == 200 and result.completion_tokens == 80


def test_scores_outside_the_bands_fail_their_checks_with_a_detail():  # AC22
    result = run_feedback_case(Grader(1), case("strong-behavioral"), **RUN)

    failed = {c.name: c.detail for c in result.checks if not c.passed}
    assert failed["overall_in_band"] == "1.0 not in 3.5-5"
    assert failed["criterion:1:outcome"] == "1 not in 4-5"
    assert not result.passed


def test_the_near_empty_case_is_decided_by_the_code_with_no_call():  # AC22, EC9
    grader = Grader()

    result = run_feedback_case(grader, case("near-empty"), **RUN)

    assert result.passed and result.insufficient and grader.score_calls == 0


def test_quotes_rejected_on_both_attempts_make_the_case_an_error():  # AC22, EC11
    result = run_feedback_case(Grader(4, quote="words nobody said in the answer", write=False), case("strong-behavioral"), **RUN)

    assert result.error == "invalid_reply:quote_not_found" and result.quotes_rejected == 2 and not result.passed


def test_the_template_fallback_is_reported_with_why():
    result = run_feedback_case(Grader(4, write=False), case("strong-behavioral"), **RUN)

    assert result.text_source == "template" and result.write_failure == "invalid_reply:format"
    assert [c.detail for c in result.checks if c.name == "write_valid"] == ["template used (invalid_reply:format)"]


def test_a_provider_error_is_the_cases_error():
    result = run_feedback_case(Grader(fail=True), case("strong-behavioral"), **RUN)

    assert result.error == "LLMServerError" and result.checks == [] and not result.passed


# --- the run: summary and spread ---


def test_the_summary_counts_validity_quotes_bands_and_cost():  # AC22
    results = [run_feedback_case(Grader(4), c, **RUN) for c in CASES]

    summary = summarize_feedback(results)

    assert summary.total == len(CASES) and summary.valid == len(CASES)
    assert summary.insufficient == 1 and summary.quotes_rejected == 0
    labelled = [c for c in CASES if c.expect_overall]
    assert summary.overall_labelled == len(labelled)
    assert summary.overall_in_band == sum(c.expect_overall.low <= 4.0 <= c.expect_overall.high for c in labelled)
    assert summary.prompt_tokens > 0 and summary.completion_tokens > 0


def test_the_spread_is_the_largest_move_of_any_criterion_across_repeats():  # AC22, spec goal: spread <= 1
    runs = [[FeedbackCaseResult(case_id="a", checks=[], scores={"1:depth": v, "1:clarity": 3})] for v in (2, 4, 3)]

    assert criterion_spread(runs) == {"a": 2}
    assert criterion_spread(runs[:1]) == {}  # one run has no spread


# --- the level pair: the same answers must score lower at a higher level ---


def test_the_senior_case_is_paired_with_the_junior_case_before_it():
    ids = [c.id for c in CASES]

    assert case("same-answer-senior").lower_than == "same-answer-junior"
    assert ids.index("same-answer-junior") < ids.index("same-answer-senior")


@pytest.mark.parametrize("lower_than", ["a-later-case", "no-such-case"])
def test_a_pair_must_name_an_earlier_case(tmp_path, lower_than):
    first = case("strong-behavioral").model_dump(mode="json") | {"id": "first", "lower_than": lower_than}
    later = case("strong-behavioral").model_dump(mode="json") | {"id": "a-later-case"}
    path = tmp_path / "cases.json"
    path.write_text(json.dumps([first, later]), encoding="utf-8")

    with pytest.raises(ValueError, match="lower_than must name an earlier case"):
        load_feedback_cases(path)


def test_the_higher_level_must_score_at_least_half_a_point_lower():
    senior = case("same-answer-senior")
    junior = {"same-answer-junior": FeedbackCaseResult(case_id="same-answer-junior", checks=[], overall=4.5)}

    def check(overall):
        return level_gap_check(senior, FeedbackCaseResult(case_id=senior.id, checks=[], overall=overall), junior)

    assert check(4.0).passed and check(3.6).passed
    too_close = check(4.4)
    assert not too_close.passed and too_close.detail == "4.4 vs same-answer-junior 4.5: gap 0.1, needs 0.5"
    result = FeedbackCaseResult(case_id=senior.id, checks=[too_close], overall=4.4)
    assert any("experienced line" in h for h in feedback_trace_output(senior, result)["hints"])


def test_nothing_to_compare_is_not_a_level_failure():
    senior, junior = case("same-answer-senior"), FeedbackCaseResult(case_id="same-answer-junior", checks=[], overall=4.5)
    scored = FeedbackCaseResult(case_id=senior.id, checks=[], overall=4.4)
    errored = FeedbackCaseResult(case_id=senior.id, checks=[], error="LLMRateLimitError")
    junior_errored = FeedbackCaseResult(case_id="same-answer-junior", checks=[], error="LLMRateLimitError")

    assert level_gap_check(senior, errored, {"same-answer-junior": junior}) is None
    assert level_gap_check(senior, scored, {"same-answer-junior": junior_errored}) is None
    assert level_gap_check(senior, scored, {}) is None  # the junior did not run in this repeat
    assert level_gap_check(case("strong-behavioral"), scored, {"same-answer-junior": junior}) is None  # no pair


# --- Langfuse (plan step 8) ---


def test_the_dataset_items_carry_the_interview_and_the_expected_bands():
    items = feedback_dataset_items(CASES)

    first = items[0]
    assert first["id"] == f"feedback:{CASES[0].id}" and first["metadata"]["kind"] == CASES[0].kind
    assert first["input"]["questions"][0]["turns"][0]["answer"] == CASES[0].questions[0].turns[0].answer
    assert first["expected_output"]["overall"] == {"low": 3.5, "high": 5.0}
    assert first["expected_output"]["criteria"]["1:outcome"] == {"low": 4, "high": 5}


def test_the_output_and_scores_are_readable():
    c = case("strong-behavioral")
    result = run_feedback_case(Grader(1), c, **RUN)

    output = feedback_trace_output(c, result)
    assert output["verdict"].startswith("FAIL: ") and output["overall"] == 1.0
    assert output["expected_overall"] == {"low": 3.5, "high": 5.0} and output["scores"]["1:outcome"] == 1
    scores = {name: value for name, value, _ in feedback_scores_for(result)}
    assert scores["valid_reply"] is True and scores["overall_in_band"] is False and scores["case_passed"] is False


def test_an_errored_case_scores_only_validity_and_the_verdict():
    result = run_feedback_case(Grader(fail=True), case("strong-behavioral"), **RUN)

    assert feedback_scores_for(result) == [
        ("valid_reply", False, "LLMServerError"),
        ("case_passed", False, "ERROR: LLMServerError"),
    ]


# --- hints in the eval trace, like the decide and write tasks ---


def test_a_passing_case_has_no_hints():
    c = case("strong-behavioral")

    assert feedback_trace_output(c, run_feedback_case(Grader(4), c, **RUN))["hints"] == []


def test_an_out_of_band_case_points_at_the_rubric_and_the_band():
    c = case("strong-behavioral")

    hints = feedback_trace_output(c, run_feedback_case(Grader(1), c, **RUN))["hints"]

    assert any("rubric" in h and "band" in h for h in hints)  # overall_in_band
    assert any("criterion" in h for h in hints)  # criterion:1:outcome, criterion:1:ownership


def test_a_template_text_hint_tells_a_rate_limit_from_a_bad_text():
    c = case("strong-behavioral")
    limited = run_feedback_case(Grader(4, write_error=LLMRateLimitError("429", status_code=429)), c, **RUN)
    badly_written = run_feedback_case(Grader(4, write=False), c, **RUN)

    assert "not a quality problem" in " ".join(feedback_trace_output(c, limited)["hints"])
    assert hint_for("invalid_reply:format") in feedback_trace_output(c, badly_written)["hints"]


def test_an_errored_case_hints_at_its_error():
    c = case("strong-behavioral")

    hints = feedback_trace_output(c, run_feedback_case(Grader(4, quote="words nobody said in the answer"), c, **RUN))["hints"]

    assert hints == [hint_for("invalid_reply:quote_not_found")]


def test_a_case_scored_when_it_should_not_have_been_points_at_the_pre_check():
    c = case("near-empty")
    result = FeedbackCaseResult(case_id=c.id, checks=check_feedback(c, insufficient=False, overall=3.0))

    assert any("pre-check" in h for h in feedback_trace_output(c, result)["hints"])


@pytest.fixture
def lf(monkeypatch):
    """A fake Langfuse client and a fixed git state (feedback runs as a Langfuse experiment, langfuse-experiments Step 10)."""
    monkeypatch.setattr(evals_module, "git_commit", lambda: "abc1234")
    return FakeLangfuse()


def run_main(client, argv, provider):
    tracer = Tracer(client, propagate=lambda **_: nullcontext()) if client is not None else Tracer(None)
    return main(["--task", "feedback", *argv], provider=provider, tracer=tracer)


def test_pause_seconds_spaces_the_feedback_cases_across_repeats():  # free-tier limits: every task, not just RAG
    slept: list[float] = []

    argv = ["--task", "feedback", "--repeat", "2", "--pause-seconds", "1"]
    assert main(argv, provider=Grader(4), tracer=Tracer(None), sleep=slept.append) == 0

    assert slept == [1.0] * (len(CASES) * 2 - 1)  # one wait per case, none before the very first


def trace_of(client, case_id, repeat=1):
    run = client.experiments[repeat - 1]["run_name"]
    return f"trace-{run}-feedback:{case_id}"


def scores_on(client, case_id, repeat=1):
    trace_id = trace_of(client, case_id, repeat)
    return {s["name"]: s for s in client.scores if s.get("trace_id") == trace_id and "run_name" in s}


def test_main_runs_every_case_as_one_run_and_mirrors_the_dataset(lf, capsys):  # AC15, eval-langfuse plan step 8
    assert run_main(lf, [], Grader(4)) == 0

    [run] = lf.experiments
    assert run["item_ids"] == [f"feedback:{c.id}" for c in CASES]
    assert set(lf.datasets) == {FEEDBACK_DATASET} and len(lf.datasets[FEEDBACK_DATASET]) == len(CASES)
    names = set(scores_on(lf, CASES[0].id))
    assert {"valid_reply", "overall_in_band", "quotes_verified", "write_valid", "case_passed", "errored"} <= names
    first = f"feedback:{CASES[0].id}"
    steps = [o for o in lf.observations if o.get("as_type") == "chain" and o["item"] == first]
    assert [s["name"] for s in steps] == ["score", "write"]  # each case's result shows both steps under it
    assert steps[0]["output"]["outcome"] == "ok" and steps[1]["output"]["text_source"] == "llm"
    checks = [o["name"] for o in lf.observations if str(o.get("name", "")).startswith("check-") and o["item"] == first]
    assert checks == ["check-score-reply", "check-write-reply"]
    out = capsys.readouterr().out
    assert "valid replies" in out and "overall in band" in out


def test_each_run_carries_both_prompts_and_its_settings(lf):  # AC2, AC15
    run_main(lf, ["--repeat", "2", "--note", "rubric v3"], Grader(4))

    first, second = lf.experiments
    assert first["run_name"].startswith(f"feedback/{FEEDBACK_SCORE_PROMPT_VERSION}/") and first["run_name"].endswith("/r1")
    meta = first["metadata"]
    assert (meta["prompt.score"], meta["prompt.write"]) == (FEEDBACK_SCORE_PROMPT_VERSION, FEEDBACK_WRITE_PROMPT_VERSION)
    assert {"flag.score_max_tokens", "flag.write_max_tokens", "flag.score_temperature", "flag.budget_seconds"} <= set(meta)
    assert (meta["note"], first["description"], second["metadata"]["repeat"]) == ("rubric v3", "rubric v3", "2")


def test_the_run_scores_equal_the_console_summary(lf, capsys):  # AC15
    run_main(lf, [], Grader(4))

    out = capsys.readouterr().out
    line = re.search(r"passed (\d+)/(\d+)  valid replies (\d+)/\d+  overall in band (\d+)/(\d+).*"
                     r"quotes rejected (\d+)  template texts (\d+)", out)
    passed, total, valid, in_band, labelled, rejected, templates = (int(n) for n in line.groups())
    run = lf.experiments[0]["run_name"]
    assert lf.run_score(run, "pass_rate")["value"] == pytest.approx(passed / total)
    assert lf.run_score(run, "valid_reply_rate")["value"] == pytest.approx(valid / total)
    assert lf.run_score(run, "overall_in_band_rate")["value"] == pytest.approx(in_band / labelled)
    assert lf.run_score(run, "quotes_rejected_count")["value"] == rejected
    assert lf.run_score(run, "template_text_count")["value"] == templates
    assert lf.run_score(run, "errored_count")["value"] == 0.0


def test_cases_run_in_file_order_so_the_senior_case_finds_its_junior_pair(monkeypatch, capsys):  # AC6, AC15
    monkeypatch.setattr(evals_module, "git_commit", lambda: "abc1234")
    reversed_fetch = FakeLangfuse(reverse_fetch=True)

    run_main(reversed_fetch, [], Grader(3))  # the same score at both levels: no gap

    assert reversed_fetch.task_calls == [f"feedback:{c.id}" for c in CASES]
    gap = scores_on(reversed_fetch, "same-answer-senior")["level_gap"]
    assert gap["value"] == 0.0
    assert "level_gap(3.0 vs same-answer-junior 3.0: gap 0, needs 0.5)" in capsys.readouterr().out


def test_with_repeats_the_spread_is_printed_and_posted_on_each_cases_last_run(lf, capsys):  # AC15, AC22 (feedback)
    scored_cases = [c for c in CASES if not c.expect_insufficient]
    values = [3] * len(scored_cases) + [5] * len(scored_cases)

    run_main(lf, ["--repeat", "2"], Grader(score_values=values))

    spreads = [s for s in lf.scores if s["name"] == "criterion_spread_max"]
    assert len(spreads) == len(scored_cases) and all(s["value"] == 2.0 for s in spreads)
    last_run = lf.experiments[1]["run_name"]
    assert all(s["trace_id"].startswith(f"trace-{last_run}-") for s in spreads)
    assert all(s["score_id"] == f"criterion_spread_max-{s['trace_id']}" for s in spreads)
    assert "criterion spread" in capsys.readouterr().out


def test_a_single_run_posts_no_spread(lf):  # EC19
    run_main(lf, [], Grader(4))

    assert not [s for s in lf.scores if s["name"] == "criterion_spread_max"]


def test_a_langfuse_outage_does_not_change_the_run(monkeypatch, capsys):  # EC2
    monkeypatch.setattr(evals_module, "git_commit", lambda: "abc1234")

    assert run_main(FakeLangfuse(fail_run=True), [], Grader(4)) == 0

    out = capsys.readouterr().out
    assert "overall in band" in out and out.rstrip("\n").splitlines()[-1].startswith("Langfuse: not recorded")


def test_without_keys_the_last_line_says_nothing_was_recorded(capsys):  # AC8
    assert run_main(None, [], Grader(4)) == 0

    assert capsys.readouterr().out.rstrip("\n").splitlines()[-1] == "Langfuse: not recorded (no LANGFUSE keys set)."


def test_the_console_shows_a_failing_cases_hints(lf, capsys):
    run_main(lf, [], Grader(1))

    assert "hint: The overall is outside the expected band" in capsys.readouterr().out


def test_the_existing_tasks_are_unchanged():
    assert Criterion.structure in CATEGORY_CRITERIA[QuestionCategory.behavioral]  # imports stay valid
    with pytest.raises(SystemExit):
        main(["--task", "nonsense"], provider=Grader())
