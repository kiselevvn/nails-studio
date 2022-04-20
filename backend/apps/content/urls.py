from django.urls import path

from .views import MessageFormView, ThanksView

urlpatterns = [
    path("message/", MessageFormView.as_view(), name="message"),
    path("thanks/", ThanksView.as_view(), name="thanks"),
    # path("news/", NewsListView.as_view(), name="news-list"),
    # path("news/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
]
