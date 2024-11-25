"""change user model

Revision ID: fad50d3f31ef
Revises: d0ee42901742
Create Date: 2024-11-25 22:21:44.260050

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fad50d3f31ef"
down_revision: Union[str, None] = "d0ee42901742"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users", sa.Column("registration_date", sa.DateTime(), nullable=False)
    )
    op.drop_constraint("uq_users_username", "users", type_="unique")
    op.drop_column("users", "username")


def downgrade() -> None:
    op.add_column(
        "users",
        sa.Column("username", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.create_unique_constraint("uq_users_username", "users", ["username"])
    op.drop_column("users", "registration_date")
