from django.db import models

from apps.space.models import List


class Task(models.Model):
    class Status(models.TextChoices):
        TO_DO = 'to_do', 'TO DO'
        IN_PROGRESS = 'in_progress', 'IN PROGRESS'
        COMPLETE = 'complete', 'COMPLETE'

    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.TO_DO)
    due_date = models.DateField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)