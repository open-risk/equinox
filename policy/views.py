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

import json

from django.conf import settings
from django.db.models import Q
from django.views.generic import DetailView, ListView
from policy.models import DashBoardParams
from policy.models import DataFlow
from policy.models import DataSeries
from policy.models import GeoSlice

from policy.settings import country_dict, activities_short, activities, stat_strings


#
# 0 General Views
#

# Policy Data Overview
class PolicyOverview(ListView):
    """
    Retrieve all dataflow objects and construct content description text for help display
    """

    model = DataFlow
    template_name = 'policy/policy_overview.html'

    def get_context_data(self, **kwargs):

        object_list = DataFlow.objects.all()
        statistics = {}
        total_datasets = 0
        tracked_datasets = 0
        live_datasets = 0
        for df in object_list:
            total_datasets += df.oxford_n
            if df.tracked:
                tracked_datasets += df.dashboard_n
                live_datasets += df.live_n

        statistics['total_datasets'] = total_datasets
        statistics['tracked_datasets'] = tracked_datasets
        statistics['live_datasets'] = live_datasets

        context = super(ListView, self).get_context_data(**kwargs)
        context.update({'statistics': json.dumps(statistics)})
        return context


#
# 1 DataFlow Categories View
#

class DataFlowCategoriesView(ListView):
    """
    Retrieve all dataflow objects and construct content description text. Useful for help displays

    """
    model = DataFlow
    template_name_suffix = '_categories'

    def get_context_data(self, **kwargs):
        parameter_list = DashBoardParams.objects.all().first()

        freshness = {}
        statistics = {}

        try:
            statistics['total_datasets'] = parameter_list.total_datasets
            statistics['tracked_datasets'] = parameter_list.tracked_datasets
            statistics['live_datasets'] = parameter_list.live_datasets

            freshness['red'] = parameter_list.red_datasets
            freshness['orange'] = parameter_list.orange_datasets
            freshness['yellow'] = parameter_list.yellow_datasets
            freshness['gray'] = parameter_list.gray_datasets
        except:
            statistics['total_datasets'] = 0
            statistics['tracked_datasets'] = 0
            statistics['live_datasets'] = 0

            freshness['red'] = 0
            freshness['orange'] = 0
            freshness['yellow'] = 0
            freshness['gray'] = 0

        context = super(ListView, self).get_context_data(**kwargs)
        context.update({'freshness': json.dumps(freshness)})
        context.update({'statistics': json.dumps(statistics)})
        context.update({'region': 'all'})
        context.update({'color': 'all'})
        return context


class DataFlowListView(DetailView):
    """
    2a Dataflow Detail View (List of All Data Series)
    class DataFlowView(LoginRequiredMixin, DetailView)
    """

    model = DataFlow
    template_name_suffix = '_detail'
    slug_field = 'identifier'

    def get_object(self):
        dataflow = super(DataFlowListView, self).get_object()
        return dataflow

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataflow = super(DataFlowListView, self).get_object()
        df = dataflow.identifier
        # Retrieve **all dataseries** objects and filter for selected dataflow
        series_list = DataSeries.objects.filter(df_name=df)
        # Construct content description for help display
        content_data = {}
        for ds in series_list:
            content_data[ds.pk] = "<h4>" + ds.title + "</h4>" + "<i>" + ds.title_long + "</i>"
        context.update({'series_list': series_list})
        context.update({'content_data': json.dumps(content_data)})
        return context


class DataFlowDimensionsView(DetailView):
    model = DataFlow
    template_name_suffix = '_dimensions'
    slug_field = 'name'
    pass


class DataFlowGeoSliceView(DetailView):
    """
    2c Dataflow Geo Slice View (For GEO tagged DF's produce a slice for graphing)
    """

    model = DataFlow
    template_name_suffix = '_geoslice'
    slug_field = 'name'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataflow = super(DataFlowGeoSliceView, self).get_object()
        geoslices = GeoSlice.objects.filter(df_name=dataflow.name)
        dataset = []
        for geo in geoslices:
            dataset.append({'id': geo.identifier, 'desc': geo.long_desc, 'location_no': len(geo.dataset_id)})
        # construct dimensions structure for selector view
        obj = dataflow.dimensions
        for dimension in obj:
            dimension['DimString'] = dimension['DimDescription'].replace(" ", "_").replace("/", "_")
        context.update({'geoslices': json.dumps(dataset)})
        context.update({'dimension_list': obj})
        # context.update({'root_view': root_view})
        return context


class DataFlowSliceView(DetailView):
    """
    2d Dataflow Slice View (Slicing a Dataflow along some Dataflow Dimension)
    class DataFlowView(LoginRequiredMixin, DetailView)
    The view passes all the DF JSON dataseries list to the template to be sliced there
    """

    model = DataFlow
    template_name_suffix = '_slice'
    slug_field = 'identifier'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataflow = super(DataFlowSliceView, self).get_object()

        # construct dimensions structure for selector view
        obj = dataflow.dimensions
        for dimension in obj:
            dimension['DimString'] = dimension['DimDescription'].replace(" ", "_").replace("/", "_")

        context.update({'dataseries': json.dumps(dataflow.dataset_id)})
        context.update({'dimension_list': obj})
        # context.update({'root_view': root_view})
        return context


class DataFlowFilterView(DetailView):
    """
    2e Dataflow Filter View (Filtering the DS of a Dataflow using some filter e.g. color)
    The view passes all filtered DF JSON dataseries to the template
    """
    model = DataFlow
    template_name_suffix = '_filter'

    # slug_field = 'identifier'

    def get_object(self):
        # Call the superclass
        identifier = self.kwargs['identifier']
        # dataflow = super(DataFlowFilterView, self).get_object()
        dataflow = DataFlow.objects.get(identifier=identifier)
        return dataflow

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)

        identifier = self.kwargs['identifier']
        color = self.kwargs['color']
        region = self.kwargs['region']
        # dataflow = super(DataFlowFilterView, self).get_object()
        dataflow = DataFlow.objects.get(identifier=identifier)
        df = dataflow.identifier

        series_list = []
        if region == 'all':
            if color == 'active':
                # Retrieve all active dataseries objects and filter for selected dataflow
                f1 = Q(color='red')
                f2 = Q(color='orange')
                f3 = Q(color='yellow')
                f0 = Q(df_name=df)
                series_list = DataSeries.objects.filter(f0 & (f1 | f2 | f3))
                print('all active')
                print(len(series_list))
            elif color == 'all':
                # Retrieve all dataseries objects and filter for selected dataflow
                f0 = Q(df_name=df)
                series_list = DataSeries.objects.filter(f0)
                print('all all')
                print(len(series_list))
        elif len(region) > 0:
            if color == 'active':
                # Retrieve all active dataseries objects and filter for selected region
                f0 = Q(df_name=df)
                f4 = Q(region=region)
                f1 = Q(color='red')
                f2 = Q(color='orange')
                f3 = Q(color='yellow')
                series_list = DataSeries.objects.filter(f0 & f4 & (f1 | f2 | f3))
                print('region active')
                print(len(series_list))
            elif color == 'all':
                # Retrieve all dataseries objects and filter for selected dataflow
                f0 = Q(df_name=df)
                f4 = Q(region=region)
                series_list = DataSeries.objects.filter(f0 & f4)
                print('region all')
                print(len(series_list))
        else:
            print('NO REGION SPECIFIED')

        # Construct content description for help display
        content_data = {}
        # series_list = []
        # for ds in series_list:
        #     content_data[ds.pk] = "<h4>" + ds.title + "</h4>" + "<i>" + ds.title_long + "</i>"
        context.update({'series_list': series_list})
        context.update({'content_data': json.dumps(content_data)})

        return context


class DataFlowCountryView(DetailView):
    """
    2f Dataflow Country View (Display Regional Groupings within Dataflow)

    """
    model = DataFlow
    template_name_suffix = '_country'
    slug_field = 'identifier'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataflow = super(DataFlowCountryView, self).get_object()

        # count all tracked series per region
        series_list = DataSeries.objects.filter(df_name=dataflow.identifier)
        # count all active series per region
        f1 = Q(color='red')
        f2 = Q(color='orange')
        f3 = Q(color='yellow')
        f0 = Q(df_name=dataflow.identifier)
        active_list = DataSeries.objects.filter(f0 & (f1 | f2 | f3))

        dimensions = dataflow.dimensions
        regions = {}
        for dim in dimensions:
            if dim['DimName'] == 'Reference Area':
                regions = dim['ActualCodes']

        region_list = []

        for code in regions:
            code_parts = code.split('.')
            dashboard_n = 0
            live_n = 0
            if len(code_parts) == 2:
                region = {}
                region['title'] = code_parts[1]
                region['title_long'] = regions[code]

                for tracked in series_list:
                    tregion = tracked.identifier.split('.')[1]
                    if tregion == region['title']:
                        dashboard_n += 1

                for active in active_list:
                    tregion = active.identifier.split('.')[1]
                    if tregion == region['title']:
                        live_n += 1

                region['dashboard_n'] = dashboard_n
                region['live_n'] = live_n

                region_list.append(region)

        # Construct region list datas
        content_data = {}
        context.update({'content_data': content_data})
        context.update({'identifier': dataflow.identifier})
        context.update({'region_list': region_list})

        return context


class DataFlowCountryAggregateView(DetailView):
    """
    2g Dataflow Country Aggregate View (Display Only Top Level Aggregate Groupings within Dataflow)

    """
    model = DataFlow
    template_name_suffix = '_country_aggregate'
    slug_field = 'identifier'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataflow = super(DataFlowCountryAggregateView, self).get_object()
        df = dataflow.identifier
        f0 = Q(df_name=df)
        series_list = DataSeries.objects.filter(f0)
        aggregate = []
        for series in series_list:
            if len(series.region) == 0:
                print(series.title)
                aggregate.append(series)

        # Construct content description for help display
        name = dataflow.name
        context.update({'country_name': name.replace("_", " ")})
        context.update({'series_list': aggregate})

        return context


#
# Individual Data Series Exploration Views
#

# 3 Data Series Data (Table)

class DataSeriesView(DetailView):
    model = DataSeries
    slug_field = 'identifier'
    template_name_suffix = '_table'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataseries = super(DataSeriesView, self).get_object()
        dataflow = DataFlow.objects.get(identifier=dataseries.df_name)
        unit = dataseries.unit
        context.update({'unit': json.dumps(unit)})
        context.update({'df_size': dataflow.dashboard_n})
        return context


# 3a Data Series Explore (Metrics)
class DSMetricsView(DetailView):
    model = DataSeries
    slug_field = 'identifier'
    template_name_suffix = '_metrics'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataseries = super(DSMetricsView, self).get_object()
        dataflow = DataFlow.objects.get(identifier=dataseries.df_name)
        unit = dataseries.unit
        context.update({'unit': json.dumps(unit)})
        context.update({'df_size': dataflow.dashboard_n})
        return context


# 3b Data Series Explore (Histogram)
# TODO Not enabled
class DSHistogramView(DetailView):
    model = DataSeries
    slug_field = 'identifier'
    template_name_suffix = '_histogram'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataseries = super(DSHistogramView, self).get_object()
        dataflow = DataFlow.objects.get(identifier=dataseries.df_name)
        unit = dataseries.unit
        context.update({'unit': json.dumps(unit)})
        context.update({'df_size': dataflow.dashboard_n})
        return context


# 3c Data Series Explore (Plot)
#
class DSPlotView(DetailView):
    model = DataSeries
    slug_field = 'identifier'
    template_name_suffix = '_plot'

    # We pass the following to the template
    # * the Dataseries object (implicitly as object, used in ds_breadcrumb)
    # * object.values, object.unit, object.dates, object.dates as json to
    # timeseries_graph_numerical.js or
    # timeseries_graph_ordinal.js

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataseries = super(DSPlotView, self).get_object()
        metrics = json.loads(dataseries.metrics)
        maxval = metrics['Max']
        minval = metrics['Min']
        average = metrics['Mean']
        latest = metrics['T']
        code_list = dataseries.code_list
        context.update({'maxval': maxval, 'minval': minval, 'average': average, 'latest': latest})
        context.update({'code_list': code_list})
        return context


# 3d Data Series Explore (Interactive)
class DSInteractiveView(DetailView):
    model = DataSeries
    slug_field = 'identifier'
    template_name_suffix = '_interactive'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dataseries = super(DSInteractiveView, self).get_object()
        dataflow = DataFlow.objects.get(identifier=dataseries.df_name)
        unit = dataseries.unit
        context.update({'unit': json.dumps(unit)})
        # context.update({'root_view': root_view})
        context.update({'df_size': dataflow.dashboard_n})
        return context


# 4 Data Series Filtered by Date List
# class DataSeriesListView(LoginRequiredMixin, ListView):
class DataSeriesListView(ListView):
    model = DataSeries
    template_name_suffix = '_list'

    # var = {"key":cutoff_date_red}
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    # def dispatch(self, request, *args, **kwargs):
    #    return super(DataSeriesListView, self).dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        color = self.kwargs['color']
        queryset = DataSeries.objects.filter(color=color)
        return queryset

    def get_context_data(self, **kwargs):

        try:
            params = DashBoardParams.objects.all().first()

            freshness = {'red': params.red_datasets, 'yellow': params.yellow_datasets, 'orange': params.orange_datasets,
                         'gray': params.gray_datasets}
        except:
            freshness = {'red': 0, 'yellow': 0, 'orange': 0, 'gray': 0}
        context = super(ListView, self).get_context_data(**kwargs)
        content_data = {}
        for ds in self.get_queryset():
            content_data[ds.pk] = "<h4>" + ds.title + "</h4>" + "<i>" + ds.title_long + "</i>"

        context.update({'content_data': json.dumps(content_data)})
        context.update({'freshness': json.dumps(freshness)})
        # context.update({'root_view': root_view})
        return context


# 5 GeoSlice Explore (Map)
class GSMapView(DetailView):
    model = GeoSlice
    slug_field = 'identifier'
    template_name_suffix = '_map'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        # get the geoslice
        geoslice = super(GSMapView, self).get_object()
        ac = geoslice.identifier.split('.')[1]
        # get the list of dataseries that are part of the geoslice
        dataseries = geoslice.dataset_id
        # print(dataseries)
        # construct the dataset to send to the template
        # the dataset for the mobility type for each country
        dataset = {}
        query = Q()
        for ds in dataseries:
            query |= Q(identifier=ds)
        entries = DataSeries.objects.filter(query)

        for full_entry in entries:
            print(full_entry)
            entry = {}
            # the redirect url in case we want to drill down
            entry['url'] = 'plot/' + full_entry.identifier
            # # we fetch the actual dataseries
            # full_entry = DataSeries.objects.filter(identifier=ds)
            # TBD
            dataid = full_entry.identifier.split('.')[0]
            # DS title
            entry['title'] = full_entry.title
            # DS long title
            entry['title_long'] = full_entry.title_long
            # DS observation dates
            entry['dates'] = full_entry.dates
            # DS observation values
            # values (% change)
            entry['values'] = full_entry.values
            # values (demeaned)
            dataset[dataid] = entry

        activity_dict = {}
        for i in activities_short:
            activity_dict[i] = activities[activities_short.index(i)]

        activity_string = activities[activities_short.index(ac)]

        context.update({'activity': activity_string})
        context.update({'activity_dict': activity_dict})
        context.update({'dataset': json.dumps(dataset)})
        return context


class GSListView(DetailView):
    # 5 GeoSlice Explore (Detail)

    model = GeoSlice
    template_name_suffix = '_detail'
    slug_field = 'identifier'

    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        geoslice = super(GSListView, self).get_object()
        gs_list = geoslice.dataset_id
        series_list = []
        for ds in gs_list:
            series_data = {}
            dataset = DataSeries.objects.filter(identifier=ds)
            series_data['pk'] = dataset[0].pk
            series_data['title'] = dataset[0].title
            series_data['title_long'] = dataset[0].title_long
            series_data['last_observation_date'] = dataset[0].last_observation_date
            series_data['identifier'] = dataset[0].identifier
            series_data['rest_url'] = dataset[0].rest_url
            series_list.append(series_data)

        # Construct content description for help display
        content_data = {}
        for ds in series_list:
            content_data[ds['pk']] = "<h4>" + ds['title'] + "</h4>" + "<i>" + ds['title_long'] + "</i>"
        context.update({'series_list': series_list})
        context.update({'content_data': json.dumps(content_data)})
        return context


#
# 6 Statistics Views
#

# 6a. Statistics (Overview) View
class Statistics(ListView):
    model = DataFlow
    template_name = 'policy/statistics.html'

    def get_context_data(self, **kwargs):
        # Retrieve all dataflow objects and construct content description text for help display
        # object_list = DataFlow.objects.all()
        # statistics = {}
        # total_datasets = 0
        # tracked_datasets = 0
        # live_datasets = 0
        # for df in object_list:
        #     total_datasets += df.google_n
        #     if df.tracked:
        #         tracked_datasets += df.dashboard_n
        #         live_datasets += len(df.dataset_id)
        #
        # statistics['total_datasets'] = total_datasets
        # statistics['tracked_datasets'] = tracked_datasets
        # statistics['live_datasets'] = live_datasets

        activity_dict = {}
        for i in activities_short:
            activity_dict[i] = activities[activities_short.index(i)]
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({'activity_dict': activity_dict})
        context.update({'activity': activities_short})
        return context


# 6b. Statistics Table View
# We compute the statistics on the fly based on filters
class StatsCountryTableView(ListView):
    model = DataFlow
    template_name = 'policy/statistics_table.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        activity = self.kwargs['activity']

        # Iterate over all dataflows and construct the relevant dataseries list

        f1 = Q(agg_level='Country')
        f2 = Q(activity=activity)
        series_list = DataSeries.objects.filter(f1 & f2)

        # series_list = DataSeries.objects.all()
        stats_list = []
        for series in series_list:
            # if series.region == '' and series.activity == activity:
            stats = {}
            stats['name'] = country_dict[series.df_name]
            stats['Max'] = json.loads(series.metrics)['Max']
            stats['Min'] = json.loads(series.metrics)['Min']
            stats['Average'] = json.loads(series.metrics)['Mean']
            stats['Latest'] = json.loads(series.metrics)['T']
            stats['Vol'] = json.loads(series.metrics)['Vol']
            stats_list.append(stats)

        activity_string = activities[activities_short.index(activity)]
        context.update({'activity': activity_string})
        context.update({'stats_list': stats_list})
        print(stats_list)
        return context


# 6c. Statistics Histogram View
# We compute the statistics on the fly based on filters
class StatsCountryHistogramView(ListView):
    model = DataFlow
    template_name = 'policy/statistics_histogram.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        activity = self.kwargs['activity']
        stat = self.kwargs['stat']
        activity_string = activities[activities_short.index(activity)]
        stat_string = stat_strings[stat]

        # Iterate over all dataflows and construct the relevant dataseries list

        f1 = Q(agg_level='Country')
        f2 = Q(activity=activity)
        series_list = DataSeries.objects.filter(f1 & f2)

        # series_list = DataSeries.objects.all()
        values = []
        for series in series_list:
            # if series.region == '' and series.activity == activity:
            value = json.loads(series.metrics)[stat]
            values.append(value)

        print(stat)
        context.update({'stat': stat_string})
        context.update({'activity': activity_string})
        context.update({'values': values})
        return context


class StatsCountryCorrelationView(ListView):
    model = DataFlow
    template_name = 'policy/statistics_correlation.html'

    def get_context_data(self, **kwargs):

        metadata = DashBoardParams.objects.all()[0].country_metadata
        print(metadata)

        context = super(ListView, self).get_context_data(**kwargs)
        activity1 = self.kwargs['activity1']
        activity2 = self.kwargs['activity2']

        activity_string1 = activities[activities_short.index(activity1)]
        activity_string2 = activities[activities_short.index(activity2)]

        # Filter the relevant dataseries list

        f1 = Q(agg_level='Country')
        f2 = Q(activity=activity1)
        f3 = Q(activity=activity2)
        series_list1 = DataSeries.objects.filter(f1 & f2)
        series_list2 = DataSeries.objects.filter(f1 & f3)
        N1 = len(series_list1)
        N2 = len(series_list2)

        dictionary_data = {
            'A1': 'Minimum Observed ' + activity_string1 + ' Mobility',
            'A2': 'Maximum Observed ' + activity_string1 + ' Mobility',
            'A3': 'Average Observed Mobility for ' + activity_string1,
            'A4': 'Latest Mobility Observation for ' + activity_string1,
        }

        stat_dict = {
            ''
        }

        # All country dict
        policy1 = {}
        policy2 = {}

        i = 1
        for series1 in series_list1:
            for series2 in series_list2:
                if series2.df_name == series1.df_name:
                    # country data dict
                    country_name = country_dict[series1.df_name]
                    country1 = {}
                    country1['A1'] = json.loads(series1.metrics)['Min']
                    country1['A2'] = json.loads(series1.metrics)['Max']
                    country1['A3'] = json.loads(series1.metrics)['Mean']
                    country1['A4'] = json.loads(series1.metrics)['T']
                    country1['M0'] = country_name
                    country1['M1'] = metadata[series1.df_name]['population_count']
                    try:
                        country1['M2'] = metadata[series1.df_name]['stress_level']
                    except:
                        country1['M2'] = 0
                    country2 = {}
                    country2['A1'] = json.loads(series2.metrics)['Min']
                    country2['A2'] = json.loads(series2.metrics)['Max']
                    country2['A3'] = json.loads(series2.metrics)['Mean']
                    country2['A4'] = json.loads(series2.metrics)['T']
                    country2['M0'] = country_name
                    country1['M1'] = metadata[series1.df_name]['population_count']
                    # country1['M2'] = metadata[series1.df_name]['stress_level']
                    # indexed by integer value
                    policy1[str(i)] = country1
                    policy2[str(i)] = country2
                    i += 1

        context.update({'policy1': policy1})
        context.update({'policy2': policy2})
        context.update({'dict_data': dictionary_data})
        context.update({'activity1': activity_string1 + ' Mobility'})
        context.update({'activity2': activity_string2 + ' Mobility'})
        return context

# @login_required(login_url='/login/')
# def eve_volatility_gauge_view(request):
#     t = loader.get_template('visual_apps/index.html')
#     context = RequestContext(request, {})
#     return HttpResponse(t.template.render(context))
#
#
# @login_required(login_url='/login/')
# def eve_correlation_radar_view(request):
#     t = loader.get_template('visual_apps/correlation_radar.html')
#     context = RequestContext(request, {})
#     return HttpResponse(t.template.render(context))
#
#
# @login_required(login_url='/login/')
# def sdw_3D_scan_view(request):
#     t = loader.get_template('visual_apps/3D_scan.html')
#     context = RequestContext(request, {})
#     return HttpResponse(t.template.render(context))
