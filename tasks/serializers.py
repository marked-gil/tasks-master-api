from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """ Serializer for Task Model """

    class Meta:
        """ Specifies the fields returned by the API """
        model = Task
        fields = [
            'id', 'owner', 'task_name', 'details', 'due_date', 'due_time',
            'progress', 'datetime_created', 'datetime_updated'
        ]
