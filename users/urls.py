from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserApiView, MeApiView, ChangePasswordApiView

urlpatterns = [
    path("", UserApiView.as_view()),
    path("me/", MeApiView.as_view()),
    path("me/password/", ChangePasswordApiView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
