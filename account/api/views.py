from curses import qiflush
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.serializers import serialize

from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from account.models import *
from account.api.serializer import *


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, ]

        return super(ProfileViewSet, self).get_permissions()

    @action(methods=['post'], detail=True)
    def follow(self, request, *args, **kwargs):
        target_profile_id = int(self.kwargs['pk'])
        logged_profile_id = int(self.request.user.id)

        if logged_profile_id == target_profile_id:
            response = {'message': 'Self reference'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        logged_profile = Profile.objects.get(id=logged_profile_id)

        if logged_profile.following.filter(id=target_profile_id).exists():
            response = {'message': 'Already follows'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            resp = logged_profile.following.add(target_profile_id)
            print(resp)
            return Response({'message': 'ok'})

    @ action(methods=['post'], detail=True)
    def unfollow(self, request, *args, **kwargs):
        target_profile_id = int(self.kwargs['pk'])
        logged_profile_id = int(self.request.user.id)

        if logged_profile_id == target_profile_id:
            response = {'message': 'Self reference'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        logged_profile = Profile.objects.get(id=logged_profile_id)

        if logged_profile.following.filter(id=target_profile_id).exists():
            resp = logged_profile.following.remove(target_profile_id)
            print(resp)
            return Response({'message': 'ok'})
        else:
            response = {'message': 'Does not follows'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @ action(methods=['get'], detail=True)
    def followers(self, request, *args, **kwargs):
        response_data = self.handle_follow_list({
            'profile_id': self.kwargs['pk'],
            'page': self.request.GET.get('page'),
            'type': 'followers'
        })

        return Response(data=response_data)

    @ action(methods=['get'], detail=True)
    def following(self, request, *args, **kwargs):
        response_data = self.handle_follow_list({
            'profile_id': self.kwargs['pk'],
            'page': self.request.GET.get('page'),
            'type': 'following'
        })

        return Response(data=response_data)

    def handle_follow_list(self, data):
        profile_request = ProfileRequestSerializer(data=data)
        profile_request.is_valid(raise_exception=True)

        queryset = None

        if data['type'] == 'following':
            queryset = Profile.objects.filter(
                followers=data['profile_id']).order_by('id')
        elif data['type'] == 'followers':
            queryset = Profile.objects.filter(
                following=data['profile_id']).order_by('id')

        paginator = Paginator(queryset, 100)

        profiles = []
        print(data['page'])

        try:
            page_obj = paginator.page(int(data['page']))
            serializer = self.serializer_class(page_obj.object_list, many=True)
            profiles = serializer.data
            print(profiles)

        except PageNotAnInteger:
            page_obj = paginator.page(1)
            serializer = self.serializer_class(page_obj.object_list, many=True)
            profiles = serializer.data
            print(profiles)

        # except EmptyPage:
        #     profiles = []

        return profiles

    # def get_queryset(self):
    #     print('get query set!!')

    #     queryset = Profile.objects.all()

    #     print(self.request.query_params)
    #     print(self.kwargs)

    #     profile_following_id = self.request.query_params.get('following')
    #     profile_followers_id = self.request.query_params.get('followers')

    #     if profile_followers_id is not None:
    #         queryset = queryset.filter(following=profile_followers_id)
    #     elif profile_following_id is not None:
    #         queryset = queryset.filter(followers=profile_following_id)

    #     # print(queryset.query)
    #     # print(queryset[0].user.email)

    #     return queryset

    def create(self, request):
        response = {'message': 'Create function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    # def update(self, request, pk=None):

    #     return Response(response, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


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
