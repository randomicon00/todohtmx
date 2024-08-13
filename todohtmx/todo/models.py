from django.db import models
from django.db.models import Count, Q
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Todo(models.Model):
    task = models.TextField()

    STATUS_CHOICES = [
        (1, "Pending"),
        (2, "In Progress"),
        (3, "Completed"),
        (4, "Archived"),
    ]

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __repr__(self) -> str:
        return f"<Todo Task: {self.task}, Status: {self.get_status_display()}>"

    def __str__(self) -> str:
        return f"Task: {self.task}, Status: {self.get_status_display()}"


class Faq(model.Models):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __repr__(self) -> str:
        return f"<Faq Question: {self.question}, Answer: {self.answer}>"

    def __str__(self) -> str:
        return self.question


class Statistics(models.Model):
    pending_count = models.IntegerField(default=0)
    in_progress_count = models.IntegerField(default=0)
    completed_count = models.IntegerField(default=0)
    archived_count = models.IntegerField(default=0)

    def update_stats(self):
        counts = Todo.objects.aggregate(
            pending_count=Count("id", filter=Q(status=1)),
            in_progress_count=Count("id", filter=Q(status=2)),
            completed_count=Count("id", filter=Q(status=3)),
            archived_count=Count("id", filter=Q(status=4)),
        )

        self.pending_count = counts["pending_count"]
        self.in_progress_count = counts["in_progress_count"]
        self.completed_count = counts["completed_count"]
        self.archived_count = counts["archived_count"]

        self.save()

    def __repr__(self) -> str:
        return f"<Statistics Pending: {self.pending_count}, In Progress: {self.in_progress_count}, Completed: {self.completed_count}, Archived: {self.archived_count}>"

    def __str__(self) -> str:
        return f"Pending: {self.pending_count}, In Progress: {self.in_progress_count}, Completed: {self.completed_count}, Archived: {self.archived_count}"


class Message(models.Models):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"<Message Content: {self.content}, TimeStamp: {self.timestamp}>"

    def __str__(self):
        return f"Content: {self.content}, TimeStamp: {self.timestamp}"


@receiver(post_save, sender=Todo)
@receiver(post_detele, sender=Todo)
def update_statistics(sender, instance, **kwargs):
    stats, created = Statistics.objects.get_or_create(pk=1)
    if created:
        initial_counts = {
            "pending_count": 0,
            "in_progress_count": 0,
            "completed_count": 0,
            "archived_count": 0,
        }
        for key, value in initial_counts.items():
            setattr(stats, key, value)
    stats.update_stats()
