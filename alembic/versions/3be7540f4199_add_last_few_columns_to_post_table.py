"""add last few columns to post table

Revision ID: 3be7540f4199
Revises: 7a7f08156912
Create Date: 2023-05-26 07:48:07.263779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3be7540f4199'
down_revision = '7a7f08156912'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
