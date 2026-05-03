from django.contrib.auth import urls as auth_urls
from django.urls import include, path

from .views import register

app_name = "accounts"

urlpatterns = [
    path("", include(auth_urls)),
    path("sign_up/", view=register, name="register"),
]
