from django.db import models


class UserProfile(models.Model):
    user_id = models.CharField(max_length=120, unique=True)
    role = models.CharField(max_length=50, default="analyst")
    department = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id
