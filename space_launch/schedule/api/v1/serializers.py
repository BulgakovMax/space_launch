from rest_framework import serializers

from schedule.models import Rocket, Location, Agency


class RocketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rocket
        fields = ('id', 'title', 'content', 'type', 'location', 'agency', 'user')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'country_code', 'content')


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ('id', 'name', 'type', 'content')


