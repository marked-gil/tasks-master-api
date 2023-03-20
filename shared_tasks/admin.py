from django.contrib import admin
from .models import SharedTask


@admin.register(SharedTask)
class SharedTaskAdmin(admin.ModelAdmin):
    """ Sets up the admin display for SharedTask model """
    list_display = ('id', 'owner', 'task', 'datetime_created',
                    'datetime_updated')
    exclude = ('owner',)
    filter_horizontal = ['shared_to',]

    def save_model(self, request, obj, form, change):
        """ Automatically sets the current user as owner of the instance """
        obj.owner = request.user
        super().save_model(request, obj, form, change)
