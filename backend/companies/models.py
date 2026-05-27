from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    ticker = models.CharField(max_length=30, unique=True)
    esg_score = models.FloatField(default=0)
    risk_level = models.CharField(max_length=40, default="moderate")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.ticker})"
