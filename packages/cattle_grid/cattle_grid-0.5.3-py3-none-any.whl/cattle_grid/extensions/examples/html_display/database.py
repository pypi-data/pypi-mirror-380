import datetime

from sqlalchemy import ForeignKey, String, func, JSON
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from sqlalchemy_utils.types import UUIDType


class Base(AsyncAttrs, DeclarativeBase):
    """Base model"""

    pass


class PublishingActor(Base):
    __tablename__ = "html_display_publishing_actor"

    id: Mapped[int] = mapped_column(primary_key=True)

    actor: Mapped[str] = mapped_column(String(256))
    name: Mapped[str] = mapped_column(String(256), unique=True)


class PublishedObject(Base):
    """HTML display object in the database"""

    __tablename__ = "html_display_stored_object"

    id: Mapped[bytes] = mapped_column(UUIDType(binary=True), primary_key=True)
    data: Mapped[dict] = mapped_column(JSON)
    actor: Mapped[str] = mapped_column()
    create_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class ExportPermission(Base):
    """Records a one time token required to download the export"""

    __tablename__ = "html_display_export_permission"

    id: Mapped[int] = mapped_column(primary_key=True)
    publishing_actor_id: Mapped[str] = mapped_column(
        ForeignKey("html_display_publishing_actor.id")
    )
    publishing_actor: Mapped[PublishingActor] = relationship()
    one_time_token: Mapped[bytes] = mapped_column(UUIDType(binary=True))
