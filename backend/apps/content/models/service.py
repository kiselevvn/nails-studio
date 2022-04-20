from django.db import models
from django.utils.translation import gettext as _


class Service(models.Model):
    """
    Услуга
    """

    category_service = models.ForeignKey(
        "content.CategoryService",
        verbose_name=_("Категория услуги"),
        on_delete=models.CASCADE,
        related_name="services",
        blank=True,
        null=True,
    )
    name = models.TextField(
        verbose_name=_("Наименование услуги"),
    )
    price = models.CharField(_("Цена"), blank=True, null=True, max_length=50)
    is_published = models.BooleanField(
        verbose_name=_("Услуга опубликована"), default=False
    )
    order = models.IntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")
        ordering = ["order"]

    def __str__(self):
        return f"{self.name}"
