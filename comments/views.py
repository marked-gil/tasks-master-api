from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from tasks.models import Task
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
from tasks_master_api.permissions import IsOwner, IsAuthenticatedReadOnly


class CommentList(generics.ListCreateAPIView):
    """
    Returns a list of comments, and creates new comments
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        """ Returns a single comment """
        user = self.request.user
        task_ids = Task.objects.filter(
            Q(shared_to=user.id) | Q(owner=user)
        ).values('id')
        return Comment.objects.filter(
            Q(owner=user.id) |
            Q(task__id__in=task_ids)
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
        task_ids = Task.objects.filter(
            Q(shared_to=user.id) | Q(owner=user)
        ).values('id')
        return Comment.objects.filter(
            Q(owner=user.id) | Q(task__id__in=task_ids)
        ).distinct()
