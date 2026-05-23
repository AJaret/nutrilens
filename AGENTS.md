# AGENTS.md

This file is the shared handoff context for any AI agent working in this repository.

## Project Summary

NutriLens is a calorie and nutrition tracking product for a portfolio project.

Phase 1 MVP scope:

- JWT authentication
- user profile
- calorie and macro goal calculation
- manual meal tracking
- basic food catalog
- daily dashboard
- weight and progress history

Primary stack for Phase 1:

- Mobile: Flutter
- Web: Next.js + TypeScript
- Backend: FastAPI + SQLAlchemy 2.x + Alembic + JWT
- Database: PostgreSQL
- Infra: Docker Compose

## Current Repository Structure

```txt
backend/
  alembic/
  app/
docs/
mobile/
web/
.env.example
docker-compose.yml
README.md
```

## Architecture Decisions Already Taken

- Start with backend first.
- Build Phase 1 in vertical slices, not by completing all backend work before clients.
- Prioritize Flutter over web in the MVP.
- Keep the web client smaller in Phase 1.
- Use UUID primary keys.
- Store `timezone` in `user_profiles`.
- Persist `maintenance_calories` in `user_goals`.
- Store nutrition snapshots on `meal_items` so historical data does not drift if foods change later.
- Keep nutrition target calculation centralized in the backend.
- Use a small seeded food catalog first.

## Delivery Order

Recommended implementation order:

1. Auth end-to-end
2. Profile and goals end-to-end
3. Foods and meals end-to-end
4. Dashboard end-to-end
5. Weight progress end-to-end

## Backend Status

Implemented scaffold only. Business flows are not implemented yet.

Already created:

- FastAPI app entrypoint in `backend/app/main.py`
- API v1 router in `backend/app/api/v1/router.py`
- endpoint modules:
  - `auth`
  - `profile`
  - `goals`
  - `foods`
  - `meals`
  - `dashboard`
  - `progress`
  - `health`
- configuration and security helpers:
  - `backend/app/core/config.py`
  - `backend/app/core/security.py`
- DB base/session:
  - `backend/app/db/base.py`
  - `backend/app/db/session.py`
- SQLAlchemy models for MVP resources
- Pydantic schemas for MVP resources
- goal calculation service in `backend/app/services/goal_service.py`
- Alembic config and initial migration
- Dockerfile for backend
- root `docker-compose.yml` for API + Postgres

Current endpoint behavior:

- `/` returns API status
- `/api/v1/health` returns health status
- all other endpoints currently return `501 Not Implemented`

## Database Models Present

- `users`
- `user_profiles`
- `user_goals`
- `foods`
- `meals`
- `meal_items`
- `weight_logs`

## Key Files To Read First

- `README.md`
- `docs/roadmap.md`
- `docker-compose.yml`
- `backend/app/main.py`
- `backend/app/api/v1/router.py`
- `backend/app/models/`
- `backend/app/schemas/`
- `backend/app/services/goal_service.py`
- `backend/alembic/versions/20260418_0001_initial_schema.py`

## Commands Useful For Continuing

From repo root:

- `docker compose up --build`
- `python -m compileall backend`

From `backend/`:

- `alembic upgrade head`
- `uvicorn app.main:app --reload`

## Known Gaps

- No real auth flow yet
- No DB dependencies wired into endpoints yet
- No repositories/services implemented beyond goal calculation rules
- No food seed script yet
- No tests yet
- No Flutter app scaffold yet
- No Next.js app scaffold yet

## Next Recommended Work

Implement the first functional slice: auth.

Target for the next agent:

1. Create DB-backed auth service and dependencies.
2. Implement `POST /auth/register`.
3. Implement `POST /auth/login`.
4. Implement `POST /auth/refresh`.
5. Implement `GET /auth/me`.
6. Add initial auth-related schemas if needed.
7. Verify API boots and auth routes work.

## Working Rules For Future Agents

- Do not expand scope beyond Phase 1 MVP unless the user asks.
- Prefer the smallest correct change.
- Keep backend logic centralized and consistent.
- Do not remove or overwrite user changes you did not make.
- If you make substantial progress, update the log below.
- Keep this file current after meaningful milestones.

## Progress Log

### 2026-04-18

- Reviewed repository state and confirmed it started effectively empty.
- Defined the initial monorepo layout with `backend/`, `mobile/`, `web/`, and `docs/`.
- Added root documentation in `README.md`.
- Added planning notes in `docs/roadmap.md`.
- Added `.env.example`.
- Added root `docker-compose.yml` for PostgreSQL and FastAPI.
- Added backend `Dockerfile` and `requirements.txt`.
- Added FastAPI application scaffold and versioned routing.
- Added placeholder endpoint modules for all MVP resources.
- Added SQLAlchemy models for the initial MVP schema.
- Added Pydantic schemas for auth, profile, goals, foods, meals, dashboard, and progress.
- Added JWT/password helpers in `backend/app/core/security.py`.
- Added nutrition goal calculation logic in `backend/app/services/goal_service.py`.
- Added Alembic config and an initial schema migration.
- Extended `.gitignore` to cover Next.js and Flutter artifacts.
- Verified backend Python syntax with `python -m compileall backend`.
- Added this `AGENTS.md` handoff file to keep shared project context and progress history current.

## How To Update This File

After each meaningful implementation step, append a short bullet to the current date in `Progress Log` or add a new date section.
