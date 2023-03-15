from rest_framework import serializers

from schedule.models import Rocket


class RocketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rocket
        fields = ('user', 'id', 'title', 'content')

