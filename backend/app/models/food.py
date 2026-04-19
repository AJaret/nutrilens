from __future__ import annotations

from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy import Numeric, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.mixins import TimestampMixin


class Food(TimestampMixin, Base):
    __tablename__ = "foods"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(160), nullable=False, index=True)
    brand: Mapped[str | None] = mapped_column(String(160), nullable=True)
    serving_size: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    serving_unit: Mapped[str] = mapped_column(String(32), nullable=False)
    calories: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    protein: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    carbs: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    fat: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
