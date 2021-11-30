from django.db.models import fields
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Stop, Trip
from .forms import StopForm

@login_required
def trips_index(request):
  trips = Trip.objects.filter(user=request.user)
  return render(request, 'trips/index.html', { 'trips': trips })

@login_required
def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  stop_form = StopForm()
  return render(request, 'trips/detail.html', { 'trip': trip, 'stop_form': stop_form })

@login_required
def add_stop(request, trip_id):
  form = StopForm(request.POST)
  if form.is_valid():
    new_stop = form.save(commit=False)
    new_stop.trip_id = trip_id
    new_stop.save()
  return redirect('trips_detail', trip_id=trip_id)

@login_required
def stops_delete(request, stop_id):
  stop = Stop.objects.get(id=stop_id)
  trip_id = stop.trip_id
  stop.delete()
  return redirect('trips_detail', trip_id=trip_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('trips_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class Home(LoginView):
  template_name = 'home.html'

class TripCreate(LoginRequiredMixin, CreateView):
  model = Trip
  fields = ['name', 'start', 'end', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TripUpdate(LoginRequiredMixin, UpdateView):
  model = Trip
  fields = ['name', 'start', 'end', 'description']

class TripDelete(LoginRequiredMixin, DeleteView):
  model = Trip
  success_url = '/trips/'

class StopUpdate(LoginRequiredMixin, UpdateView):
  model = Stop
  fields = ['name', 'arrive', 'depart', 'position', 'lodging', 'food', 'todos']

  def get_success_url(self):
      return reverse('trips_detail', kwargs={'trip_id': self.object.trip_id})