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

# from django.contrib import admin
from django.contrib.gis import admin
from django.core import serializers
from django.http import HttpResponse
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from reference.CPVData import CPVData
from reference.EmissionFactor import EmissionFactor, BuildingEmissionFactor
from reference.EmissionIntensity import ReferenceIntensity
from reference.GPCSector import GPCSector
from reference.NUTS3Data import NUTS3PointData
from reference.IOData import IOMatrix, IOMatrixEntry

actions = ['export2json', 'export2xml']


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


@admin.register(NUTS3PointData)
class NUTS3PointDataAdmin(admin.GISModelAdmin):
    """NUTS3 Point Data admin."""

    search_fields = ['nuts_id', 'nuts_name', 'name_latn']
    list_display = ('nuts_id', 'nuts_name', 'cntr_code', 'mount_type', 'urbn_type', 'coast_type')
    list_filter = ('cntr_code',)
    view_on_site = False
    save_as = True


class BuildingEmissionFactorResource(resources.ModelResource):
    class Meta:
        model = BuildingEmissionFactor
        exclude = ('creation_date', 'last_change_date')
        # TODO fix choice fields
        # Emission_factor_type = fields.Field(attribute='get_Emission_factor_type_display')
        # Emission_factor_year_1 = fields.Field(attribute='get_Emission_factor_year_1_display')
        # Emission_factor_year_2 = fields.Field(attribute='get_Emission_factor_year_2_display')
        # Emission_factor_year_3 = fields.Field(attribute='get_Emission_factor_year_3_display')
        # Emission_factor_year_4 = fields.Field(attribute='get_Emission_factor_year_4_display')


@admin.register(BuildingEmissionFactor)
class BuildingEmissionFactorAdmin(ImportExportModelAdmin):
    search_fields = ['Emission_factor_methodology_description']
    list_display = (
        'Emission_factor_name', 'Emission_factor', 'Country', 'EPC_Rating', 'Emission_factor_functional_unit_name',
        'PCAF_data_quality_score')
    list_filter = ('Emission_factor_type', 'Country',)
    resource_class = BuildingEmissionFactorResource
    view_on_site = False
    save_as = True
    date_hierarchy = ('creation_date')


# @admin.register(BuildingEmissionFactor)
# class BuildingEmissionFactorAdmin(admin.ModelAdmin):
#     view_on_site = False
#     save_as = True
#     date_hierarchy = ('creation_date')


@admin.register(EmissionFactor)
class EmissionFactorAdmin(admin.ModelAdmin):
    """Emission Factor admin"""
    view_on_site = False
    search_fields = ['Description', 'Gases', 'Fuel', 'Technology_Practices', 'Regional_Conditions', 'IPCC_Category']
    list_display = (
        'EF_ID', 'IPCC_Category', 'Gases', 'Fuel', 'Value', 'Unit', 'Parameter_Type', 'Description', 'Data_Source')
    list_filter = ('Parameter_Type',)
    save_as = True

    fieldsets = (
        ('Identification', {
            'fields': ('EF_ID', 'IPCC_Category', 'Gases', 'Fuel', 'Parameter_Type', 'Description')
        }),
        ('Practices/Conditions', {
            'fields': ('Technology_Practices', 'Parameter_Conditions', 'Regional_Conditions', 'Control_Technologies',
                       'Other_Properties'),
        }),
        ('Quantitative', {
            'fields': ('Value', 'Unit', 'Lower_Bound', 'Upper_Bound', 'Equation', 'Data_Quality'),
        }),
        ('Reference', {
            'fields': (
                'Data_Source', 'Technical_Reference', 'Data_Quality_Reference', 'Data_Provider', 'Link'),
        }),
        ('Other', {
            'fields': (
                'IPCC_Worksheet', 'English_Abstract', 'Other_Data_Quality', 'Data_Provider_Comments', 'Other_Comments'),
        }),
    )


class GPCSectorAdmin(TreeAdmin):
    view_on_site = False
    list_display = ('name',)
    save_as = True
    # date_hierarchy = ('creation_date')

    form = movenodeform_factory(GPCSector)


admin.site.register(GPCSector, GPCSectorAdmin)


@admin.register(CPVData)
class CPVDataAdmin(admin.ModelAdmin):
    search_fields = ['description']
    list_display = ('CPV_ID', 'short_code', 'level', 'description')
    list_filter = ('level',)
    view_on_site = False
    save_as = True


@admin.register(ReferenceIntensity)
class ReferenceIntensityAdmin(admin.ModelAdmin):
    search_fields = ['Sector']
    list_display = ('Sector', 'Region', 'Gases', 'Value', 'Unit')
    list_filter = ('Region',)
    view_on_site = False
    save_as = True


@admin.register(IOMatrix)
class IOMatrixAdmin(admin.ModelAdmin):
    search_fields = ['io_family']
    list_display = ('io_family', 'io_year', 'io_part', 'nrows', 'ncols')
    list_filter = ('io_family', 'io_year', 'io_part', 'nrows', 'ncols')
    view_on_site = False
    save_as = True


@admin.register(IOMatrixEntry)
class IOMatrixEntryAdmin(admin.ModelAdmin):

    # def get_readonly_fields(self, request, obj=None):
    #     return ('__all__',)

    search_fields = ['row_lbl', 'col_lbl']
    list_display = ('row_lbl', 'col_lbl', 'value')
    view_on_site = False
    save_as = False
