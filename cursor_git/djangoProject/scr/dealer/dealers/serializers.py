from rest_framework import serializers

from dealer.users.serializers import UserSerializer


class DealerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    user = UserSerializer()
