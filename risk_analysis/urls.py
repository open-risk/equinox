# Copyright (c) 2021 - 2022 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from django.urls import re_path
import views

app_name = 'workflow_explorer'

""" Custom URL's in addition to the admin url's

"""

urlpatterns = [
    re_path(r'^workflow_list$', views.WorkflowList.as_view(), name='workflow_list'),
    re_path(r'^playbook_list$', views.PlaybookList.as_view(), name='playbook_list'),
    re_path(r'^published$', views.PublishedWorkflowList.as_view(), name='published_workflow_list'),
    re_path(r'^batch_jobs$', views.BatchWorkflowList.as_view(), name='batch_workflow_list'),
    re_path(r'^objectives$', views.WorkflowObjectiveList.as_view(), name='workflow_objective_list'),
    re_path(r'^workflow_interactive/(?P<pk>\d+)$', views.workflow_interactive, name='workflow_interactive'),
    re_path(r'^workflow_debug/(?P<pk>\d+)$', views.workflow_cgi_debug, name='workflow_debug'),
    re_path(r'^workflow_calculate/(?P<pk>\d+)$', views.workflow_batch, name='workflow_calculate'),
    re_path(r'^workflow_view/(?P<pk>\d+)$', views.WorkflowView.as_view(), name='workflow_view'),
    re_path(r'^workflow_clone/(?P<pk>\d+)$', views.WorkflowClone.as_view(), name='workflow_clone'),
    re_path(r'^workflow_delete/(?P<pk>\d+)$', views.WorkflowDelete.as_view(), name='workflow_delete'),
    re_path(r'^workflow_create$', views.WorkflowCreate.as_view(), name='workflow_create'),
    re_path(r'^playbook_calculate/(?P<pk>\d+)$', views.playbook_calculate, name='playbook_calculate'),
    re_path(r'^scenario_list$', views.ScenarioList.as_view(), name='scenario_list'),
    re_path(r'^scenario_graphical_editor/(?P<pk>\d+)$', views.ScenarioEdit.as_view(), name='scenario_graphical_editor'),
    re_path(r'^scenario_form_editor/(?P<pk>\d+)$', views.scenario_editor, name='scenario_form_editor'),
]
