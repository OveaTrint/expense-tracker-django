from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExpensesForm
from .models import Expenses

"""
Views module for expenses app.
All views require a logged in user barring the `index`
"""


# Create your views here.
def index(request):
    """Home page view"""
    return render(request, "expenses/index.html")


@login_required
def expenses(request):
    """View for displaying all expenses of a user"""
    expenses = Expenses.objects.filter(owner=request.user)
    total_expenses = expenses.aggregate(total_expense=Sum("amount"))

    if total_expenses["total_expense"] is None:
        total_expenses["total_expense"] = 0

    context = {"expenses": expenses}
    context.update(total_expenses)
    return render(request, "expenses/expenses.html", context=context)


@login_required
def new_expense(request):
    """View for adding a new expense"""
    if request.method == "POST":
        form = ExpensesForm(request.POST)

        if form.is_valid():
            new_expense = form.save(commit=False)
            new_expense.owner = request.user
            new_expense.save()

            return redirect("expenses:expenses")
    else:
        form = ExpensesForm()

    return render(request, "expenses/new_expense.html", {"form": form})


@login_required
def expense(request, expense_id):
    """View for showing the details of an expense"""
    expense = get_object_or_404(Expenses, id=expense_id, owner=request.user)
    context = {"expense": expense}

    return render(request, template_name="expenses/expense.html", context=context)


@login_required
def delete_expense(request, expense_id):
    """
    View for deleting an expense.
    Redirects to a template that uses a POST request for deletion.
    """
    expense = get_object_or_404(Expenses, id=expense_id, owner=request.user)

    if request.method == "POST":
        expense.delete()
        return redirect("expenses:expenses")

    return render(request, template_name="expenses/delete_expense.html")


@login_required
def update_expense(request, expense_id):
    """View for updating an expense"""
    context = {}

    expense = Expenses.objects.get(id=expense_id, owner=request.user)
    form = ExpensesForm(request.POST or None, instance=expense)

    if form.is_valid():
        form.save()
        return redirect("expenses:expenses")

    context["form"] = form
    return render(request, "expenses/update_expense.html", context)
