"""add interview use_profile: opt-in to the candidate profile per interview (resume-aware-interview)

Revision ID: 667c6bd6bf94
Revises: 3d8e5a1c7f42
Create Date: 2026-11-14 16:50:52.713473

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '667c6bd6bf94'
down_revision: str | Sequence[str] | None = '3d8e5a1c7f42'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # NOT NULL is safe on existing rows: Postgres stores the constant default in the catalog (no table rewrite),
    # and every interview from before this column reads false (EC11).
    op.add_column(
        'interview_sessions',
        sa.Column('use_profile', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('interview_sessions', 'use_profile')
