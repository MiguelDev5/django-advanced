from django.apps import AppConfig
from . import updater

class Scheduler01Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.scheduler01'
    def ready(self):
        updater.start()
