import os
import json
import random
import string
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Resets the secret key'

    def handle(self, *args, **options):
        BASE_DIR = str(settings.BASE_DIR)
        config_file = os.path.join(BASE_DIR, ".json")

        with open(config_file, 'r') as f:
            filedata = f.read()
            try:
                jsn = json.loads(filedata)
            except ValueError as e:
                return False

        digits = string.digits
        ascii_letters = string.ascii_letters
        punctuation = string.punctuation.replace("\"", "")
        strings = digits + ascii_letters + punctuation
        SECRET_KEY = "".join(random.choice(strings) for i in range(0, 50))
        jsn["SECRET_KEY"] = SECRET_KEY

        with open(config_file, 'w') as file:
            file.write(json.dumps(jsn))
