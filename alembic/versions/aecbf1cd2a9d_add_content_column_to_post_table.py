"""add content column to post table

Revision ID: aecbf1cd2a9d
Revises: c1547936c2f8
Create Date: 2023-05-26 07:37:26.159947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aecbf1cd2a9d'
down_revision = 'c1547936c2f8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
