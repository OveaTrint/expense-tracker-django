from django.urls import path

from .views import base, delete_expense, expense, expenses, new_expense

app_name = "expenses"

urlpatterns = [
    path("", base, name="base"),
    path("expenses/", expenses, name="expenses"),
    path("expenses/<int:expense_id>/", view=expense, name="expense"),
    path("new_expense/", view=new_expense, name="new_expense"),
    path("delete/<int:expense_id>", view=delete_expense, name="delete_expense"),
]
