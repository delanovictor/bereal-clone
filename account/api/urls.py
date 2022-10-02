from email.mime import base
from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'register', UserRegisterViewSet, basename='register')

router.register(r'profiles', ProfileViewSet)

# router.register(
#     r"profiles/(?P<profile_id>[\w]+)/(?P<action_type>[\w]+)", ProfileViewSet, basename="profiles")
# router.register(
#     r"profiles/(?P<profile_id>[\w]+)/", ProfileViewSet, basename="profiles")

urlpatterns = [
    # path('profiles/<int:pk>/followers/',
    #      ProfileViewSet.as_view({"get": "followers"}))
]
