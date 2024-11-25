from typing import TYPE_CHECKING

from datetime import datetime, timezone

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
    registration_date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
