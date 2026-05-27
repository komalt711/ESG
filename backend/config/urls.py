from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/core/", include("esg_core.urls")),
    path("api/companies/", include("companies.urls")),
    path("api/risk/", include("risk_engine.urls")),
    path("api/documents/", include("documents.urls")),
    path("api/sentiment/", include("sentiment.urls")),
]
