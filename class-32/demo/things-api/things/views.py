from rest_framework import generics
from .models import Things
from .serializer import ThingsSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ThingsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Things.objects.all()
    serializer_class = ThingsSerializer


class ThingsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Things.objects.all()
    serializer_class = ThingsSerializer
