from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'
    def ready(self):
        print("ready")
        import main.signals
