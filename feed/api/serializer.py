from rest_framework import serializers

from django.contrib.auth.models import User
from feed.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'person', 'image', 'likes',  'latitude',
                  'longitude', 'created_at', 'updated_at']
