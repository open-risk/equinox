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


from django.contrib.gis import admin

from portfolio.models import Marker, ProjectRegion
from portfolio.ProjectCompany import ProjectCompany
from portfolio.Revenue import Revenue
from portfolio.Loan import Loan
from portfolio.Stakeholders import Stakeholders
from portfolio.Sponsor import Sponsor
from portfolio.Asset import Asset
from portfolio.Contractor import Contractor
from portfolio.Operator import Operator
from portfolio.Swap import Swap


@admin.register(Asset)
class AssetAdmin(admin.OSMGeoAdmin):
    """Project Asset."""
    pass


@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location")


@admin.register(ProjectRegion)
class ProjectRegionAdmin(admin.OSMGeoAdmin):
    """Project Region admin."""

    list_display = ("name", "location")


@admin.register(ProjectCompany)
class ProjectCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    pass


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass


@admin.register(Stakeholders)
class StakeholdersAdmin(admin.ModelAdmin):
    pass


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    pass


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    pass


@admin.register(Swap)
class SwapAdmin(admin.ModelAdmin):
    pass
