"""add interview sessions user index

Revision ID: a72345efd4c2
Revises: e3b8f41a6c27
Create Date: 2026-11-04 18:39:33.167367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a72345efd4c2'
down_revision: Union[str, Sequence[str], None] = 'e3b8f41a6c27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # The history list (one user's interviews, newest first). UUIDv7 ids are time-ordered, and a btree on
    # (user_id, id) serves ORDER BY id DESC by scanning backwards, so no DESC column is needed.
    op.create_index('ix_interview_sessions_user_id_id', 'interview_sessions', ['user_id', 'id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('ix_interview_sessions_user_id_id', table_name='interview_sessions')
