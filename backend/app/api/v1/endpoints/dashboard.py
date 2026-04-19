from datetime import date

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.dashboard import DailyDashboardResponse

router = APIRouter(prefix="/users/dashboard", tags=["dashboard"])


@router.get("/today", response_model=DailyDashboardResponse)
def get_today_dashboard() -> DailyDashboardResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Today dashboard endpoint pending implementation")


@router.get("/daily", response_model=DailyDashboardResponse)
def get_daily_dashboard(target_date: date = Query(..., alias="date")) -> DailyDashboardResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Daily dashboard endpoint pending implementation")
