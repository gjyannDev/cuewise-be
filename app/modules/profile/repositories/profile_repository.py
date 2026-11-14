import uuid
from datetime import datetime

from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..models.profile_model import CandidateProfileRow


class ProfileRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id: uuid.UUID) -> CandidateProfileRow | None:
        return self.db.scalar(select(CandidateProfileRow).where(CandidateProfileRow.user_id == user_id))

    def release(self) -> None:
        """End the read transaction before the slow model call, so no connection sits idle in a transaction."""
        self.db.rollback()

    def replace_for_user(
        self, user_id: uuid.UUID, profile: dict, *, prompt_version: str, model: str, now: datetime
    ) -> CandidateProfileRow:
        """The user's one profile, inserted or replaced in one commit. Select-then-write (portable to the SQLite test
        database); if a concurrent upload inserted first, the unique user_id refuses ours and we retry once as an
        update."""
        for attempt in range(2):
            try:
                row = self.get(user_id)
                if row is None:
                    row = CandidateProfileRow(user_id=user_id)
                    self.db.add(row)
                row.profile = profile
                row.prompt_version, row.model, row.updated_at = prompt_version, model, now
                self.db.commit()
            except IntegrityError:
                self.db.rollback()
                if attempt:
                    raise
                continue
            except Exception:
                self.db.rollback()
                raise
            self.db.refresh(row)
            return row
        raise AssertionError("unreachable")  # pragma: no cover

    def delete(self, user_id: uuid.UUID) -> None:
        """Hard delete; a no-op when there is none."""
        try:
            self.db.execute(delete(CandidateProfileRow).where(CandidateProfileRow.user_id == user_id))
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
