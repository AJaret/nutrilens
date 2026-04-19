# Roadmap

## Scope Adjustments

The MVP stays focused on the mobile experience first. The web client starts smaller and can follow once the backend contract is stable.

- Backend first
- Flutter as primary client for Phase 1
- Web limited to login, dashboard, profile, and weight history

## Delivery Slices

### Slice 1: Auth

- register
- login
- refresh token
- current user endpoint
- authenticated Flutter session

### Slice 2: Profile and Goals

- profile creation/update
- calorie and macro calculation in backend
- persist calculated goals
- onboarding flow in mobile app

### Slice 3: Foods and Meals

- seed food catalog
- meal creation with items and nutrition snapshots
- meal list and detail endpoints
- daily meal view in mobile app

### Slice 4: Dashboard

- daily totals from meals
- remaining calories/macros
- summary endpoint for today and arbitrary date

### Slice 5: Progress

- weight logs
- basic weight history
- simple trend visualization in clients

## Decisions Locked In Early

- UUID primary keys
- timezone stored at profile level
- nutrition snapshots stored on `meal_items`
- maintenance calories persisted alongside target calories
- consistent backend-owned macro calculation rules

## Out of Scope for Phase 1

- image-based AI recognition
- barcode scanning
- offline sync
- push notifications
- admin roles
- advanced food-unit conversion engine
