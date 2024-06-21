from django.contrib.auth.models import User
from django.db.models import JSONField
from django.urls import reverse
from django.db import models


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
