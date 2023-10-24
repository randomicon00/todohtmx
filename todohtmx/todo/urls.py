from django.urls import path
from .views import TodoAPIViewOld, TodoAPIView

urlpatterns = [
    # path('apiold/', TodoAPIViewOld.as_view(), name='api_todos_old'),
    path('api/', TodoAPIView.as_view(), name='api_todos'),
]
