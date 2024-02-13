from django.db import models
import datetime

# Create your models here.

CHOICE = (('danger', 'high'),('warning', 'normal'),('primary', 'low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(max_length=50, choices = CHOICE)
    duedate = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.title