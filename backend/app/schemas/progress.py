from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field


class WeightLogCreate(BaseModel):
    weight_kg: Decimal = Field(gt=0)
    logged_at: datetime
    note: str | None = Field(default=None, max_length=255)


class WeightLogResponse(BaseModel):
    id: UUID
    user_id: UUID
    weight_kg: Decimal
    logged_at: datetime
    note: str | None

    model_config = {"from_attributes": True}
