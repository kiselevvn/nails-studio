from django.db import models
from django.utils.translation import gettext as _


class CategoryService(
    models.Model,
):
    """
    Категория услуги
    """

    name = models.TextField(
        verbose_name=_("Категория услуги"),
    )
    description = models.TextField(
        verbose_name=_("Краткое описание"), blank=True, null=True
    )
    is_published = models.BooleanField(
        verbose_name=_("Катеория услуг опубликована"), default=False
    )
    order = models.IntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Категория услуг")
        verbose_name_plural = _("Категории услуг")

    def __str__(self):
        return f"{self.name}"
