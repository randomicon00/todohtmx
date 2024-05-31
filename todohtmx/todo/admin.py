from django.contrib import admin
from .models import Todo, Faq, Statistics


class TodoAdmin(admin.ModelAdmin):
    list_display = ("task", "status", "status_display")
    list_filter = ("status",)
    search_fields = ("task",)

    def status_display(self, obj):
        return obj.get_status_display()

    status_display.short_description = "Status"


class FaqAdmin(admin.ModelAdmin):
    list_display = ("task", "status", "status_display")
    search_fields = ("question",)


class StatisticsAdmin(admin.ModelAdmin):
    list_display = (
        "pending_count",
        "in_progress_count",
        "completed_count",
        "archived_count",
    )


admin.site.register(Todo)
admin.site.register(Faq)
admin.site.register(Statistics)
