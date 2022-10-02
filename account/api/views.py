from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from account.models import *
from account.api.serializer import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, ]

        return super(PersonViewSet, self).get_permissions()

    def get_queryset(self):

        queryset = Person.objects.all()

        person_following_id = self.request.query_params.get('following')
        person_followers_id = self.request.query_params.get('followers')

        if person_followers_id is not None:
            queryset = queryset.filter(following=person_followers_id)
        elif person_following_id is not None:
            queryset = queryset.filter(followers=person_following_id)

        # print(queryset.query)
        # print(queryset[0].user.email)

        return queryset
