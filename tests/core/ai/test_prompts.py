"""The shared prompt loader (prompt-registry AC9, EC13): one cached read per directory and version."""

import pytest

from app.core.ai.prompts import load_prompt


def test_returns_the_text_of_the_versioned_file(tmp_path):
    (tmp_path / "greet_v1.md").write_text("Hello {{name}}", encoding="utf-8")

    assert load_prompt(tmp_path, "greet_v1") == "Hello {{name}}"


def test_a_second_call_does_not_read_the_file_again(tmp_path):
    path = tmp_path / "greet_v1.md"
    path.write_text("first", encoding="utf-8")
    load_prompt(tmp_path, "greet_v1")
    path.write_text("second", encoding="utf-8")

    assert load_prompt(tmp_path, "greet_v1") == "first"


def test_the_same_version_in_two_directories_gives_two_texts(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    a.mkdir()
    b.mkdir()
    (a / "p_v1.md").write_text("from a", encoding="utf-8")
    (b / "p_v1.md").write_text("from b", encoding="utf-8")

    assert (load_prompt(a, "p_v1"), load_prompt(b, "p_v1")) == ("from a", "from b")


def test_an_unknown_version_raises_file_not_found_naming_the_path(tmp_path):
    with pytest.raises(FileNotFoundError, match="nope_v9.md"):
        load_prompt(tmp_path, "nope_v9")
