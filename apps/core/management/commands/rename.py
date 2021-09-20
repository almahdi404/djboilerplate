import os
import glob
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Renames the Project"

    def add_arguments(self, parser):
        parser.add_argument('old', nargs='+', type=str, help="current project name")
        parser.add_argument('new', nargs='+', type=str, help="new project name")

    def handle(self, *args, **options):
        old = options["old"][0]
        new = options["new"][0]

        BASE_DIR = str(settings.BASE_DIR)
        projectfiles = []
        managefile = os.path.join(BASE_DIR, "manage.py")
        projectfiles.append(managefile)
        projectfiles += glob.glob(os.path.join(BASE_DIR, old, "*.py"))
        projectfiles += glob.glob(os.path.join(BASE_DIR, old, "**\*.py"))

        for pythonfile in projectfiles:
            with open(pythonfile, 'r') as f:
                filedata = f.read()

            filedata = filedata.replace(old, new)

            with open(pythonfile, 'w') as f:
                f.write(filedata)
        os.rename(os.path.join(BASE_DIR, old), os.path.join(BASE_DIR, new))
