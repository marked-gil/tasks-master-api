from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from shared_tasks.models import SharedTask
from .models import Comment
from shared_tasks.models import SharedTask
from .serializers import CommentSerializer
from tasks_master_api.permissions import IsOwner, IsAuthenticatedReadOnly


class CommentList(generics.ListCreateAPIView):
    """
    Returns a list of comments, and creates new comments
    """
    serializer_class = CommentSerializer

    def get_queryset(self):
        """ Returns a single comment """
        user = self.request.user
        tasks = SharedTask.objects.filter(shared_to=user.id).values('task_id')
        return Comment.objects.filter(
            Q(reply_to=user.id) | Q(owner=user.id) |
            Q(task__id__in=tasks)
        ).distinct()

    def perform_create(self, serializer):
        """ Sets the current user as the owner """
        serializer.save(owner=self.request.user)


class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates and deletes a single Comment instance
    """
    permission_classes = [IsOwner | IsAuthenticatedReadOnly]
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        """ Returns a single comment """
        user = self.request.user
        tasks = SharedTask.objects.filter(shared_to=user.id).values('task_id')
        return Comment.objects.filter(
            Q(reply_to=user.id) | Q(owner=user.id) |
            Q(task__id__in=tasks)
        ).distinct()
