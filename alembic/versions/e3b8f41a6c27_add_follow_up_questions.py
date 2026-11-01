"""add follow-up questions: kind, parent, main number, decision prompt version

Revision ID: e3b8f41a6c27
Revises: c7d41e2a9b03
Create Date: 2026-10-31 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3b8f41a6c27'
down_revision: Union[str, Sequence[str], None] = 'c7d41e2a9b03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

FK_NAME = 'fk_interview_questions_parent_question_id'


def upgrade() -> None:
    """Upgrade schema."""
    # Every existing question is a main question: the server default fills them in.
    op.add_column('interview_questions', sa.Column('kind', sa.String(length=16), server_default='main', nullable=False))
    op.add_column('interview_questions', sa.Column('parent_question_id', sa.Uuid(), nullable=True))
    op.create_foreign_key(
        FK_NAME, 'interview_questions', 'interview_questions', ['parent_question_id'], ['id'], ondelete='CASCADE'
    )
    # Added nullable, backfilled (before follow-ups every position was a main question number), then required.
    op.add_column('interview_questions', sa.Column('main_number', sa.Integer(), nullable=True))
    op.execute('UPDATE interview_questions SET main_number = position')
    op.alter_column('interview_questions', 'main_number', existing_type=sa.Integer(), nullable=False)
    op.add_column('interview_questions', sa.Column('decision_prompt_version', sa.String(length=64), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    # Data is kept: a follow-up row then reads as an ordinary question (only sessions with follow-ups notice).
    op.drop_column('interview_questions', 'decision_prompt_version')
    op.drop_column('interview_questions', 'main_number')
    op.drop_constraint(FK_NAME, 'interview_questions', type_='foreignkey')
    op.drop_column('interview_questions', 'parent_question_id')
    op.drop_column('interview_questions', 'kind')
