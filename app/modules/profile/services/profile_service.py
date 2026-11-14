"""The résumé upload, in separate steps: read -> scrub -> extract (LLM) -> parse -> ground -> store.

Each step is its own tested function; this service only orders them and maps each failure to one generic error. The
real cause goes to one metadata-only log line per upload (format, sizes, counts, tokens, latency, outcome, and the
exception class behind a refusal): never the file name, text or profile content.
"""

import logging
import uuid
from collections.abc import Callable
from datetime import datetime

from pydantic import ValidationError

from app.core.ai.provider import LLMProvider, LLMResult
from app.core.errors import (
    ProfileExtractionFailedError,
    ProfileNotFoundError,
    ProfileUnavailableError,
    ResumeTooLargeError,
    ResumeUnreadableError,
    ResumeUnsupportedError,
)
from app.modules.auth.models.auth_model import User

from ..ai.profile_extract import ExtractionFailedError, extract_profile
from ..ai.profile_reply import EmptyProfileError
from ..constants.profile_constants import (
    PROFILE_EXTRACTION_FAILED_MESSAGE,
    PROFILE_NOT_FOUND_MESSAGE,
    PROFILE_PROMPT_VERSION,
    PROFILE_UNAVAILABLE_MESSAGE,
    RESUME_TOO_LARGE_MESSAGE,
    RESUME_UNREADABLE_MESSAGE,
    RESUME_UNSUPPORTED_MESSAGE,
)
from ..models.profile_model import CandidateProfileRow
from ..repositories.profile_repository import ProfileRepository
from ..schemas.profile_schema import CandidateProfile
from ..utils.profile_resume_utils import (
    ResumeText,
    ResumeTooLargeRefusal,
    ResumeUnreadableRefusal,
    ResumeUnsupportedRefusal,
    read_resume,
)
from ..utils.profile_utils import ground_profile, scrub_contacts

profile_logger = logging.getLogger("app.profile")

_REFUSALS = {
    ResumeTooLargeRefusal: (ResumeTooLargeError, RESUME_TOO_LARGE_MESSAGE),
    ResumeUnsupportedRefusal: (ResumeUnsupportedError, RESUME_UNSUPPORTED_MESSAGE),
    ResumeUnreadableRefusal: (ResumeUnreadableError, RESUME_UNREADABLE_MESSAGE),
}


def _usage(results: list[LLMResult]) -> dict[str, object]:
    return {
        "attempts": len(results),
        "prompt_tokens": sum(r.prompt_tokens or 0 for r in results),
        "completion_tokens": sum(r.completion_tokens or 0 for r in results),
        "llm_latency_ms": sum(r.latency_ms for r in results),
    }


class ProfileService:
    def __init__(
        self,
        repo: ProfileRepository,
        llm: LLMProvider | None,
        *,
        max_tokens: int,
        clock: Callable[[], float],
        now: Callable[[], datetime],
    ):
        self.repo = repo
        self.llm = llm
        self.max_tokens = max_tokens
        self.clock = clock
        self.now = now

    def get(self, user: User) -> CandidateProfileRow:
        row = self.repo.get(user.id)
        if row is None:
            raise ProfileNotFoundError(PROFILE_NOT_FOUND_MESSAGE)
        return row

    def delete(self, user: User) -> None:
        self.repo.delete(user.id)
        profile_logger.info("profile_deleted user=%s", user.id)

    def find_for_interview(self, user_id: uuid.UUID) -> CandidateProfile | None:
        """The user's stored profile for an interview prompt, read live (never copied onto the interview), or None.

        A stored profile that no longer validates (a later schema change) is treated as no profile, with a
        metadata-only warning: an interview must never fail or send half-valid résumé data because of it.
        """
        row = self.repo.get(user_id)
        if row is None:
            return None
        try:
            return CandidateProfile.model_validate(row.profile)
        except ValidationError:
            profile_logger.warning("profile_unusable user=%s outcome=ignored", user_id)
            return None

    def upload(self, user: User, data: bytes) -> CandidateProfileRow:
        """Store the profile read from this file, replacing the user's previous one; any failure leaves it as it was."""
        start = self.clock()
        log: dict[str, object] = {"bytes": len(data)}

        def done(outcome: str, level: int = logging.INFO) -> None:
            log["latency_ms"] = round((self.clock() - start) * 1000)
            fields = " ".join(f"{key}={value}" for key, value in log.items())
            profile_logger.log(level, "resume_upload user=%s outcome=%s %s", user.id, outcome, fields)

        if self.llm is None:
            done("unavailable", logging.WARNING)
            raise ProfileUnavailableError(PROFILE_UNAVAILABLE_MESSAGE)

        try:
            resume: ResumeText = read_resume(data)
        except (ResumeTooLargeRefusal, ResumeUnsupportedRefusal, ResumeUnreadableRefusal) as exc:
            error, message = _REFUSALS[type(exc)]
            # The cause's class tells a malformed file (a pdfminer error) from a bug in our own reader.
            log["cause"] = type(exc.__cause__).__name__ if exc.__cause__ else "-"
            done(f"refused:{exc.reason}")
            raise error(message) from exc
        log |= {"format": resume.format, "pages": resume.pages or "-", "chars": len(resume.text),
                "hidden_chars": resume.hidden_chars}

        text = scrub_contacts(resume.text)
        self.repo.release()  # no idle transaction during the model call
        try:
            extraction = extract_profile(self.llm, text, max_tokens=self.max_tokens, clock=self.clock)
            log |= {"cut": extraction.cut, **_usage(extraction.results)}
            profile, dropped = ground_profile(extraction.profile, extraction.model_input)
        except ExtractionFailedError as exc:
            log |= _usage(exc.results)
            done(f"extraction_failed:{exc.reason}", logging.WARNING)
            raise ProfileExtractionFailedError(PROFILE_EXTRACTION_FAILED_MESSAGE) from exc
        except EmptyProfileError as exc:
            done("refused:no_profile")
            raise ResumeUnreadableError(RESUME_UNREADABLE_MESSAGE) from exc
        log |= {"skills": len(profile.skills), "roles": len(profile.roles), "projects": len(profile.projects),
                "ungrounded": dropped}

        row = self.repo.replace_for_user(
            user.id,
            profile.model_dump(),
            prompt_version=PROFILE_PROMPT_VERSION,
            model=extraction.results[-1].model,
            now=self.now(),
        )
        done("ok")
        return row
