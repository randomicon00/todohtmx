from django.urls import path
from .views import TodoAPIView, FaqAPIView, StatisticsAPIView

urlpatterns = [
    path("api/", TodoAPIView.as_view(), name="todos_api"),
    path("api/faq", FaqAPIView.as_view(), name="faq_api"),
    path("api/stats", StatisticsAPIView.as_view(), name="stats_api"),
    # TODO use web sockets and htmx to build a live chat support app
    # TODO Add consumer and middleware logic
    # path("api/chat", consumers.ChatConsumer.as_asgi(), name="stats_api"),
    # path("api/chat", ChatAPIView.as_view(), name="chat_api"),
    # add more paths here
]
