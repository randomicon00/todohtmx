from django.urls import path
from .views import TodoAPIView, FaqAPIView, StatisticsAPIView

urlpatterns = [
    path("api/todos", TodoAPIView.as_view(), name="todos_api"),
    path("api/faq/", FaqAPIView.as_view(), name="faq_api"),
    path("api/stats/", StatisticsAPIView.as_view(), name="stats_api"),
]
