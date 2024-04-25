from django.urls import path
from .views import TodoAPIView

urlpatterns = [
    path("api/", TodoAPIView.as_view(), name="api_todos"),
    path("api/faqs", FAQAPIView.as_view(), name="api_faq"),
    # add more app paths here
]
