from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.food import FoodResponse

router = APIRouter(prefix="/foods", tags=["foods"])


@router.get("", response_model=list[FoodResponse])
def list_foods() -> list[FoodResponse]:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Foods list endpoint pending implementation")


@router.get("/search", response_model=list[FoodResponse])
def search_foods(q: str = Query(..., min_length=1)) -> list[FoodResponse]:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Food search endpoint pending implementation")


@router.get("/{food_id}", response_model=FoodResponse)
def get_food(food_id: UUID) -> FoodResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Food detail endpoint pending implementation")
