from django.db import models
from django.db.models import Count, Q


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
        return f"<Todo {self.task}> Status: {self.get_status_display()}"

    def __str__(self) -> str:
        return f"{self.task} - {self.get_status_display()}"


class Faq(model.Models):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __repr__(self) -> str:
        return f"<Faq {self.task}>"

    def __str__(self) -> str:
        return self.question


class Statistics(models.Model):
    pending_count = models.IntegerField(default=0)
    in_progress_count = models.IntegerField(default=0)
    completed_count = models.IntegerField(default=0)
    archived_count = models.IntegerField(default=0)

    def update_stats(self):
        # Aggregate counts for each status
        counts = Todo.objects.aggregate(
            pending_count=Count("id", filter=Q(status=1)),
            in_progress_count=Count("id", filter=Q(status=2)),
            completed_count=Count("id", filter=Q(status=3)),
            archived_count=Count("id", filter=Q(status=4)),
        )

        # Update the model's fields with the aggregated counts
        self.pending_count = counts["pending_count"]
        self.in_progress_count = counts["in_progress_count"]
        self.completed_count = counts["completed_count"]
        self.archived_count = counts["archived_count"]

        # Save the updated counts to the database
        self.save()

    def __repr__(self) -> str:
        return f"<Statistics Pending: {self.pending_count}, In Progress: {self.in_progress_count}, Completed: {self.completed_count}, Archived: {self.archived_count}>"

    def __str__(self) -> str:
        return f"Pending: {self.pending_count}, In Progress: {self.in_progress_count}, Completed: {self.completed_count}, Archived: {self.archived_count}"
