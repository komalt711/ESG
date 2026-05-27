from django.db import models
from companies.models import Company


class NewsSentiment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="sentiment_items")
    headline = models.CharField(max_length=300)
    source = models.CharField(max_length=120)
    sentiment_score = models.FloatField()
    sentiment_label = models.CharField(max_length=20)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.ticker} - {self.sentiment_label}"
