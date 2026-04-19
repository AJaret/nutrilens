from datetime import date
from decimal import Decimal

from pydantic import BaseModel

from app.schemas.meal import MealResponse


class DailyDashboardResponse(BaseModel):
    date: date
    consumed_calories: Decimal
    remaining_calories: Decimal
    consumed_protein: Decimal
    target_protein: Decimal
    consumed_carbs: Decimal
    target_carbs: Decimal
    consumed_fat: Decimal
    target_fat: Decimal
    meals: list[MealResponse]
