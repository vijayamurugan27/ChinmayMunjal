#### Using generic class based views
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework import permissions

permission_classes = [permissions.IsAuthenticatedOrReadOnly]
from snippets.permissions import IsOwnerOrReadOnly

permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def perform_create(self, serializer):
    serializer.save(owner=self.request.user)