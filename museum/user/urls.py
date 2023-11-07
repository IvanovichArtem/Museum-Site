from django.urls import path
from .views import login, logout, UserRegistrationView, UserProfileView
from django.contrib.auth.decorators import login_required

app_name = "user"

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("logout", logout, name="logout"),
    path(
        "profile/<int:pk>/", login_required(UserProfileView.as_view()), name="profile"
    ),
]
