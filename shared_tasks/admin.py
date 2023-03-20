from django.contrib import admin
from .models import SharedTask


@admin.register(SharedTask)
class SharedTaskAdmin(admin.ModelAdmin):
    """ Sets up the admin display for SharedTask model """
    list_display = ('id', 'task', 'datetime_created',
                    'datetime_updated')
    exclude = ('owner',)
    filter_horizontal = ['shared_to',]
