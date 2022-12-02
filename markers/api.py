"""Markers API URL Configuration."""
from rest_framework import routers
from markers.viewsets import MarkerViewSet

router = routers.DefaultRouter()
router.register(r'markers', MarkerViewSet)
#r prefix stands for "raw string"

urlpatterns = router.urls
