from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return f"<Todo {self.task}>"

    def __str__(self) -> str:
        return self.task
