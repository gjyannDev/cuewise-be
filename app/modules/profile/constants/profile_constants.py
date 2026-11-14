"""Limits, thresholds and messages of the résumé upload (resume-upload spec)."""

# --- the file ---
RESUME_MAX_BYTES = 2 * 1024 * 1024
RESUME_MAX_PAGES = 5
# A DOCX is a zip: its parts' declared sizes, read from the zip directory without unpacking (zip bombs).
RESUME_MAX_UNZIPPED_BYTES = 10 * 1024 * 1024
# Below this much visible text there is nothing to build a profile from (a scan, a near-empty page).
RESUME_MIN_CHARS = 150

# --- hidden text (spec: dropped before the model) ---
# A colour at or above this lightness (0 black .. 1 white) is "near-white": invisible on a white page.
NEAR_WHITE = 0.9
# A filled shape or image behind near-white text makes it visible when the shape is at most this light.
DARK_BACKGROUND = 0.6
# Text smaller than this (points) is not meant to be read.
MIN_FONT_SIZE = 4.0

# --- two-column reading ---
# An empty vertical band at least this wide (points), with words on both sides, splits a page into two columns.
COLUMN_MIN_GAP = 18.0
# Each side must hold at least this many lines, so one stray word or one wide line is not a column. Lines, not a share
# of words: a skills sidebar holds few words (about a tenth of the page) but many lines.
COLUMN_MIN_LINES = 3

# --- the model call ---
# About four pages of dense text; the rest is cut (the first part is kept) and the log says so.
PROFILE_INPUT_MAX_CHARS = 12_000
PROFILE_TOTAL_SECONDS = 20.0
PROFILE_PROMPT_VERSION = "profile_extract_v1"
PROFILE_TASK = "profile-extract"
# Extraction copies facts; a low temperature keeps two runs on the same résumé close (and the eval comparable).
PROFILE_TEMPERATURE = 0.0
RESUME_UPLOADS_PER_MINUTE = 5

# --- the profile's caps (worst case under 4,000 characters as JSON, so 8d's prompt cost is bounded; AC13) ---
MAX_SKILLS = 20
MAX_ROLES = 4
MAX_PROJECTS = 3
MAX_TECHNOLOGIES = 6
SKILL_MAX_LENGTH = 30
TITLE_MAX_LENGTH = 60
ORGANIZATION_MAX_LENGTH = 60
PERIOD_MAX_LENGTH = 20
SUMMARY_MAX_LENGTH = 220
PROJECT_NAME_MAX_LENGTH = 60
DESCRIPTION_MAX_LENGTH = 220
TECHNOLOGY_MAX_LENGTH = 30
PROFILE_MAX_JSON_CHARS = 4_000

# --- messages (generic; each ends with a next step) ---
RESUME_TOO_LARGE_MESSAGE = "That file is too large. Please upload a PDF or Word résumé of up to 2 MB and 5 pages."
RESUME_UNSUPPORTED_MESSAGE = "That file isn't a PDF or Word document. Please upload a PDF or .docx résumé."
RESUME_UNREADABLE_MESSAGE = (
    "We couldn't read a résumé from that file. Please upload a text-based PDF or Word résumé "
    "(not a scan or a password-protected file)."
)
PROFILE_EXTRACTION_FAILED_MESSAGE = "We couldn't read your résumé right now. Please try again in a moment."
PROFILE_UNAVAILABLE_MESSAGE = "The résumé feature isn't available right now. Please try again later."
PROFILE_NOT_FOUND_MESSAGE = "You haven't uploaded a résumé yet. Upload one to create your profile."
