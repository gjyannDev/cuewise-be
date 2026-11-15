"""Prompt files: versioned Markdown read once per process. Feature modules pass their own prompts directory."""

from functools import cache
from pathlib import Path


@cache
def load_prompt(prompts_dir: Path, version: str) -> str:
    """`<prompts_dir>/<version>.md`. Cached: shipped versions are never edited in place, so one read is enough."""
    return (prompts_dir / f"{version}.md").read_text(encoding="utf-8")
