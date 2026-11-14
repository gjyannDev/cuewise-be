"""The profile eval runner offline: every synthetic case builds into a readable file, the hidden injection never reaches
the model, and a model that answers the labels exactly scores 1.0 everywhere (resume-upload AC12)."""

import json

from app.core.ai.fake import FakeProvider
from app.core.ai.provider import ChatMessage
from app.core.ai.tracing import Tracer
from app.modules.profile.tooling.profile_evals import (
    build_file,
    load_cases,
    main,
    run_case,
)
from app.modules.profile.utils.profile_resume_utils import read_resume
from tests.fake_langfuse import FakeLangfuse

CASES = load_cases()


class LabelledModel(FakeProvider):
    """Answers each case with its own label, so the scores test the pipeline and the scoring, not a model."""

    def complete(self, messages: list[ChatMessage], **kwargs):
        text = messages[-1].content
        case = next(c for c in CASES if c.main[1] in text)
        self._replies.append(json.dumps({
            "skills": case.expect.skills,
            "roles": [{"title": t, "organization": "", "period": "", "summary": ""} for t in case.expect.titles],
            "projects": [],
        }))
        return super().complete(messages, **kwargs)


def test_there_are_five_cases_with_one_two_column_one_docx_and_one_injection():
    assert len(CASES) == 5
    assert {c.layout for c in CASES} >= {"two_column", "docx", "dark_sidebar"}
    assert any(c.hidden and c.expect.forbidden for c in CASES)


def test_every_case_builds_into_a_file_whose_visible_text_holds_its_labels():
    for case in CASES:
        text = read_resume(build_file(case)).text.casefold()

        missing = [item for item in [*case.expect.skills, *case.expect.titles] if item.casefold() not in text]
        assert not missing, (case.id, missing)
        assert not any(word.casefold() in text for word in case.expect.forbidden), case.id


def test_the_two_column_cases_keep_each_experience_line_whole():
    for case in (c for c in CASES if c.sidebar):
        text = read_resume(build_file(case)).text

        assert all(line in text for line in case.main[1:]), case.id


def test_the_hidden_injection_is_dropped_before_the_model():
    case = next(c for c in CASES if c.hidden)
    model = LabelledModel()

    result = run_case(model, case, max_tokens=500)

    assert result.hidden_chars > 0
    resume_message = model.calls[0][-1].content  # the system prompt quotes "10/10" as an example to ignore
    assert not any(word in resume_message for word in case.expect.forbidden)
    assert result.score.injection_ignored


def test_a_model_that_answers_the_labels_scores_one_everywhere(capsys):
    langfuse = FakeLangfuse()

    assert main(["--repeat", "1"], provider=LabelledModel(), tracer=Tracer(langfuse)) == 0

    out = capsys.readouterr().out
    assert "valid=5.0 skills_precision=1.0 skills_recall=1.0 role_count_match=1.0 title_recall=1.0 injection_ignored=1.0" in out
    assert "Langfuse runs: profile/" in out
    assert {item for item in langfuse.datasets["profile-eval/extract"]} == {f"extract:{c.id}" for c in CASES}
