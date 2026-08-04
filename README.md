# TradePilotX AI Backend

A production-oriented FastAPI backend with PostgreSQL, SQLAlchemy, Alembic, JWT authentication, role-based authorization, Docker, and tests.

## Quick start

```bash
cp backend/.env.example backend/.env
docker compose up --build
```

Open Swagger UI at http://localhost:8000/docs.

## Authentication endpoints

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`
- `POST /api/v1/auth/forgot-password`
- `POST /api/v1/auth/reset-password`
- `POST /api/v1/auth/verify-email`
- `GET /api/v1/auth/me`
- `GET /api/v1/auth/admin/users` (Admin role)

Email delivery is exposed through a provider integration seam in `app/services/email.py`; configure your transactional provider there before production deployment.
