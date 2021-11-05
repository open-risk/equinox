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
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from portfolio.models import Marker, ProjectRegion
from portfolio.ProjectCompany import ProjectCompany
from portfolio.Project import Project
from portfolio.ProjectCategory import ProjectCategory
from portfolio.Revenue import Revenue
from portfolio.Loan import Loan
from portfolio.Stakeholders import Stakeholders
from portfolio.Sponsor import Sponsor
from portfolio.Asset import Asset
from portfolio.Contractor import Contractor
from portfolio.Operator import Operator
from portfolio.Swap import Swap


#
# Tree Objects
#

# @admin.register(ProjectCategory)
# class ProjectCategoryAdmin(TreeAdmin):
#     form = movenodeform_factory(ProjectCategory)

class ProjectCategoryAdmin(TreeAdmin):
    view_on_site = False
    list_display = ('name',)
    form = movenodeform_factory(ProjectCategory)

admin.site.register(ProjectCategory, ProjectCategoryAdmin)

# admin.site.register(MyNode, MyAdmin)



#
# Geospatial Objects
#


@admin.register(Asset)
class AssetAdmin(admin.OSMGeoAdmin):
    """Project Asset."""
    view_on_site = False


@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location")
    view_on_site = False


@admin.register(ProjectRegion)
class ProjectRegionAdmin(admin.OSMGeoAdmin):
    """Project Region admin."""

    list_display = ("name", "location")
    view_on_site = False


#
# Regular Objects
#

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Project admin"""
    view_on_site = False


@admin.register(ProjectCompany)
class ProjectCompanyAdmin(admin.ModelAdmin):
    view_on_site = False


@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    view_on_site = False


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    view_on_site = False


@admin.register(Stakeholders)
class StakeholdersAdmin(admin.ModelAdmin):
    view_on_site = False


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    view_on_site = False


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    view_on_site = False


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    view_on_site = False


@admin.register(Swap)
class SwapAdmin(admin.ModelAdmin):
    view_on_site = False
