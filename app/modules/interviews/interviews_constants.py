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


# Bank-only role tag: a question tagged "general" is eligible for every JobRole.
GENERAL_ROLE = "general"

MIN_QUESTION_COUNT = 1
MAX_QUESTION_COUNT = 10
FIRST_POSITION = 1
# Bounded now because a later story puts this untrusted text into LLM prompts.
JOB_DESCRIPTION_MAX_LENGTH = 2000

QUESTION_BANK_PATH = Path(__file__).parent / "data" / "questions.json"
