from django.contrib import admin
from .models import Todo, Faq, Statistics, Message


class BaseAdmin(admin.ModelAdmin):
    # Common functionality for other admins can be added here in the future
    pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("task", "status", "status_display")
    list_filter = ("status",)
    search_fields = ("task",)

    @admin.display(description="Task Status")
    def status_display(self, obj):
        return obj.get_status_display()


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")
    search_fields = ("question",)
    ordering = ("-created_at",)


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = (
        "pending_count",
        "in_progress_count",
        "completed_count",
        "archived_count",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "timestamp",
    )
