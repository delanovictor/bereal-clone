from rest_framework import serializers
from beRealClone.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'userName', 'phoneNumber', 'profileImage', 'latitude', 'longitude', 'followers', 'following', 'createdAt', 'updatedAt']
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'image', 'likes',  'latitude', 'longitude', 'createdAt', 'updatedAt']