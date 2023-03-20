from rest_framework import serializers
from tasks.models import Task
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for Comment model """
    owner = serializers.ReadOnlyField(source='owner.username')
    task = serializers.SlugRelatedField(
        slug_field='task_name',
        queryset=Task.objects.all()
    )
    task_id = serializers.ReadOnlyField(source='task.id')
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
            'is_reply_to_comment', 'datetime_created', 'datetime_updated'
        ]
