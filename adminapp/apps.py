from django.apps import AppConfig


class AdminAppConfig(AppConfig):
    name = 'adminapp'

    def ready(self):
        from . import signals