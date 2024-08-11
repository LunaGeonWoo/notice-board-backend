from django.urls import path
from .views import (
    UserApiView,
    MeApiView,
    ChangePasswordApiView,
    LogInApiView,
    LogOutApiView,
    GithubLogInApiView,
)

urlpatterns = [
    path("", UserApiView.as_view()),
    path("me/", MeApiView.as_view()),
    path("me/password/", ChangePasswordApiView.as_view()),
    path("log-in/", LogInApiView.as_view(), name="log_in"),
    path("log-out/", LogOutApiView.as_view(), name="log_out"),
    path("github/", GithubLogInApiView.as_view(), name="log_out"),
]
