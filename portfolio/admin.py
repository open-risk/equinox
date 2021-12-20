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

from django import forms
from django.contrib.gis import admin
from django.forms.widgets import NumberInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from portfolio.Asset import Asset
from portfolio.EmissionsSource import EmissionsSource
from portfolio.Contractor import Contractor
from portfolio.Loan import Loan
from portfolio.Operator import Operator
from portfolio.Portfolios import Portfolio, PortfolioData, LimitStructure
from portfolio.PrimaryEffect import PrimaryEffect
from portfolio.Project import Project
from portfolio.ProjectActivity import ProjectActivity
from portfolio.ProjectCategory import ProjectCategory
from portfolio.ProjectCompany import ProjectCompany
from portfolio.Revenue import Revenue
from portfolio.SecondaryEffect import SecondaryEffect
from portfolio.Sponsor import Sponsor
from portfolio.Stakeholders import Stakeholders
from portfolio.Swap import Swap
from portfolio.models import PointSource, AreaSource


#
# Tree Objects
#


class ProjectCategoryAdmin(TreeAdmin):
    view_on_site = False
    list_display = ('name',)
    form = movenodeform_factory(ProjectCategory)


admin.site.register(ProjectCategory, ProjectCategoryAdmin)


#
# Geospatial Objects (Source Geometries)
#

@admin.register(PointSource)
class PointSourceAdmin(admin.OSMGeoAdmin):
    """Point Source admin."""

    list_display = ("name", "location")
    view_on_site = False
    save_as = True
    search_fields = ['name']
    list_filter = ('location',)
    date_hierarchy = ('creation_date')


@admin.register(AreaSource)
class AreaSourceAdmin(admin.OSMGeoAdmin):
    """Project Region admin."""

    list_display = ("name", "location")
    view_on_site = False
    save_as = True
    search_fields = ['name']
    list_filter = ('location',)
    date_hierarchy = ('creation_date')


#
# Regular Objects
#

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    """Project Asset admin"""
    view_on_site = False
    save_as = True
    search_fields = ['name']
    list_filter = ('asset_class', 'project')
    date_hierarchy = ('creation_date')

    fieldsets = (
        ('Identification', {
            'fields': ('asset_identifier', 'description', 'asset_class')
        }),
        ('Relations', {
            'fields': ('project', 'legal_owner'),
        }),
        ('GHG Emissions', {
            'fields': ('asset_ghg_emissions',),
        }),
        ('Financial', {
            'fields': ('latest_valuation_amount',),
        }),
        ('Other', {
            'classes': ('collapse',),
            'fields': ('activation_of_guarantee',),
        }),
    )


@admin.register(EmissionsSource)
class EmissionsSourceAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Project admin"""
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(PrimaryEffect)
class PrimaryEffectAdmin(admin.ModelAdmin):
    """Primary Effect admin"""
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(SecondaryEffect)
class SecondaryEffectAdmin(admin.ModelAdmin):
    """Secondary Effect admin"""
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(ProjectActivity)
class ProjectActivityAdmin(admin.ModelAdmin):
    """Project Activity admin"""
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(ProjectCompany)
class ProjectCompanyAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(Stakeholders)
class StakeholdersAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(Swap)
class SwapAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


class PortfolioDataAdminForm(forms.ModelForm):
    EAD = forms.fields.FloatField(min_value=0, widget=NumberInput(attrs={'step': 0.01}), label="EAD",
                                  help_text="Exposure at Default")
    LGD = forms.fields.IntegerField(min_value=0, max_value=5, label="LGD", help_text="Loss Given Default Class (0 - 5)")
    Tenor = forms.fields.IntegerField(min_value=1, max_value=10, help_text="Tenor (Maturity) in Integer Years")

    def __init__(self, *args, **kwargs):
        super(PortfolioDataAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PortfolioData
        fields = '__all__'
        # exclude = ('portfolio_id', 'Obligor_ID')
        # widgets = {
        #     'Obligor_ID': TextInput(attrs={'disabled': True}),
        # }


class LimitStructureAdmin(admin.ModelAdmin):
    search_fields = ['notes']
    list_display = ('name', 'creation_date', 'notes')
    save_as = True
    view_on_site = False
    date_hierarchy = ('creation_date')

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            'message': 'LimitStructure Administration: Overview of User Generated Limit Structures and their Properties',
        }
        return super(LimitStructureAdmin, self).changelist_view(request, extra_context=extra_context)


class PortfolioAdmin(admin.ModelAdmin):
    search_fields = ['notes']
    list_display = ('name', 'portfolio_type', 'generation', 'creation_date', 'notes')
    list_filter = ('portfolio_type', 'generation')
    save_as = True
    view_on_site = False
    date_hierarchy = ('creation_date')

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            'message': 'Portfolio Administration: Overview of User Generated Portfolios and their Properties',
        }
        return super(PortfolioAdmin, self).changelist_view(request, extra_context=extra_context)

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect(reverse("portfolio_explorer:portfolio_list"))


class PortfolioDataAdmin(admin.ModelAdmin):
    # readonly_fields = ('portfolio_id')
    fields = ('portfolio_id', 'Obligor_ID', 'EAD', 'LGD', 'Tenor', 'Sector', 'Country')
    form = PortfolioDataAdminForm
    list_display = ('Obligor_ID', 'EAD', 'LGD', 'Tenor', 'Sector', 'Country')
    list_filter = ('portfolio_id',)
    save_as = True
    view_on_site = False
    date_hierarchy = ('creation_date')

    def response_change(self, request, obj, post_url_continue=None):
        """This makes the response after adding go to another apps changelist for some model"""
        return HttpResponseRedirect(reverse("portfolio_explorer:portfolio_view", args=[obj.portfolio_id.pk]))

    # def response_delete(self, request, obj, post_url_continue=None):
    #     return HttpResponseRedirect(reverse("portfolio_view", args=[obj.portfolio_id.pk]))

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            'message': 'Portfolio Data Administration: Overview of User Generated Portfolio Data',
        }
        return super(PortfolioDataAdmin, self).changelist_view(request, extra_context=extra_context)

    # Hack to be able to return to parent portfolio after item delete
    deleted_fk = None

    def delete_view(self, request, object_id, extra_context=None):
        self.deleted_fk = PortfolioData.objects.get(id=object_id).portfolio_id.pk
        return super(PortfolioDataAdmin, self).delete_view(request, object_id, extra_context)

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect(reverse("portfolio_explorer:portfolio_view", args=[self.deleted_fk]))


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioData, PortfolioDataAdmin)
admin.site.register(LimitStructure, LimitStructureAdmin)
