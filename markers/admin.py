"""Markers admin."""
from django.contrib.gis import admin
from .models import Marker


# Register your models here.
admin.site.register(Marker)
class MarkerAdmin(admin.GISModelAdmin):
    """Marker admin."""
    list_display = ('name', 'location')
