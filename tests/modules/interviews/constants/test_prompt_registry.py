"""The prompt registry's guards (prompt-registry AC1, AC2, AC6, EC1-EC4).

Each rule is a pure function over plain data, so it is tested on a synthetic failing case and then on the real
registry. A failure names the file, task, variant or version that broke the rule.
"""

import ast
from collections.abc import Collection, Mapping
from pathlib import Path

from app.modules.interviews.constants import interviews_constants
from app.modules.interviews.constants import interviews_prompt_registry as registry
from app.modules.interviews.constants.interviews_constants import PROMPTS_DIR
from app.modules.interviews.constants.interviews_prompt_registry import (
    Data,
    PromptVersion,
    Status,
)


def catalog_mismatches(catalog: Collection[str], files: Collection[str]) -> list[str]:
    missing = [f"{name}.md has no catalog entry" for name in sorted(set(files) - set(catalog))]
    extra = [f"catalog entry {name} has no file" for name in sorted(set(catalog) - set(files))]
    return missing + extra


def incomplete_entries(catalog: Mapping[str, PromptVersion]) -> list[str]:
    return [
        f"{name}: needs its file name, a status and a reason"
        for name, entry in catalog.items()
        if entry.name != name or not isinstance(entry.status, Status) or not entry.why.strip()
    ]


def archived_routes(routes: Mapping[str, str], catalog: Mapping[str, PromptVersion]) -> list[str]:
    problems = []
    for where, version in routes.items():
        if version not in catalog:
            problems.append(f"{where} routes to {version}, which is not in the catalog")
        elif catalog[version].status == Status.archived:
            problems.append(f"{where} routes to {version}, which is archived")
    return problems


def variant_gaps(tables: Mapping[str, Mapping[Data, str]]) -> list[str]:
    return [
        f"{table} lacks {', '.join(sorted(set(Data) - set(versions)))}"
        for table, versions in tables.items()
        if set(versions) != set(Data)
    ]


def version_literals(files: Mapping[str, str], versions: Collection[str]) -> list[str]:
    """A string literal that is exactly a version name, outside the registry: a version chosen somewhere else."""
    return [
        f"{path}:{node.lineno}: {node.value!r}"
        for path, source in sorted(files.items())
        for node in ast.walk(ast.parse(source))
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value in versions
    ]


def real_routes() -> dict[str, str]:
    routes = {
        f"{table}[{variant}]": version
        for table, versions in registry.INTERVIEWER_ROUTES.items()
        for variant, version in versions.items()
    }
    return routes | dict(registry.SINGLE_ROUTES)


# --- each rule fails on a synthetic case ---


def test_a_file_without_an_entry_and_an_entry_without_a_file_are_named():  # EC1, EC2
    assert catalog_mismatches({"a_v1", "b_v1"}, {"a_v1", "c_v1"}) == [
        "c_v1.md has no catalog entry",
        "catalog entry b_v1 has no file",
    ]


def test_an_entry_with_no_reason_or_a_wrong_name_is_named():
    catalog = {
        "a_v1": PromptVersion("a_v1", Status.live, " "),
        "b_v1": PromptVersion("other", Status.live, "why"),
        "c_v1": PromptVersion("c_v1", Status.archived, "why"),
    }
    assert incomplete_entries(catalog) == [
        "a_v1: needs its file name, a status and a reason",
        "b_v1: needs its file name, a status and a reason",
    ]


def test_a_route_to_an_archived_or_unknown_version_is_named():  # EC3
    catalog = {
        "old_v1": PromptVersion("old_v1", Status.archived, "why"),
        "new_v2": PromptVersion("new_v2", Status.live, "why"),
        "try_v3": PromptVersion("try_v3", Status.experiment, "why"),
    }
    routes = {"json[plain]": "old_v1", "stream[plain]": "new_v2", "baseline": "try_v3", "decide": "gone_v1"}
    assert archived_routes(routes, catalog) == [
        "json[plain] routes to old_v1, which is archived",
        "decide routes to gone_v1, which is not in the catalog",
    ]


def test_a_table_missing_a_variant_is_named():  # EC4
    tables = {"json": {Data.plain: "a", Data.notes: "b", Data.profile: "c"}, "stream": {Data.plain: "a"}}
    assert variant_gaps(tables) == ["stream lacks notes, profile"]


def test_a_version_literal_is_named_but_prose_mentioning_one_is_not():  # AC3
    files = {"app/x.py": 'V = "interviewer_v8"\n"""Uses interviewer_v8 for profiles."""\n'}
    assert version_literals(files, {"interviewer_v8"}) == ["app/x.py:1: 'interviewer_v8'"]


# --- the real registry ---


def test_the_catalog_matches_the_prompt_files():  # AC1, EC1, EC2
    assert catalog_mismatches(registry.CATALOG, {p.stem for p in PROMPTS_DIR.glob("*.md")}) == []


def test_every_catalog_entry_has_a_status_and_a_reason():  # AC1
    assert incomplete_entries(registry.CATALOG) == []


def test_no_route_points_at_an_archived_version():  # EC3
    assert archived_routes(real_routes(), registry.CATALOG) == []


def test_both_interviewer_tables_cover_every_variant():  # EC4
    assert variant_gaps(registry.INTERVIEWER_ROUTES) == []


def test_the_routes_are_todays_versions():  # AC2
    assert dict(registry.INTERVIEWER_JSON) == {
        Data.plain: "interviewer_v4",
        Data.notes: "interviewer_v7_json",
        Data.profile: "interviewer_v8_json",
    }
    assert dict(registry.INTERVIEWER_STREAM) == {
        Data.plain: "interviewer_v5",
        Data.notes: "interviewer_v7",
        Data.profile: "interviewer_v8",
    }
    assert dict(registry.SINGLE_ROUTES) == {
        "full_history": "interviewer_v1",
        "follow_up_decision": "follow_up_decision_v1",
        "job_description_summary": "job_description_summary_v2",
        "feedback_score": "feedback_score_v2",
        "feedback_write": "feedback_write_v1",
    }


def test_the_old_constant_names_are_aliases_of_the_registry():  # AC10, EC11
    aliases = {
        "INTERVIEWER_PROMPT_VERSION": registry.FULL_HISTORY_VERSION,
        "INTERVIEWER_V2_PROMPT_VERSION": registry.INTERVIEWER_V2,
        "INTERVIEWER_V3_PROMPT_VERSION": registry.INTERVIEWER_V3,
        "INTERVIEWER_V4_PROMPT_VERSION": registry.INTERVIEWER_JSON[Data.plain],
        "INTERVIEWER_V5_PROMPT_VERSION": registry.INTERVIEWER_STREAM[Data.plain],
        "INTERVIEWER_V7_PROMPT_VERSION": registry.INTERVIEWER_STREAM[Data.notes],
        "INTERVIEWER_V7_JSON_PROMPT_VERSION": registry.INTERVIEWER_JSON[Data.notes],
        "INTERVIEWER_V8_PROMPT_VERSION": registry.INTERVIEWER_STREAM[Data.profile],
        "INTERVIEWER_V8_JSON_PROMPT_VERSION": registry.INTERVIEWER_JSON[Data.profile],
        "DECISION_PROMPT_VERSION": registry.DECISION_VERSION,
        "SUMMARY_PROMPT_VERSION": registry.SUMMARY_VERSION,
        "FEEDBACK_SCORE_PROMPT_VERSION": registry.FEEDBACK_SCORE_VERSION,
        "FEEDBACK_WRITE_PROMPT_VERSION": registry.FEEDBACK_WRITE_VERSION,
    }
    assert {name: getattr(interviews_constants, name) for name in aliases} == aliases


def test_no_version_name_is_written_outside_the_registry():  # AC3
    app = Path(__file__).resolve().parents[4] / "app"
    registry_file = Path(registry.__file__).resolve()
    files = {
        p.relative_to(app.parent).as_posix(): p.read_text(encoding="utf-8")
        for p in app.rglob("*.py")
        if p.resolve() != registry_file
    }
    assert version_literals(files, registry.CATALOG) == []
