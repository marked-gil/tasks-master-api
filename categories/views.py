from rest_framework import generics
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """
    Returns a list of all categories, and creates new category
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        """ Returns all categories created by the current user """
        user = self.request.user
        return Category.objects.filter(owner=user)

    def perform_create(self, serializer):
        """ Sets the current user as the owner """
        serializer.save(owner=self.request.user)


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, and deletes a single Category instance
    """
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        """ Returns all categories created by the current user """
        user = self.request.user
        return Category.objects.filter(owner=user)
