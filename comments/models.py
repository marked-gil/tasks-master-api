from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task
import uuid


class Comment(models.Model):
    """
    Model for the Comment table in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='commenting')
    content = models.TextField(max_length=150, blank=True, editable=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 blank=True, related_name='replied_to')
    is_reply_to_comment = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """ Arranges comments based on their update """
        ordering = ['-datetime_updated']

    def __str__(self):
        """
        Returns the task name of the Task's instance
        """
        comment = self.content
        return f"{comment}... by {self.owner}"
