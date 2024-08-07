from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostLikeAPIView,
    PostDislikeAPIView,
    ReplyAPIView,
    ReplyModifyAPIView,
)

urlpatterns = [
    path("", PostListAPIView.as_view()),
    path("<int:pk>/", PostDetailAPIView.as_view()),
    path("<int:pk>/like/", PostLikeAPIView.as_view()),
    path("<int:pk>/dislike/", PostDislikeAPIView.as_view()),
    path("comments/<int:comment_pk>/replies/", ReplyAPIView.as_view()),
    path("replies/<int:reply_pk>/", ReplyModifyAPIView.as_view()),
]
