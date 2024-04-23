from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (UserRegistrationView, TokenObtainView,
                    TitleViewSet, CategoryViewSet, GenreViewSet,
                    ReviewViewSet, CommentViewSet, UserViewSet,)

router_v1 = DefaultRouter()
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('users', UserViewSet, basename='users')

v1_prefix = 'v1/'

urlpatterns = [
    path(v1_prefix + 'users/me/', UserViewSet.as_view(
        {'get': 'me', 'patch': 'patch_me', 'post': 'post_me'}
    ), name='user-me'),
    path(v1_prefix, include(router_v1.urls)),
    path(v1_prefix + 'auth/token/',
         TokenObtainView.as_view(), name='token_obtain'),
    path(v1_prefix + 'auth/signup/',
         UserRegistrationView.as_view(), name='signup')
]
