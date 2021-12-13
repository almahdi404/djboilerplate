from django.apps import AppConfig
from core.sass import compiler


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        compiler()
