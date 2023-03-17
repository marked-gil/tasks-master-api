from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'first_name', 'last_name', 'email', 'image',
            'datetime_created', 'datetime_updated'
        ]
