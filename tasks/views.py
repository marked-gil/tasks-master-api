from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tasks_master_api.permissions import IsOwner, IsSharingTask
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Task
from .serializers import TaskSerializer
from datetime import date, datetime


class TaskList(generics.ListCreateAPIView):
    """
    Returns a list of current user's tasks, and creates new task
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'due_date', 'priority', 'progress', 'category', 'shared_to',
        'is_shared'
    ]
    ordering_fields = ['due_date', 'due_time', 'priority']
    search_fields = ['category__category_name', 'task_name']

    def get_queryset(self):
        """
        Returns all tasks created by the logged-in user
        """
        user = self.request.user
        if user.is_authenticated:
            user_all_tasks = Task.objects.filter(
                Q(owner=user) | Q(shared_to__id=user.id)
            ).distinct()
        else:
            user_all_tasks = Task.objects.none()
        return user_all_tasks

        for task in user_all_tasks:
            if task.progress != 'completed':
                if task.due_date == date.today():
                    if task.due_time is not None:
                        if task.due_time >= datetime.now().time():
                            task.progress = 'to-do'
                        else:
                            task.progress = 'overdue'
                    else:
                        task.progress = 'to-do'
                elif task.due_date < date.today():
                    task.progress = 'overdue'
                elif task.due_date > date.today():
                    task.progress = 'to-do'
                task.save()

        return Task.objects.filter(
            Q(owner=user) | Q(shared_to__id=user.id)
        ).distinct()

    def perform_create(self, serializer):
        """ Sets the current user as the owner """
        serializer.save(owner=self.request.user)


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, and deletes a single Task instance
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwner | IsSharingTask]

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        """ Returns a single task created by the current user """
        user = self.request.user
        return Task.objects.filter(
            Q(owner=user) | Q(shared_to__id=user.id)
        ).distinct()
