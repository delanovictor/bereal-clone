from django.contrib import admin
from django.urls import path, include
from beRealClone.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
