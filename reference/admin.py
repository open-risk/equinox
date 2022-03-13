from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from reference.EmissionFactor import EmissionFactor, BuildingEmissionFactor
from reference.GPCSector import GPCSector

actions = ['export']


@admin.action(description='Export Selected Entries')
def export(self, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response


admin.site.add_action(export)


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
    list_display = ('Emission_factor_name', 'Emission_factor', 'Country', 'EPC_Rating', 'Emission_factor_functional_unit_name', 'PCAF_data_quality_score')
    list_filter = ('Emission_factor_type', 'Country', )
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
