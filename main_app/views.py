from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trip

# Create your views here.
def home(request):
  return render(request, 'home.html')

def trips_index(request):
  trips = Trip.objects.all()
  return render(request, 'trips/index.html', { 'trips': trips })

def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  return render(request, 'trips/detail.html', { 'trip': trip })

class TripCreate(CreateView):
  model = Trip
  fields = '__all__'

class TripUpdate(UpdateView):
  model = Trip
  fields = '__all__'

class TripDelete(DeleteView):
  model = Trip
  success_url = '/trips/'