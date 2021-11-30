from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('trips/', views.trips_index, name='trips_index'),
  path('trips/<int:trip_id>/', views.trips_detail, name='trips_detail'),
  path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
  path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
  path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
  path('trips/<int:trip_id>/add_stop/', views.add_stop, name='add_stop'),
  path('stops/<int:stop_id>/delete', views.stops_delete, name='stops_delete'),
  path('stops/<int:pk>/update', views.StopUpdate.as_view(), name='stops_update'),
  
]