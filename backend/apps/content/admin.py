from django.contrib import admin

from .models import (
    AdditionalService,
    CategoryService,
    Comment,
    Course,
    Gallery,
    OfferSlide,
    Service,
    Worker,
    Сertificate,
)




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Админ панель
    Новость в админке
    """

    list_display = (
        "name",
        "category",
        "date_created",
        # "is_published_landing",
    )
    list_filter = (
        # "is_published_landing",
        "category",
    )


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
    Фото Галереи
    """

    list_display = (
        "__str__",
        "is_published",
        "order",
    )
    list_filter = ("is_published",)
