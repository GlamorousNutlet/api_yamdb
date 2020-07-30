from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )
from rest_framework.routers import DefaultRouter

from .views import *

api_router = DefaultRouter()
api_router.register(r'users', PatchUserView, basename='customuser')
api_router.register(r'categories', CategoryViewSet, basename='categories')
api_router.register(r'genres', GenreViewSet, basename='categories')
api_router.register(r'titles', TitleViewSet, basename='categories')
api_router.register(r'review', ReviewViewSet, basename='categories')
api_router.register(r'comment', CommentViewSet, basename='categories')


urlpatterns = api_router.urls

urlpatterns += [
    path('auth/email/', EmailValidView.as_view()),
    path('auth/token/', JwtGetView.as_view()),
]

urlpatterns += [
    path('token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
