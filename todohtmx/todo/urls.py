from django.urls import path
from .views import TodoAPIView

urlpatterns = [
    # api/todo
    path("api/", TodoAPIView.as_view(), name="api_todos"),
]
