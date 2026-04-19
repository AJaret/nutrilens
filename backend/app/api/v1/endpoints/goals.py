from fastapi import APIRouter, HTTPException, status

from app.schemas.goal import GoalResponse

router = APIRouter(prefix="/users/me/goals", tags=["goals"])


@router.get("", response_model=GoalResponse)
def get_current_goals() -> GoalResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Current goals endpoint pending implementation")


@router.post("/recalculate", response_model=GoalResponse, status_code=status.HTTP_201_CREATED)
def recalculate_goals() -> GoalResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Goal recalculation endpoint pending implementation")
