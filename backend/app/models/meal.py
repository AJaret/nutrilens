from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import MealType
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.meal_item import MealItem
    from app.models.user import User


class Meal(TimestampMixin, Base):
    __tablename__ = "meals"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    meal_type: Mapped[MealType] = mapped_column(Enum(MealType, name="meal_type_enum"), nullable=False)
    consumed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, index=True)
    notes: Mapped[str | None] = mapped_column(String(500), nullable=True)
    total_calories: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    total_protein: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    total_carbs: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    total_fat: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)

    user: Mapped[User] = relationship(back_populates="meals")
    items: Mapped[list[MealItem]] = relationship(back_populates="meal", cascade="all, delete-orphan")
