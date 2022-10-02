from django.contrib import admin
from django.urls import path, include

from rest_framework import routers


from feed.api.views import PostViewSet
from account.api.views import PersonViewSet

router = routers.DefaultRouter()

router.register(r'persons', PersonViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
