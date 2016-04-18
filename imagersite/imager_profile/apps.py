from django.apps import AppConfig

class ImagerProfileConfig(AppConfig):
    name = 'imager_profile'

    # first create a handles file
    def ready(self):
        """"Code to run when the app is ready."""
        from imager_profile import handlers
