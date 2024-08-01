from django.urls import path
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostLikeAPIView,
    PostDislikeAPIView,
    CommentAPIView,
)

urlpatterns = [
    path("", PostListAPIView.as_view()),
    path("<int:pk>/", PostDetailAPIView.as_view()),
    path("<int:pk>/like/", PostLikeAPIView.as_view()),
    path("<int:pk>/dislike/", PostDislikeAPIView.as_view()),
    path("<int:pk>/comments/", CommentAPIView.as_view()),
]
