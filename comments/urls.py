from django.urls import path
from .views import CommentDetailAPIView
from replies.views import ReplyListCreateAPIView, ReplyDetailAPIView

urlpatterns = [
    path("<int:id>/", CommentDetailAPIView.as_view(), name="comment-detail"),
    path(
        "<int:comment_id>/replies/",
        ReplyListCreateAPIView.as_view(),
        name="reply-list-create",
    ),
]
