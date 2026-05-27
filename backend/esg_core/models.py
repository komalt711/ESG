from django.db import models
from companies.models import Company


class ESGScoreSnapshot(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="score_snapshots")
    environmental = models.FloatField()
    social = models.FloatField()
    governance = models.FloatField()
    composite = models.FloatField()
    source = models.CharField(max_length=120, default="internal")
    captured_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.ticker} - {self.composite}"
