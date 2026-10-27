import uuid

from sqlalchemy import Uuid
from sqlalchemy.orm import Mapped, mapped_column


class UUIDPrimaryKeyMixin:
    """Primary key for every table (CLAUDE.md IDs rule).

    UUIDv7 is time-ordered, so new rows append to the index and ordering by id is creation order;
    unlike auto-increment integers, the ids can't be guessed or enumerated from URLs or tokens.
    """

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid7)
