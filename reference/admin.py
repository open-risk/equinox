from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from reference.EmissionFactor import EmissionFactor
from reference.GPCSector import GPCSector

actions = ['export']


@admin.action(description='Export Selected Entries')
def export(self, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response


admin.site.add_action(export)


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
