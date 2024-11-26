"""adding follow table

Revision ID: 749153448e8a
Revises: eedc8b2bb781
Create Date: 2024-11-26 06:09:18.858337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '749153448e8a'
down_revision: Union[str, None] = 'eedc8b2bb781'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "follows",
        sa.Column("follower_id", sa.Integer(), nullable=False),
        sa.Column("followed_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("follower_id", "followed_id"),
        sa.ForeignKeyConstraint(
            ["follower_id"], ["users.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["followed_id"], ["users.id"], ondelete="CASCADE")
    )


def downgrade() -> None:
    op.drop_table("follows")
