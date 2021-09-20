import os
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Changes the env module"

    def add_arguments(self, parser):
        parser.add_argument(
            'old', nargs='+', type=str, help="current env name")
        parser.add_argument('new', nargs='+', type=str, help="new env name")

    def handle(self, *args, **options):
        old = "settings." % options["old"][0]
        new = "settings." % options["new"][0]

        BASE_DIR = str(settings.BASE_DIR)
        filename = os.path.join(BASE_DIR, "manage.py")

        with open(filename, 'r') as f:
            filedata = f.read()

        filedata = filedata.replace(old, new)

        with open(filename, 'w') as f:
            f.write(filedata)
