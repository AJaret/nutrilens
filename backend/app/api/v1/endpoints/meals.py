from datetime import date
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.meal import MealCreate, MealResponse, MealUpdate

router = APIRouter(prefix="/users/meals", tags=["meals"])


@router.post("", response_model=MealResponse, status_code=status.HTTP_201_CREATED)
def create_meal(payload: MealCreate) -> MealResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Meal creation endpoint pending implementation")


@router.get("", response_model=list[MealResponse])
def list_meals(consumed_on: date | None = Query(default=None)) -> list[MealResponse]:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Meals list endpoint pending implementation")


@router.get("/{meal_id}", response_model=MealResponse)
def get_meal(meal_id: UUID) -> MealResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Meal detail endpoint pending implementation")


@router.put("/{meal_id}", response_model=MealResponse)
def update_meal(meal_id: UUID, payload: MealUpdate) -> MealResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Meal update endpoint pending implementation")


@router.delete("/{meal_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_meal(meal_id: UUID) -> None:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Meal delete endpoint pending implementation")
