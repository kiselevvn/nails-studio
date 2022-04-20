from apps.content.forms import MessageForm
from apps.content.models import (
    AdditionalService,
    CategoryService,
    Comment,
    Course,
    Gallery,
    OfferSlide,
    Worker,
    Сertificate,
)
from django.views.generic import TemplateView


class LandingView(TemplateView):
    """
    Лэндиннг сайта
    """

    template_name = "landing.html"

    def get_context_data(self, **kwargs):
        """
        Контекст данных лэндинга
        """
        data = super().get_context_data(**kwargs)
        data["form"] = MessageForm()

        data["category_service"] = CategoryService.objects.filter(
            is_published=True
        )
        data["additional_services"] = AdditionalService.objects.filter(
            is_published=True
        )
        data["offer_slides"] = OfferSlide.objects.filter(is_published=True)
        data["workers"] = Worker.objects.filter(is_published_landing=True)
        data["courses"] = Course.objects.filter(is_published=True)
        data["certificates"] = Сertificate.objects.filter(is_published=True)
        data["gallery_photo"] = Gallery.objects.filter(is_published=True)
        return data
