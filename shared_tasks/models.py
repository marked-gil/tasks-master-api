from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task
import uuid


class SharedTask(models.Model):
    """
    Model for the SharedTask table in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task,
        related_name='task',
        on_delete=models.CASCADE
    )
    shared_to = models.ManyToManyField(User, related_name='sharing')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
