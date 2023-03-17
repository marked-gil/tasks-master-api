from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Specifies the layout and content of admin display for Category model
    """
    list_display = ('id', 'owner', 'category_name', 'datetime_created',
                    'datetime_updated')
