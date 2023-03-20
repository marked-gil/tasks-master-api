from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """ Sets up the admin display for Task model """
    list_display = ('id', 'owner', 'task_name', 'details',
                    'due_date', 'due_time', 'progress')
