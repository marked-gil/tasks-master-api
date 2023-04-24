from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth.models import User
from tasks.models import Task
from .models import Comment


class TaskSlugRelatedSerializer(serializers.SlugRelatedField):
    """
    Custom serializer to filter tasks owned or shared with the user
    [Idea taken from StackOverflow (See 'Credits' in README.md)]
    """
    def get_queryset(self):
        """ Retrieves filtered Task querysets """
        queryset = Task.objects.all()
        request = self.context.get('request', None)
        return queryset.filter(
            Q(owner=request.user) | Q(shared_to__id=request.user.id)
        ).distinct()


class ReplyToSlugRelatedSerializer(serializers.SlugRelatedField):
    """
    Custom serializer to filter comments with tasks shared with, or
    owned by, the user.
    [Idea taken from StackOverflow (See 'Credits' in README.md)]
    """
    def get_queryset(self):
        """ Retrieves Comment filtered querysets """
        queryset = Comment.objects.all()
        request = self.context.get('request', None)
        task_ids = Task.objects.filter(
            Q(shared_to__id=request.user.id) |
            Q(owner__id=request.user.id)).values('id')
        return queryset.filter(task__id__in=task_ids).distinct()


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for Comment model """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    task = TaskSlugRelatedSerializer(slug_field='task_name')
    task_id = serializers.ReadOnlyField(source='task.id')
    content = serializers.CharField(
        max_length=250,
        allow_blank=False,
        style={'base_template': 'textarea.html'}
    )
    reply_to = ReplyToSlugRelatedSerializer(
        slug_field='content',
        allow_null=True
    )
    reply_to_id = serializers.ReadOnlyField(
        source='reply_to.id',
        allow_null=True
    )
    is_reply_to_comment = serializers.SerializerMethodField()
    datetime_created = serializers.DateTimeField(read_only=True)
    datetime_updated = serializers.DateTimeField(read_only=True)

    def get_is_owner(self, obj):
        """ Identifies if current user is the owner of the comment """
        user = self.context['request'].user
        return obj.owner == user

    def get_is_reply_to_comment(self, obj):
        """ Boolean value for a comment replied to another comment """
        return bool(obj.reply_to)

    class Meta:
        """ Specifies the fields returned by the API """
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'task', 'task_id', 'content',
            'reply_to', 'reply_to_id', 'is_reply_to_comment',
            'datetime_created', 'datetime_updated'
        ]
