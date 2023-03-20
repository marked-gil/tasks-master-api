from rest_framework import serializers
from .models import SharedTask


class SharedTaskSerializer(serializers.ModelSerializer):
    """ """
    owner = serializers.ReadOnlyField(source='owner.username')
    datetime_created = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )
    datetime_updated = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )

    class Meta:
        """ """
        model = SharedTask
        fields = [
            'id', 'owner', 'task', 'shared_to', 'datetime_created',
            'datetime_updated'
        ]
