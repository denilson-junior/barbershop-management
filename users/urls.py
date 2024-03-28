from django.urls import path
from users.views import (
    UserAPIView,
    LoginView,
    UserConfirmationRequestEmailView,
    UserConfirmationRequestCodeView,
    UserMeAPIView
)


urlpatterns = [
    path("users/", UserAPIView.as_view(), name="users"),
    path("user/me/", UserMeAPIView.as_view(), name="user_me"),
    path("token/", LoginView.as_view(), name="token"),
    path(
        "confirmation/send_email/",
        UserConfirmationRequestEmailView.as_view(),
        name="code_email",
    ),
    path(
        "confirmation/send_code/",
        UserConfirmationRequestCodeView.as_view(),
        name="confirmation_code",
    ),
]
