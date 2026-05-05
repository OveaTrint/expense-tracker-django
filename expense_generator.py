import random

import factory
from django.contrib.auth.models import User
from faker import Faker

from expenses.models import Expenses

fake = Faker()


def get_description():
    description = " ".join(fake.words(5)).title()
    return description


def get_amount():
    amount = fake.pydecimal(
        left_digits=random.randint(1, 5),
        right_digits=2,
        positive=True,
    )
    return amount


def get_category():
    category = random.choice(Expenses.Category.values)
    return category


def create_users(n: int):
    for i in range(n):
        user = User.objects.create_user(
            username=fake.user_name(),
            password=fake.password(),
        )
        user.save()


def get_owner():
    users = User.objects.all()
    return random.choice(users)


class ExpensesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expenses

    description = factory.LazyFunction(get_description)
    category = factory.LazyFunction(get_category)
    amount = factory.LazyFunction(get_amount)
    owner = factory.LazyFunction(get_owner)
