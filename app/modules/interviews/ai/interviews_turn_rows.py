"""How an answer turn's inputs are built from the session, and how a question the LLM wrote is stored as a row.

These two sit with the other `ai/` turn code (they use `InterviewerInputs` and the turn's `Written`), so the `utils/`
helpers stay below `ai/` (tests/test_layers.py).
"""

from collections.abc import Sequence

from app.core.ai.provider import LLMResult

from ..constants.interviews_constants import QuestionKind, QuestionSource
from ..dependencies.models.interviews_model import InterviewQuestion
from ..utils.interviews_session_utils import InterviewSetup, Thread
from ..utils.interviews_utils import QuestionTurn
from .interviews_context import InterviewerInputs
from .interviews_turn_log import sum_known
from .interviews_turn_types import Written


def interviewer_inputs(setup: InterviewSetup, turns: Sequence[QuestionTurn]) -> InterviewerInputs:
    return InterviewerInputs(
        role=setup.role,
        level=setup.level,
        interview_type=setup.interview_type,
        question_count=setup.question_count,
        job_description=setup.job_description_summary or setup.job_description,
        turns=turns,
        summary_used=setup.job_description_summary is not None,
        reference_notes=setup.reference_notes,
        candidate_profile=setup.profile,
    )


def llm_question(
    written: Written,
    results: Sequence[LLMResult],
    position: int,
    main_number: int,
    *,
    kind: QuestionKind = QuestionKind.main,
    thread: Thread | None = None,
    decision_version: str | None = None,
) -> InterviewQuestion:
    """A question the LLM wrote; `results` is every call of the turn, so the stored usage is what the turn cost.

    A follow-up takes its thread's main question as parent and its category, whatever the model would have chosen.
    """
    reply = written.reply
    assert reply is not None
    return InterviewQuestion(
        position=position,
        main_number=main_number,
        kind=kind,
        parent_question_id=thread.main_id if thread else None,
        text=reply.question,
        category=thread.category if thread else reply.category,
        source=QuestionSource.llm,
        model=written.results[-1].model,
        prompt_version=written.prompt_version,
        decision_prompt_version=decision_version,
        prompt_tokens=sum_known([r.prompt_tokens for r in results]),
        completion_tokens=sum_known([r.completion_tokens for r in results]),
        latency_ms=sum(r.latency_ms for r in results),
    )
