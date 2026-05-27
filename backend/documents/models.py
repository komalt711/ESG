from django.db import models
from companies.models import Company


class ESGDocument(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="documents")
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="esg_documents/")
    extracted_summary = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
