"""add the reference-note corpus (pgvector) and the notes each interview was given

Revision ID: 9b4e2d7c1a35
Revises: f5c2a9d84b17
Create Date: 2026-11-09 12:00:00.000000

Needs Postgres with the `vector` extension available (the pgvector/pgvector Docker image locally, see README); on a
server without it, this migration fails at the first statement and changes nothing.
"""
from collections.abc import Sequence

import sqlalchemy as sa
from pgvector.sqlalchemy import VECTOR

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '9b4e2d7c1a35'
down_revision: str | Sequence[str] | None = 'f5c2a9d84b17'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

# Fixed here on purpose: a model with another vector size needs a new migration and a re-ingest.
VECTOR_SIZE = 768


def upgrade() -> None:
    """Upgrade schema."""
    op.execute('CREATE EXTENSION IF NOT EXISTS vector')
    op.create_table(
        'knowledge_chunks',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('note_key', sa.String(length=255), nullable=False),
        sa.Column('competency', sa.String(length=128), nullable=False),
        sa.Column('source', sa.String(length=16), nullable=False),
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('content_hash', sa.String(length=64), nullable=False),
        sa.Column('embedding', VECTOR(VECTOR_SIZE), nullable=False),
        sa.Column('embedding_model', sa.String(length=128), nullable=False),
        sa.Column('active', sa.Boolean(), server_default=sa.text('true'), nullable=False),
        sa.Column('corpus_order', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    # One active row per note section; retired versions keep their key for the interviews that point at them.
    op.create_index(
        'uq_knowledge_chunks_active_note_key',
        'knowledge_chunks',
        ['note_key'],
        unique=True,
        postgresql_where=sa.text('active'),
    )
    op.create_table(
        'knowledge_chunk_scopes',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('chunk_id', sa.Uuid(), nullable=False),
        sa.Column('role', sa.String(length=32), nullable=False),
        sa.Column('level', sa.String(length=32), nullable=False),
        sa.ForeignKeyConstraint(['chunk_id'], ['knowledge_chunks.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('chunk_id', 'role', 'level'),
    )
    op.create_index('ix_knowledge_chunk_scopes_level_role', 'knowledge_chunk_scopes', ['level', 'role'])
    op.create_table(
        'interview_session_chunks',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('session_id', sa.Uuid(), nullable=False),
        sa.Column('chunk_id', sa.Uuid(), nullable=False),
        sa.Column('rank', sa.Integer(), nullable=False),
        sa.Column('score', sa.Float(), nullable=True),
        sa.Column('mode', sa.String(length=16), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        # Deleting an interview deletes its note references; no cascade from the chunk, so a referenced one stays.
        sa.ForeignKeyConstraint(['session_id'], ['interview_sessions.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['chunk_id'], ['knowledge_chunks.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('session_id', 'rank'),
    )
    op.create_index('ix_interview_session_chunks_chunk_id', 'interview_session_chunks', ['chunk_id'])


def downgrade() -> None:
    """Downgrade schema. The `vector` extension stays: other database objects may use it, and it holds no data."""
    op.drop_table('interview_session_chunks')
    op.drop_table('knowledge_chunk_scopes')
    op.drop_table('knowledge_chunks')
