from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.


class Channel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    name = models.CharField(
        max_length=100,
        verbose_name=_("Channel Name"),
    )
    channel_id = models.CharField(
        max_length=100,
        verbose_name=_("Channel ID"),
        help_text=_("Without @"),
    )
    date_add = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name=_("Date Add"),
    )
    active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")
