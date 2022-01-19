import os
import shutil
from django.db import connection
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Removes apps migrations and tables"

    def add_arguments(self, parser):
        parser.add_argument('apps', nargs='+', type=str, help="apps name")

    def handle(self, *args, **options):
        while True:
            confirmation = str(
                input(
                    "Warning: Are you sure you want to remove the Migrations and Tables (y/n)? "
                )
            )
            if confirmation == "y" or confirmation == "n":
                break
        if confirmation == "y":
            BASE_DIR = str(settings.BASE_DIR)

            apps = options["apps"]
            for app in apps:
                call_command("migrate", app, "zero")
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM django_migrations WHERE app='%s'" % app)
                migration = os.path.join(BASE_DIR, "apps", app, 'migrations')
                if os.path.isdir(migration):
                    shutil.rmtree(migration)

                os.mkdir(migration)
                open(os.path.join(migration, "__init__.py"), "x").close()
