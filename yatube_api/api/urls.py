from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import (CommentViewSet, GroupViewSet,
                       PostViewSet, FollowViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
