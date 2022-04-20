from django.db import models
from django.utils.translation import gettext as _


class Сertificate(models.Model):
    """
    Сертфикат
    """

    picture = models.ImageField(verbose_name=_("Изображение"))
    description = models.TextField(
        verbose_name=_("Краткое описание"), blank=True, null=True
    )
    is_published = models.BooleanField(
        verbose_name=_("Является опубликованым"), default=False
    )
    order = models.IntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Сертфикат")
        verbose_name_plural = _("Сертфикаты")
        ordering = ["order"]

    def __str__(self):
        return f"Сертфикат"
