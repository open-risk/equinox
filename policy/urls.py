# Copyright (c) 2020 - 2024 Open Risk (https://www.openriskmanagement.com)
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

from . import views

app_name = 'policy'

urlpatterns = [
    # HTML SINGLE PAGES
    re_path(r'^policy_overview$', views.PolicyOverview.as_view(), name='Policy_overview'),

    # DATAFLOW VIEWS
    re_path(r'^dataflow/categories$', views.DataFlowCategoriesView.as_view(), name='DataFlow_categories'),

    re_path(r'^dataflow/(?P<pk>\d+)$', views.DataFlowListView.as_view(), name='DataFlow'),
    re_path(r'^dataflow/(?P<slug>[-\w]+)$', views.DataFlowListView.as_view(), name='DataFlow2'),
    re_path(r'^dataflow/slice/(?P<slug>[-\w]+)$', views.DataFlowSliceView.as_view(), name='DataFlow_slice'),
    re_path(r'^dataflow/filter/(?P<identifier>\w+)/(?P<region>\w+)/(?P<color>\w+)', views.DataFlowFilterView.as_view(),
            name='DataFlow_filter'),
    re_path(r'^dataflow/country/(?P<slug>[-\w]+)$', views.DataFlowCountryView.as_view(), name='DataFlow_country'),
    re_path(r'^dataflow/country_aggregate/(?P<slug>[-\w]+)$', views.DataFlowCountryAggregateView.as_view(),
            name='DataFlow_country_aggregate'),

    # DATASERIES VIEWS
    re_path(r'^dataseries/(?P<pk>\d+)$', views.DataSeriesView.as_view(), name='DataSeries'),
    re_path(r'^dataseries/(?P<slug>[-\w.]+)$', views.DataSeriesView.as_view(), name='DataSeries2'),
    re_path(r'^dataseries/metrics/(?P<slug>[-\w.]+)$', views.DSMetricsView.as_view(), name='Metrics'),
    re_path(r'^dataseries/all/(?P<color>\w+)$', views.DataSeriesListView.as_view(), name='DataSeries_filter'),
    re_path(r'^dataseries/plot/(?P<slug>[-\w.]+)$', views.DSPlotView.as_view(), name='Plot'),

    # STATISTICS VIEWS
    re_path(r'^statistics/country/table/(?P<activity>[-\w]+)$', views.StatsCountryTableView.as_view(),
            name='StatsCountryTable'),
    re_path(r'^statistics/country/histogram/(?P<activity>\w+)/(?P<stat>\w+)$',
            views.StatsCountryHistogramView.as_view(), name='StatsCountryHistogram'),
]
