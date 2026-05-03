from decimal import Decimal

import django.forms.forms
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Expenses(models.Model):
    class Category(models.TextChoices):
        FOOD = "food"
        BEAUTY = "beauty"
        COMMUNICATION = "communication"
        ENJOYMENT = "enjoyment"
        MISCELLANEOUS = "misc"
        TRANSPORTATION = "transportation"

    description = models.CharField(max_length=50)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    category = models.CharField(choices=Category)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description[:10]
