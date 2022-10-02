from django.contrib import admin
from django.urls import path, include

from rest_framework import routers


from feed.api.views import PostViewSet
from account.api.views import PersonViewSet, MyTokenObtainPairView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


router = routers.DefaultRouter()

router.register(r'persons', PersonViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
