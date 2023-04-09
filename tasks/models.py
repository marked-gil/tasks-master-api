from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from categories.models import Category
import uuid


class Task(models.Model):
    """
    Model for the Task table in the database
    """
    PROGRESS = [
        ("overdue", "Overdue"),
        ("to-do", "To-do"),
        ("completed", "Completed")
    ]

    PRIORITY = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(
        max_length=250, blank=False, editable=True, unique_for_date="due_date"
    )
    details = models.TextField(max_length=1000, blank=True, editable=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 default=None)
    due_date = models.DateField(blank=False)
    due_time = models.TimeField(blank=True, null=True)
    progress = models.CharField(max_length=15, choices=PROGRESS)
    is_completed = models.BooleanField(default=False, blank=False,
                                       editable=True)
    datetime_completed = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY, default=1)
    shared_to = models.ManyToManyField(User, related_name='sharing')
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

    def __init__(self, *args, **kwargs):
        """ """
        super(Task, self).__init__(*args, **kwargs)
        self.old_is_completed = self.is_completed

    def save(self, *args, **kwargs):
        """
        Sets datetime value indatetime_completed set when is_completed is True
        (Idea taken from Edureka Community [See 'Credits' Section in ReadMe])
        """
        if self.is_completed and self.old_is_completed != self.is_completed:
            self.datetime_completed = datetime.now()
        if self.due_date >= date.today():
            self.progress = 'to-do'
        elif self.due_date < date.today():
            self.progress = 'overdue'
        super(Task, self).save(*args, **kwargs)
