from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trip
from .forms import StopForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def trips_index(request):
  trips = Trip.objects.all()
  return render(request, 'trips/index.html', { 'trips': trips })

def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  stop_form = StopForm()
  return render(request, 'trips/detail.html', { 'trip': trip, 'stop_form': stop_form })

def add_stop(request, trip_id):
  form = StopForm(request.POST)
  if form.is_valid():
    new_stop = form.save(commit=False)
    new_stop.trip_id = trip_id
    new_stop.save()
  return redirect('trips_detail', trip_id=trip_id)

class TripCreate(CreateView):
  model = Trip
  fields = '__all__'

class TripUpdate(UpdateView):
  model = Trip
  fields = '__all__'

class TripDelete(DeleteView):
  model = Trip
  success_url = '/trips/'