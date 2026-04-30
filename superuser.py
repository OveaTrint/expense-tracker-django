import os

import django
from django.core.management import call_command

os.environ["DJANGO_SETTINGS_MODULE"] = "expense_tracker.settings"
os.environ["DJANGO_SUPERUSER_PASSWORD"] = "kdeen"

django.setup()

cmd = "createsuperuser"
cmd += " --username kdeen"
cmd += " --email kbaiyewu@gmail.com"
cmd += " --noinput"

cmd_parts = cmd.split()

call_command(*cmd_parts)
