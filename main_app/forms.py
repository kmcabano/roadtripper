from django.forms import ModelForm
from .models import Stop

class StopForm(ModelForm):
  class Meta:
    model = Stop
    fields = ['name', 'arrive', 'depart', 'position', 'lodging', 'food', 'todos']