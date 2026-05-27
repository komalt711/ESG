# AI-powered ESG Compliance & Risk Intelligence Platform

## 1) Project Architecture
- **Frontend:** React + Vite + Chart.js (dark enterprise dashboard)
- **Backend:** Django + Django REST Framework
- **Database:** Django relational store for auth/admin + MongoDB Atlas via PyMongo for ESG analytics
- **Document Pipeline:** ESG PDF upload endpoint -> parser/OCR worker (next phase)
- **AI Layer:** risk recommendation service and sentiment classification service (next phase)

## 2) Folder Structure
```text
backend/
  config/                  # Django project config and root routing
  accounts/                # authentication and user profile APIs
  esg_core/                # ESG KPI/score dashboard APIs
  companies/               # company profile and comparative analytics APIs
  risk_engine/             # AI recommendation APIs
  documents/               # ESG document upload and parsing APIs
  sentiment/               # news and sentiment APIs
  manage.py
  requirements.txt
  .env.example
```

## 3) Database Schema (Core Collections)
- **companies_company**
  - `name`, `sector`, `region`, `ticker`, `esg_score`, `risk_level`, timestamps
- **esg_core_esgscoresnapshot**
  - `company_id`, `environmental`, `social`, `governance`, `composite`, `source`, `captured_at`
- **risk_engine_riskrecommendation**
  - `company_id`, `title`, `description`, `priority`, `model_version`, `created_at`
- **documents_esgdocument**
  - `company_id`, `title`, `file`, `extracted_summary`, `uploaded_at`
- **sentiment_newssentiment**
  - `company_id`, `headline`, `source`, `sentiment_score`, `sentiment_label`, `published_at`
- **accounts_userprofile**
  - `user_id`, `role`, `department`, `created_at`

> In this scaffold, Django models run on the default relational DB for stability. ESG analytics and ingestion can be persisted in MongoDB collections accessed through `esg_core/mongo.py`.

## 4) API Structure
- `GET /api/core/dashboard-summary/`
- `GET /api/core/score-trend/`
- `GET /api/companies/`
- `GET /api/companies/comparison/`
- `GET /api/risk/recommendations/`
- `POST /api/documents/upload/`
- `GET /api/documents/parsed/`
- `GET /api/sentiment/news-feed/`
- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `GET /api/auth/profile/`

## 5) Recommended Django Apps
- `accounts`: auth, role-based access, profile and audit ownership
- `esg_core`: scoring logic, KPI snapshots, trend calculations
- `companies`: issuer entities, sectors, watchlists
- `risk_engine`: AI recommendations and model outcomes
- `documents`: uploads, extraction metadata, parser state
- `sentiment`: news ingestion, sentiment labeling, event signals

## 6) Deployment Architecture
- **Frontend:** Vercel / Netlify (React static app)
- **Backend API:** Render / Railway / Azure App Service (Django Gunicorn)
- **DB:** MongoDB Atlas (managed cluster)
- **Storage:** S3-compatible bucket for PDF docs
- **Queue/Workers (next):** Celery + Redis for PDF parsing and scheduled sentiment ingestion
- **Monitoring:** Sentry + structured logs + uptime checks

## 7) Step-by-Step Development Plan
1. Finalize auth flow (JWT or session) and role-based permissions.
2. Implement CRUD for companies and ESG score snapshots.
3. Connect frontend cards/charts to backend APIs.
4. Add PDF upload storage + extraction worker.
5. Add external news ingestion and sentiment scoring pipeline.
6. Implement risk recommendation model service API contract.
7. Add tests (unit + API integration), rate limiting, and audit logs.
8. Deploy staging environment with MongoDB Atlas + CI/CD.
9. Harden for demo: seed data, observability, and performance checks.
