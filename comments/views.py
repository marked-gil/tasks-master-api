from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from .models import Comment
from shared_tasks.models import SharedTask
from .serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):
    """
    Returns a list of comments, and creates new comments
    """   
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """ Sets the current user as the owner """
        serializer.save(owner=self.request.user)
