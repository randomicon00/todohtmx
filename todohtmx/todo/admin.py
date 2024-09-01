from django.contrib import admin
from .models import Todo, Faq, Statistics, Message


class TodoAdmin(admin.ModelAdmin):
    list_display = ("task", "status", "status_display")
    list_filter = ("status",)
    search_fields = ("task",)

    def status_display(self, obj):
        return obj.get_status_display()

    status_display.short_description = "Task Status"


class FaqAdmin(admin.ModelAdmin):
    list_display = ("question", "answer")
    search_fields = ("question",)
    ordering = ("-created_at",)


class StatisticsAdmin(admin.ModelAdmin):
    list_display = (
        "pending_count",
        "in_progress_count",
        "completed_count",
        "archived_count",
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "timestamp",
    )


admin.site.register(Todo, TodoAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Statistics, StatisticsAdmin)
admin.site.register(Message, MessageAdmin)
