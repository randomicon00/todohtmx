from django.urls import path
from .views import TodoAPIView, FaqAPIView, StatisticsAPIView
from .consumers import ChatConsumer

# API URL patterns
urlpatterns = [
    path("api/", TodoAPIView.as_view(), name="todos_api"),
    path("api/faq/", FaqAPIView.as_view(), name="faq_api"),
    path("api/stats/", StatisticsAPIView.as_view(), name="stats_api"),
]
