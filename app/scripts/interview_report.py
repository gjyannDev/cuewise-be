"""Print the cost, effectiveness and efficiency of the interviewer. Numbers and ids only, never any text.

Run an interview, then:

    uv run python -m app.scripts.interview_report                 # the newest interview, in detail
    uv run python -m app.scripts.interview_report --session <id>  # a specific one
    uv run python -m app.scripts.interview_report --last 10       # the same numbers pooled over the newest 10
    uv run python -m app.scripts.interview_report --html          # also write the designed HTML page

The HTML page is saved as logs/reports/report_<session id>.html (a pooled one as rollup_last-<N>_<newest id>.html),
so every interview keeps its own file; running it again for the same interview refreshes only that file. Give
--html a folder to save elsewhere, or a path ending in .html to choose the file name yourself.

The questions and answer lengths come from the database; decisions, per-call usage and timing come from
logs/app.log (and the rotated logs/app.log.1), joined on the session id.
"""

import argparse
import uuid
from collections.abc import Sequence
from pathlib import Path

from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import LOG_FILE
from app.db import models  # noqa: F401  (registers every model before the session is used)
from app.db.session import SessionLocal
from app.modules.interviews.models.interviews_model import InterviewSession
from app.modules.interviews.repositories.interviews_repository import (
    InterviewsRepository,
)
from app.modules.interviews.tooling.interviews_log import parse_log
from app.modules.interviews.tooling.interviews_report import (
    analyze_interview,
    analyze_rollup,
)
from app.modules.interviews.tooling.interviews_report_render import (
    render_html,
    render_text,
)

DEFAULT_REPORTS_DIR = LOG_FILE.parent / "reports"


def html_target(where: Path, sessions: Sequence[InterviewSession], pooled: bool) -> Path:
    """A path ending in .html is the file; anything else is a folder, and the file is named after the interview."""
    if where.suffix == ".html":
        return where
    newest = sessions[0].id
    return where / (f"rollup_last-{len(sessions)}_{newest}.html" if pooled else f"report_{newest}.html")


def read_log_lines(log: Path) -> list[str]:
    """The rotated log first, so the lines stay in time order."""
    lines: list[str] = []
    for path in (log.with_name(f"{log.name}.1"), log):
        if path.exists():
            lines += path.read_text(encoding="utf-8", errors="replace").splitlines()
    return lines


def main(
    db: Session,
    log_lines: Sequence[str],
    session_id: uuid.UUID | None = None,
    last: int | None = None,
    html_path: Path | None = None,
) -> str:
    repository = InterviewsRepository(db)
    if session_id:
        found = repository.get_session(session_id)
        sessions = [found] if found else []
    else:
        sessions = repository.latest_sessions(last or 1)
    if not sessions:
        return "no interview found"
    interviews = [(s, repository.list_session_questions(s.id), repository.list_messages(s.id)) for s in sessions]
    events = parse_log(log_lines)
    budget = settings.llm_total_budget_seconds
    if last:
        report = analyze_rollup(interviews, events, budget_seconds=budget)
    else:
        session, questions, messages = interviews[0]
        report = analyze_interview(session, questions, messages, events, budget_seconds=budget)
    text = render_text(report)
    if html_path is None:
        return text
    target = html_target(html_path, sessions, pooled=bool(last))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_html(report), encoding="utf-8")
    return f"{text}\n\nhtml report: {target.resolve()}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cost, effectiveness and efficiency of the interviewer.")
    which = parser.add_mutually_exclusive_group()
    which.add_argument("--session", type=uuid.UUID, help="interview id (default: the newest interview)")
    which.add_argument("--last", type=int, metavar="N", help="pool the newest N interviews instead of one in detail")
    parser.add_argument("--log", type=Path, default=LOG_FILE, help=f"log file (default: {LOG_FILE})")
    parser.add_argument(
        "--html",
        nargs="?",
        const=DEFAULT_REPORTS_DIR,
        type=Path,
        metavar="DIR_OR_FILE",
        help=f"also write a designed HTML page, named after the interview (default folder: {DEFAULT_REPORTS_DIR})",
    )
    args = parser.parse_args()
    with SessionLocal() as session:
        print(main(session, read_log_lines(args.log), args.session, args.last, args.html))
