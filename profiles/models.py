from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    """
    Model for user Profile's table in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    image = models.ImageField(
        upload_to='images/',
        default=''
    )
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Arranges the instances in descending order based on date and
        time created
        """
        ordering = ['-datetime_created']

    def __str__(self):
        """
        Returns the owner of the profile
        """
        return f"{self.owner}'s profile"