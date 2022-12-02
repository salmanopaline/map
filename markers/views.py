"""Markers view."""

from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Marker

# Create your views here.

class MarkersMapView(TemplateView):
    # Markers map view.
    template_name = 'map.html'

def allpoints(request):
    allpoints = Marker.objects.all()
    names = [i for i in allpoints]
    name = [i.name for i in allpoints]
    loc = [i.location for i in names]
    xy = [[j for j in i] for i in loc]
    lat = [i[1] for i in xy]
    long = [i[0] for i in xy]
    return render(request, 'allpoints.html', {
        'allpoints':allpoints, 'name':name, 'lat':lat, 'long':long
    }) 
    