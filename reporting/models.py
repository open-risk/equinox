# Copyright (c) 2020 - 2026 Open Risk (https://www.openriskmanagement.com)
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
from django.db.models import JSONField

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

def padding_default():
    return {"left": 5, "top": 5, "right": 5, "bottom": 5}


CATEGORY_CHOICES = (
    (0, 'line plot'),
    (1, 'timeseries'),
    (2, 'bar plot'),
    (3, 'histogram'),
    (4, 'x-y plot'),
    (5, 'radial chart'),
    (6, 'box plot'),
    (7, 'distribution'),
    (8, 'contingency chart'),
    (9, 'tree diagram'),
    (10, 'network diagram'),
    (11, 'geographical map'),
    (12, 'ternary'),
    (13, 'specialty'),
    (14, 'customized'))

MARK_CHOICES = (
    (0, "area"),
    (1, "bar"),
    (2, "circle"),
    (3, "line"),
    (4, "point"),
    (5, "rect"),
    (6, "rule"),
    (7, "square"),
    (8, "text"),
    (9, "tick"),
    (10, "geoshape")
)


class VegaSpecification(models.Model):
    """
    Data object holds normalized vega specification

    The specification allows multiple possible types for each property (e.g. both a Number, an Object and a Signal) We select the most common / simple use case. Alternative use cases must override the model defaults at some point during the View or Page rendering phase

    The basic data model used by Vega is tabular data, similar to a spreadsheet or database table. Individual data sets are assumed to contain a collection of records (or “rows”), which may contain any number of named data attributes (fields, or “columns”). Records are modeled using standard JavaScript objects.

    Principle 1 is that datasets are from a finite list of distinct reference formats that are already implemented as Django models. This does not fix the format into a dataframe because there could be JSONFields. Datasets could have a REST API (alternative channel)
    Examples:
        * 1 array (timeseries data) / dataseries like (also SDMX)
        * 2 tabular (portfolio data) / dataframe like
        * 3 graph like (node - links), stored in multiple models
        * tree like

    Principle 2 is that the view that renders the visualization compiles a full Vega specification including the data needed Hence the client side javascript is minimal (loading the full specification, bindings etc.), always the same, easy to maintain Changes to the visualization are done on the path to full spec creation:
        * changing the dataset source endpoints from the eligible classes -> choices from admin or via user forms
        * changing the specification from the vega spec collection -> manual admin exercise or user forms
        * structural changes -> require python view modifications

    Principle 3 is that a visualization is a type of post-processing and data transformation that is applied to a primary dataset. Additional datasets might be required. Such datasets might be generic (mashups with other dataseries), or specific (geographical data) Hence the core Vega visualization specification is a view that renders a given model with all eligible visualizations

    Principle 4 is that the overall data and specification flow architecture should make sense and ber re-usable for non-vega visualizations
        * Internal (matplotlib, pygal)
        * Partially custom js (d3)
        * Fully custom js (vol gauge etc)

    Principle 5 is that the URL patterns follow a well-structured REST API
        * The pattern has intuitive placeholders for object selection (viz & data)

    Principle 6 is that the rendered graphic is a well-behaved component
        * The Rendered object (svg) is self-documenting as a static object
        * NO DYNAMIC CHANGES of DATA or VIZ (Ajax calls) beyond what is achievable via signals
        * Can be replicated on the page as multiple objects (expressing an option list or parameter range)

    """

    schema = models.URLField(default="https://vega.github.io/schema/vega/v5.json",
                             help_text=" 	The URL for the Vega schema.")

    # category choices are preselected
    # sub-category choices are free form text (for flexibility)
    category = models.IntegerField(default=0, choices=CATEGORY_CHOICES,
                                   help_text="The high level category to which the visualization belongs")

    subcategory = models.CharField(max_length=200, null=True, blank=True,
                                   help_text="Subcategory to which the visualization belongs")

    description = models.CharField(max_length=500, default="Specification Description",
                                   help_text="A text description of the visualization. In versions ≥ 5.10, "
                                             "the description determines the aria-label attribute for the "
                                             "container element of a Vega view.")
    width = models.IntegerField(default=500, help_text="The width of the visualization in pixels.")
    height = models.IntegerField(default=200, help_text="The height of the visualization in pixels")
    padding = JSONField(default=padding_default, null=True, blank=True,
                        help_text="The padding in pixels to add around the visualization."
                                  "Number and Schema Types")

    AUTOSIZE_CHOICES = ((0, 'pad'), (1, 'fit'), (2, 'fit-x'), (3, 'fit-y'), (4, 'none'))
    autosize = models.IntegerField(default=0, choices=AUTOSIZE_CHOICES,
                                   help_text="Sets how the visualization size should be determined")

    config = JSONField(default=dict, null=True, blank=True,
                       help_text="Configuration settings with default values for marks, axes, and legends.")

    signals = JSONField(default=dict, null=True, blank=True,
                        help_text="Signals are dynamic variables that parameterize a visualization.")

    scales = JSONField(default=dict, null=True, blank=True,
                       help_text="Scales map data values (numbers, dates, categories, etc) to visual values "
                                 "(pixels, colors, sizes).")

    projections = JSONField(default=dict, null=True, blank=True,
                            help_text="Cartographic projections map (longitude, latitude) pairs to projected "
                                      "(x, y) coordinates.")

    axes = JSONField(default=dict, null=True, blank=True,
                     help_text="Coordinate axes visualize spatial scale mappings.")

    legends = JSONField(default=dict, null=True, blank=True,
                        help_text="Legends visualize scale mappings for visual values such as color, shape and size.")

    title = models.CharField(max_length=200, default="Visualization",
                             help_text="Title text to describe a visualization.")

    marks = JSONField(default=dict, null=True, blank=True,
                      help_text="Graphical marks visually encode data using geometric primitives such as rectangles, "
                                "lines, and plotting symbols.")

    encode = JSONField(default=dict, null=True, blank=True,
                       help_text="Encoding directives for the visual properties of the top-level group mark "
                                 "representing a chart’s data rectangle. For example, this can be used to set a "
                                 "background fill color for the plotting area, rather than the entire view.")

    usermeta = JSONField(default=dict, null=True, blank=True,
                         help_text="Optional metadata that will be ignored by the Vega parser.")

    extradata = JSONField(default=dict, null=True, blank=True,
                          help_text="Additional data that will be added to the vega data specification.")

    transform = JSONField(default=dict, null=True, blank=True,
                          help_text="Transform that will be applied to the primary data object.")

    intermediatedata = JSONField(default=dict, null=True, blank=True,
                                 help_text="Transform generating intermediate data from the primary data object.")

    def __str__(self):
        # Construct a unique name on the basis of title and pk
        return self.title + " (Object: " + str(self.pk) + ")"

    def get_absolute_url(self):
        return reverse('visualization:vega_specification_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Vega Specification"
        verbose_name_plural = "Vega Specifications"


class VegaLiteSpecification(models.Model):
    """
    Data object holds normalized vega lite specification

    """

    # Category is for internal use
    # category choices are preselected
    # sub-category choices are free form text (for flexibility)

    category = models.IntegerField(default=0, choices=CATEGORY_CHOICES,
                                   help_text="The high level category to which the visualization belongs")

    subcategory = models.CharField(max_length=200, null=True, blank=True,
                                   help_text="Subcategory to which the visualization belongs")

    #
    # TOP LEVEL SPECIFICATION
    #

    schema = models.URLField(default="https://vega.github.io/schema/vega-lite/v4.json",
                             help_text=" 	The URL for the Vega Lite schema.")

    title = models.CharField(max_length=200, default="Visualization",
                             help_text="Title text to describe a visualization.")

    description = models.CharField(max_length=500, default="Specification Description",
                                   help_text="A text description of the visualization.")

    width = models.IntegerField(default=500, help_text="The width of the visualization in pixels.")
    height = models.IntegerField(default=200, help_text="The height of the visualization in pixels")

    mark = models.IntegerField(default=0, choices=MARK_CHOICES, help_text="Choice of mark to use in the visualization")

    encoding = JSONField(default=dict, null=True, blank=True,
                         help_text="Encoding directives for the visual properties of the top-level group mark "
                                   "representing a chart’s data rectangle. For example, this can be used to set a "
                                   "background fill color for the plotting area, rather than the entire view.")

    transform = JSONField(default=dict, null=True, blank=True,
                          help_text="Transform that will be applied to the primary data object.")

    # padding = JSONField(default=padding_default, null=True, blank=True,
    #                     help_text="The padding in pixels to add around the visualization."
    #                               "Number and Schema Types")
    #
    # AUTOSIZE_CHOICES = ((0, 'pad'), (1, 'fit'), (2, 'fit-x'), (3, 'fit-y'), (4, 'none'))
    # autosize = models.IntegerField(default=0, choices=AUTOSIZE_CHOICES,
    #                                help_text="Sets how the visualization size should be determined")
    #
    config = JSONField(default=dict, null=True, blank=True,
                       help_text="Configuration settings with default values for marks, axes, and legends.")

    # signals = JSONField(default=dict, null=True, blank=True,
    #                     help_text="Signals are dynamic variables that parameterize a visualization.")
    #
    # scales = JSONField(default=dict, null=True, blank=True,
    #                    help_text="Scales map data values (numbers, dates, categories, etc) to visual values "
    #                              "(pixels, colors, sizes).")
    #
    # projections = JSONField(default=dict, null=True, blank=True,
    #                         help_text="Cartographic projections map (longitude, latitude) pairs to projected "
    #                                   "(x, y) coordinates.")
    #
    # axes = JSONField(default=dict, null=True, blank=True,
    #                  help_text="Coordinate axes visualize spatial scale mappings.")
    #
    # legends = JSONField(default=dict, null=True, blank=True,
    #                     help_text="Legends visualize scale mappings for visual values such as color, shape and size.")
    #
    #
    # marks = JSONField(default=dict, null=True, blank=True,
    #                   help_text="Graphical marks visually encode data using geometric primitives such as rectangles, "
    #                             "lines, and plotting symbols.")
    #
    # usermeta = JSONField(default=dict, null=True, blank=True,
    #                      help_text="Optional metadata that will be ignored by the Vega parser.")
    #
    # extradata = JSONField(default=dict, null=True, blank=True,
    #                       help_text="Additional data that will be added to the vega data specification.")
    #

    #
    # intermediatedata = JSONField(default=dict, null=True, blank=True,
    #                              help_text="Transform generating intermediate data from the primary data object.")

    def __str__(self):
        # Construct a unique name on the basis of title and pk
        return self.title + " (Object: " + str(self.pk) + ")"

    def get_absolute_url(self):
        return reverse('visualization:vega_lite_specification_view', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "VegaLite Specification"
        verbose_name_plural = "VegaLite Specifications"
