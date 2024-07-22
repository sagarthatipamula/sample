from django.apps import AppConfig

class MonitoringConfig(AppConfig):
    name = 'track'

    def ready(self):
        from . import scheduler
        scheduler.start()
