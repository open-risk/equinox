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

from datetime import datetime

from django.db import models
from django.db.models import JSONField
from django.urls import reverse

"""
Classes to store Policy data

A portfolio-wide policy consists of (indicatively):

* Policy ID (Example: C1)
* Policy Name (Example: C1_School_Closing)
* Policy Description (Records closing of schools and universities)
* The policy type (C, E, H, M)
* The Geospatial Scope of the Policy (if applicable) (C1_Flag)
* The Observation Date for a Policy value
* The Policy Value (Can be Categorical, Ordinal or Numerical)
* The entity adopting the policy (country, firm etc)
    * Country Name
    * Country Code 

"""


class DashBoardParams(models.Model):

    # key value store for policy dashboard parameters
    # captures dataseries statistics etc.

    total_dataflows = models.IntegerField(blank=True, null=True)
    total_datasets = models.IntegerField(blank=True, null=True)
    tracked_datasets = models.IntegerField(blank=True, null=True)
    live_datasets = models.IntegerField(blank=True, null=True)
    red_datasets = models.IntegerField(blank=True, null=True)
    orange_datasets = models.IntegerField(blank=True, null=True)
    yellow_datasets = models.IntegerField(blank=True, null=True)
    gray_datasets = models.IntegerField(blank=True, null=True)

    country_metadata = JSONField(null=True, blank=True, help_text="Auxiliary country metadata")

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Dashboard Parameters"
        verbose_name_plural = "Dashboard Parameters"


# TODO Fine-Grained Policy data storage
# class PolicyDatum(models.Model):
#     country_region_code = models.CharField(max_length=80)
#     country_region = models.CharField(max_length=80, blank=True, null=True)
#     sub_region_1 = models.CharField(max_length=80, blank=True, null=True)
#     sub_region_2 = models.CharField(max_length=80, blank=True, null=True)
#
#     # The date of the measurement
#     observation_date = models.DateTimeField()
#
#     # Measurement by type of activity
#     retail_and_recreation_percent_change_from_baseline = models.FloatField(blank=True, null=True)
#     grocery_and_pharmacy_percent_change_from_baseline = models.FloatField(blank=True, null=True)
#     parks_percent_change_from_baseline = models.FloatField(blank=True, null=True)
#     transit_stations_percent_change_from_baseline = models.FloatField(blank=True, null=True)
#     workplaces_percent_change_from_baseline = models.FloatField(blank=True, null=True)
#     residential_percent_change_from_baseline = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         verbose_name = "Policy Datum"
#         verbose_name_plural = "Policy Data"


class DataSeries(models.Model):
    # formal identifier of the policy timeseries (constructed from region identifiers)
    identifier = models.CharField(null=True, blank=True, max_length=400, help_text="The unique identifier of the Policy dataseries")

    # policy dataflow metadata
    title = models.CharField(null=True, blank=True, max_length=400, help_text="The title of the Policy (Short)")
    title_long = models.CharField(null=True, blank=True, max_length=1600, help_text="The title of the Policy (Long)")

    # TODO FK relation to stored dataflows
    df_name = models.CharField(null=True, blank=True, max_length=80, help_text="The  Dataflow to which the Policy Dataseries belongs")

    rest_url = models.CharField(null=True, blank=True, max_length=400, help_text="API URL")

    documentation_url = models.CharField(null=True, blank=True, max_length=400, help_text="Documentation URL")

    agg_level = models.CharField(null=True, blank=True, default="Country", max_length=80, help_text="The applicable aggregation level of the policy data")

    frequency = models.CharField(null=True, blank=True, default="A", max_length=80, help_text="Policy update frequency")

    color = models.CharField(null=True, blank=True, default="0", max_length=80, help_text="The temporal freshness of measurement indicator")

    region = models.CharField(null=True, blank=True, default="N/A", max_length=80, help_text="Region to which policy applies")

    # TODO Hierarchical activity classifications
    activity = models.CharField(null=True, blank=True, default="N/A", max_length=80, help_text="Type of activity the policy concerns")

    status = models.CharField(null=True, blank=True, default="Valid", max_length=50, help_text="Validity status of the numerical data as usable timeseries")

    last_observation_date = models.DateTimeField(null=True, blank=True,
                                                 default=datetime(1916, 9, 25, 17, 22, 22, 90879), help_text="Last observation date of the timeseries,tracked separately for filtering purposes")

    field_type = models.CharField(null=True, blank=True, default="numerical", max_length=50, help_text="Mathematical nature of the timeseries data (categorical, ordinal, numerical)")

    dates = JSONField(null=True, blank=True, help_text="Array of observation dates")
    values = JSONField(null=True, blank=True, help_text="Array of observation values")

    unit = models.CharField(null=True, blank=True, default="%", max_length=50, help_text="The units the data are specified in (if numerical)")

    code_list = JSONField(null=True, blank=True, help_text="Ordinal/Categorical data code descriptions (code lists)")

    # storage of derived data in pre-processing stage
    metrics = JSONField(null=True, blank=True, help_text="Derived metrics (statistics)")
    geometry_1D = JSONField(null=True, blank=True, help_text="Derived graph geometries")
    values_diff = JSONField(null=True, blank=True, help_text="Value differences")
    values_diff_p = JSONField(null=True, blank=True, help_text="Value differences %")

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.identifier

    def get_absolute_url(self):
        return reverse('policy:DataSeries', kwargs={'identifier': self.identifier})

    class Meta:
        verbose_name = "Dataseries"
        verbose_name_plural = "Dataseries"


class DataFlow(models.Model):
    #
    # Policy Dataflow MetaData (Country Based)
    #
    # Dataflow name (=Country 2 Letter Code)
    name = models.CharField(null=True, blank=True, max_length=80, help_text="Internal dataflow name")
    # formal identifier of the dataflow (country code)
    identifier = models.CharField(null=True, blank=True, max_length=80, help_text="Formal identifier of the dataflow")
    # dataflow short description
    # short_desc = models.CharField(max_length=200, help_text="List of desired result dataseries")
    short_desc = models.TextField(null=True, blank=True, help_text="Dataflow short description")
    # dataflow long description
    # long_desc = models.CharField(max_length=800)
    long_desc = models.TextField(null=True, blank=True, help_text="Dataflow long description")
    # dataflow description node url (TODO not used)
    node_url = models.CharField(null=True, blank=True, max_length=400, help_text="Dataflow description node url")
    # number of dataseries
    available_n = models.IntegerField(null=True, blank=True, help_text="Number of available dataseries")
    # number of regions (level 1)
    regions_n = models.IntegerField(null=True, blank=True, default=0, help_text="Number of regions")
    # number of regions (level 2)
    subregions_n = models.IntegerField(null=True, blank=True, default=0, help_text="Number of sub-regions")

    # dimensions and codelists
    dimensions = JSONField(null=True, blank=True, help_text="Dimensions and codelists")
    # update frequency
    update = models.CharField(null=True, blank=True, default="W", max_length=10, help_text="Update frequency")

    # list of dataseries ID's
    dataset_id = JSONField(null=True, blank=True, help_text="List of dataseries ID's")
    # tracked within dashboard
    tracked = models.BooleanField(null=True, blank=True, help_text="Whether tracked within dashboard")
    # number of tracked dashboard series
    dashboard_n = models.IntegerField(null=True, blank=True, help_text="Number of tracked dashboard series")
    # number of geolocation tags
    geo = models.IntegerField(null=True, blank=True, help_text="Number of geolocation tags")
    # number of geoslices
    geoslices = models.IntegerField(null=True, blank=True, help_text="Number of geoslices")
    # number of tracked dashboard series
    live_n = models.IntegerField(null=True, blank=True, help_text="Number of live dashboard series")
    # dataseries SDW selector fields
    selectors = JSONField(null=True, blank=True, help_text="Dataseries selector field")
    # equinox category dictionary for each dataflow (placeholder in case of additional data sources)
    category_list = JSONField(null=True, blank=True, help_text="Equinox category dictionary for each dataflow")
    # category string to use in Category based list view of all dataflows
    menu_category = models.CharField(null=True, blank=True, max_length=200,
                                     help_text="Category string to use in Category based list view of all dataflows")
    # freshness data
    # Array with summary date buckets [red, orange, yellow]
    freshness = JSONField(null=True, blank=True, help_text="Array with summary date buckets [red, orange, yellow]")

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('DataSeries_list', kwargs={'name': self.name})
        return reverse('policy:DataFlow', kwargs={'name': self.name})

    class Meta:
        verbose_name = "Dataflow"
        verbose_name_plural = "Dataflows"


class GeoSlice(models.Model):
    # formal identifier of the GeoSlice (eg. "EU.RR")
    identifier = models.CharField(max_length=80)
    # dataflow to which it belongs (if applicable)
    df_name = models.CharField(null=True, blank=True, max_length=80)
    # geoslice short description
    short_desc = models.TextField(help_text="Short description of the Geoslice")
    # geoslice long description
    long_desc = models.TextField(help_text="Long description of the Geoslice")
    # dimensions and codelists (if applicable)
    dimensions = JSONField(null=True, blank=True, help_text="List of desired result dataseries")
    # list of dataseries ID's
    dataset_id = JSONField(null=True, blank=True, help_text="List of desired result dataseries")

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.identifier

    def get_absolute_url(self):
        return reverse('policy:GeoSlice', kwargs={'identifier': self.identifier})

    class Meta:
        verbose_name = "Geographic Slice"
        verbose_name_plural = "Geographic Slices"
