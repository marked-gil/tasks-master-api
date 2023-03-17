from rest_framework import generics
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
