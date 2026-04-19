from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.project_name,
    version="0.1.0",
    openapi_url=f"{settings.api_v1_prefix}/openapi.json",
)

app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    return {
        "name": settings.project_name,
        "status": "ok",
        "docs": "/docs",
    }
