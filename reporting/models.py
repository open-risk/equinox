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

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django_countries.fields import CountryField


class SummaryStatistics(models.Model):
    """
    A Container for global (portfolio-wide) statistics

    """

    year = models.IntegerField(null=True, blank=True, help_text='The period of the measurement')
    country = CountryField(null=True, blank=True, help_text='The country of the measurement')
    sector = models.CharField(max_length=20, blank=True, null=True, help_text="Business Sector (NACE, CPA etc)")
    contracts = models.IntegerField(null=True, blank=True, help_text='The count of contracts')
    currency = models.CharField(max_length=4, blank=True, null=True, help_text="The currency of the measurement")
    value_total = models.FloatField(blank=True, null=True, help_text='The monetary value (in Currency units)')

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('admin:summary_statistics_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Summary Statistics"
        verbose_name_plural = "Summary Statistics"


class AggregatedStatistics(models.Model):
    """
    A Simplified Container for aggregated statistics of C02 / Value per country and sector
    It provides no temporal or currency dimensions
    It can hold aggregations of more granular Summary Statistics

    """

    country = CountryField(null=True, blank=True, help_text='The Country of the measurement')
    sector = models.CharField(max_length=20, blank=True, null=True, help_text="Business Sector")
    value_total = models.FloatField(blank=True, null=True, help_text='The monetary value (in common currency units)')
    co2_amount = models.FloatField(null=True, blank=True, help_text='CO2 amount in tonnes')

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('admin:aggregated_statistics_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Aggregated Statistics"
        verbose_name_plural = "Aggregated Statistics"


class ResultGroup(models.Model):
    """
    The ResultGroup Data object holds a group of calculation results

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    group_type = models.IntegerField(default=0)

    # The number of results include in the group
    # Must be manually augmented whenever there is a result added or deleted

    calculation_count = models.IntegerField(default=0)

    # the playbook that created this result group (if available)
    # ATTN result groups can also be formed in ad-hoc ways (e.g. user defined collections)
    # in that case there is no playbook associated and thus standardized reports
    # and visualization are not available

    # TODO reinstate once playbooks are implemented
    # playbook = models.ForeignKey(Playbook, on_delete=models.CASCADE, null=True, blank=True,
    #                              help_text="Playbook that created this ResultGroup (if any)")

    # TODO Does not make strict sense for a collection
    calculation_timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('admin:reporting_result_group_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Result Group"
        verbose_name_plural = "Result Groups"


class Calculation(models.Model):
    """
    The Calculation Data object holds the complete outcome of a workflow calculation as returned by a model server.

    It includes reference to the user initiating the calculation and the submitted workflow.

    The Logfile holds a logstring
    Result is json object with flexible structure. Typically:
    'Graph'     : json object (different types)
    'Statistics': json object (tabular)

    """

    result_group = models.ForeignKey(ResultGroup, on_delete=models.CASCADE, null=True, blank=True,
                                     help_text="Result Group to which this Calculation belong (if any)")

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # TODO reinstate once workflows are implemented
    # The Base Workflow object that was used for the calculation
    # workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, default=1)

    # The final workflow_data used for the calculation
    # In principle starting with the base workflow, performing all the FK embeddings
    # and applying the workflow delta should reproduce the workflow data stored here

    workflow_data = models.JSONField(null=True, blank=True, help_text="Verbatim storage of the calculation input "
                                                                      "in JSON format")

    # The result object creation time (may differ from the server execution time)
    creation_date = models.DateTimeField(auto_now_add=True)

    logfile = models.TextField(null=True, blank=True, help_text="Verbatim storage of the calculation logfile")
    results_data = models.JSONField(null=True, blank=True, help_text="Verbatim storage of the calculation results "
                                                                     "in JSON format")
    calculation_timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('admin:reporting_calculation_change', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"


OBJECTIVE_CHOICE = [(0, 'General Information'), (1, 'Concentration Risk'), (2, 'Origination'),
                    (3, 'Risk Appetite'), (4, 'Risk Capital'), (5, 'Other')]


class Visualization(models.Model):
    """
    The Visualization Data object holds the structural Vega / Vega-Lite specification of a visualization

    Includes reference to user creating the Visualization
    """

    name = models.CharField(max_length=200, help_text="Assigned name to help manage Visualization collections")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1, help_text="The creator of the Visualization")
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    objective = models.IntegerField(default=0, null=True, blank=True, choices=OBJECTIVE_CHOICE,
                                    help_text="Objective fulfilled by the Visualization")

    description = models.TextField(null=True, blank=True, help_text="A description of the main purpose and "
                                                                    "characteristics of the Visualization")

    visualization_data = models.JSONField(null=True, blank=True, help_text="Container for visualization data")
    visualization_data_url = models.URLField(null=True, blank=True, help_text="URL for visualization data")
    results_url = models.CharField(max_length=200, null=True, blank=True, help_text="Where to store the results")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reporting:visualization_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Visualization"
        verbose_name_plural = "Visualizations"
