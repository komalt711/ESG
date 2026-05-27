from django.urls import path
from .views import dashboard_summary, score_trend

urlpatterns = [
    path("dashboard-summary/", dashboard_summary, name="dashboard-summary"),
    path("score-trend/", score_trend, name="score-trend"),
]
