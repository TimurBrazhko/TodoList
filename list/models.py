import uuid

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True)

    def __str__(self):
        return self.title