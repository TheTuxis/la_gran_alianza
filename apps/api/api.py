from rest_framework import generics, permissions

from django.contrib.auth.models import User
from apps.api.serializers import UserSerializer#, PostSerializer
#from .permissions import PostAuthorCanEditPermission


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'username'
