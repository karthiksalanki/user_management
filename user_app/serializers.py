from rest_framework import serializers
from .models import User, Friend
from .serializers import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','first_name', 'last_name',]

class FriendSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    friend = UserSerializer(many=True)
    class Meta:
        model = Friend
        fields = ['id', 'user', 'friend']