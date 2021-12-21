from django.conf.urls import url
from results_explorer import views

app_name = 'results_explorer'

urlpatterns = [
    url(r'^ghg_reduction$', views.ghg_reduction, name='ghg_reduction'),
    url(r'^result_types$', views.result_types, name='result_types'),
    url(r'^results_view/(?P<pk>\d+)$', views.results_view, name='results_view'),
    url(r'^visualization_view/(?P<pk>\d+)$', views.visualization_view, name='visualization_view'),
]
