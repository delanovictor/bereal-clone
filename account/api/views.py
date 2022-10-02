from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from account.models import *
from account.api.serializer import *


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


class UserRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegisterSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        post_data = {}
        post_data['response'] = 'Successfully registrated a new user'
        post_data['email'] = serializer.email
        post_data['username'] = serializer.username

        return Response(post_data, status=status.HTTP_201_CREATED, headers=headers)
