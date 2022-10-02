from dataclasses import field
from rest_framework import serializers, fields

from django.contrib.auth.models import User
from feed.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'person', 'image',  'latitude',
                  'longitude', 'created_at', 'updated_at']


class FeedRequestSerializer(serializers.Serializer):
    person_id = fields.IntegerField(min_value=0)
    feed_type = fields.CharField(max_length=255)
    page = fields.IntegerField(min_value=0)

    def validate(self, data):

        feed_type_list = ['friends', 'discovery', 'memories']

        if (data['feed_type'] not in feed_type_list):
            raise serializers.ValidationError("Invalid feed type")

        if (data['person_id'] is None):
            raise serializers.ValidationError("Unauthorized")

        if (data['page'] is None):
            raise serializers.ValidationError("Invalid page")

        return data
