# Copyright (c) 2020 - 2025 Open Risk (https://www.openriskmanagement.com)
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


from django.contrib.gis.db.models import PointField, MultiPolygonField, PolygonField
from django.db import models
from django.urls import reverse

from portfolio.Asset import ProjectAsset

"""
The main Portfolio models are defined in individual files for readability
Use models.py for any additional / auxiliary models

* General Geospatial Models

"""


class PointSource(models.Model):
    """
    A point marker with name and location (supports an elementary geospatial reference).
    """

    # data
    name = models.CharField(max_length=255, null=True, blank=True)
    location = PointField()

    # links

    asset = models.ForeignKey('portfolio.ProjectAsset', null=True, blank=True, on_delete=models.CASCADE)
    project = models.ForeignKey('portfolio.Project', null=True, blank=True, on_delete=models.CASCADE)

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:PointSource_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Point Source"
        verbose_name_plural = "Point Sources"


class AreaSource(models.Model):
    """A simple polygon geometry demarcating the area of a Project or Real Estate boundaries (where applicable)"""

    # IDENTIFICATION

    name = models.CharField(max_length=255)

    # LINKS

    asset = models.ForeignKey('portfolio.ProjectAsset', null=True, blank=True, on_delete=models.CASCADE)

    # ATTRIBUTES

    # ATTN location cannot be null
    location = PolygonField()

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:AreaSource_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Area Source"
        verbose_name_plural = "Area Sources"


class MultiAreaSource(models.Model):
    """A multi-polygon geometry demarcating the area of a Project or Real Estate boundaries (where applicable)"""

    # IDENTIFICATION

    name = models.CharField(max_length=255)

    # LINKS

    asset = models.ForeignKey('portfolio.ProjectAsset', null=True, blank=True, on_delete=models.CASCADE)

    # ATTRIBUTES
    location = MultiPolygonField()

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:MultiAreaSource_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Multi Area Source"
        verbose_name_plural = "Multi Area Sources"
