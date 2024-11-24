from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import MetaData

from core.config import settings

class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
