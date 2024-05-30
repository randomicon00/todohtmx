from django.contrib import admin
from .models import Todo, Faq, Statistics


class TodoAdmin(admin.ModelAdmin):
    pass


class FaqAdmin(admin.ModelAdmin):
    pass


class StatisticsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Todo)
admin.site.register(Faq)
admin.site.register(Statistics)
