"""The section splitter of note ingestion (U3b2 Step 10): LangChain's `MarkdownHeaderTextSplitter`."""

from app.modules.interviews.ai.interviews_split import split_sections


def test_each_level_two_heading_gives_its_text_and_the_title_has_none():
    body = "# Title\n\n## First\nline one\nline two\n\n## Second\n### Detail\nmore\n"

    assert split_sections(body) == {"First": "line one\nline two", "Second": "### Detail\nmore"}


def test_a_heading_with_no_text_is_absent():
    assert split_sections("## Empty\n## Full\ntext\n") == {"Full": "text"}
