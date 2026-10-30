"""add job description summary and running notes

Revision ID: c7d41e2a9b03
Revises: 51dfe1f2b1fd
Create Date: 2026-10-29 21:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7d41e2a9b03'
down_revision: Union[str, Sequence[str], None] = '51dfe1f2b1fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Both nullable: existing sessions have no summary and existing answers no note, and keep working as they are.
    op.add_column('interview_sessions', sa.Column('job_description_summary', sa.String(length=500), nullable=True))
    op.add_column('interview_messages', sa.Column('note', sa.String(length=200), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('interview_messages', 'note')
    op.drop_column('interview_sessions', 'job_description_summary')
