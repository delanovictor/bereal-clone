from email.mime import base
from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'persons', PersonViewSet)
router.register(r'register', UserRegisterViewSet, basename='register')
