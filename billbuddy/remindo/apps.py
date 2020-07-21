from django.apps import AppConfig

class RemindoConfig(AppConfig):
    name = 'remindo'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals