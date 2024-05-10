from django.db import models
from django.db.models import Count


class Todo(models.Model):
    task = models.CharField(max_length=255)

    STATUS_CHOICES = [
        (1, "Pending"),
        (2, "In Progress"),
        (3, "Completed"),
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

    def update_statistics(self):
        self.pending_count = Todo.objects.filter(status=1).count()
        self.in_progress_count = Todo.objects.filter(status=2).count()
        self.completed_count = Todo.objects.filter(status=3).count()
        self.save()

    def __repr__(self) -> str:
        return f"<Statistics Pending: {self.pending_count}, In Progress: {self.in_progress_count}, Completed: {self.completed_count}>"

    def __str__(self) -> str:
        return f"Pending: {self.pending_count}, In Progress: {self.in_progress_count}, Completed: {self.completed_count}"
