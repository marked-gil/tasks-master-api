from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for Comment model """
    class Meta:
        """ Specifies the fields returned by the API """
        model = Comment
        fields = [
            'id', 'owner', 'task', 'content', 'reply_to',
            'is_reply_to_comment', 'datetime_created', 'datetime_updated'
        ]
