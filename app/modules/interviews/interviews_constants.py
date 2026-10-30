from enum import StrEnum
from pathlib import Path


class JobRole(StrEnum):
    frontend = "frontend"
    backend = "backend"
    fullstack = "fullstack"
    mobile = "mobile"
    data = "data"


class Level(StrEnum):
    intern = "intern"
    junior = "junior"
    mid = "mid"
    senior = "senior"


class QuestionCategory(StrEnum):
    behavioral = "behavioral"
    technical = "technical"


class InterviewType(StrEnum):
    behavioral = "behavioral"
    technical = "technical"
    mixed = "mixed"


class SessionStatus(StrEnum):
    in_progress = "in_progress"
    abandoned = "abandoned"
    completed = "completed"


class MessageRole(StrEnum):
    candidate = "candidate"
    interviewer = "interviewer"


class QuestionSource(StrEnum):
    """Who wrote a stored question: the LLM, or the hand-written bank (fallback and pre-slice-2 sessions)."""

    llm = "llm"
    bank = "bank"


class MessageKind(StrEnum):
    """Transcript item kinds: a question comes from interview_questions, the other two from interview_messages."""

    question = "question"
    answer = "answer"
    reaction = "reaction"


# Bank-only role tag: a question tagged "general" is eligible for every JobRole.
GENERAL_ROLE = "general"

MIN_QUESTION_COUNT = 1
MAX_QUESTION_COUNT = 10
FIRST_POSITION = 1
# Bounded now because a later story puts this untrusted text into LLM prompts.
JOB_DESCRIPTION_MAX_LENGTH = 2000
# Bounds the tokens (and money) one answer can push into every later LLM call of the session.
MAX_ANSWER_LENGTH = 2000
# An LLM-written question longer than this is treated as an invalid reply (a rambling model, not a question).
MAX_QUESTION_LENGTH = 500
# One retry for a reply that came back but broke the contract; never more (each attempt costs a call).
MAX_REPLY_ATTEMPTS = 2
# A retry is only worth starting if this much of the turn's LLM time budget is left.
MIN_SECONDS_FOR_RETRY = 5.0

QUESTION_BANK_PATH = Path(__file__).parent / "data" / "questions.json"

# The prompt file in use. Never edit a shipped version in place: stored replies name it.
INTERVIEWER_PROMPT_VERSION = "interviewer_v1"
PROMPTS_DIR = Path(__file__).parent / "prompts"

# --- Context management: what each LLM call sends (see app/core/ai/context.py) ---
INTERVIEWER_TASK = "interviewer_turn"
SUMMARY_TASK = "job_description_summary"
FULL_HISTORY = "full_history"
WINDOW_LEDGER = "window_ledger"
# Stable-prefix prompt used by window_ledger: no question number in it, so the system prompt never changes.
INTERVIEWER_V2_PROMPT_VERSION = "interviewer_v2"
SUMMARY_PROMPT_VERSION = "job_description_summary_v2"
# Starting values, tuned by the eval comparison (docs/features/context-management/learnings.md).
WINDOW_TURNS = 3
WINDOW_ANSWER_CAP = 600
# Estimated tokens. A safety net, not a cost target: a worst-case window_ledger call is about 4,000.
WINDOW_INPUT_LIMIT = 5000
TRUNCATION_MARKER = " [answer shortened]"
NOTE_MAX_LENGTH = 200
# A job description longer than this is condensed once at interview start.
SUMMARY_THRESHOLD = 600
SUMMARY_MAX_LENGTH = 500
# Models count tokens, not characters, so the prompt asks for words: 60 words is about 400 characters, under the cap.
SUMMARY_MAX_WORDS = 60
SUMMARY_TIME_CAP_SECONDS = 10.0

# Fills {{level_guidance}} in interviewer_v2, so difficulty is spelled out rather than left to the level word.
LEVEL_GUIDANCE = {
    Level.intern: (
        "For an intern, test fundamentals and how they learn; school or personal projects are fine as examples; "
        "one concept per question."
    ),
    Level.junior: (
        "For a junior, focus on everyday work: small features, debugging, reading existing code and handling "
        "review feedback."
    ),
    Level.mid: (
        "For a mid-level developer, focus on owning features end to end, design trade-offs, production issues and "
        "working across teams."
    ),
    Level.senior: (
        "For a senior, focus on system design at scale, ambiguous problems, technical leadership, mentoring and "
        "cross-team decisions."
    ),
}


class LevelGroup(StrEnum):
    """Reactions are warmer for people early in their career and briefer for experienced ones."""

    early = "early"
    experienced = "experienced"


LEVEL_GROUPS = {
    Level.intern: LevelGroup.early,
    Level.junior: LevelGroup.early,
    Level.mid: LevelGroup.experienced,
    Level.senior: LevelGroup.experienced,
}

# Predefined reactions shown after an answer: no LLM, no tokens, no risk. The app can't tell a strong answer from a
# weak one, so every line is a neutral acknowledgement (no praise, verdict or score); a test enforces the rules.
# Placeholder copy: edit freely while keeping at least 5 entries per pool.
REACTION_POOLS: dict[tuple[QuestionCategory, LevelGroup], tuple[str, ...]] = {
    (QuestionCategory.behavioral, LevelGroup.early): (
        "Thanks for sharing that experience with me.",
        "Thank you for walking me through that.",
        "I appreciate you telling me about that.",
        "Thanks, that helps me understand how you work.",
        "Thank you for being open about that experience.",
        "Thanks for taking the time to explain that.",
    ),
    (QuestionCategory.behavioral, LevelGroup.experienced): (
        "Thanks for sharing that.",
        "Understood, thank you.",
        "Got it, thanks.",
        "Thank you, that is helpful context.",
        "Noted, thanks for the detail.",
        "Thanks, that gives me a clear picture.",
    ),
    (QuestionCategory.technical, LevelGroup.early): (
        "Thanks for talking me through your thinking.",
        "Thank you for explaining your approach.",
        "I appreciate you walking me through that.",
        "Thanks, it helps to hear how you reason about it.",
        "Thank you for sharing how you would tackle that.",
    ),
    (QuestionCategory.technical, LevelGroup.experienced): (
        "Thanks for walking through that.",
        "Understood, thanks for the explanation.",
        "Got it, thank you.",
        "Noted, thanks for the detail on your approach.",
        "Thanks, that is clear.",
    ),
}

# Shown after the last answer, when the interview completes.
CLOSING_REACTIONS: dict[LevelGroup, tuple[str, ...]] = {
    LevelGroup.early: (
        "Thank you, that was the last question. Thanks for taking the time to practice.",
        "That was the final question. Thank you for your time today.",
        "Thanks, that wraps up the interview. I appreciate your time.",
        "That brings us to the end of the interview. Thank you for practicing with me.",
        "Thank you, we are done with the questions for today.",
    ),
    LevelGroup.experienced: (
        "Thanks, that was the last question.",
        "That wraps up the interview. Thank you for your time.",
        "That was the final question, thanks.",
        "We are done for today. Thank you.",
        "Thanks, that completes the interview.",
    ),
}
