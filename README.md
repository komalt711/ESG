# AI-powered ESG Compliance Platform

Enterprise-style ESG dashboard (React + Chart.js) with Django API scaffold for compliance, risk intelligence, document workflows, and sentiment insights.

## Tech Stack
- Frontend: React, Vite, Chart.js
- Backend: Django, Django REST Framework
- Data: SQLite (core scaffold) + MongoDB Atlas integration via PyMongo

## Frontend Setup
```bash
npm install
npm run dev
```

## Backend Setup
```bash
cd backend
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
copy .env.example .env
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py runserver
```

## API Modules
- `api/auth/` - register/login/profile
- `api/core/` - dashboard summary and ESG trend
- `api/companies/` - entity list and score comparison
- `api/risk/` - AI recommendation feed
- `api/documents/` - upload and parsed docs
- `api/sentiment/` - news sentiment feed

## Architecture Details
See `backend/ARCHITECTURE.md` for full architecture, schema, deployment design, and development roadmap.
