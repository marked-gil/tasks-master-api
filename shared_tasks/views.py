from rest_framework import generics
from rest_framework.response import Response
from .models import SharedTask
from .serializers import SharedTaskSerializer
from django.db.models import Q
from tasks_master_api.permissions import IsOwner, IsAuthenticatedReadOnly


class SharedTaskList(generics.ListCreateAPIView):
    """
    Returns a list of current user's shared tasks, and creates new shared task
    """
    serializer_class = SharedTaskSerializer

    def get_queryset(self):
        """
        Returns shared tasks created by, or shared to, the current user
        """
        user = self.request.user
        return SharedTask.objects.filter(
            Q(shared_to=user.id) | Q(owner=user)
        ).distinct()

    def perform_create(self, serializer):
        """ Sets the current user as the owner """
        serializer.save(owner=self.request.user)


class SharedTaskDetails(generics.RetrieveDestroyAPIView):
    """
    Retrieves and deletes a single SharedTask instance
    """
    serializer_class = SharedTaskSerializer
    permission_classes = [IsOwner | IsAuthenticatedReadOnly]
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        """ Returns a single task created by the current user """
        user = self.request.user
        return SharedTask.objects.filter(
            Q(shared_to=user.id) | Q(owner=user.id)
        ).distinct()
