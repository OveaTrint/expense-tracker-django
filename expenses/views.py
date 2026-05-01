from django.shortcuts import render

from .models import Expenses


# Create your views here.
def base(request):
    return render(request, "expenses/base.html")


def expenses(request):
    expenses = Expenses.objects.all()
    context = {"expenses": expenses}

    return render(request, "expenses/expenses.html", context=context)
