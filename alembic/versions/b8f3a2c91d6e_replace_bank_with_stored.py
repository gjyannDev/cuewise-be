"""replace the question bank with stored questions: source 'bank' -> 'stored', drop bank_id (U3c)

Revision ID: b8f3a2c91d6e
Revises: 667c6bd6bf94
Create Date: 2026-11-28 12:00:00.000000

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b8f3a2c91d6e'
down_revision: str | Sequence[str] | None = '667c6bd6bf94'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # The hand-written bank is gone: its questions (the fallback and the pre-slice-2 sessions) are just "stored" now,
    # i.e. not written by the LLM. A database with no such rows makes this a no-op.
    op.execute("UPDATE interview_questions SET source = 'stored' WHERE source = 'bank'")
    # Every new row is LLM-written, so the default follows.
    op.alter_column('interview_questions', 'source', existing_type=sa.String(length=16), server_default='llm')
    op.drop_column('interview_questions', 'bank_id')


def downgrade() -> None:
    """Downgrade schema."""
    # The bank file is not restored, so the ids it held are lost: the column comes back empty (it is nullable).
    op.add_column('interview_questions', sa.Column('bank_id', sa.String(length=64), nullable=True))
    op.alter_column('interview_questions', 'source', existing_type=sa.String(length=16), server_default='bank')
    op.execute("UPDATE interview_questions SET source = 'bank' WHERE source = 'stored'")
