from django.urls import path

from .views import base, expenses, new_expense

app_name = "expenses"

urlpatterns = [
    path("", base, name="base"),
    path("expenses/", expenses, name="expenses"),
    path("new_expense/", view=new_expense, name="new_expense"),
]
