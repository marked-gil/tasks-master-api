from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for Category Model """
    owner = serializers.ReadOnlyField(source='owner.username')
    datetime_created = serializers.DateTimeField(read_only=True)
    datetime_updated = serializers.DateTimeField(read_only=True)

    class Meta:
        """ Specifies the fields returned by the API """
        model = Category
        fields = [
            'id', 'owner', 'category_name', 'description', 'datetime_created',
            'datetime_updated'
        ]

    def validate(self, attrs):
        """ Validate that category and owner are unique together """
        message = "You already have this category."
        user = self.context["request"].user
        category = attrs['category_name']

        if Category.objects.filter(owner=user, category_name=category
                                   ).exists():
            raise serializers.ValidationError(message)
        return attrs
