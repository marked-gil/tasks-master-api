from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
import uuid


class Task(models.Model):
    """
    Model for the Task table in the database
    """
    PROGRESS = [
        ("overdue", "Overdue"),
        ("todo", "Todo")
    ]

    PRIORITY = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(
        max_length=250, blank=False, editable=True, unique_for_date="due_date"
    )
    details = models.TextField(max_length=1000, blank=True, editable=True)
    # Category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                #  default=DEFAULT_CATEGORY)
    due_date = models.DateField(blank=False)
    due_time = models.TimeField(blank=True, null=True)
    progress = models.CharField(max_length=15, choices=PROGRESS,
                                default="todo")
    priority = models.CharField(max_length=10, choices=PRIORITY, default="low")
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Arranges the Task's instances based on their due dates
        """
        ordering = ['due_date']

    def __str__(self):
        """
        Returns the task name of the Task's instance
        """
        return self.task_name
