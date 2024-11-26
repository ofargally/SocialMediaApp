"""update user model

Revision ID: b4a7e0d991e6
Revises: 749153448e8a
Create Date: 2024-11-26 23:48:30.596623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4a7e0d991e6'
down_revision: Union[str, None] = '749153448e8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("bio", sa.String(), nullable=True))
    op.add_column("users", sa.Column("user_name", sa.String(), nullable=True))
    op.add_column("users", sa.Column(
        "profile_picture", sa.String(), nullable=True))
    op.add_column("users", sa.Column("followers_count",
                  sa.Integer(), nullable=False, server_default="0"))
    op.add_column("users", sa.Column("followees_count",
                  sa.Integer(), nullable=False, server_default="0"))


def downgrade() -> None:
    op.drop_column("users", "bio")
    op.drop_column("users", "user_name")
    op.drop_column("users", "profile_picture")
    op.drop_column("users", "followers_count")
    op.drop_column("users", "followees_count")
