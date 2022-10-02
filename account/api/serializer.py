from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import Person
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PersonSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source='user.username', read_only=True)
    email = serializers.CharField(
        source='user.email', read_only=True)

    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ['id', 'username', 'email',
                  'profile_image', 'followers_count', 'following_count', 'latitude', 'longitude', 'created_at', 'updated_at']

    def get_followers_count(self, instance):
        return instance.followers_count()

    def get_following_count(self, instance):
        return instance.following_count()


# Register Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token
