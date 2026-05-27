from django.db import models
from companies.models import Company


class RiskRecommendation(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="risk_recommendations")
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="medium")
    model_version = models.CharField(max_length=80, default="v1")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.ticker} - {self.title}"
