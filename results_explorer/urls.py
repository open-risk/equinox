from django.conf.urls import url
from . import views

app_name = 'results_explorer'

urlpatterns = [
    url(r'^$', views.ResultsList.as_view(), name='results_list'),
    url(r'^about$', views.About.as_view(), name='results_about'),
    url(r'^result_types$', views.result_types, name='result_types'),
    url(r'^results_list$', views.ResultsList.as_view(), name='results_list'),
    url(r'^result_group_list$', views.ResultGroupList.as_view(), name='result_group_list'),
    url(r'^results_view/(?P<pk>\d+)$', views.results_view, name='results_view'),
    url(r'^result_group_view/(?P<pk>\d+)$', views.result_group_view, name='result_group_view'),
    url(r'^result_group_logfiles/(?P<pk>\d+)$', views.result_group_logfiles, name='result_group_logfiles'),
    url(r'^single_period_metrics/(?P<pk>\d+)$', views.single_period_metrics, name='single_period_metrics'),
    # url(r'^objectives$', views.VisualizationObjectiveList.as_view(), name='Visualization_objective_list'),
    # url(r'^about$', views.About.as_view(), name='Visualization_about'),
    url(r'^loss_dist_1P$', views.loss_distribution_1p_view, name='loss_distribution_1P_view'),
    url(r'^loss_dist_MP$', views.loss_distribution_mp_view, name='loss_distribution_MP_view'),
    url(r'^visualization_list$', views.VisualizationList.as_view(), name='Visualization_list'),
    url(r'^visualization_interactive/(?P<pk>\d+)$', views.Visualization_interactive, name='Visualization_interactive'),
    url(r'^visualization_view/(?P<pk>\d+)$', views.Visualization_view, name='Visualization_view'),
    url(r'^visualization_clone/(?P<pk>\d+)$', views.VisualizationClone.as_view(), name='Visualization_clone'),
    url(r'^visualization_delete/(?P<pk>\d+)$', views.VisualizationDelete.as_view(), name='Visualization_delete'),
    url(r'^visualization_create$', views.VisualizationCreate.as_view(), name='Visualization_create'),
]
