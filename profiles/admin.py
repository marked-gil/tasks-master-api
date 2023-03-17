from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Specifies the layout and content of admin display for Profile model
    """
    list_display = ('id', 'owner', 'first_name', 'last_name', 'email',
                    'datetime_created', 'datetime_updated')
