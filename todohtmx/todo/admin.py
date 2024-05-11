from django.contrib import admin
from .models import Todo, Faq, Statistics

admin.site.register(Todo)
admin.site.register(Faq)
admin.site.register(Statistics)
