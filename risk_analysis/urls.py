from django.conf.urls import url
import views

app_name = 'workflow_explorer'

urlpatterns = [
    url(r'^workflow_list$', views.WorkflowList.as_view(), name='workflow_list'),
    url(r'^playbook_list$', views.PlaybookList.as_view(), name='playbook_list'),
    url(r'^published$', views.PublishedWorkflowList.as_view(), name='published_workflow_list'),
    url(r'^batch_jobs$', views.BatchWorkflowList.as_view(), name='batch_workflow_list'),
    url(r'^objectives$', views.WorkflowObjectiveList.as_view(), name='workflow_objective_list'),
    url(r'^workflow_interactive/(?P<pk>\d+)$', views.workflow_interactive, name='workflow_interactive'),
    url(r'^workflow_debug/(?P<pk>\d+)$', views.workflow_cgi_debug, name='workflow_debug'),
    url(r'^workflow_calculate/(?P<pk>\d+)$', views.workflow_batch, name='workflow_calculate'),
    url(r'^workflow_view/(?P<pk>\d+)$', views.WorkflowView.as_view(), name='workflow_view'),
    url(r'^workflow_clone/(?P<pk>\d+)$', views.WorkflowClone.as_view(), name='workflow_clone'),
    url(r'^workflow_delete/(?P<pk>\d+)$', views.WorkflowDelete.as_view(), name='workflow_delete'),
    url(r'^workflow_create$', views.WorkflowCreate.as_view(), name='workflow_create'),
    url(r'^playbook_calculate/(?P<pk>\d+)$', views.playbook_calculate, name='playbook_calculate'),
    url(r'^scenario_list$', views.ScenarioList.as_view(), name='scenario_list'),
    url(r'^scenario_graphical_editor/(?P<pk>\d+)$', views.ScenarioEdit.as_view(), name='scenario_graphical_editor'),
    url(r'^scenario_form_editor/(?P<pk>\d+)$', views.scenario_editor, name='scenario_form_editor'),
]
