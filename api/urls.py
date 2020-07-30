from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )
from rest_framework.routers import DefaultRouter

from .views import EmailValidView, JwtGetView, UsernameView, MeView

urlpatterns = [
    path('users/me/', MeView.as_view({
                                      'get' : 'list',
                                      'patch' : 'update'
                                      })),
]

custom_user_router = DefaultRouter()

custom_user_router.register(r'users', UsernameView, basename='customuser')

urlpatterns += custom_user_router.urls

urlpatterns += [
    path('auth/email/', EmailValidView.as_view()),
    path('auth/token/', JwtGetView.as_view()),
]

urlpatterns += [
    path('api/v1/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
