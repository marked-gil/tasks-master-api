from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Specifies the fields returned by the API
        """
        model = Profile
        fields = [
            'id', 'owner', 'first_name', 'last_name', 'email', 'image',
            'datetime_created', 'datetime_updated'
        ]
