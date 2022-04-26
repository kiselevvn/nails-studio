from django.views.generic import DetailView

from ..forms import MessageForm
from ..models import Course


class CourseBuyFormView(DetailView):
    """
    Купить курс
    """

    model = Course
    template_name = "course-buy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MessageForm()
        return context
