from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import GroupViewSet, PostViewSet, FollowViewSet, CommentViewSet

router_v1 = SimpleRouter()
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(
    r'posts/(?P<post_id>[\d]+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
