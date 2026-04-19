from fastapi import APIRouter

from app.api.v1.endpoints import auth, dashboard, foods, goals, health, meals, profile, progress

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(profile.router)
api_router.include_router(goals.router)
api_router.include_router(foods.router)
api_router.include_router(meals.router)
api_router.include_router(dashboard.router)
api_router.include_router(progress.router)
