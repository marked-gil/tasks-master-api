from rest_framework import generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    """
    Returns a list of current user's tasks, and creates new task
    """
    serializer_class = TaskSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = ['due_date', 'priority', 'progress', 'category']
    ordering_fields = ['due_date', 'due_time', 'priority']
    search_fields = ['category__category_name', 'task_name']

    def get_queryset(self):
        """
        Returns all tasks created by the logged-in user
        """
        user = self.request.user
        return Task.objects.filter(owner=user)

    def perform_create(self, serializer):
        """ Sets the current user as the owner """
        serializer.save(owner=self.request.user)


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, and deletes a single Task instance
    """
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        """ Returns a single task created by the current user """
        user = self.request.user
        return Task.objects.filter(owner=user)
