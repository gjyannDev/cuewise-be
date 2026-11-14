"""Synthetic résumé data and the scripted model shared by the profile tests (no real person anywhere)."""

import json
from contextlib import nullcontext

from app.core.ai.fake import FakeProvider
from app.core.ai.tracing import Tracer, TracingProvider
from tests.fake_langfuse import FakeLangfuse
from tests.resume_files import Text, make_docx, make_pdf

# A synthetic résumé (no real person). The contact line must never reach the model.
RESUME_LINES = [
    "Ana Example - ana.example@mail.test - +63 917 555 0123",
    "Skills: Python, FastAPI, PostgreSQL, Redis, Docker",
    "Senior Backend Engineer, Acme Payments (2021-2024)",
    "Rebuilt the payments API in Python and FastAPI for two million users.",
    "Backend Engineer, Northwind Retail (2018-2021)",
    "Built the order service in Go and Postgres and led the move to Kubernetes.",
    "Project Ledger: a double-entry ledger service in Go with Kafka.",
]

PROFILE = {
    "skills": ["Python", "FastAPI", "PostgreSQL", "Redis", "Docker"],
    "roles": [
        {"title": "Senior Backend Engineer", "organization": "Acme Payments", "period": "2021-2024",
         "summary": "Rebuilt the payments API for two million users."},
        {"title": "Backend Engineer", "organization": "Northwind Retail", "period": "2018-2021",
         "summary": "Built the order service and led the move to Kubernetes."},
    ],
    "projects": [{"name": "Ledger", "description": "A double-entry ledger service.", "technologies": ["Go", "Kafka"]}],
}


def resume_pdf(lines=RESUME_LINES, *, extra=()):
    return make_pdf([[Text(72, 720 - i * 16, line) for i, line in enumerate(lines)] + list(extra)])


def resume_docx(lines=RESUME_LINES, *, extra_runs=()):
    paragraphs = [[(line, {})] for line in lines]
    if extra_runs:
        paragraphs.append(list(extra_runs))
    return make_docx(paragraphs)


def profile_json(**overrides) -> str:
    return json.dumps(PROFILE | overrides)


class ProfileLLM:
    """The scripted model behind the real tracing wrapper, so traces are observed as Langfuse would get them."""

    def __init__(self):
        self.langfuse = FakeLangfuse()
        self.tracer = Tracer(self.langfuse, propagate=lambda **_: nullcontext())
        self.script()

    def script(self, *replies):
        self.fake = FakeProvider(replies, default=profile_json())
        self.provider = TracingProvider(self.fake, self.tracer)
        return self.fake

    @property
    def calls(self):
        return self.fake.calls

    def model_input(self, call: int = 0) -> str:
        return "\n".join(m.content for m in self.fake.calls[call])
