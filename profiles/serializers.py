from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer for Profile Model """
    user_id = serializers.ReadOnlyField(source='owner.id')
    owner = serializers.ReadOnlyField(source='owner.username')
    datetime_created = serializers.DateTimeField(read_only=True)
    datetime_updated = serializers.DateTimeField(read_only=True)

    class Meta:
        """
        Specifies the fields returned by the API
        """
        model = Profile
        fields = [
            'id', 'user_id', 'owner', 'first_name', 'last_name', 'email',
            'image', 'datetime_created', 'datetime_updated'
        ]

    def validate_image(self, photo):
        """
        Validates the uploaded images to keep them within set parameter size
        [Code copied from CI's drf-api repository]
        """
        if photo.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image too large! Only 2 MB is allowed.'
            )
        if photo.image.width > 2000:
            raise serializers.ValidationError(
                'Image width & height should be less than 2000px'
            )
        if photo.image.height > 2000:
            raise serializers.ValidationError(
                'Image width & height should be less than 2000px'
            )
        return photo
