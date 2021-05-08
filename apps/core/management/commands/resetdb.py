import os
import glob
import shutil
from decouple import config
from django.db import connection
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Resets the migrations and database"

    def handle(self, *args, **options):
        while True:
            confirmation = str(input(
                "Warning: Are you sure you want to reset the Migrations and Database (y/n)? "))
            if confirmation == "y" or confirmation == "n":
                break
        if confirmation == "y":
            dbname = settings.DATABASES["default"]["NAME"]
            with connection.cursor() as cursor:
                cursor.execute("DROP DATABASE %s" % dbname)
                cursor.execute("CREATE DATABASE %s" % dbname)

            PYTHON = config("PYTHON")
            BASE_DIR = str(settings.BASE_DIR)
            migrations = glob.glob(os.path.join(
                BASE_DIR, "apps", "**", "migrations"))

            for migration in migrations:
                if os.path.isdir(migration):
                    shutil.rmtree(migration)

            apps = [migration.split("\\")[-2] for migration in migrations]
            for app in apps:
                os.system("%s manage.py makemigrations %s" % (PYTHON, app))
            os.system("%s manage.py migrate" % PYTHON)
