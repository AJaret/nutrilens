from fastapi import APIRouter, HTTPException, status

from app.schemas.progress import WeightLogCreate, WeightLogResponse

router = APIRouter(prefix="/users/progress", tags=["progress"])


@router.post("/weight", response_model=WeightLogResponse, status_code=status.HTTP_201_CREATED)
def create_weight_log(payload: WeightLogCreate) -> WeightLogResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Weight log endpoint pending implementation")


@router.get("/weight-history", response_model=list[WeightLogResponse])
def get_weight_history() -> list[WeightLogResponse]:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Weight history endpoint pending implementation")
