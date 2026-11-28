"""Splitting a note's body into its `##` sections with LangChain's `MarkdownHeaderTextSplitter` (U3b2).

Adopted only after it reproduced every chunk and content hash of the corpus (75 of 75, 2026-11-27; the one-off
comparison is in docs/features/u3b2-retrieval/learnings.md). It gives the text only: it drops a heading with
no text and merges sections that share a heading, so `parse_note` keeps its own heading scan for those checks.
"""

from langchain_text_splitters import MarkdownHeaderTextSplitter

_SPLITTER = MarkdownHeaderTextSplitter(headers_to_split_on=[("##", "heading")])


def split_sections(body: str) -> dict[str, str]:
    """Each `##` heading's text; text before the first `##` (the `#` title) has no heading and is left out."""
    return {d.metadata["heading"]: d.page_content for d in _SPLITTER.split_text(body) if "heading" in d.metadata}
