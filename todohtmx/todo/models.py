from django.db import models


class Todo(models.Model):
    task = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return f"<Todo {self.task}>"

    def __str__(self) -> str:
        return self.task


class FAQ(model.Models):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __repr__(self) -> str:
        return f"<FAQ {self.task}>"

    def __str__(self) -> str:
        return self.question
