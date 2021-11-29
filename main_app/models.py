from typing import Text
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.fields import TextField
from django.urls import reverse

POSITIONS = (
  ('O', 'Origin'),
  ('S', "Stop"),
  ('D', 'Destination')
)

class Trip(models.Model):
  name = models.CharField(max_length=100)
  start = models.DateField()
  end = models.DateField()
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("trips_detail", kwargs={"trip_id": self.id})
  
class Stop(models.Model):
  name = models.CharField(max_length=100)
  arrive = models.DateField(null=True, blank=True)
  depart = models.DateField(null=True, blank=True)
  position = models.CharField(
    max_length=1,
    choices=POSITIONS,
    default = POSITIONS[1][1]
  )
  lodging = models.CharField(max_length=100, null=True, blank=True)
  food = TextField(max_length=500)
  todos = TextField(max_length=2000)

  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

  def __str__(self):
      return self.name
  