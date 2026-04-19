from fastapi import APIRouter, HTTPException, status

from app.schemas.profile import UserProfileResponse, UserProfileUpdate

router = APIRouter(prefix="/users/me/profile", tags=["profile"])


@router.get("", response_model=UserProfileResponse)
def get_profile() -> UserProfileResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Profile endpoint pending implementation")


@router.put("", response_model=UserProfileResponse)
def update_profile(payload: UserProfileUpdate) -> UserProfileResponse:
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Profile update endpoint pending implementation")
