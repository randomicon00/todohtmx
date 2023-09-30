from django.db import models

# Create your models here.
class Todo:
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    #created = models.DateTimeField(auto_now_add=True)
    #edited = models.DateTimeField(auto_now=True)