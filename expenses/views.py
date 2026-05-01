from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ExpensesForm
from .models import Expenses


# Create your views here.
def base(request):
    return render(request, "expenses/base.html")


@login_required
def expenses(request):
    expenses = Expenses.objects.filter(owner=request.user)
    context = {"expenses": expenses}

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
