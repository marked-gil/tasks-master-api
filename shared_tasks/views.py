from rest_framework import generics
from rest_framework.response import Response
from .models import SharedTask
from .serializers import SharedTaskSerializer
from django.db.models import Q


class SharedTaskList(generics.ListCreateAPIView):
    """
    Returns a list of current user's shared tasks, and creates new shared task
    """
    serializer_class = SharedTaskSerializer

    def get_queryset(self):
        """
        Returns all shared tasks created by the current user
        """
        user = self.request.user
        return SharedTask.objects.filter(Q(shared_to=user.id) | Q(owner=user))

    def perform_create(self, serializer):
        """ Sets the current user as the owner """
        serializer.save(owner=self.request.user)
