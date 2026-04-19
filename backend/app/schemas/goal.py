from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class GoalResponse(BaseModel):
    id: UUID
    user_id: UUID
    maintenance_calories: Decimal
    target_calories: Decimal
    target_protein: Decimal
    target_carbs: Decimal
    target_fat: Decimal
    calculated_at: datetime

    model_config = {"from_attributes": True}
