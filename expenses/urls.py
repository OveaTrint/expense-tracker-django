from django.urls import path

from .views import base, expenses

app_name = "expenses"

urlpatterns = [
    path("", base, name="base"),
    path("expenses/", expenses, name="expenses"),
]
