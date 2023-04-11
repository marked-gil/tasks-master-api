from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    """
    Model for the Category table in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50, blank=False, editable=True)
    description = models.TextField(max_length=100, blank=True, editable=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Sets the ordering and uniqueness of the Category instance
        in the database
        """
        ordering = ['-datetime_updated']

    def __str__(self):
        """
        Returns the name of the Category's instance
        """
        return self.category_name
