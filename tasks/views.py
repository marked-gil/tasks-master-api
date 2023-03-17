from rest_framework import generics
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        """ Creates a Task model instance for the current user """
        serializer.save(owner=self.request.user)
