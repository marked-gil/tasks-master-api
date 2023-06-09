from rest_framework import serializers
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.models import User
from datetime import date, datetime
from categories.models import Category
from .models import Task
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


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
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.SerializerMethodField()
    category = CategorySlugSerializer(slug_field='category_name')
    progress = serializers.ReadOnlyField()
    due_time = serializers.TimeField(format="%H:%M", allow_null=True)
    shared_to = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        queryset=User.objects.all()
    )
    datetime_created = serializers.DateTimeField(read_only=True)
    datetime_updated = serializers.DateTimeField(read_only=True)

    def get_is_owner(self, obj):
        """ Identifies if the current user is the owner of the task """
        user = self.context['request'].user
        return obj.owner == user

    def get_profile_image(self, obj):
        """ Retrieves the task owner's profile image URL """
        request = self.context.get('request')
        if obj.owner.profile.image:
            return request.build_absolute_uri(obj.owner.profile.image.url)
        return None

    class Meta:
        """ Specifies the fields returned by the API """
        model = Task
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'task_name', 'details', 'category', 'due_date', 'due_time',
            'priority', 'progress', 'is_completed', 'datetime_completed',
            'shared_to', 'is_shared', 'datetime_created', 'datetime_updated',
            'due_datetime'
        ]
