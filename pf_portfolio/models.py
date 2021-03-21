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


# Create your models here.
class Marker(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    location = PointField()

from pf_portfolio.ProjectCompany import ProjectCompany
from pf_portfolio.Revenue import Revenue
from pf_portfolio.Loan import Loan
from pf_portfolio.Stakeholders import Stakeholders
from pf_portfolio.Sponsor import Sponsor
from pf_portfolio.Asset import Asset
from pf_portfolio.Contractor import Contractor
from pf_portfolio.Operator import Operator
from pf_portfolio.Swap import Swap
