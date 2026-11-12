"""Cost, effectiveness and efficiency of the interviewer: for one interview, or pooled over the newest N.

The stored questions and answers (database) are laid beside what the app logged while producing them (see
interviews_log). This module only works the numbers out and returns them as a `Report`: plain data, with no layout in
it. interviews_report_render turns the same `Report` into terminal text or into the HTML page, so the two can never
disagree. Every metric section takes a list of interviews, so one interview and a rollup of ten use the same code.
Numbers, ids and reason codes only: no question, answer or job-description text (an answer is only counted in
characters), the same rule the log lines follow.
"""

import statistics
import uuid
from collections import Counter
from collections.abc import Iterable, Sequence
from dataclasses import dataclass, field

from ..constants.interviews_constants import (
    DECIDE_MAX_SECONDS,
    DECISION_TASK,
    INTERVIEWER_TASK,
    MAX_FOLLOW_UPS,
    SUMMARY_TASK,
    MessageRole,
    QuestionKind,
    QuestionSource,
    SessionStatus,
)
from ..dependencies.models.interviews_model import (
    InterviewMessage,
    InterviewQuestion,
    InterviewSession,
)
from ..tooling.interviews_log import Call, LogEvent, Turn, group_requests, turns_of
from ..utils.interviews_utils import percentile

# A call or turn that used this much of its time limit is flagged: a slower reply would have been cut off.
WATCH_RATIO = 0.8
# Reliability below this is a problem, not just a warning.
BAD_RELIABILITY = 0.8
OK_OUTCOMES = {"ok", "summary_ok"}
TASK_NAMES = {INTERVIEWER_TASK: "write", DECISION_TASK: "decide", SUMMARY_TASK: "jd_summary"}


# --- what a report is made of (layout-free) ---


@dataclass
class Metric:
    """One number with its meaning. `fraction` (0..1) draws a meter in the HTML; `tone` is "warn" or "bad"."""

    label: str
    value: str
    detail: str = ""
    fraction: float | None = None
    tone: str = ""


@dataclass
class Table:
    title: str
    header: list[str]
    rows: list[list[str]]
    note: str = ""
    # Each row's share of one whole (first column names the part): the HTML draws them as a thin segmented bar.
    shares: list[float] | None = None
    # A long table that backs up the summary: the HTML puts it after the sections.
    detail: bool = False


@dataclass
class Section:
    title: str
    question: str
    metrics: list[Metric]
    tables: list[Table] = field(default_factory=list)


@dataclass
class Watch:
    notes: list[str]


@dataclass
class Checks:
    # Each check with the problems it found (none = passed).
    items: list[tuple[str, list[str]]]


Block = Section | Table | Watch | Checks


@dataclass
class Report:
    title: str
    heading: str
    subtitle: str
    facts: list[tuple[str, str]]
    tiles: list[Metric]
    blocks: list[Block]


@dataclass
class Bundle:
    """Everything known about one interview: its stored rows and its logged turns."""

    session: InterviewSession
    questions: Sequence[InterviewQuestion]
    turns: list[Turn]
    # Characters in the candidate's answer to each question: the length only, never the text.
    answer_chars: dict[uuid.UUID, int]

    @property
    def calls(self) -> list[Call]:
        return [call for turn in self.turns for call in turn.calls]

    @property
    def answered(self) -> list[Turn]:
        return [turn for turn in self.turns if turn.summary]

    @property
    def expected_answers(self) -> int | None:
        """How many answers the stored questions imply, or None when it can't be told (an abandoned interview)."""
        if self.session.status == SessionStatus.completed:
            return len(self.questions)
        if self.session.status == SessionStatus.in_progress:
            return max(len(self.questions) - 1, 0)
        return None


Interview = tuple[InterviewSession, Sequence[InterviewQuestion], Sequence[InterviewMessage]]


@dataclass
class Stats:
    """The numbers the sections and tiles share, worked out once over a list of interviews."""

    bundles: Sequence[Bundle]
    turns: list[Turn]
    calls: list[Call]
    answered: list[Turn]
    summaries: list[dict[str, str]]
    following: list[Turn]
    moving: list[Turn]
    mains: int
    follow_ups: int
    threads: int
    endings: Counter[str]
    growth: list[float]
    total: int
    decide_moving: int
    decide_following: int
    follow_writes: int
    turn_ms: list[int]
    clean: int

    @property
    def feature(self) -> int:
        return self.decide_moving + self.decide_following + self.follow_writes


# --- building a report ---


def analyze_interview(
    session: InterviewSession,
    questions: Sequence[InterviewQuestion],
    messages: Sequence[InterviewMessage],
    events: Iterable[LogEvent],
    *,
    budget_seconds: float,
) -> Report:
    bundle = _bundle((session, questions, messages), group_requests(events))
    stats = _stats([bundle])
    return Report(
        title=f"interview {session.id}",
        heading="Interview report",
        subtitle=str(session.id),
        facts=_facts(bundle),
        tiles=_tiles(stats, budget_seconds),
        blocks=[
            _question_table(bundle),
            _turn_table(bundle),
            _call_table(bundle),
            _cost(stats),
            _effectiveness(stats),
            _efficiency(stats, budget_seconds),
            Watch(_watch_notes(bundle, budget_seconds)),
            Checks(_checks(bundle)),
        ],
    )


def analyze_rollup(interviews: Sequence[Interview], events: Iterable[LogEvent], *, budget_seconds: float) -> Report:
    """The same metric sections pooled over several interviews, plus one line per interview."""
    requests = group_requests(events)
    bundles = [_bundle(interview, requests) for interview in interviews]
    stats = _stats(bundles)
    return Report(
        title=f"last {len(bundles)} interviews, newest first; the numbers below are pooled over all of them",
        heading=f"Last {len(bundles)} interviews",
        subtitle="Newest first. The numbers are pooled over all of them.",
        facts=[],
        tiles=_tiles(stats, budget_seconds),
        blocks=[
            _rollup_table(bundles, budget_seconds),
            _cost(stats),
            _effectiveness(stats),
            _efficiency(stats, budget_seconds),
        ],
    )


def _bundle(interview: Interview, requests: dict[str, list[LogEvent]]) -> Bundle:
    session, questions, messages = interview
    chars = {m.question_id: len(m.content) for m in messages if m.role == MessageRole.candidate}
    return Bundle(session, questions, turns_of(requests, str(session.id)), chars)


def _stats(bundles: Sequence[Bundle]) -> Stats:
    turns = [t for b in bundles for t in b.turns]
    calls = [c for t in turns for c in t.calls]
    answered = [t for t in turns if t.summary]
    summaries = [t.summary for t in answered if t.summary]
    following = [t for t in answered if t.summary and t.summary.get("action") == "follow_up"]
    moving = [t for t in answered if t.summary and t.summary.get("action") != "follow_up"]
    questions = [q for b in bundles for q in b.questions]

    def decide(group: Sequence[Turn]) -> int:
        return sum(c.tokens for t in group for c in t.calls if c.task == DECISION_TASK)

    return Stats(
        bundles=bundles,
        turns=turns,
        calls=calls,
        answered=answered,
        summaries=summaries,
        following=following,
        moving=moving,
        mains=sum(1 for q in questions if q.kind == QuestionKind.main),
        follow_ups=sum(1 for q in questions if q.kind == QuestionKind.follow_up),
        threads=sum(len({q.main_number for q in b.questions if q.kind == QuestionKind.follow_up}) for b in bundles),
        endings=sum((_thread_endings(b) for b in bundles), Counter()),
        growth=[ratio for b in bundles for ratio in _answer_growth(b)],
        total=sum(c.tokens for c in calls),
        decide_moving=decide(moving),
        decide_following=decide(following),
        # Without the feature an answer turn is one write that asks the next main question; a follow-up turn's write
        # is an extra question on top of the main ones, and every answer turn also pays a decide call.
        follow_writes=sum(c.tokens for t in following for c in t.calls if c.task == INTERVIEWER_TASK),
        turn_ms=[t.llm_ms for t in answered if t.llm_ms is not None],
        clean=sum(1 for s in summaries if s.get("fallback", "-") == "-" and s.get("decision") != "none"),
    )


def _facts(b: Bundle) -> list[tuple[str, str]]:
    models = ", ".join(sorted({c.model for c in b.calls if c.model != "-"})) or "-"
    expected = b.expected_answers
    return [
        ("role", b.session.role),
        ("level", b.session.level),
        ("type", b.session.interview_type),
        ("main_questions", str(b.session.question_count)),
        ("status", b.session.status),
        ("stored_questions", str(len(b.questions))),
        ("follow_ups", str(sum(1 for q in b.questions if q.kind == QuestionKind.follow_up))),
        ("models", models),
        ("log_turns", f"{len(b.answered)}{'' if expected is None else f' of {expected}'}"),
        *_retrieval_fact(b),
    ]


def _retrieval_fact(b: Bundle) -> list[tuple[str, str]]:
    """The reference notes the interview got at start, as ids-free metadata; nothing for interviews from before them."""
    found = next((turn.retrieval for turn in b.turns if turn.retrieval), None)
    if found is None:
        return []
    parts = [
        found.get("mode", "-"),
        f"{found.get('count', '0')} notes",
        f"scores {found.get('scores', '-')}",
        found.get("outcome", "-"),
        f"{found.get('latency_ms', '-')} ms",
    ]
    return [("reference_notes", ", ".join(parts))]


# --- the headline tiles ---


def _tiles(s: Stats, budget_seconds: float) -> list[Metric]:
    budget_ms, cap_ms = budget_seconds * 1000, DECIDE_MAX_SECONDS * 1000
    slowest_turn = max(s.turn_ms, default=0)
    slowest_decide = max((c.latency_ms or 0 for c in s.calls if c.task == DECISION_TASK), default=0)
    reliability = _ratio(s.clean, len(s.answered))
    turn_used, decide_used = _ratio(slowest_turn, budget_ms), _ratio(slowest_decide, cap_ms)
    return [
        Metric("Tokens", f"{s.total:,}", f"{round(s.total / len(s.bundles)):,} per interview" if s.bundles else ""),
        Metric("Follow-up feature", _pct(s.feature, s.total), f"{s.feature:,} of those tokens", _ratio(s.feature, s.total)),
        Metric("Follow-ups asked", str(s.follow_ups), f"over {s.mains} main questions"),
        Metric(
            "Reliability",
            _pct(s.clean, len(s.answered)),
            f"{s.clean} of {len(s.answered)} answer turns ran clean",
            reliability,
            _reliability_tone(reliability),
        ),
        Metric(
            "Slowest turn",
            _seconds(slowest_turn),
            f"{_pct(slowest_turn, budget_ms)} of the {budget_seconds:g} s deadline",
            turn_used,
            _limit_tone(turn_used),
        ),
        Metric(
            "Slowest decide call",
            _seconds(slowest_decide),
            f"{_pct(slowest_decide, cap_ms)} of its {DECIDE_MAX_SECONDS:g} s cap",
            decide_used,
            _limit_tone(decide_used),
        ),
    ]


# --- one interview, in detail ---


def _question_table(b: Bundle) -> Table:
    rows = [
        [
            q.position,
            q.kind,
            q.main_number,
            q.category,
            q.source,
            _dash(q.prompt_version),
            _dash(q.decision_prompt_version),
            f"{_dash(q.prompt_tokens)}/{_dash(q.completion_tokens)}",
            _dash(q.latency_ms),
            _dash(b.answer_chars.get(q.id)),
        ]
        for q in b.questions
    ]
    header = ["pos", "kind", "main", "category", "source", "write_prompt", "decide_prompt", "tokens_in/out", "llm_ms", "answer_chars"]
    return Table("questions", header, _strings(rows), "database; usage is the whole turn that produced the question", detail=True)


def _turn_table(b: Bundle) -> Table:
    """Turn N answers the question at position N and asks position N+1: positions are one sequential counter."""
    by_position = {q.position: q for q in b.questions}
    rows = []
    for turn in b.turns:
        s = turn.summary or {}
        number = int(turn.label) if turn.label.isdigit() else None
        asked_position = 1 if turn.is_start else (number + 1 if number else None)
        rows.append(
            [
                turn.label,
                _tag(by_position[number]) if number in by_position else "-",
                _tag(by_position[asked_position]) if asked_position in by_position else "-",
                s.get("decision", "-"),
                s.get("action", "-"),
                s.get("override", "-"),
                s.get("source", "-"),
                s.get("fallback", "-"),
                _dash(turn.llm_ms),
                _dash(turn.http_ms),
                turn.status or "-",
                turn.request,
            ]
        )
    header = ["turn", "answered", "asked", "decision", "action", "override", "source", "fallback", "llm_ms", "http_ms", "http", "request"]
    note = "log; llm_ms = LLM time, http_ms = what the browser waited, request = id to search the log for"
    return Table("turns", header, _strings(rows), note, detail=True)


def _call_table(b: Bundle) -> Table:
    rows = [
        [
            turn.label,
            TASK_NAMES.get(c.task, c.task),
            c.prompt_version,
            _dash(c.prompt_tokens),
            _dash(c.completion_tokens),
            _dash(c.latency_ms),
            _dash(c.budget_left_ms),
            _dash(c.est_tokens),
            _dash(c.attempts),
            c.finish,
            c.outcome + (f" {c.action}/{c.gap or '-'}" if c.action else ""),
        ]
        for turn in b.turns
        for c in turn.calls
    ]
    header = ["turn", "call", "prompt_version", "in", "out", "ms", "budget_left", "est_in", "attempts", "finish", "outcome"]
    return Table("calls", header, _strings(rows), "log; every LLM call, in order", detail=True)


# --- the three questions: what does it cost, does it work, is it efficient ---


def _cost(s: Stats) -> Section:
    purpose_rows: list[list[str]] = []
    shares: list[float] = []
    # Calls logged before the task name existed (older interviews) fold into "other", so the rows add up to the total.
    groups = {name: [c for c in s.calls if c.task == task] for task, name in TASK_NAMES.items()}
    groups["other"] = [c for c in s.calls if c.task not in TASK_NAMES]
    for name, group in groups.items():
        if not group:
            continue
        tokens = sum(c.tokens for c in group)
        purpose_rows.append(
            _strings([[name, len(group), _n(sum(c.prompt_tokens or 0 for c in group)), _n(sum(c.completion_tokens or 0 for c in group)), _n(tokens), _pct(tokens, s.total)]])[0]
        )
        shares.append(tokens / s.total if s.total else 0)
    in_out = f"in {_total(c.prompt_tokens for c in s.calls)} + out {_total(c.completion_tokens for c in s.calls)}"
    return Section(
        "cost",
        "tokens, from the log",
        [
            Metric("total", f"{_n(s.total)} tokens", f"{in_out}; {_per(s.total, len(s.bundles))} per interview, {_per(s.total, s.mains)} per main question"),
            Metric(
                "follow-up feature",
                f"{_n(s.feature)} tokens = {_pct(s.feature, s.total)} of all",
                f"decide calls on move-on turns {_n(s.decide_moving)}, decide calls on follow-up turns {_n(s.decide_following)}, "
                f"follow-up question writes {_n(s.follow_writes)}",
                _ratio(s.feature, s.total),
            ),
            Metric(
                "per answer turn",
                f"follow-up turns avg {_avg([_turn_tokens(t) for t in s.following])} (n={len(s.following)}); "
                f"move-on turns avg {_avg([_turn_tokens(t) for t in s.moving])} (n={len(s.moving)})",
            ),
        ],
        [Table("tokens by purpose", ["purpose", "calls", "in", "out", "total", "share"], purpose_rows, "from the log", shares=shares)],
    )


def _effectiveness(s: Stats) -> Section:
    reliability = _ratio(s.clean, len(s.answered))
    overrides = Counter(x["override"] for x in s.summaries if x.get("override", "-") != "-")
    fallbacks = Counter(x["fallback"] for x in s.summaries if x.get("fallback", "-") != "-")
    if s.growth:
        length = Metric(
            "answer length",
            f"{statistics.median(s.growth):.1f}x the characters of the answer they followed",
            f"median over {len(s.growth)} follow-up answers; a proxy, not a quality score",
        )
    else:
        length = Metric("answer length", "n/a", "no answered follow-up yet")
    return Section(
        "effectiveness",
        "does the follow-up feature do its job",
        [
            Metric(
                "follow-ups",
                f"{s.follow_ups} asked over {s.mains} main questions",
                f"{_per(s.follow_ups, s.mains, 2)} per main question; main questions with at least one: {s.threads}",
            ),
            Metric("decisions", _counts(Counter(x.get("decision", "-") for x in s.summaries))),
            Metric(
                "how threads ended",
                _counts(s.endings),
                "model = it decided to move on; cap / time = the code stopped it; failed = a call failed",
            ),
            Metric("overrides", _counts(overrides)),
            Metric("fallbacks", _counts(fallbacks)),
            # A turn that completes the interview asks no question, so it has no source.
            Metric("sources", _counts(Counter(x["source"] for x in s.summaries if x.get("source", "-") != "-"))),
            Metric(
                "reliability",
                f"{s.clean} of {len(s.answered)} answer turns ({_pct(s.clean, len(s.answered))})",
                "ran without a failed decide call or a fallback",
                reliability,
                _reliability_tone(reliability),
            ),
            length,
            Metric(
                "decision quality",
                "not measurable from live logs",
                "run the eval runner with --task decide for accuracy, over- and under-probing",
            ),
        ],
    )


def _efficiency(s: Stats, budget_seconds: float) -> Section:
    budget_ms, cap_ms = budget_seconds * 1000, DECIDE_MAX_SECONDS * 1000
    decide_ms = sum(c.latency_ms or 0 for t in s.answered for c in t.calls if c.task == DECISION_TASK)
    decide_calls = [c.latency_ms for c in s.calls if c.task == DECISION_TASK and c.latency_ms is not None]
    busiest, slowest_decide = max(s.turn_ms, default=0), max(decide_calls, default=0)
    low = min((c.budget_left_ms for c in s.calls if c.budget_left_ms is not None), default=None)
    sized = [c for c in s.calls if c.system_tokens is not None and c.est_tokens]
    system = sum(c.system_tokens or 0 for c in sized)
    cached = [c for c in s.calls if c.cached_tokens is not None and c.prompt_tokens]
    failed = [c for c in s.calls if c.outcome not in OK_OUTCOMES]
    retried = [c for c in s.calls if (c.attempts or 1) > 1]
    cut_off = [c for c in s.calls if c.finish not in ("stop", "-")]
    drift = {
        name: [
            round((c.est_tokens / c.prompt_tokens - 1) * 100)
            for c in s.calls
            if c.task == task and c.est_tokens is not None and c.prompt_tokens
        ]
        for task, name in TASK_NAMES.items()
    }
    shown = [f"{name} {sum(v) / len(v):+.0f}%" for name, v in drift.items() if v]
    latency = [
        _latency_row(name, [c.latency_ms for c in s.calls if c.task == task and c.latency_ms is not None])
        for task, name in TASK_NAMES.items()
    ]
    latency += [_latency_row("turn llm", s.turn_ms), _latency_row("request", [t.http_ms for t in s.turns if t.http_ms is not None])]
    return Section(
        "efficiency",
        "time, deadline, repeated and wasted tokens",
        [
            Metric("decide time", _pct(decide_ms, sum(s.turn_ms)), "of the LLM time of an answer turn", _ratio(decide_ms, sum(s.turn_ms))),
            Metric(
                "busiest turn",
                _pct(busiest, budget_ms),
                f"{_n(busiest)} of {_n(round(budget_ms))} ms turn deadline",
                _ratio(busiest, budget_ms),
                _limit_tone(_ratio(busiest, budget_ms)),
            ),
            Metric(
                "slowest decide call",
                _pct(slowest_decide, cap_ms),
                f"{_n(slowest_decide)} of {_n(round(cap_ms))} ms decide cap",
                _ratio(slowest_decide, cap_ms),
                _limit_tone(_ratio(slowest_decide, cap_ms)),
            ),
            Metric("lowest budget left", f"{'-' if low is None else _n(low)} ms", "at the start of a call"),
            Metric(
                "fixed system prompt",
                _pct(system, sum(c.est_tokens or 0 for c in sized)),
                "of the estimated input is the same system prompt every call repeats",
                _ratio(system, sum(c.est_tokens or 0 for c in sized)),
            ),
            Metric(
                "provider cache hit",
                _pct(sum(c.cached_tokens or 0 for c in cached), sum(c.prompt_tokens or 0 for c in cached)) if cached else "not reported",
                "share of input tokens served from the provider's prompt cache",
                _ratio(sum(c.cached_tokens or 0 for c in cached), sum(c.prompt_tokens or 0 for c in cached)) if cached else None,
            ),
            Metric(
                "waste",
                f"{len(failed)} calls without a usable reply ({_n(sum(c.tokens for c in failed))} tokens)",
                f"{len(retried)} provider retries; {len(cut_off)} cut off (finish is not stop)",
                tone="warn" if failed or retried or cut_off else "",
            ),
            Metric("estimate", ", ".join(shown) or "-", "context estimate vs provider input tokens, est/actual-1"),
        ],
        [Table("latency", ["call", "n", "p50", "p95", "max"], [row for row in latency if row], "milliseconds, from the log")],
    )


def _latency_row(name: str, values: Sequence[int | None]) -> list[str]:
    known = sorted(v for v in values if v is not None)
    if not known:
        return []
    return [name, str(len(known)), str(percentile(known, 50)), str(percentile(known, 95)), str(known[-1])]


def _turn_tokens(turn: Turn) -> int:
    return sum(c.tokens for c in turn.calls)


def _thread_endings(b: Bundle) -> Counter[str]:
    """How each follow-up thread was closed, read from the turn that answered its last question.

    A thread whose last stored row is a follow-up can only have been closed by that answer (a follow-up is never
    allowed past the cap), so the turn's override and fallback say who stopped it.
    """
    by_label = {t.label: t for t in b.answered}
    last_of_thread: dict[int, InterviewQuestion] = {}
    for q in b.questions:  # ordered by position, so the last row of a thread wins
        last_of_thread[q.main_number] = q
    endings: Counter[str] = Counter()
    for q in last_of_thread.values():
        turn = by_label.get(str(q.position))
        if q.kind != QuestionKind.follow_up or turn is None or turn.summary is None:
            continue  # no follow-up in this thread, or its last answer isn't in the log yet
        s = turn.summary
        if s.get("override") == "cap_reached":
            endings["cap"] += 1
        elif s.get("override") == "no_time":
            endings["time"] += 1
        elif s.get("fallback", "-") != "-":
            endings["failed"] += 1
        else:
            endings["model"] += 1
    return endings


def _answer_growth(b: Bundle) -> list[float]:
    """Each follow-up answer's length relative to the answer before it (characters only)."""
    by_position = {q.position: q for q in b.questions}
    ratios = []
    for q in b.questions:
        previous = by_position.get(q.position - 1)
        now, before = b.answer_chars.get(q.id), previous and b.answer_chars.get(previous.id)
        if q.kind == QuestionKind.follow_up and now is not None and before:
            ratios.append(now / before)
    return ratios


# --- what to look at, and whether the data agrees with itself ---


def _watch_notes(b: Bundle, budget_seconds: float) -> list[str]:
    """Time limits nearly used up, failed or odd calls, overrides, fallbacks, missing log lines."""
    notes: list[str] = []
    expected = b.expected_answers
    if expected is not None and len(b.answered) < expected:
        notes.append(
            f"log has {len(b.answered)} of {expected} answer turns: older lines may have rotated away, or the interview predates the logs"
        )
    for turn in b.turns:
        for c in turn.calls:
            name = TASK_NAMES.get(c.task, c.task)
            if c.task == DECISION_TASK and c.latency_ms is not None:
                used = c.latency_ms / (DECIDE_MAX_SECONDS * 1000)
                if used >= WATCH_RATIO:
                    notes.append(f"turn {turn.label}: decide call used {used:.0%} of its {DECIDE_MAX_SECONDS:g}s cap ({c.latency_ms} ms)")
            if c.outcome not in OK_OUTCOMES:
                notes.append(f"turn {turn.label}: {name} call outcome={c.outcome}")
            if (c.attempts or 1) > 1:
                notes.append(f"turn {turn.label}: {name} call needed {c.attempts} provider attempts, so its latency hides a retry")
            if c.finish not in ("stop", "-"):
                notes.append(f"turn {turn.label}: {name} call finish={c.finish} (the reply may be cut off)")
        s = turn.summary or {}
        if turn.summary and turn.llm_ms is not None and turn.llm_ms >= WATCH_RATIO * budget_seconds * 1000:
            notes.append(f"turn {turn.label}: LLM time {turn.llm_ms} ms is {turn.llm_ms / (budget_seconds * 1000):.0%} of the {budget_seconds:g}s turn deadline")
        if s.get("override", "-") != "-" or s.get("fallback", "-") != "-":
            notes.append(f"turn {turn.label}: override={s.get('override', '-')} fallback={s.get('fallback', '-')} source={s.get('source', '-')}")
        if s.get("decision") == "none":
            notes.append(f"turn {turn.label}: the decide call failed, so no follow-up was possible")
    return notes


def _checks(b: Bundle) -> list[tuple[str, list[str]]]:
    """Each check with the problems it found (none = passed)."""
    by_id = {q.id: q for q in b.questions}
    follow_ups = [q for q in b.questions if q.kind == QuestionKind.follow_up]
    per_main = Counter(q.main_number for q in follow_ups)
    positions = [q.position for q in b.questions]
    mains = [q.main_number for q in b.questions if q.kind == QuestionKind.main]

    def bad_parent(q: InterviewQuestion) -> bool:
        parent = by_id.get(q.parent_question_id)
        return parent is None or parent.kind != QuestionKind.main or (parent.main_number, parent.category) != (q.main_number, q.category)

    return [
        ("positions run 1..N without gaps", [] if positions == list(range(1, len(positions) + 1)) else [f"found {positions}"]),
        ("main questions are numbered 1..K", [] if mains == list(range(1, len(mains) + 1)) else [f"found {mains}"]),
        (f"at most {MAX_FOLLOW_UPS} follow-ups per main question", [f"main {m} has {n}" for m, n in sorted(per_main.items()) if n > MAX_FOLLOW_UPS]),
        ("every follow-up has a main parent with the same main number and category", [f"position {q.position}" for q in follow_ups if bad_parent(q)]),
        *_consistency(b),
    ]


def _consistency(b: Bundle) -> list[tuple[str, list[str]]]:
    """Does what the log says happened match what was stored? These guard the numbers above."""
    by_position = {q.position: q for q in b.questions}
    kinds: list[str] = []
    sources: list[str] = []
    tokens: list[str] = []
    for turn in b.turns:
        if turn.is_start:
            asked = by_position.get(1)
        elif turn.label.isdigit():
            asked = by_position.get(int(turn.label) + 1)
        else:
            continue
        if asked is None:
            continue  # the interview ended on this answer
        if turn.summary:
            action, source = turn.summary.get("action"), turn.summary.get("source")
            expected_kind = QuestionKind.follow_up if action == "follow_up" else QuestionKind.main
            if asked.kind != expected_kind:
                kinds.append(f"turn {turn.label}: log says {action}, stored {asked.kind}")
            if source in {QuestionSource.llm, QuestionSource.bank} and asked.source != source:
                sources.append(f"turn {turn.label}: log says {source}, stored {asked.source}")
        counted = [c for c in turn.calls if c.task != SUMMARY_TASK]
        if asked.source == QuestionSource.llm and counted:
            logged = (sum(c.prompt_tokens or 0 for c in counted), sum(c.completion_tokens or 0 for c in counted))
            stored = (asked.prompt_tokens or 0, asked.completion_tokens or 0)
            if logged != stored:
                tokens.append(f"turn {turn.label}: log {logged[0]}/{logged[1]}, stored {stored[0]}/{stored[1]}")
    return [
        ("log action matches the stored question kind", kinds),
        ("log source matches the stored question source", sources),
        ("the turn's call tokens add up to the stored usage (the jd summary is not part of a question)", tokens),
    ]


# --- the rollup's one line per interview ---


def _rollup_table(bundles: Sequence[Bundle], budget_seconds: float) -> Table:
    rows = []
    for b in bundles:
        s = _stats([b])
        expected = b.expected_answers
        rows.append(
            [
                b.session.id,
                b.session.status,
                s.mains,
                s.follow_ups,
                f"{len(b.answered)}/{_dash(expected)}",
                s.total,
                _pct(s.feature, s.total),
                percentile(sorted(s.turn_ms), 95) if s.turn_ms else "-",
                _pct(s.clean, len(s.answered)),
                sum(1 for _, problems in _checks(b) if problems) or "ok",
                len(_watch_notes(b, budget_seconds)),
            ]
        )
    header = ["interview", "status", "main", "follow_ups", "log_turns", "tokens", "feature", "turn_p95_ms", "reliable", "failed_checks", "watch_notes"]
    return Table("interviews", header, _strings(rows), "newest first")


# --- small helpers for values ---


def _strings(rows: Sequence[Sequence[object]]) -> list[list[str]]:
    return [[str(cell) for cell in row] for row in rows]


def _tag(q: InterviewQuestion) -> str:
    return f"q{q.position} {q.kind}#{q.main_number}"


def _dash(value: object) -> str:
    return "-" if value is None else str(value)


def _total(values: Iterable[int | None]) -> str:
    known = [v for v in values if v is not None]
    return f"{sum(known):,}" if known else "-"


def _ratio(part: float, whole: float) -> float | None:
    return part / whole if whole else None


def _pct(part: float, whole: float) -> str:
    return f"{part / whole:.0%}" if whole else "n/a"


def _per(total: float, count: int, digits: int = 0) -> str:
    return f"{total / count:,.{digits}f}" if count else "-"


def _avg(values: Sequence[int]) -> str:
    return _per(sum(values), len(values))


def _n(value: int) -> str:
    return f"{value:,}"


def _seconds(ms: int) -> str:
    return f"{ms / 1000:.1f} s" if ms else "-"


def _counts(counter: Counter[str]) -> str:
    return " ".join(f"{key}={count}" for key, count in sorted(counter.items())) or "none"


def _limit_tone(used: float | None) -> str:
    """How close something is to its time limit."""
    if used is None:
        return ""
    return "bad" if used >= 1 else "warn" if used >= WATCH_RATIO else ""


def _reliability_tone(reliability: float | None) -> str:
    if reliability is None:
        return ""
    return "bad" if reliability < BAD_RELIABILITY else "warn" if reliability < 1 else ""
