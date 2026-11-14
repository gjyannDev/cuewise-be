from typing import Any, ClassVar

from pydantic import BaseModel


class AppError(Exception):
    """Base for expected errors. Services raise these instead of HTTPException."""

    status_code: ClassVar[int] = 500
    code: ClassVar[str] = "INTERNAL_ERROR"
    headers: ClassVar[dict[str, str] | None] = None

    def __init__(self, message: str, details: Any = None, headers: dict[str, str] | None = None):
        super().__init__(message)
        self.message = message
        self.details = details
        # Instance copy so per-raise headers never mutate the class-level dict.
        self.response_headers = {**(type(self).headers or {}), **(headers or {})}


class BadRequestError(AppError):
    status_code, code = 400, "BAD_REQUEST"


class ForbiddenError(AppError):
    status_code, code = 403, "FORBIDDEN"


class NotFoundError(AppError):
    status_code, code = 404, "NOT_FOUND"


class ConflictError(AppError):
    status_code, code = 409, "CONFLICT"


class NotEnoughQuestionsError(ConflictError):
    code = "NOT_ENOUGH_QUESTIONS"


class ProfileRequiredError(ConflictError):
    """An interview asked to use the candidate's profile, and there is none to use (resume-aware-interview)."""

    code = "PROFILE_REQUIRED"


class SessionNotInProgressError(ConflictError):
    code = "SESSION_NOT_IN_PROGRESS"


class QuestionNotCurrentError(ConflictError):
    code = "QUESTION_NOT_CURRENT"


class InterviewNotCompletedError(ConflictError):
    code = "INTERVIEW_NOT_COMPLETED"


class FeedbackInProgressError(ConflictError):
    code = "FEEDBACK_IN_PROGRESS"


class FeedbackNotFoundError(NotFoundError):
    code = "FEEDBACK_NOT_FOUND"


class FeedbackFailedError(AppError):
    """The LLM could not produce valid scores in time: nothing partial is returned; the client may POST again."""

    status_code, code = 502, "FEEDBACK_FAILED"


class FeedbackUnavailableError(AppError):
    status_code, code = 503, "FEEDBACK_UNAVAILABLE"


class AudioTooLargeError(AppError):
    status_code, code = 413, "AUDIO_TOO_LARGE"


class UnsupportedAudioError(AppError):
    status_code, code = 415, "UNSUPPORTED_AUDIO"


class AudioTooLongError(AppError):
    status_code, code = 422, "AUDIO_TOO_LONG"


class NoSpeechError(AppError):
    status_code, code = 422, "NO_SPEECH"


class RateLimitedError(AppError):
    """Raise with `headers={"Retry-After": "<seconds>"}`."""

    status_code, code = 429, "RATE_LIMITED"


class TranscriptionUnavailableError(AppError):
    status_code, code = 503, "TRANSCRIPTION_UNAVAILABLE"


class JobUrlUnreachableError(AppError):
    """Any network-side failure of a job link. One message for every cause, so refusals can't map internal hosts."""

    status_code, code = 422, "JOB_URL_UNREACHABLE"


class JobUrlUnreadableError(AppError):
    """The job link answered, but no job description could be read from it (not HTML, too large, too little text)."""

    status_code, code = 422, "JOB_URL_UNREADABLE"


class JobTextUnreadableError(AppError):
    """A pasted page held no job description (too little text, or not recognisably a posting)."""

    status_code, code = 422, "JOB_TEXT_UNREADABLE"


class ResumeTooLargeError(AppError):
    """Over the byte, page or unzipped-size limit of a résumé upload."""

    status_code, code = 413, "RESUME_TOO_LARGE"


class ResumeUnsupportedError(AppError):
    """Not a PDF or a Word document by its content (the file name is never trusted)."""

    status_code, code = 415, "RESUME_UNSUPPORTED"


class ResumeUnreadableError(AppError):
    """Encrypted, corrupt, scanned, too little text, or no usable profile in it."""

    status_code, code = 422, "RESUME_UNREADABLE"


class ProfileExtractionFailedError(AppError):
    """The model gave no valid profile after the retry, timed out, or the provider failed."""

    status_code, code = 502, "PROFILE_EXTRACTION_FAILED"


class ProfileUnavailableError(AppError):
    status_code, code = 503, "PROFILE_UNAVAILABLE"


class ProfileNotFoundError(AppError):
    status_code, code = 404, "PROFILE_NOT_FOUND"


class UnauthorizedError(AppError):
    status_code, code = 401, "UNAUTHORIZED"
    headers = {"WWW-Authenticate": "Bearer"}  # noqa: RUF012


class InvalidCredentialsError(UnauthorizedError):
    code = "INVALID_CREDENTIALS"


class TokenMissingError(UnauthorizedError):
    code = "TOKEN_MISSING"


class TokenExpiredError(UnauthorizedError):
    code = "TOKEN_EXPIRED"


class TokenInvalidError(UnauthorizedError):
    code = "TOKEN_INVALID"


class ErrorBody(BaseModel):
    code: str
    message: str
    details: Any = None
    request_id: str | None = None


class ErrorResponse(BaseModel):
    error: ErrorBody
