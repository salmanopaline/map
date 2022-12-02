"""Markers urls."""

from django.urls import path
from .views import MarkersMapView
from .views import allpoints

app_name = 'markers'

urlpatterns = [
    path('map/', MarkersMapView.as_view()),
    path('mappoints/', allpoints, name='allpoints'),
]