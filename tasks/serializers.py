from rest_framework import serializers
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.models import User
from datetime import date, datetime
from categories.models import Category
from .models import Task
from shared_tasks.models import SharedTask


class CategorySlugSerializer(serializers.SlugRelatedField):
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
    category = CategorySlugSerializer(slug_field='category_name')
    due_date = serializers.DateField(format="%d %B %Y")
    due_time = serializers.TimeField(format="%I:%M %p", required=False)
    progress = serializers.SerializerMethodField()
    is_shared = serializers.SerializerMethodField()
    shared_to = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        queryset=User.objects.all()
    )
    datetime_created = serializers.DateTimeField(read_only=True)
    datetime_updated = serializers.DateTimeField(read_only=True)

    def get_progress(self, obj):
        """ Sets the value of progress field """
        if obj.due_time is None:
            time_ok = True
        else:
            time_ok = datetime.now().time() < obj.due_time

        if obj.due_date < date.today() or obj.due_date == date.today() \
                and not time_ok:
            obj.progress = 'overdue'
        return obj.progress

    def get_is_shared(self, obj):
        """ Shows if the task is shared or not """
        return obj.shared_to.exists()

    class Meta:
        """ Specifies the fields returned by the API """
        model = Task
        fields = [
            'id', 'owner', 'profile_id', 'task_name', 'details', 'category',
            'due_date', 'due_time', 'priority', 'progress', 'shared_to',
            'is_shared', 'datetime_created', 'datetime_updated'
        ]
