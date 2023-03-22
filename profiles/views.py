from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from tasks_master_api.permissions import IsOwner, IsAuthenticatedReadOnly


class ProfileList(generics.ListAPIView):
    """
    Returns a list of all profiles
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetails(generics.RetrieveUpdateAPIView):
    """
    Retrieves (for authenticated users) and Updates (for owners only)
    current user's profile
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsOwner | IsAuthenticatedReadOnly]
    lookup_url_kwarg = 'id'
