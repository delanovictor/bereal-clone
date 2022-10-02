from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from feed.api.urls import router as feed_router
from account.api.urls import router as account_router


from account.api.views import MyTokenObtainPairView
from feed.api.views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


router = routers.DefaultRouter()

router.registry.extend(feed_router.registry)
router.registry.extend(account_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
