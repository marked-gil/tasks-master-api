from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Sets up the admin display for Comment model """
    list_display = ('id', 'owner', 'content', 'task', 'reply_to',
                    'datetime_updated', 'datetime_created',)
