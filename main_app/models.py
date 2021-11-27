from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Trip(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateField()
  end = models.DateField()
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name