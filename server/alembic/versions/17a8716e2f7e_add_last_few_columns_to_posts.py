"""add last few columns to posts

Revision ID: 17a8716e2f7e
Revises: 9293b5cacc3e
Create Date: 2024-11-21 12:51:14.740895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17a8716e2f7e'
down_revision: Union[str, None] = '9293b5cacc3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(),
                  nullable=False, server_default="True"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                  nullable=False, server_default=sa.text('NOW()')))


def downgrade() -> None:
    op.drop_column('posts', "published")
    op.drop_column('posts', "created_at")
