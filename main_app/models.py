from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from datetime import date

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
  food = ArrayField(models.CharField(max_length=200), null=True, blank=True)
  todos = ArrayField(models.CharField(max_length=200, null=True, blank=True))

  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

  # def __str__(self):
  #     return f"{self.get_position_display()}"
  