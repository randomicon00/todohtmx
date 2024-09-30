from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")),
    # Add more app-specific or view-specific routes here as needed.
]
