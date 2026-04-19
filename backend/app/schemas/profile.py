from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from app.models.enums import ActivityLevel, DeficitLevel, GoalType, Sex


class UserProfileUpdate(BaseModel):
    age: int = Field(ge=13, le=120)
    sex: Sex
    height_cm: Decimal = Field(gt=0)
    weight_kg: Decimal = Field(gt=0)
    activity_level: ActivityLevel
    goal_type: GoalType
    deficit_level: DeficitLevel
    timezone: str = Field(default="UTC", min_length=1, max_length=64)


class UserProfileResponse(UserProfileUpdate):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
