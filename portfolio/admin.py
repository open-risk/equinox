# Copyright (c) 2020 - 2023 Open Risk (https://www.openriskmanagement.com)
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
from django.core import serializers
from django.forms.widgets import NumberInput
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from portfolio.Asset import ProjectAsset, Building
from portfolio.Borrower import Borrower
from portfolio.Contractor import Contractor
from portfolio.Counterparty import Counterparty
from portfolio.EmissionsSource import EmissionsSource, BuildingEmissionsSource
from portfolio.EmissionsSource import GPCEmissionsSource, GPPEmissionsSource
from portfolio.Loan import Loan
from portfolio.Mortgage import Mortgage
from portfolio.Operator import Operator
from portfolio.PortfolioManager import PortfolioManager
from portfolio.Portfolios import PortfolioSnapshot, LimitStructure
from portfolio.Portfolios import ProjectPortfolio, PortfolioTable
from portfolio.PrimaryEffect import PrimaryEffect
from portfolio.Project import Project
from portfolio.ProjectActivity import ProjectActivity
from portfolio.ProjectCategory import ProjectCategory
from portfolio.ProjectCompany import ProjectCompany
from portfolio.ProjectEvent import ProjectEvent
from portfolio.Revenue import Revenue
from portfolio.SecondaryEffect import SecondaryEffect
from portfolio.Sponsor import Sponsor
from portfolio.Stakeholders import Stakeholders
from portfolio.Swap import Swap
from portfolio.Certificate import Certificate
from portfolio.Asset import PowerPlant
from portfolio.models import PointSource, AreaSource, MultiAreaSource


@admin.action(description='Export Selected Entries as JSON')
def export2json(self, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response


@admin.action(description='Export Selected Entries as XML')
def export2xml(self, request, queryset):
    response = HttpResponse(content_type="application/xml")
    serializers.serialize("xml", queryset, stream=response)
    return response


admin.site.add_action(export2json)
admin.site.add_action(export2xml)


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

    list_display = ("name",)
    view_on_site = False
    save_as = True
    search_fields = ['name']
    # list_filter = ('location',)
    date_hierarchy = ('creation_date')


@admin.register(AreaSource)
class AreaSourceAdmin(admin.OSMGeoAdmin):
    """Project Region admin. (Simple Polygon) """

    list_display = ("name",)
    view_on_site = False
    save_as = True
    search_fields = ['name']
    date_hierarchy = ('creation_date')


@admin.register(MultiAreaSource)
class MultiAreaSourceAdmin(admin.OSMGeoAdmin):
    """Project Region admin. (Multi Polygon) """

    list_display = ("name",)
    view_on_site = False
    save_as = True
    search_fields = ['name']
    date_hierarchy = ('creation_date')


#
# Regular Objects
#

@admin.register(ProjectAsset)
class ProjectAssetAdmin(admin.ModelAdmin):
    """Project Asset admin"""
    view_on_site = False
    save_as = True
    search_fields = ['name']
    list_display = ('asset_identifier', 'asset_class', 'asset_ghg_emissions', 'project')
    list_filter = ('asset_class', 'project')

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
            'fields': ('initial_valuation_amount', 'latest_valuation_amount',),
        }),
        ('Other', {
            'classes': ('collapse',),
            'fields': ('activation_of_guarantee',),
        }),
    )


@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(PortfolioManager)
class PortfolioManagerAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    search_fields = ['name_of_manager']
    list_display = ('manager_identifier', 'name_of_manager', 'address', 'town', 'region', 'country', 'website')


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(EmissionsSource)
class EmissionsSourceAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(BuildingEmissionsSource)
class BuildingEmissionsSourceAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(GPCEmissionsSource)
class GPCEmissionsSourceAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    list_display = ('source_identifier', 'gpc_subsector', 'co2_amount')
    date_hierarchy = ('creation_date')


@admin.register(GPPEmissionsSource)
class GPPEmissionsSourceAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    list_filter = ('project__cpa_code',)
    list_display = ('source_identifier', 'link_to_project', 'project__cpa_code', 'project__budget', 'co2_amount')

    def link_to_project(self, obj):
        link = reverse("admin:portfolio_project_change", args=[obj.project.pk])
        return format_html('<a href="{}">{}</a>', link, obj.project.pk)

    link_to_project.short_description = 'Project'

    def project__cpa_code(self, obj):
        return obj.project.cpa_code

    project__cpa_code.short_description = 'CPA Code'

    def project__cpv_code(self, obj):
        return obj.project.cpv_code

    project__cpv_code.short_description = 'CPV Code'

    def project__budget(self, obj):
        return obj.project.project_budget

    project__budget.short_description = 'Budget'


@admin.register(ProjectEvent)
class ProjectEventAdmin(admin.ModelAdmin):
    """Project Event admin"""
    view_on_site = False
    save_as = True
    list_display = ('project_event_identifier', 'project', 'project_event_date', 'project_event_type')
    date_hierarchy = ('project_event_date')


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


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Project admin"""
    view_on_site = False
    save_as = True
    search_fields = ['project_title']
    list_display = (
        'pk', 'project_title', 'cpv_code', 'cpa_code', 'country', 'region', 'project_budget', 'project_currency',
        'project_category')
    list_filter = ('project_category', 'country', 'cpa_code')


@admin.register(ProjectActivity)
class ProjectActivityAdmin(admin.ModelAdmin):
    """Project Activity admin"""

    def link_to_project(self, obj):
        link = reverse("admin:portfolio_project_change", args=[obj.project.pk])
        return format_html('<a href="{}">{}</a>', link, obj.project.pk)

    link_to_project.short_description = 'Project'
    view_on_site = False
    save_as = True
    list_display = ('pk', 'project_activity_title', 'link_to_project', 'region', 'main_site')
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


@admin.register(Mortgage)
class MortgageAdmin(admin.ModelAdmin):
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
    def link_to_project(self, obj):
        link = reverse("admin:portfolio_project_change", args=[obj.project.pk])
        return format_html('<a href="{}">{}</a>', link, obj.project.pk)

    link_to_project.short_description = 'Project'

    view_on_site = False
    save_as = True
    list_display = ('pk', 'name_of_contractor', 'is_sme', 'link_to_project', 'address', 'town', 'region', 'country')
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


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(PowerPlant)
class PowerPlantAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


@admin.register(Counterparty)
class CounterpartyAdmin(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


class PortfolioTableAdminForm(forms.ModelForm):
    """
    EAD, LGD, Tenor constraints

    """
    EAD = forms.fields.FloatField(min_value=0, widget=NumberInput(attrs={'step': 0.01}), label="EAD",
                                  help_text="Exposure at Default")
    LGD = forms.fields.IntegerField(min_value=0, max_value=5, label="LGD", help_text="Loss Given Default Class (0 - 5)")
    Tenor = forms.fields.IntegerField(min_value=1, max_value=10, help_text="Tenor (Maturity) in Integer Years")

    def __init__(self, *args, **kwargs):
        super(PortfolioTableAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PortfolioTable
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


@admin.register(PortfolioSnapshot)
class PortfolioSnapshot(admin.ModelAdmin):
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


class ProjectPortfolioAdmin(admin.ModelAdmin):
    search_fields = ['notes']
    list_display = ('name', 'portfolio_type', 'creation_date', 'notes')
    list_filter = ('portfolio_type',)
    save_as = True
    view_on_site = False
    date_hierarchy = ('creation_date')

    def changelist_view(self, request, extra_context=None):
        extra_context = {
            'message': 'Portfolio Administration: Overview of User Generated Portfolios and their Properties',
        }
        return super(ProjectPortfolioAdmin, self).changelist_view(request, extra_context=extra_context)

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect(reverse("portfolio:ProjectPortfolio_list"))


class PortfolioTableAdmin(admin.ModelAdmin):
    # readonly_fields = ('portfolio_id')
    fields = ('portfolio_id', 'Obligor_ID', 'EAD', 'LGD', 'Tenor', 'Sector', 'Country')
    form = PortfolioTableAdminForm
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
            'message': 'Portfolio Table Data Administration: Overview of User Generated Portfolio Data',
        }
        return super(PortfolioTableAdmin, self).changelist_view(request, extra_context=extra_context)

    # Hack to be able to return to parent portfolio after item delete
    deleted_fk = None

    def delete_view(self, request, object_id, extra_context=None):
        self.deleted_fk = PortfolioTable.objects.get(id=object_id).projectportfolio_id.pk
        return super(PortfolioTableAdmin, self).delete_view(request, object_id, extra_context)

    def response_delete(self, request, obj_display, obj_id):
        return HttpResponseRedirect(reverse("portfolio:ProjectPortfolio_edit", args=[self.deleted_fk]))


admin.site.register(ProjectPortfolio, ProjectPortfolioAdmin)
admin.site.register(PortfolioTable, PortfolioTableAdmin)
admin.site.register(LimitStructure, LimitStructureAdmin)
