from django.db import models
from django.utils.translation import gettext as _


class Gallery(models.Model):
    """
    Галерея
    """

    picture = models.ImageField(verbose_name=_("Изображение"))
    description = models.TextField(
        verbose_name=_("Краткое описание"), blank=True, null=True
    )
    is_published = models.BooleanField(
        verbose_name=_("Является опубликованым"), default=False
    )
    worker = models.ForeignKey(
        "content.Worker",
        related_name="pictures",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    order = models.IntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Галерея")
        verbose_name_plural = _("Фото Галереи")
        ordering = ["order"]

    def __str__(self):
        return f"Фото Галереи"
