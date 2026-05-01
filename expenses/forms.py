from django.forms import ModelForm

from .models import Expenses


class ExpensesForms(ModelForm):
    class Meta:
        model = Expenses
        fields = ["description", "catgeory", "amount"]
