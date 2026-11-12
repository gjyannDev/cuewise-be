# Writing a knowledge-base note (guide)

Template to copy: `note-template.md` (same folder). Notes live in `app/modules/interviews/data/knowledge/*.md`.
Do not put guidance text inside a note file: anything outside the header and `##` sections is refused, and text after
a section is embedded as part of that section.

## Rules the ingest CLI enforces (a broken rule refuses the whole file)
- **Header**, exactly three keys:
  - `roles:` one or more of `backend, frontend, fullstack, mobile, data, designer, qa, devops, general`, comma
    separated. Use `general` for material every role needs, and list a specific role only when the note is really
    about it: a candidate sees the notes of their own role plus `general`, so a QA note tagged `frontend` would reach
    frontend candidates. Cover each role at every level, the way the existing roles split into a fundamentals note
    (intern, junior) and a second note (mid, senior).
  - `levels:` one or more of `intern, junior, mid, senior`
  - `source:` `drafted`, `posting` or `user`
- Every chunk is a `## Heading` section. A `# Title` line before the first section is allowed; other text is not.
- Heading: unique in the file, at most 128 characters.
- Section text: at most **600 characters** (about 90 words).
- No invisible or zero-width characters (pasting from a web page can bring them). Phrases like "ignore the
  instructions" or "act as" only warn, because notes reach the model as data.
- At least a third of all notes must have a source other than `drafted` (the shipped-corpus test enforces it).

## What makes a section good
Four parts, inside the 600 characters:
1. **Probe:** the situation or question an interviewer opens with.
2. **Strong:** what a good answer contains, concrete and observable ("names a rollback signal", not "communicates well").
3. **Weak:** what a poor answer sounds like. Lets later feedback grounding (Slice 8e) tell the two apart.
4. **Follow-up:** one or two questions that dig into the answer.

One idea per section: a match returns a single section, so mixing two topics ranks badly for both.
Name the heading the way a job posting would ("Caching and scaling reads"); it is embedded together with the text.

## Where real material comes from
- `source: posting`: skills and wording from 3-5 real postings for that role and level. Use the posting's own words
  ("on-call", "CI/CD", "event-driven"): candidates' job descriptions use the same words, so embeddings match. Do not
  paste company names, salaries, contact details or long verbatim passages.
- `source: user`: what you would expect from a junior versus a senior, or a question you were really asked.

## Check a note before ingesting (reads the file only; no database, no API call)
```sh
uv run python -c "from pathlib import Path; from app.modules.interviews.utils.interviews_knowledge_utils import parse_note; p=Path('app/modules/interviews/data/knowledge/YOUR-NOTE.md'); n=parse_note(p.name,p.read_text(encoding='utf-8')); print(len(n.chunks),'chunks', n.warnings)"
```
Then, with the database up: `uv run python -m app.modules.interviews.tooling.interviews_knowledge_ingest`
(embeds only new or changed sections).
