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

from django.urls import reverse
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

"""
Data Center related models
"""

# The Campus class is a composite of discrete data center facilities
# ATTN the term is different from how OSM defines a campus

DATACENTER_CLASS_CHOICES = [(0, '(a) Enterprise'),
                            (1, '(b) Cloud'),
                            (2, '(c) Colocation'),
                            (3, '(d) Unknown')]

AREA_TYPE_CHOICES = [(0, '(a) City'), (1, '(b) Industrial'), (2, '(c) Rural')]

AGGREGATION_TYPE = [(0, '(a) Facility'), (1, '(b) Colocation Share'), (2, '(c) Campus')]

SURFACE_AREA_UNITS = [(0, 'Square Feet'), (1, 'Square Meters')]

WATER_VOLUME_UNITS = [(0, 'Gallons'), (1, 'Liters'), (2, 'm3')]


class DataCenter(models.Model):
    """
    The Data Center Asset model holds data center specific data

    """

    GEOMETRY_CHOICES = [(0, 'LineString'), (1, 'Polygon'), (2, 'Multipolygon'), (3, 'Point')]

    # IDENTIFICATION & CATEGORIZATION

    datacenter_id = models.CharField(max_length=80, blank=True, null=True,
                                     help_text='Data Center ID (defaults to OSM @id)', verbose_name='OSM ID')

    datacenter_name = models.CharField(max_length=80, blank=True, null=True,
                                       help_text='Name of Data Center (from OSM or elsewhere)',
                                       verbose_name="Data Center")

    datacenter_ref = models.CharField(max_length=80, blank=True, null=True,
                                      help_text='Reference ID of Data Center (from OSM or elsewhere)',
                                      verbose_name="Reference")

    notes = models.TextField(blank=True, null=True,
                             help_text='Additional unstructured information about the Data Center',
                             verbose_name="Notes")

    asset_class = models.IntegerField(blank=True, null=True, choices=DATACENTER_CLASS_CHOICES,
                                      help_text='This identifies the way the data center is used <a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>',
                                      verbose_name="Type")

    aggregation_type = models.IntegerField(blank=True, null=True, choices=AGGREGATION_TYPE, default=0,
                                           help_text='How the data center is reported', verbose_name="Aggregation")

    campus = models.ForeignKey('DataCenterCampus', blank=True, null=True, on_delete=models.CASCADE,
                               help_text="Campus to which the facility belongs", verbose_name="Campus")

    portfolio = models.ForeignKey('ProjectPortfolio', blank=True, null=True, on_delete=models.CASCADE,
                                  help_text="The portfolio to which this data center belongs", verbose_name="Portfolio")

    snapshot = models.ForeignKey('PortfolioSnapshot', on_delete=models.CASCADE, blank=True, null=True,
                                 help_text="The portfolio snapshot to which the date center record belongs",
                                 verbose_name="Snapshot")

    website = models.URLField(null=True, blank=True, help_text="URL for further information", verbose_name='Website')

    # FACILITY CHARACTERISTICS

    surface_area = models.FloatField(blank=True, null=True,
                                     help_text="Surface area of facility polygon, measured in square feet or square meters. Only available for OSM building and campus layers")

    surface_area_units = models.IntegerField(blank=True, null=True, choices=SURFACE_AREA_UNITS,
                                             help_text="Surface area units of measurement")

    prov_surface_area = models.ForeignKey('provenance.Agent', blank=True, null=True, on_delete=models.CASCADE,
                                          help_text="Provenance Agent for Surface Area",
                                          related_name='prov_surface_area', verbose_name='Provenance surface area')

    number_of_floors = models.IntegerField(blank=True, null=True,
                                           help_text="The number of floors of the facility. Building:levels in OSM")

    # FACILITY OPERATOR

    operator = models.ForeignKey('portfolio.Operator', blank=True, null=True, on_delete=models.CASCADE,
                                 help_text="The operator (corporate entity) of the data center",
                                 verbose_name="Operator")

    prov_operator = models.ForeignKey('provenance.Agent', blank=True, null=True, on_delete=models.CASCADE,
                                      help_text="Provenance Agent for Operator Data", related_name='prov_operator', verbose_name='Provenance operator')

    # GEOGRAPHICAL DATA

    country = models.CharField(max_length=300, blank=True, null=True,
                               help_text='Country of Datacenter Location (Word)', verbose_name='Country')

    country_code = models.CharField(max_length=2, blank=True, null=True,
                               help_text='Country Code of Datacenter Location - 2 Letter', verbose_name='Country Code')

    county = models.CharField(max_length=300, blank=True, null=True,
                              help_text='County of Datacenter Location - if applicable')

    county_id = models.IntegerField(blank=True, null=True,
                                    help_text='County ID of Datacenter Location - if applicable')

    state = models.CharField(max_length=300, blank=True, null=True,
                             help_text='State of Datacenter Location - if applicable')

    state_abb = models.CharField(max_length=2, blank=True, null=True,
                                 help_text='2-Letter State Abbreviation of Datacenter Location - if applicable',
                                 verbose_name="State")

    state_id = models.IntegerField(blank=True, null=True,
                                   help_text='State ID of Datacenter Location - if applicable')

    city = models.CharField(max_length=300, blank=True, null=True,
                            help_text='City Name (OSM)', verbose_name='City')

    address_street = models.CharField(max_length=300, blank=True, null=True,
                                      help_text='Street Name (OSM)')

    address_number = models.CharField(max_length=30, blank=True, null=True,
                                      help_text='Street Number (OSM)')

    postcode = models.CharField(max_length=30, blank=True, null=True,
                                help_text='Post Code (OSM)')

    #
    # GEOSPATIAL DATA
    #

    datacenter_location = LocationField(based_fields=['city'], zoom=7, blank=True, null=True,
                                        help_text='The barycenter location of the data center (LOLA format)')

    # Common OSM geometries used in this context:
    # 'MultiPolygon', 'LineString', 'Polygon'
    # NB: 'Point' is converted to datacenter location

    # point_geometry = models.PointField(blank=True, null=True, srid=4326, spatial_index=False,
    #                                    default=Point(0, 0), help_text='Store GeoJSON Point Geometry')

    # linestring_geometry = models.LineStringField(blank=True, null=True, srid=4326, spatial_index=False,                                     help_text='Store GeoJSON LineString Geometry')
    #
    # polygon_geometry = models.PolygonField(blank=True, null=True, srid=4326, spatial_index=False,                                     help_text='Store GeoJSON Polygon Geometry')
    #
    # multipolygon_geometry = models.MultiPolygonField(blank=True, null=True, srid=4326, spatial_index=False,                                     help_text='Store GeoJSON MultiPolygon Geometry')

    geometry = models.GeometryField(blank=True, null=True, srid=4326, help_text='Store GeoJSON Geometry (one of LineString, Polygon, Multipolygon')

    geometry_type = models.IntegerField(blank=True, null=True, choices=GEOMETRY_CHOICES,
                                        help_text='Identifies Geometry Type',
                                        verbose_name="Geometry Type")

    prov_location = models.ForeignKey('provenance.Agent', blank=True, null=True,
                                      on_delete=models.CASCADE,
                                      help_text="Provenance Agent for Geographical Data (Default is OSM)",
                                      related_name='prov_location', verbose_name='Provenance location')

    #
    # Environmental Data
    #

    electricity_consumption = models.FloatField(blank=True, null=True,
                                                help_text='This field stores the aggregate current annualized electricity consumption (MWh)')

    prov_electricity_consumption = models.ForeignKey('provenance.Agent', blank=True, null=True,
                                                     on_delete=models.CASCADE,
                                                     help_text="Provenance Agent for Electricity Consumption",
                                                     related_name='prov_electricity_consumption', verbose_name='Provenance electricity consumption')

    power_usage_effectiveness = models.FloatField(blank=True, null=True,
                                                  help_text='Ratio of total power use to IT power use (dimensionless)', verbose_name='Power Usage Effectiveness')

    prov_pue = models.ForeignKey('provenance.Agent', blank=True, null=True, on_delete=models.CASCADE,
                                 help_text="Provenance Agent for PUE", related_name='prov_pue', verbose_name='Provenance PUE')

    asset_ghg_emissions = models.FloatField(blank=True, null=True,
                                            help_text='This field stores the aggregate current annualized emissions of an asset in tCO2 of CO2 equivalents - Scope 2', verbose_name='Asset GHG emissions')

    prov_ghg_emissions = models.ForeignKey('provenance.Agent', blank=True, null=True, on_delete=models.CASCADE,
                                           help_text="Provenance Agent for GHG Emissions",
                                           related_name='prov_ghg_emissions', verbose_name='Provenance GHG emissions')

    # TODO, various possible units
    # e.g., gCO2/KWh, tCO2/MWh (multiply gCO2/kWh by 0.001 to get tCO2/MWh)

    grid_carbon_intensity = models.FloatField(blank=True, null=True,
                                              help_text='This field stores the electricity grid carbon intensity of the production mix in units of tCO2/MWh', verbose_name='Production mix carbon intensity')

    grid_carbon_intensity_r = models.FloatField(blank=True, null=True,
                                              help_text='This field stores the electricity grid carbon intensity of the residual mix in units of tCO2/MWh', verbose_name='Residual mix carbon intensity')

    grid_carbon_intensity_s = models.FloatField(blank=True, null=True,
                                              help_text='This field stores the electricity grid carbon intensity of the supplier mix in units of tCO2/MWh', verbose_name='Supplier mix carbon intensity')

    prov_grid_carbon_intensity = models.ForeignKey('provenance.Agent', blank=True, null=True, on_delete=models.CASCADE,
                                                   help_text="Provenance Agent for Grid Carbon Intensities",
                                                   related_name='prov_grid_carbon_intensity', verbose_name='Provenance of grid carbon intensities')

    grid_water_intensity = models.FloatField(blank=True, null=True,
                                             help_text='This field stores the electricity grid water intensity in units of L/KWh')

    prov_grid_water_intensity = models.ForeignKey('provenance.Agent', blank=True, null=True, on_delete=models.CASCADE,
                                                  help_text="Provenance Agent for Grid Water Intensity",
                                                  related_name='prov_grid_water_intensity', verbose_name='Provenance grid water intensity')

    asset_water_usage = models.FloatField(blank=True, null=True,
                                          help_text='This field stores the aggregate current annualized water usage of an asset (Millions of Gallons, Liters or M3).')

    embedded_water_usage = models.FloatField(blank=True, null=True,
                                             help_text='This field stores the embedded (Scope 2) current annualized water usage of an asset (Millions of Gallons, Liters or M3).')

    prov_water_usage = models.ForeignKey('provenance.Agent', blank=True, null=True, on_delete=models.CASCADE,
                                         help_text="Provenance Agent for Water Usage Data",
                                         related_name='prov_water_usage', verbose_name='Provenance water usage')

    water_usage_effectiveness = models.FloatField(blank=True, null=True,
                                                  help_text='Ratio of water consumption over IT power use (liters per kilowatt-hour or gallons per megawatt-hour)')

    prov_wue = models.ForeignKey('provenance.Agent', blank=True, null=True, on_delete=models.CASCADE,
                                 help_text="Provenance Agent for WUE", related_name='prov_wue', verbose_name='Provenance WUE')

    water_volume_units = models.IntegerField(blank=True, null=True, choices=WATER_VOLUME_UNITS,
                                             help_text="Water volume units of measurement")

    # OTHER

    date_of_commissioning = models.DateField(blank=True, null=True,
                                             help_text='Commissioning date of the data center. Determines earliest available data points.<a class="risk_manual_url" href="https://www.openriskmanual.org/wiki">Documentation</a>')

    wikidata_object = models.CharField(max_length=30, blank=True, null=True,
                                       help_text='Wikidata Object (from OSM)')

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    @classmethod
    def get_geometry_by_display(cls, display_value):
        for value, display in cls.GEOMETRY_CHOICES:
            if display == display_value:
                return value
        return None

    def __str__(self):
        return self.datacenter_name

    def get_absolute_url(self):
        return reverse('admin:portfolio_datacenter_change', args=[self.pk])

    class Meta:
        verbose_name = "Data Center"
        verbose_name_plural = "Data Centers"


class DataCenterCampus(models.Model):
    """
    The Data Center Campus model allows compiling campus-wide information
    for multiple adjacent data centers

    The model acts as a collection. If a campus of data centers is not resolved into individual facilities, then it should be entered as a single data center

    """

    # OWNER / OPERATOR Role

    operator = models.ForeignKey('portfolio.Operator', blank=True, null=True, on_delete=models.CASCADE,
                                 help_text="The operator (corporate entity) of the campus",
                                 verbose_name="Operator")

    aggregation_type = models.IntegerField(blank=True, null=True, choices=AGGREGATION_TYPE, default=0,
                                           help_text='How the data center campus is reported',
                                           verbose_name="Aggregation")

    # IDENTIFICATION & CATEGORIZATION

    campus_name = models.CharField(max_length=80, blank=True, null=True,
                                   help_text='Name of Campus', verbose_name="Campus")

    notes = models.TextField(blank=True, null=True,
                             help_text='Additional information about the Data Center Campus', verbose_name="Notes")

    portfolio = models.ForeignKey('ProjectPortfolio', blank=True, null=True, on_delete=models.CASCADE,
                                  help_text="The portfolio to which this data center belongs", verbose_name="Portfolio")

    snapshot = models.ForeignKey('PortfolioSnapshot', on_delete=models.CASCADE, blank=True, null=True,
                                 help_text="The portfolio snapshot to which the date center record belongs",
                                 verbose_name="Snapshot")

    address = models.TextField(blank=True, null=True,
                               help_text='Street address where the Property is located at')

    area_type = models.IntegerField(blank=True, null=True, choices=AREA_TYPE_CHOICES,
                                    help_text='Area type where the Property is located at, i.e. City, Industrial, Rural')

    # CAMPUS CHARACTERISTICS (DERIVED)

    surface_area = models.FloatField(blank=True, null=True,
                                     help_text="Total surface area of campus", verbose_name='Floor Space')

    surface_area_units = models.IntegerField(blank=True, null=True, choices=SURFACE_AREA_UNITS,
                                             help_text="Surface area units of measurement")

    # GEOGRAPHICAL DATA

    country = models.CharField(max_length=300, blank=True, null=True,
                               help_text='Country of Campus Location')

    county = models.CharField(max_length=300, blank=True, null=True,
                              help_text='County of Campus Location')

    county_id = models.IntegerField(blank=True, null=True,
                                    help_text='County ID of Campus Location')

    state = models.CharField(max_length=300, blank=True, null=True,
                             help_text='State of Campus Location')

    state_abb = models.CharField(max_length=2, blank=True, null=True,
                                 help_text='2-Letter State Abbreviation of Campus Location', verbose_name="State")

    state_id = models.IntegerField(blank=True, null=True,
                                   help_text='State ID of Campus Location')

    #
    # Environmental Data Scope 1
    #

    gas_consumption = models.FloatField(blank=True, null=True,
                                        help_text='This field stores the aggregate current annualized gas consumption (MMBtu)',
                                        verbose_name="Gas (MMBtu)")

    scope1_ghg_emissions = models.FloatField(blank=True, null=True,
                                             help_text='This field stores the aggregate current annualized emissions of an asset in tCO2 of CO2 equivalents - Scope 1',
                                             verbose_name='Scope 1 GHG')

    #
    # Environmental Data Scope 2
    #

    electricity_consumption = models.FloatField(blank=True, null=True,
                                                help_text='This field stores the aggregate current annualized electricity consumption (MWh)',
                                                verbose_name="Electricity (MWh)")

    power_usage_effectiveness = models.FloatField(blank=True, null=True,
                                                  help_text='Ratio of tota power use to IT power use (dimensionless)')

    scope2_ghg_emissions = models.FloatField(blank=True, null=True,
                                             help_text='This field stores the aggregate current annualized emissions of an asset in tCO2 of CO2 equivalents - Scope 2',
                                             verbose_name='Scope 2 GHG')

    grid_carbon_intensity = models.FloatField(blank=True, null=True,
                                              help_text='This field stores the electricity grid carbon intensity in units of tCO2/MWh',
                                              verbose_name="Grid Carbon Intensity")

    grid_water_intensity = models.FloatField(blank=True, null=True,
                                             help_text='This field stores the electricity grid water intensity in units of L/KWh',
                                             verbose_name="Grid Water Intensity")

    asset_water_usage = models.FloatField(blank=True, null=True,
                                          help_text='This field stores the aggregate current annualized water usage of an asset (Millions of Gallons, Liters or M3).')

    embedded_water_usage = models.FloatField(blank=True, null=True,
                                             help_text='This field stores the embedded (Scope 2) current annualized water usage of an asset (Millions of Gallons, Liters or M3).',
                                             verbose_name="Embedded Water")

    water_usage_effectiveness = models.FloatField(blank=True, null=True,
                                                  help_text='Ratio of water consumption over IT power use (liters per kilowatt-hour or gallons per megawatt-hour)')

    water_volume_units = models.IntegerField(blank=True, null=True, choices=WATER_VOLUME_UNITS,
                                             help_text="Water volume units of measurement")

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campus_name

    def get_absolute_url(self):
        return reverse('admin:portfolio_datacentercampus_change', args=[self.pk])

    class Meta:
        verbose_name = "Data Center Campus"
        verbose_name_plural = "Data Center Campuses"
