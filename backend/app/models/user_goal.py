from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Numeric, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class UserGoal(Base):
    __tablename__ = "user_goals"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    maintenance_calories: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    target_calories: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    target_protein: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    target_carbs: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    target_fat: Mapped[Decimal] = mapped_column(Numeric(7, 2), nullable=False)
    calculated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user: Mapped[User] = relationship(back_populates="goals")
