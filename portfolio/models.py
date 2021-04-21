# Copyright (c) 2021 Open Risk (https://www.openriskmanagement.com)
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
from django.contrib.gis.db.models import PointField, PolygonField
from django.urls import reverse


class Marker(models.Model):
    """A point marker with name and location (to create elementary geospatial reference)."""

    name = models.CharField(max_length=255)
    location = PointField()

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:Marker_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "PointMarker"
        verbose_name_plural = "PointMarkers"


class ProjectRegion(models.Model):
    """A polygon geometry demarcating the area of a Project."""

    name = models.CharField(max_length=255)
    location = PolygonField()

    #
    # BOOKKEEPING FIELDS
    #
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:ProjectRegion_edit', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Project Region"
        verbose_name_plural = "Project Regions"


from portfolio.ProjectCompany import ProjectCompany
from portfolio.Revenue import Revenue
from portfolio.Loan import Loan
from portfolio.Stakeholders import Stakeholders
from portfolio.Sponsor import Sponsor
from portfolio.Asset import Asset
from portfolio.Contractor import Contractor
from portfolio.Operator import Operator
from portfolio.Swap import Swap
