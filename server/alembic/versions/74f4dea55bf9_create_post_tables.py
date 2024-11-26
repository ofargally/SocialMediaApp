"""Create post tables

Revision ID: 74f4dea55bf9
Revises: 
Create Date: 2024-11-21 11:36:01.688898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74f4dea55bf9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# Runs commands for making changes needed
def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("Title", sa.String(), nullable=False, ))

# Remove all changes specified in upgrade


def downgrade() -> None:
    op.drop_table("posts")
