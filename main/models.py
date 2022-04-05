import imp
from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=50),
    description = models.CharField(max_length=200),
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )