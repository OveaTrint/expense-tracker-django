import os

import django
from django.core.management import call_command

os.environ["DJANGO_SETTINGS_MODULE"] = "expense_tracker.settings"
os.environ["DJANGO_SUPERUSER_PASSWORD"] = "fake_pw"
django.setup()


call_command("flush", "--no-input")
print("flushed existing db")


cmd = "createsuperuser --username kamal"
cmd += " --email fake_email@example.com"
cmd += " --noinput"

call_command(*cmd.split())

from expense_generator import ExpensesFactory, create_users

create_users(10)

n_expense = 50
for _ in range(n_expense):
    ExpensesFactory.create()
