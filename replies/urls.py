from django.urls import path
from .views import ReplyDetailAPIView

urlpatterns = [
    path("<int:id>/", ReplyDetailAPIView.as_view(), name="reply-detail"),
]
