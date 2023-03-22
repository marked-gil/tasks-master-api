from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SharedTask
from tasks.models import Task


class TaskSlugRelatedSerializer(serializers.SlugRelatedField):
    """
    Custom serializer for task field
    [Idea taken from StackOverflow (See 'Credits' in README.md)]
    """
    def get_queryset(self):
        """ Retrieves Task querysets created by current user """
        queryset = Task.objects.all()
        request = self.context.get('request', None)
        tasks = SharedTask.objects.filter(
            shared_to=request.user.id).values('task_id')
        return queryset.filter(owner=request.user).distinct()


class SharedTaskSerializer(serializers.ModelSerializer):
    """ Serializer for SharedTask model """
    owner = serializers.ReadOnlyField(source='owner.username')
    task = TaskSlugRelatedSerializer(slug_field='task_name')
    task_id = serializers.SerializerMethodField()
    shared_to = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        queryset=User.objects.all()
    )
    datetime_created = serializers.DateTimeField(read_only=True)
    datetime_updated = serializers.DateTimeField(read_only=True)

    def get_task_id(self, obj):
        """
        Gets the id of the task
        """
        return obj.task.id

    class Meta:
        """ Specifies the fields returned by the API """
        model = SharedTask
        fields = [
            'id', 'owner', 'task', 'task_id', 'shared_to', 'datetime_created',
            'datetime_updated'
        ]
