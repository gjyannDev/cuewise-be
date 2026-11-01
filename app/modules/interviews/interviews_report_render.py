"""Turning a Report into terminal text or into the HTML page.

Both renderers read the same `Report` (see interviews_report), so the numbers cannot differ between them. The HTML
page is a design template (templates/interview_report.html) with two holes, {{title}} and {{body}}: the look lives
in that file, this module only produces the markup that goes in the hole. Everything is escaped; the report holds
numbers, ids and reason codes only.
"""

import html
import re
from collections.abc import Sequence
from datetime import datetime
from pathlib import Path

from .interviews_report import Block, Checks, Metric, Report, Section, Table, Watch

# Loaded at import like the prompts: a missing template stops the script at startup, not half-way through a report.
HTML_TEMPLATE = (Path(__file__).parent / "templates" / "interview_report.html").read_text(encoding="utf-8")

_NUMBER = re.compile(r"-?[\d.,]+(?:[/%x][\d.,]*)?")
_MONO_COLUMNS = {"request", "interview"}
_TONE_WORDS = {"warn": "Watch", "bad": "Problem"}
_ICONS = {"ok": "✓", "warn": "!", "bad": "×"}  # check mark, !, multiplication sign
_esc = html.escape


# --- terminal text ---


def render_text(report: Report) -> str:
    lines = [report.title]
    if report.facts:
        lines.append("  " + " ".join(f"{key}={value}" for key, value in report.facts))
    for block in report.blocks:
        lines += _text_block(block)
    return "\n".join(lines)


def _text_block(block: Block) -> list[str]:
    if isinstance(block, Table):
        return ["", _heading(block.title, block.note), *_text_table(block.header, block.rows)]
    if isinstance(block, Section):
        lines = ["", _heading(block.title, block.question), *(_text_metric(m) for m in block.metrics)]
        for table in block.tables:
            lines += _text_block(table)
        return lines
    if isinstance(block, Watch):
        return ["", "watch", *(f"  {note}" for note in block.notes or ["nothing to flag"])]
    return [
        "",
        "checks (database, and log vs database)",
        *(f"  {'FAIL' if problems else 'ok  '} {text}{': ' + '; '.join(problems) if problems else ''}" for text, problems in block.items),
    ]


def _heading(title: str, note: str) -> str:
    return f"{title} ({note})" if note else title


def _text_metric(m: Metric) -> str:
    return f"  {m.label:<20} {m.value}" + (f"  ({m.detail})" if m.detail else "")


def _text_table(header: Sequence[str], rows: Sequence[Sequence[str]]) -> list[str]:
    grid = [list(header), *rows]
    widths = [max(len(row[i]) for row in grid) for i in range(len(header))]
    return ["  " + "  ".join(cell.ljust(w) for cell, w in zip(row, widths, strict=True)).rstrip() for row in grid]


# --- the HTML page ---


def render_html(report: Report) -> str:
    """What needs attention comes first (watch, checks), then the sections, then the long tables that back them up."""
    attention = [b for b in report.blocks if isinstance(b, Watch | Checks)]
    detail = [b for b in report.blocks if isinstance(b, Table) and b.detail]
    main = [b for b in report.blocks if not isinstance(b, Watch | Checks) and not (isinstance(b, Table) and b.detail)]
    parts = [_html_header(report), _html_tiles(report.tiles)]
    if attention:
        parts.append('<div class="pair">' + "".join(_html_block(b) for b in attention) + "</div>")
    parts += [_html_block(b) for b in [*main, *detail]]
    parts.append(
        f'<p class="foot">Generated {datetime.now():%Y-%m-%d %H:%M} from the database and logs/app.log. '
        "Numbers, ids and reason codes only: no question, answer or job-description text.</p>"
    )
    return HTML_TEMPLATE.replace("{{title}}", _esc(report.heading)).replace("{{body}}", "\n".join(parts))


def _html_header(report: Report) -> str:
    facts = "".join(f"<div><dt>{_esc(key)}</dt><dd>{_esc(value)}</dd></div>" for key, value in report.facts)
    return (
        f'<header class="top"><h1>{_esc(report.heading)}</h1><p class="sub">{_esc(report.subtitle)}</p>'
        + (f'<dl class="facts">{facts}</dl>' if facts else "")
        + "</header>"
    )


def _html_tiles(tiles: Sequence[Metric]) -> str:
    return '<section class="tiles" aria-label="Headline numbers">' + "".join(_html_tile(m) for m in tiles) + "</section>"


def _html_tile(m: Metric) -> str:
    return (
        f'<div class="tile {_tone(m)}"><div class="label"><span>{_esc(m.label)}</span>{_pill(m.tone)}</div>'
        f'<div class="value">{_esc(m.value)}</div>{_meter(m)}<div class="detail">{_esc(m.detail)}</div></div>'
    )


def _html_metric_row(m: Metric) -> str:
    detail = f'<span class="detail">{_esc(m.detail)}</span>' if m.detail else ""
    return f'<dt>{_esc(m.label)}</dt><dd class="{_tone(m)}"><span class="val">{_esc(m.value)}</span>{_pill(m.tone)}{_meter(m)}{detail}</dd>'


def _html_block(block: Block) -> str:
    if isinstance(block, Section):
        rows = "".join(_html_metric_row(m) for m in block.metrics)
        tables = "".join(_html_table(t, level=3) for t in block.tables)
        return (
            f'<section class="card"><h2>{_esc(block.title)}</h2><p class="q">{_esc(block.question)}</p>'
            f'<dl class="metrics">{rows}</dl>{tables}</section>'
        )
    if isinstance(block, Table):
        return f'<section class="card">{_html_table(block, level=2)}</section>'
    if isinstance(block, Watch):
        if block.notes:
            items = "".join(_html_item("warn", "Watch", note) for note in block.notes)
        else:
            items = _html_item("ok", "Passed", "Nothing to flag")
        return _html_list_card("Watch", "time limits, failed or odd calls, overrides, fallbacks", items)
    items = "".join(
        _html_item("bad" if problems else "ok", "Failed" if problems else "Passed", text, "; ".join(problems))
        for text, problems in block.items
    )
    return _html_list_card("Checks", "the stored rows, and the log against the database", items)


def _html_list_card(title: str, question: str, items: str) -> str:
    return f'<section class="card"><h2>{title}</h2><p class="q">{question}</p><ul class="list">{items}</ul></section>'


def _html_item(tone: str, word: str, text: str, problems: str = "") -> str:
    extra = f'<span class="problems">{_esc(problems)}</span>' if problems else ""
    return f'<li><i class="icon {tone}">{_ICONS[tone]}</i><span><span class="sr">{word}: </span>{_esc(text)}{extra}</span></li>'


def _html_table(t: Table, *, level: int) -> str:
    numeric = [_is_numeric_column(t, i) for i in range(len(t.header))]
    head = "".join(f'<th scope="col"{_cell_class(numeric[i])}>{_esc(h)}</th>' for i, h in enumerate(t.header))
    body = "".join(
        "<tr>"
        + "".join(
            f"<td{_cell_class(numeric[i], t.header[i] in _MONO_COLUMNS)}>"
            + (f'<i class="sw c{min(r, 3)}"></i>' if t.shares is not None and i == 0 else "")
            + f"{_esc(cell)}</td>"
            for i, cell in enumerate(row)
        )
        + "</tr>"
        for r, row in enumerate(t.rows)
    )
    return (
        f"<h{level}>{_esc(t.title)}</h{level}>"
        + (f'<p class="q">{_esc(t.note)}</p>' if t.note else "")
        + _segmented_bar(t)
        + f'<div class="scroll"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
    )


def _segmented_bar(t: Table) -> str:
    """One whole split into parts, thin and without text: the table under it carries the names and the figures."""
    if not t.shares:
        return ""
    label = ", ".join(f"{row[0]} {row[-1]}" for row in t.rows)
    parts = "".join(f'<span class="c{min(i, 3)}" style="flex:{share:.4f}"></span>' for i, share in enumerate(t.shares) if share > 0)
    return f'<div class="seg" role="img" aria-label="{_esc(label)}">{parts}</div>'


def _is_numeric_column(t: Table, index: int) -> bool:
    cells = [row[index] for row in t.rows]
    return bool(cells) and all(c == "-" or _NUMBER.fullmatch(c) for c in cells) and any(c != "-" for c in cells)


def _cell_class(numeric: bool, mono: bool = False) -> str:
    classes = [name for name, on in (("num", numeric), ("mono", mono)) if on]
    return f' class="{" ".join(classes)}"' if classes else ""


def _tone(m: Metric) -> str:
    return f"tone-{m.tone}" if m.tone else ""


def _pill(tone: str) -> str:
    if tone not in _TONE_WORDS:
        return ""
    return f'<span class="pill"><i class="icon {tone}">{_ICONS[tone]}</i>{_TONE_WORDS[tone]}</span>'


def _meter(m: Metric) -> str:
    """A ratio against a limit or a whole. The value is always printed beside it, so the bar is never the only way to read it."""
    if m.fraction is None:
        return ""
    percent = round(min(max(m.fraction, 0), 1) * 100)
    return (
        f'<div class="meter" role="meter" aria-label="{_esc(m.label)}" aria-valuemin="0" aria-valuemax="100" '
        f'aria-valuenow="{percent}"><span style="width:{percent}%"></span></div>'
    )
