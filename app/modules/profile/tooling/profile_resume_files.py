"""Synthetic résumé files written in code: the tests and the profile eval build every PDF and DOCX they use, so each
layout and hidden-text case is spelled out where it is used and no binary fixture is committed.

`make_pdf` writes a tiny but valid PDF from text runs (position, size, colour), filled rectangles and placeholder
images. Coordinates are PDF points with the origin at the bottom left of a US Letter page (612 x 792), as in the PDF
spec. `make_docx` writes a Word document with python-docx, including the run properties that hide text.
"""

import io
import os
import zipfile
from dataclasses import dataclass

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

PAGE_WIDTH, PAGE_HEIGHT = 612, 792

# A colour is a grey level (0 black .. 1 white), an RGB triple or a CMYK quadruple, each component 0..1.
Color = float | tuple[float, float, float] | tuple[float, float, float, float]


@dataclass(frozen=True)
class Text:
    x: float
    y: float
    text: str
    size: float = 11
    color: Color = 0.0


@dataclass(frozen=True)
class Rect:
    x: float
    y: float
    width: float
    height: float
    color: Color = 0.0


@dataclass(frozen=True)
class Image:
    x: float
    y: float
    width: float
    height: float


def _fill(color: Color) -> str:
    if isinstance(color, int | float):
        return f"{color} g"
    if len(color) == 3:
        return "{} {} {} rg".format(*color)
    return "{} {} {} {} k".format(*color)


def _escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _content(items: list[Text | Rect | Image]) -> bytes:
    ops = []
    for item in items:
        if isinstance(item, Text):
            ops.append(f"BT /F1 {item.size} Tf {_fill(item.color)} {item.x} {item.y} Td ({_escape(item.text)}) Tj ET")
        elif isinstance(item, Rect):
            ops.append(f"{_fill(item.color)} {item.x} {item.y} {item.width} {item.height} re f")
        else:
            ops.append(f"q {item.width} 0 0 {item.height} {item.x} {item.y} cm /Im1 Do Q")
    return "\n".join(ops).encode("latin-1")


def make_pdf(pages: list[list[Text | Rect | Image]], *, encrypt: bool = False) -> bytes:
    """A PDF with one page per list. `encrypt` adds a standard security handler whose user password is not empty, so
    a reader cannot open the file without a password (the check fails before any content is decrypted)."""
    objects: list[bytes] = []

    def add(body: bytes) -> int:
        objects.append(body)
        return len(objects)

    font = add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    image = add(b"<< /Type /XObject /Subtype /Image /Width 1 /Height 1 /ColorSpace /DeviceGray "
                b"/BitsPerComponent 8 /Length 1 >>\nstream\n\x40\nendstream")
    pages_id = len(objects) + 1 + 2 * len(pages)  # the page tree comes after every page and its content
    kids = []
    for items in pages:
        stream = _content(items)
        content = add(b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream")
        kids.append(add(
            b"<< /Type /Page /Parent %d 0 R /MediaBox [0 0 %d %d] /Contents %d 0 R "
            b"/Resources << /Font << /F1 %d 0 R >> /XObject << /Im1 %d 0 R >> >> >>"
            % (pages_id, PAGE_WIDTH, PAGE_HEIGHT, content, font, image)
        ))
    assert add(b"<< /Type /Pages /Kids [%s] /Count %d >>" % (b" ".join(b"%d 0 R" % k for k in kids), len(kids))) == pages_id
    catalog = add(b"<< /Type /Catalog /Pages %d 0 R >>" % pages_id)
    extra = b""
    if encrypt:
        owner, user = os.urandom(32).hex().encode(), os.urandom(32).hex().encode()
        encrypt_id = add(b"<< /Filter /Standard /V 1 /R 2 /O <%s> /U <%s> /P -4 >>" % (owner, user))
        file_id = os.urandom(16).hex().encode()
        extra = b" /Encrypt %d 0 R /ID [<%s> <%s>]" % (encrypt_id, file_id, file_id)

    out = io.BytesIO()
    out.write(b"%PDF-1.4\n")
    offsets = []
    for number, body in enumerate(objects, start=1):
        offsets.append(out.tell())
        out.write(b"%d 0 obj\n" % number + body + b"\nendobj\n")
    xref = out.tell()
    out.write(b"xref\n0 %d\n0000000000 65535 f \n" % (len(objects) + 1))
    out.write(b"".join(b"%010d 00000 n \n" % offset for offset in offsets))
    out.write(b"trailer\n<< /Size %d /Root %d 0 R%s >>\nstartxref\n%d\n%%%%EOF\n" % (len(objects) + 1, catalog, extra, xref))
    return out.getvalue()


# A run is its text and its properties: hidden (bool), color ("RRGGBB"), size (points), shading ("RRGGBB" fill).
Run = tuple[str, dict]


def make_docx(paragraphs: list[list[Run]], *, table: list[list[str]] | None = None) -> bytes:
    document = Document()
    for runs in paragraphs:
        paragraph = document.add_paragraph()
        for text, props in runs:
            run = paragraph.add_run(text)
            if props.get("hidden"):
                run.font.hidden = True
            if "color" in props:
                run.font.color.rgb = RGBColor.from_string(props["color"])
            if "size" in props:
                run.font.size = Pt(props["size"])
            if "shading" in props:
                shading = OxmlElement("w:shd")
                shading.set(qn("w:val"), "clear")
                shading.set(qn("w:fill"), props["shading"])
                run._r.get_or_add_rPr().append(shading)
    if table:
        grid = document.add_table(rows=len(table), cols=len(table[0]))
        for row, values in zip(grid.rows, table, strict=True):
            for cell, value in zip(row.cells, values, strict=True):
                cell.text = value
    out = io.BytesIO()
    document.save(out)
    return out.getvalue()


def rezip(data: bytes, *, add: dict[str, bytes] | None = None, replace: dict[str, bytes] | None = None) -> bytes:
    """A copy of a zip (a DOCX) with parts added or replaced: macros, embedded objects, external relationships."""
    add, replace = add or {}, replace or {}
    out = io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(data)) as source, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as target:
        for info in source.infolist():
            target.writestr(info.filename, replace.get(info.filename, source.read(info.filename)))
        for name, content in add.items():
            target.writestr(name, content)
    return out.getvalue()


def plain_zip(files: dict[str, bytes]) -> bytes:
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as target:
        for name, content in files.items():
            target.writestr(name, content)
    return out.getvalue()
