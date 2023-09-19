import datetime
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=30)
  description = models.CharField(max_length=500)
  date_created = datetime.datetime.now()
  due_date = models.DateField()

  def __str__(self):
    return self.title