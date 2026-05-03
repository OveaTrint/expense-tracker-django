from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ExpensesForm
from .models import Expenses


# Create your views here.
def index(request):
    return render(request, "expenses/index.html")


@login_required
def expenses(request):
    expenses = Expenses.objects.filter(owner=request.user)
    total_expense = 0
    for expense in expenses:
        total_expense += expense.amount

    context = {"expenses": expenses, "total_expense": total_expense}

    return render(request, "expenses/expenses.html", context=context)


@login_required
def new_expense(request):
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
    expense = Expenses.objects.get(id=expense_id)
    context = {"expense": expense}

    return render(request, template_name="expenses/expense.html", context=context)


@login_required
def delete_expense(request, expense_id):
    expense = Expenses.objects.get(id=expense_id)

    expense.delete()

    return render(request, template_name="expenses/delete_expense.html")


@login_required
def update_expense(request, expense_id):
    context = {}
    expense = Expenses.objects.get(id=expense_id)

    form = ExpensesForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect("expenses:expenses")

    context["form"] = form
    return render(request, "expenses/update_expense.html", context)
