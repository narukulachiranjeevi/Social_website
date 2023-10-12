from django.apps import AppConfig


class PicturesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pictures'
    def ready(self):
        # import signal handlers
        import pictures.signals
