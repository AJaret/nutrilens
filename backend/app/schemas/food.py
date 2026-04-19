from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class FoodResponse(BaseModel):
    id: UUID
    name: str
    brand: str | None
    serving_size: Decimal
    serving_unit: str
    calories: Decimal
    protein: Decimal
    carbs: Decimal
    fat: Decimal
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
