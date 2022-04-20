from django.db import models
from django.utils.translation import gettext as _


class AdditionalService(models.Model):
    """
    Дополнительная услуга
    """

    name = models.TextField(
        verbose_name=_("Наименование"),
    )
    price = models.CharField(_("Цена"), blank=True, null=True, max_length=50)
    is_published = models.BooleanField(
        verbose_name=_("Является опубликованым"), default=False
    )
    order = models.IntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Дополнительная услуга")
        verbose_name_plural = _("Дополнительные услуги")

    def __str__(self):
        return f"{self.name}"
