from django.urls import path
from .views import TodoAPIViewOld, TodoAPIView

urlpatterns = [
    path('api/', TodoAPIView.as_view(), name='api_todos'),
]
