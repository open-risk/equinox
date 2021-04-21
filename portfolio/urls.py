from django.urls import path
from djgeojson.views import GeoJSONLayerView

from .views import PFMapView

app_name = "portfolio"

urlpatterns = [
    path("", PFMapView.as_view()),
    path(r'^geojson$', GeoJSONLayerView.as_view(model=MushroomSpot), name='data'),
]
