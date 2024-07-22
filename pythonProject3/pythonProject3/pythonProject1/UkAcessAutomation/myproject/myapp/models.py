# models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file_name
