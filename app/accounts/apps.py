from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.accounts' # フォルダをapp配下に移動したので「accounts → app.accounts」にnameを変更する必要がある
