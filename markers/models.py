from django.db import models

# Create your models here.

"""Markers models."""
from django.contrib.gis.db import models

class Marker(models.Model):
    """A marker with name and location.
    location == Stores a Point """
    name = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        """The __str__ method returns a string indicating the object's state."""
        """Return string representation."""
        return self.name
