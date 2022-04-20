from django.contrib import admin

from .models import (
    AdditionalService,
    CategoryNews,
    CategoryService,
    Comment,
    Course,
    Gallery,
    News,
    OfferSlide,
    QuestionAnswer,
    Service,
    Worker,
    Сertificate,
)

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Новость в админке
#     """

#     list_display = (
#         "title",
#         "category_news",
#         "date",
#         "is_published",
#         "is_published_landing",
#     )
#     list_filter = (
#         "is_published",
#         "is_published_landing",
#     )


# @admin.register(CategoryNews)
# class CategoryNewsAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Новость в админке
#     """

#     list_display = (
#         "name",
#         "date_created",
#         "is_published",
#     )
#     list_filter = ("is_published",)


# @admin.register(QuestionAnswer)
# class QuestionAnswerAdmin(admin.ModelAdmin):
#     """
#     Админ панель
#     Вопрос ответ в админке
#     """

#     list_display = (
#         "question",
#         "date_updated",
#         "date_created",
#     )
#     list_filter = ("date_created",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Админ панель
    Новость в админке
    """

    list_display = (
        "name",
        "date_created",
        "is_published_landing",
    )
    list_filter = ("is_published_landing",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Админ панель
    Услуга
    """

    list_display = (
        "name",
        "category_service",
        "is_published",
    )
    list_filter = (
        "is_published",
        "category_service",
    )


@admin.register(CategoryService)
class CategoryServiceAdmin(admin.ModelAdmin):
    """
    Админ панель
    Категория услуги
    """

    list_display = (
        "name",
        "is_published",
        "order",
    )
    list_filter = ("is_published",)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    """
    Админ панель
    Сотрудник
    """

    list_display = (
        "name",
        "is_published_landing",
    )
    list_filter = ("is_published_landing",)


@admin.register(OfferSlide)
class OfferSlideAdmin(admin.ModelAdmin):
    """
    Админ панель
    Слайд предложения
    """

    list_display = (
        "title",
        "is_published",
    )
    list_filter = ("is_published",)


@admin.register(AdditionalService)
class AdditionalServiceAdmin(admin.ModelAdmin):
    """
    Админ панель
    Дополнительная услуга
    """

    list_display = (
        "name",
        "price",
        "is_published",
        "order",
    )
    list_filter = ("is_published",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Админ панель
    Дополнительная услуга
    """

    list_display = (
        "name",
        "price",
        "is_published",
        "order",
    )
    list_filter = ("is_published",)


@admin.register(Сertificate)
class СertificateAdmin(admin.ModelAdmin):
    """
    Админ панель
    Сертификаты
    """

    list_display = (
        "__str__",
        "is_published",
        "order",
    )
    list_filter = ("is_published",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """
    Админ панель
    Фото галлереи
    """

    list_display = (
        "__str__",
        "is_published",
        "order",
    )
    list_filter = ("is_published",)
