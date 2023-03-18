from rest_framework import generics
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """
    Returns a list of all categories, and creates new category
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        """ Sets the current user as the owner """
        serializer.save(owner=self.request.user)


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, and deletes a single Category instance
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_url_kwarg = 'id'
