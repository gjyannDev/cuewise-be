"""Reference notes: the corpus file format, its validation and chunking, and the pure helpers retrieval uses.

A note is a markdown file with a small header, then one chunk per `##` section (the heading is the competency):

    ---
    roles: backend, general
    levels: junior, mid
    source: posting
    ---
    # Optional title
    ## Error handling
    What interviewers probe, what strong and weak answers look like.

"Chunking" means cutting a document into the pieces that get embedded and retrieved on their own. Splitting by
heading keeps each piece about one competency, so a match brings back one focused idea instead of a whole page.

Notes may hold third-party text (skills from real job postings), so before anything is embedded every file is checked:
hidden characters fail it (they can carry instructions a reviewer can't see), and instruction-like phrases are listed
as warnings for a human to look at.
"""

import hashlib
import json
import math
import random
import re
import unicodedata
import uuid
from collections.abc import Sequence
from pathlib import Path
from typing import NamedTuple

from ..constants.interviews_constants import (
    GENERAL_ROLE,
    KNOWLEDGE_HEADING_MAX_LENGTH,
    KNOWLEDGE_SECTION_MAX_LENGTH,
    MIN_NON_DRAFTED_SHARE,
    JobRole,
    Level,
    NoteSource,
)

_HEADER_KEYS = ("roles", "levels", "source")
_KNOWN_ROLES = {*JobRole, GENERAL_ROLE}
_SECTION = re.compile(r"^##(?!#)\s*(.*?)\s*$")
_TITLE = re.compile(r"^#(?!#)")
# Phrases that try to talk to the model rather than describe interviews. Warnings only: a human decides.
_INSTRUCTION_LIKE = re.compile(
    r"\b(ignore|disregard|forget)\b[^.\n]{0,40}\b(instructions?|rules|prompt)\b"
    r"|\byou are now\b|\bsystem prompt\b|\bact as\b|\bnew instructions\b",
    re.IGNORECASE,
)


class CorpusError(Exception):
    """A note that can't be ingested; the message starts with the file name (or "corpus") and never quotes note text."""

    def __init__(self, where: str, reason: str):
        super().__init__(f"{where}: {reason}")


class NoteChunk(NamedTuple):
    # "file.md#Heading": stable across environments, so eval labels can name it.
    note_key: str
    competency: str
    text: str
    source: NoteSource
    # JobRole values or GENERAL_ROLE, in header order.
    roles: tuple[str, ...]
    levels: tuple[Level, ...]
    content_hash: str
    # Position in the corpus (set by load_corpus); within one parsed note, its section index.
    order: int


class ParsedNote(NamedTuple):
    file_name: str
    source: NoteSource
    chunks: list[NoteChunk]
    warnings: list[str]


class Corpus(NamedTuple):
    notes: list[ParsedNote]
    # Every note's chunks, numbered in corpus order (file name, then section).
    chunks: list[NoteChunk]
    warnings: list[str]


class ReferenceNote(NamedTuple):
    """A note an interview was given: what the question writer sees (competency and text) plus where it came from."""

    chunk_id: uuid.UUID
    competency: str
    text: str
    # 1 = most relevant.
    rank: int
    # Cosine similarity in vector mode; None in filter mode.
    score: float | None


def merge_note_rankings(
    jd_ranked: Sequence[ReferenceNote], profile_ranked: Sequence[ReferenceNote], *, k: int, profile_slots: int
) -> tuple[list[ReferenceNote], int]:
    """The quota merge: job-description notes first, then at most `profile_slots` profile notes the job description
    didn't already pick; slots the profile leaves unused go back to the job description. Never more than k notes, and
    never more profile notes than the quota, even when the job-description side is short (EC17). Ranks are renumbered
    from 1; each note keeps its own score. Also returns how many notes the profile side added (for logs and traces).

    Why a quota and not one blended query: the job description stays in control by construction (not just on
    average), every note can be traced to the side that found it, and 0 slots turns the profile half off.
    """
    reserved = min(profile_slots, k)
    jd_part = list(jd_ranked[: k - reserved])
    taken = {note.chunk_id for note in jd_part}
    profile_part: list[ReferenceNote] = []
    for note in profile_ranked:
        if len(profile_part) == reserved:
            break
        if note.chunk_id not in taken:
            profile_part.append(note)
            taken.add(note.chunk_id)
    for note in jd_ranked[k - reserved :]:
        if len(jd_part) + len(profile_part) == k:
            break
        if note.chunk_id not in taken:
            jd_part.append(note)
            taken.add(note.chunk_id)
    merged = [note._replace(rank=rank) for rank, note in enumerate([*jd_part, *profile_part], start=1)]
    return merged, len(profile_part)


def parse_note(file_name: str, text: str) -> ParsedNote:
    """One note file -> its chunks. Raises CorpusError naming the file for anything that can't be ingested."""
    _check_hidden(file_name, text)
    lines = text.splitlines()
    roles, levels, source, body = _parse_header(file_name, lines)
    chunks: list[NoteChunk] = []
    warnings: list[str] = []
    for index, (heading, section) in enumerate(_sections(file_name, body)):
        key = f"{file_name}#{heading}"
        chunks.append(NoteChunk(key, heading, section, source, roles, levels, _hash(roles, levels, source, heading, section), index))
        if _INSTRUCTION_LIKE.search(section):
            warnings.append(f"{key}: instruction-like phrase; review it (third-party text must stay data)")
    return ParsedNote(file_name, source, chunks, warnings)


def load_corpus(directory: Path) -> Corpus:
    """Every `*.md` note in the folder, in file-name order; stops at the first invalid one."""
    notes = [parse_note(path.name, path.read_text(encoding="utf-8")) for path in sorted(directory.glob("*.md"))]
    if not notes:
        raise CorpusError("corpus", f"no notes (*.md) in {directory}")
    chunks = [chunk for note in notes for chunk in note.chunks]
    return Corpus(
        notes,
        [chunk._replace(order=order) for order, chunk in enumerate(chunks)],
        [warning for note in notes for warning in note.warnings],
    )


def source_share_problem(notes: Sequence[ParsedNote]) -> str | None:
    """Why the corpus leans too much on drafted notes, or None. A model grounded on a model's own drafts mostly hears
    back what it already knows, so at least a third must come from supplied or approved material."""
    other = sum(note.source != NoteSource.drafted for note in notes)
    if other >= MIN_NON_DRAFTED_SHARE * len(notes):
        return None
    return f"only {other} of {len(notes)} notes have a source other than drafted; at least a third must"


def embedding_text(chunk: NoteChunk) -> str:
    """What a chunk is embedded as: its heading, then its text. The heading names the competency, which is often the
    word a job description uses ("caching", "API design"), so it helps the match."""
    return f"{chunk.competency}\n{chunk.text}"


def query_text(summary: str | None, job_description: str | None) -> str | None:
    """What vector mode embeds: the summary, else the job description as entered, else None (filter mode). Only that
    text: role and level are filters, never part of the query, so the job description can't change them."""
    for text in (summary, job_description):
        if text is not None and text.strip():
            return text
    return None


def pick_filter_notes[T](eligible: Sequence[T], session_id: uuid.UUID, k: int) -> list[T]:
    """Up to k of the eligible notes in an order seeded by the interview id: the same interview always gets the same
    notes, and different interviews can get different ones."""
    picked = list(eligible)
    random.Random(session_id.int).shuffle(picked)
    return picked[:k]


def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    """1 = same direction (same meaning), 0 = unrelated, -1 = opposite. Length is ignored, so unnormalised vectors are
    fine. A zero vector has no direction: 0."""
    norms = math.hypot(*a) * math.hypot(*b)
    return math.sumprod(a, b) / norms if norms else 0.0


def _check_hidden(file_name: str, text: str) -> None:
    for number, line in enumerate(text.splitlines(), start=1):
        for char in line:
            # Format and control characters (zero-width spaces, direction overrides, ...) render as nothing.
            if char != "\t" and unicodedata.category(char) in ("Cf", "Cc", "Co", "Cs"):
                raise CorpusError(file_name, f"hidden or zero-width character U+{ord(char):04X} on line {number}")


def _parse_header(
    file_name: str, lines: list[str]
) -> tuple[tuple[str, ...], tuple[Level, ...], NoteSource, list[str]]:
    if not lines or lines[0].strip() != "---" or "---" not in (line.strip() for line in lines[1:]):
        raise CorpusError(file_name, "missing header: start with a --- block holding roles, levels and source")
    end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        key, colon, value = line.partition(":")
        key = key.strip().lower()
        if not colon or key not in _HEADER_KEYS:
            raise CorpusError(file_name, f"unknown header line '{key}' (use roles, levels and source)")
        if key in values:
            raise CorpusError(file_name, f"header key '{key}' appears twice")
        values[key] = value
    roles = _listed(file_name, values, "roles")
    for role in roles:
        if role not in _KNOWN_ROLES:
            raise CorpusError(file_name, f"unknown role '{role}' (use {', '.join(sorted(_KNOWN_ROLES))})")
    levels = _listed(file_name, values, "levels")
    for level in levels:
        if level not in set(Level):
            raise CorpusError(file_name, f"unknown level '{level}' (use {', '.join(Level)})")
    source = values.get("source", "").strip().lower()
    if not source:
        raise CorpusError(file_name, "missing or empty header value: source")
    if source not in set(NoteSource):
        raise CorpusError(file_name, f"unknown source '{source}' (use {', '.join(NoteSource)})")
    return roles, tuple(Level(level) for level in levels), NoteSource(source), lines[end + 1 :]


def _listed(file_name: str, values: dict[str, str], key: str) -> tuple[str, ...]:
    items = tuple(dict.fromkeys(item.strip().lower() for item in values.get(key, "").split(",") if item.strip()))
    if not items:
        raise CorpusError(file_name, f"missing or empty header value: {key}")
    return items


def _sections(file_name: str, body: list[str]) -> list[tuple[str, str]]:
    sections: list[tuple[str, list[str]]] = []
    for line in body:
        heading = _SECTION.match(line)
        if heading:
            sections.append((heading.group(1), []))
        elif sections:
            sections[-1][1].append(line)
        elif line.strip() and not _TITLE.match(line):
            raise CorpusError(file_name, "text outside a section: every chunk needs a ## heading")
    if not sections:
        raise CorpusError(file_name, "no sections: add at least one ## heading")
    seen: set[str] = set()
    result = []
    for heading, lines in sections:
        text = "\n".join(lines).strip()
        if not heading:
            raise CorpusError(file_name, "a ## heading is empty")
        if len(heading) > KNOWLEDGE_HEADING_MAX_LENGTH:
            raise CorpusError(file_name, f"heading '{heading[:40]}...' is too long (max {KNOWLEDGE_HEADING_MAX_LENGTH})")
        if heading in seen:
            raise CorpusError(file_name, f"duplicate section heading '{heading}'")
        if not text:
            raise CorpusError(file_name, f"empty section '{heading}'")
        if len(text) > KNOWLEDGE_SECTION_MAX_LENGTH:
            raise CorpusError(
                file_name, f"section '{heading}' is too long ({len(text)} characters, max {KNOWLEDGE_SECTION_MAX_LENGTH})"
            )
        seen.add(heading)
        result.append((heading, text))
    return result


def _hash(roles: tuple[str, ...], levels: tuple[Level, ...], source: NoteSource, heading: str, text: str) -> str:
    # Header values are part of it: the same text re-scoped to other levels is a changed chunk.
    payload = {"roles": sorted(roles), "levels": sorted(levels), "source": source, "competency": heading, "text": text}
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
