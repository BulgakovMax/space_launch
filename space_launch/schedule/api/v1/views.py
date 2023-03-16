from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from schedule.models  import Rocket, Location, Agency
from schedule.api.v1.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from schedule.api.v1.serializers import RocketSerializer, LocationSerializer, AgencySerializer


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


class LocationAPIList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AgencyAPIList(generics.ListCreateAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )