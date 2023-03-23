from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer
from tasks_master_api.permissions import IsOwner, IsAuthenticatedReadOnly


class ProfileList(generics.ListAPIView):
    """
    Returns a list of all profiles
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves (for authenticated users), Updates and deletes (for owners only)
    current user's profile
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner | IsAuthenticatedReadOnly]
    lookup_url_kwarg = 'id'
    queryset = Profile.objects.all()

    def perform_destroy(self, instance):
        """ Deletes both the user account and their profile """
        instance.delete()
        User.objects.get(id=instance.owner.id).delete()
