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

from django.db import models
from django.urls import reverse
from django.contrib.gis.db.models import PointField


class NUTS3PointData(models.Model):
    """
    The NUTS3 Point Data model holds NUTS3 Data with a Point Geometry

    https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts

    {"type":"FeatureCollection",
    "features": [{"type":"Feature",
                  "geometry":  {"type":"Point",
                                "coordinates":[4309292.7645,3441513.4943]},
                                "properties":{"NUTS_ID":"DEF0",
                                               "LEVL_CODE":2,
                                               "CNTR_CODE":"DE",
                                               "NAME_LATN":"Schleswig-Holstein",
                                               "NUTS_NAME":"Schleswig-Holstein",
                                               "MOUNT_TYPE":0,
                                               "URBN_TYPE":null,
                                               "COAST_TYPE":0,
                                               "FID":"DEF0"},
                                "id":"DEF0"},

    """

    coordinates = PointField()
    nuts_id = models.CharField(max_length=6, null=True, blank=True)
    levl_code = models.IntegerField(null=True, blank=True)
    cntr_code = models.CharField(max_length=6, null=True, blank=True)
    name_latn = models.CharField(max_length=200, null=True, blank=True)
    nuts_name = models.CharField(max_length=200, null=True, blank=True)
    mount_type = models.IntegerField(null=True, blank=True)
    urbn_type = models.IntegerField(null=True, blank=True)
    coast_type = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('reference:NUTS3PointData_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "NUT3 Point Geometry"
        verbose_name_plural = "NUTS3 Point Geometries"
