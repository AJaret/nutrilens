# NutriLens

NutriLens is a calorie and nutrition tracking platform with a FastAPI backend, a Flutter mobile app, and a lightweight Next.js web client.

## MVP Focus

Phase 1 is intentionally centered on a usable product, not an oversized first release.

- JWT authentication
- User profile and calorie goal calculation
- Seeded food catalog
- Manual meal tracking
- Daily dashboard
- Weight and progress history

## Recommended Delivery Order

Build the MVP in vertical slices instead of finishing an entire layer first.

1. Authentication end-to-end
2. Profile and goal calculation end-to-end
3. Foods and meals end-to-end
4. Daily dashboard end-to-end
5. Weight progress end-to-end

## Repository Structure

```txt
backend/
  app/
  alembic/
  Dockerfile
  requirements.txt
docs/
mobile/
web/
docker-compose.yml
```

## Quick Start

1. Copy `.env.example` to `.env`.
2. Start the infrastructure with `docker compose up --build`.
3. Open `http://localhost:8000/docs` for the API docs.

## Initial Backend Scope

The backend scaffold already includes:

- FastAPI application wiring
- versioned API router
- SQLAlchemy 2.x base models
- Alembic configuration
- JWT/password utility helpers
- nutrition target calculation service
- module layout for the MVP resources

Detailed planning notes live in `docs/roadmap.md`.
