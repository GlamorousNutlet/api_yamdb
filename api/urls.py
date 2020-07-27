from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )

from .views import EmailvalidView, JwtGetView

urlpatterns = [
    path('auth/email/', EmailvalidView.as_view()),
    path('auth/token/', JwtGetView.as_view()),
]

urlpatterns += [
    path('api/v1/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
