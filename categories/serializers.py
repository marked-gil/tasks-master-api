from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for Category Model """

    class Meta:
        """ Specifies the fields returned by the API """
        model = Category
        fields = [
            'id', 'owner', 'category_name', 'description', 'datetime_created',
            'datetime_updated'
        ]
