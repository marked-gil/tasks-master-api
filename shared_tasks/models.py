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
        related_name='shared_tasks',
        on_delete=models.CASCADE
    )
    shared_to = models.ManyToManyField(User, related_name='shared')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """ Sets the order and uniqueness of instances """
        ordering = ['-datetime_updated']
        unique_together = ['owner', 'task']

    def __str__(self):
        """ Returns the shared task's name """
        return f"Shared: {self.task}"
