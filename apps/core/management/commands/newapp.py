import os
import shutil
from decouple import config
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Resets the database'

    def add_arguments(self, parser):
        parser.add_argument('app', nargs='+', type=str, help="new app name")

    def handle(self, *args, **options):
        appname = options["app"][0]
        PYTHON = config("PYTHON")
        BASE_DIR = str(settings.BASE_DIR)
        os.system("%s manage.py startapp %s" % (PYTHON, appname))
        oldapp = os.path.join(BASE_DIR, appname)
        newapp = os.path.join(BASE_DIR, "apps", appname)
        shutil.move(oldapp, newapp)
