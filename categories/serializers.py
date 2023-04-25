from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for Category Model """
    username = serializers.SerializerMethodField()
    datetime_created = serializers.DateTimeField(read_only=True)
    datetime_updated = serializers.DateTimeField(read_only=True)

    def get_username(self, obj):
        """ Gets the username of the owner """
        return obj.owner.username

    class Meta:
        """
        Specifies the fields returned by the API and validates posted and
        updated category
        """
        model = Category
        fields = [
            'id', 'owner', 'username', 'category_name', 'description',
            'datetime_created', 'datetime_updated'
        ]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('owner', 'category_name'),
                message=_("The same category already exists. Try a new one.")
            )
        ]
