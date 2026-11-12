"""add interview feedback: one row per interview with scores, text, usage and status

Revision ID: f5c2a9d84b17
Revises: a72345efd4c2
Create Date: 2026-11-05 12:00:00.000000

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'f5c2a9d84b17'
down_revision: str | Sequence[str] | None = 'a72345efd4c2'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'interview_feedback',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('session_id', sa.Uuid(), nullable=False),
        sa.Column('status', sa.String(length=16), nullable=False),
        sa.Column('enough_evidence', sa.Boolean(), nullable=True),
        sa.Column('rubric_version', sa.String(length=64), nullable=False),
        sa.Column('score_prompt_version', sa.String(length=64), nullable=True),
        sa.Column('write_prompt_version', sa.String(length=64), nullable=True),
        sa.Column('text_source', sa.String(length=16), nullable=True),
        sa.Column('overall', sa.Float(), nullable=True),
        sa.Column('result', sa.JSON(), nullable=True),
        sa.Column('score_model', sa.String(length=128), nullable=True),
        sa.Column('score_prompt_tokens', sa.Integer(), nullable=True),
        sa.Column('score_completion_tokens', sa.Integer(), nullable=True),
        sa.Column('score_latency_ms', sa.Integer(), nullable=True),
        sa.Column('write_model', sa.String(length=128), nullable=True),
        sa.Column('write_prompt_tokens', sa.Integer(), nullable=True),
        sa.Column('write_completion_tokens', sa.Integer(), nullable=True),
        sa.Column('write_latency_ms', sa.Integer(), nullable=True),
        sa.Column('failure_reason', sa.String(length=64), nullable=True),
        sa.Column('started_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('finished_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        # Deleting an interview deletes its feedback.
        sa.ForeignKeyConstraint(['session_id'], ['interview_sessions.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        # The guarantee behind "once per interview": two simultaneous first requests can't both insert.
        sa.UniqueConstraint('session_id', name='uq_interview_feedback_session_id'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('interview_feedback')
