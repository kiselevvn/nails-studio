from django.db import models
from django.utils.translation import gettext as _


class OfferSlide(
    models.Model,
):
    """
    Слайд предложения
    """

    title = models.CharField(
        verbose_name=_("Заголовок"),
        max_length=255,
    )
    text = models.TextField(
        verbose_name=_("Подзаголовок"), blank=True, null=True
    )
    picture = models.ImageField(_("Картинка"), blank=True, null=True)

    is_published = models.BooleanField(
        verbose_name=_("Является опубликованым"), default=False
    )
    order = models.IntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Слайд предложения")
        verbose_name_plural = _("Слайды предложений")
        ordering = ["order"]

    def __str__(self):
        return f"№{self.order} {self.title}"
