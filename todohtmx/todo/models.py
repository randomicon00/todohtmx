from django.db import models


class Todo(models.Model):
    # Task description
    task = models.CharField(max_length=255)

    # Status choices
    STATUS_CHOICES = [
        (1, "Pending"),
        (2, "In Progress"),
        (3, "Completed"),
    ]

    # Task status
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


# TODO Add a model for managing statistics
