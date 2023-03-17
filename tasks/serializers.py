from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """ Serializer for Task Model """
    owner = serializers.ReadOnlyField(source='owner.username')
    due_date = serializers.DateField(format="%d %B %Y")
    due_time = serializers.TimeField(format="%I:%M %p", required=False)
    progress = serializers.ReadOnlyField()
    datetime_created = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )
    datetime_updated = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )

    class Meta:
        """ Specifies the fields returned by the API """
        model = Task
        fields = [
            'id', 'owner', 'task_name', 'details', 'due_date', 'due_time',
            'progress', 'datetime_created', 'datetime_updated'
        ]
