from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from categories.models import Category
import uuid


class Profile(models.Model):
    """
    Model for user Profile's table in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(
        max_length=150, unique=True, blank=True, null=True
    )
    image = models.ImageField(
        upload_to='images/',
        default='../profile-avatar_omfvlb'
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

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        """
        Automatically creates a profile for registered users
        (Idea to use @receiver decorator taken from Stackoverflow.
        See Credits in README.md)
        """
        DEFAULT_CATEGORIES = ["at home", "at work"]

        if created:
            Profile.objects.create(owner=instance)
            for cat_name in DEFAULT_CATEGORIES:
                Category.objects.create(owner=instance, category_name=cat_name)
