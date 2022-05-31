from django.db import models
from django.utils.translation import gettext as _


class Comment(
    models.Model,
):
    """
    Модель Сообщение
    """

    MESSAGE = 0
    COYRSE_BUY = 1
    CATEGORIES = [(MESSAGE, "Сообщение"), (COYRSE_BUY, "Курсы")]

    category = models.IntegerField(
        _("Категория сообщения"), default=0, choices=CATEGORIES
    )
    course = models.ForeignKey(
        "content.Course",
        verbose_name=_("Курс"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(
        verbose_name=_("Имя"),
        max_length=255,
    )
    phone = models.CharField(
        verbose_name=_("Номер телефона"), max_length=25
    )
    text = models.TextField(verbose_name=_("Сообщение"), blank=True, null=True)
    email = models.EmailField(
        _("Электронная почта"), max_length=254
    )
    # is_published_landing = models.BooleanField(
    #     verbose_name=_("Отзыв опубликован"), default=False
    # )
    date_created = models.DateTimeField(
        verbose_name=_("Дата создания"), auto_now_add=True
    )

    class Meta:
        verbose_name = _("Сообщение")
        verbose_name_plural = _("Сообщения")
        ordering = ["-date_created"]

    def __str__(self):
        return f"{self.name} " + f"(дата создания: {self.date_created}) "
