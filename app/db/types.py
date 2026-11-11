"""Column types shared by every module."""

from pgvector.sqlalchemy import VECTOR
from sqlalchemy import JSON
from sqlalchemy.types import TypeEngine


def portable_vector(size: int) -> TypeEngine[list[float]]:
    """A fixed-size vector column: pgvector's `vector(size)` on Postgres, a JSON list on SQLite.

    Postgres (with the `vector` extension) can rank rows by distance inside the query (`<=>`). The test suite runs on
    in-memory SQLite, which has no vector type, so there the same column holds a JSON list and similarity is computed
    in Python; an opt-in Postgres test checks that both orderings agree. Both read back as `list[float]`.
    """
    return VECTOR(size).with_variant(JSON(), "sqlite")
