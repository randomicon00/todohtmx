from django.db import models
from django.db.models import Count, Q
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Todo(models.Model):
    task = models.TextField()

    STATUS_PENDING = 1
    STATUS_IN_PROGRESS = 2
    STATUS_COMPLETED = 3
    STATUS_ARCHIVED = 4

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_IN_PROGRESS, "In Progress"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __repr__(self) -> str:
        return f"<Task: {self.task}, Status: {self.get_status_display()}>"

    def __str__(self) -> str:
        return f"Task: {self.task}, Status: {self.get_status_display()}"


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __repr__(self) -> str:
        return f"<Question: {self.question}, Answer: {self.answer}>"

    def __str__(self) -> str:
        return self.question


class Statistics(models.Model):
    pending_count = models.IntegerField(default=0)
    in_progress_count = models.IntegerField(default=0)
    completed_count = models.IntegerField(default=0)
    archived_count = models.IntegerField(default=0)

    def update(self):
        status_counts = Todo.objects.values("status").annotate(count=Count("id"))
        count_map = {status: 0 for status, _ in Todo.STATUS_CHOICES}

        for item in status_counts:
            count_map[item["status"]] = item["count"]

        self.pending_count = count_map[Todo.STATUS_PENDING]
        self.in_progress_count = count_map[Todo.STATUS_IN_PROGRESS]
        self.completed_count = count_map[Todo.STATUS_COMPLETED]
        self.archived_count = count_map[Todo.STATUS_ARCHIVED]

        self.save()

    def __repr__(self) -> str:
        return (
            f"<Statistics Pending: {self.pending_count}, In Progress: {self.in_progress_count}, "
            f"Completed: {self.completed_count}, Archived: {self.archived_count}>"
        )

    def __str__(self) -> str:
        return (
            f"Pending: {self.pending_count}, In Progress: {self.in_progress_count}, "
            f"Completed: {self.completed_count}, Archived: {self.archived_count}"
        )


@receiver(post_save, sender=Todo)
@receiver(post_delete, sender=Todo)
def update_statistics(sender, instance, **kwargs):
    statistics, _ = Statistics.objects.get_or_create(pk=1)
    statistics.update()
