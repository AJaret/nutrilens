from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.meal import Meal
    from app.models.user_goal import UserGoal
    from app.models.user_profile import UserProfile
    from app.models.weight_log import WeightLog


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    profile: Mapped[UserProfile | None] = relationship(back_populates="user", uselist=False)
    goals: Mapped[list[UserGoal]] = relationship(back_populates="user", cascade="all, delete-orphan")
    meals: Mapped[list[Meal]] = relationship(back_populates="user", cascade="all, delete-orphan")
    weight_logs: Mapped[list[WeightLog]] = relationship(back_populates="user", cascade="all, delete-orphan")
