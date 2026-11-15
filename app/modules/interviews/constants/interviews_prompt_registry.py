"""Every interviews prompt version, and which one each LLM call sends. Data only: nothing here reads or renders a file.

Reading it: the routing tables say what a task sends; the catalog says what each version is and why it exists.

Adding a version (never edit a shipped .md in place: stored replies, logs and traces name the version):
1. Copy the current file to `prompts/<name>_v<N+1>.md` and change the copy.
2. Add a constant and a CATALOG entry below, with its status and the one line saying why it exists.
3. Point the route at it (and set the old one to archived, or experiment if the evals still compare against it).
The guard tests (tests/modules/interviews/constants/test_prompt_registry.py) fail until the file, the entry and the
route agree; the startup check refuses to start if a routed file is missing or has a placeholder its renderer lacks.
"""

from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from types import MappingProxyType


class Data(StrEnum):
    """What an interviewer write carries beyond the job description; it picks the prompt."""

    plain = "plain"
    # The interview's reference notes (knowledge-base RAG, Slice 8a).
    notes = "notes"
    # The candidate profile, with any notes too (resume-aware interview, Slice 8d).
    profile = "profile"


class Status(StrEnum):
    # A request can send it today.
    live = "live"
    # Only the eval runner sends it, as a baseline to compare against.
    experiment = "experiment"
    # Never routed; kept so stored replies stay explained and old eval runs can be repeated (`--prompt`).
    archived = "archived"


@dataclass(frozen=True)
class PromptVersion:
    name: str  # the file stem: prompts/<name>.md
    status: Status
    why: str


INTERVIEWER_V1 = "interviewer_v1"
INTERVIEWER_V2 = "interviewer_v2"
INTERVIEWER_V3 = "interviewer_v3"
INTERVIEWER_V4 = "interviewer_v4"
INTERVIEWER_V5 = "interviewer_v5"
INTERVIEWER_V7 = "interviewer_v7"
INTERVIEWER_V7_JSON = "interviewer_v7_json"
INTERVIEWER_V8 = "interviewer_v8"
INTERVIEWER_V8_JSON = "interviewer_v8_json"
FOLLOW_UP_DECISION_V1 = "follow_up_decision_v1"
JOB_DESCRIPTION_SUMMARY_V2 = "job_description_summary_v2"
FEEDBACK_SCORE_V2 = "feedback_score_v2"
FEEDBACK_WRITE_V1 = "feedback_write_v1"

_VERSIONS = (
    # --- interviewer: writes the next question ---
    PromptVersion(INTERVIEWER_V1, Status.experiment, "The first writer: question number in the prompt, whole history sent; full_history baseline."),
    PromptVersion(INTERVIEWER_V2, Status.archived, "Stable prefix: no question number, so the system prompt is the same on every call of an interview."),
    PromptVersion(INTERVIEWER_V3, Status.archived, "v2's rules in about half the characters (v2's ~1,400 tokens were most of every call)."),
    PromptVersion(INTERVIEWER_V4, Status.live, "v3 without the answer note (moved to the decide call) and with a follow-up mode; the JSON writer."),
    PromptVersion(INTERVIEWER_V5, Status.live, "v4's rules as plain text (a CATEGORY: line, then the question), so the reply can stream."),
    PromptVersion("interviewer_v6", Status.archived, "v5 plus reference notes; the notes chose the topic and crowded out the job description (skill_coverage 0.83 -> 0.57)."),
    PromptVersion("interviewer_v6_json", Status.archived, "v6 in the JSON format; replaced by v7_json for the same reason."),
    PromptVersion(INTERVIEWER_V7, Status.live, "v5 plus reference notes: the job description picks the topic, the notes only set the depth."),
    PromptVersion(INTERVIEWER_V7_JSON, Status.live, "v7 in v4's JSON format."),
    PromptVersion(INTERVIEWER_V8, Status.live, "v7 plus the candidate profile, used only for main questions of an opted-in interview; drops 'developer' from the role line."),
    PromptVersion(INTERVIEWER_V8_JSON, Status.live, "v8 in v4's JSON format."),
    # --- the other tasks ---
    PromptVersion(FOLLOW_UP_DECISION_V1, Status.live, "Judges the latest answer within its thread: follow up on one named gap, or move on."),
    PromptVersion("job_description_summary_v1", Status.archived, "First summary prompt; models counted the cap in words and came back too long (summary_invalid:too_long)."),
    PromptVersion(JOB_DESCRIPTION_SUMMARY_V2, Status.live, "Asks for words and states the character cap, after v1 replies came back too long."),
    PromptVersion("feedback_score_v1", Status.archived, "First rubric scorer; a whole-answer quote broke the 200-character evidence limit on both attempts."),
    PromptVersion(FEEDBACK_SCORE_V2, Status.live, "One-sentence quotes, and no evidence item when no single sentence shows a criterion."),
    PromptVersion(FEEDBACK_WRITE_V1, Status.live, "Writes the coaching text from the stored scores and evidence, never from the answers."),
)
CATALOG: Mapping[str, PromptVersion] = MappingProxyType({v.name: v for v in _VERSIONS})

# --- routing: what each task sends ---

# Task interviewer_turn (the first question and the JSON answer route).
INTERVIEWER_JSON: Mapping[Data, str] = MappingProxyType(
    {Data.plain: INTERVIEWER_V4, Data.notes: INTERVIEWER_V7_JSON, Data.profile: INTERVIEWER_V8_JSON}
)
# Task interviewer_stream (the streamed answer turn; plain text so it can be shown while it streams).
INTERVIEWER_STREAM: Mapping[Data, str] = MappingProxyType(
    {Data.plain: INTERVIEWER_V5, Data.notes: INTERVIEWER_V7, Data.profile: INTERVIEWER_V8}
)
INTERVIEWER_ROUTES: Mapping[str, Mapping[Data, str]] = MappingProxyType(
    {"interviewer_turn": INTERVIEWER_JSON, "interviewer_stream": INTERVIEWER_STREAM}
)

# The full_history strategy: never the live default, only the eval runner's baseline.
FULL_HISTORY_VERSION = INTERVIEWER_V1
DECISION_VERSION = FOLLOW_UP_DECISION_V1
SUMMARY_VERSION = JOB_DESCRIPTION_SUMMARY_V2
FEEDBACK_SCORE_VERSION = FEEDBACK_SCORE_V2
FEEDBACK_WRITE_VERSION = FEEDBACK_WRITE_V1
SINGLE_ROUTES: Mapping[str, str] = MappingProxyType(
    {
        "full_history": FULL_HISTORY_VERSION,
        "follow_up_decision": DECISION_VERSION,
        "job_description_summary": SUMMARY_VERSION,
        "feedback_score": FEEDBACK_SCORE_VERSION,
        "feedback_write": FEEDBACK_WRITE_VERSION,
    }
)
