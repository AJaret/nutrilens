from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from app.models.enums import MealType


class MealItemBase(BaseModel):
    food_id: UUID | None = None
    custom_food_name: str | None = Field(default=None, max_length=160)
    quantity: Decimal = Field(gt=0)
    unit: str = Field(min_length=1, max_length=32)
    calories: Decimal = Field(ge=0)
    protein: Decimal = Field(ge=0)
    carbs: Decimal = Field(ge=0)
    fat: Decimal = Field(ge=0)


class MealItemCreate(MealItemBase):
    pass


class MealItemResponse(MealItemBase):
    id: UUID

    model_config = {"from_attributes": True}


class MealCreate(BaseModel):
    meal_type: MealType
    consumed_at: datetime
    notes: str | None = Field(default=None, max_length=500)
    items: list[MealItemCreate]


class MealUpdate(MealCreate):
    pass


class MealResponse(BaseModel):
    id: UUID
    user_id: UUID
    meal_type: MealType
    consumed_at: datetime
    notes: str | None
    total_calories: Decimal
    total_protein: Decimal
    total_carbs: Decimal
    total_fat: Decimal
    created_at: datetime
    updated_at: datetime
    items: list[MealItemResponse]

    model_config = {"from_attributes": True}
