from rest_framework import serializers
from django.db.models.base import ObjectDoesNotExist
from categories.models import Category
from .models import Task
from shared_tasks.models import SharedTask


class CategorySlugRelatedSerializer(serializers.SlugRelatedField):
    """
    Custom serializer for category field
    [Idea taken from StackOverflow (See 'Credits' in README.md)]
    """
    def get_queryset(self):
        """ Retrieves Category querysets created by current user """
        queryset = Category.objects.all()
        request = self.context.get('request', None)
        return queryset.filter(owner=request.user)


class TaskSerializer(serializers.ModelSerializer):
    """ Serializer for Task Model """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    category = CategorySlugRelatedSerializer(slug_field='category_name')
    due_date = serializers.DateField(format="%d %B %Y")
    due_time = serializers.TimeField(format="%I:%M %p", required=False)
    progress = serializers.ReadOnlyField()
    is_shared = serializers.SerializerMethodField()
    shared_task_id = serializers.SerializerMethodField()
    datetime_created = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )
    datetime_updated = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )

    def get_is_shared(self, obj):
        """ Shows if the task is shared or not"""
        task_id = obj.id
        shared_task = SharedTask.objects.filter(task=obj)
        return bool(shared_task)

    def get_shared_task_id(self, obj):
        """
        Gets the id of the shared task from SharedTask model
        """
        try:
            shared_task = SharedTask.objects.get(task=obj)
            shared_task_id = shared_task.id
        except SharedTask.DoesNotExist:
            return None
        else:
            return shared_task_id

    class Meta:
        """ Specifies the fields returned by the API """
        model = Task
        fields = [
            'id', 'owner', 'profile_id', 'task_name', 'details', 'category',
            'due_date', 'due_time', 'priority', 'progress', 'is_shared',
            'shared_task_id', 'datetime_created', 'datetime_updated'
        ]
