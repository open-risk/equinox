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
from reporting import views

app_name = 'reporting'

"""
Custom reporting URL's (in addition to the admin url's) that implement the Equinox reporting functionality

"""

urlpatterns = [
    re_path(r'^portfolio_overview$', views.portfolio_overview, name='portfolio_overview'),
    re_path(r'^ghg_reduction$', views.ghg_reduction, name='ghg_reduction'),
    re_path(r'^gpc_report$', views.gpc_report, name='gpc_report'),
    re_path(r'^gpp_report$', views.gpp_report, name='gpp_report'),
    re_path(r'^contractor_nuts3_map$', views.contractor_nuts3_map, name='contractor_nuts3_map'),
    re_path(r'^manager_nuts3_map$', views.manager_nuts3_map, name='manager_nuts3_map'),
    re_path(r'^project_nuts3_map$', views.project_nuts3_map, name='project_nuts3_map'),
    re_path(r'^portfolio_summary/(?P<pk>\d+)$', views.portfolio_summary, name='portfolio_summary'),
    re_path(r'^portfolio_stats/(?P<pk>[-\w.]+)$', views.portfolio_stats_view, name='portfolio_stats'),
    re_path(r'^portfolio_aggregates$', views.portfolio_aggregates, name='portfolio_aggregates'),
    re_path(r'^pcaf_mortgage_report$', views.pcaf_mortgage_report, name='pcaf_mortgage_report'),
    # re_path(r'^result_types$', views.result_types, name='result_types'),
    re_path(r'^results_view/(?P<pk>\d+)$', views.results_view, name='results_view'),
    re_path(r'^visualization_country$', views.visualization_country, name='visualization_country'),
    re_path(r'^visualization_sector$', views.visualization_sector, name='visualization_sector'),
]
