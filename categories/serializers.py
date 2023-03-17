from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for Category Model """
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
        """ Specifies the fields returned by the API """
        model = Category
        fields = [
            'id', 'owner', 'category_name', 'description', 'datetime_created',
            'datetime_updated'
        ]
