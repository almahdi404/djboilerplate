import os
import glob
import shutil
from decouple import config
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import connection


class Command(BaseCommand):
    help = "Resets apps migrations and tables"

    def add_arguments(self, parser):
        parser.add_argument('apps', nargs='+', type=str, help="apps name")

    def handle(self, *args, **options):
        while True:
            confirmation = str(input(
                "Warning: Are you sure you want to reset the Migrations and Tables (y/n)? "))
            if confirmation == "y" or confirmation == "n":
                break
        if confirmation == "y":
            PYTHON = config("PYTHON")
            BASE_DIR = str(settings.BASE_DIR)

            apps = options["apps"]
            for app in apps:
                migration = os.path.join(BASE_DIR, "apps", app, 'migrations')
                os.system("%s manage.py migrate %s zero" % (PYTHON, app))
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM django_migrations WHERE app='%s'" % app)
                if os.path.isdir(migration):
                    shutil.rmtree(migration)
                os.system("%s manage.py makemigrations %s" % (PYTHON, app))
                os.system("%s manage.py migrate %s" % (PYTHON, app))
