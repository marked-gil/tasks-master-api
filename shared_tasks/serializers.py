from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SharedTask
from tasks.models import Task


class SharedTaskSerializer(serializers.ModelSerializer):
    """ """
    owner = serializers.ReadOnlyField(source='owner.username')
    task = serializers.SlugRelatedField(
        slug_field='task_name',
        queryset=Task.objects.all()
    )
    task_id = serializers.SerializerMethodField()
    shared_to = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        queryset=User.objects.all()
    )
    datetime_created = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )
    datetime_updated = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )

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
