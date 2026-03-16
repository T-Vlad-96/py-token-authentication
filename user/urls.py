from django.urls import path

from user.views import UserRegisterView, UserLoginView, UserRetrieveUpdateView

app_name = "user"


urlpatterns = [
    path(
        "register/",
        UserRegisterView.as_view(),
        name="user_register"
    ),
    path(
        "login/",
        UserLoginView.as_view(),
        name="get_user_token"
    ),
    path(
        "me/",
        UserRetrieveUpdateView.as_view(),
        name="user_retrieve_update"
    ),
]
