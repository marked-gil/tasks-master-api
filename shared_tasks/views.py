from rest_framework import generics
from rest_framework.response import Response
from .models import SharedTask
from .serializers import SharedTaskSerializer


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
        return SharedTask.objects.filter(owner=user)
