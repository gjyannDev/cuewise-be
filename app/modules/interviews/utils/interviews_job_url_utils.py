"""Turn a fetched job page into plain job-description text (Slice 8b). Pure functions: no network, no I/O.

Order: the page's schema.org JobPosting (JSON-LD) when it has one, because job boards publish it for search engines
and it holds the posting without the page around it; else trafilatura's main-content extraction, which drops
navigation, footers, sidebars and scripts. The HTML always comes from our own SafeFetcher: trafilatura is only handed
a string, so its own downloader (which has no SSRF guard) is never used.

The result is untrusted text. It goes back to the candidate to read and edit, and only reaches a model through the
existing job-description path and its delimiters, like pasted text.
"""

import html as html_lib
import json
import re
from html.parser import HTMLParser

import trafilatura

from ..constants.interviews_constants import (
    JOB_TERMS,
    JOB_TERMS_MIN_HITS,
    JOB_TEXT_MIN_CHARS,
)

_JSONLD = re.compile(
    r"""<script[^>]*type\s*=\s*["']application/ld\+json["'][^>]*>(.*?)</script\s*>""", re.IGNORECASE | re.DOTALL
)
_BLOCK_TAGS = {"p", "div", "br", "ul", "ol", "li", "h1", "h2", "h3", "h4", "h5", "h6", "section", "tr"}
_HIDDEN_TAGS = {"script", "style", "noscript", "template"}
_LIST_FIELDS = (("skills", "Skills"), ("qualifications", "Qualifications"), ("responsibilities", "Responsibilities"))


def extract_job_text(page_html: str) -> str | None:
    """The posting as plain text, or None when the page has too little text to be one (a JavaScript shell, a login
    or cookie wall)."""
    for candidate in (_from_jsonld(page_html), _from_main_content(page_html)):
        if candidate and len(candidate) >= JOB_TEXT_MIN_CHARS:
            return candidate
    return None


def pasted_job_text(content: str, content_format: str) -> str | None:
    """A page the candidate copied from their own browser (for sites that block our fetch), cleaned like a fetched page,
    or None when it holds too little text. `html` is the clipboard's HTML copy: main-content extraction first, and when
    that skips a small fragment, its visible text. `text` has no structure to strip menus with, so it is only tidied."""
    if content_format == "html":
        text = extract_job_text(content) or _tidy(_visible_text(content))
    else:
        text = _tidy(content)
    return text if len(text) >= JOB_TEXT_MIN_CHARS else None


def job_term_hits(text: str) -> int:
    """How many different job-ad terms the text contains; repeats count once."""
    lowered = text.lower()
    return sum(term in lowered for term in JOB_TERMS)


def looks_like_job_posting(text: str) -> bool:
    return job_term_hits(text) >= JOB_TERMS_MIN_HITS


def truncate_on_word(text: str, limit: int) -> tuple[str, bool]:
    """At most `limit` characters, cut at the last whitespace so no word is split; (text, whether it was cut)."""
    if len(text) <= limit:
        return text, False
    cut = text[: limit + 1]
    boundary = max(cut.rfind(" "), cut.rfind("\n"))
    # One enormous "word" (a URL, a base64 blob): a hard cut beats returning almost nothing.
    head = cut[:boundary] if boundary > limit // 2 else text[:limit]
    return head.rstrip(), True


def _from_jsonld(page_html: str) -> str | None:
    for block in _JSONLD.findall(page_html):
        try:
            data = json.loads(block)
        except ValueError:
            continue
        posting = _find_posting(data)
        if posting is not None:
            return _posting_text(posting)
    return None


def _find_posting(data: object) -> dict | None:
    if isinstance(data, list):
        return next((p for item in data if (p := _find_posting(item)) is not None), None)
    if not isinstance(data, dict):
        return None
    kind = data.get("@type")
    if kind == "JobPosting" or (isinstance(kind, list) and "JobPosting" in kind):
        return data
    return _find_posting(data.get("@graph"))


def _posting_text(posting: dict) -> str | None:
    title = _plain(posting.get("title"))
    organization = posting.get("hiringOrganization")
    org_name = _plain(organization.get("name")) if isinstance(organization, dict) else _plain(organization)
    lines = [f"{title} at {org_name}" if title and org_name else title or ""]
    lines.append(_html_to_text(posting.get("description")))
    for field, label in _LIST_FIELDS:
        value = posting.get(field)
        if isinstance(value, list):
            items = [_plain(v) for v in value if _plain(v)]
            if field == "skills":
                lines.append(f"{label}: {', '.join(items)}" if items else "")
            else:
                lines.extend([f"{label}:", *(f"- {item}" for item in items)] if items else [])
        elif _plain(value):
            lines.append(f"{label}: {_html_to_text(value)}")
    return _tidy("\n".join(lines)) or None


def _from_main_content(page_html: str) -> str | None:
    if not page_html.strip():
        return None
    # include_comments=False: blog-style comment threads under a posting are not part of it.
    return _tidy(trafilatura.extract(page_html, include_comments=False, include_tables=True) or "") or None


def _plain(value: object) -> str:
    return " ".join(html_lib.unescape(value).split()) if isinstance(value, str) else ""


class _TextCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._hidden = 0  # inside script/style/noscript: code and CSS, never text the candidate saw

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in _HIDDEN_TAGS:
            self._hidden += 1
        elif tag in _BLOCK_TAGS:
            self.parts.append("\n- " if tag == "li" else "\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in _HIDDEN_TAGS:
            self._hidden = max(0, self._hidden - 1)
        elif tag in _BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._hidden:
            self.parts.append(data)


def _visible_text(markup: str) -> str:
    collector = _TextCollector()
    collector.feed(markup)
    collector.close()
    return "".join(collector.parts)


def _html_to_text(value: object) -> str:
    """A JSON-LD description is usually HTML, sometimes entity-escaped HTML: unescape, then keep text and line breaks."""
    return _visible_text(html_lib.unescape(value)) if isinstance(value, str) else ""


def _tidy(text: str) -> str:
    """One space between words, no blank lines, list markers kept."""
    lines = (" ".join(line.split()) for line in text.splitlines())
    return "\n".join(line for line in lines if line and line != "-")
