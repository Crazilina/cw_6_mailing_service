from django.apps import AppConfig
from django.utils.autoreload import autoreload_started


class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'

    def ready(self):
        from mailings.tasks import start_scheduler
        autoreload_started.connect(start_scheduler)
