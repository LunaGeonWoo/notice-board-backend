from django.urls import path
from .views import CommentAPIView, CommentModifyAPIView


urlpatterns = [
    path("<int:id>/", CommentModifyAPIView.as_view()),
    path("<int:id>/comments/", CommentAPIView.as_view()),
]
