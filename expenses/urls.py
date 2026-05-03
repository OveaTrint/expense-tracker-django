from django.urls import path

from .views import (
    delete_expense,
    expense,
    expenses,
    index,
    new_expense,
    update_expense,
)

app_name = "expenses"

urlpatterns = [
    path("", index, name="index"),
    path("expenses/", expenses, name="expenses"),
    path("expenses/<int:expense_id>/", view=expense, name="expense"),
    path("new_expense/", view=new_expense, name="new_expense"),
    path("expenses/<int:expense_id>/delete", view=delete_expense, name="delete"),
    path(
        "expenses/<int:expense_id>/update",
        view=update_expense,
        name="update",
    ),
]
