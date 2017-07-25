from django.db import models

# Create your models here.
class ToDoListItem(models.Model):
    url = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    completed = models.BooleanField()
    date = models.DateField()
    userid = models.CharField(max_length=10)