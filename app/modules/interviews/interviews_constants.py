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


class QuestionKind(StrEnum):
    """A main question opens a thread; a follow-up digs into the latest answer of that thread."""

    main = "main"
    follow_up = "follow_up"


class FollowUpAction(StrEnum):
    """What the decide call may answer (a closed list: anything else is an invalid reply)."""

    follow_up = "follow_up"
    next_question = "next_question"


class FollowUpGap(StrEnum):
    """The one clear gap a follow-up targets. Closed, so the write call gets app data, not model free text."""

    missing_situation = "missing_situation"
    missing_own_action = "missing_own_action"
    missing_result = "missing_result"
    no_tradeoff = "no_tradeoff"
    no_how = "no_how"
    no_example = "no_example"
    partial_answer = "partial_answer"


class MessageKind(StrEnum):
    """Transcript item kinds: a question comes from interview_questions, the other two from interview_messages."""

    question = "question"
    answer = "answer"
    reaction = "reaction"


class TurnPhase(StrEnum):
    """What a streamed answer turn is doing, sent as `status` events so the candidate never waits on a silent page."""

    received = "received"
    deciding = "deciding"
    writing = "writing"


class StreamEvent(StrEnum):
    """The SSE event names of a streamed turn: the contract with the client. `done` and `error` are terminal."""

    status = "status"
    reaction = "reaction"
    question_delta = "question.delta"
    reset = "reset"
    done = "done"
    error = "error"


class AudioContainer(StrEnum):
    """Recording containers a voice answer may arrive in (what browsers' MediaRecorder produces, plus WAV)."""

    webm = "webm"
    ogg = "ogg"
    mp4 = "mp4"
    wav = "wav"


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

# --- Follow-ups: the model decides, the code enforces these (starting values, tuned from the logged latencies) ---
MAX_FOLLOW_UPS = 2
# The decide call never runs longer than this, so a slow one can't eat the time of the question the user sees.
DECIDE_MAX_SECONDS = 10.0
# Below this much time left on the turn, no write call is started: the bank asks instead.
MIN_SECONDS_FOR_WRITE = 5.0
# Kept back from the decide call for the write call that follows it.
WRITE_RESERVE_SECONDS = MIN_SECONDS_FOR_WRITE

# --- SSE streaming of an answer turn ---
# Comment lines sent while a stream is idle, so proxies with idle timeouts keep the connection open.
STREAM_PING_SECONDS = 15

# --- Voice answers (speech-to-text) ---
# Declared upload type (without codec parameters) -> the container it must really be.
AUDIO_CONTENT_TYPES = {
    "audio/webm": AudioContainer.webm,
    "audio/ogg": AudioContainer.ogg,
    "audio/mp4": AudioContainer.mp4,
    "audio/x-m4a": AudioContainer.mp4,
    "audio/m4a": AudioContainer.mp4,
    "audio/wav": AudioContainer.wav,
    "audio/x-wav": AudioContainer.wav,
    "audio/wave": AudioContainer.wav,
}
# Compressed audio can't be measured without decoding, so size bounds a clip (and its cost): 120 s of browser Opus or
# AAC is about 1-2 MB. The web app also stops recording at 120 s.
TRANSCRIPTION_MAX_BYTES = 3 * 1024 * 1024
# Checked against the duration the vendor reports; a little over the web app's 120 s for encoder rounding.
TRANSCRIPTION_MAX_SECONDS = 125
TRANSCRIPTIONS_PER_MINUTE = 10

# Terms Deepgram should favour when it transcribes an answer (keyterm prompting, Nova-3). Without them the spike heard
# "useEffect" as "use event" and "Redis" as "Redix"; keyterms only help the terms listed, so domain phrases are here too.
# Plain text, no weights; each role's list stays far below Deepgram's 500-token cap.
SHARED_KEYTERMS = (
    "API",
    "REST",
    "GraphQL",
    "JSON",
    "OAuth",
    "JWT",
    "CI/CD",
    "Docker",
    "Kubernetes",
    "AWS",
    "PostgreSQL",
    "Redis",
    "TypeScript",
    "microservices",
    "row-level security",
    "QR code",
    "push notification",
    "unit tests",
)
_ROLE_ONLY_KEYTERMS = {
    JobRole.frontend: (
        "React",
        "useEffect",
        "useState",
        "useMemo",
        "TanStack Query",
        "Next.js",
        "Tailwind",
        "Redux",
        "Zustand",
        "Vite",
        "webpack",
        "hydration",
        "server-side rendering",
        "ARIA",
        "flexbox",
        "Core Web Vitals",
        "Storybook",
        "Playwright",
        "Vitest",
    ),
    JobRole.backend: (
        "FastAPI",
        "Django",
        "Flask",
        "Node.js",
        "Express",
        "NestJS",
        "SQLAlchemy",
        "Alembic",
        "MySQL",
        "MongoDB",
        "Kafka",
        "RabbitMQ",
        "Celery",
        "gRPC",
        "nginx",
        "Terraform",
        "idempotency",
        "sharding",
        "N+1 query",
        "rate limiting",
    ),
    JobRole.fullstack: (
        "React",
        "useEffect",
        "TanStack Query",
        "Next.js",
        "Tailwind",
        "Node.js",
        "Express",
        "FastAPI",
        "Prisma",
        "tRPC",
        "Supabase",
        "Vercel",
        "nginx",
        "server-side rendering",
        "rate limiting",
    ),
    JobRole.mobile: (
        "React Native",
        "Expo",
        "Flutter",
        "Swift",
        "SwiftUI",
        "Kotlin",
        "Jetpack Compose",
        "Xcode",
        "Android Studio",
        "TestFlight",
        "App Store",
        "Google Play",
        "Reanimated",
        "deep link",
        "offline-first",
    ),
    JobRole.data: (
        "pandas",
        "NumPy",
        "PySpark",
        "Apache Spark",
        "Airflow",
        "dbt",
        "Snowflake",
        "BigQuery",
        "Databricks",
        "ETL",
        "Kafka",
        "Parquet",
        "Jupyter",
        "scikit-learn",
        "PyTorch",
        "data warehouse",
        "data lake",
    ),
}
ROLE_KEYTERMS: dict[JobRole, tuple[str, ...]] = {
    role: SHARED_KEYTERMS + terms for role, terms in _ROLE_ONLY_KEYTERMS.items()
}

QUESTION_BANK_PATH = Path(__file__).parent / "data" / "questions.json"

# The prompt file in use. Never edit a shipped version in place: stored replies name it.
INTERVIEWER_PROMPT_VERSION = "interviewer_v1"
PROMPTS_DIR = Path(__file__).parent / "prompts"

# --- Context management: what each LLM call sends (see app/core/ai/context.py) ---
INTERVIEWER_TASK = "interviewer_turn"
SUMMARY_TASK = "job_description_summary"
FULL_HISTORY = "full_history"
WINDOW_LEDGER = "window_ledger"
# Stable-prefix prompts: no question number in them, so the system prompt never changes during an interview.
INTERVIEWER_V2_PROMPT_VERSION = "interviewer_v2"
# v2's rules in about half the characters (v2's ~1,400 tokens were most of every call); window_ledger's default.
# v2 stays for comparison: `interviews_evals --prompt interviewer_v2`.
INTERVIEWER_V3_PROMPT_VERSION = "interviewer_v3"
# v3 without the note (moved to the decide call) and with a follow-up mode; window_ledger's default since follow-ups.
INTERVIEWER_V4_PROMPT_VERSION = "interviewer_v4"
# v4's rules as plain text that can be shown while it streams: a `CATEGORY:` line (main questions only), then the
# question. Used by the streamed turn only; the JSON turn keeps v4 until the evals compare them.
INTERVIEWER_V5_PROMPT_VERSION = "interviewer_v5"
INTERVIEWER_STREAM_TASK = "interviewer_stream"
DECISION_TASK = "follow_up_decision"
DECISION_PROMPT_VERSION = "follow_up_decision_v1"
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
