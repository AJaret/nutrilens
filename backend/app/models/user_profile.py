from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Enum, ForeignKey, Integer, Numeric, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import ActivityLevel, DeficitLevel, GoalType, Sex
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.user import User


class UserProfile(TimestampMixin, Base):
    __tablename__ = "user_profiles"
    __table_args__ = (UniqueConstraint("user_id"),)

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    sex: Mapped[Sex] = mapped_column(Enum(Sex, name="sex_enum"), nullable=False)
    height_cm: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    weight_kg: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False)
    activity_level: Mapped[ActivityLevel] = mapped_column(Enum(ActivityLevel, name="activity_level_enum"), nullable=False)
    goal_type: Mapped[GoalType] = mapped_column(Enum(GoalType, name="goal_type_enum"), nullable=False)
    deficit_level: Mapped[DeficitLevel] = mapped_column(Enum(DeficitLevel, name="deficit_level_enum"), nullable=False)
    timezone: Mapped[str] = mapped_column(String(64), default="UTC", nullable=False)

    user: Mapped[User] = relationship(back_populates="profile")
