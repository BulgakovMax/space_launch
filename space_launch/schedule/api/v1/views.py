from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from space_launch.schedule.models import Rocket
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serializers import RocketSerializer

class RocketAPIList(generics.ListCreateAPIView):
    queryset = Rocket.objects.all()
    serializer_class = RocketSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class RocketAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Rocket.objects.all()
    serializer_class = RocketSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class RocketAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Rocket.objects.all()
    serializer_class = RocketSerializer
    permission_classes = (IsAdminOrReadOnly, )