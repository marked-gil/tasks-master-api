from rest_framework import serializers
from categories.models import Category
from .models import Task


class CategorySlugRelatedSerializer(serializers.SlugRelatedField):
    """
    Custom serializer for category field
    [Idea taken from StackOverflow (See 'Credits' in README.md)]
    """
    def get_queryset(self):
        """ Retrieves Category querysets created by current user """
        queryset = Category.objects.all()
        request = self.context.get('request', None)
        return queryset.filter(owner=request.user)


class TaskSerializer(serializers.ModelSerializer):
    """ Serializer for Task Model """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    category = CategorySlugRelatedSerializer(slug_field='category_name')
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
            'id', 'owner', 'profile_id', 'task_name', 'details', 'category',
            'due_date', 'due_time', 'priority', 'progress', 'datetime_created',
            'datetime_updated'
        ]
