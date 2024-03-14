from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # add more paths here
    path('todo/', include('todo.urls')),
]
