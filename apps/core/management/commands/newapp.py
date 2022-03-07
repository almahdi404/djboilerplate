import os
import shutil
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a new app in apps folder"

    def add_arguments(self, parser):
        parser.add_argument("app", nargs="+", type=str, help="new app name")

    def handle(self, *args, **options):
        appname = options["app"][0]
        BASE_DIR = str(settings.BASE_DIR)
        call_command("startapp", appname)
        oldapp = os.path.join(BASE_DIR, appname)
        newapp = os.path.join(BASE_DIR, "apps", appname)
        shutil.move(oldapp, newapp)
