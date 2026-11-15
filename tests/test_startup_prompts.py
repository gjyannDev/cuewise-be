"""The app lifespan runs the prompt check before anything else (prompt-registry AC8, EC5, EC6)."""

import pytest
from fastapi.testclient import TestClient

from app import main
from app.modules.interviews.utils.interviews_prompt_utils import PromptCheckError


def test_the_app_starts_with_the_shipped_prompts():
    with TestClient(main.app) as http:
        assert http.get("/health").status_code == 200


def test_a_failed_prompt_check_stops_startup_before_the_provider_is_built(monkeypatch):
    built = []

    def broken():
        raise PromptCheckError("Prompt check failed:\ninterviewer_v8_json: file not found")

    monkeypatch.setattr(main, "check_prompts", broken)
    monkeypatch.setattr(main, "build_tracer", lambda _settings: built.append("tracer"))

    with pytest.raises(PromptCheckError, match="interviewer_v8_json: file not found"), TestClient(main.app):
        pass
    assert built == []
