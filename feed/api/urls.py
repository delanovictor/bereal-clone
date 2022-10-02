from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r"feed/(?P<feed_type>[\w]+)", FeedViewSet, basename="feed")

urlpatterns = [
    path('', include(router.urls)),
]
