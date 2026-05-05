from django.forms import ModelForm

from .models import Expenses


class ExpensesForm(ModelForm):
    """
    Form for adding or updating an expense
    """

    class Meta:
        model = Expenses
        fields = ["description", "category", "amount"]
