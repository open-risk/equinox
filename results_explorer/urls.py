from django.urls import re_path
from results_explorer import views

app_name = 'results_explorer'

urlpatterns = [
    re_path(r'^ghg_reduction$', views.ghg_reduction, name='ghg_reduction'),
    re_path(r'^gpc_report$', views.gpc_report, name='gpc_report'),
    re_path(r'^result_types$', views.result_types, name='result_types'),
    re_path(r'^results_view/(?P<pk>\d+)$', views.results_view, name='results_view'),
    re_path(r'^visualization_view/(?P<pk>\d+)$', views.visualization_view, name='visualization_view'),
]
