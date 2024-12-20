from django.contrib import admin
from .models import Todo, Faq, Statistics


class BaseAdmin(admin.ModelAdmin):
    pass


class StatusDisplayMixin:
    @admin.display(description="Task Status")
    def status_display(self, obj):
        return obj.get_status_display()


@admin.register(Todo)
class TodoAdmin(BaseAdmin, StatusDisplayMixin):
    list_display = ("task", "status", "status_display")
    list_filter = ("status",)
    search_fields = ("task",)


@admin.register(Faq)
class FaqAdmin(BaseAdmin):
    list_display = ("question", "answer", "created_at", "updated_at")
    search_fields = ("question",)
    ordering = ("created_at",)


@admin.register(Statistics)
class StatisticsAdmin(BaseAdmin):
    list_display = (
        "pending_count",
        "in_progress_count",
        "completed_count",
        "archived_count",
    )
