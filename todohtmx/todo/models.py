from django.db import models


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __repr__(self) -> str:
        return f"<Todo {self.question}>"

    def __str__(self) -> str:
        return self.question


class Todo(models.Model):
    task = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return f"<Todo {self.task}>"

    def __str__(self) -> str:
        return self.task
