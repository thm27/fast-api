"""add user table

Revision ID: 00568be604f0
Revises: aecbf1cd2a9d
Create Date: 2023-05-26 07:41:36.872050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00568be604f0'
down_revision = 'aecbf1cd2a9d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
