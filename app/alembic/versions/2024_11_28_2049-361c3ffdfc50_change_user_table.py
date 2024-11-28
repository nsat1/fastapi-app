"""change user table

Revision ID: 361c3ffdfc50
Revises: fad50d3f31ef
Create Date: 2024-11-28 20:49:00.196330

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "361c3ffdfc50"
down_revision: Union[str, None] = "fad50d3f31ef"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("users", "registration_date")


def downgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "registration_date",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=False,
        ),
    )
