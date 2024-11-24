"""create access tokens

Revision ID: d0ee42901742
Revises: f1384b883e9e
Create Date: 2024-11-24 19:49:15.065435

"""

from typing import Sequence, Union
import fastapi_users_db_sqlalchemy

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d0ee42901742"
down_revision: Union[str, None] = "f1384b883e9e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "accesstokens",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(length=43), nullable=False),
        sa.Column(
            "created_at",
            fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_accesstokens_user_id_users"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("token", name=op.f("pk_accesstokens")),
    )
    op.create_index(
        op.f("ix_accesstokens_created_at"),
        "accesstokens",
        ["created_at"],
        unique=False,
    )
    op.add_column(
        "users", sa.Column("email", sa.String(length=320), nullable=False)
    )
    op.add_column(
        "users",
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
    )
    op.add_column(
        "users", sa.Column("is_active", sa.Boolean(), nullable=False)
    )
    op.add_column(
        "users", sa.Column("is_superuser", sa.Boolean(), nullable=False)
    )
    op.add_column(
        "users", sa.Column("is_verified", sa.Boolean(), nullable=False)
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)



def downgrade() -> None:
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_column("users", "is_verified")
    op.drop_column("users", "is_superuser")
    op.drop_column("users", "is_active")
    op.drop_column("users", "hashed_password")
    op.drop_column("users", "email")
    op.drop_index(
        op.f("ix_accesstokens_created_at"), table_name="accesstokens"
    )
    op.drop_table("accesstokens")
