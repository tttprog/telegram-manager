from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ManagerAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "manager_app"
    verbose_name = _("Manager")
