"""Reading an uploaded résumé: untrusted bytes in, visible text in reading order out, or a typed refusal.

Everything happens in memory. The format is decided by the file's first bytes, never its name. Hidden text (near-white
with nothing dark behind it, too small, off the page, Word's hidden runs) is dropped here, before any model sees it:
it is the first of the layered defences against résumé prompt injection (then the fence, the schema, the grounding
check). This is CPU-bound and synchronous; the service runs it in a worker thread.
"""

import io
import re
import zipfile
from collections.abc import Callable, Iterator
from typing import Any, Literal, NamedTuple

# lxml ships etree as a compiled module without type stubs, so the type checker cannot see it; it imports fine at runtime.
from lxml import etree  # pyright: ignore[reportAttributeAccessIssue]

from ..constants.profile_constants import (
    COLUMN_MIN_GAP,
    COLUMN_MIN_LINES,
    DARK_BACKGROUND,
    MIN_FONT_SIZE,
    NEAR_WHITE,
    RESUME_MAX_BYTES,
    RESUME_MAX_PAGES,
    RESUME_MAX_UNZIPPED_BYTES,
    RESUME_MIN_CHARS,
)

_PDF_MAGIC = b"%PDF-"
_ZIP_MAGIC = b"PK\x03\x04"
_OLE_MAGIC = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"  # legacy .doc (and .xls/.ppt)
_WORD_MAIN = b"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"
_HYPERLINK = "/relationships/hyperlink"
_EMBEDDED_PREFIXES = ("word/embeddings/", "word/activeX/")
# A header above two columns may span the page; at most this many lines of it are looked past.
_MAX_HEADER_LINES = 8
_SAFE_XML = etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=False)


class ResumeRefusal(Exception):
    """Why a file was refused; `reason` is short and machine-readable (logged, never shown)."""

    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


class ResumeTooLargeRefusal(ResumeRefusal):
    pass


class ResumeUnsupportedRefusal(ResumeRefusal):
    pass


class ResumeUnreadableRefusal(ResumeRefusal):
    pass


class ResumeText(NamedTuple):
    text: str
    format: Literal["pdf", "docx"]
    pages: int | None  # PDFs only
    hidden_chars: int  # dropped as hidden (logged as a count)


def read_resume(data: bytes) -> ResumeText:
    if len(data) > RESUME_MAX_BYTES:
        raise ResumeTooLargeRefusal("bytes")
    if data.startswith(_PDF_MAGIC):
        result = _read_pdf(data)
    elif data.startswith(_ZIP_MAGIC):
        result = _read_docx(data)
    elif data.startswith(_OLE_MAGIC):
        raise ResumeUnsupportedRefusal("legacy_doc")
    else:
        raise ResumeUnsupportedRefusal("not_pdf_or_docx")
    if len(result.text) < RESUME_MIN_CHARS:
        raise ResumeUnreadableRefusal("too_little_text")
    return result


def _clean(lines: Iterator[str]) -> str:
    return "\n".join(cleaned for line in lines if (cleaned := " ".join(line.split())))


# --- colours -----------------------------------------------------------------------------------------------------------


def _lightness(color: Any) -> float | None:
    """0 (black) to 1 (white) for a grey, RGB or CMYK colour; None when unknown (a pattern, no colour)."""
    if not isinstance(color, tuple | list) or not all(isinstance(c, int | float) for c in color):
        return None
    if len(color) == 1:
        return float(color[0])
    if len(color) == 3:
        r, g, b = color
    elif len(color) == 4:
        c, m, y, k = color
        r, g, b = (1 - c) * (1 - k), (1 - m) * (1 - k), (1 - y) * (1 - k)
    else:
        return None
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _hex_lightness(value: str | None) -> float | None:
    if not value or not re.fullmatch(r"[0-9A-Fa-f]{6}", value):
        return None  # "auto", theme colours: not white by our rule
    return _lightness(tuple(int(value[i : i + 2], 16) / 255 for i in (0, 2, 4)))


# --- PDF ---------------------------------------------------------------------------------------------------------------


def _read_pdf(data: bytes) -> ResumeText:
    import pdfplumber
    from pdfminer.pdfdocument import PDFEncryptionError, PDFPasswordIncorrect

    try:
        with pdfplumber.open(io.BytesIO(data)) as pdf:
            if len(pdf.pages) > RESUME_MAX_PAGES:
                raise ResumeTooLargeRefusal("pages")
            texts, hidden, any_chars = [], 0, False
            for page in pdf.pages:
                text, dropped, had_chars = _read_page(page)
                texts.append(text)
                hidden += dropped
                any_chars = any_chars or had_chars
            pages = len(pdf.pages)
    except ResumeRefusal:
        raise
    except Exception as exc:  # pdfminer raises many types on malformed input; all mean "unreadable"
        causes = (exc, *getattr(exc, "args", ()), exc.__cause__)
        if any(isinstance(c, PDFPasswordIncorrect | PDFEncryptionError) for c in causes):
            raise ResumeUnreadableRefusal("encrypted") from exc
        raise ResumeUnreadableRefusal("corrupt") from exc
    if not any_chars:
        raise ResumeUnreadableRefusal("no_text")
    return ResumeText(_clean(iter("\n".join(texts).splitlines())), "pdf", pages, hidden)


def _read_page(page: Any) -> tuple[str, int, bool]:
    """The page's visible text in reading order, the count of hidden characters dropped, and whether it had text."""
    backgrounds = [
        (r["x0"], r["top"], r["x1"], r["bottom"])
        for r in page.rects
        if r.get("fill") and (light := _lightness(r.get("non_stroking_color"))) is not None and light <= DARK_BACKGROUND
    ] + [(i["x0"], i["top"], i["x1"], i["bottom"]) for i in page.images]
    width, height = page.width, page.height

    def visible(char: dict) -> bool:
        if char["size"] < MIN_FONT_SIZE:
            return False
        cx, cy = (char["x0"] + char["x1"]) / 2, (char["top"] + char["bottom"]) / 2
        if not (0 <= cx <= width and 0 <= cy <= height):
            return False
        light = _lightness(char.get("non_stroking_color"))
        if light is None or light < NEAR_WHITE:
            return True
        return any(x0 <= cx <= x1 and top <= cy <= bottom for x0, top, x1, bottom in backgrounds)

    chars = page.chars
    kept = [c for c in chars if visible(c)]
    shown = page.filter(lambda obj: obj.get("object_type") != "char" or visible(obj))
    return _in_reading_order(shown, width, height), len(chars) - len(kept), bool(chars)


def _in_reading_order(page: Any, width: float, height: float) -> str:
    """One column top to bottom, or, when the words fall into two columns separated by an empty vertical band (below
    an optional full-width header), the header, then the left column, then the right one."""
    words = page.extract_words()
    split = _find_columns(words)
    if split is None:
        return page.extract_text() or ""
    header_bottom, gap_x = split
    parts = [
        page.within_bbox((0, header_bottom, gap_x, height)),
        page.within_bbox((gap_x, header_bottom, width, height)),
    ]
    if header_bottom > 0:
        parts.insert(0, page.within_bbox((0, 0, width, header_bottom)))
    return "\n".join(part.extract_text() or "" for part in parts)


def _find_columns(words: list[dict]) -> tuple[float, float] | None:
    """(where the header ends, the x of the column gap), or None for a one-column page."""
    if not words:
        return None
    line_tops = sorted({round(w["top"]) for w in words})
    for skipped in range(min(_MAX_HEADER_LINES, len(line_tops) - 1) + 1):
        body = [w for w in words if round(w["top"]) >= line_tops[skipped]]
        gap = _widest_gap(body)
        if gap is not None:
            header_bottom = (
                0.0 if skipped == 0 else (max(w["bottom"] for w in words if round(w["top"]) < line_tops[skipped])
                                          + min(w["top"] for w in body)) / 2
            )
            return header_bottom, gap
    return None


def _widest_gap(words: list[dict]) -> float | None:
    """The middle of the widest empty vertical band between words, if it is wide enough and both sides hold enough."""
    spans = sorted((w["x0"], w["x1"]) for w in words)
    best: tuple[float, float] | None = None
    reach = spans[0][1]
    for x0, x1 in spans[1:]:
        if x0 - reach >= COLUMN_MIN_GAP and (best is None or x0 - reach > best[1] - best[0]):
            best = (reach, x0)
        reach = max(reach, x1)
    if best is None:
        return None
    left_lines = {round(w["top"]) for w in words if w["x1"] <= best[0]}
    right_lines = {round(w["top"]) for w in words if w["x0"] >= best[1]}
    if min(len(left_lines), len(right_lines)) < COLUMN_MIN_LINES:
        return None
    return (best[0] + best[1]) / 2


# --- DOCX --------------------------------------------------------------------------------------------------------------


def _read_docx(data: bytes) -> ResumeText:
    try:
        archive = zipfile.ZipFile(io.BytesIO(data))
    except (zipfile.BadZipFile, ValueError) as exc:
        raise ResumeUnreadableRefusal("corrupt") from exc
    with archive:
        infos = archive.infolist()
        # Declared sizes from the zip directory; reading a member never inflates past its declared size.
        if sum(info.file_size for info in infos) > RESUME_MAX_UNZIPPED_BYTES:
            raise ResumeTooLargeRefusal("unzipped")
        names = {info.filename for info in infos}
        if "[Content_Types].xml" not in names:
            raise ResumeUnsupportedRefusal("not_word")
        try:
            content_types = archive.read("[Content_Types].xml")
            if _WORD_MAIN not in content_types:
                raise ResumeUnsupportedRefusal("not_word")
            if any(name.endswith("vbaProject.bin") for name in names) or b"macroEnabled" in content_types:
                raise ResumeUnsupportedRefusal("macros")
            if any(name.startswith(_EMBEDDED_PREFIXES) for name in names):
                raise ResumeUnsupportedRefusal("embedded")
            for name in names:
                if name.endswith(".rels") and _has_external_relationship(archive.read(name)):
                    raise ResumeUnsupportedRefusal("external")
        except (zipfile.BadZipFile, etree.XMLSyntaxError, RuntimeError, OSError) as exc:
            raise ResumeUnreadableRefusal("corrupt") from exc

    try:
        import docx

        document = docx.Document(io.BytesIO(data))
        lines, hidden = _docx_lines(document)
    except ResumeRefusal:
        raise
    except Exception as exc:  # python-docx/lxml raise many types on malformed parts; all mean "unreadable"
        raise ResumeUnreadableRefusal("corrupt") from exc
    return ResumeText(_clean(iter(lines)), "docx", None, hidden)


def _has_external_relationship(rels: bytes) -> bool:
    """A relationship the document would fetch from outside (a remote template, a linked object). Hyperlinks are
    allowed: a résumé's profile links are common, and nothing here ever follows them."""
    root = etree.fromstring(rels, _SAFE_XML)
    return any(
        rel.get("TargetMode") == "External" and not (rel.get("Type") or "").endswith(_HYPERLINK) for rel in root
    )


def _docx_lines(document: Any) -> tuple[list[str], int]:
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    lines: list[str] = []
    hidden = 0

    def paragraph(p: Paragraph) -> None:
        nonlocal hidden
        parts = []
        for run in _runs(p):
            if _docx_run_visible(run, p):
                parts.append(run.text)
            else:
                hidden += len(run.text)
        lines.append("".join(parts))

    def table(t: Table) -> None:
        seen = set()
        for row in t.rows:
            for cell in row.cells:
                if id(cell._tc) in seen:  # a merged cell repeats in every row and column it spans
                    continue
                seen.add(id(cell._tc))
                for block in cell.iter_inner_content():
                    paragraph(block) if isinstance(block, Paragraph) else table(block)

    for block in document.iter_inner_content():
        paragraph(block) if isinstance(block, Paragraph) else table(block)
    return lines, hidden


def _runs(p: Any) -> Iterator[Any]:
    """Every run of a paragraph, including the ones inside hyperlinks (paragraph.runs skips those)."""
    from docx.text.hyperlink import Hyperlink

    for item in p.iter_inner_content():
        if isinstance(item, Hyperlink):
            yield from item.runs
        else:
            yield item


def _style_chain(style: Any) -> Iterator[Any]:
    seen = 0
    while style is not None and seen < 20:
        yield style
        style, seen = style.base_style, seen + 1


def _effective(run: Any, p: Any, read: Callable[[Any], Any]) -> Any:
    """A run property as Word resolves it: the run's own, then its character style, then its paragraph's style."""
    for font in [run.font, *(s.font for s in _style_chain(run.style)), *(s.font for s in _style_chain(p.style))]:
        value = read(font)
        if value is not None:
            return value
    return None


def _docx_run_visible(run: Any, p: Any) -> bool:
    if _effective(run, p, lambda f: f.hidden):
        return False
    size = _effective(run, p, lambda f: f.size)
    if size is not None and size.pt < MIN_FONT_SIZE:
        return False
    rgb = _effective(run, p, lambda f: f.color.rgb if f.color.type is not None else None)
    light = _hex_lightness(str(rgb) if rgb is not None else None)
    if light is None or light < NEAR_WHITE:
        return True
    fill = _shading(run._r) or _shading(p._p)
    background = _hex_lightness(fill)
    return background is not None and background <= DARK_BACKGROUND


def _shading(element: Any) -> str | None:
    found = element.xpath("./w:rPr/w:shd/@w:fill | ./w:pPr/w:shd/@w:fill")
    return str(found[0]) if found else None
