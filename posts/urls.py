from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView
from comments.views import CommentListCreateAPIView

urlpatterns = [
    path("", PostListCreateAPIView.as_view(), name="post-list-create"),
    path("<int:id>/", PostDetailAPIView.as_view(), name="post-detail"),
    path(
        "<int:post_id>/comments/",
        CommentListCreateAPIView.as_view(),
        name="comment-list-create",
    ),
]
