from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView


class PFMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"
