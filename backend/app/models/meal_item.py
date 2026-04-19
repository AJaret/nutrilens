from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.meal import Meal


class MealItem(Base):
    __tablename__ = "meal_items"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    meal_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("meals.id", ondelete="CASCADE"), nullable=False, index=True)
    food_id: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True), ForeignKey("foods.id", ondelete="SET NULL"), nullable=True)
    custom_food_name: Mapped[str | None] = mapped_column(String(160), nullable=True)
    quantity: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    unit: Mapped[str] = mapped_column(String(32), nullable=False)
    calories: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    protein: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    carbs: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    fat: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)

    meal: Mapped[Meal] = relationship(back_populates="items")
