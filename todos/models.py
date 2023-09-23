import datetime
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=30, null=True)
  description = models.CharField(max_length=500, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  date_updated = models.DateTimeField(auto_now=True, null=True)
  due_date = models.DateTimeField(null=True)
  is_completed = models.BooleanField(default=False, null=True)

  def __str__(self):
    return self.title
  