from django.db import models


class Faq(models.Model):
    message = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return f"< {self.message}>"

    def __str__(self) -> str:
        return self.message


class Todo(models.Model):
    task = models.CharField(max_length=255)

    def __repr__(self) -> str:
        return f"<Todo {self.task}>"

    def __str__(self) -> str:
        return self.task
