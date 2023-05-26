"""add size field

Revision ID: 4236c8a25ce9
Revises: b50c5c2fcdc6
Create Date: 2023-05-15 17:05:54.604172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4236c8a25ce9'
down_revision = 'b50c5c2fcdc6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('size', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'size')
    # ### end Alembic commands ###
