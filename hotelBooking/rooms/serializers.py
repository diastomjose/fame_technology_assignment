from .models import roomsModel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = roomsModel
        fields = ('room_no', 'room_cost', 'room_status')

