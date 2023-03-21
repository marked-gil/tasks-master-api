from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth.models import User
from shared_tasks.models import SharedTask
from tasks.models import Task
from .models import Comment


class TaskSlugRelatedSerializer(serializers.SlugRelatedField):
    """
    Custom serializer for task field
    [Idea taken from StackOverflow (See 'Credits' in README.md)]
    """
    def get_queryset(self):
        """ Retrieves filtered Task querysets """
        queryset = Task.objects.all()
        request = self.context.get('request', None)
        tasks = SharedTask.objects.filter(
            shared_to=request.user.id).values('task_id')
        return queryset.filter(
            Q(owner=request.user) | Q(id__in=tasks)
        ).distinct()


class ReplyToSlugRelatedSerializer(serializers.SlugRelatedField):
    """
    Custom serializer for reply_to field
    [Idea taken from StackOverflow (See 'Credits' in README.md)]
    """
    def get_queryset(self):
        """ Retrieves Comment filtered querysets """
        queryset = Comment.objects.all()
        request = self.context.get('request', None)
        tasks = SharedTask.objects.filter(
            shared_to=request.user.id).values('task_id')
        return queryset.filter(
            Q(owner=request.user) | Q(task__id__in=tasks)
        ).distinct()


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for Comment model """
    owner = serializers.ReadOnlyField(source='owner.username')
    task = TaskSlugRelatedSerializer(slug_field='task_name')
    task_id = serializers.ReadOnlyField(source='task.id')
    reply_to = ReplyToSlugRelatedSerializer(
        slug_field='content',
        allow_null=True
    )
    reply_to_id = serializers.ReadOnlyField(
        source='reply_to.id',
        allow_null=True
    )
    is_reply_to_comment = serializers.SerializerMethodField()
    datetime_created = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )
    datetime_updated = serializers.DateTimeField(
        format="%b %d, %Y | %H:%M",
        read_only=True
    )

    def get_is_reply_to_comment(self, obj):
        """ Boolean value for a comment replied to another comment """
        return bool(obj.reply_to)

    class Meta:
        """ Specifies the fields returned by the API """
        model = Comment
        fields = [
            'id', 'owner', 'task', 'task_id', 'content', 'reply_to',
            'reply_to_id', 'is_reply_to_comment', 'datetime_created',
            'datetime_updated'
        ]
