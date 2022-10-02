from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()


feed_list = PostViewSet.as_view({
    'get': 'list'
})

router.register(r'posts', PostViewSet)
router.register(r"feed/(?P<feed_type>[\w]+)", FeedViewSet, basename="test")

urlpatterns = [
    path('', include(router.urls)),
]
