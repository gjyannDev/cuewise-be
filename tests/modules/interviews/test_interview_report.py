import logging
import uuid

import pytest

from app.core.logging import LOG_FORMAT, request_id_ctx
from app.modules.interviews.interviews_constants import DECISION_TASK, INTERVIEWER_TASK, SUMMARY_TASK
from app.modules.interviews.interviews_log import parse_log
from app.modules.interviews.interviews_model import InterviewMessage, InterviewQuestion, InterviewSession
from app.modules.interviews.interviews_report import analyze_interview, analyze_rollup
from app.modules.interviews.interviews_report_render import render_html, render_text
from app.modules.interviews.interviews_turn import log_llm_call, log_turn_summary
from app.scripts.interview_report import main, read_log_lines

S = uuid.UUID(int=10)
OTHER = uuid.UUID(int=11)
BUDGET = 30.0


@pytest.fixture(autouse=True)
def _reset_request_id():
    yield
    request_id_ctx.set("-")


def session(status="in_progress", count=5, id_=S):
    return InterviewSession(
        id=id_, user_id=uuid.UUID(int=1), role="backend", level="mid", interview_type="mixed", question_count=count, status=status
    )


def question(position, kind="main", main=None, parent=None, category="technical", decide=None, prompt=100, completion=10, source="llm"):
    return InterviewQuestion(
        id=uuid.UUID(int=100 + position),
        session_id=S,
        position=position,
        kind=kind,
        main_number=main or position,
        parent_question_id=parent,
        text="Secret question text",
        category=category,
        source=source,
        prompt_version="interviewer_v4",
        decision_prompt_version=decide,
        prompt_tokens=prompt,
        completion_tokens=completion,
        latency_ms=1000,
    )


def answer(position, chars, role="candidate"):
    return InterviewMessage(session_id=S, question_id=uuid.UUID(int=100 + position), role=role, content="Secret answer "[:1] * chars)


# --- emitting log lines with the app's own log functions, so a format change breaks these tests ---


def emit_call(
    session_id, task, version, *, prompt, completion, ms, left, est, system=700, outcome="ok", action=None, gap=None,
    attempts=1, finish="stop", cached=None,
):  # fmt: skip
    logging.getLogger("app.llm.context").info(
        "context_build task=%s strategy=%s est_tokens=%s system_tokens=%s dropped=%s outcome=%s %s",
        task, "window_ledger", est, system, 0, "ok", "ledger=0 notes=0 summary=1 turns_full=1",
    )  # fmt: skip
    log_llm_call(
        logging.INFO, session_id, outcome, task=task, prompt_version=version, model="test-model", prompt_tokens=prompt,
        completion_tokens=completion, cached_tokens=cached, latency_ms=ms, attempts=attempts, finish=finish,
        budget_left_ms=left, action=action, gap=gap,
    )  # fmt: skip


def emit_http(method, path, status, ms):
    logging.getLogger("app.request").info("%s %s -> %s (%.1fms)", method, path, status, ms)


def emit_start(session_id=S, request="req-start"):
    request_id_ctx.set(request)
    emit_call(session_id, SUMMARY_TASK, "job_description_summary_v2", prompt=444, completion=60, ms=9669, left=None, est=542, outcome="summary_ok")
    emit_call(session_id, INTERVIEWER_TASK, "interviewer_v4", prompt=824, completion=38, ms=6586, left=30000, est=926)
    emit_http("POST", "/api/v1/interviews", 201, 16300.1)


def emit_answer_turn(
    session_id=S, request="req-1", *, decision="next_question", action="next_question", override=None, source="llm",
    fallback=None, llm_ms=5000, decide=(700, 30, 2000), write=(800, 30, 3000), est=800, **write_extra,
):  # fmt: skip
    request_id_ctx.set(request)
    chosen, _, gap = decision.partition(":")
    emit_call(session_id, DECISION_TASK, "follow_up_decision_v1", prompt=decide[0], completion=decide[1], ms=decide[2], left=30000, est=est, action=chosen, gap=gap or None)
    emit_call(session_id, INTERVIEWER_TASK, "interviewer_v4", prompt=write[0], completion=write[1], ms=write[2], left=30000 - decide[2], est=est, **write_extra)
    log_turn_summary(session_id, decision=decision, action=action, override=override, source=source, fallback=fallback, llm_ms=llm_ms)
    emit_http("POST", f"/api/v1/interviews/{session_id}/messages", 201, llm_ms + 20)


def emit_follow_up_turn(session_id=S, request="req-1"):
    """The turn from a real run: a vague answer, `no_example`, 9.7 s to decide and 12.8 s to write."""
    emit_answer_turn(
        session_id, request, decision="follow_up:no_example", action="follow_up", llm_ms=22536,
        decide=(777, 42, 9735), write=(943, 36, 12800), est=1000,
    )  # fmt: skip


def lines_of(app_logs):
    formatter = logging.Formatter(LOG_FORMAT)
    return [formatter.format(record) for record in app_logs.records]


def squash(report):
    """Collapse the table padding so assertions don't depend on column widths."""
    return "\n".join(" ".join(line.split()) for line in report.splitlines())


def analysis(app_logs, questions, messages=(), **session_args):
    return analyze_interview(session(**session_args), questions, messages, parse_log(lines_of(app_logs)), budget_seconds=BUDGET)


def report_for(app_logs, questions, messages=(), **session_args):
    return squash(render_text(analysis(app_logs, questions, messages, **session_args)))


def html_for(app_logs, questions, messages=(), **session_args):
    return render_html(analysis(app_logs, questions, messages, **session_args))


FOLLOW_UP_INTERVIEW = [
    question(1, prompt=824, completion=38),
    question(2, "follow_up", main=1, parent=uuid.UUID(int=101), decide="follow_up_decision_v1", prompt=1720, completion=78),
]


# --- reading the log ---


def test_parse_log_reads_the_apps_own_lines_and_skips_traceback_lines(app_logs):
    emit_follow_up_turn()
    lines = [*lines_of(app_logs), "Traceback (most recent call last):", '  File "x.py", line 1, in f', "ValueError: boom"]

    events = parse_log(lines)

    assert [e.event for e in events if e.event != "POST"][:5] == [
        "context_build", "llm_call", "context_build", "llm_call", "turn_summary",
    ]  # fmt: skip
    decide = next(e for e in events if e.event == "llm_call")
    assert decide.request == "req-1"
    assert decide.fields["task"] == DECISION_TASK
    assert (decide.fields["action"], decide.fields["gap"], decide.fields["latency_ms"]) == ("follow_up", "no_example", "9735")


def test_the_start_the_answers_and_a_request_that_failed_half_way_are_told_apart(app_logs):
    emit_start()
    emit_answer_turn(request="req-1")
    request_id_ctx.set("req-crashed")
    emit_call(S, DECISION_TASK, "follow_up_decision_v1", prompt=700, completion=30, ms=100, left=30000, est=700, action="next_question")
    emit_http("POST", f"/api/v1/interviews/{S}/messages", 500, 150)

    report = report_for(app_logs, [question(1), question(2)])

    assert "start - q1 main#1" in report
    assert "1 q1 main#1 q2 main#2" in report
    assert "partial - - - - - - - 100 150 500 req-crashed" in report


# --- the detail of one interview ---


def test_a_follow_up_turn_is_laid_out_question_by_question(app_logs):
    emit_start()
    emit_follow_up_turn()

    report = report_for(app_logs, FOLLOW_UP_INTERVIEW, [answer(1, 162)])

    assert "log_turns=1 of 1" in report
    assert "start - q1 main#1 - - - - - 16255 16300 201 req-start" in report
    assert "1 q1 main#1 q2 follow_up#1 follow_up:no_example follow_up - llm - 22536 22556 201 req-1" in report
    assert "2 follow_up 1 technical llm interviewer_v4 follow_up_decision_v1 1720/78 1000 -" in report
    assert "1 main 1 technical llm interviewer_v4 - 824/38 1000 162" in report
    assert "models=test-model" in report


def test_every_call_shows_its_usage_budget_estimate_attempts_and_finish(app_logs):
    emit_start()
    emit_follow_up_turn()

    report = report_for(app_logs, FOLLOW_UP_INTERVIEW)

    assert "start jd_summary job_description_summary_v2 444 60 9669 - 542 1 stop summary_ok" in report
    assert "1 decide follow_up_decision_v1 777 42 9735 30000 1000 1 stop ok follow_up/no_example" in report
    assert "1 write interviewer_v4 943 36 12800 20265 1000 1 stop ok" in report


# --- cost ---


def test_cost_adds_up_tokens_and_prices_the_follow_up_feature(app_logs):
    emit_start()
    emit_follow_up_turn(request="req-1")
    emit_answer_turn(request="req-2")  # a move-on turn: decide 700+30, write 800+30
    questions = [question(1), question(2, "follow_up", main=1), question(3)]

    report = report_for(app_logs, questions)

    assert "total 4,724 tokens (in 4,488 + out 236; 4,724 per interview, 2,362 per main question)" in report
    assert "write 3 2,567 104 2,671 57%" in report
    assert "decide 2 1,477 72 1,549 33%" in report
    assert "jd_summary 1 444 60 504 11%" in report
    assert (
        "follow-up feature 2,528 tokens = 54% of all (decide calls on move-on turns 730, "
        "decide calls on follow-up turns 819, follow-up question writes 979)"
    ) in report
    assert "per answer turn follow-up turns avg 1,798 (n=1); move-on turns avg 1,560 (n=1)" in report


# --- effectiveness ---


def test_effectiveness_counts_follow_ups_decisions_and_reliability(app_logs):
    emit_follow_up_turn(request="req-1")
    emit_answer_turn(request="req-2", decision="none", fallback=None)
    questions = [question(1), question(2, "follow_up", main=1), question(3)]

    report = report_for(app_logs, questions)

    assert "follow-ups 1 asked over 2 main questions (0.50 per main question; main questions with at least one: 1)" in report
    assert "decisions follow_up:no_example=1 none=1" in report
    assert "reliability 1 of 2 answer turns (50%) (ran without a failed decide call or a fallback)" in report
    assert "decision quality not measurable from live logs" in report


@pytest.mark.parametrize(
    ("override", "fallback", "ended_by"),
    [(None, None, "model"), ("cap_reached", None, "cap"), ("no_time", "no_time", "time"), (None, "write_failed", "failed")],
)
def test_it_tells_who_closed_a_follow_up_thread(app_logs, override, fallback, ended_by):
    emit_follow_up_turn(request="req-1")
    emit_answer_turn(request="req-2", decision="follow_up:no_example", override=override, fallback=fallback)
    questions = [question(1), question(2, "follow_up", main=1, parent=uuid.UUID(int=101)), question(3)]

    assert f"how threads ended {ended_by}=1" in report_for(app_logs, questions)


def test_a_thread_whose_last_answer_is_not_logged_yet_is_not_counted_as_ended(app_logs):
    emit_follow_up_turn(request="req-1")

    report = report_for(app_logs, [question(1), question(2, "follow_up", main=1)])

    assert "how threads ended none" in report


def test_answer_length_compares_a_follow_up_answer_to_the_answer_it_followed(app_logs):
    questions = [question(1), question(2, "follow_up", main=1), question(3, "follow_up", main=1)]
    messages = [answer(1, 100), answer(2, 250), answer(3, 125), answer(1, 999, role="interviewer")]

    report = report_for(app_logs, questions, messages)

    assert (
        "answer length 1.5x the characters of the answer they followed "
        "(median over 2 follow-up answers; a proxy, not a quality score)"
    ) in report


def test_answer_length_is_not_available_without_an_answered_follow_up(app_logs):
    assert "answer length n/a" in report_for(app_logs, [question(1)], [answer(1, 100)])


# --- efficiency ---


def test_efficiency_reports_time_deadline_and_repeated_prompt(app_logs):
    emit_answer_turn(llm_ms=5000, decide=(700, 30, 2000), write=(800, 30, 3000), est=1000)

    report = report_for(app_logs, [question(1), question(2)])

    assert "decide time 40% (of the LLM time of an answer turn)" in report
    assert "decide 1 2000 2000 2000" in report
    assert "turn llm 1 5000 5000 5000" in report
    assert "busiest turn 17% (5,000 of 30,000 ms turn deadline)" in report
    assert "slowest decide call 20% (2,000 of 10,000 ms decide cap)" in report
    assert "lowest budget left 28,000 ms (at the start of a call)" in report
    assert "fixed system prompt 70% (of the estimated input is the same system prompt every call repeats)" in report
    assert "provider cache hit not reported" in report


def test_the_provider_cache_hit_rate_is_shown_when_reported(app_logs):
    request_id_ctx.set("req-1")
    emit_call(S, INTERVIEWER_TASK, "interviewer_v4", prompt=1000, completion=30, ms=900, left=30000, est=1000, cached=500)
    log_turn_summary(S, decision="next_question", action="next_question", source="llm", llm_ms=900)

    assert "provider cache hit 50%" in report_for(app_logs, [question(1), question(2)])


def test_waste_counts_unusable_replies_retries_and_cut_off_replies(app_logs):
    emit_answer_turn(write=(800, 30, 3000), outcome="invalid_json", attempts=2, finish="length")

    report = report_for(app_logs, [question(1), question(2)])

    assert "waste 1 calls without a usable reply (830 tokens) (1 provider retries; 1 cut off (finish is not stop))" in report
    assert "turn 1: write call outcome=invalid_json" in report
    assert "turn 1: write call needed 2 provider attempts, so its latency hides a retry" in report
    assert "turn 1: write call finish=length (the reply may be cut off)" in report


# --- watch ---


def test_watch_flags_a_decide_call_close_to_its_cap(app_logs):
    emit_start()
    emit_follow_up_turn()

    assert "turn 1: decide call used 97% of its 10s cap (9735 ms)" in report_for(app_logs, FOLLOW_UP_INTERVIEW)


def test_a_healthy_interview_has_nothing_to_flag(app_logs):
    emit_answer_turn(decide=(700, 30, 2000), write=(800, 30, 3000), llm_ms=5000)

    assert "watch\nnothing to flag" in report_for(app_logs, [question(1), question(2)])


def test_watch_explains_an_override_a_fallback_and_a_turn_near_the_deadline(app_logs):
    emit_answer_turn(decision="follow_up:no_tradeoff", override="no_time", source="bank", fallback="no_time", llm_ms=25000)

    report = report_for(app_logs, [question(1), question(2)])

    assert "turn 1: LLM time 25000 ms is 83% of the 30s turn deadline" in report
    assert "turn 1: override=no_time fallback=no_time source=bank" in report
    assert "overrides no_time=1" in report
    assert "fallbacks no_time=1" in report


def test_a_failed_decide_call_is_called_out(app_logs):
    request_id_ctx.set("req-1")
    log_turn_summary(S, decision="none", action="next_question", source="llm", llm_ms=100)

    assert "turn 1: the decide call failed, so no follow-up was possible" in report_for(app_logs, [question(1), question(2)])


def test_lines_of_another_interview_are_left_out(app_logs):
    emit_follow_up_turn(session_id=OTHER, request="req-other")

    report = report_for(app_logs, [question(1), question(2)])

    assert "log_turns=0 of 1" in report
    assert "follow_up:no_example" not in report
    assert "log has 0 of 1 answer turns" in report


def test_missing_log_turns_are_reported(app_logs):
    emit_follow_up_turn()

    assert "log has 1 of 2 answer turns" in report_for(app_logs, [question(1), question(2)], status="completed")


def test_an_abandoned_interview_has_no_expected_turn_count(app_logs):
    report = report_for(app_logs, [question(1)], status="abandoned")

    assert "log_turns=0\n" in report
    assert "log has" not in report


# --- checks ---


def test_every_check_passes_for_a_consistent_follow_up_interview(app_logs):
    emit_start()
    emit_follow_up_turn()

    report = report_for(app_logs, FOLLOW_UP_INTERVIEW)

    assert "FAIL" not in report
    assert "ok log action matches the stored question kind" in report
    assert "ok the turn's call tokens add up to the stored usage" in report


def test_the_log_and_the_database_disagreeing_is_caught(app_logs):
    emit_start()
    emit_follow_up_turn()
    stored_as_main = [question(1, prompt=824, completion=38), question(2, prompt=100, completion=10, source="bank")]

    report = report_for(app_logs, stored_as_main)

    assert "FAIL log action matches the stored question kind: turn 1: log says follow_up, stored main" in report
    assert "FAIL log source matches the stored question source: turn 1: log says llm, stored bank" in report


def test_a_token_mismatch_between_the_log_and_the_stored_usage_is_caught(app_logs):
    emit_start()
    emit_follow_up_turn()
    wrong = [question(1, prompt=824, completion=38), question(2, "follow_up", main=1, parent=uuid.UUID(int=101), prompt=100, completion=10)]

    assert "FAIL the turn's call tokens add up to the stored usage" in report_for(app_logs, wrong)
    assert "turn 1: log 1720/78, stored 100/10" in report_for(app_logs, wrong)


def test_integrity_passes_for_a_well_formed_follow_up_thread(app_logs):
    report = report_for(app_logs, FOLLOW_UP_INTERVIEW)

    assert "FAIL" not in report
    assert report.count("ok ") >= 4


def test_integrity_fails_on_a_third_follow_up_under_one_main_question(app_logs):
    parent = uuid.UUID(int=101)
    questions = [question(1), *(question(n, "follow_up", main=1, parent=parent) for n in (2, 3, 4))]

    assert "FAIL at most 2 follow-ups per main question: main 1 has 3" in report_for(app_logs, questions)


def test_integrity_fails_on_a_follow_up_without_a_parent_or_with_another_category(app_logs):
    orphan = [question(1), question(2, "follow_up", main=1, parent=None)]
    other_category = [question(1), question(2, "follow_up", main=1, parent=uuid.UUID(int=101), category="behavioral")]

    for questions in (orphan, other_category):
        assert "FAIL every follow-up has a main parent with the same main number and category: position 2" in report_for(app_logs, questions)


def test_integrity_fails_on_a_gap_in_the_positions(app_logs):
    assert "FAIL positions run 1..N without gaps" in report_for(app_logs, [question(1), question(3)])


def test_the_report_never_contains_question_or_answer_text(app_logs):  # privacy
    emit_start()
    emit_follow_up_turn()

    report = report_for(app_logs, FOLLOW_UP_INTERVIEW, [answer(1, 50)])

    assert "Secret question" not in report
    assert "Secret answer" not in report


# --- the rollup ---


def rollup_analysis(app_logs, *interviews):
    return analyze_rollup(interviews, parse_log(lines_of(app_logs)), budget_seconds=BUDGET)


def rollup(app_logs, *interviews):
    return squash(render_text(rollup_analysis(app_logs, *interviews)))


def test_the_rollup_has_a_line_per_interview_and_pools_the_numbers(app_logs):
    emit_follow_up_turn(session_id=S, request="req-a")
    emit_answer_turn(session_id=OTHER, request="req-b")  # decide 700/30 + write 800/30 = 1560
    first = (session(id_=S), [question(1), question(2, "follow_up", main=1, parent=uuid.UUID(int=101), prompt=1720, completion=78)], [])
    second = (session(id_=OTHER), [question(1), question(2)], [])

    report = rollup(app_logs, first, second)

    assert "last 2 interviews, newest first" in report
    assert f"{S} in_progress 1 1 1/1 1798 100% 22536 100% ok 1" in report
    # The move-on turn's decide call is feature overhead too (730 of its 1560 tokens); its stored usage (the default
    # 100/10) doesn't match the log, which is the one failed check.
    assert f"{OTHER} in_progress 2 0 1/1 1560 47% 5000 100% 1 0" in report
    assert "total 3,358 tokens (in 3,220 + out 138; 1,679 per interview, 1,119 per main question)" in report
    assert "per answer turn follow-up turns avg 1,798 (n=1); move-on turns avg 1,560 (n=1)" in report
    assert "follow-ups 1 asked over 3 main questions" in report


# --- the script ---


def add_session(db, n, status="completed"):
    db.add(session(status=status, id_=uuid.UUID(int=n)))
    db.commit()


def test_the_script_reports_the_newest_interview_by_default(db):
    add_session(db, 1)
    add_session(db, 2)

    out = main(db, [])

    assert f"interview {uuid.UUID(int=2)}" in out
    assert str(uuid.UUID(int=1)) not in out


def test_the_script_can_report_a_chosen_interview(db):
    add_session(db, 1)
    add_session(db, 2)

    assert f"interview {uuid.UUID(int=1)}" in main(db, [], uuid.UUID(int=1))


def test_the_script_can_pool_the_newest_interviews(db):
    for n in (1, 2, 3):
        add_session(db, n)

    out = main(db, [], last=2)

    assert "last 2 interviews, newest first" in out
    assert str(uuid.UUID(int=3)) in out
    assert str(uuid.UUID(int=2)) in out
    assert str(uuid.UUID(int=1)) not in out


def test_the_script_says_so_when_there_is_no_interview(db):
    assert main(db, []) == "no interview found"
    assert main(db, [], uuid.UUID(int=5)) == "no interview found"
    assert main(db, [], last=3) == "no interview found"


def test_the_script_reads_the_rotated_log_before_the_current_one(tmp_path):
    (tmp_path / "app.log.1").write_text("old\n", encoding="utf-8")
    (tmp_path / "app.log").write_text("new\n", encoding="utf-8")

    assert read_log_lines(tmp_path / "app.log") == ["old", "new"]
    assert read_log_lines(tmp_path / "missing.log") == []


# --- the HTML page ---


def test_the_html_page_fills_the_design_template(app_logs):
    page = html_for(app_logs, FOLLOW_UP_INTERVIEW)

    assert page.startswith("<!doctype html>")
    assert "<title>Interview report</title>" in page
    assert "{{" not in page
    assert '<section class="tiles" aria-label="Headline numbers">' in page
    assert f"<p class=\"sub\">{S}</p>" in page


def test_the_tiles_carry_a_meter_and_a_status_pill_when_a_limit_is_nearly_used(app_logs):
    emit_start()
    emit_follow_up_turn()  # the decide call took 9.7 s of its 10 s cap

    page = html_for(app_logs, FOLLOW_UP_INTERVIEW)

    assert '<div class="tile tone-warn">' in page
    assert '<span class="pill"><i class="icon warn">!</i>Watch</span>' in page
    assert 'aria-label="Slowest decide call" aria-valuemin="0" aria-valuemax="100" aria-valuenow="97"' in page
    assert "<div class=\"value\">9.7 s</div>" in page


def test_a_healthy_interview_shows_no_status_pill_and_a_passed_watch_card(app_logs):
    emit_answer_turn(decide=(700, 30, 2000), write=(800, 30, 3000), llm_ms=5000)

    page = html_for(app_logs, [question(1), question(2)])

    assert '<span class="pill">' not in page
    assert "Nothing to flag" in page


def test_the_token_split_is_a_thin_segmented_bar_beside_its_table(app_logs):
    emit_start()
    emit_follow_up_turn()

    page = html_for(app_logs, FOLLOW_UP_INTERVIEW)

    assert '<div class="seg" role="img" aria-label="write ' in page
    assert '<i class="sw c0"></i>write' in page
    assert '<i class="sw c1"></i>decide' in page


def test_attention_comes_first_then_the_sections_then_the_long_tables(app_logs):
    page = html_for(app_logs, FOLLOW_UP_INTERVIEW)

    order = [page.index(f"<h2>{title}</h2>") for title in ("Watch", "Checks", "cost", "effectiveness", "efficiency", "questions", "turns", "calls")]

    assert order == sorted(order)


def test_failed_checks_show_an_icon_a_word_and_what_was_found(app_logs):
    emit_start()
    emit_follow_up_turn()

    page = html_for(app_logs, [question(1, prompt=824, completion=38), question(2, prompt=100, completion=10, source="bank")])

    assert '<i class="icon bad">×</i>' in page
    assert '<span class="sr">Failed: </span>log source matches the stored question source' in page
    assert '<span class="problems">turn 1: log says llm, stored bank</span>' in page
    assert '<i class="icon ok">✓</i>' in page


def test_number_columns_are_right_aligned_and_ids_are_monospace(app_logs):
    emit_start()
    emit_follow_up_turn()

    page = html_for(app_logs, FOLLOW_UP_INTERVIEW)

    assert '<th scope="col" class="num">llm_ms</th>' in page
    assert '<td class="mono">req-1</td>' in page
    assert '<th scope="col">decision</th>' in page


def test_the_html_escapes_everything_it_prints(app_logs):
    page = analysis(app_logs, [question(1)])
    page.facts[0] = ("role", "<script>alert(1)</script>")

    out = render_html(page)

    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in out
    assert "<script>alert(1)" not in out


def test_the_html_page_never_contains_question_or_answer_text(app_logs):  # privacy
    emit_start()
    emit_follow_up_turn()

    page = html_for(app_logs, FOLLOW_UP_INTERVIEW, [answer(1, 50)])

    assert "Secret question" not in page
    assert "Secret answer" not in page


def test_the_rollup_page_leads_with_the_interviews_table_then_the_pooled_sections(app_logs):
    emit_follow_up_turn(session_id=S, request="req-a")
    first = (session(id_=S), [question(1), question(2, "follow_up", main=1, parent=uuid.UUID(int=101))], [])

    page = render_html(rollup_analysis(app_logs, first))

    assert "<h1>Last 1 interviews</h1>" in page
    assert page.index("<h2>interviews</h2>") < page.index("<h2>cost</h2>") < page.index("<h2>efficiency</h2>")
    assert f"<td class=\"mono\">{S}</td>" in page


def test_the_script_writes_the_html_page_and_says_where(db, tmp_path):
    add_session(db, 1)
    target = tmp_path / "reports" / "report.html"

    out = main(db, [], html_path=target)

    assert target.read_text(encoding="utf-8").startswith("<!doctype html>")
    assert out.endswith(f"html report: {target.resolve()}")
    assert out.startswith(f"interview {uuid.UUID(int=1)}")


def test_calls_logged_before_the_task_name_existed_fold_into_other_so_the_rows_add_up(app_logs):
    emit_answer_turn()
    legacy = (
        f"2026-10-30 10:00:00,000 INFO    [req-old] app.llm: llm_call session={S} model=m prompt_version=interviewer_v1 "
        "prompt_tokens=100 cached_tokens=- completion_tokens=10 reasoning_tokens=- latency_ms=5 attempts=1 finish=stop outcome=ok"
    )
    events = parse_log([*lines_of(app_logs), legacy])

    analysis_ = analyze_interview(session(), [question(1), question(2)], [], events, budget_seconds=BUDGET)
    report = squash(render_text(analysis_))

    assert "other 1 100 10 110 7%" in report
    assert "write 1 800 30 830 50%" in report
    assert "decide 1 700 30 730 44%" in report


def test_a_folder_gets_a_file_named_after_the_interview(db, tmp_path):
    add_session(db, 1)

    out = main(db, [], html_path=tmp_path)

    expected = tmp_path / f"report_{uuid.UUID(int=1)}.html"
    assert expected.read_text(encoding="utf-8").startswith("<!doctype html>")
    assert out.endswith(f"html report: {expected.resolve()}")


def test_each_interview_keeps_its_own_page_and_a_rerun_only_refreshes_that_one(db, tmp_path):
    add_session(db, 1)
    add_session(db, 2)

    main(db, [], uuid.UUID(int=1), html_path=tmp_path)
    main(db, [], uuid.UUID(int=2), html_path=tmp_path)
    first = tmp_path / f"report_{uuid.UUID(int=1)}.html"
    first.write_text("old", encoding="utf-8")
    main(db, [], uuid.UUID(int=2), html_path=tmp_path)

    assert sorted(p.name for p in tmp_path.iterdir()) == [f"report_{uuid.UUID(int=n)}.html" for n in (1, 2)]
    assert first.read_text(encoding="utf-8") == "old"


def test_a_pooled_report_is_named_after_its_size_and_the_newest_interview(db, tmp_path):
    for n in (1, 2, 3):
        add_session(db, n)

    main(db, [], last=2, html_path=tmp_path)

    assert [p.name for p in tmp_path.iterdir()] == [f"rollup_last-2_{uuid.UUID(int=3)}.html"]
