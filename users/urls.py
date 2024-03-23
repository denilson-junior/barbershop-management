from django.urls import path
from users.views import UserAPIView


urlpatterns = [path("users/", UserAPIView.as_view(), name="users")]
