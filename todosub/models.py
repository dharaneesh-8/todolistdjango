from django.db import models

# Create your models here.

class Todoapp(models.Model):
    task = models.TextField()
    description = models.TextField()

class DeleteTodoApp(models.Model):
    task = models.TextField()
    description = models.TextField()