from django.db import models
from django.utils.translation import gettext as _


class Worker(
    models.Model,
):
    """
    Сотрудник
    """

    name = models.CharField(
        verbose_name=_("Имя"),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    photo = models.ImageField(_("Фотогорафия"), blank=True, null=True)

    is_published_landing = models.BooleanField(
        verbose_name=_("Запись опубликована"), default=False
    )
    order = models.IntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Сотрудник")
        verbose_name_plural = _("Сотрудники")
        ordering = ["order"]

    def __str__(self):
        return f"{self.name}"
