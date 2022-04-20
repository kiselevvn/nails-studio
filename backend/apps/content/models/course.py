from django.db import models
from django.utils.translation import gettext as _


class Course(models.Model):
    """
    Курс
    """

    name = models.TextField(
        verbose_name=_("Наименование курса"),
    )
    description = models.TextField(
        verbose_name=_("Краткое описание"), blank=True, null=True
    )
    price = models.CharField(_("Цена"), blank=True, null=True, max_length=50)
    is_published = models.BooleanField(
        verbose_name=_("Является опубликованым"), default=False
    )
    order = models.IntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Курс")
        verbose_name_plural = _("Курсы")
        ordering = ["order"]

    def __str__(self):
        return f"{self.name}"
