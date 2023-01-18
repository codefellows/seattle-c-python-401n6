from rest_framework import generics
from .models import Things
from .serializer import ThingsSerializer


class ThingsList(generics.ListCreateAPIView):
    queryset = Things.objects.all()
    serializer_class = ThingsSerializer


class ThingsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Things.objects.all()
    serializer_class = ThingsSerializer
