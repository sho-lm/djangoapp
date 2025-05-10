from django.apps import AppConfig


class BudgetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.budgets' # フォルダをapp配下に移動したので「budgets → app.budgets」にnameを変更する必要がある
