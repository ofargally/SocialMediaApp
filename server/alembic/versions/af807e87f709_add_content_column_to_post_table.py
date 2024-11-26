"""add content column to post table

Revision ID: af807e87f709
Revises: 74f4dea55bf9
Create Date: 2024-11-21 12:15:58.880486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af807e87f709'
down_revision: Union[str, None] = '74f4dea55bf9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
